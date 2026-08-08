def factorial(n: int) -> int:
    """Return the factorial of n using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python factorial_recursive.py <non-negative-integer>")
        sys.exit(1)

    try:
        value = int(sys.argv[1])
        print(factorial(value))
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
