"""Example module demonstrating common pylint warnings and errors.

This module intentionally contains various issues that pylint will detect,
organized by category: Convention (C), Refactor (R), Warning (W), Error (E).
"""

import sys
import os
import time


# Global variable without constant naming (C0103)
myGlobalVar = 42


# Function with too many arguments (R0913)
def process_data(name, age, email, phone, address, city, state, zipcode, country, notes):
    """Process user data with too many arguments."""
    return f"{name} from {city}, {state}"


# Function with too many local variables (R0914)
def calculate_complex_result(x, y):
    """Function with too many local variables."""
    var1 = x + y
    var2 = x - y
    var3 = x * y
    var4 = x / y if y != 0 else 0
    var5 = x ** 2
    var6 = y ** 2
    var7 = var1 + var2
    var8 = var3 + var4
    var9 = var5 + var6
    var10 = var7 + var8
    var11 = var9 + var10
    var12 = var11 * 2
    var13 = var12 / 3
    var14 = var13 + 100
    var15 = var14 - 50
    var16 = var15 * var1
    return var16


# Class without docstring (C0115)
class DataProcessor:
    
    # Method without docstring (C0116)
    def __init__(self, data):
        self.data = data
        self.result = None
    
    # Method that could be a function (R0201)
    def helper_function(self, value):
        """Helper that doesn't use self."""
        return value * 2
    
    # Method with unused argument (W0613)
    def process(self, mode="default", debug=False):
        """Process data."""
        self.result = [x * 2 for x in self.data]
        return self.result


# Function with too many branches (R0912)
def complex_conditional(status_code):
    """Function with too many branches."""
    if status_code == 200:
        return "OK"
    elif status_code == 201:
        return "Created"
    elif status_code == 204:
        return "No Content"
    elif status_code == 301:
        return "Moved Permanently"
    elif status_code == 302:
        return "Found"
    elif status_code == 400:
        return "Bad Request"
    elif status_code == 401:
        return "Unauthorized"
    elif status_code == 403:
        return "Forbidden"
    elif status_code == 404:
        return "Not Found"
    elif status_code == 500:
        return "Internal Server Error"
    elif status_code == 502:
        return "Bad Gateway"
    elif status_code == 503:
        return "Service Unavailable"
    else:
        return "Unknown"


# Function with too many return statements (R0911)
def validate_input(value):
    """Function with too many return statements."""
    if value is None:
        return False
    if not isinstance(value, str):
        return False
    if len(value) == 0:
        return False
    if len(value) > 100:
        return False
    if value[0].isdigit():
        return False
    if not value.isalnum():
        return False
    if value.isupper():
        return False
    return True


# Unused import (W0611) - 'time' imported but not used above


# Function name not snake_case (C0103)
def CalculateTotal(items):
    """Function with incorrect naming convention."""
    total = 0
    for item in items:
        total += item
    return total


# Line too long (C0301)
def function_with_very_long_line():
    """Demonstrate line length issue."""
    message = "This is an extremely long line that exceeds the recommended line length limit and should be split across multiple lines for better readability"
    return message


# Missing function docstring (C0116)
def add(a, b):
    return a + b


# Dangerous default argument (W0102)
def append_to_list(item, target_list=[]):
    """Function with mutable default argument."""
    target_list.append(item)
    return target_list


# Broad exception catch (W0703)
def risky_operation():
    """Function catching broad exception."""
    try:
        result = 10 / 0
        return result
    except Exception:
        return None


# Pointless statement (W0104)
def pointless_code():
    """Function with pointless statement."""
    x = 10
    x  # This line does nothing
    return x


# Comparison with True (C0121)
def check_status(is_active):
    """Function with explicit True comparison."""
    if is_active == True:
        return "Active"
    return "Inactive"


# Comparison with None using != instead of 'is not' (C0121)
def check_value(value):
    """Function with incorrect None comparison."""
    if value != None:
        return value
    return 0


# Consider using enumerate (C0200)
def process_items(items):
    """Function that should use enumerate."""
    result = []
    for i in range(len(items)):
        result.append(f"{i}: {items[i]}")
    return result


# Consider using with statement for file operations (R1732)
def read_file(filename):
    """Function not using context manager."""
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


# Inconsistent return statements (R1710)
def inconsistent_returns(x):
    """Function with inconsistent returns."""
    if x > 0:
        return x
    elif x < 0:
        print("Negative")
    # Missing explicit return for x == 0 case


# Too few public methods (R0903)
class SimpleContainer:
    """Class with too few public methods."""
    
    def __init__(self, value):
        """Initialize container."""
        self.value = value


if __name__ == "__main__":
    # Demonstrate some of the issues
    print(myGlobalVar)
    print(CalculateTotal([1, 2, 3, 4, 5]))
    print(add(5, 3))
