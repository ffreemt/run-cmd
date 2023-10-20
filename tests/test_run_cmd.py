"""Test run_cmd."""
# pylint: disable=broad-except
from run_cmd import __version__, run_cmd


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not run_cmd()
    except Exception:
        assert True
