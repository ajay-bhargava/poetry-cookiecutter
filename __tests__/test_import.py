"""Test Poetry Cookiecutter."""

import poetry_cookiecutter


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(poetry_cookiecutter.__name__, str)
