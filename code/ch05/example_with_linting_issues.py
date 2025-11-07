"""
Example module demonstrating common linting issues that flake8 can detect.
This code works but violates PEP 8 style guidelines.
"""

import os
import sys
import math
import json
import random


# Variable names don't follow naming conventions
MyGlobalVariable = 100
another_WEIRD_variable = 200


# Function with too many blank lines before it



def calculateTotal(x,y,z):  # Missing spaces after commas
    """Calculate total with poor formatting."""
    result=x+y+z  # Missing spaces around operators
    return result


def ProcessData( data ):  # Extra spaces in parameters, PascalCase function name
    """Process data with various style issues."""
    
    # Multiple statements on one line
    x = 1; y = 2; z = 3
    
    # Line too long - this is a really long line that exceeds the recommended 79 character limit for Python code and should be split
    very_long_variable_name_that_makes_line_exceed_limit = "This is a string that when combined with the variable name makes the line way too long"
    
    # Comparison to True/False (should use 'if variable:' instead)
    if data == True:
        return "yes"
    
    # Using bare except
    try:
        result = int(data)
    except:  # Bare except clause
        result = 0
    
    return result


class  myClass:  # Class name should be PascalCase, extra space after 'class'
    """Example class with style issues."""
    
    def __init__(self,value):  # Missing space after comma
        self.value=value  # Missing spaces around =
        
    def getValue(self):  # Method should be snake_case
        return self.value
        
    def setValue(self,new_value):  # Missing space after comma
        self.value = new_value


def function_with_trailing_whitespace():
    """This function has trailing whitespace."""
    x = 1    
    y = 2  
    return x + y


def unused_imports_example():
    """Function that doesn't use all imported modules."""
    # os, sys, and random are imported but never used
    return math.sqrt(16)


# Incorrect indentation in dictionary
config = {
        'name': 'example',
    'version': '1.0',
        'debug': True
}


# Lambda when def would be better
multiply = lambda x, y: x * y


# Comparison using 'is' for string literals
def check_status(status):
    """Check status with incorrect comparison."""
    if status is "active":  # Should use == for value comparison
        return True
    return False


# Function with too many blank lines after it



def another_function():
    """Another function with spacing issues."""
    pass


# Tab mixed with spaces (if tabs were present)
def	tabbed_function():  # Contains a tab character
    """This function uses a tab character."""
    return "tabs and spaces mixed"


# Missing newline at end of file (will be detected by flake8)
def final_function():
    """Final function."""
    return "no newline at end"