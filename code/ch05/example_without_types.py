"""
Example module without type hints, demonstrating potential runtime errors.

This code works at runtime but lacks type safety, making it prone to
errors that could be caught with type checking.
"""


def calculate_discount(price, discount_percent):
    """Calculate the discounted price."""
    discount = price * (discount_percent / 100)
    return price - discount


def process_items(items):
    """Process a list of items and return their total."""
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total


def format_user_name(first_name, last_name=None):
    """Format a user's full name."""
    if last_name:
        return f"{first_name} {last_name}"
    return first_name


class ShoppingCart:
    """Shopping cart without type hints."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
        self.discount_rate = 0
    
    def add_item(self, name, price, quantity=1):
        """Add an item to the cart."""
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def set_discount(self, rate):
        """Set the discount rate."""
        self.discount_rate = rate
    
    def get_total(self):
        """Calculate the total price with discount."""
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        discount = subtotal * (self.discount_rate / 100)
        return subtotal - discount
    
    def get_item_count(self):
        """Get the total number of items."""
        return sum(item['quantity'] for item in self.items)


def find_expensive_items(items, threshold):
    """Find items above a price threshold."""
    return [item for item in items if item['price'] > threshold]


def apply_bulk_discount(price, quantity):
    """Apply bulk discount based on quantity."""
    if quantity >= 100:
        return price * 0.8
    elif quantity >= 50:
        return price * 0.9
    elif quantity >= 10:
        return price * 0.95
    return price


def combine_data(data1, data2):
    """Combine two data structures."""
    result = data1.copy()
    result.update(data2)
    return result


def parse_config(config_string):
    """Parse a configuration string."""
    parts = config_string.split('=')
    if len(parts) == 2:
        return {parts[0].strip(): parts[1].strip()}
    return None


def safe_divide(numerator, denominator):
    """Safely divide two numbers."""
    if denominator == 0:
        return None
    return numerator / denominator
