"""
Basic test suite for calculator module with incomplete coverage.

This demonstrates what happens when you don't test all code paths.
Coverage will be around 50-60%.
"""

import pytest
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    factorial,
    is_even,
    absolute_value,
    calculate_percentage,
)


class TestBasicArithmetic:
    """Test basic arithmetic operations."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(4, 5) == 20

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5


class TestPowerAndFactorial:
    """Test power and factorial functions."""

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2, 3) == 8

    def test_factorial_positive_number(self):
        """Test factorial with positive number."""
        assert factorial(5) == 120


# Note: Missing tests for:
# - Edge cases (zero, negative numbers)
# - Error conditions (divide by zero, negative factorial)
# - is_even function (not tested at all)
# - absolute_value function (not tested at all)
# - calculate_percentage function (not tested at all)
# - power with zero exponent
# - factorial of 0 and 1
