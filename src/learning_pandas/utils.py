"""Utility functions for the learning_pandas package."""


def greet(name: str = "Learner") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to Learning Pandas."


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()