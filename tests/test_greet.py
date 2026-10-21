import pytest

from src.greet import greet


def test_greet_returns_hello_name() -> None:
    assert greet("Hassan") == "Hello, Hassan!"


def test_greet_strips_whitespace() -> None:
    assert greet("  Ada  ") == "Hello, Ada!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError):
        greet("   ")
