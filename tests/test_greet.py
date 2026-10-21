from io import StringIO
from unittest.mock import patch

import pytest

from src.__main__ import main
from src.greet import greet


def test_greet_returns_hello_name() -> None:
    assert greet("Hassan") == "Hello, Hassan!"


def test_greet_strips_whitespace() -> None:
    assert greet("  Ada  ") == "Hello, Ada!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError):
        greet("   ")


def test_main_uses_cli_name() -> None:
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        main(["Ada"])
    assert stdout.getvalue() == "Hello, Ada!\n"


def test_main_defaults_to_hassan() -> None:
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        main([])
    assert stdout.getvalue() == "Hello, Hassan!\n"
