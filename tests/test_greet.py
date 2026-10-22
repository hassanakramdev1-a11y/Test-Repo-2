from io import StringIO
from unittest.mock import patch

import pytest

from src.__main__ import main
from src.greet import greet


def test_greet_returns_hello_name() -> None:
    assert greet("Hassan") == "Hello, Hassan!"


def test_greet_strips_whitespace() -> None:
    assert greet("  Adam  ") == "Hello, Adam!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError):
        greet("   ")


def test_main_uses_cli_name() -> None:
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        main(["Adam"])
    assert stdout.getvalue() == "Hello, Adam!\n"


def test_main_defaults_to_hassan() -> None:
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        main([])
    assert stdout.getvalue() == "Hello, Hassan!\n"
