import lib_template
from typer.testing import CliRunner

runner = CliRunner(mix_stderr=False)


def test_cli_version():
    result = runner.invoke(lib_template.cli.app, "--version")
    assert result.exit_code == 0
    assert "lib-template" in result.stdout


def test_cli_license():
    result = runner.invoke(lib_template.cli.app, "--license")
    assert result.exit_code == 0
    assert "MIT" in result.stdout
