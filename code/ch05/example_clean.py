"""
Example module demonstrating clean, PEP 8 compliant code.
This is the corrected version of example_with_linting_issues.py
"""

import math


# Follow naming conventions: constants in UPPERCASE
GLOBAL_VARIABLE = 100
ANOTHER_GLOBAL_VARIABLE = 200


def calculate_total(x, y, z):
    """
    Calculate total with proper formatting.

    Args:
        x: First number
        y: Second number
        z: Third number

    Returns:
        Sum of x, y, and z
    """
    result = x + y + z
    return result


def process_data(data):
    """
    Process data with proper style.

    Args:
        data: Data to process (should be convertible to int or boolean)

    Returns:
        Processed result as string or integer
    """
    # Separate statements on different lines
    x = 1
    y = 2
    z = 3

    # Split long lines appropriately
    very_long_variable_name = (
        "This string is split across multiple lines "
        "to keep line length under 79 characters"
    )

    # Use truthiness directly (Pythonic way)
    if data:
        return "yes"

    # Specify exception type
    try:
        result = int(data)
    except (ValueError, TypeError):
        result = 0

    return result


class MyClass:
    """Example class following PEP 8 conventions."""

    def __init__(self, value):
        """
        Initialize MyClass with a value.

        Args:
            value: Initial value to store
        """
        self.value = value

    def get_value(self):
        """
        Get the current value.

        Returns:
            Current value
        """
        return self.value

    def set_value(self, new_value):
        """
        Set a new value.

        Args:
            new_value: New value to store
        """
        self.value = new_value


def function_with_no_trailing_whitespace():
    """This function has no trailing whitespace."""
    x = 1
    y = 2
    return x + y


def used_imports_example():
    """Function that uses only necessary imports."""
    return math.sqrt(16)


# Proper indentation in dictionary
config = {
    'name': 'example',
    'version': '1.0',
    'debug': True
}


# Use def instead of lambda for named functions
def multiply(x, y):
    """
    Multiply two numbers.

    Args:
        x: First number
        y: Second number

    Returns:
        Product of x and y
    """
    return x * y


# Use == for value comparison
def check_status(status):
    """
    Check if status is active.

    Args:
        status: Status string to check

    Returns:
        True if status is "active", False otherwise
    """
    if status == "active":
        return True
    return False


def another_function():
    """Another function with proper spacing."""
    pass


def properly_spaced_function():
    """This function uses only spaces for indentation."""
    return "consistent spacing"


def final_function():
    """Final function with proper ending."""
    return "proper newline at end"
