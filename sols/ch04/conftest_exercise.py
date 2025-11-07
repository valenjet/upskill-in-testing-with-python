"""
Exercise: Organizing Tests with conftest.py

This file demonstrates how to use conftest.py for sharing fixtures.
Rename this file to 'conftest.py' to activate it.

Complete the TODOs below to practice creating shared fixtures.

INSTRUCTIONS:
1. Complete all TODOs in this file
2. Rename this file from 'conftest_exercise.py' to 'conftest.py'
3. Create test files that use these fixtures (or use existing test files)
4. Run pytest and observe how fixtures are automatically discovered

NOTE: conftest.py files are special - pytest automatically discovers them
and makes their fixtures available to all tests in the directory and subdirectories.
"""

import pytest
import tempfile
from pathlib import Path


# =============================================================================
# PART 1: Session-Scoped Fixtures
# =============================================================================

# TODO: Create a session-scoped fixture called "test_config"
# It should return a dictionary with test configuration:
# {"environment": "test", "debug": True, "api_url": "http://localhost:8000"}
# Hint: Use @pytest.fixture(scope="session")


# =============================================================================
# PART 2: Module-Scoped Database Fixture
# =============================================================================

# TODO: Create a module-scoped fixture called "db_connection"
# Simulate a database connection:
# 1. Print "Opening database connection..." at setup
# 2. Yield a dictionary: {"connected": True, "db_name": "test_db"}
# 3. Print "Closing database connection..." at teardown
# Hint: Use @pytest.fixture(scope="module") and yield


# =============================================================================
# PART 3: Function-Scoped Data Fixtures
# =============================================================================

# TODO: Create a fixture called "sample_users" (function scope)
# Return a list of user dictionaries:
# [
#     {"id": 1, "name": "Alice", "email": "alice@example.com"},
#     {"id": 2, "name": "Bob", "email": "bob@example.com"},
#     {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
# ]


# TODO: Create a fixture called "sample_products" (function scope)
# Return a list of product dictionaries:
# [
#     {"id": 1, "name": "Laptop", "price": 999.99},
#     {"id": 2, "name": "Mouse", "price": 29.99},
#     {"id": 3, "name": "Keyboard", "price": 79.99}
# ]


# =============================================================================
# PART 4: Fixture Factories
# =============================================================================

# TODO: Create a fixture factory called "create_user"
# Return a function that creates user dictionaries with:
# - name (required parameter)
# - email (required parameter)
# - id (auto-generated using a counter or random number)


# TODO: Create a fixture factory called "create_order"
# Return a function that creates order dictionaries with:
# - user_id (required parameter)
# - product_ids (required parameter, list of product IDs)
# - total (required parameter)
# - order_id (auto-generated)


# =============================================================================
# PART 5: Temporary File System Fixtures
# =============================================================================

# TODO: Create a fixture called "temp_workspace"
# Use tmp_path to create a temporary directory structure:
# - temp_dir/
#   - data/
#   - output/
#   - config/
# Yield the temp_dir path
# Hint: You can use tmp_path fixture as a parameter


# =============================================================================
# PART 6: Autouse Fixtures
# =============================================================================

# TODO: Create an autouse fixture called "test_timer"
# This fixture should:
# 1. Record the start time before the test
# 2. Yield
# 3. Calculate and print the test duration after the test
# Hint: Use @pytest.fixture(autouse=True) and import time


# =============================================================================
# PART 7: Fixtures with Dependencies
# =============================================================================

# TODO: Create a fixture called "authenticated_user"
# This fixture should:
# 1. Use the "create_user" fixture to create a user
# 2. Add an "authenticated" field set to True
# 3. Add a "token" field with value "test-token-12345"
# 4. Return the authenticated user dictionary


# =============================================================================
# BONUS CHALLENGE
# =============================================================================

# TODO: Create a fixture called "api_client" that:
# 1. Uses "test_config" fixture to get the API URL
# 2. Creates a mock API client dictionary with:
#    - "base_url" from config
#    - "headers" with {"Authorization": "Bearer test-token"}
#    - "timeout" set to 30
# 3. Returns the client

# TODO: Create a fixture called "database_with_data" that:
# 1. Uses "db_connection" fixture
# 2. Uses "sample_users" fixture
# 3. Simulates inserting users into the database
# 4. Returns a dictionary with both connection and users


# =============================================================================
# TIPS
# =============================================================================

"""
Remember:
1. conftest.py is automatically discovered by pytest
2. Fixtures in conftest.py are available to all tests in the directory
3. You can have multiple conftest.py files in different directories
4. Fixtures can use other fixtures from the same conftest.py
5. Use appropriate scopes to optimize test performance

After completing this file:
1. Rename it to 'conftest.py'
2. Create test files (e.g., test_with_conftest.py) that use these fixtures
3. Run: pytest -v --setup-show

Example test file content:

def test_config(test_config):
    assert test_config["environment"] == "test"

def test_users(sample_users):
    assert len(sample_users) == 3

def test_create_user(create_user):
    user = create_user("David", "david@example.com")
    assert user["name"] == "David"
"""
