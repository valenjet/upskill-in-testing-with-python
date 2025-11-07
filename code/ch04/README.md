# Chapter 4: Testing Frameworks

This directory contains code examples for Chapter 4 of "Upskill in Testing with Python".

## Files

### test_user_registration.py

An acceptance testing example demonstrating the Given-When-Then approach to testing. This example illustrates:

- **Acceptance Testing Principles**: How to write tests that verify business requirements
- **Given-When-Then Format**: Clear test structure that communicates intent to all stakeholders
- **Multiple Test Scenarios**: Success and failure cases for user registration
- **Self-Contained Example**: Includes both the test class and the system under test

#### Running the Tests

```bash
# Run all tests in the file
pytest code/ch04/test_user_registration.py

# Run with verbose output
pytest code/ch04/test_user_registration.py -v

# Run a specific test
pytest code/ch04/test_user_registration.py::TestUserRegistration::test_successful_registration_with_valid_email_and_password
```

#### Test Scenarios Covered

1. **Successful Registration**: Valid email and strong password
2. **Invalid Email Format**: Registration fails with malformed email
3. **Weak Password**: Registration fails when password is too short
4. **Duplicate Email**: Registration fails when email already exists

---

### test_markers.py

Comprehensive examples of pytest markers including built-in and custom markers. This example demonstrates:

- **Built-in Markers**: skip, skipif, xfail, parametrize
- **Custom Markers**: slow, integration, unit, smoke, api
- **Marker Combinations**: Using multiple markers on a single test
- **Class-Level Markers**: Applying markers to all tests in a class
- **Conditional Execution**: Running tests based on marker selection

#### Running the Tests

```bash
# Run all tests
pytest code/ch04/test_markers.py -v

# Run only unit tests
pytest code/ch04/test_markers.py -m unit -v

# Run fast unit tests (exclude slow ones)
pytest code/ch04/test_markers.py -m "unit and not slow" -v

# Run integration or API tests
pytest code/ch04/test_markers.py -m "integration or api" -v

# Run only smoke tests for quick validation
pytest code/ch04/test_markers.py -m smoke -v

# Run all tests except slow ones
pytest code/ch04/test_markers.py -m "not slow" -v

# Show skip reasons
pytest code/ch04/test_markers.py -rs

# Show expected failure details
pytest code/ch04/test_markers.py -rx

# List all available markers
pytest code/ch04/test_markers.py --markers
```

#### Markers Demonstrated

**Built-in Markers:**
- `skip` - Unconditionally skip a test
- `skipif` - Conditionally skip based on a boolean expression
- `xfail` - Mark a test as expected to fail
- `parametrize` - Run a test with multiple parameter sets

**Custom Markers:**
- `unit` - Fast, isolated unit tests
- `integration` - Tests requiring external resources
- `slow` - Tests that take longer to execute
- `smoke` - Quick validation tests
- `api` - Tests that interact with external APIs

#### Typical Workflows

**Development (fast feedback):**
```bash
pytest -m "unit and not slow"
```

**Before committing:**
```bash
pytest -m unit
```

**Integration testing:**
```bash
pytest -m integration
```

**Quick smoke test:**
```bash
pytest -m smoke
```

---

### pytest.ini

Configuration file for pytest that:

- **Registers Custom Markers**: Defines all custom markers with descriptions
- **Configures Test Discovery**: Sets patterns for finding tests
- **Sets Output Options**: Configures reporting and display preferences
- **Enforces Standards**: Enables strict marker checking

This configuration ensures pytest recognizes all markers and provides helpful error messages.

---

### conftest.py

Shared fixtures and configuration for all Chapter 4 tests. This file demonstrates:

- **Session-Scoped Fixtures**: Expensive resources created once per test session
- **Module-Scoped Fixtures**: Resources shared across all tests in a module
- **Function-Scoped Fixtures**: Fresh resources for each test
- **Fixture Factories**: Functions that create multiple instances
- **Autouse Fixtures**: Fixtures that run automatically for all tests
- **Fixture Dependencies**: Fixtures that depend on other fixtures

#### Key Fixtures Provided

**Session-Scoped:**
- `test_config` - Application configuration for testing
- `session_timestamp` - Timestamp when test session started

**Module-Scoped:**
- `database_connection` - In-memory SQLite database with schema
- `sample_data` - Sample users and products data

**Function-Scoped:**
- `database_transaction` - Clean database transaction (auto-rollback)
- `temp_directory` - Temporary directory (auto-cleanup)
- `temp_file` - Temporary file with initial content
- `api_client` - Mock API client for testing

**Fixture Factories:**
- `user_factory` - Creates users in database
- `product_factory` - Creates products in database
- `file_factory` - Creates files in temp directory

#### Running the Tests

```bash
# See all available fixtures from conftest.py
pytest --fixtures

# Run tests showing fixture setup/teardown
pytest code/ch04/test_conftest_demo.py --setup-show

# Run specific test to see fixture chain
pytest code/ch04/test_conftest_demo.py::test_combining_multiple_fixtures --setup-show -v
```

---

### test_conftest_demo.py

Comprehensive demonstration of using fixtures from conftest.py. This file shows:

- **Automatic Fixture Discovery**: No imports needed for conftest.py fixtures
- **Fixture Scopes**: Using session, module, and function-scoped fixtures
- **Fixture Dependencies**: Fixtures that depend on other fixtures
- **Fixture Factories**: Creating multiple instances with factory functions
- **Transaction Isolation**: Database changes rolled back after each test
- **Temporary Files**: Working with temporary directories and files
- **Combining Fixtures**: Using multiple fixtures in complex test scenarios

#### Running the Tests

```bash
# Run all conftest demo tests
pytest code/ch04/test_conftest_demo.py -v

# Show fixture setup/teardown for all tests
pytest code/ch04/test_conftest_demo.py --setup-show

# Run with verbose output and show prints
pytest code/ch04/test_conftest_demo.py -v -s

# Run specific test showing complete fixture chain
pytest code/ch04/test_conftest_demo.py::test_combining_multiple_fixtures --setup-show
```

#### Test Categories

**Session and Module Fixtures (Tests 1-5):**
- Using shared configuration
- Working with module-scoped data
- Database connection availability

**Transaction Isolation (Tests 6-7):**
- Database changes in one test don't affect others
- Automatic rollback after each test

**Fixture Factories (Tests 8-10):**
- Creating multiple users with user_factory
- Creating multiple products with product_factory
- Querying factory-created data

**Temporary Files (Tests 11-13):**
- Working with temporary directories
- Using pre-created temp files
- Creating multiple files with file_factory

**API Client (Tests 14-15):**
- Mock GET requests
- Mock POST requests

**Complex Scenarios (Tests 16-17):**
- Combining multiple fixtures
- Database + files + API in one test

**Class-Based Tests (Tests 18-20):**
- Using fixtures in test classes
- Multiple fixtures per method

**Parametrized Tests (Tests 21-23):**
- Combining parametrize with conftest fixtures
- Tests run multiple times with different parameters

#### Key Learning Points

1. **No Imports Required**: Fixtures from conftest.py are automatically available
2. **Scope Matters**: Session fixtures shared across all tests, function fixtures fresh each time
3. **Automatic Cleanup**: pytest handles teardown based on fixture scope
4. **Dependency Resolution**: pytest automatically provides all required fixtures
5. **Factory Pattern**: Use factories when tests need multiple instances
6. **Transaction Isolation**: Use database transactions for test isolation

---

## Learning Objectives

This chapter's examples demonstrate:

1. **Acceptance Testing**: Writing tests that verify business requirements
2. **Test Organization**: Using markers to categorize and organize tests
3. **Selective Execution**: Running specific test subsets based on markers
4. **Test Documentation**: Using docstrings and marker names to document test intent
5. **pytest Configuration**: Setting up pytest.ini for project-wide settings
6. **CI/CD Integration**: Strategies for running different test categories in pipelines

---

## Expected Test Results

When running all Chapter 4 tests:

```bash
pytest code/ch04/ -v
```

**test_user_registration.py:**
- ✅ 4 passed - All registration scenarios work correctly

**test_markers.py:**
- ✅ 22 passed - All active tests pass
- ⏭️ 4 skipped - Tests skipped due to conditions (skip/skipif markers)
- ✖️ 3 xfailed - Tests expected to fail (xfail marker, demonstrating known issues)

**test_conftest_demo.py:**
- ✅ 23 passed - All conftest fixture examples work correctly
- Demonstrates: session (2 tests), module (3 tests), function-scoped fixtures (18 tests)
- Shows: transaction isolation, fixture factories, temporary files, fixture combinations

**test_plugins_demo.py:**
- ✅ 24 passed - All tests that don't require optional plugins
- ⏭️ 4 skipped - Tests requiring pytest-timeout (if not installed)
- Demonstrates: timeout concepts, parallel execution, built-in fixtures
- Optional: Install pytest-timeout to run all 28 tests

**Total (without optional plugins):**
- ✅ 73 passed
- ⏭️ 8 skipped (4 markers + 4 plugins)
- ✖️ 3 xfailed

**Total (with pytest-timeout installed):**
- ✅ 77 passed
- ⏭️ 4 skipped (only marker examples)
- ✖️ 3 xfailed

---

## Plugin Installation (Optional but Recommended)

To get the most out of Chapter 4 examples, install these plugins:

```bash
# Essential plugins for development
pip install pytest-timeout pytest-xdist

# Enhanced features
pip install pytest-mock pytest-cov

# Reporting and UI
pip install pytest-html pytest-sugar

# All at once
pip install pytest-timeout pytest-xdist pytest-mock pytest-cov pytest-html pytest-sugar
```

### What Each Plugin Does

- **pytest-timeout**: Prevents tests from hanging indefinitely
- **pytest-xdist**: Runs tests in parallel for faster execution
- **pytest-mock**: Provides mocker fixture for easier mocking
- **pytest-cov**: Code coverage reporting (covered in Chapter 5)
- **pytest-html**: Generates attractive HTML test reports
- **pytest-sugar**: Enhanced progress bar and output

---

---

## test_plugins_demo.py

Demonstrations of pytest plugin usage and built-in features. This example shows:

- **pytest-timeout**: Preventing tests from running indefinitely
- **pytest-xdist**: Parallel test execution concepts
- **pytest-mock**: Enhanced mocking (examples provided)
- **Built-in Fixtures**: capsys, tmp_path, monkeypatch
- **Plugin Configuration**: Examples of configuring plugins via pytest.ini
- **Combining Features**: Using multiple plugins together

### Running the Tests

```bash
# Run all plugin demos
pytest code/ch04/test_plugins_demo.py -v

# Run with timeout enabled (requires pytest-timeout)
pytest code/ch04/test_plugins_demo.py --timeout=10

# Run in parallel (requires pytest-xdist)
pytest code/ch04/test_plugins_demo.py -n auto

# Combine timeout and parallel execution
pytest code/ch04/test_plugins_demo.py -n 4 --timeout=30

# Run only tests with specific marker
pytest code/ch04/test_plugins_demo.py -m slow
```

### Plugin Installation

To use all features in this demo, install the plugins:

```bash
# Install pytest-timeout for test timeouts
pip install pytest-timeout

# Install pytest-xdist for parallel execution
pip install pytest-xdist

# Install pytest-mock for enhanced mocking (optional)
pip install pytest-mock

# Install pytest-cov for coverage (covered in Chapter 5)
pip install pytest-cov

# Install all at once
pip install pytest-timeout pytest-xdist pytest-mock pytest-cov
```

### Features Demonstrated

**pytest-timeout:**
- Setting timeouts per test with `@pytest.mark.timeout(seconds)`
- Thread-based vs signal-based timeouts
- Global timeout configuration
- Preventing hung tests

**pytest-xdist:**
- Tests designed for parallel execution
- Using `xdist_group` for sequential execution when needed
- Fixture safety in parallel execution
- Load balancing strategies

**Built-in Fixtures (no plugins needed):**
- `capsys` - Capturing stdout/stderr
- `tmp_path` - Temporary directories and files
- `monkeypatch` - Modifying environment and attributes
- `request` - Accessing test context

**Plugin Configuration:**
- Setting default timeouts in pytest.ini
- Registering markers for plugin features
- Command-line option combinations

### Key Plugin Concepts

1. **Plugin Discovery**: pytest automatically loads installed plugins
2. **Configuration**: Plugins can be configured via pytest.ini, pyproject.toml, or command-line
3. **Composability**: Plugins work together seamlessly
4. **Extensibility**: Custom plugins can be created for specific needs
5. **Community**: Large ecosystem of plugins for various needs

### Common Plugin Workflows

**Development (fast tests with timeout safety):**
```bash
pytest -m "unit and not slow" --timeout=5
```

**CI/CD (parallel with coverage):**
```bash
pytest -n auto --timeout=300 --cov=myproject --cov-report=xml
```

**Debugging (verbose with no timeout):**
```bash
pytest -vv --timeout=0 -s
```

**Integration tests (sequential with longer timeout):**
```bash
pytest -m integration --timeout=600
```

### Notes

- Some tests in this file include commented examples for optional plugins
- Uncomment pytest-mock examples if you have pytest-mock installed
- The timeout tests use safe durations to avoid actual timeouts
- Parallel execution examples use fixtures safe for concurrent access

---

