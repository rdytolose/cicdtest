"""A small example for testing pull request automation."""


def greet(name: str = "world") -> str:
    """Return a greeting, using 'world' for a blank name."""
    return f"Hello, {name.strip() or 'world'}!"


if __name__ == "__main__":
    print(greet())
