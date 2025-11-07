"""
Solution: Organizing Tests with conftest.py

This is the complete solution showing how to create shared fixtures in conftest.py.

NOTE: This is named conftest_solution.py for reference.
In a real project, you would name this file 'conftest.py' and place it
in your tests directory to make fixtures available to all tests.
"""

import pytest
import time
from pathlib import Path
from datetime import datetime


# =============================================================================
# PART 1: Session-Scoped Fixtures
# =============================================================================

@pytest.fixture(scope="session")
def test_config():
    """Session-scoped configuration fixture"""
    print("\n[SESSION] Loading test configuration...")
    config = {
        "environment": "test",
        "debug": True,
        "api_url": "http://localhost:8000"
    }
    yield config
    print("\n[SESSION] Test session completed")


# =============================================================================
# PART 2: Module-Scoped Database Fixture
# =============================================================================

@pytest.fixture(scope="module")
def db_connection():
    """Module-scoped database connection fixture"""
    print("\n[DB] Opening database connection...")
    connection = {
        "connected": True,
        "db_name": "test_db",
        "host": "localhost",
        "port": 5432
    }
    
    yield connection
    
    print("\n[DB] Closing database connection...")
    connection["connected"] = False


# =============================================================================
# PART 3: Function-Scoped Data Fixtures
# =============================================================================

@pytest.fixture
def sample_users():
    """Function-scoped fixture providing sample user data"""
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ]


@pytest.fixture
def sample_products():
    """Function-scoped fixture providing sample product data"""
    return [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Mouse", "price": 29.99},
        {"id": 3, "name": "Keyboard", "price": 79.99}
    ]


# =============================================================================
# PART 4: Fixture Factories
# =============================================================================

@pytest.fixture
def create_user():
    """Fixture factory for creating user objects"""
    user_counter = 0
    
    def _create_user(name, email):
        nonlocal user_counter
        user_counter += 1
        return {
            "id": user_counter,
            "name": name,
            "email": email,
            "created_at": datetime.now().isoformat()
        }
    
    return _create_user


@pytest.fixture
def create_order():
    """Fixture factory for creating order objects"""
    order_counter = 0
    
    def _create_order(user_id, product_ids, total):
        nonlocal order_counter
        order_counter += 1
        return {
            "order_id": order_counter,
            "user_id": user_id,
            "product_ids": product_ids,
            "total": total,
            "status": "pending",
            "created_at": datetime.now().isoformat()
        }
    
    return _create_order


# =============================================================================
# PART 5: Temporary File System Fixtures
# =============================================================================

@pytest.fixture
def temp_workspace(tmp_path):
    """Create a temporary workspace with directory structure"""
    # Create directory structure
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "output"
    config_dir = tmp_path / "config"
    
    data_dir.mkdir()
    output_dir.mkdir()
    config_dir.mkdir()
    
    # Optionally create some default files
    config_file = config_dir / "settings.json"
    config_file.write_text('{"debug": true}')
    
    yield tmp_path
    
    # Cleanup happens automatically with tmp_path


# =============================================================================
# PART 6: Autouse Fixtures
# =============================================================================

@pytest.fixture(autouse=True)
def test_timer():
    """Automatically time each test"""
    start_time = time.time()
    
    yield
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"\n⏱️  Test duration: {duration:.4f} seconds")


# =============================================================================
# PART 7: Fixtures with Dependencies
# =============================================================================

@pytest.fixture
def authenticated_user(create_user):
    """Create an authenticated user using the create_user factory"""
    user = create_user("TestUser", "testuser@example.com")
    user["authenticated"] = True
    user["token"] = "test-token-12345"
    user["permissions"] = ["read", "write"]
    return user


# =============================================================================
# BONUS CHALLENGE
# =============================================================================

@pytest.fixture
def api_client(test_config):
    """Create a mock API client using test configuration"""
    client = {
        "base_url": test_config["api_url"],
        "headers": {
            "Authorization": "Bearer test-token",
            "Content-Type": "application/json"
        },
        "timeout": 30,
        "debug": test_config["debug"]
    }
    
    print(f"\n[API] Created API client for {client['base_url']}")
    return client


@pytest.fixture
def database_with_data(db_connection, sample_users):
    """Database fixture with pre-loaded user data"""
    # Simulate inserting users into database
    print(f"\n[DB] Inserting {len(sample_users)} users into {db_connection['db_name']}...")
    
    database = {
        "connection": db_connection,
        "users": sample_users,
        "inserted_count": len(sample_users)
    }
    
    yield database
    
    print(f"\n[DB] Cleaning up {database['inserted_count']} test records...")


# =============================================================================
# Additional Useful Fixtures
# =============================================================================

@pytest.fixture
def mock_datetime():
    """Fixture for mocking datetime - useful for testing time-dependent code"""
    fixed_time = datetime(2025, 11, 7, 12, 0, 0)
    return fixed_time


@pytest.fixture
def create_product():
    """Fixture factory for creating product objects"""
    product_counter = 0
    
    def _create_product(name, price, category="general"):
        nonlocal product_counter
        product_counter += 1
        return {
            "id": product_counter,
            "name": name,
            "price": price,
            "category": category,
            "in_stock": True
        }
    
    return _create_product


@pytest.fixture(scope="module")
def cache_service():
    """Module-scoped cache service fixture"""
    print("\n[CACHE] Initializing cache service...")
    cache = {
        "data": {},
        "hits": 0,
        "misses": 0
    }
    
    def get(key):
        if key in cache["data"]:
            cache["hits"] += 1
            return cache["data"][key]
        cache["misses"] += 1
        return None
    
    def set(key, value):
        cache["data"][key] = value
    
    cache["get"] = get
    cache["set"] = set
    
    yield cache
    
    print(f"\n[CACHE] Stats - Hits: {cache['hits']}, Misses: {cache['misses']}")


@pytest.fixture
def cleanup_tracker():
    """Track resources that need cleanup"""
    resources = []
    
    def register(resource):
        resources.append(resource)
    
    yield register
    
    # Cleanup all registered resources
    print(f"\n[CLEANUP] Cleaning up {len(resources)} resources...")
    for resource in resources:
        print(f"  - Cleaning: {resource}")


# =============================================================================
# Fixture for parametrized database backends (advanced)
# =============================================================================

@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def database_backend(request):
    """Parametrized fixture for testing with different database backends"""
    backend = request.param
    print(f"\n[DB] Using {backend} backend")
    return {
        "type": backend,
        "connection_string": f"{backend}://localhost/test_db"
    }
