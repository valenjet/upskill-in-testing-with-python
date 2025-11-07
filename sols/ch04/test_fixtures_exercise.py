"""
Exercise: Creating and Using Fixtures

Complete the TODOs below to practice creating and using pytest fixtures.
Run this file with: pytest test_fixtures_exercise.py -v

Learn about:
- Creating fixtures with different scopes
- Using yield for setup/teardown
- Fixture factories
- Composing fixtures
"""

import pytest
from pathlib import Path


# =============================================================================
# PART 1: Basic Fixtures
# =============================================================================

# TODO: Create a fixture called "sample_data" that returns a list of numbers
# Hint: Use @pytest.fixture decorator
# The fixture should return [1, 2, 3, 4, 5]


def test_sum_with_fixture(sample_data):
    """Test that uses the sample_data fixture"""
    result = sum(sample_data)
    assert result == 15


def test_length_with_fixture(sample_data):
    """Another test using the same fixture"""
    assert len(sample_data) == 5


# =============================================================================
# PART 2: Fixtures with Setup and Teardown
# =============================================================================

# TODO: Create a fixture called "temp_file" that:
# 1. Creates a temporary file
# 2. Yields the file path
# 3. Cleans up (deletes) the file after the test
# Hint: Use yield, then put cleanup code after yield


def test_write_to_file(temp_file):
    """Test writing to a temporary file"""
    temp_file.write_text("Hello, fixtures!")
    content = temp_file.read_text()
    assert content == "Hello, fixtures!"


def test_file_exists(temp_file):
    """Test that the file exists during the test"""
    assert temp_file.exists()


# =============================================================================
# PART 3: Fixture Scopes
# =============================================================================

# TODO: Create a module-scoped fixture called "expensive_resource"
# This fixture should only run once for the entire module
# Hint: Use @pytest.fixture(scope="module")
# Have it return a dictionary: {"initialized": True, "value": 42}


def test_resource_first(expensive_resource):
    """First test using the module-scoped fixture"""
    assert expensive_resource["initialized"] is True
    # Modify the resource
    expensive_resource["test_count"] = 1


def test_resource_second(expensive_resource):
    """Second test - should share the same resource"""
    # This should see the modification from the first test
    # because they share the same module-scoped fixture
    assert expensive_resource["initialized"] is True
    # TODO: Add an assertion to check if "test_count" exists in the resource


# =============================================================================
# PART 4: Fixture Factories
# =============================================================================

# TODO: Create a fixture factory called "user_factory"
# It should return a function that creates user dictionaries
# The function should accept name and age parameters
# Example: user_factory("Alice", 30) returns {"name": "Alice", "age": 30}


def test_create_single_user(user_factory):
    """Test creating one user"""
    user = user_factory("Alice", 30)
    assert user["name"] == "Alice"
    assert user["age"] == 30


def test_create_multiple_users(user_factory):
    """Test creating multiple users with the factory"""
    alice = user_factory("Alice", 30)
    bob = user_factory("Bob", 25)
    
    assert alice["name"] == "Alice"
    assert bob["name"] == "Bob"
    # TODO: Add assertions to check that alice and bob are different objects


# =============================================================================
# PART 5: Composing Fixtures (Fixtures Using Other Fixtures)
# =============================================================================

# TODO: Create a fixture called "database" that returns {"connected": True}


# TODO: Create a fixture called "database_cursor" that:
# 1. Uses the "database" fixture as a parameter
# 2. Checks that database["connected"] is True
# 3. Returns a cursor dictionary: {"database": database, "position": 0}


def test_database_cursor(database_cursor):
    """Test using composed fixtures"""
    assert database_cursor["database"]["connected"] is True
    assert database_cursor["position"] == 0


# =============================================================================
# PART 6: Parametrizing Fixtures
# =============================================================================

# TODO: Create a fixture called "sample_user" that is parametrized
# with these values: "Alice", "Bob", "Charlie"
# Hint: Use @pytest.fixture(params=[...])
# The fixture should return the parameter value


def test_greet_user(sample_user):
    """This test will run 3 times, once for each parameter"""
    greeting = f"Hello, {sample_user}!"
    assert sample_user in greeting
    assert greeting.startswith("Hello")


# =============================================================================
# PART 7: Class-based Tests with Fixtures
# =============================================================================

class TestShoppingCart:
    """Tests for a shopping cart"""
    
    # TODO: Create a fixture called "cart" that returns an empty list
    # This fixture should be at class level (indent it inside the class)
    
    
    def test_add_item(self, cart):
        """Test adding an item to the cart"""
        cart.append("apple")
        assert len(cart) == 1
        assert "apple" in cart
    
    def test_add_multiple_items(self, cart):
        """Test adding multiple items"""
        cart.extend(["apple", "banana", "orange"])
        assert len(cart) == 3


# =============================================================================
# BONUS CHALLENGE
# =============================================================================

# TODO: Create a fixture called "api_client" that:
# 1. Prints "Connecting to API..." at setup
# 2. Yields a dictionary with {"connected": True, "requests": 0}
# 3. Prints "Disconnecting from API..." at teardown
# 4. Verifies that at least one request was made (requests > 0)

# TODO: Create a test that uses the api_client fixture
# The test should increment the "requests" count


# =============================================================================
# TIPS
# =============================================================================

"""
Remember:
1. Fixtures are functions decorated with @pytest.fixture
2. Use yield for setup/teardown pattern
3. Scopes: function (default), class, module, package, session
4. Fixtures can use other fixtures as parameters
5. Fixture factories return functions that create objects
6. Use params to parametrize fixtures

Run with -v to see fixture setup/teardown:
    pytest test_fixtures_exercise.py -v --setup-show
"""
