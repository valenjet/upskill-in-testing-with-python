"""
Solution: Creating and Using Fixtures

This is the complete solution for the fixtures exercise.
Run this file with: pytest test_fixtures_solution.py -v
"""

import pytest
from pathlib import Path
import tempfile
import os


# =============================================================================
# PART 1: Basic Fixtures
# =============================================================================

@pytest.fixture
def sample_data():
    """Basic fixture that returns sample data"""
    return [1, 2, 3, 4, 5]


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

@pytest.fixture
def temp_file(tmp_path):
    """Fixture with setup and teardown"""
    # Setup: create temporary file
    file_path = tmp_path / "test_file.txt"
    file_path.touch()
    
    # Provide the file to the test
    yield file_path
    
    # Teardown: cleanup (file is automatically cleaned up by tmp_path)
    # But we can add explicit cleanup if needed
    if file_path.exists():
        file_path.unlink()


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

@pytest.fixture(scope="module")
def expensive_resource():
    """Module-scoped fixture - runs once for the entire module"""
    print("\n[SETUP] Initializing expensive resource...")
    resource = {"initialized": True, "value": 42}
    yield resource
    print("\n[TEARDOWN] Cleaning up expensive resource...")


def test_resource_first(expensive_resource):
    """First test using the module-scoped fixture"""
    assert expensive_resource["initialized"] is True
    # Modify the resource
    expensive_resource["test_count"] = 1


def test_resource_second(expensive_resource):
    """Second test - should share the same resource"""
    # This should see the modification from the first test
    assert expensive_resource["initialized"] is True
    assert "test_count" in expensive_resource
    assert expensive_resource["test_count"] == 1


# =============================================================================
# PART 4: Fixture Factories
# =============================================================================

@pytest.fixture
def user_factory():
    """Fixture factory that returns a function to create users"""
    def create_user(name, age):
        return {
            "name": name,
            "age": age,
            "id": id(name)  # Unique ID for each user
        }
    return create_user


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
    assert alice != bob  # Different objects
    assert alice["id"] != bob["id"]


# =============================================================================
# PART 5: Composing Fixtures (Fixtures Using Other Fixtures)
# =============================================================================

@pytest.fixture
def database():
    """Database connection fixture"""
    print("\n[DB] Connecting to database...")
    db = {"connected": True, "host": "localhost"}
    yield db
    print("\n[DB] Disconnecting from database...")


@pytest.fixture
def database_cursor(database):
    """Cursor fixture that depends on database fixture"""
    assert database["connected"] is True
    print("\n[CURSOR] Creating database cursor...")
    cursor = {
        "database": database,
        "position": 0
    }
    yield cursor
    print("\n[CURSOR] Closing cursor...")


def test_database_cursor(database_cursor):
    """Test using composed fixtures"""
    assert database_cursor["database"]["connected"] is True
    assert database_cursor["position"] == 0


# =============================================================================
# PART 6: Parametrizing Fixtures
# =============================================================================

@pytest.fixture(params=["Alice", "Bob", "Charlie"])
def sample_user(request):
    """Parametrized fixture - test runs once for each parameter"""
    return request.param


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
    
    @pytest.fixture
    def cart(self):
        """Fixture for shopping cart"""
        return []
    
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

@pytest.fixture
def api_client():
    """API client with setup and teardown"""
    print("\n[API] Connecting to API...")
    client = {"connected": True, "requests": 0}
    
    yield client
    
    print(f"\n[API] Disconnecting from API... (Made {client['requests']} requests)")
    assert client["requests"] > 0, "API client should have made at least one request"


def test_api_get_request(api_client):
    """Test using the API client"""
    api_client["requests"] += 1
    response = {"status": 200, "data": "success"}
    assert response["status"] == 200


def test_api_post_request(api_client):
    """Another test using the API client"""
    api_client["requests"] += 1
    request_data = {"name": "test"}
    response = {"status": 201, "id": 1}
    assert response["status"] == 201


# =============================================================================
# Additional Examples
# =============================================================================

@pytest.fixture(scope="session")
def session_config():
    """Session-scoped fixture - runs once for entire test session"""
    print("\n[SESSION] Loading configuration...")
    config = {
        "environment": "test",
        "debug": True,
        "version": "1.0.0"
    }
    yield config
    print("\n[SESSION] Cleaning up configuration...")


def test_config_values(session_config):
    """Test using session-scoped configuration"""
    assert session_config["environment"] == "test"
    assert session_config["debug"] is True


@pytest.fixture
def product_factory():
    """Factory fixture for creating product objects"""
    created_products = []
    
    def create_product(name, price):
        product = {
            "name": name,
            "price": price,
            "id": len(created_products) + 1
        }
        created_products.append(product)
        return product
    
    yield create_product
    
    # Cleanup: log created products
    print(f"\n[CLEANUP] Created {len(created_products)} products")


def test_product_factory(product_factory):
    """Test creating products with factory"""
    apple = product_factory("Apple", 1.99)
    banana = product_factory("Banana", 0.99)
    
    assert apple["name"] == "Apple"
    assert apple["price"] == 1.99
    assert banana["id"] == 2  # Second product


@pytest.fixture
def temp_directory(tmp_path):
    """Fixture that creates a temporary directory structure"""
    # Create directory structure
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    
    config_file = data_dir / "config.json"
    config_file.write_text('{"setting": "value"}')
    
    yield data_dir
    
    # Cleanup happens automatically with tmp_path


def test_directory_structure(temp_directory):
    """Test using temporary directory"""
    assert temp_directory.exists()
    assert temp_directory.is_dir()
    
    config_file = temp_directory / "config.json"
    assert config_file.exists()
    assert "setting" in config_file.read_text()


# =============================================================================
# Run with --setup-show to see fixture execution order
# =============================================================================
