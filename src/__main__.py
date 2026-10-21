import sys

from .greet import greet


def main(argv: list[str] | None = None) -> None:
    args = sys.argv[1:] if argv is None else argv
    name = args[0] if args else "Hassan"
    print(greet(name))


if __name__ == "__main__":
    main()
