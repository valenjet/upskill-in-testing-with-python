"""
Test file demonstrating usage of conftest.py fixtures

This file shows how tests automatically have access to fixtures
defined in conftest_solution.py

To run these tests with the conftest fixtures:
1. Copy conftest_solution.py to conftest.py
2. Run: pytest test_with_conftest.py -v --setup-show
"""

import pytest


# =============================================================================
# Tests Using Session-Scoped Fixtures
# =============================================================================

def test_config_environment(test_config):
    """Test accessing session-scoped configuration"""
    assert test_config["environment"] == "test"
    assert test_config["debug"] is True


def test_config_api_url(test_config):
    """Another test using the same session config"""
    assert "localhost" in test_config["api_url"]


# =============================================================================
# Tests Using Module-Scoped Database Fixture
# =============================================================================

def test_database_connection(db_connection):
    """Test database connection"""
    assert db_connection["connected"] is True
    assert db_connection["db_name"] == "test_db"


def test_database_host(db_connection):
    """Test accessing database host"""
    assert db_connection["host"] == "localhost"


# =============================================================================
# Tests Using Data Fixtures
# =============================================================================

def test_sample_users_count(sample_users):
    """Test the number of sample users"""
    assert len(sample_users) == 3


def test_sample_users_content(sample_users):
    """Test sample user data"""
    alice = sample_users[0]
    assert alice["name"] == "Alice"
    assert alice["email"] == "alice@example.com"


def test_sample_products_count(sample_products):
    """Test the number of sample products"""
    assert len(sample_products) == 3


def test_sample_products_prices(sample_products):
    """Test that all products have prices"""
    for product in sample_products:
        assert "price" in product
        assert product["price"] > 0


# =============================================================================
# Tests Using Fixture Factories
# =============================================================================

def test_create_single_user(create_user):
    """Test creating a user with the factory"""
    user = create_user("David", "david@example.com")
    assert user["name"] == "David"
    assert user["email"] == "david@example.com"
    assert "id" in user


def test_create_multiple_users(create_user):
    """Test creating multiple users"""
    user1 = create_user("Eve", "eve@example.com")
    user2 = create_user("Frank", "frank@example.com")
    
    assert user1["id"] != user2["id"]
    assert user1["name"] == "Eve"
    assert user2["name"] == "Frank"


def test_create_order(create_order):
    """Test creating an order"""
    order = create_order(
        user_id=1,
        product_ids=[1, 2, 3],
        total=1109.97
    )
    
    assert order["order_id"] is not None
    assert order["user_id"] == 1
    assert len(order["product_ids"]) == 3
    assert order["status"] == "pending"


# =============================================================================
# Tests Using Temporary Workspace
# =============================================================================

def test_temp_workspace_structure(temp_workspace):
    """Test that workspace directories exist"""
    assert (temp_workspace / "data").exists()
    assert (temp_workspace / "output").exists()
    assert (temp_workspace / "config").exists()


def test_temp_workspace_config_file(temp_workspace):
    """Test reading the config file in workspace"""
    config_file = temp_workspace / "config" / "settings.json"
    assert config_file.exists()
    content = config_file.read_text()
    assert "debug" in content


# =============================================================================
# Tests Using Authenticated User
# =============================================================================

def test_authenticated_user_has_token(authenticated_user):
    """Test that authenticated user has a token"""
    assert authenticated_user["authenticated"] is True
    assert authenticated_user["token"] == "test-token-12345"


def test_authenticated_user_permissions(authenticated_user):
    """Test authenticated user permissions"""
    assert "permissions" in authenticated_user
    assert "read" in authenticated_user["permissions"]
    assert "write" in authenticated_user["permissions"]


# =============================================================================
# Tests Using API Client
# =============================================================================

def test_api_client_base_url(api_client):
    """Test API client configuration"""
    assert api_client["base_url"] == "http://localhost:8000"


def test_api_client_headers(api_client):
    """Test API client has correct headers"""
    assert "Authorization" in api_client["headers"]
    assert "Bearer" in api_client["headers"]["Authorization"]


# =============================================================================
# Tests Using Composed Fixtures
# =============================================================================

def test_database_with_data_users(database_with_data):
    """Test database with pre-loaded users"""
    assert database_with_data["connection"]["connected"] is True
    assert len(database_with_data["users"]) == 3
    assert database_with_data["inserted_count"] == 3


def test_query_users_from_database(database_with_data):
    """Test querying users from database"""
    users = database_with_data["users"]
    alice = [u for u in users if u["name"] == "Alice"][0]
    assert alice["email"] == "alice@example.com"


# =============================================================================
# Tests Demonstrating Multiple Fixture Usage
# =============================================================================

def test_complete_workflow(create_user, create_order, sample_products):
    """Test a complete workflow using multiple fixtures"""
    # Create a user
    user = create_user("George", "george@example.com")
    
    # Get product IDs
    product_ids = [p["id"] for p in sample_products]
    
    # Calculate total
    total = sum(p["price"] for p in sample_products)
    
    # Create an order
    order = create_order(user["id"], product_ids, total)
    
    # Verify the workflow
    assert order["user_id"] == user["id"]
    assert len(order["product_ids"]) == len(sample_products)
    assert order["total"] == total


def test_user_product_interaction(create_user, sample_products, create_product):
    """Test user interacting with products"""
    user = create_user("Hannah", "hannah@example.com")
    
    # User views products
    assert len(sample_products) == 3
    
    # User adds a new product (admin action)
    new_product = create_product("Monitor", 299.99, "electronics")
    
    # Verify
    assert user["name"] == "Hannah"
    assert new_product["category"] == "electronics"


# =============================================================================
# Class-based Tests with Fixtures
# =============================================================================

class TestUserOrders:
    """Group of tests for user orders"""
    
    def test_create_user_and_order(self, create_user, create_order):
        """Test creating user and their order"""
        user = create_user("Ivan", "ivan@example.com")
        order = create_order(user["id"], [1, 2], 1029.98)
        
        assert order["user_id"] == user["id"]
    
    def test_user_with_multiple_orders(self, create_user, create_order):
        """Test user with multiple orders"""
        user = create_user("Jane", "jane@example.com")
        
        order1 = create_order(user["id"], [1], 999.99)
        order2 = create_order(user["id"], [2, 3], 109.98)
        
        assert order1["order_id"] != order2["order_id"]
        assert order1["user_id"] == user["id"]
        assert order2["user_id"] == user["id"]


class TestCacheService:
    """Tests for cache service fixture"""
    
    def test_cache_set_and_get(self, cache_service):
        """Test setting and getting cache values"""
        cache_service["set"]("key1", "value1")
        result = cache_service["get"]("key1")
        assert result == "value1"
        assert cache_service["hits"] == 1
    
    def test_cache_miss(self, cache_service):
        """Test cache miss"""
        result = cache_service["get"]("nonexistent")
        assert result is None
        assert cache_service["misses"] >= 1


# =============================================================================
# Autouse Fixture Demonstration
# =============================================================================
# Note: The test_timer fixture runs automatically for every test
# You'll see timing output for each test when running with -v

def test_quick_operation():
    """Quick test to see autouse timer"""
    assert 1 + 1 == 2


def test_slower_operation():
    """Slightly slower test to see timing difference"""
    import time
    time.sleep(0.1)
    assert True
