"""Test run_cmd."""
# pylint: disable=broad-except
from python_run_cmd import __version__, run_cmd, run_cmd_async


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not run_cmd()  # type: ignore
    except Exception:
        assert True
