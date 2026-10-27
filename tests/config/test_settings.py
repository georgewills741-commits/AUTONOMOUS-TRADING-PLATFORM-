"""The configuration contracts (MIG-010, MIG-027, OPS-004, MODE-006, SEC-004, SEC-005)."""

from __future__ import annotations

import pytest

from atp.config import (
    Environment,
    EnvironmentConfiguration,
    PortableConfiguration,
    SecretDeclaration,
    SecretKind,
)
from atp.contracts import ContractError

# Assembled at run time so that no file holds a credential-shaped sample.
SECRET = "sk" + "_live_" + "Q7x9Z2" + "secretvalue"


def _environment(name: str, *secrets: tuple[str, str]) -> str:
    declared = ",".join(f'{{"name":"{n}","kind":"{k}"}}' for n, k in secrets)
    return (
        f'{{"environment":"{name}","environment_id":"example-{name}",'
        f'"secrets":[{declared}]}}'
    )


def _types(error: pytest.ExceptionInfo[ContractError]) -> list[str]:
    return [detail.type for detail in error.value.details]


@pytest.mark.req("OPS-004")
def test_the_six_environments_are_those_of_ops_004() -> None:
    assert [environment.value for environment in Environment] == [
        "development",
        "testing",
        "research",
        "paper",
        "staging",
        "production",
    ]


def test_the_secret_kinds_are_a_closed_set() -> None:
    assert {kind.value for kind in SecretKind} == {"trading", "ai", "server"}
    with pytest.raises(ContractError) as error:
        SecretDeclaration.from_json('{"name":"ATP_X","kind":"transfer"}')
    assert _types(error) == ["enum"]


@pytest.mark.parametrize("platform_id", ["example-platform", "atp", "a1-b2-c3", "x9"])
@pytest.mark.req("MIG-027")
def test_a_platform_identifier_is_lowercase_parts_joined_by_hyphens(
    platform_id: str,
) -> None:
    portable = PortableConfiguration.from_json(f'{{"platform_id":"{platform_id}"}}')
    assert portable.platform_id == platform_id


@pytest.mark.parametrize(
    "platform_id",
    ["", "Example", "1atp", "-atp", "atp-", "atp--x", "atp_x", "atp x", "atp\\n", "é"],
)
def test_a_malformed_identifier_is_refused(platform_id: str) -> None:
    with pytest.raises(ContractError) as error:
        PortableConfiguration.from_json(f'{{"platform_id":"{platform_id}"}}')
    assert _types(error) == ["string_pattern_mismatch"]
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(
            f'{{"environment":"paper","environment_id":"{platform_id}"}}'
        )
    assert _types(error) == ["string_pattern_mismatch"]


@pytest.mark.parametrize(
    "name", ["", "atp_x", "1ATP", "_ATP", "ATP-X", "ATP X", "ATP\\n"]
)
def test_a_malformed_secret_name_is_refused(name: str) -> None:
    with pytest.raises(ContractError) as error:
        SecretDeclaration.from_json(f'{{"name":"{name}","kind":"server"}}')
    assert _types(error) == ["string_pattern_mismatch"]


@pytest.mark.parametrize(
    ("text", "types"),
    [
        ("{}", ["missing"]),
        ('{"platform_id":7}', ["string_type"]),
        ('{"platform_id":"atp","extra":1}', ["extra_forbidden"]),
    ],
)
@pytest.mark.req("MIG-010")
def test_a_missing_unknown_or_mistyped_portable_setting_is_refused(
    text: str, types: list[str]
) -> None:
    with pytest.raises(ContractError) as error:
        PortableConfiguration.from_json(text)
    assert _types(error) == types


@pytest.mark.parametrize(
    ("text", "types"),
    [
        ('{"environment_id":"x"}', ["missing"]),
        ('{"environment":"paper"}', ["missing"]),
        ('{"environment":"prod","environment_id":"x"}', ["enum"]),
        ('{"environment":"Paper","environment_id":"x"}', ["enum"]),
        ('{"environment":"paper","environment_id":"x","secrets":{}}', ["tuple_type"]),
        (
            '{"environment":"paper","environment_id":"x","host":"h"}',
            ["extra_forbidden"],
        ),
    ],
)
@pytest.mark.req("MIG-010")
def test_a_missing_unknown_or_mistyped_environment_setting_is_refused(
    text: str, types: list[str]
) -> None:
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(text)
    assert _types(error) == types


@pytest.mark.req("SEC-005")
def test_a_secret_declaration_holds_no_value() -> None:
    text = f'{{"name":"ATP_X","kind":"server","value":"{SECRET}"}}'
    with pytest.raises(ContractError) as error:
        SecretDeclaration.from_json(text)
    assert _types(error) == ["extra_forbidden"]
    assert SECRET not in str(error.value)
    assert SECRET not in error.value.to_json()


def test_secrets_are_optional_and_held_as_a_tuple() -> None:
    bare = EnvironmentConfiguration.from_json(
        '{"environment":"paper","environment_id":"x"}'
    )
    assert bare.secrets == ()
    declared = EnvironmentConfiguration.from_json(
        _environment("paper", ("ATP_A", "server"), ("ATP_B", "ai"))
    )
    assert declared.secrets == (
        SecretDeclaration(name="ATP_A", kind=SecretKind.SERVER),
        SecretDeclaration(name="ATP_B", kind=SecretKind.AI),
    )


@pytest.mark.parametrize(
    "environment", [e.value for e in Environment if e is not Environment.PRODUCTION]
)
@pytest.mark.req("MODE-006", "SEC-004")
def test_a_trading_credential_is_refused_outside_production(environment: str) -> None:
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(
            _environment(environment, ("ATP_A", "server"), ("ATP_T", "trading"))
        )
    assert _types(error) == ["trading_credential_outside_production"]


def test_a_trading_credential_is_refused_when_the_environment_is_invalid() -> None:
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(_environment("prod", ("ATP_T", "trading")))
    assert sorted(_types(error)) == ["enum", "trading_credential_outside_production"]


def test_a_trading_credential_is_accepted_in_production() -> None:
    production = EnvironmentConfiguration.from_json(
        _environment("production", ("ATP_T", "trading"))
    )
    assert production.secrets[0].kind is SecretKind.TRADING


def test_the_rule_holds_for_a_contract_built_in_code_too() -> None:
    with pytest.raises(ValueError, match="trading_credential_outside_production"):
        EnvironmentConfiguration(
            environment=Environment.PAPER,
            environment_id="x",
            secrets=(SecretDeclaration(name="ATP_T", kind=SecretKind.TRADING),),
        )


def test_a_secret_declared_twice_is_refused() -> None:
    with pytest.raises(ContractError) as error:
        EnvironmentConfiguration.from_json(
            _environment("production", ("ATP_A", "server"), ("ATP_A", "ai"))
        )
    assert _types(error) == ["duplicate_secret_name"]


def test_a_refused_value_is_not_in_the_error() -> None:
    with pytest.raises(ContractError) as error:
        PortableConfiguration.from_json(f'{{"platform_id":"{SECRET}"}}')
    assert SECRET not in str(error.value)
    with pytest.raises(ContractError) as error:
        PortableConfiguration.from_json(f'{{"platform_id":"atp","{SECRET}":1}}')
    assert SECRET not in str(error.value)
    assert SECRET not in error.value.to_json()
