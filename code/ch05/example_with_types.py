"""
Example module with comprehensive type hints.

This code demonstrates proper type annotation for improved code clarity,
better IDE support, and early error detection through static type checking.
"""

from typing import Dict, List, Optional, Union


def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the discounted price.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (0-100)
    
    Returns:
        Price after discount applied
    """
    discount = price * (discount_percent / 100)
    return price - discount


def process_items(items: List[Dict[str, Union[str, float, int]]]) -> float:
    """
    Process a list of items and return their total.
    
    Args:
        items: List of item dictionaries with 'price' and 'quantity'
    
    Returns:
        Total price of all items
    """
    total = 0.0
    for item in items:
        price = float(item['price'])
        quantity = int(item['quantity'])
        total += price * quantity
    return total


def format_user_name(first_name: str, last_name: Optional[str] = None) -> str:
    """
    Format a user's full name.
    
    Args:
        first_name: User's first name
        last_name: User's last name (optional)
    
    Returns:
        Formatted full name
    """
    if last_name:
        return f"{first_name} {last_name}"
    return first_name


class ShoppingCart:
    """Shopping cart with proper type hints."""
    
    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self.items: List[Dict[str, Union[str, float, int]]] = []
        self.discount_rate: float = 0.0
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the cart.
        
        Args:
            name: Item name
            price: Item price
            quantity: Number of items (default: 1)
        """
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def set_discount(self, rate: float) -> None:
        """
        Set the discount rate.
        
        Args:
            rate: Discount rate as percentage (0-100)
        """
        self.discount_rate = rate
    
    def get_total(self) -> float:
        """
        Calculate the total price with discount.
        
        Returns:
            Total price after discount
        """
        subtotal = sum(
            float(item['price']) * int(item['quantity']) 
            for item in self.items
        )
        discount = subtotal * (self.discount_rate / 100)
        return subtotal - discount
    
    def get_item_count(self) -> int:
        """
        Get the total number of items.
        
        Returns:
            Total item count
        """
        return sum(int(item['quantity']) for item in self.items)


def find_expensive_items(
    items: List[Dict[str, Union[str, float, int]]], 
    threshold: float
) -> List[Dict[str, Union[str, float, int]]]:
    """
    Find items above a price threshold.
    
    Args:
        items: List of item dictionaries
        threshold: Minimum price threshold
    
    Returns:
        List of items with price above threshold
    """
    return [item for item in items if float(item['price']) > threshold]


def apply_bulk_discount(price: float, quantity: int) -> float:
    """
    Apply bulk discount based on quantity.
    
    Args:
        price: Base price per unit
        quantity: Number of units
    
    Returns:
        Adjusted price per unit after bulk discount
    """
    if quantity >= 100:
        return price * 0.8
    elif quantity >= 50:
        return price * 0.9
    elif quantity >= 10:
        return price * 0.95
    return price


def combine_data(
    data1: Dict[str, Union[str, int, float]], 
    data2: Dict[str, Union[str, int, float]]
) -> Dict[str, Union[str, int, float]]:
    """
    Combine two data structures.
    
    Args:
        data1: First dictionary
        data2: Second dictionary
    
    Returns:
        Merged dictionary
    """
    result = data1.copy()
    result.update(data2)
    return result


def parse_config(config_string: str) -> Optional[Dict[str, str]]:
    """
    Parse a configuration string.
    
    Args:
        config_string: Configuration in format "key=value"
    
    Returns:
        Dictionary with parsed key-value pair, or None if invalid
    """
    parts = config_string.split('=')
    if len(parts) == 2:
        return {parts[0].strip(): parts[1].strip()}
    return None


def safe_divide(numerator: float, denominator: float) -> Optional[float]:
    """
    Safely divide two numbers.
    
    Args:
        numerator: Number to be divided
        denominator: Number to divide by
    
    Returns:
        Result of division, or None if denominator is zero
    """
    if denominator == 0:
        return None
    return numerator / denominator
