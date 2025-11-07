"""
Shared test fixtures for Chapter 4 examples.

This conftest.py provides common fixtures used across multiple test modules,
demonstrating pytest's fixture discovery and sharing mechanism.

Fixtures are organized by scope:
- Session-scoped: Created once for entire test session
- Module-scoped: Created once per test module
- Function-scoped: Created fresh for each test function

Usage:
    These fixtures are automatically discovered by pytest and available
    to all test files in this directory without requiring imports.
"""
import pytest
import tempfile
import sqlite3
from pathlib import Path
from datetime import datetime


# ============================================================================
# SESSION-SCOPED FIXTURES
# ============================================================================
# These are expensive to create and shared across all tests

@pytest.fixture(scope="session")
def test_config():
    """
    Application configuration for testing.
    
    Session-scoped: Created once and shared across all tests.
    Useful for configuration that doesn't change between tests.
    """
    return {
        'environment': 'test',
        'debug': True,
        'database_url': 'sqlite:///:memory:',
        'cache_enabled': False,
        'timeout': 30,
        'max_retries': 3
    }


@pytest.fixture(scope="session")
def session_timestamp():
    """
    Timestamp when the test session started.
    
    Session-scoped: Same value used across all tests.
    Useful for logging and debugging test runs.
    """
    return datetime.now()


# ============================================================================
# MODULE-SCOPED FIXTURES
# ============================================================================
# These are created once per test module (file)

@pytest.fixture(scope="module")
def database_connection():
    """
    In-memory SQLite database connection.
    
    Module-scoped: Created once per test module, shared by all tests
    in that module. Useful for expensive database setup.
    
    Provides:
        sqlite3.Connection: Active database connection
    
    Cleanup:
        Connection closed automatically after module tests complete
    """
    # Setup
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row  # Enable column access by name
    
    # Create schema
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    
    yield conn
    
    # Teardown
    conn.close()


@pytest.fixture(scope="module")
def sample_data():
    """
    Sample data for testing.
    
    Module-scoped: Created once per test module.
    Provides immutable test data that can be safely shared.
    
    Returns:
        dict: Dictionary containing sample users and products
    """
    return {
        'users': [
            {'name': 'Alice', 'email': 'alice@example.com', 'role': 'admin'},
            {'name': 'Bob', 'email': 'bob@example.com', 'role': 'user'},
            {'name': 'Charlie', 'email': 'charlie@example.com', 'role': 'user'},
        ],
        'products': [
            {'name': 'Laptop', 'price': 999.99, 'stock': 10},
            {'name': 'Mouse', 'price': 29.99, 'stock': 50},
            {'name': 'Keyboard', 'price': 79.99, 'stock': 30},
        ]
    }


# ============================================================================
# FUNCTION-SCOPED FIXTURES
# ============================================================================
# These are created fresh for each test function

@pytest.fixture
def database_transaction(database_connection):
    """
    Clean database transaction for each test.
    
    Function-scoped: Creates a new transaction for each test and rolls
    back after the test completes. Ensures test isolation.
    
    Depends on:
        database_connection: Module-scoped database connection
    
    Provides:
        sqlite3.Connection: Connection with active transaction
    
    Cleanup:
        Transaction rolled back automatically after test
    """
    # Begin transaction
    database_connection.execute('BEGIN')
    
    yield database_connection
    
    # Rollback transaction (undo all changes made during test)
    database_connection.rollback()


@pytest.fixture
def temp_directory():
    """
    Temporary directory for test file operations.
    
    Function-scoped: Creates a new temporary directory for each test.
    Automatically cleaned up after the test completes.
    
    Provides:
        Path: Pathlib Path object pointing to temporary directory
    
    Cleanup:
        Directory and all contents deleted automatically
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)
    # Directory automatically deleted when context exits


@pytest.fixture
def temp_file(temp_directory):
    """
    Temporary file for testing.
    
    Function-scoped: Creates a temporary file in the temp directory.
    
    Depends on:
        temp_directory: Temporary directory fixture
    
    Provides:
        Path: Pathlib Path object pointing to temporary file
    
    Cleanup:
        File deleted when temp_directory is cleaned up
    """
    file_path = temp_directory / "test_file.txt"
    file_path.write_text("Initial content for testing")
    return file_path


@pytest.fixture
def api_client(test_config):
    """
    Mock API client for testing.
    
    Function-scoped: Creates a fresh mock client for each test.
    
    Depends on:
        test_config: Session-scoped configuration
    
    Provides:
        MockAPIClient: Configured mock API client
    """
    client = MockAPIClient(test_config)
    yield client
    client.cleanup()


# ============================================================================
# FIXTURE FACTORIES
# ============================================================================
# These return functions that create instances on demand

@pytest.fixture
def user_factory(database_transaction):
    """
    Factory for creating test users in the database.
    
    Function-scoped: Returns a function to create users.
    Each user is created in the database transaction, which
    is automatically rolled back after the test.
    
    Depends on:
        database_transaction: Database with active transaction
    
    Usage:
        def test_example(user_factory):
            admin = user_factory('Admin', 'admin@example.com', role='admin')
            user = user_factory('User', 'user@example.com')
    
    Returns:
        callable: Function that creates users
    """
    created_ids = []
    
    def _create_user(name, email, role='user'):
        """Create a user in the database and return the user ID."""
        cursor = database_transaction.execute(
            'INSERT INTO users (name, email, role) VALUES (?, ?, ?)',
            (name, email, role)
        )
        user_id = cursor.lastrowid
        created_ids.append(user_id)
        return user_id
    
    yield _create_user
    
    # No explicit cleanup needed - transaction rollback handles it


@pytest.fixture
def product_factory(database_transaction):
    """
    Factory for creating test products in the database.
    
    Function-scoped: Returns a function to create products.
    
    Depends on:
        database_transaction: Database with active transaction
    
    Usage:
        def test_example(product_factory):
            laptop = product_factory('Laptop', 999.99, stock=5)
            mouse = product_factory('Mouse', 29.99)
    
    Returns:
        callable: Function that creates products
    """
    def _create_product(name, price, stock=0):
        """Create a product in the database and return the product ID."""
        cursor = database_transaction.execute(
            'INSERT INTO products (name, price, stock) VALUES (?, ?, ?)',
            (name, price, stock)
        )
        return cursor.lastrowid
    
    return _create_product


@pytest.fixture
def file_factory(temp_directory):
    """
    Factory for creating multiple test files.
    
    Function-scoped: Returns a function to create files.
    
    Depends on:
        temp_directory: Temporary directory for files
    
    Usage:
        def test_example(file_factory):
            file1 = file_factory('data1.txt', 'content 1')
            file2 = file_factory('data2.txt', 'content 2')
    
    Returns:
        callable: Function that creates files
    """
    created_files = []
    
    def _create_file(filename, content=''):
        """Create a file and return its path."""
        file_path = temp_directory / filename
        file_path.write_text(content)
        created_files.append(file_path)
        return file_path
    
    yield _create_file
    
    # Files automatically cleaned up when temp_directory is removed


# ============================================================================
# AUTOUSE FIXTURES
# ============================================================================
# These run automatically for all tests without being explicitly requested

@pytest.fixture(autouse=True)
def test_logger():
    """
    Set up logging for each test.
    
    Autouse: Runs automatically for every test without being requested.
    Useful for setup that should apply to all tests.
    """
    # Setup - runs before each test
    import logging
    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)
    
    yield
    
    # Teardown - runs after each test
    # Could add cleanup code here if needed


# ============================================================================
# HELPER CLASSES
# ============================================================================

class MockAPIClient:
    """
    Mock API client for testing.
    
    Simulates an API client without making actual network requests.
    """
    
    def __init__(self, config):
        self.config = config
        self.requests_made = []
    
    def get(self, endpoint):
        """Simulate a GET request."""
        self.requests_made.append(('GET', endpoint))
        return {
            'status': 200,
            'data': f'Mock response for GET {endpoint}'
        }
    
    def post(self, endpoint, data):
        """Simulate a POST request."""
        self.requests_made.append(('POST', endpoint, data))
        return {
            'status': 201,
            'data': f'Mock response for POST {endpoint}'
        }
    
    def cleanup(self):
        """Clean up resources."""
        self.requests_made.clear()


# ============================================================================
# FIXTURE INTROSPECTION
# ============================================================================
# To see all fixtures available from this conftest.py, run:
#   pytest --fixtures
#
# To see fixture setup/teardown in action, run with -v -s:
#   pytest -v -s
#
# To see which fixtures a test uses, run with --setup-show:
#   pytest --setup-show
