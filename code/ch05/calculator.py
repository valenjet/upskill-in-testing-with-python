"""
Calculator module for demonstrating code coverage with pytest-cov.

This module provides basic arithmetic operations and demonstrates
various code paths for coverage analysis.
"""


def add(a, b):
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        The difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        The quotient of a divided by b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """
    Raise base to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        base raised to the power of exponent

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
    """
    if exponent < 0:
        raise ValueError("Negative exponents not supported")

    result = 1
    for _ in range(exponent):
        result *= base
    return result


def factorial(n):
    """
    Calculate the factorial of n.

    Args:
        n: Non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        ValueError: If n is negative

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n):
    """
    Check if a number is even.

    Args:
        n: Integer to check

    Returns:
        True if n is even, False otherwise
    """
    return n % 2 == 0


def absolute_value(n):
    """
    Calculate the absolute value of a number.

    Args:
        n: Number (int or float)

    Returns:
        The absolute value of n
    """
    if n < 0:
        return -n
    return n


def calculate_percentage(value, total):
    """
    Calculate what percentage value is of total.

    Args:
        value: The value to calculate percentage for
        total: The total amount

    Returns:
        The percentage (0-100)

    Raises:
        ValueError: If total is zero

    Examples:
        >>> calculate_percentage(25, 100)
        25.0
        >>> calculate_percentage(50, 200)
        25.0
    """
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (value / total) * 100
