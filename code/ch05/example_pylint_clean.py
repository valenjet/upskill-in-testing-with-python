"""Example module demonstrating pylint best practices.

This module shows the same functionality as example_with_pylint_issues.py
but refactored to address all pylint warnings and achieve a high quality score.
"""

# Global constant following naming convention
MY_GLOBAL_VAR = 42


def process_user_data(name, city, state):
    """Process user data with reasonable number of arguments.

    Args:
        name: User's full name
        city: User's city
        state: User's state

    Returns:
        Formatted string with user information
    """
    return f"{name} from {city}, {state}"


def calculate_result(x, y):
    """Calculate result with reasonable complexity.

    Args:
        x: First number
        y: Second number

    Returns:
        Calculated result
    """
    sum_xy = x + y
    diff_xy = x - y
    product_xy = x * y
    quotient_xy = x / y if y != 0 else 0

    # Combine operations meaningfully
    intermediate = (sum_xy + diff_xy) * (product_xy + quotient_xy)
    result = intermediate + 100

    return result


class DataProcessor:
    """Process data with transformation operations.

    Attributes:
        data: Input data to process
        result: Processed result
    """

    def __init__(self, data):
        """Initialize processor with data.

        Args:
            data: List of items to process
        """
        self.data = data
        self.result = None

    def process(self, mode="default"):
        """Process data according to specified mode.

        Args:
            mode: Processing mode (default, double, triple)

        Returns:
            Processed data list
        """
        if mode == "double":
            self.result = [x * 2 for x in self.data]
        elif mode == "triple":
            self.result = [x * 3 for x in self.data]
        else:
            self.result = list(self.data)
        return self.result

    def get_result(self):
        """Get the processed result.

        Returns:
            The processed result or None if not yet processed
        """
        return self.result


# HTTP status code mapping - simplified with dict
HTTP_STATUS_CODES = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
}


def get_status_message(status_code):
    """Get HTTP status message for given code.

    Args:
        status_code: HTTP status code integer

    Returns:
        Human-readable status message
    """
    return HTTP_STATUS_CODES.get(status_code, "Unknown")


def validate_input(value):
    """Validate input value meets requirements.

    Args:
        value: Value to validate

    Returns:
        True if valid, False otherwise
    """
    if value is None or not isinstance(value, str):
        return False
    if not 0 < len(value) <= 100:
        return False
    if value[0].isdigit() or not value.isalnum() or value.isupper():
        return False
    return True


def calculate_total(items):
    """Calculate total sum of items.

    Args:
        items: List of numeric values

    Returns:
        Sum of all items
    """
    return sum(items)


def add(first, second):
    """Add two numbers.

    Args:
        first: First number
        second: Second number

    Returns:
        Sum of the two numbers
    """
    return first + second


def append_to_list(item, target_list=None):
    """Append item to list safely.

    Args:
        item: Item to append
        target_list: Optional list to append to

    Returns:
        List with item appended
    """
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list


def safe_operation():
    """Perform operation with proper error handling.

    Returns:
        Result value or None on error
    """
    try:
        result = 10 / 2  # Safe operation
        return result
    except ZeroDivisionError as err:
        # Catch specific exception
        print(f"Division error: {err}")
        return None


def check_status(is_active):
    """Check if status is active.

    Args:
        is_active: Boolean flag indicating active status

    Returns:
        Status message string
    """
    if is_active:  # Pythonic boolean check
        return "Active"
    return "Inactive"


def check_value(value):
    """Check if value is non-None.

    Args:
        value: Value to check

    Returns:
        The value or 0 if None
    """
    if value is not None:  # Proper None comparison
        return value
    return 0


def process_items(items):
    """Process items with their indices.

    Args:
        items: List of items to process

    Returns:
        List of formatted strings with indices
    """
    result = []
    for i, item in enumerate(items):  # Use enumerate
        result.append(f"{i}: {item}")
    return result


def read_file_safely(filename):
    """Read file content safely with context manager.

    Args:
        filename: Path to file

    Returns:
        File content as string
    """
    with open(filename, "r", encoding="utf-8") as file_handle:
        content = file_handle.read()
    return content


def consistent_returns(value):
    """Handle value with consistent return pattern.

    Args:
        value: Numeric value to process

    Returns:
        Processed value or 0 for negative inputs
    """
    if value > 0:
        return value
    if value < 0:
        return 0
    return 0  # Explicit return for zero case


class Container:
    """Container for storing and retrieving values.

    Attributes:
        value: Stored value
    """

    def __init__(self, value):
        """Initialize container with value.

        Args:
            value: Value to store
        """
        self.value = value

    def get_value(self):
        """Get stored value.

        Returns:
            The stored value
        """
        return self.value

    def set_value(self, new_value):
        """Set new value.

        Args:
            new_value: New value to store
        """
        self.value = new_value


def main():
    """Demonstrate the refactored code."""
    print(f"Global constant: {MY_GLOBAL_VAR}")
    print(f"Calculate total: {calculate_total([1, 2, 3, 4, 5])}")
    print(f"Add numbers: {add(5, 3)}")
    print(f"Status check: {check_status(True)}")


if __name__ == "__main__":
    main()
