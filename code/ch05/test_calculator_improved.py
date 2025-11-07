"""
Comprehensive test suite for calculator module with high coverage.

This demonstrates best practices for thorough testing, achieving ~95%+ coverage.
Tests include happy paths, edge cases, and error conditions.
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


class TestAddition:
    """Comprehensive tests for addition."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5

    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtraction:
    """Comprehensive tests for subtraction."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(5, -3) == 8

    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiplication:
    """Comprehensive tests for multiplication."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(4, 5) == 20
        assert multiply(3, 7) == 21

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-4, 5) == -20
        assert multiply(-4, -5) == 20

    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_multiply_with_one(self):
        """Test multiplying with one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5


class TestDivision:
    """Comprehensive tests for division."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, 2) == -5
        assert divide(10, -2) == -5
        assert divide(-10, -2) == 5

    def test_divide_with_remainder(self):
        """Test division with remainder."""
        assert divide(7, 2) == 3.5
        assert divide(5, 4) == 1.25

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestPower:
    """Comprehensive tests for power function."""

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(3, 4) == 81

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        assert power(5, 0) == 1
        assert power(100, 0) == 1

    def test_power_exponent_one(self):
        """Test power with exponent of one."""
        assert power(5, 1) == 5
        assert power(7, 1) == 7

    def test_power_negative_exponent_raises_error(self):
        """Test that negative exponent raises ValueError."""
        with pytest.raises(ValueError, match="Negative exponents not supported"):
            power(2, -1)


class TestFactorial:
    """Comprehensive tests for factorial function."""

    def test_factorial_positive_numbers(self):
        """Test factorial with positive numbers."""
        assert factorial(5) == 120
        assert factorial(3) == 6
        assert factorial(4) == 24

    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial(1) == 1

    def test_factorial_negative_raises_error(self):
        """Test that negative factorial raises ValueError."""
        with pytest.raises(
            ValueError, match="Factorial not defined for negative numbers"
        ):
            factorial(-1)
        with pytest.raises(ValueError):
            factorial(-5)


class TestIsEven:
    """Comprehensive tests for is_even function."""

    def test_even_numbers(self):
        """Test that even numbers return True."""
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(100) is True
        assert is_even(0) is True

    def test_odd_numbers(self):
        """Test that odd numbers return False."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False

    def test_negative_even_numbers(self):
        """Test negative even numbers."""
        assert is_even(-2) is True
        assert is_even(-4) is True

    def test_negative_odd_numbers(self):
        """Test negative odd numbers."""
        assert is_even(-1) is False
        assert is_even(-3) is False


class TestAbsoluteValue:
    """Comprehensive tests for absolute_value function."""

    def test_positive_numbers(self):
        """Test absolute value of positive numbers."""
        assert absolute_value(5) == 5
        assert absolute_value(10) == 10

    def test_negative_numbers(self):
        """Test absolute value of negative numbers."""
        assert absolute_value(-5) == 5
        assert absolute_value(-10) == 10

    def test_zero(self):
        """Test absolute value of zero."""
        assert absolute_value(0) == 0

    def test_floats(self):
        """Test absolute value with floats."""
        assert absolute_value(3.14) == 3.14
        assert absolute_value(-3.14) == 3.14


class TestCalculatePercentage:
    """Comprehensive tests for calculate_percentage function."""

    def test_basic_percentage(self):
        """Test basic percentage calculations."""
        assert calculate_percentage(25, 100) == 25.0
        assert calculate_percentage(50, 200) == 25.0
        assert calculate_percentage(75, 100) == 75.0

    def test_percentage_over_100(self):
        """Test when value exceeds total."""
        assert calculate_percentage(150, 100) == 150.0

    def test_percentage_with_floats(self):
        """Test percentage with float values."""
        assert calculate_percentage(33.33, 100) == pytest.approx(33.33)

    def test_zero_value(self):
        """Test percentage when value is zero."""
        assert calculate_percentage(0, 100) == 0.0

    def test_zero_total_raises_error(self):
        """Test that zero total raises ValueError."""
        with pytest.raises(ValueError, match="Total cannot be zero"):
            calculate_percentage(50, 0)


# Parametrized tests for efficiency
class TestParametrizedExamples:
    """Examples of parametrized tests for better coverage."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (1, 1, 2),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
        ],
    )
    def test_add_parametrized(self, a, b, expected):
        """Parametrized test for addition."""
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, True),
            (2, True),
            (4, True),
            (1, False),
            (3, False),
            (5, False),
        ],
    )
    def test_is_even_parametrized(self, n, expected):
        """Parametrized test for is_even."""
        assert is_even(n) == expected
