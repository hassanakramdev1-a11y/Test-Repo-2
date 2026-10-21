"""Simple greeting helpers."""


def greet(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"
