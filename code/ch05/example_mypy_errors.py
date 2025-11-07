"""
Example module demonstrating common mypy type errors.

This code contains intentional type mismatches and errors to demonstrate
what mypy catches during static type checking.
"""

from typing import Dict, List, Optional, Union


def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def process_name(name: str) -> str:
    """Process a name string."""
    return name.upper()


def get_user_age(user: Dict[str, int]) -> int:
    """Get user age from dictionary."""
    return user['age']


def find_item(items: List[str], target: str) -> Optional[int]:
    """Find item index in list."""
    try:
        return items.index(target)
    except ValueError:
        return None


class User:
    """User class with typed attributes."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize user."""
        self.name: str = name
        self.age: int = age
    
    def get_info(self) -> str:
        """Get user info."""
        return f"{self.name} is {self.age} years old"


# Error 1: Argument type mismatch
result1 = add_numbers(5, "10")  # Error: str not compatible with int

# Error 2: Return type mismatch
def get_double(x: int) -> int:
    """Double a number."""
    return x * 2.0  # Error: float not compatible with int return type

# Error 3: Incompatible type assignment
age: int = 25
age = "twenty-five"  # Error: str not compatible with int

# Error 4: None type error
def get_length(text: str) -> int:
    """Get text length."""
    return len(text)

value: Optional[str] = None
length = get_length(value)  # Error: None not compatible with str

# Error 5: Missing return statement
def calculate_discount(price: float, rate: float) -> float:
    """Calculate discounted price."""
    if price > 0:
        return price * (1 - rate / 100)
    # Error: Missing return statement for else case

# Error 6: Attribute error
user = User("Alice", 30)
print(user.email)  # Error: User has no attribute "email"

# Error 7: Dict key error
data: Dict[str, int] = {"a": 1, "b": 2}
value = data["c"]  # Not caught by mypy (runtime error)
# But this is caught:
def get_value(d: Dict[str, int], key: int) -> int:
    """Get value from dict."""
    return d[key]  # Error: key should be str, not int

# Error 8: List type mismatch
numbers: List[int] = [1, 2, 3]
numbers.append("four")  # Error: str not compatible with int

# Error 9: Wrong number of arguments
result2 = add_numbers(5)  # Error: missing positional argument

# Error 10: Incompatible return
def process_data(data: List[int]) -> List[str]:
    """Process data."""
    return data  # Error: List[int] not compatible with List[str]

# Error 11: Using Optional incorrectly
def greet(name: Optional[str]) -> str:
    """Greet user."""
    return f"Hello, {name.upper()}"  # Error: name might be None

# Error 12: Type narrowing issue
def format_value(value: Union[int, str]) -> str:
    """Format a value."""
    return value.upper()  # Error: int has no method 'upper'

# Error 13: Incorrect generic usage
def get_first(items: List) -> int:  # Error: Missing type parameter
    """Get first item."""
    return items[0]

# Error 14: Incompatible type in comparison
def is_valid_age(age: int) -> bool:
    """Check if age is valid."""
    return age > "18"  # Error: can't compare int with str

# Error 15: Return type too specific
def get_config() -> Dict[str, str]:
    """Get configuration."""
    return {"port": 8080}  # Error: int value incompatible with str
