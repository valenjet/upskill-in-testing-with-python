# test_conftest_demo.py
"""
Demonstration of using fixtures from conftest.py.

This module shows how pytest automatically discovers and provides
fixtures defined in conftest.py without requiring any imports.

Key Concepts Demonstrated:
1. Automatic fixture discovery from conftest.py
2. Using session, module, and function-scoped fixtures
3. Fixture dependencies (fixtures using other fixtures)
4. Fixture factories for creating multiple instances
5. No import statements needed for conftest.py fixtures

Run examples:
    pytest test_conftest_demo.py -v                # Run all tests
    pytest test_conftest_demo.py -v -s             # Show fixture output
    pytest test_conftest_demo.py --setup-show      # Show fixture setup/teardown
    pytest --fixtures                               # List all available fixtures
"""

import pytest


# ============================================================================
# TESTS USING SESSION-SCOPED FIXTURES
# ============================================================================

def test_using_test_config(test_config):
    """
    Demonstrates using a session-scoped fixture.
    
    The test_config fixture is defined in conftest.py and automatically
    available without any import statement.
    
    Session-scoped fixtures are created once and reused across all tests.
    """
    assert test_config['environment'] == 'test'
    assert test_config['debug'] is True
    assert 'timeout' in test_config
    print(f"\nUsing config: {test_config}")


def test_session_timestamp(session_timestamp):
    """
    Uses session-scoped timestamp.
    
    All tests in the session will see the same timestamp value,
    demonstrating that session fixtures are shared.
    """
    assert session_timestamp is not None
    print(f"\nSession started at: {session_timestamp}")


# ============================================================================
# TESTS USING MODULE-SCOPED FIXTURES
# ============================================================================

def test_sample_data_users(sample_data):
    """
    Uses module-scoped sample_data fixture.
    
    The sample_data fixture provides test data that's created once
    per test module and shared by all tests in this file.
    """
    users = sample_data['users']
    assert len(users) == 3
    assert users[0]['name'] == 'Alice'
    assert users[0]['role'] == 'admin'


def test_sample_data_products(sample_data):
    """
    Another test using the same module-scoped fixture.
    
    This test shares the exact same sample_data instance as the
    previous test, demonstrating module-scope sharing.
    """
    products = sample_data['products']
    assert len(products) == 3
    assert products[0]['name'] == 'Laptop'
    assert products[0]['price'] == 999.99


def test_database_connection_is_available(database_connection):
    """
    Uses module-scoped database connection.
    
    The database_connection fixture creates an in-memory SQLite database
    once per module and shares it across tests.
    """
    cursor = database_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    
    assert 'users' in tables
    assert 'products' in tables
    print(f"\nDatabase tables: {tables}")


# ============================================================================
# TESTS USING FUNCTION-SCOPED FIXTURES (WITH TRANSACTIONS)
# ============================================================================

def test_database_transaction_isolation_1(database_transaction):
    """
    Demonstrates transaction isolation.
    
    Changes made in this test are rolled back automatically after
    the test completes, ensuring tests don't affect each other.
    """
    # Insert a user
    cursor = database_transaction.execute(
        'INSERT INTO users (name, email, role) VALUES (?, ?, ?)',
        ('Test User', 'test@example.com', 'user')
    )
    user_id = cursor.lastrowid
    
    # Verify insert worked
    cursor = database_transaction.execute(
        'SELECT * FROM users WHERE id = ?', (user_id,)
    )
    user = cursor.fetchone()
    assert user is not None
    assert user['name'] == 'Test User'
    
    # This insert will be rolled back after the test


def test_database_transaction_isolation_2(database_transaction):
    """
    Demonstrates that the previous test's changes were rolled back.
    
    This test starts with a clean database state because the previous
    test's transaction was rolled back.
    """
    cursor = database_transaction.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    
    # Database should be empty because previous test was rolled back
    assert count == 0, "Database should be clean (previous test rolled back)"


# ============================================================================
# TESTS USING FIXTURE FACTORIES
# ============================================================================

def test_user_factory_creates_users(user_factory):
    """
    Demonstrates using a fixture factory.
    
    The user_factory fixture returns a function that can be called
    multiple times to create multiple users in the database.
    """
    # Create multiple users
    admin_id = user_factory('Admin User', 'admin@example.com', role='admin')
    user1_id = user_factory('Regular User 1', 'user1@example.com')
    user2_id = user_factory('Regular User 2', 'user2@example.com')
    
    # All should have different IDs
    assert admin_id != user1_id != user2_id
    assert admin_id > 0
    assert user1_id > 0
    assert user2_id > 0


def test_user_factory_with_database_query(user_factory, database_transaction):
    """
    Creates users and queries them from the database.
    
    Demonstrates that factory-created users are actually in the database
    and can be queried.
    """
    # Create users
    user_factory('Alice', 'alice@example.com', role='admin')
    user_factory('Bob', 'bob@example.com')
    
    # Query database
    cursor = database_transaction.execute(
        'SELECT name, email, role FROM users ORDER BY name'
    )
    users = cursor.fetchall()
    
    assert len(users) == 2
    assert users[0]['name'] == 'Alice'
    assert users[0]['role'] == 'admin'
    assert users[1]['name'] == 'Bob'
    assert users[1]['role'] == 'user'


def test_product_factory(product_factory, database_transaction):
    """
    Demonstrates using the product factory.
    
    Similar to user_factory, but for products.
    """
    # Create products
    laptop_id = product_factory('Laptop', 999.99, stock=10)
    mouse_id = product_factory('Mouse', 29.99, stock=50)
    keyboard_id = product_factory('Keyboard', 79.99)  # Default stock=0
    
    # Query products
    cursor = database_transaction.execute(
        'SELECT * FROM products ORDER BY id'
    )
    products = cursor.fetchall()
    
    assert len(products) == 3
    assert products[0]['name'] == 'Laptop'
    assert products[0]['stock'] == 10
    assert products[1]['name'] == 'Mouse'
    assert products[1]['stock'] == 50
    assert products[2]['name'] == 'Keyboard'
    assert products[2]['stock'] == 0  # Keyboard with default stock


# ============================================================================
# TESTS USING TEMPORARY FILE FIXTURES
# ============================================================================

def test_temp_directory(temp_directory):
    """
    Demonstrates using the temporary directory fixture.
    
    The temp_directory fixture provides a Path object to a temporary
    directory that's automatically cleaned up after the test.
    """
    assert temp_directory.exists()
    assert temp_directory.is_dir()
    
    # Can create files in the temp directory
    test_file = temp_directory / "test.txt"
    test_file.write_text("Hello, World!")
    
    assert test_file.exists()
    assert test_file.read_text() == "Hello, World!"
    
    # Directory will be automatically cleaned up after test


def test_temp_file(temp_file):
    """
    Uses the temp_file fixture.
    
    The temp_file fixture depends on temp_directory (both from conftest.py)
    and provides a pre-created temporary file.
    """
    assert temp_file.exists()
    assert temp_file.is_file()
    
    # File was created with initial content
    content = temp_file.read_text()
    assert content == "Initial content for testing"
    
    # Can modify the file
    temp_file.write_text("Modified content")
    assert temp_file.read_text() == "Modified content"


def test_file_factory(file_factory):
    """
    Demonstrates using the file factory.
    
    The file_factory fixture returns a function that creates files
    in the temporary directory.
    """
    # Create multiple files
    file1 = file_factory('data1.txt', 'Content for file 1')
    file2 = file_factory('data2.txt', 'Content for file 2')
    file3 = file_factory('empty.txt')  # Empty file
    
    # All files exist
    assert file1.exists()
    assert file2.exists()
    assert file3.exists()
    
    # Files have correct content
    assert file1.read_text() == 'Content for file 1'
    assert file2.read_text() == 'Content for file 2'
    assert file3.read_text() == ''


# ============================================================================
# TESTS USING API CLIENT FIXTURE
# ============================================================================

def test_api_client_get(api_client):
    """
    Demonstrates using the mock API client fixture.
    
    The api_client fixture provides a mock API client configured
    with test settings from test_config.
    """
    response = api_client.get('/users')
    
    assert response['status'] == 200
    assert 'data' in response
    assert len(api_client.requests_made) == 1
    assert api_client.requests_made[0] == ('GET', '/users')


def test_api_client_post(api_client):
    """
    Uses the API client to make a POST request.
    
    Each test gets a fresh api_client instance because it's function-scoped.
    """
    response = api_client.post('/users', {'name': 'Alice'})
    
    assert response['status'] == 201
    assert len(api_client.requests_made) == 1
    assert api_client.requests_made[0][0] == 'POST'
    assert api_client.requests_made[0][1] == '/users'


# ============================================================================
# TESTS COMBINING MULTIPLE FIXTURES
# ============================================================================

def test_combining_multiple_fixtures(user_factory, product_factory, 
                                     database_transaction, test_config):
    """
    Demonstrates using multiple fixtures from conftest.py in one test.
    
    pytest automatically provides all requested fixtures, resolving
    their dependencies correctly.
    
    Fixture dependency chain:
    - user_factory → database_transaction → database_connection
    - product_factory → database_transaction → database_connection
    - database_connection is module-scoped, shared by both factories
    - test_config is session-scoped
    """
    # Create users
    admin_id = user_factory('Admin', 'admin@example.com', role='admin')
    user_id = user_factory('User', 'user@example.com')
    
    # Create products
    product1_id = product_factory('Product 1', 99.99, stock=10)
    product2_id = product_factory('Product 2', 49.99, stock=5)
    
    # Verify in database
    cursor = database_transaction.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]
    
    cursor = database_transaction.execute('SELECT COUNT(*) FROM products')
    product_count = cursor.fetchone()[0]
    
    assert user_count == 2
    assert product_count == 2
    assert test_config['environment'] == 'test'


def test_complex_scenario(user_factory, product_factory, temp_directory, 
                         api_client, database_transaction):
    """
    Complex test combining database, files, and API operations.
    
    Demonstrates that fixtures from conftest.py can be mixed freely
    to create complex test scenarios.
    """
    # Create test data in database
    user_id = user_factory('Test User', 'test@example.com')
    product_id = product_factory('Test Product', 19.99, stock=100)
    
    # Create a report file
    report_file = temp_directory / 'report.txt'
    report_file.write_text(f'User {user_id} created product {product_id}')
    
    # Make API call
    response = api_client.get(f'/users/{user_id}')
    
    # Verify everything works together
    assert report_file.exists()
    assert response['status'] == 200
    
    cursor = database_transaction.execute(
        'SELECT COUNT(*) FROM products WHERE id = ?', (product_id,)
    )
    assert cursor.fetchone()[0] == 1


# ============================================================================
# CLASS-BASED TESTS USING CONFTEST FIXTURES
# ============================================================================

class TestConfTestWithClasses:
    """
    Test class demonstrating that conftest.py fixtures work with classes.
    
    Fixtures from conftest.py are available to all test methods in the class.
    """
    
    def test_class_method_1(self, sample_data):
        """First method using sample_data fixture."""
        assert len(sample_data['users']) == 3
    
    def test_class_method_2(self, sample_data, test_config):
        """Second method using multiple fixtures."""
        assert len(sample_data['products']) == 3
        assert test_config['debug'] is True
    
    def test_class_with_factory(self, user_factory):
        """Test method using a factory fixture."""
        user_id = user_factory('Class User', 'classuser@example.com')
        assert user_id > 0


# ============================================================================
# PARAMETRIZED TESTS WITH CONFTEST FIXTURES
# ============================================================================

@pytest.mark.parametrize("name,email,role", [
    ("User1", "user1@example.com", "user"),
    ("User2", "user2@example.com", "user"),
    ("Admin", "admin@example.com", "admin"),
])
def test_parametrized_with_factory(user_factory, database_transaction, 
                                   name, email, role):
    """
    Demonstrates combining parametrize with conftest.py fixtures.
    
    This test runs 3 times (once for each parameter set) and uses
    fixtures from conftest.py in each run.
    """
    user_id = user_factory(name, email, role=role)
    
    # Query the created user
    cursor = database_transaction.execute(
        'SELECT * FROM users WHERE id = ?', (user_id,)
    )
    user = cursor.fetchone()
    
    assert user['name'] == name
    assert user['email'] == email
    assert user['role'] == role


# ============================================================================
# NOTES ON FIXTURE DISCOVERY
# ============================================================================

"""
KEY POINTS DEMONSTRATED IN THIS FILE:

1. NO IMPORTS NEEDED
   - All fixtures from conftest.py are automatically available
   - No need to import test_config, user_factory, etc.

2. FIXTURE SCOPES
   - Session: test_config, session_timestamp (shared across all tests)
   - Module: database_connection, sample_data (shared within this file)
   - Function: database_transaction, temp_directory, etc. (fresh each test)

3. FIXTURE DEPENDENCIES
   - database_transaction depends on database_connection
   - user_factory depends on database_transaction
   - pytest automatically resolves the entire dependency chain

4. AUTOMATIC CLEANUP
   - Function-scoped fixtures clean up after each test
   - Module-scoped fixtures clean up after all tests in the module
   - Session-scoped fixtures clean up after entire test session

5. FIXTURE FACTORIES
   - Provide functions that create multiple instances
   - Useful when tests need to create multiple database records, files, etc.

6. WORKS WITH ALL pytest FEATURES
   - Test classes
   - Parametrized tests
   - Markers
   - Any combination

USEFUL COMMANDS:

    # See all available fixtures
    pytest --fixtures
    
    # Show fixture setup/teardown
    pytest test_conftest_demo.py --setup-show
    
    # Run with verbose output and show prints
    pytest test_conftest_demo.py -v -s
    
    # See help about fixtures
    pytest --fixtures -v
"""
