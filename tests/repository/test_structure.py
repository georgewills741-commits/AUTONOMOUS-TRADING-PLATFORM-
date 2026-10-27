"""Repository structure tests, read from the source with `ast` (the Stage 1 plan, section 8).

- Amounts are built only in `atp.numeric` (ARCH-010, TEC-003; the numerical policy, N1 to N3,
  N7): outside it, no `Decimal(...)` call, no `Decimal` handed on as a converter or bound to
  another name, no star import from `decimal`, no call of a value's own type, and no use of the
  decimal context (reached through `decimal`), and `Decimal` reached through any module counts
  (`fractions.Decimal` is the same class). `Decimal`, or `Annotated[Decimal, ...]`, which stands
  for it, is a type use only in an annotation, a `type` statement, a type check, `cast` or
  `NewType`, or a type variable's bound (`Kind = Annotated[Decimal, ...]` could be called;
  `type Kind = ...` cannot); inside another type (`dict[str, Decimal]`, `Decimal | None`) it
  is a type use anywhere. Anywhere in
  `src/`: no `Decimal.from_float` or `create_decimal_from_float`; no TOML read without
  `parse_float`, no JSON read without `parse_float` and `parse_constant`, and no
  `ast.literal_eval`; no amount built from a value's text (`str()`, `repr()`, `format()`, an
  f-string, `.format()`, `json.dumps()`, or `%` formatting inside `amount()`).
- No silent rounding or conversion to float (N4): no `round()`, `to_integral`,
  `to_integral_value`, rounding dunders, `__float__`, or `__int__`; no `math`, `cmath`, or
  `statistics`; no `float` or `complex` called or handed on as a converter; no integer
  division, remainder, or `divmod` (also a decimal context's `divide_int`) outside the modules
  in `INTEGER_DIVISION_ALLOWED` (only `atp.numeric._rounding`). Only the modules in
  `FLOAT_ALLOWED` are exempt; none is.
- Outside `atp.contracts`, Pydantic is used only through the names in `PYDANTIC_ALLOWED`: no
  model that is not a contract, no Pydantic dataclass, `create_model`, `validate_call`,
  `TypeAdapter`, or `pydantic_core` (N2; the contract conventions).
- Imports between the platform's modules point one way: `atp.numeric` imports no other platform
  module; `atp.contracts` imports only `atp.numeric`. A new module needs its entry here. No
  module imports another package's private modules or names (`atp.<package>._<name>`, or
  `from atp.<package> import _<name>`). A name imported from the package root is the package
  it names (`from atp import contracts`), and so is an attribute path on the root
  (`atp.contracts.Outcome` after `import atp`).
- An outcome's private members are read only inside `atp.contracts` (ARCH-042).
- Outside `atp.contracts`, input is validated only with a contract's `from_python` or
  `from_json`, which raise errors with redacted details; Pydantic's methods that validate
  without that redaction, or skip validation, are not called there (TEC-004, SEC-005).

Each scanner is also run on planted samples in a temporary copy, so a scanner that stopped
finding anything would fail.
"""

from __future__ import annotations

import ast
import shutil
from collections.abc import Iterator
from pathlib import Path

import pytest

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
TESTS_ROOT = REPOSITORY_ROOT / "tests"

# Which platform modules each module may import (besides itself).
ALLOWED_IMPORTS: dict[str, frozenset[str]] = {
    "numeric": frozenset(),
    "contracts": frozenset({"numeric"}),
    "config": frozenset({"contracts", "numeric"}),
    "cli": frozenset({"config"}),
}

FLOAT_CONVERSIONS = frozenset({"from_float", "create_decimal_from_float"})
# The decimal module's context functions and objects, found when reached through `decimal`
# (a `contextvars.Context`, or a class of the platform's own called `Context`, is not one).
MODULE_CONTEXT_NAMES = frozenset(
    {
        "localcontext",
        "setcontext",
        "getcontext",
        "DefaultContext",
        "BasicContext",
        "ExtendedContext",
        "Context",
    }
)
# Attributes of a decimal context, distinctive enough to find on any object.
CONTEXT_ATTRIBUTES = frozenset({"create_decimal", "traps"})
SILENT_ROUNDING = frozenset(
    {
        "to_integral",
        "to_integral_value",
        "__round__",
        "__floor__",
        "__ceil__",
        "__trunc__",
        "__float__",
        "__int__",
        "__floordiv__",
        "__rfloordiv__",
        "__mod__",
        "__rmod__",
        "__divmod__",
        "__rdivmod__",
        "remainder_near",
    }
)
# The operator module's names for integer division and remainder, also its dunder ones.
OPERATOR_DIVISION = frozenset(
    {
        "floordiv",
        "ifloordiv",
        "mod",
        "imod",
        "__floordiv__",
        "__ifloordiv__",
        "__mod__",
        "__imod__",
    }
)
# A decimal context's integer division, on any object (outside atp.numeric the context
# itself is a finding), and `divmod` reached as an attribute (`builtins.divmod`).
DIVISION_METHODS = frozenset({"divide_int", "divmod"})
# Modules that compute in floats or round without signalling (math.floor, math.isclose,
# statistics.fmean, ...): not imported at all.
FLOAT_MODULES = frozenset({"math", "cmath", "statistics"})
# Integer division and remainder truncate toward zero on a Decimal without signalling; the one
# module that implements rounding uses `divmod` exactly (N4). A module that divides only
# integers (timestamps, counts) gets its entry here by a reviewed change (numerical policy, N4).
INTEGER_DIVISION_ALLOWED = frozenset({"atp.numeric._rounding"})
FLOAT_CONVERTERS = frozenset({"float", "complex"})
# Modules allowed to use floats and float rounding (TEC-003: indicators, signals, research).
# A module that needs it gets its entry here deliberately; none does in Stage 1.
FLOAT_ALLOWED: frozenset[str] = frozenset()
TEXT_OF_A_VALUE = frozenset({"str", "repr", "format", "ascii"})
AMOUNT_BUILDERS = frozenset({"amount", "amount_from_toml"})
PYDANTIC_MODELS = frozenset({"BaseModel", "RootModel"})
PYDANTIC_VALIDATORS = frozenset({"validate_call", "TypeAdapter", "create_model"})
# What a module outside atp.contracts may import from Pydantic, to declare a contract's fields
# (`ValidationInfo` types a cross-field check's argument; `ValidationError` is what building a
# contract in code raises).
PYDANTIC_ALLOWED = frozenset(
    {"Field", "AfterValidator", "field_validator", "ValidationInfo", "ValidationError"}
)
# Methods that write a value as text, on any object (`json.dumps(x)`, `x.__str__()`,
# `locale.str(x)`, which also rounds a float to 12 digits).
TEXT_METHODS = frozenset(
    {
        "format",
        "dumps",
        "__str__",
        "__repr__",
        "__format__",
        "str",
        "format_string",
        "currency",
    }
)
# Built-in functions that round or convert, refused when imported from `builtins` by name.
ROUNDING_BUILTINS = frozenset({"round", "divmod", "float", "complex"})
RAW_VALIDATION = frozenset(
    {
        "__pydantic_validator__",
        "validate_assignment",
        "model_validate",
        "model_validate_json",
        "model_validate_strings",
        "model_construct",
        "model_copy",
        "validate_python",
        "validate_json",
        "validate_strings",
        "construct",
        "parse_obj",
        "parse_raw",
        "parse_file",
        "from_orm",
    }
)


def _python_files(root: Path) -> Iterator[Path]:
    yield from sorted(path for path in root.rglob("*.py") if path.is_file())


def _parse(path: Path) -> ast.Module:
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _module_of(path: Path, source_root: Path) -> str:
    parts = path.relative_to(source_root).with_suffix("").parts
    return ".".join(parts[:-1] if parts[-1] == "__init__" else parts)


def _parents(tree: ast.Module) -> dict[ast.AST, ast.AST]:
    return {
        child: node for node in ast.walk(tree) for child in ast.iter_child_nodes(node)
    }


def _typing_names(tree: ast.Module, name: str) -> set[str]:
    """Local names for a typing construct: its own name, and any name it is imported as, from
    any module (`from typing import Annotated as A`)."""
    return {name} | {
        alias.asname
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
        if alias.name == name and alias.asname
    }


def _subscript_of(subscript: ast.Subscript, names: set[str]) -> bool:
    """Whether a subscript's value is one of the names, or an attribute of that name."""
    value = subscript.value
    return (isinstance(value, ast.Name) and value.id in names) or (
        isinstance(value, ast.Attribute) and value.attr in names
    )


def _import_functions(tree: ast.Module) -> set[str]:
    """Names that import a module named by a string: `import_module`, under any name it is
    imported as, and `__import__`."""
    return {"import_module", "__import__"} | _imported_names(
        tree, "importlib", "import_module"
    )


def _type_use_only(
    node: ast.AST,
    parents: dict[ast.AST, ast.AST],
    annotated: set[str],
    unions: set[str],
) -> bool:
    """Whether a reference to a type is only a type hint or a type check, not a use as a value.

    The reference stands for the type itself, and so does an `Annotated[...]` around it
    (calling or subclassing `Annotated[Decimal, ...]` calls or subclasses `Decimal`), or a
    `Union[...]` with one member (which is that member). Where it
    stands for the type, it is a type use only as: either side of an `is` or `is not`
    comparison; a `case Decimal()` pattern; an annotation; the value of a `type` statement; the
    class argument of `isinstance` or `issubclass`, also in a tuple; the type argument of
    `cast` or `NewType`; or a type variable's bound or constraint. Anywhere else it is a value:
    called, subclassed, handed on, or assigned to a name that could then be called
    (`Kind = Annotated[Decimal, ...]`; a `type` statement makes an alias that cannot be). A
    type argument of another subscript (`dict[str, Decimal]`, `tuple[Decimal, ...]`) and a
    member of a `|` union (`Decimal | None`) make a different type, which builds no `Decimal`,
    so they are type uses wherever they are; `Annotated`'s metadata is a value. A call is
    never a type use (`Annotated[Decimal, Field(gt=Decimal("0"))]` builds an amount): the climb
    stops at it.
    """
    path: list[ast.AST] = [node]
    child = node
    while (parent := parents.get(child)) is not None:
        if (
            (isinstance(parent, ast.arg) and parent.annotation is child)
            or (
                isinstance(parent, ast.FunctionDef | ast.AsyncFunctionDef)
                and parent.returns is child
            )
            or (isinstance(parent, ast.AnnAssign) and parent.annotation is child)
            or (isinstance(parent, ast.TypeAlias) and parent.value is child)
            or (isinstance(parent, ast.TypeVar) and parent.bound is child)
            or (isinstance(parent, ast.MatchClass) and parent.cls is child)
            or (
                isinstance(parent, ast.Compare)
                and all(isinstance(op, ast.Is | ast.IsNot) for op in parent.ops)
            )
            or (isinstance(parent, ast.BinOp) and isinstance(parent.op, ast.BitOr))
        ):
            return True
        if isinstance(parent, ast.Call):
            name = _called_name(parent)
            return (
                (name == "cast" and parent.args[:1] == [child])
                or (name == "NewType" and parent.args[1:2] == [child])
                or (
                    name in {"isinstance", "issubclass", "TypeVar"}
                    and child in parent.args[1:]
                )
            )
        if isinstance(parent, ast.keyword):
            call = parents.get(parent)
            return (
                parent.arg == "bound"
                and isinstance(call, ast.Call)
                and _called_name(call) == "TypeVar"
            )
        if isinstance(parent, ast.Subscript) and parent.slice is child:
            arguments = child.elts if isinstance(child, ast.Tuple) else [child]
            if _subscript_of(parent, annotated):
                stands_for = arguments[:1]  # `Annotated[T, ...]` is T
            elif _subscript_of(parent, unions) and not isinstance(child, ast.Tuple):
                stands_for = arguments  # a one-member `Union[T]` is T
            else:
                return True  # a type argument of another type
            if not any(argument in path for argument in stands_for):
                return False  # `Annotated`'s metadata
            # It stands for the type it names: see where it is used.
        elif not isinstance(parent, ast.Tuple | ast.List):
            return False
        path.append(parent)
        child = parent
    return False


def _used_as_converter(node: ast.AST, parents: dict[ast.AST, ast.AST]) -> bool:
    """Whether a name is called, or handed on where it could be called: as an argument (not a
    type check's), a keyword, a default, a returned or assigned value, or a dictionary value."""
    parent = parents.get(node)
    if isinstance(parent, ast.Call):
        if parent.func is node:
            return True
        checks_type = isinstance(parent.func, ast.Name) and parent.func.id in {
            "isinstance",
            "issubclass",
        }
        return not checks_type and node in parent.args
    return (
        isinstance(parent, ast.keyword | ast.Return | ast.Lambda)
        or (
            isinstance(parent, ast.arguments)
            and node in parent.defaults + parent.kw_defaults
        )
        or (
            isinstance(parent, ast.Assign | ast.AnnAssign | ast.NamedExpr)
            and parent.value is node
        )
        or (isinstance(parent, ast.Dict) and node in parent.values)
    )


def _imported_names(tree: ast.Module, module: str, wanted: str) -> set[str]:
    """Local names bound to `module.wanted` (`from module import wanted [as x]`)."""
    return {
        alias.asname or alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module == module
        for alias in node.names
        if alias.name == wanted
    }


def _module_names(tree: ast.Module, module: str) -> set[str]:
    """Local names bound to the module itself (`import module [as x]`)."""
    return {
        alias.asname or alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name == module
    }


def _reads_floats_as_amounts(node: ast.Call, wanted: tuple[str, ...]) -> bool:
    """Whether a TOML or JSON read names each reader in `wanted` as something other than None,
    the default that makes floats: `parse_float`, and for JSON `parse_constant` too, which
    reads `NaN`, `Infinity`, and `-Infinity` (`parse_float` never sees them)."""
    return all(
        any(
            keyword.arg == reader
            and not (
                isinstance(keyword.value, ast.Constant) and keyword.value.value is None
            )
            for keyword in node.keywords
        )
        for reader in wanted
    )


def _called_name(node: ast.Call) -> str | None:
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return None


def _is_text_of_a_value(node: ast.AST) -> bool:
    """Whether an expression turns a value into text: `str(x)`, `repr(x)`, `format(x)`, an
    f-string with a replacement field, `'...'.format(x)`, `json.dumps(x)`, `x.__str__()`, or
    `'...' % x`."""
    return (
        (
            isinstance(node, ast.Call)
            and (
                (isinstance(node.func, ast.Name) and node.func.id in TEXT_OF_A_VALUE)
                or (
                    isinstance(node.func, ast.Attribute)
                    and node.func.attr in TEXT_METHODS
                )
            )
        )
        or (
            isinstance(node, ast.JoinedStr)
            and any(isinstance(part, ast.FormattedValue) for part in node.values)
        )
        or (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod))
    )


def decimal_findings(source_root: Path) -> list[str]:
    """Amounts built, or the decimal context touched, outside `atp.numeric`; float conversions.

    Outside `atp.numeric`, any reference to `Decimal` that is not only a type hint or a type
    check is a finding: a call, but also `Decimal` handed on as a converter, stored, returned,
    or bound to another name, whichever module it is reached through (`from fractions import
    Decimal` gives the same class). So are a star import from `decimal`, calling a value's own
    type (`type(x)(…)`, `x.__class__(…)`), and any use of the decimal context. Anywhere in
    `src/`, a conversion from a float, reading TOML without `parse_float` or JSON without
    `parse_float` and `parse_constant`, `ast.literal_eval` (it reads `0.1` as a float), and
    building an amount from a value's text (a float's text holds its binary error) are
    findings.
    """
    findings: list[str] = []
    for path in _python_files(source_root):
        module = _module_of(path, source_root)
        inside_numeric = module == "atp.numeric" or module.startswith("atp.numeric.")
        tree = _parse(path)
        parents = _parents(tree)
        decimal_names = {
            alias.asname or alias.name
            for imported in ast.walk(tree)
            if isinstance(imported, ast.ImportFrom)
            for alias in imported.names
            if alias.name == "Decimal"
        }
        decimal_modules = _module_names(tree, "decimal")
        annotated = _typing_names(tree, "Annotated")
        unions = _typing_names(tree, "Union")
        toml_loaders = _imported_names(tree, "tomllib", "load") | _imported_names(
            tree, "tomllib", "loads"
        )
        toml_modules = _module_names(tree, "tomllib")
        json_loaders = _imported_names(tree, "json", "load") | _imported_names(
            tree, "json", "loads"
        )
        json_modules = _module_names(tree, "json")
        json_decoders = {"JSONDecoder"} | {
            alias.asname
            for imported in ast.walk(tree)
            if isinstance(imported, ast.ImportFrom)
            for alias in imported.names
            if alias.name == "JSONDecoder" and alias.asname
        }
        amount_builders = AMOUNT_BUILDERS | {
            alias.asname
            for imported in ast.walk(tree)
            if isinstance(imported, ast.ImportFrom)
            for alias in imported.names
            if alias.name in AMOUNT_BUILDERS and alias.asname
        }
        for node in ast.walk(tree):
            where = f"{path.relative_to(source_root)}:{getattr(node, 'lineno', 0)}"
            if isinstance(node, ast.Attribute) and node.attr in FLOAT_CONVERSIONS:
                findings.append(f"{where}: float conversion {node.attr}")
            if (
                isinstance(node, ast.Call)
                and (
                    (isinstance(node.func, ast.Name) and node.func.id in toml_loaders)
                    or (
                        isinstance(node.func, ast.Attribute)
                        and node.func.attr in {"load", "loads"}
                        and isinstance(node.func.value, ast.Name)
                        and node.func.value.id in toml_modules
                    )
                )
                and not _reads_floats_as_amounts(node, ("parse_float",))
            ):
                findings.append(f"{where}: TOML read without parse_float")
            if (
                isinstance(node, ast.Call)
                and (
                    (isinstance(node.func, ast.Name) and node.func.id in json_loaders)
                    or (
                        isinstance(node.func, ast.Attribute)
                        and node.func.attr in {"load", "loads"}
                        and isinstance(node.func.value, ast.Name)
                        and node.func.value.id in json_modules
                    )
                    # However it is reached: json.JSONDecoder, json.decoder.JSONDecoder,
                    # or a name it is imported as.
                    or _called_name(node) in json_decoders
                )
                and not _reads_floats_as_amounts(
                    node, ("parse_float", "parse_constant")
                )
            ):
                findings.append(
                    f"{where}: JSON read without parse_float and parse_constant"
                )
            if (
                isinstance(node, ast.Call)
                and _called_name(node) in amount_builders
                and any(
                    _is_text_of_a_value(part)
                    for argument in [
                        *node.args,
                        *(keyword.value for keyword in node.keywords),
                    ]
                    for part in ast.walk(argument)
                )
            ):
                findings.append(f"{where}: an amount built from a value's text")
            if isinstance(node, ast.Call) and _called_name(node) == "literal_eval":
                findings.append(f"{where}: literal_eval reads numbers as floats")
            if inside_numeric:
                continue
            if (
                (isinstance(node, ast.Name) and node.id in decimal_names)
                or (isinstance(node, ast.Attribute) and node.attr == "Decimal")
            ) and not _type_use_only(node, parents, annotated, unions):
                findings.append(f"{where}: Decimal used as a value outside atp.numeric")
            if (
                isinstance(node, ast.ImportFrom)
                and node.module == "decimal"
                and any(alias.name == "*" for alias in node.names)
            ):
                findings.append(f"{where}: star import from decimal")
            if isinstance(node, ast.Call) and (
                (
                    isinstance(node.func, ast.Call)
                    and isinstance(node.func.func, ast.Name)
                    and node.func.func.id == "type"
                )
                or (
                    isinstance(node.func, ast.Attribute)
                    and node.func.attr == "__class__"
                )
            ):
                findings.append(f"{where}: a value's own type called")
            if (
                isinstance(node, ast.Attribute)
                and node.attr in MODULE_CONTEXT_NAMES
                and isinstance(node.value, ast.Name)
                and node.value.id in decimal_modules
            ) or (isinstance(node, ast.Attribute) and node.attr in CONTEXT_ATTRIBUTES):
                findings.append(f"{where}: decimal context used outside atp.numeric")
            if (
                isinstance(node, ast.ImportFrom)
                and node.module == "decimal"
                and any(
                    alias.name in MODULE_CONTEXT_NAMES | CONTEXT_ATTRIBUTES
                    for alias in node.names
                )
            ):
                findings.append(
                    f"{where}: decimal context imported outside atp.numeric"
                )
    return findings


def pydantic_findings(source_root: Path) -> list[str]:
    """Pydantic constructs outside `atp.contracts` that validate without its rules.

    A `BaseModel` or `RootModel` that is not a contract, a Pydantic dataclass, `create_model`,
    `validate_call`, or a `TypeAdapter` would build values, `Decimal` from a float included,
    without the contract kernel's strictness and redaction. Outside `atp.contracts`, Pydantic
    is therefore imported only by name, and only the names in `PYDANTIC_ALLOWED`: no
    `import pydantic`, no import from its submodules, and nothing from `pydantic_core`.
    """
    findings: list[str] = []
    for path in _python_files(source_root):
        module = _module_of(path, source_root)
        if module == "atp.contracts" or module.startswith("atp.contracts."):
            continue
        tree = _parse(path)
        import_functions = _import_functions(tree)
        for node in ast.walk(tree):
            where = f"{path.relative_to(source_root)}:{getattr(node, 'lineno', 0)}"
            if (
                isinstance(node, ast.Call)
                and _called_name(node) in import_functions
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)
                and node.args[0].value.split(".")[0] in {"pydantic", "pydantic_core"}
            ):
                findings.append(f"{where}: {node.args[0].value} imported by name")
            if isinstance(node, ast.ClassDef):
                for listed in node.bases:
                    base = listed.value if isinstance(listed, ast.Subscript) else listed
                    base_name = (
                        base.id
                        if isinstance(base, ast.Name)
                        else base.attr
                        if isinstance(base, ast.Attribute)
                        else None
                    )
                    if base_name in PYDANTIC_MODELS:
                        findings.append(
                            f"{where}: a Pydantic model that is not a contract"
                        )
            name = (
                node.attr
                if isinstance(node, ast.Attribute)
                else node.id
                if isinstance(node, ast.Name)
                else node.name
                if isinstance(node, ast.alias)
                else None
            )
            if name in PYDANTIC_VALIDATORS:
                findings.append(f"{where}: Pydantic {name} outside atp.contracts")
            if isinstance(node, ast.Import):
                findings.extend(
                    f"{where}: {alias.name} imported as a module outside atp.contracts"
                    for alias in node.names
                    if alias.name.split(".")[0] in {"pydantic", "pydantic_core"}
                )
            if isinstance(node, ast.ImportFrom) and node.module is not None:
                root = node.module.split(".")[0]
                if root == "pydantic_core" or (
                    root == "pydantic" and node.module != "pydantic"
                ):
                    findings.append(
                        f"{where}: import from {node.module} outside atp.contracts"
                    )
                elif node.module == "pydantic":
                    findings.extend(
                        f"{where}: Pydantic {alias.name} is not in PYDANTIC_ALLOWED"
                        for alias in node.names
                        if alias.name not in PYDANTIC_ALLOWED
                        and alias.name not in PYDANTIC_VALIDATORS
                    )
    return findings


def rounding_findings(source_root: Path) -> list[str]:
    """Silent rounding and conversion to float anywhere in `src/`.

    `round()` (called or referenced), `to_integral`, `to_integral_value`, and the rounding
    dunders round without signalling; `__float__`, `__int__`, and `float` called or handed on
    as a converter, convert (naming `float` in a type hint, a type check, or a tuple of types
    does not). The `math`, `cmath`, and `statistics` modules compute in floats or round, so
    importing them is a finding. Integer division (`//`), remainder (`%`, which is also `%`
    formatting), `divmod` (also as an attribute), their dunders, the `operator` module's
    `floordiv` and `mod` (also their dunder names), and a decimal context's `divide_int`
    truncate toward zero on a `Decimal` without signalling; only `atp.numeric._rounding` uses
    `divmod`, exactly. Only the modules in `FLOAT_ALLOWED` may use floats (TEC-003 allows them
    for indicators, signals, and research); none does in Stage 1.
    """
    findings: list[str] = []
    for path in _python_files(source_root):
        module = _module_of(path, source_root)
        if module in FLOAT_ALLOWED:
            continue
        divides = module not in INTEGER_DIVISION_ALLOWED
        tree = _parse(path)
        parents = _parents(tree)
        operator_modules = _module_names(tree, "operator")
        builtins_modules = _module_names(tree, "builtins")
        operator_names = {
            name
            for wanted in OPERATOR_DIVISION
            for name in _imported_names(tree, "operator", wanted)
        }
        for node in ast.walk(tree):
            where = f"{path.relative_to(source_root)}:{getattr(node, 'lineno', 0)}"
            if (isinstance(node, ast.Name) and node.id == "round") or (
                isinstance(node, ast.Attribute)
                and node.attr == "round"
                and isinstance(node.value, ast.Name)
                and node.value.id in builtins_modules
            ):
                findings.append(f"{where}: round")
            if isinstance(node, ast.ImportFrom) and node.module == "builtins":
                findings.extend(
                    f"{where}: {alias.name} imported from builtins"
                    for alias in node.names
                    if alias.name in ROUNDING_BUILTINS
                )
            if isinstance(node, ast.Attribute) and node.attr in SILENT_ROUNDING:
                findings.append(f"{where}: {node.attr}")
            imported = (
                [alias.name for alias in node.names]
                if isinstance(node, ast.Import)
                else [node.module]
                if isinstance(node, ast.ImportFrom) and node.module
                else []
            )
            findings.extend(
                f"{where}: the float module {name}"
                for name in imported
                if name.split(".")[0] in FLOAT_MODULES
            )
            if divides and (
                (
                    isinstance(node, ast.BinOp | ast.AugAssign)
                    and isinstance(node.op, ast.FloorDiv | ast.Mod)
                )
                or (isinstance(node, ast.Name) and node.id == "divmod")
                or (isinstance(node, ast.Attribute) and node.attr in DIVISION_METHODS)
                or (isinstance(node, ast.Name) and node.id in operator_names)
                or (
                    isinstance(node, ast.Attribute)
                    and node.attr in OPERATOR_DIVISION
                    and isinstance(node.value, ast.Name)
                    and node.value.id in operator_modules
                )
            ):
                findings.append(f"{where}: integer division or remainder")
            if (
                isinstance(node, ast.Name)
                and node.id in FLOAT_CONVERTERS
                and _used_as_converter(node, parents)
            ):
                findings.append(f"{where}: {node.id} used as a converter")
            if (
                isinstance(node, ast.Attribute)
                and node.attr in FLOAT_CONVERTERS
                and isinstance(node.value, ast.Name)
                and node.value.id in builtins_modules
                and _used_as_converter(node, parents)
            ):
                findings.append(f"{where}: builtins.{node.attr} used as a converter")
            if (
                isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name)
                and node.value.id in FLOAT_CONVERTERS
            ):
                # `float.fromhex(...)` builds a float too.
                findings.append(f"{where}: {node.value.id}.{node.attr}")
    return findings


def _imported_modules(
    tree: ast.Module, module: str, is_package: bool
) -> Iterator[tuple[str, tuple[str, ...]]]:
    """Each imported module, with the names imported from it (none for `import module`).

    A name imported from the package root is the package it names (`from atp import contracts`
    and `from .. import contracts` import `atp.contracts`). So is an attribute path on a name
    bound to the root (`import atp` or `import atp.numeric`, then `atp.contracts.Outcome`; the
    root's own dunders, such as `atp.__path__`, are not modules), and a module named by a
    constant in `importlib.import_module` or `__import__`. A module named only at run time (a
    computed or relative name given to `import_module`) is caught in review.
    """
    parents = _parents(tree)
    import_functions = _import_functions(tree)
    root_names = {
        alias.asname or "atp"
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name == "atp" or (alias.name.startswith("atp.") and not alias.asname)
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            yield from ((alias.name, ()) for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names = tuple(alias.name for alias in node.names)
            if node.level:
                package = module if is_package else module.rpartition(".")[0]
                for _ in range(node.level - 1):
                    package = package.rpartition(".")[0]
                imported = f"{package}.{node.module}" if node.module else package
            elif node.module:
                imported = node.module
            else:
                continue
            if imported == "atp":
                yield from ((f"atp.{name}", ()) for name in names)
            else:
                yield imported, names
        elif (
            isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id in root_names
            and not node.attr.startswith("__")
        ):
            path = ["atp", node.attr]
            child: ast.AST = node
            while (
                isinstance(parent := parents.get(child), ast.Attribute)
                and parent.value is child
            ):
                path.append(parent.attr)
                child = parent
            yield ".".join(path), ()
        elif (
            isinstance(node, ast.Call)
            and _called_name(node) in import_functions
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            yield node.args[0].value, ()


def import_findings(source_root: Path) -> list[str]:
    """Imports between platform modules that the allowed directions do not permit."""
    findings: list[str] = []
    for path in _python_files(source_root / "atp"):
        module = _module_of(path, source_root)
        parts = module.split(".")
        if len(parts) < 2:
            owner = None
        else:
            owner = parts[1]
            if owner not in ALLOWED_IMPORTS:
                findings.append(
                    f"{module}: module {owner} has no entry in ALLOWED_IMPORTS"
                )
                continue
        tree = _parse(path)
        for imported, names in _imported_modules(
            tree, module, path.name == "__init__.py"
        ):
            imported_parts = imported.split(".")
            if imported_parts == ["atp"] and owner is not None:
                continue  # `import atp`: what it reaches is checked as attribute paths
            if imported_parts[0] != "atp":
                continue
            target = imported_parts[1] if len(imported_parts) > 1 else None
            if owner is None:
                findings.append(f"{module}: the package root imports {imported}")
            elif target != owner and target not in ALLOWED_IMPORTS[owner]:
                findings.append(f"{module}: imports {imported}")
            elif target != owner and any(
                part.startswith("_") for part in imported_parts[2:]
            ):
                findings.append(f"{module}: imports the private module {imported}")
            elif target != owner and any(name.startswith("_") for name in names):
                # `from atp.numeric import _context` reaches a private module or name too.
                findings.append(f"{module}: imports a private name from {imported}")
    return findings


def private_outcome_findings(
    roots: list[Path], private_names: frozenset[str]
) -> list[str]:
    """Reads of an outcome's private members outside `atp.contracts`."""
    findings: list[str] = []
    for root in roots:
        for path in _python_files(root):
            if "atp/contracts" in path.as_posix():
                continue
            for node in ast.walk(_parse(path)):
                names: list[str] = []
                if isinstance(node, ast.Attribute):
                    names.append(node.attr)
                elif isinstance(node, ast.MatchClass):
                    names.extend(node.kwd_attrs)
                elif (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id in {"getattr", "setattr", "hasattr", "delattr"}
                ):
                    names.extend(
                        argument.value
                        for argument in node.args[1:2]
                        if isinstance(argument, ast.Constant)
                        and isinstance(argument.value, str)
                    )
                findings.extend(
                    f"{path}:{getattr(node, 'lineno', 0)}: {name}"
                    for name in names
                    if name in private_names
                )
    return findings


def raw_validation_findings(source_root: Path) -> list[str]:
    """Calls of Pydantic's methods that validate without redaction, or skip validation, outside
    `atp.contracts` (including the deprecated version 1 names and `copy(update=…)`)."""
    findings: list[str] = []
    for path in _python_files(source_root):
        module = _module_of(path, source_root)
        if module == "atp.contracts" or module.startswith("atp.contracts."):
            continue
        for node in ast.walk(_parse(path)):
            where = f"{path.relative_to(source_root)}:{getattr(node, 'lineno', 0)}"
            if isinstance(node, ast.Attribute) and node.attr in RAW_VALIDATION:
                findings.append(f"{where}: {node.attr}")
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "copy"
                and any(keyword.arg == "update" for keyword in node.keywords)
            ):
                findings.append(f"{where}: copy(update=...)")
    return findings


@pytest.mark.req("ARCH-010", "TEC-003")
def test_amounts_are_built_only_in_atp_numeric() -> None:
    assert decimal_findings(SOURCE_ROOT) == []


@pytest.mark.req("ARCH-010", "TEC-003")
def test_nothing_rounds_outside_the_named_directions() -> None:
    assert rounding_findings(SOURCE_ROOT) == []


@pytest.mark.req("TEC-004")
def test_no_pydantic_validation_outside_the_contract_kernel() -> None:
    assert pydantic_findings(SOURCE_ROOT) == []


@pytest.mark.req("TEC-008")
def test_imports_between_modules_point_one_way() -> None:
    assert import_findings(SOURCE_ROOT) == []


def test_input_is_validated_only_through_the_redacting_methods() -> None:
    assert raw_validation_findings(SOURCE_ROOT) == []


@pytest.mark.req("TEC-008")
def test_every_platform_module_has_an_import_rule() -> None:
    modules = {path.name for path in (SOURCE_ROOT / "atp").iterdir() if path.is_dir()}
    modules.discard("__pycache__")
    assert modules == set(ALLOWED_IMPORTS)


def test_outcome_private_members_are_read_only_inside_contracts() -> None:
    from atp.contracts import Outcome

    private_names = frozenset(Outcome.__slots__)
    assert private_names, "the outcome keeps its kind and value in private slots"
    assert private_outcome_findings([SOURCE_ROOT, TESTS_ROOT], private_names) == []


@pytest.fixture
def bare_source(tmp_path: Path) -> Path:
    """A source tree with only the packages' `__init__` files: a sample planted there is the
    only code the scanners read, so one list entry is tried at a time, quickly."""
    root = tmp_path / "bare"
    for package in ("atp", "atp/numeric", "atp/contracts"):
        (root / package).mkdir(parents=True, exist_ok=True)
        (root / package / "__init__.py").write_text("", encoding="utf-8")
    return root


# One sample per entry of each scanner list, the entries written out here, so removing an entry
# from a list fails a test.
LIST_SAMPLES = [
    *(
        ("rounding", f"def f(x):\n    return x.{name}()\n")
        for name in (
            "to_integral",
            "to_integral_value",
            "__round__",
            "__floor__",
            "__ceil__",
            "__trunc__",
            "__float__",
            "__int__",
            "__floordiv__",
            "__rfloordiv__",
            "__mod__",
            "__rmod__",
            "__divmod__",
            "__rdivmod__",
            "remainder_near",
        )
    ),
    *(
        ("rounding", f"import operator\nf = operator.{name}\n")
        for name in (
            "floordiv",
            "ifloordiv",
            "mod",
            "imod",
            "__floordiv__",
            "__ifloordiv__",
            "__mod__",
            "__imod__",
        )
    ),
    *(
        ("rounding", f"from operator import {name}\nx = {name}(1, 2)\n")
        for name in (
            "floordiv",
            "ifloordiv",
            "mod",
            "imod",
            "__floordiv__",
            "__ifloordiv__",
            "__mod__",
            "__imod__",
        )
    ),
    *(
        ("rounding", f"def f(c, x, y):\n    return c.{name}(x, y)\n")
        for name in ("divide_int", "divmod")
    ),
    *(("rounding", f"import {name}\n") for name in ("math", "cmath", "statistics")),
    *(("rounding", f"x = {name}\n") for name in ("float", "complex")),
    *(
        ("rounding", f"from builtins import {name}\n")
        for name in ("round", "divmod", "float", "complex")
    ),
    *(
        ("decimal", f"import decimal\nx = decimal.{name}\n")
        for name in (
            "localcontext",
            "setcontext",
            "getcontext",
            "DefaultContext",
            "BasicContext",
            "ExtendedContext",
            "Context",
        )
    ),
    *(
        ("decimal", f"def f(c):\n    return c.{name}\n")
        for name in ("create_decimal", "traps")
    ),
    *(
        ("decimal", f"def f(x):\n    return x.{name}(0.5)\n")
        for name in ("from_float", "create_decimal_from_float")
    ),
    *(
        ("decimal", f"from atp.numeric import amount\nx = amount({name}(0.1))\n")
        for name in ("str", "repr", "format", "ascii")
    ),
    *(
        (
            "decimal",
            f"from atp.numeric import amount\ndef f(v):\n    return amount(v.{name}())\n",
        )
        for name in (
            "format",
            "dumps",
            "__str__",
            "__repr__",
            "__format__",
            "str",
            "format_string",
            "currency",
        )
    ),
    *(
        ("decimal", f"from atp.numeric import {name}\nx = {name}(str(0.1))\n")
        for name in ("amount", "amount_from_toml")
    ),
    *(
        ("pydantic", f"from pydantic import {name}\nclass T({name}):\n    pass\n")
        for name in ("BaseModel", "RootModel")
    ),
    *(
        ("pydantic", f"import pydantic\nx = pydantic.{name}\n")
        for name in ("validate_call", "TypeAdapter", "create_model")
    ),
]
# Each scanner, and the package a sample is planted in: amounts may be built in atp.numeric,
# and Pydantic may be used in atp.contracts, so their samples go to the other one.
LIST_SCANNERS = {
    "rounding": (rounding_findings, "numeric"),
    "decimal": (decimal_findings, "contracts"),
    "pydantic": (pydantic_findings, "numeric"),
}


@pytest.mark.parametrize(("scanner", "planted"), LIST_SAMPLES)
def test_every_entry_of_a_scanner_list_is_found(
    bare_source: Path, scanner: str, planted: str
) -> None:
    findings, package = LIST_SCANNERS[scanner]
    (bare_source / "atp" / package / "planted.py").write_text(planted, encoding="utf-8")
    assert findings(bare_source)


@pytest.fixture
def copy_of_source(tmp_path: Path) -> Path:
    destination = tmp_path / "src"
    shutil.copytree(
        SOURCE_ROOT, destination, ignore=shutil.ignore_patterns("__pycache__")
    )
    return destination


@pytest.mark.parametrize(
    "planted",
    [
        "from decimal import Decimal\nx = Decimal.from_float(0.5)\n",
        "import decimal\nx = decimal.getcontext().create_decimal_from_float(0.5)\n",
        "from decimal import Decimal\nx = Decimal('1')\n",
        "from decimal import Decimal as D\nx = D('1')\n",
        "import decimal as d\nx = d.Decimal('1')\n",
        "import json\nfrom decimal import Decimal\nx = json.loads('1', parse_float=Decimal)\n",
        "from decimal import Decimal\nx = list(map(Decimal, ['1']))\n",
        "import decimal\nD = decimal.Decimal\n",
        "import decimal\nwith decimal.localcontext() as c:\n    pass\n",
        "import decimal\ndecimal.getcontext().traps\n",
        "from decimal import setcontext\n",
        "import decimal\nx = decimal.Context(prec=5)\n",
        "from decimal import *\nx = Decimal('1')\n",
        "from decimal import Decimal\nCONVERTERS = {'amount': Decimal}\n",
        "from decimal import Decimal\ndef f(s, convert=Decimal):\n    return convert(s)\n",
        "from decimal import Decimal\ndef f():\n    return Decimal\n",
        "from decimal import Decimal\nx = [Decimal]\n",
        "from decimal import Decimal\nif (D := Decimal):\n    pass\n",
        "def f(x):\n    return type(x)('0.1')\n",
        "def f(x):\n    return x.__class__('0.1')\n",
        "import tomllib\nx = tomllib.loads('a = 1')\n",
        "from tomllib import loads\nx = loads('a = 1')\n",
        "from tomllib import load\ndef f(stream):\n    return load(stream)\n",
        "from decimal import Decimal\nconvert = lambda: Decimal\n",
        "from decimal import Decimal\ndef f(t):\n    return t == Decimal\n",
        "import json\nx = json.loads('1.5', parse_float=None)\n",
        "import json\nfrom atp.numeric import amount\nx = amount(json.dumps(0.1))\n",
        "from atp.numeric import amount\nx = amount((0.1).__str__())\n",
        "from fractions import Decimal\nx = Decimal('0.1')\n",
        "import fractions\nx = fractions.Decimal('0.1')\n",
        (
            "from decimal import Decimal\nfrom typing import Annotated\n"
            "from pydantic import Field\n"
            "Price = Annotated[Decimal, Field(gt=Decimal('0'))]\n"
        ),
        "from decimal import Decimal\nx = {'a': 1}[Decimal('1')]\n",
        "import ast\nx = ast.literal_eval('0.1')\n",
        "from decimal import Decimal\nx = {}[list(map(Decimal, ['1']))]\n",
        "def f(context):\n    context.traps.clear()\n",
        "from ast import literal_eval\nx = literal_eval('[0.1]')\n",
        "import json\nx = json.loads('1.5')\n",
        "import json\ndef f(stream):\n    return json.load(stream)\n",
        "from json import loads\nx = loads('1.5')\n",
        "import json\ndecoder = json.JSONDecoder()\n",
        "import json.decoder\ndecoder = json.decoder.JSONDecoder()\n",
        "from json.decoder import JSONDecoder\ndecoder = JSONDecoder()\n",
        "from atp.numeric import amount as to_amount\nx = to_amount(str(0.1))\n",
        "from atp.numeric import amount\nx = amount(value=str(0.1))\n",
        "from atp.numeric import amount\nx = amount(str(0.1).strip())\n",
        "from atp.numeric import amount\nx = amount(str(1 / 3))\n",
        "from atp.numeric import amount\nx = amount(repr(0.1))\n",
        "from atp.numeric import amount\nx = amount(format(0.1))\n",
        "from atp.numeric import amount\nx = amount(ascii(0.1))\n",
        "from atp.numeric import amount\ny = 0.1\nx = amount(f'{y}')\n",
        "from atp.numeric import amount\nx = amount('{}'.format(0.1))\n",
        "from atp.numeric import amount\nx = amount('%s' % 0.1)\n",
        "import atp.numeric\nx = atp.numeric.amount(str(0.1))\n",
        "from atp.numeric import amount_from_toml\nx = amount_from_toml(str(0.1))\n",
        (
            "from decimal import Decimal\nfrom typing import Annotated\n"
            "x = Annotated[Decimal, 'm']('NaN')\n"
        ),
        "from decimal import Decimal\nfrom typing import Annotated\nKind = Annotated[Decimal, 'm']\n",
        (
            "from decimal import Decimal\nfrom typing import Annotated\n"
            "class Money(Annotated[Decimal, 'm']):\n    pass\n"
        ),
        "from decimal import Decimal\nfrom typing import TypeAlias\nPrice: TypeAlias = Decimal\n",
        (
            "from decimal import Decimal\nfrom typing import Annotated as A\n"
            "x = A[Decimal, 'm']('NaN')\n"
        ),
        "from decimal import Decimal\nimport typing\nx = typing.Annotated[Decimal, 'm']('1')\n",
        "from decimal import Decimal\nfrom typing import Annotated\nx: Annotated[int, Decimal] = 1\n",
        "import json\nfrom atp.numeric import amount\nx = json.loads('1', parse_float=amount)\n",
        (
            "import json\nfrom atp.numeric import amount\n"
            "x = json.loads('1', parse_float=amount, parse_constant=None)\n"
        ),
        "from json import JSONDecoder as Reader\ndecoder = Reader()\n",
        "from decimal import Decimal\nfrom typing import Union\nx = Union[Decimal]('NaN')\n",
        "from decimal import Decimal\nimport typing\nx = typing.Union[Decimal]('1')\n",
        "from atp.numeric import amount\nimport locale\nx = amount(locale.str(0.1))\n",
    ],
)
def test_the_decimal_scanner_finds_planted_samples(
    copy_of_source: Path, planted: str
) -> None:
    (copy_of_source / "atp" / "contracts" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert decimal_findings(copy_of_source)


def test_a_decimal_type_check_is_not_a_finding(copy_of_source: Path) -> None:
    planted = (
        "import tomllib\n"
        "import json\n"
        "from decimal import Decimal\n"
        "from typing import Annotated\n"
        "from atp.numeric import amount, amount_from_toml\n"
        "type Kind = Annotated[Decimal, 'metadata']\n"
        "value: Decimal | None = None\n"
        "def f(x: Decimal) -> bool:\n"
        "    return isinstance(x, (Decimal, int)) or type(x) is Decimal\n"
        "document = tomllib.loads('a = 1', parse_float=amount_from_toml)\n"
        "message = json.loads('{}', parse_float=amount, parse_constant=amount)\n"
        "price = amount('1.5')\n"
        "text = json.dumps({'price': str(price)})\n"
        "from contextvars import Context\n"
        "from typing import TypeVar, cast\n"
        "type Prices = dict[str, Decimal]\n"
        "type Ledger = tuple[Decimal, ...]\n"
        "type Price = Decimal\n"
        "T = TypeVar('T', bound=Decimal)\n"
        "def g(x: object, c: Context) -> Decimal:\n"
        "    return cast(Decimal, x)\n"
        "def h(x: object) -> Decimal | None:\n"
        "    if isinstance(x, Decimal | int):\n"
        "        return cast(Decimal | None, x)\n"
        "    match x:\n"
        "        case Decimal():\n"
        "            return x\n"
        "    return None\n"
        "class Box[V: Decimal]:\n"
        "    pass\n"
        "U = TypeVar('U', bound=Decimal | None)\n"
        "W = TypeVar('W', Decimal, int)\n"
        "Ledger = dict[str, Decimal]\n"
        "class Book(dict[str, Decimal]):\n"
        "    pass\n"
        "Maybe = Decimal | None\n"
        "from typing import NewType\n"
        "Price = NewType('Price', Decimal)\n"
        "from typing import Annotated as A\n"
        "import typing\n"
        "y: A[Decimal, 'm'] | typing.Annotated[Decimal, 'n'] | None = None\n"
        "from collections.abc import Callable\n"
        "def k(handler: Callable[[Decimal], None]) -> None:\n"
        "    pass\n"
        "price: Decimal\n"
        "from typing import Union\n"
        "Either = Union[Decimal, int]\n"
    )
    (copy_of_source / "atp" / "contracts" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert decimal_findings(copy_of_source) == []


@pytest.mark.parametrize(
    "planted",
    [
        "def f(x):\n    return round(x)\n",
        "def f(x):\n    return x.to_integral_value()\n",
        "def f(x):\n    return x.to_integral()\n",
        "def f(x):\n    return x.__round__()\n",
        "def f(x):\n    return x.__floor__()\n",
        "r = round\n",
        "import builtins\nr = builtins.round\n",
        "import math\ndef f(x):\n    return math.floor(x)\n",
        "import math as m\ndef f(x):\n    return m.trunc(x)\n",
        "from math import ceil\ndef f(x):\n    return ceil(x)\n",
        "from math import isclose\n",
        "import cmath\n",
        "import statistics\n",
        "from statistics import fmean\n",
        "def f(x):\n    return float(x)\n",
        "convert = float\n",
        "convert = lambda: float\n",
        "CONVERTERS = {'ratio': float}\n",
        "def f(x):\n    return complex(x)\n",
        "def f(p, t):\n    return p - p.remainder_near(t)\n",
        "def f(x):\n    return x.__float__()\n",
        "def f(x, tick):\n    return x // tick * tick\n",
        "def f(x, tick):\n    return x % tick\n",
        "def f(x, tick):\n    x //= tick\n    return x\n",
        "def f(x, tick):\n    return divmod(x, tick)\n",
        "def f(x, tick):\n    return x.__floordiv__(tick)\n",
        "def f(x, tick):\n    return x.__mod__(tick)\n",
        "import operator\ndef f(x, tick):\n    return operator.floordiv(x, tick)\n",
        "from operator import mod\ndef f(x, tick):\n    return mod(x, tick)\n",
        "def f(x):\n    return x.__int__()\n",
        "from operator import __floordiv__\ndef f(x, tick):\n    return __floordiv__(x, tick)\n",
        "def f(context, x, tick):\n    return context.divide_int(x, tick)\n",
        "import builtins\ndef f(x, tick):\n    return builtins.divmod(x, tick)\n",
        "import builtins\ndef f(x):\n    return builtins.float(x)\n",
        "import builtins as b\nr = b.round\n",
        "from builtins import round as r\n",
        "from builtins import float\n",
        "def f(text):\n    return float.fromhex(text)\n",
    ],
)
def test_the_rounding_scanner_finds_planted_samples(
    copy_of_source: Path, planted: str
) -> None:
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert len(rounding_findings(copy_of_source)) == 1


def test_a_float_type_hint_or_check_is_not_a_finding(copy_of_source: Path) -> None:
    planted = (
        "def f(x: float) -> float | None:\n"
        "    return x if isinstance(x, float) else None\n"
        "def g(x, y):\n"
        "    return x / y\n"
    )
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert rounding_findings(copy_of_source) == []


@pytest.mark.parametrize(
    "planted",
    [
        "from pydantic import BaseModel\nclass T(BaseModel):\n    x: int\n",
        "import pydantic\nclass T(pydantic.RootModel[int]):\n    pass\n",
        "from pydantic import validate_call\n",
        "from pydantic.dataclasses import dataclass\n",
        "from pydantic import TypeAdapter\n",
        "from pydantic import dataclasses\n@dataclasses.dataclass\nclass T:\n    x: int\n",
        "import pydantic\n@pydantic.dataclasses.dataclass\nclass T:\n    x: int\n",
        "import pydantic\nT = pydantic.create_model('T', x=(int, ...))\n",
        "from pydantic import create_model\n",
        "from pydantic import BeforeValidator\n",
        "from pydantic.functional_validators import BeforeValidator\n",
        "from pydantic_core import SchemaValidator\n",
        "import pydantic_core\n",
        "def f(module):\n    return module.create_model('T')\n",
        "from atp.contracts._model import BaseModel\nclass T(BaseModel):\n    x: int\n",
        "import importlib\nm = importlib.import_module('pydantic')\n",
        "from importlib import import_module as load\nm = load('pydantic.dataclasses')\n",
    ],
)
def test_the_pydantic_scanner_finds_planted_samples(
    copy_of_source: Path, planted: str
) -> None:
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert pydantic_findings(copy_of_source)


def test_the_listed_pydantic_names_are_not_findings(copy_of_source: Path) -> None:
    planted = (
        "from pydantic import AfterValidator, Field, ValidationError, ValidationInfo\n"
        "from pydantic import field_validator\n"
    )
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert pydantic_findings(copy_of_source) == []


def test_integer_division_is_allowed_only_in_the_rounding_module(
    copy_of_source: Path,
) -> None:
    rounding = copy_of_source / "atp" / "numeric" / "_rounding.py"
    assert "divmod" in rounding.read_text(encoding="utf-8")
    assert rounding_findings(copy_of_source) == []
    (copy_of_source / "atp" / "numeric" / "_other.py").write_text(
        rounding.read_text(encoding="utf-8"), encoding="utf-8"
    )
    assert rounding_findings(copy_of_source)


def test_a_float_conversion_is_found_inside_atp_numeric_too(
    copy_of_source: Path,
) -> None:
    planted = "from decimal import Decimal\nx = Decimal.from_float(0.5)\n"
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert [
        finding
        for finding in decimal_findings(copy_of_source)
        if "from_float" in finding
    ]


@pytest.mark.parametrize(
    ("module", "planted"),
    [
        ("numeric", "from atp.contracts import Outcome\n"),
        ("numeric", "import atp.contracts\n"),
        ("contracts", "from atp.config import x\n"),
        ("contracts", "from atp.numeric._context import PRECISION\n"),
        ("contracts", "from atp.numeric import _context\n"),
        ("contracts", "from atp.numeric import _amount\nx = _amount.amount('1')\n"),
        ("contracts", "from ..numeric import _context\n"),
        ("numeric", "from atp import contracts\n"),
        ("numeric", "from .. import contracts\n"),
        ("numeric", "import atp\nx = atp.contracts.Outcome\n"),
        ("numeric", "import atp.numeric\nx = atp.contracts.Outcome\n"),
        ("numeric", "import atp as platform\nx = platform.contracts.Outcome\n"),
        ("contracts", "import atp\nx = atp.numeric._context.PRECISION\n"),
        ("contracts", "from atp import config\n"),
        # The command-line module imports only atp.config, and no module imports it.
        ("cli", "from atp.contracts import Contract\n"),
        ("cli", "from atp.numeric import amount\n"),
        ("config", "from atp.cli import main\n"),
        ("config", "from atp import cli\n"),
        ("contracts", "import atp.cli\n"),
        ("numeric", "from atp.config import load_configuration\n"),
        ("numeric", "import importlib\nm = importlib.import_module('atp.contracts')\n"),
        (
            "numeric",
            "from importlib import import_module as load\nm = load('atp.contracts')\n",
        ),
    ],
)
def test_the_import_scanner_finds_planted_samples(
    copy_of_source: Path, module: str, planted: str
) -> None:
    (copy_of_source / "atp" / module / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert len(import_findings(copy_of_source)) == 1


def test_an_allowed_import_from_the_package_root_is_not_a_finding(
    copy_of_source: Path,
) -> None:
    planted = (
        "import atp\n"
        "import atp.numeric\n"
        "from atp import numeric\n"
        "from .. import numeric as n\n"
        "from . import _model\n"
        "x = atp.__path__\n"
        "y = atp.numeric.amount\n"
        "z = atp.contracts._model\n"
    )
    (copy_of_source / "atp" / "contracts" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert import_findings(copy_of_source) == []


def test_a_relative_import_is_resolved(copy_of_source: Path) -> None:
    planted = "from ..contracts import Outcome\n"
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert len(import_findings(copy_of_source)) == 1


@pytest.mark.parametrize(
    "planted",
    [
        "def f(o):\n    return o._kind\n",
        "def f(o):\n    return getattr(o, '_kind')\n",
        "def f(o):\n    match o:\n        case object(_kind=k):\n            return k\n",
    ],
)
def test_the_private_member_scanner_finds_planted_samples(
    tmp_path: Path, planted: str
) -> None:
    (tmp_path / "planted.py").write_text(planted, encoding="utf-8")
    assert len(private_outcome_findings([tmp_path], frozenset({"_kind"}))) == 1


@pytest.mark.parametrize(
    "method",
    [
        "model_validate",
        "model_validate_json",
        "model_validate_strings",
        "model_construct",
        "model_copy",
        "validate_python",
        "validate_json",
        "validate_strings",
        "construct",
        "parse_obj",
        "parse_raw",
        "parse_file",
        "from_orm",
        "__pydantic_validator__",
        "validate_assignment",
    ],
)
def test_the_raw_validation_scanner_finds_planted_samples(
    copy_of_source: Path, method: str
) -> None:
    planted = f"def f(model, data):\n    return model.{method}(data)\n"
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert len(raw_validation_findings(copy_of_source)) == 1


def test_a_copy_with_update_is_found(copy_of_source: Path) -> None:
    planted = "def f(model):\n    return model.copy(update={'a': 1})\n"
    (copy_of_source / "atp" / "numeric" / "planted.py").write_text(
        planted, encoding="utf-8"
    )
    assert len(raw_validation_findings(copy_of_source)) == 1
