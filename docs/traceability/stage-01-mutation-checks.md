# Stage 1 — Mutation Checks as Run

> **Status:** REFERENCE (evidence) — the scripts of Stage 1's two mutation checks, exactly as they ran in the builder's session workspace, committed so that both checks can be repeated from the repository (master execution constitution §22) and do not exist only in the workspace ([owner decisions 14](../handoffs/owner-decisions-14-company-grade-order-and-traceability.md), §27; [owner decisions 15](../handoffs/owner-decisions-15-stage-transition-persistence-and-commit-integrity.md); [DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). They are not maintained tooling: kept in text blocks, they are neither linted nor run by the machine checks. Check 7 becomes maintained tooling with checkpoint C's work ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6), which also adds mutations for the secret scanner that U5 extends. The checks' results are in the verification records named below.

## Check 11 (checkpoint A): the secret scanner's twenty mutations

Run from the repository root as `python3 mutate4.py <empty work directory>`: nineteen mutations each write a mutated copy of the scanner's test module into the work directory and run it; the twentieth (M21) writes a mutant beside the real module, runs it, and removes it. Result, recorded in [checkpoint A's verification](stage-01-checkpoint-a-verification.md), check 11: each of the twenty mutations makes a test fail. Original: 3,390 bytes, sha256 `d5860dc7e8ab91edf525d0c0665f18dff3694d60870ee8d30b18cc253aa97b7e`.

```text
import pathlib, subprocess, sys, re
repo = pathlib.Path(".")
src = (repo / "tests/repository/test_no_secrets.py").read_text()
work = pathlib.Path(sys.argv[1])
M = [
 ("prefix rule back to a word boundary", r'rb"(?i)(?<![a-z0-9])"', r'rb"(?i)\b"'),
 ("no string prefixes", r'(?:[bru]{1,2})?', r''),
 ("single quote only", r'''[\"']{1,3}"''', r'''[\"']"'''),
 ("no template exclusion in settings", r'(?![$%]?\{)', r''),
 ("no environment-name exception", r'''(?!(?-i:[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)[\"'])''', r''),
 ("quoted values without the letter-and-digit rule", r'''(?=[^\"'\s]*[0-9])(?=[^\"'\s]*[A-Za-z])''', r''),
 ("URL user required", r"<>{}$%]*:", r"<>{}$%]+:"),
 ("URL templates and variables allowed", r"""[^\s/?#:@\"'<>{}$%]*:[^\s/?#@\"'<>{}$%]{3,}@""", r"""[^\s/:@\"'<>]*:[^\s/@\"'<>]{3,}@"""),
 ("unquoted assignment without the letter-and-digit rule", r"=[ \t]*(?=\S*[0-9])(?=\S*[A-Za-z])", r"=[ \t]*"),
 ("unquoted setting without the letter rule only (run 3 M10)", r'rb"(?=\S*[0-9])(?=\S*[A-Za-z])[A-Za-z0-9/+=_.~-]{12,}', r'rb"(?=\S*[0-9])[A-Za-z0-9/+=_.~-]{12,}'),
 ("unquoted assignment without CRLF", r'(?:#[^\r\n]*)?\r?$', r'(?:#[^\r\n]*)?$'),
 ("unquoted setting without CRLF", r'{12,}[ \t]*\r?$', r'{12,}[ \t]*$'),
 ("bare token name dropped (run 3 M26)", r'|secret|token)', r'|secret)'),
 ("ghs_ tokens dropped (run 3 M27)", r'gh[pousr]_', r'gh[pour]_'),
 ("ASIA keys dropped (run 3 M28)", r'(?:AKIA|ASIA)', r'(?:AKIA)'),
 ("value in the kind slot (run 3 M36)", 'findings.append(f"{relative}:{line}: secret-like value ({label})")',
    'findings.append(f"{relative}:{line}: secret-like value ({label})")\n                findings.append(f"{relative}:{line}: secret-like value ({match.group()[:6].decode()})")'),
 ("extra report with a value fragment (run 2 N3)", 'findings.append(f"{relative}:{line}: secret-like value ({label})")',
    'findings.append(f"{relative}:{line}: secret-like value ({label})")\n                findings.append(f"{relative}:{line}: secret-like value ({label}) {match.group()[-8:].decode()}")'),
 ("listing without untracked files", '"--others", ', ''),
 ("listing without the ignore rules", ', "--exclude-standard"', ''),
]
for name, old, new in M:
    n = src.count(old)
    if n != 1:
        print(f"{name}: SKIPPED, found {n} times"); continue
    out = work / "test_mutant.py"
    out.write_text(src.replace(old, new))
    r = subprocess.run(["uv", "run", "--locked", "pytest", "-q", "-p", "no:cacheprovider", str(out), "-k", "not test_repository_has"], capture_output=True, text=True)
    failed = sorted({l.split("::")[1].split("[")[0].split(" ")[0] for l in r.stdout.splitlines() if l.startswith("FAILED")})
    print(f"{'KILLED ' if r.returncode else 'SURVIVED'} {name}: {failed}")
# M21: repository root mis-set, run inside a copy at the right depth so only the root changes
mut = src.replace("REPOSITORY_ROOT = Path(__file__).resolve().parents[2]", "REPOSITORY_ROOT = Path(__file__).resolve().parents[1]")
assert mut != src
target = repo / "tests" / "repository" / "test_zz_root_mutant.py"
target.write_text(mut)
try:
    r = subprocess.run(["uv", "run", "--locked", "pytest", "-q", "-p", "no:cacheprovider", str(target), "-k", "test_repository_has"], capture_output=True, text=True)
    print(f"{'KILLED ' if r.returncode else 'SURVIVED'} repository root mis-set (run 3 M21): exit {r.returncode}")
finally:
    target.unlink()
```

## Check 7 (checkpoint B): the 329 mutations of the numeric and contract modules and the structure test

Run as `python3 mutate3.py <copy of the repository>`: each mutation edits one file of the copy, checks that it still parses (a mutation that does not parse is reported as invalid, never as caught), runs the tests without the repository test for secrets, or the type check, as the mutation names, and restores the file; the variables `ONLY` and `SLICE` select mutations. Result, recorded in [checkpoint B's verification](stage-01-checkpoint-b-verification.md), check 7: 329 of 329 caught on the tree of `4816059`. Original: 65,631 bytes, sha256 `17b44b8ab66f45f24613c3d7c0302a58fcb3546f8a1077c8006e0e6e48f61a5f`.

```text
"""Apply one mutation at a time to the scratch copy; each must make the tests or the type check fail."""
import os, subprocess, sys
from pathlib import Path

ROOT = Path(sys.argv[1])
PYTEST = ["uv", "run", "--locked", "pytest", "-q", "-x", "-p", "no:cacheprovider",
          "--ignore=tests/repository/test_no_secrets.py"]
MYPY = ["uv", "run", "--locked", "mypy", "--no-incremental"]

M = [
 ("N1 bool accepted", "src/atp/numeric/_amount.py", "elif type(value) is int:", "elif isinstance(value, int):", PYTEST),
 ("N1 subclass of str accepted", "src/atp/numeric/_amount.py", "if type(value) is str:", "if isinstance(value, str):", PYTEST),
 ("N1 Decimal subclass accepted", "src/atp/numeric/_amount.py", "elif type(value) is Decimal:", "elif isinstance(value, Decimal):", PYTEST),
 ("N1 non-finite accepted", "src/atp/numeric/_amount.py", "if not result.is_finite():", "if False:", PYTEST),
 ("N1 digit limit removed", "src/atp/numeric/_amount.py", "if len(digits) > PRECISION:", "if False:", PYTEST),
 ("N1 exponent range removed", "src/atp/numeric/_amount.py", "        or exponent < context.Etiny()\n        or result.adjusted() > context.Emax\n", "        and False\n", PYTEST),
 ("N1 Etiny loosened by 10", "src/atp/numeric/_amount.py", "exponent < context.Etiny()", "exponent < context.Etiny() - 10", PYTEST),
 ("N1 huge exponent not caught", "src/atp/numeric/_amount.py", "        except InvalidOperation:", "        except ZeroDivisionError:", PYTEST),
 ("N1 text form not ASCII-only", "src/atp/numeric/_amount.py", "_AMOUNT_RE: Final = re.compile(_AMOUNT_FORM, flags=re.ASCII)", "_AMOUNT_RE: Final = re.compile(_AMOUNT_FORM.replace('[0-9]', r'\\d'))", PYTEST),
 ("N1 text form check removed", "src/atp/numeric/_amount.py", "if _AMOUNT_RE.fullmatch(value) is None:", "if False:", PYTEST),
 ("N3 Inexact not trapped", "src/atp/numeric/_context.py", "        decimal.Inexact,\n", "", PYTEST),
 ("N3 FloatOperation not trapped", "src/atp/numeric/_context.py", "        decimal.FloatOperation,\n", "", PYTEST),
 ("N3 Overflow not trapped", "src/atp/numeric/_context.py", "        decimal.Overflow,\n", "", PYTEST),
 ("N3 DivisionByZero not trapped", "src/atp/numeric/_context.py", "        decimal.DivisionByZero,\n", "", PYTEST),
 ("N3 Emax 99", "src/atp/numeric/_context.py", "_EMAX: Final = 999_999", "_EMAX: Final = 99", PYTEST),
 ("N3 check ignores traps", "src/atp/numeric/_context.py", "        and all(\n            checked.traps[signal] == (signal in TRAPPED_SIGNALS)\n            for signal in checked.traps\n        )\n", "", PYTEST),
 ("N3 check ignores Emax", "src/atp/numeric/_context.py", "        and checked.Emax == _EMAX\n", "", PYTEST),
 ("N3 check ignores Emin", "src/atp/numeric/_context.py", "        and checked.Emin == _EMIN\n", "", PYTEST),
 ("N3 default context not set", "src/atp/numeric/_context.py", "    _apply(decimal.DefaultContext)\n", "", PYTEST),
 ("N3 unconfigured context allowed", "src/atp/numeric/_context.py", "    if not decimal_context_is_configured(context):", "    if False:", PYTEST),
 ("N3 quantize skips the context check", "src/atp/numeric/_rounding.py", "    require_configured_context()\n    _check(value, \"value\")", "    _check(value, \"value\")", PYTEST),
 ("N5 rounded division instead of divmod", "src/atp/numeric/_rounding.py", "    whole, remainder = divmod(value, increment)\n", "    import decimal as _d\n    with _d.localcontext() as _c:\n        _c.traps[_d.Inexact] = False\n        whole = (value / increment).to_integral_value(rounding=_d.ROUND_DOWN)\n    remainder = value - whole * increment\n", PYTEST),
 ("N5 away-from-zero wrong for negatives", "src/atp/numeric/_rounding.py", "        result = toward_zero + increment if value > 0 else toward_zero - increment", "        result = toward_zero + increment", PYTEST),
 ("N5 toward minus infinity wrong for negatives", "src/atp/numeric/_rounding.py", "        result = toward_zero if value > 0 else toward_zero - increment", "        result = toward_zero", PYTEST),
 ("N5 zero keeps its sign", "src/atp/numeric/_rounding.py", "    return result.copy_abs() if result.is_zero() else result", "    return result", PYTEST),
 ("N5 non-positive increment allowed", "src/atp/numeric/_rounding.py", "    if increment <= 0:", "    if increment < 0:", PYTEST),
 ("N5 non-Decimal operand allowed", "src/atp/numeric/_rounding.py", "    if type(value) is not Decimal:", "    if False:", PYTEST),
 ("N7 TOML underscores kept", "src/atp/numeric/_amount.py", 'return amount(text.replace("_", ""))', "return amount(text)", PYTEST),
 ("N6 JSON number accepted", "src/atp/contracts/_amount.py", "    if type(value) is not str and type(value) is not Decimal:", "    if type(value) in (int, float):\n        value = str(value)\n    if type(value) is not str and type(value) is not Decimal:", PYTEST),
 ("C strict off", "src/atp/contracts/_model.py", "    model_config = ConfigDict(\n        strict=True,", "    model_config = ConfigDict(\n        strict=False,", PYTEST),
 ("C frozen off", "src/atp/contracts/_model.py", "        frozen=True,", "        frozen=False,", PYTEST),
 ("C unknown fields ignored", "src/atp/contracts/_model.py", '        extra="forbid",', '        extra="ignore",', PYTEST),
 ("C instances not revalidated", "src/atp/contracts/_model.py", '        revalidate_instances="always",\n', "", PYTEST),
 ("C setattr allowed", "src/atp/contracts/_model.py", "    def __setattr__(self, name: str, value: object) -> NoReturn:\n        # Pydantic's own refusal for a frozen model repeats the assigned value in its text.\n        msg = \"a contract is immutable\"\n        raise AttributeError(msg)\n", "", PYTEST),
 ("C allowlist accepts anything", "src/atp/contracts/_model.py", "    msg = (\n        f\"{where}: a contract holds only immutable types", "    return\n    msg = (\n        f\"{where}: a contract holds only immutable types", PYTEST),
 ("C plain Decimal accepted", "src/atp/contracts/_model.py", "    if annotation is Decimal:\n        msg =", "    if annotation is Decimal:\n        return\n        msg =", PYTEST),
 ("C nested types not checked", "src/atp/contracts/_model.py", "            if argument is not Ellipsis:\n                _refuse_field_type(argument, where)", "            pass", PYTEST),
 ("C unresolved annotation accepted", "src/atp/contracts/_model.py", "    if isinstance(annotation, str | typing.ForwardRef):\n", "    if isinstance(annotation, str | typing.ForwardRef):\n        return\n", PYTEST),
 ("C identity form loosened", "src/atp/contracts/_model.py", "    if _CONTRACT_ID.fullmatch(contract_id) is None:", "    if not contract_id:", PYTEST),
 ("C inherited identity accepted", "src/atp/contracts/_model.py", "    declared = cls.__dict__", "    declared = {name: getattr(cls, name, None) for name in ('contract_id', 'contract_version')}", PYTEST),
 ("C aliases not registered", "src/atp/contracts/_model.py", "        if field.alias is not None:\n            names.append(field.alias)\n", "", PYTEST),
 ("E refusal keeps the original error as context", "src/atp/contracts/_model.py", "            return cls.model_validate(data)\n        except ValidationError as error:\n            details = validation_error_details(error)\n", "            return cls.model_validate(data)\n        except ValidationError as error:\n            raise ContractError(cls.contract_id, validation_error_details(error)) from None\n", PYTEST),
 ("E JSON refusal keeps the original error as context", "src/atp/contracts/_model.py", "            return cls.model_validate_json(data)\n        except ValidationError as error:\n            details = validation_error_details(error)\n", "            return cls.model_validate_json(data)\n        except ValidationError as error:\n            raise ContractError(cls.contract_id, validation_error_details(error)) from None\n", PYTEST),
 ("E unknown key name kept", "src/atp/contracts/_errors.py", "            part if isinstance(part, int) or part in _known_names else REDACTED", "            part", PYTEST),
 ("E input-key redaction off", "src/atp/contracts/_errors.py", "        if kind in _INPUT_KEY_TYPES and parts:", "        if False:", PYTEST),
 ('E all messages kept', 'src/atp/contracts/_errors.py', '        if not _is_own_message(kind, message, item.get("ctx")):\n            message = GENERIC_MESSAGE\n', '', PYTEST),
 ("E value_error messages kept", "src/atp/contracts/_errors.py", "        \"union_tag_not_found\",\n", "        \"union_tag_not_found\",\n        \"value_error\",\n", PYTEST),
 ("E input hidden off", "src/atp/contracts/_model.py", "        hide_input_in_errors=True,", "        hide_input_in_errors=False,", PYTEST),
 ("E refusal not picklable", "src/atp/contracts/_errors.py", "        return (ContractError, (self.contract_id, self.details))", "        return super().__reduce__()", PYTEST),
 ("V minor rule dropped", "src/atp/contracts/_version.py", "    return produced.major == understood.major and produced.minor <= understood.minor", "    return produced.major == understood.major", PYTEST),
 ("V zero major allowed", "src/atp/contracts/_version.py", "        if self.major == 0:", "        if False:", PYTEST),
 ("O __bool__ visible to mypy", "src/atp/contracts/_outcome.py", "    if not TYPE_CHECKING:\n", "    if True:\n", MYPY),
 ("O fold handler optional", "src/atp/contracts/_outcome.py", "        on_unknown: Callable[[], R],\n    ) -> R:", "        on_unknown: Callable[[], R] = lambda: None,  # type: ignore[assignment,return-value]\n    ) -> R:", MYPY),
 ("O comparison allowed", "src/atp/contracts/_outcome.py", "        def __eq__(self, other):\n            msg = \"outcomes are not compared; read them with fold\"\n            raise TypeError(msg)\n", "", PYTEST),
 ("O truth value allowed at run time", "src/atp/contracts/_outcome.py", "        def __bool__(self):\n            msg = \"an outcome has no truth value; read it with fold\"\n            raise TypeError(msg)\n", "        def __bool__(self):\n            return True\n", PYTEST),
 ("O direct construction allowed", "src/atp/contracts/_outcome.py", "        if token is not _TOKEN:", "        if False:", PYTEST),
 ("O extra JSON field accepted", "src/atp/contracts/_outcome.py", 'extra_behavior="forbid"', 'extra_behavior="ignore"', PYTEST),
 ("O envelope not strict", "src/atp/contracts/_outcome.py", "                config=core_schema.CoreConfig(strict=True),\n", "", PYTEST),
 ("O instance payload not validated", "src/atp/contracts/_outcome.py", "            if isinstance(value, Outcome):\n                value = _to_envelope(value)\n            return handler(value)", "            if isinstance(value, Outcome):\n                return value\n            return handler(value)", PYTEST),
 ("O python dump shows the envelope", "src/atp/contracts/_outcome.py", "                _to_envelope, return_schema=envelope, when_used=\"json\"", "                _to_envelope, return_schema=envelope, when_used=\"always\"", PYTEST),
 ("O mutable", "src/atp/contracts/_outcome.py", "    def __setattr__(self, name: str, value: object) -> None:\n        msg = \"an outcome is immutable\"\n        raise AttributeError(msg)\n", "", PYTEST),
 ("O deletable", "src/atp/contracts/_outcome.py", "    def __delattr__(self, name: str) -> None:\n        msg = \"an outcome is immutable\"\n        raise AttributeError(msg)\n", "", PYTEST),
 ("O subclassable", "src/atp/contracts/_outcome.py", "        msg = \"Outcome cannot be subclassed\"\n        raise TypeError(msg)\n", "        pass\n", PYTEST),
 ("O not picklable", "src/atp/contracts/_outcome.py", "        return (_rebuild, (self._kind.value, self._payload))", "        raise TypeError('no')", PYTEST),
 ("K mutable", "src/atp/contracts/_idempotency.py", "    def __setattr__(self, name: str, value: object) -> None:\n        msg = \"an idempotency key is immutable\"\n        raise AttributeError(msg)\n", "", PYTEST),
 ("K subclassable", "src/atp/contracts/_idempotency.py", "        msg = \"IdempotencyKey cannot be subclassed\"\n        raise TypeError(msg)\n", "        pass\n", PYTEST),
 ("K not picklable", "src/atp/contracts/_idempotency.py", "        return (IdempotencyKey, (self._text,))", "        raise TypeError('no')", PYTEST),
 ("K uppercase accepted", "src/atp/contracts/_idempotency.py", '_PATTERN: Final = "[0-9a-f]{32}"', '_PATTERN: Final = "[0-9a-fA-F]{32}"', PYTEST),
 ("K short key accepted", "src/atp/contracts/_idempotency.py", '_PATTERN: Final = "[0-9a-f]{32}"', '_PATTERN: Final = "[0-9a-f]{16,32}"', PYTEST),
 ('K error types merged', 'src/atp/contracts/_idempotency.py', 'raise PydanticCustomError("idempotency_key_invalid", _KEY_INVALID) from None', 'raise PydanticCustomError("idempotency_key_type", _KEY_INVALID) from None', PYTEST),
 ("S schema changed without version", "src/atp/contracts/_amount.py", '"A decimal amount written as a string.', '"A decimal amount, written as a string.', PYTEST),
 ("S overwrite allowed", "src/atp/contracts/_schemas.py", "            if path.read_text(encoding=\"utf-8\") != document.text():", "            if False:", PYTEST),
 ("S duplicate identities allowed", "src/atp/contracts/_schemas.py", "    if duplicates:\n", "    if False:\n", PYTEST),
 ("T structure: decimal module context names off", "tests/repository/test_structure.py", "                and node.attr in MODULE_CONTEXT_NAMES\n", "                and False\n", PYTEST),
 ("T structure: context attributes off", "tests/repository/test_structure.py", "            ) or (isinstance(node, ast.Attribute) and node.attr in CONTEXT_ATTRIBUTES):", "            ) or False:", PYTEST),
 ("T structure: context imports off", "tests/repository/test_structure.py", "                    alias.name in MODULE_CONTEXT_NAMES | CONTEXT_ATTRIBUTES\n", "                    False\n", PYTEST),
 ("T structure: any Context counted", "tests/repository/test_structure.py", "                and isinstance(node.value, ast.Name)\n                and node.value.id in decimal_modules\n            ) or (", "            ) or (isinstance(node, ast.Name) and node.id in MODULE_CONTEXT_NAMES) or (", PYTEST),
 ("T structure: round scanner off", "tests/repository/test_structure.py", "(isinstance(node, ast.Name) and node.id == \"round\")", "(isinstance(node, ast.Name) and node.id == \"never\")", PYTEST),
 ("T structure: private import scanner off", "tests/repository/test_structure.py", "            elif target != owner and any(\n", "            elif False and any(\n", PYTEST),
 ("T structure: model_validate dropped", "tests/repository/test_structure.py", "        \"validate_assignment\",\n        \"model_validate\",\n", "        \"validate_assignment\",\n", PYTEST),
 ("T structure: raw validation scanner off", "tests/repository/test_structure.py", "            if isinstance(node, ast.Attribute) and node.attr in RAW_VALIDATION", "            if False", PYTEST),
 ("C base settings not checked", "src/atp/contracts/_model.py", "        if cls.model_config.get(key) != _BASE_CONFIG.get(key):", "        if False:", PYTEST),
 ("C private attributes allowed", "src/atp/contracts/_model.py", "    if cls.__private_attributes__:", "    if False:", PYTEST),
 ('C field loosening allowed', 'src/atp/contracts/_model.py', '    if any(_loosens(item) for item in metadata):\n', '    if False:\n', PYTEST),
 ("C nested Field loosening missed", "src/atp/contracts/_model.py", "        return any(_loosens(inner) for inner in item.metadata)", "        return False", PYTEST),
 ("C allow_inf_nan only for strict", "src/atp/contracts/_model.py", "        or getattr(item, \"allow_inf_nan\", None) is True\n", "", PYTEST),
 ("C runtime values not checked", "src/atp/contracts/_model.py", "        if not _fields_conform(self):", "        if False:", PYTEST),
 ('C runtime tuple contents not checked', 'src/atp/contracts/_model.py', '            return all(_conforms(item, arguments[0]) for item in value)', '            return True', PYTEST),
 ("C infinities allowed", "src/atp/contracts/_model.py", "        allow_inf_nan=False,\n", "", PYTEST),
 ("C amount values not checked", "src/atp/contracts/_model.py", "    if annotation is Amount:\n        return type(value) is Decimal and value.is_finite()", "    if annotation is Amount:\n        return True", PYTEST),
 ("N3 precision check loosened", "src/atp/numeric/_context.py", "        checked.prec == PRECISION", "        checked.prec >= PRECISION", PYTEST),
 ("N7 TOML strips one underscore", "src/atp/numeric/_amount.py", 'return amount(text.replace("_", ""))', 'return amount(text.replace("_", "", 1))', PYTEST),
 ("E invalid key kept", "src/atp/contracts/_errors.py", 'frozenset({"extra_forbidden", "invalid_key"})', 'frozenset({"extra_forbidden"})', PYTEST),
 ("E assertion messages kept", "src/atp/contracts/_errors.py", "        \"union_tag_not_found\",\n", "        \"union_tag_not_found\",\n        \"assertion_error\",\n", PYTEST),
 ("E detail mutable", "src/atp/contracts/_errors.py", "@dataclass(frozen=True, slots=True)\nclass ErrorDetail:", "@dataclass(slots=True)\nclass ErrorDetail:", PYTEST),
 ("C JSON not strict", "src/atp/contracts/_model.py", "            return cls.model_validate_json(data)", "            return cls.model_validate_json(data, strict=False)", PYTEST),
 ("N6 amounts as text in Python dumps", "src/atp/contracts/_amount.py", 'str, return_schema=core_schema.str_schema(), when_used="json"', 'str, return_schema=core_schema.str_schema(), when_used="always"', PYTEST),
 ("S modules not imported", "src/atp/contracts/_schemas.py", "        importlib.import_module(name)\n", "        pass\n", PYTEST),
 ("T structure: Decimal value scanner off", "tests/repository/test_structure.py", "            ) and not _type_use_only(node, parents, annotated, unions):", "            ) and False:", PYTEST),
 ("T structure: star import off", "tests/repository/test_structure.py", "                and any(alias.name == \"*\" for alias in node.names)", "                and False", PYTEST),
 ("T structure: own type call off", "tests/repository/test_structure.py", "                and node.func.func.id == \"type\"", "                and node.func.func.id == \"never\"", PYTEST),
 ("T structure: TOML parse_float off", "tests/repository/test_structure.py", 'findings.append(f"{where}: TOML read without parse_float")', "pass", PYTEST),
 ("T structure: pydantic models off", "tests/repository/test_structure.py", "                    if base_name in PYDANTIC_MODELS:", "                    if False:", PYTEST),
 ("T structure: pydantic validators off", "tests/repository/test_structure.py", "            if name in PYDANTIC_VALIDATORS:", "            if False:", PYTEST),
 ("T structure: float converter off", "tests/repository/test_structure.py", "                and node.id in FLOAT_CONVERTERS", "                and node.id == \"never\"", PYTEST),
 ('T structure: builtins.round off', 'tests/repository/test_structure.py', '                and node.value.id in builtins_modules\n            ):\n                findings.append(f"{where}: round")', '                and False\n            ):\n                findings.append(f"{where}: round")', PYTEST),
 ('T structure: dunder rounding off', 'tests/repository/test_structure.py', '        "to_integral_value",\n        "__round__",\n', '        "to_integral_value",\n', PYTEST),
 ("T structure: copy(update) off", "tests/repository/test_structure.py", "                and any(keyword.arg == \"update\" for keyword in node.keywords)", "                and False", PYTEST),
 ("T structure: v1 from_orm dropped", "tests/repository/test_structure.py", "        \"from_orm\",\n    }\n)", "    }\n)", PYTEST),
 # Gate 3 run 3: allow-lists in the kernel
 ("C metadata allowlist off", "src/atp/contracts/_model.py", "    msg = (\n        f\"{where}: a field's metadata holds only", "    return\n    msg = (\n        f\"{where}: a field's metadata holds only", PYTEST),
 ("C amount schema on any type", "src/atp/contracts/_model.py", "        if item is AmountSchema:\n            msg = f\"{where}: an amount's schema is used only through Amount\"\n            raise TypeError(msg)\n", "        if item is AmountSchema:\n            continue\n", PYTEST),
 ("C Field settings not checked", "src/atp/contracts/_model.py", "type(item) is not _GENERAL_METADATA or set(vars(item)) <= _GENERAL_CONSTRAINTS", "True", PYTEST),
 ("C nested Field metadata not checked", "src/atp/contracts/_model.py", "        for inner in item.metadata:\n            _refuse_metadata(base, inner, where)\n        return", "        return", PYTEST),
 ("C excluded field allowed", "src/atp/contracts/_model.py", "    if field.exclude or field.exclude_if is not None:", "    if False:", PYTEST),
 ("C exclude_if allowed", "src/atp/contracts/_model.py", "    if field.exclude or field.exclude_if is not None:", "    if field.exclude:", PYTEST),
 ("C unvalidated default allowed", "src/atp/contracts/_model.py", "    if field.validate_default is False:", "    if False:", PYTEST),
 ("C settings the base lacks allowed", "src/atp/contracts/_model.py", "    for key in sorted(_BASE_CONFIG.keys() | cls.model_config.keys()):", "    for key in sorted(_BASE_CONFIG.keys()):", PYTEST),
 ("C kernel methods redefinable", "src/atp/contracts/_model.py", "        if redefined:", "        if False:", PYTEST),
 ("C __init__ redefinable", "src/atp/contracts/_model.py", "        \"__init__\",\n", "", PYTEST),
 ("C check redefinable", "src/atp/contracts/_model.py", "        \"to_json\",\n        \"_check_declared_types\",\n", "        \"to_json\",\n", PYTEST),
 ("C decorators not checked", "src/atp/contracts/_model.py", "    _refuse_decorators(cls)\n", "", PYTEST),
 ("C version 1 validators allowed", "src/atp/contracts/_model.py", "    if decorators.validators or decorators.root_validators:", "    if False:", PYTEST),
 ("C before field validators allowed", "src/atp/contracts/_model.py", "        if decorator.info.mode != \"after\":", "        if False:", PYTEST),
 ("C model validators allowed", "src/atp/contracts/_model.py", "    if model_validators != _BASE_MODEL_VALIDATORS:", "    if False:", PYTEST),
 ("C serializers allowed", "src/atp/contracts/_model.py", "        decorators.field_serializers\n        or decorators.model_serializers\n        or decorators.computed_fields", "        False", PYTEST),
 ("C computed fields allowed", "src/atp/contracts/_model.py", "        or decorators.computed_fields\n", "\n", PYTEST),
 ("C bytes accepted", "src/atp/contracts/_model.py", "_IMMUTABLE_LEAVES: Final[tuple[type, ...]] = (\n    str,\n", "_IMMUTABLE_LEAVES: Final[tuple[type, ...]] = (\n    bytes,\n    str,\n", PYTEST),
 # the run-time type check
 ("R Annotated not followed", "src/atp/contracts/_model.py", "    if origin is Annotated:\n        return _conforms(value, arguments[0])", "    if origin is Annotated:\n        return True", PYTEST),
 ("R non-finite Decimal accepted", "src/atp/contracts/_model.py", "        return type(value) is Decimal and value.is_finite()", "        return type(value) is Decimal", PYTEST),
 ("R non-finite float accepted", "src/atp/contracts/_model.py", "        return type(value) is float and _is_finite_float(value)", "        return type(value) is float", PYTEST),
 ("R finite check always true", "src/atp/contracts/_model.py", "    return value - value == 0", "    return True", PYTEST),
 ("R None not checked", "src/atp/contracts/_model.py", "        return value is None", "        return True", PYTEST),
 ("R datetime accepted as date", "src/atp/contracts/_model.py", "        return isinstance(value, datetime.date) and not isinstance(\n            value, datetime.datetime\n        )", "        return isinstance(value, datetime.date)", PYTEST),
 ("R exact leaves by isinstance", "src/atp/contracts/_model.py", "        return type(value) is annotation", "        return isinstance(value, annotation)", PYTEST),
 ("R other leaves not checked", "src/atp/contracts/_model.py", "    if annotation in _IMMUTABLE_LEAVES:\n        return isinstance(value, annotation)", "    if annotation in _IMMUTABLE_LEAVES:\n        return True", PYTEST),
 ("R literal type ignored", "src/atp/contracts/_model.py", "            type(value) is type(allowed) and value == allowed for allowed in arguments", "            value == allowed for allowed in arguments", PYTEST),
 ("R enums not checked", "src/atp/contracts/_model.py", "issubclass(annotation, enum.Enum):\n        return isinstance(value, annotation)", "issubclass(annotation, enum.Enum):\n        return True", PYTEST),
 ("R contracts not checked", "src/atp/contracts/_model.py", "        return isinstance(value, annotation) and _fields_conform(value)", "        return True", PYTEST),
 ("R nested contract fields not checked", "src/atp/contracts/_model.py", "        return isinstance(value, annotation) and _fields_conform(value)", "        return isinstance(value, annotation)", PYTEST),
 ('C top-level metadata ignored', 'src/atp/contracts/_model.py', '        _refuse_annotated(field.annotation, field.metadata, where)\n', '        _refuse_annotated(field.annotation, (), where)\n', PYTEST),
 ("R union not checked", "src/atp/contracts/_model.py", "        return any(_conforms(value, argument) for argument in arguments)", "        return True", PYTEST),
 ("R set accepted as frozenset", "src/atp/contracts/_model.py", "        return type(value) is frozenset and all(", "        return all(", PYTEST),
 ("R frozenset contents not checked", "src/atp/contracts/_model.py", "            _conforms(item, arguments[0]) for item in value\n        )", "            True for item in value\n        )", PYTEST),
 ("R list accepted as tuple", "src/atp/contracts/_model.py", "        if type(value) is not tuple:\n            return False\n", "", PYTEST),
 ("R fixed tuple length not checked", "src/atp/contracts/_model.py", "        return len(value) == len(arguments) and all(", "        return all(", PYTEST),
 ("R fixed tuple items not checked", "src/atp/contracts/_model.py", "            _conforms(item, argument)\n            for item, argument", "            True\n            for item, argument", PYTEST),
 ("R non-outcome accepted", "src/atp/contracts/_model.py", "        if not isinstance(value, Outcome):\n            return False\n", "", PYTEST),
 ("R success value not checked", "src/atp/contracts/_model.py", "            return _conforms(payload, arguments[0])", "            return True", PYTEST),
 ("R failure error not checked", "src/atp/contracts/_model.py", "            return _conforms(payload, arguments[1])", "            return True", PYTEST),
 ("N5 rounding type not checked", "src/atp/numeric/_rounding.py", "    if type(rounding) is not Rounding:", "    if False:", PYTEST),
 # the scanners
 ("T structure: JSON parse_float off", "tests/repository/test_structure.py", 'findings.append(\n                    f"{where}: JSON read without parse_float and parse_constant"\n                )', "pass", PYTEST),
 ("T structure: JSONDecoder not scanned", "tests/repository/test_structure.py", '                    or _called_name(node) in json_decoders', "                    or False", PYTEST),
 ("T structure: renamed amount builders missed", "tests/repository/test_structure.py", "            if alias.name in AMOUNT_BUILDERS and alias.asname", "            if False", PYTEST),
 ("T structure: keyword text missed", "tests/repository/test_structure.py", "                        *(keyword.value for keyword in node.keywords),\n", "", PYTEST),
 ("T structure: nested text missed", "tests/repository/test_structure.py", "                    for part in ast.walk(argument)", "                    for part in [argument]", PYTEST),
 ("T structure: floordiv dunder dropped", "tests/repository/test_structure.py", "        \"__int__\",\n        \"__floordiv__\",\n", "        \"__int__\",\n", PYTEST),
 ("T structure: mod dunder dropped", "tests/repository/test_structure.py", "        \"__rfloordiv__\",\n        \"__mod__\",\n", "        \"__rfloordiv__\",\n", PYTEST),
 ("T structure: operator attribute missed", "tests/repository/test_structure.py", "                    and node.attr in OPERATOR_DIVISION", "                    and False", PYTEST),
 ("T structure: operator names missed", "tests/repository/test_structure.py", "                or (isinstance(node, ast.Name) and node.id in operator_names)", "                or False", PYTEST),
 ("T structure: amount from text off", "tests/repository/test_structure.py", "findings.append(f\"{where}: an amount built from a value's text\")", "pass", PYTEST),
 ("T structure: f-string text off", "tests/repository/test_structure.py", "and any(isinstance(part, ast.FormattedValue) for part in node.values)", "and False", PYTEST),
 ("T structure: text methods off", "tests/repository/test_structure.py", "                    and node.func.attr in TEXT_METHODS", "                    and False", PYTEST),
 ("T structure: % text off", "tests/repository/test_structure.py", "        or (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod))\n    )", "        or False\n    )", PYTEST),
 ("T structure: ascii dropped", "tests/repository/test_structure.py", 'TEXT_OF_A_VALUE = frozenset({"str", "repr", "format", "ascii"})', 'TEXT_OF_A_VALUE = frozenset({"str", "repr", "format"})', PYTEST),
 ("T structure: amount_from_toml not scanned", "tests/repository/test_structure.py", 'AMOUNT_BUILDERS = frozenset({"amount", "amount_from_toml"})', 'AMOUNT_BUILDERS = frozenset({"amount"})', PYTEST),
 ("T structure: attribute amount not scanned", "tests/repository/test_structure.py", "    if isinstance(node.func, ast.Attribute):\n        return node.func.attr\n    return None", "    return None", PYTEST),
 ("T structure: float modules off", "tests/repository/test_structure.py", '                if name.split(".")[0] in FLOAT_MODULES', "                if False", PYTEST),
 ("T structure: statistics dropped", "tests/repository/test_structure.py", 'FLOAT_MODULES = frozenset({"math", "cmath", "statistics"})', 'FLOAT_MODULES = frozenset({"math", "cmath"})', PYTEST),
 ("T structure: cmath dropped", "tests/repository/test_structure.py", 'FLOAT_MODULES = frozenset({"math", "cmath", "statistics"})', 'FLOAT_MODULES = frozenset({"math", "statistics"})', PYTEST),
 ("T structure: from-imports of float modules missed", "tests/repository/test_structure.py", "                if isinstance(node, ast.ImportFrom) and node.module\n", "                if False\n", PYTEST),
 ("T structure: integer division off", "tests/repository/test_structure.py", 'findings.append(f"{where}: integer division or remainder")', "pass", PYTEST),
 ("T structure: remainder not scanned", "tests/repository/test_structure.py", "isinstance(node.op, ast.FloorDiv | ast.Mod)", "isinstance(node.op, ast.FloorDiv)", PYTEST),
 ("T structure: augmented division not scanned", "tests/repository/test_structure.py", "isinstance(node, ast.BinOp | ast.AugAssign)", "isinstance(node, ast.BinOp)", PYTEST),
 ("T structure: divmod not scanned", "tests/repository/test_structure.py", '                or (isinstance(node, ast.Name) and node.id == "divmod")', "                or False", PYTEST),
 ("T structure: division allowed in all of numeric", "tests/repository/test_structure.py", "        divides = module not in INTEGER_DIVISION_ALLOWED", '        divides = not module.startswith("atp.numeric")', PYTEST),
 ("T structure: division not allowed in rounding", "tests/repository/test_structure.py", "        divides = module not in INTEGER_DIVISION_ALLOWED", "        divides = True", PYTEST),
 ('T structure: __float__ dropped', 'tests/repository/test_structure.py', '        "__trunc__",\n        "__float__",\n', '        "__trunc__",\n', PYTEST),
 ("T structure: lambda converter off", "tests/repository/test_structure.py", "isinstance(parent, ast.keyword | ast.Return | ast.Lambda)", "isinstance(parent, ast.keyword | ast.Return)", PYTEST),
 ("T structure: pydantic module import off", "tests/repository/test_structure.py", '                    if alias.name.split(".")[0] in {"pydantic", "pydantic_core"}', "                    if False", PYTEST),
 ("T structure: pydantic submodule import off", "tests/repository/test_structure.py", '                if root == "pydantic_core" or (\n                    root == "pydantic" and node.module != "pydantic"\n                ):', "                if False:", PYTEST),
 ("T structure: pydantic_core from-import missed", "tests/repository/test_structure.py", '                if root == "pydantic_core" or (', "                if False or (", PYTEST),
 ("T structure: pydantic allowlist off", "tests/repository/test_structure.py", "                        if alias.name not in PYDANTIC_ALLOWED\n", "                        if False\n", PYTEST),
 ("T structure: create_model not named", "tests/repository/test_structure.py", 'PYDANTIC_VALIDATORS = frozenset({"validate_call", "TypeAdapter", "create_model"})', 'PYDANTIC_VALIDATORS = frozenset({"validate_call", "TypeAdapter"})', PYTEST),
 # Gate 3 run 4
 ("A amount's inner decimal schema dropped (strict=True cannot apply)", "src/atp/contracts/_amount.py", "        return core_schema.no_info_before_validator_function(\n            _validate,\n            handler(source),\n", "        return core_schema.no_info_plain_validator_function(\n            _validate,\n", PYTEST),
 ('C float bounds allowed', 'src/atp/contracts/_model.py', '        value is None or _is_amount_bound(value) for value in bounds\n', '        True for value in bounds\n', PYTEST),
 ('C amount unions allowed', 'src/atp/contracts/_model.py', '        msg = (\n            f"{where}: an amount is combined in a union only with None or a literal of "\n            "strings"\n        )\n        raise TypeError(msg)\n', '        pass\n', PYTEST),
 ("C validator exception escapes from_python", "src/atp/contracts/_model.py", "        except Exception as error:\n            if isinstance(error, DecimalContextError):\n                raise  # the process", "        except ZeroDivisionError as error:\n            if isinstance(error, DecimalContextError):\n                raise  # the process", PYTEST),
 ("C validator exception escapes from_json", "src/atp/contracts/_model.py", "        except Exception as error:\n            if isinstance(error, DecimalContextError):\n                raise\n            details", "        except ZeroDivisionError as error:\n            if isinstance(error, DecimalContextError):\n                raise\n            details", PYTEST),
 ("C validator exception text kept", "src/atp/contracts/_model.py", 'f"a validator raised {type(error).__name__}"', 'f"a validator raised {error!r}"', PYTEST),
 ("C written under the field name", "src/atp/contracts/_model.py", "        serialize_by_alias=True,\n", "", PYTEST),
 ("C second read name allowed", "src/atp/contracts/_model.py", "    if field.validation_alias not in (None, field.alias) or (", "    if False or (", PYTEST),
 ("C second written name allowed", "src/atp/contracts/_model.py", "        field.serialization_alias not in (None, field.alias)\n", "        False\n", PYTEST),
 ("C unlisted field settings allowed", "src/atp/contracts/_model.py", "        if setting not in _ALLOWED_FIELD_SETTINGS and getattr(", "        if False and getattr(", PYTEST),
 ("C frozen listed", "src/atp/contracts/_model.py", "        \"metadata\",\n    }\n)\n_BOUNDS", "        \"metadata\",\n        \"frozen\",\n    }\n)\n_BOUNDS", PYTEST),
 ("C mixins not checked", "src/atp/contracts/_model.py", "    for klass in cls.__mro__:", "    for klass in cls.__mro__[:1]:", PYTEST),
 ("N3 capitals not checked", "src/atp/numeric/_context.py", "        and checked.capitals == 1\n", "", PYTEST),
 ('T structure: remainder_near dropped', 'tests/repository/test_structure.py', '        "__rdivmod__",\n        "remainder_near",\n', '        "__rdivmod__",\n', PYTEST),
 ("T structure: dumps not text", "tests/repository/test_structure.py", "TEXT_METHODS = frozenset(\n    {\n        \"format\",\n        \"dumps\",\n", "TEXT_METHODS = frozenset(\n    {\n        \"format\",\n", PYTEST),
 ("T structure: __str__ not text", "tests/repository/test_structure.py", "        \"dumps\",\n        \"__str__\",\n        \"__repr__\",\n", "        \"dumps\",\n        \"__repr__\",\n", PYTEST),
 ("T structure: parse_float=None accepted", "tests/repository/test_structure.py", "            isinstance(keyword.value, ast.Constant) and keyword.value.value is None", "            False", PYTEST),
 ("T structure: ValidationInfo not allowed", "tests/repository/test_structure.py", '{"Field", "AfterValidator", "field_validator", "ValidationInfo", "ValidationError"}', '{"Field", "AfterValidator", "field_validator", "ValidationError"}', PYTEST),
 # Gate 3 run 5
 ("C metaclass checks skipped", "src/atp/contracts/_model.py", "            _check_contract_class(typing.cast(\"type[Contract]\", cls))", "            pass", PYTEST),
 ("C checks run from the first base's hook", "src/atp/contracts/_model.py", "class Contract(BaseModel, metaclass=_ContractMeta):\n    \"\"\"Base of every contract. Subclasses set `contract_id` and `contract_version`.\"\"\"\n", "class Contract(BaseModel):\n    \"\"\"Base of every contract. Subclasses set `contract_id` and `contract_version`.\"\"\"\n\n    @classmethod\n    def __pydantic_init_subclass__(cls, **kwargs: Any) -> None:\n        super().__pydantic_init_subclass__(**kwargs)\n        _check_contract_class(cls)\n", PYTEST),
 ("C replace allowed", "src/atp/contracts/_model.py", "    def __replace__(self, **changes: object) -> NoReturn:\n", "    def _unused_replace(self, **changes: object) -> NoReturn:\n", PYTEST),
 ("C replace redefinable", "src/atp/contracts/_model.py", "        \"__replace__\",\n", "", PYTEST),
 ("C model_dump redefinable", "src/atp/contracts/_model.py", "        \"model_dump\",\n", "", PYTEST),
 ("C schema hook redefinable", "src/atp/contracts/_model.py", "        \"__get_pydantic_core_schema__\",\n", "", PYTEST),
 ('C deprecated field read as an attribute', 'src/atp/contracts/_model.py', '        _conforms(values[name], field.annotation)', '        _conforms(getattr(contract, name), field.annotation)', PYTEST),
 ('C float bound on an optional amount allowed', 'src/atp/contracts/_model.py', '    if _holds_amount(base) and not all(', '    if _is_amount(base) and not all(', PYTEST),
 ("C an amount's bound checked only on a bare amount", 'src/atp/contracts/_model.py', '    return any(member is Amount for member in _union_members(annotation))\n', '    return annotation is Amount\n', PYTEST),
 ("C context error reported as refused input (python)", "src/atp/contracts/_model.py", "            if isinstance(error, DecimalContextError):\n                raise  # the process", "            if False:\n                raise  # the process", PYTEST),
 ("C context error reported as refused input (json)", "src/atp/contracts/_model.py", "            if isinstance(error, DecimalContextError):\n                raise\n            details", "            if False:\n                raise\n            details", PYTEST),
 ("N3 context error is a plain RuntimeError", "src/atp/numeric/_context.py", "        raise DecimalContextError(msg)", "        raise RuntimeError(msg)", PYTEST),
 ("E count messages kept", "src/atp/contracts/_errors.py", "        \"string_type\",\n        \"tuple_type\",\n", "        \"string_type\",\n        \"too_long\",\n        \"tuple_type\",\n", PYTEST),
 ("T structure: private names from another package allowed", "tests/repository/test_structure.py", "            elif target != owner and any(name.startswith(\"_\") for name in names):", "            elif False:", PYTEST),
 ("T structure: Decimal through another module missed", "tests/repository/test_structure.py", "                or (isinstance(node, ast.Attribute) and node.attr == \"Decimal\")\n", "                or False\n", PYTEST),
 ("T structure: Decimal imported from another module missed", "tests/repository/test_structure.py", "            if alias.name == \"Decimal\"\n        }", "            if alias.name == \"Decimal\" and imported.module == \"decimal\"\n        }", PYTEST),
 ("T structure: cast not a type use", "tests/repository/test_structure.py", "                (name == \"cast\" and parent.args[:1] == [child])\n", "                False\n", PYTEST),
 ("T structure: TypeVar bound not a type use", "tests/repository/test_structure.py", "        and _called_name(call) == \"TypeVar\"\n", "        and False\n", PYTEST),
 ("T structure: type alias statement not a type use", "tests/repository/test_structure.py", "            or (isinstance(parent, ast.TypeAlias) and parent.value is child)\n", "", PYTEST),
 ("T structure: literal_eval off", "tests/repository/test_structure.py", "findings.append(f\"{where}: literal_eval reads numbers as floats\")", "pass", PYTEST),
 ("T structure: complex not a converter", "tests/repository/test_structure.py", "FLOAT_CONVERTERS = frozenset({\"float\", \"complex\"})", "FLOAT_CONVERTERS = frozenset({\"float\"})", PYTEST),
 ("T structure: ValidationError not allowed", "tests/repository/test_structure.py", "{\"Field\", \"AfterValidator\", \"field_validator\", \"ValidationInfo\", \"ValidationError\"}", "{\"Field\", \"AfterValidator\", \"field_validator\", \"ValidationInfo\"}", PYTEST),
 # Gate 3 run 6
 ("C Amount is an assigned alias", "src/atp/contracts/_amount.py", "type Amount = Annotated[Decimal, AmountSchema]", "Amount = Annotated[Decimal, AmountSchema]", PYTEST),
 ("C other type aliases accepted", "src/atp/contracts/_model.py", "    if isinstance(annotation, typing.TypeAliasType) or isinstance(\n        origin, typing.TypeAliasType\n    ):\n", "    if False:\n", PYTEST),
 ("C generic type aliases accepted", "src/atp/contracts/_model.py", "    if isinstance(annotation, typing.TypeAliasType) or isinstance(\n        origin, typing.TypeAliasType\n    ):\n", "    if isinstance(annotation, typing.TypeAliasType):\n", PYTEST),
 ("T structure: a subscript's slice ends the climb", "tests/repository/test_structure.py", "            or (isinstance(parent, ast.MatchClass) and parent.cls is child)\n", "            or (isinstance(parent, ast.MatchClass) and parent.cls is child)\n            or (isinstance(parent, ast.Subscript) and parent.slice is child)\n", PYTEST),
 ("T structure: a case pattern not a type check", "tests/repository/test_structure.py", "            or (isinstance(parent, ast.MatchClass) and parent.cls is child)\n", "", PYTEST),
 ("T structure: a PEP 695 bound not a type use", "tests/repository/test_structure.py", "            or (isinstance(parent, ast.TypeVar) and parent.bound is child)\n", "", PYTEST),
 ("T structure: names from the root not followed", "tests/repository/test_structure.py", "            if imported == \"atp\":\n                yield from ((f\"atp.{name}\", ()) for name in names)\n            else:\n                yield imported, names\n", "            yield imported, names\n", PYTEST),
 ("T structure: attribute paths on the root not followed", "tests/repository/test_structure.py", "            and node.value.id in root_names\n", "            and False\n", PYTEST),
 ("T structure: import atp.numeric does not bind the root", "tests/repository/test_structure.py", "        if alias.name == \"atp\" or (alias.name.startswith(\"atp.\") and not alias.asname)\n", "        if alias.name == \"atp\"\n", PYTEST),
 ("T structure: the root's dunders read as modules", "tests/repository/test_structure.py", "            and not node.attr.startswith(\"__\")\n", "", PYTEST),
 ('T structure: import_module not followed', 'tests/repository/test_structure.py', '        elif (\n            isinstance(node, ast.Call)\n            and _called_name(node) in import_functions\n', '        elif (\n            isinstance(node, ast.Call)\n            and False\n', PYTEST),
 ("T structure: attribute path stops at the first name", "tests/repository/test_structure.py", "                path.append(parent.attr)\n", "                break\n", PYTEST),
 ('C a literal of any values accepted', 'src/atp/contracts/_model.py', '        if any(type(argument) not in (str, type(None)) for argument in arguments):\n', '        if False:\n', PYTEST),
 ('C a literal of integers accepted', 'src/atp/contracts/_model.py', 'type(argument) not in (str, type(None)) for argument', 'type(argument) not in (str, int, type(None)) for argument', PYTEST),
 ('C a literal of booleans accepted', 'src/atp/contracts/_model.py', 'type(argument) not in (str, type(None)) for argument', 'type(argument) not in (str, bool, type(None)) for argument', PYTEST),
 ('C a literal of enum members accepted', 'src/atp/contracts/_model.py', '        if any(type(argument) not in (str, type(None)) for argument in arguments):\n', '        if any(type(argument) not in (str, type(None)) and not isinstance(argument, enum.Enum) for argument in arguments):\n', PYTEST),
 ('C enum values not checked', 'src/atp/contracts/_model.py', '        if not issubclass(annotation, enum.IntEnum) and any(\n', '        if False and any(\n', PYTEST),
 ('C an enum of integers accepted', 'src/atp/contracts/_model.py', '            type(member.value) is not str for member in annotation.__members__.values()\n', '            type(member.value) not in (str, int) for member in annotation.__members__.values()\n', PYTEST),
 ('C an IntEnum refused', 'src/atp/contracts/_model.py', '        if not issubclass(annotation, enum.IntEnum) and any(\n', '        if any(\n', PYTEST),
 ("C outcome names not registered", "src/atp/contracts/_outcome.py", "register_known_names([*OUTCOME_RESULTS, \"result\", \"value\", \"error\"])", "register_known_names([])", PYTEST),
 ("C JSON schema hook redefinable", "src/atp/contracts/_model.py", "        \"__get_pydantic_json_schema__\",\n", "", PYTEST),
 ("T structure: parse_constant not required", "tests/repository/test_structure.py", "(\"parse_float\", \"parse_constant\")", "(\"parse_float\",)", PYTEST),
 ("T structure: an aliased JSONDecoder missed", "tests/repository/test_structure.py", "_called_name(node) in json_decoders", "_called_name(node) == \"JSONDecoder\"", PYTEST),
 ("T structure: __int__ not scanned", "tests/repository/test_structure.py", "        \"__float__\",\n        \"__int__\",\n", "        \"__float__\",\n", PYTEST),
 ("T structure: the operator module's dunder names missed", "tests/repository/test_structure.py", "        \"__floordiv__\",\n        \"__ifloordiv__\",\n", "        \"__ifloordiv__\",\n", PYTEST),
 ("T structure: divide_int not scanned", "tests/repository/test_structure.py", "DIVISION_METHODS = frozenset({\"divide_int\", \"divmod\"})", "DIVISION_METHODS = frozenset({\"divmod\"})", PYTEST),
 ("T structure: divmod as an attribute not scanned", "tests/repository/test_structure.py", "DIVISION_METHODS = frozenset({\"divide_int\", \"divmod\"})", "DIVISION_METHODS = frozenset({\"divide_int\"})", PYTEST),
 ("T structure: __pydantic_validator__ not scanned", "tests/repository/test_structure.py", "    {\n        \"__pydantic_validator__\",\n", "    {\n", PYTEST),
 ("T structure: validate_assignment not scanned", "tests/repository/test_structure.py", "        \"validate_assignment\",\n        \"model_validate\",\n", "        \"model_validate\",\n", PYTEST),
 ("T structure: a type argument of another type is a finding", "tests/repository/test_structure.py", "                return True  # a type argument of another type\n", "                return False  # a type argument of another type\n", PYTEST),
 ("T structure: Annotated's metadata a type use", "tests/repository/test_structure.py", "                return False  # `Annotated`'s metadata\n", "                return True  # `Annotated`'s metadata\n", PYTEST),
 ("T structure: Annotated under another name missed", "tests/repository/test_structure.py", "        if alias.name == name and alias.asname\n", "        if False\n", PYTEST),
 ("T structure: Annotated under its own name missed", "tests/repository/test_structure.py", "    return {name} | {\n", "    return set() | {\n", PYTEST),
 ("T structure: a union is a value", "tests/repository/test_structure.py", "            or (isinstance(parent, ast.BinOp) and isinstance(parent.op, ast.BitOr))\n        ):\n            return True\n", "        ):\n            return True\n", PYTEST),
 ("T structure: NewType not a type use", "tests/repository/test_structure.py", "                or (name == \"NewType\" and parent.args[1:2] == [child])\n", "", PYTEST),
 ("T structure: TypeVar constraints not type uses", "tests/repository/test_structure.py", "                    name in {\"isinstance\", \"issubclass\", \"TypeVar\"}\n", "                    name in {\"isinstance\", \"issubclass\"}\n", PYTEST),
 ("T structure: isinstance not a type check", "tests/repository/test_structure.py", "                    name in {\"isinstance\", \"issubclass\", \"TypeVar\"}\n", "                    name in {\"TypeVar\"}\n", PYTEST),
 ("T structure: an is comparison a value", "tests/repository/test_structure.py", "                isinstance(parent, ast.Compare)\n                and all(", "                False\n                and all(", PYTEST),
 ("T structure: tuples not climbed", "tests/repository/test_structure.py", "        elif not isinstance(parent, ast.Tuple | ast.List):\n", "        elif not isinstance(parent, ast.List):\n", PYTEST),
 ("T structure: lists not climbed", "tests/repository/test_structure.py", "        elif not isinstance(parent, ast.Tuple | ast.List):\n", "        elif not isinstance(parent, ast.Tuple):\n", PYTEST),
 # Gate 3 run 7
 ("T structure: Annotated not followed", "tests/repository/test_structure.py", "            if _subscript_of(parent, annotated):\n", "            if False:\n", PYTEST),
 ("T structure: a one-member Union not followed", "tests/repository/test_structure.py", "            elif _subscript_of(parent, unions) and not isinstance(child, ast.Tuple):\n", "            elif False:\n", PYTEST),
 ("T structure: a union of several members followed", "tests/repository/test_structure.py", "            elif _subscript_of(parent, unions) and not isinstance(child, ast.Tuple):\n", "            elif _subscript_of(parent, unions):\n", PYTEST),
 ("T structure: typing.Annotated missed", "tests/repository/test_structure.py", "        isinstance(value, ast.Attribute) and value.attr in names\n", "        False\n", PYTEST),
 ("T structure: an annotated assignment not a type use", "tests/repository/test_structure.py", "            or (isinstance(parent, ast.AnnAssign) and parent.annotation is child)\n", "", PYTEST),
 ("T structure: builtins.float not a converter", "tests/repository/test_structure.py", "                and node.value.id in builtins_modules\n                and _used_as_converter(node, parents)\n", "                and False\n", PYTEST),
 ("T structure: imports from builtins allowed", "tests/repository/test_structure.py", "                    if alias.name in ROUNDING_BUILTINS\n", "                    if False\n", PYTEST),
 ("T structure: attributes of float allowed", "tests/repository/test_structure.py", "                and node.value.id in FLOAT_CONVERTERS\n            ):\n", "                and False\n            ):\n", PYTEST),
 ("T structure: locale.str not text", "tests/repository/test_structure.py", "        \"__format__\",\n        \"str\",\n", "        \"__format__\",\n", PYTEST),
 ("T structure: import_module of pydantic missed", "tests/repository/test_structure.py", "                and node.args[0].value.split(\".\")[0] in {\"pydantic\", \"pydantic_core\"}\n", "                and False\n", PYTEST),
 ("T structure: import_module under another name missed", "tests/repository/test_structure.py", "    return {\"import_module\", \"__import__\"} | _imported_names(\n        tree, \"importlib\", \"import_module\"\n    )\n", "    return {\"import_module\", \"__import__\"}\n", PYTEST),
 ('C metadata not taken off union members', 'src/atp/contracts/_model.py', '    while typing.get_origin(annotation) is Annotated:\n        annotation = typing.get_args(annotation)[0]\n    if typing.get_origin(annotation) in (typing.Union, types.UnionType):\n        return [\n', '    if typing.get_origin(annotation) in (typing.Union, types.UnionType):\n        return [\n', PYTEST),
 ("C anything beside an amount", "src/atp/contracts/_model.py", "    return annotation is type(None) or (\n        typing.get_origin(annotation) is Literal\n", "    return True or (\n        typing.get_origin(annotation) is Literal\n", PYTEST),
 ("C a literal of any values beside an amount", "src/atp/contracts/_model.py", "        and all(type(value) is str for value in typing.get_args(annotation))\n", "        and True\n", PYTEST),
 ("C text bound on an amount accepted", "src/atp/contracts/_model.py", "    return type(value) is int or (type(value) is Decimal and value.is_finite())\n", "    return type(value) is not float\n", PYTEST),
 ("C non-finite bound on an amount accepted", "src/atp/contracts/_model.py", "    return type(value) is int or (type(value) is Decimal and value.is_finite())\n", "    return type(value) is int or type(value) is Decimal\n", PYTEST),
 ("C field metadata read through a rebuilt Annotated", "src/atp/contracts/_model.py", "        _refuse_annotated(field.annotation, field.metadata, where)\n", "        _refuse_annotated(field.annotation, typing.get_args(Annotated[field.annotation, *field.metadata])[1:] if field.metadata else (), where)\n", PYTEST),
 ("C an enum's own _missing_ allowed", "src/atp/contracts/_model.py", "            \"_missing_\" in vars(klass)\n", "            False\n", PYTEST),
 ("C Flag's own _missing_ excluded", 'src/atp/contracts/_model.py', '            if klass is not enum.Enum\n', '            if klass not in (enum.Enum, enum.Flag)\n', PYTEST),
 ("C json_schema_extra not checked", "src/atp/contracts/_model.py", "    if extra is not None and (\n", "    if False and (\n", PYTEST),
 ("C json_schema_extra keys not checked", "src/atp/contracts/_model.py", "        or not all(str(key).startswith(\"x-\") for key in extra)\n", "", PYTEST),
 ("E a reused type keeps any message", "src/atp/contracts/_errors.py", "        if rendered.errors(include_url=False)[0][\"msg\"] == message:\n", "        if True:\n", PYTEST),
 ("E the kernel's messages not kept", "src/atp/contracts/_errors.py", "    if (kind, message) in _kernel_messages:\n        return True\n", "", PYTEST),
 ("E a kernel type keeps any message", "src/atp/contracts/_errors.py", "    if (kind, message) in _kernel_messages:\n", "    if kind in {known for known, _ in _kernel_messages}:\n", PYTEST),
 ("E Pydantic's JSON wording not recognized", "src/atp/contracts/_errors.py", "_INPUT_TYPES: Final[tuple[Literal[\"python\", \"json\"], ...]] = (\"python\", \"json\")\n", "_INPUT_TYPES: Final[tuple[Literal[\"python\", \"json\"], ...]] = (\"python\",)\n", PYTEST),
 ("N a refusal text not listed", "src/atp/numeric/_amount.py", "    {_NOT_IN_TEXT_FORM, _EXPONENT_OUT_OF_RANGE, _NOT_FINITE, _TOO_MANY_DIGITS}\n", "    {_NOT_IN_TEXT_FORM, _EXPONENT_OUT_OF_RANGE, _TOO_MANY_DIGITS}\n", PYTEST),
 # Gate 3 run 7 follow-up: metadata is written as Field(...) or AfterValidator(...), exactly
 ("C written metadata read from the merged annotation", "src/atp/contracts/_model.py", "        written = field._original_annotation  # noqa: SLF001\n", "        written = field.annotation\n", PYTEST),
 ("C written metadata not checked inside a type", "src/atp/contracts/_model.py", "        _refuse_written_metadata(metadata, where)\n        _refuse_annotated(base, metadata, where)\n", "        _refuse_annotated(base, metadata, where)\n", PYTEST),
 ("C a subclass accepted where metadata is written", "src/atp/contracts/_model.py", "        if type(item) not in (FieldInfo, AfterValidator):\n", "        if not isinstance(item, FieldInfo | AfterValidator):\n", PYTEST),
 ("C a constraint object written directly accepted", "src/atp/contracts/_model.py", "        if type(item) not in (FieldInfo, AfterValidator):\n", "        if type(item) not in (FieldInfo, AfterValidator, *_CONSTRAINT_TYPES):\n", PYTEST),
 ("C an AfterValidator subclass accepted inside a Field", "src/atp/contracts/_model.py", "    if type(item) is AfterValidator:\n        return\n", "    if isinstance(item, AfterValidator):\n        return\n", PYTEST),
 ("C a subclass of a listed constraint accepted inside a Field", "src/atp/contracts/_model.py", "    if type(item) in _CONSTRAINT_TYPES and (\n", "    if isinstance(item, tuple(_CONSTRAINT_TYPES)) and (\n", PYTEST),
 # Gate 3 run 8
 ("C a Field inside a type skips the settings list", "src/atp/contracts/_model.py", "        _refuse_field_settings(item, where)\n        for inner in item.metadata:\n", "        for inner in item.metadata:\n", PYTEST),
 ("C an inherited _missing_ allowed", "src/atp/contracts/_model.py", "            for klass in annotation.__mro__\n", "            for klass in (annotation,)\n", PYTEST),
 ("C a subclass of text or Decimal reaches amount()", "src/atp/contracts/_amount.py", "    if type(value) is not str and type(value) is not Decimal:", "    if not isinstance(value, str | Decimal):", PYTEST),
 # Gate 3 run 9
 ("E schema context left out", "src/atp/contracts/_errors.py", "include_context=True", "include_context=False", PYTEST),
 # Gate 3 run 10: union kinds, literal and enum values, keys in defaults
 ('C union kinds not checked', 'src/atp/contracts/_model.py', '            _refuse_ambiguous_union(arguments, where)\n', '            pass\n', PYTEST),
 ('C two members of one kind allowed', 'src/atp/contracts/_model.py', '    if any(len(bases) > 1 for bases in plain.values()):\n', '    if any(len(bases) > 2 for bases in plain.values()):\n', PYTEST),
 ('C null counted as a kind', 'src/atp/contracts/_model.py', '            for kind in _written_kinds(base) - {"null"}:\n', '            for kind in _written_kinds(base):\n', PYTEST),
 ('C a literal beside any member written as text', 'src/atp/contracts/_model.py', '    if beside and not all(_literal_beside(beside[0], text) for text in texts):\n', '    if False:\n', PYTEST),
 ("C a literal in an amount's text form beside an amount", 'src/atp/contracts/_model.py', '        return re.fullmatch(AMOUNT_PATTERN, text) is None\n', '        return True\n', PYTEST),
 ('C a literal beside any type written as text', 'src/atp/contracts/_model.py', '    return base is str\n', '    return True\n', PYTEST),
 ('C a literal refused beside str', 'src/atp/contracts/_model.py', '    return base is str\n', '    return False\n', PYTEST),
 ("C a union member's metadata not unwrapped", 'src/atp/contracts/_model.py', '        while typing.get_origin(base) is Annotated:\n            base = typing.get_args(base)[0]\n        if typing.get_origin(base) is Literal:\n', '        if typing.get_origin(base) is Literal:\n', PYTEST),
 ('C nested metadata not unwrapped in written kinds', 'src/atp/contracts/_model.py', '    while typing.get_origin(annotation) is Annotated:\n        annotation = typing.get_args(annotation)[0]\n    origin = typing.get_origin(annotation)\n    arguments = typing.get_args(annotation)\n    if origin is Literal:\n        return frozenset("null"', '    origin = typing.get_origin(annotation)\n    arguments = typing.get_args(annotation)\n    if origin is Literal:\n        return frozenset("null"', PYTEST),
 ('C literal values written as null', 'src/atp/contracts/_model.py', '        return frozenset("null" if value is None else "string" for value in arguments)\n', '        return frozenset({"null"})\n', PYTEST),
 ("C a nested union's kinds not read", 'src/atp/contracts/_model.py', '        return frozenset().union(*(_written_kinds(argument) for argument in arguments))\n', '        return frozenset({"string"})\n', PYTEST),
 ('C a frozenset not written as an array', 'src/atp/contracts/_model.py', '    if origin in (tuple, frozenset):\n        return frozenset({"array"})\n', '    if origin in (tuple,):\n        return frozenset({"array"})\n', PYTEST),
 ('C an outcome not written as an object', 'src/atp/contracts/_model.py', '    if origin is Outcome or (\n        isinstance(annotation, type) and issubclass(annotation, Contract)\n    ):\n        return frozenset({"object"})\n', '    if isinstance(annotation, type) and issubclass(annotation, Contract):\n        return frozenset({"object"})\n', PYTEST),
 ('C a contract not written as an object', 'src/atp/contracts/_model.py', '    if origin is Outcome or (\n        isinstance(annotation, type) and issubclass(annotation, Contract)\n    ):\n        return frozenset({"object"})\n', '    if origin is Outcome:\n        return frozenset({"object"})\n', PYTEST),
 ('C a bool written as a number', 'src/atp/contracts/_model.py', '    if annotation is bool:\n        return frozenset({"bool"})\n', '    if annotation is bool:\n        return frozenset({"number"})\n', PYTEST),
 ('C a float not written as a number', 'src/atp/contracts/_model.py', '    if annotation in (int, float) or (\n', '    if annotation in (int,) or (\n', PYTEST),
 ('C an IntEnum not written as a number', 'src/atp/contracts/_model.py', '        isinstance(annotation, type) and issubclass(annotation, enum.IntEnum)\n    ):\n        return frozenset({"number"})\n', '        False\n    ):\n        return frozenset({"number"})\n', PYTEST),
 ('C None not written as null', 'src/atp/contracts/_model.py', '    if annotation is type(None):\n        return frozenset({"null"})\n    return frozenset({"string"})\n', '    return frozenset({"string"})\n', PYTEST),
 # Gate 3 run 11's first launch (stopped at the usage limit): its probes showed keys written as text, keys in unions, and nested amount unions
 ("C a key's field type not checked for defaults", 'src/atp/contracts/_model.py', '        if _can_hold_key(field.annotation) and not _shares_nothing(field.default):\n', '        if False:\n', PYTEST),
 ('C the key itself not seen in a type', 'src/atp/contracts/_model.py', '    if annotation is IdempotencyKey:\n        return True\n', '    if annotation is IdempotencyKey:\n        return False\n', PYTEST),
 ("C a contract's key fields not seen", 'src/atp/contracts/_model.py', '        return any(\n            _can_hold_key(field.annotation)\n', '        return False and any(\n            _can_hold_key(field.annotation)\n', PYTEST),
 ('C keys inside other types not seen', 'src/atp/contracts/_model.py', '    return any(_can_hold_key(argument) for argument in typing.get_args(annotation))\n', '    return False\n', PYTEST),
 ("C None refused as a key field's default", 'src/atp/contracts/_model.py', '        or default is None\n', '', PYTEST),
 ("C an empty collection refused as a key field's default", 'src/atp/contracts/_model.py', '        or (type(default) in (tuple, frozenset) and not default)\n', '', PYTEST),
 ("C any collection allowed as a key field's default", 'src/atp/contracts/_model.py', '        or (type(default) in (tuple, frozenset) and not default)\n', '        or type(default) in (tuple, frozenset)\n', PYTEST),
 ('C a field without a default refused', 'src/atp/contracts/_model.py', '        default is PydanticUndefined\n        or default is None\n', '        default is None\n', PYTEST),
 ('C a union inside metadata not taken apart', 'src/atp/contracts/_model.py', '    if typing.get_origin(annotation) in (typing.Union, types.UnionType):\n        return [\n            member\n', '    if False:\n        return [\n            member\n', PYTEST),
 ('C the amount and key union rules given the direct members', 'src/atp/contracts/_model.py', '        _refuse_written_as_text_beside_others(_union_members(annotation), where)\n', '        _refuse_written_as_text_beside_others(arguments, where)\n', PYTEST),
 ('C a key beside anything in a union', 'src/atp/contracts/_model.py', '    if any(member is IdempotencyKey for member in members) and not all(\n', '    if False and all(\n', PYTEST),
 ('C a key refused beside None', 'src/atp/contracts/_model.py', '        member is IdempotencyKey or member is type(None) for member in members\n', '        member is IdempotencyKey for member in members\n', PYTEST),
]

failures = []
only = os.environ.get('ONLY')
if only:
    M = [m for m in M if m[0].startswith(tuple(only.split(',')))]
part = os.environ.get('SLICE')  # "k/n": every n-th mutation, starting at the k-th
if part:
    k, n = (int(x) for x in part.split('/'))
    M = [m for i, m in enumerate(M) if i % n == k]
for name, rel, old, new, cmd in M:
    path = ROOT / rel
    original = path.read_text(encoding="utf-8")
    if original.count(old) != 1:
        print(f"SKIPPED (pattern count {original.count(old)}): {name}")
        failures.append(name)
        continue
    path.write_text(original.replace(old, new), encoding="utf-8")
    try:
        # A mutation that does not parse would fail every test and look caught.
        parsed = subprocess.run(["uv", "run", "--locked", "python", "-c", "import ast, sys; ast.parse(open(sys.argv[1], encoding='utf-8').read())", str(path)], cwd=ROOT, capture_output=True, text=True)
        if parsed.returncode != 0:
            print("INVALID ", name)
            failures.append(name)
            continue
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=600)
    finally:
        path.write_text(original, encoding="utf-8")
    killed = result.returncode != 0
    print(("KILLED  " if killed else "SURVIVED"), name)
    if not killed:
        failures.append(name)
print(f"{len(M) - len(failures)} of {len(M)} mutations killed")
# a final sanity run: the unmutated copy passes
final = subprocess.run(PYTEST, cwd=ROOT, capture_output=True, text=True)
print("unmutated copy:", "PASS" if final.returncode == 0 else "FAIL")
if final.returncode:
    print(final.stdout[-3000:])
```
