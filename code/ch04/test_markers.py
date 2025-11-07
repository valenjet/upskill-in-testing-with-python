# test_markers.py
"""
Comprehensive examples of pytest markers.

This module demonstrates:
- Built-in markers: skip, skipif, xfail, parametrize
- Custom markers: slow, integration, unit, smoke, api
- Combining multiple markers
- Using markers with fixtures
- Applying markers at class level

Run examples:
    pytest test_markers.py -v                    # Run all tests
    pytest test_markers.py -m slow              # Run only slow tests
    pytest test_markers.py -m "not slow"        # Run all except slow
    pytest test_markers.py -m "unit and not slow"  # Fast unit tests only
    pytest test_markers.py -m "integration or api" # Integration or API tests
    pytest test_markers.py --markers            # List all markers
"""

import sys
import pytest
import time


# ============================================================================
# BUILT-IN MARKERS: skip
# ============================================================================

@pytest.mark.skip(reason="Feature not yet implemented")
def test_future_feature():
    """
    Unconditionally skip this test.
    
    Use skip when:
    - Feature is not yet implemented
    - Test is temporarily broken
    - Test needs to be disabled for a specific reason
    """
    # This code won't run
    assert new_feature() == expected_result


@pytest.mark.skip(reason="Waiting for API endpoint to be deployed")
def test_new_api_endpoint():
    """Skip test until external dependency is ready."""
    response = api_client.get("/v2/new-endpoint")
    assert response.status_code == 200


# ============================================================================
# BUILT-IN MARKERS: skipif
# ============================================================================

@pytest.mark.skipif(sys.version_info < (3, 10), 
                   reason="Requires Python 3.10 or higher for match statement")
def test_feature_requiring_python_310():
    """
    Conditionally skip based on Python version.
    
    This test uses the match statement introduced in Python 3.10.
    It will be skipped on Python versions < 3.10.
    """
    value = 42
    match value:
        case 42:
            result = "the answer"
        case _:
            result = "unknown"
    assert result == "the answer"


@pytest.mark.skipif(sys.platform == "win32",
                   reason="Test not applicable on Windows")
def test_unix_specific_feature():
    """
    Skip on specific platform.
    
    This demonstrates platform-specific test execution.
    On Windows, this test is skipped.
    """
    import os
    # Simple test that works on Unix-like systems
    result = os.path.exists("/tmp")
    assert result is True or result is False  # Will vary by system


@pytest.mark.skipif(sys.platform == "darwin",
                   reason="macOS has different behavior")
def test_linux_specific():
    """Skip on macOS, run on Linux and other platforms."""
    # Platform-specific test logic
    assert True


# ============================================================================
# BUILT-IN MARKERS: xfail
# ============================================================================

@pytest.mark.xfail(reason="Known issue: Bug #1234 - Division by zero not handled")
def test_known_bug():
    """
    Expect this test to fail.
    
    Use xfail when:
    - You know about a bug but haven't fixed it yet
    - You want to document the bug with a test
    - A feature has platform-specific limitations
    
    If marked xfail:
    - Test failure: marked as 'x' (expected to fail)
    - Test passes: marked as 'X' (unexpectedly passing - alerts you bug may be fixed!)
    """
    def buggy_function(x):
        return 10 / x  # Bug: doesn't handle x=0
    
    result = buggy_function(0)  # This will fail, but that's expected
    assert result == 0


@pytest.mark.xfail(sys.platform == "darwin", 
                   reason="Known to fail on macOS due to system limitation",
                   strict=False)
def test_platform_limitation():
    """
    Expected to fail on macOS.
    
    The strict=False parameter means:
    - Failure on macOS is acceptable (marked as 'x')
    - Unexpected pass will be marked but won't fail the build
    """
    # This might behave differently on macOS
    assert sys.platform != "darwin"


@pytest.mark.xfail(reason="Performance issue under investigation")
def test_performance_issue():
    """Document a performance issue that needs investigation."""
    start = time.time()
    result = slow_operation()
    elapsed = time.time() - start
    
    # We know this currently fails the performance requirement
    assert elapsed < 0.1  # Expected to fail: currently takes ~2 seconds
    assert result == "completed"


def slow_operation():
    """Simulates a slow operation."""
    time.sleep(0.5)  # Intentionally slow for demo
    return "completed"


# ============================================================================
# CUSTOM MARKERS: Categorizing Tests
# ============================================================================

@pytest.mark.unit
def test_simple_calculation():
    """
    Fast unit test.
    
    Unit tests should be:
    - Fast (milliseconds)
    - Isolated (no external dependencies)
    - Focused (test one thing)
    """
    result = 2 + 2
    assert result == 4


@pytest.mark.unit
@pytest.mark.slow
def test_complex_calculation():
    """
    Unit test that takes longer to run.
    
    Marked with both 'unit' and 'slow' to enable flexible filtering:
    - Run fast tests: -m "unit and not slow"
    - Run all unit tests: -m unit
    - Skip slow tests: -m "not slow"
    """
    time.sleep(1)  # Simulate complex calculation
    result = sum(range(1000000))
    assert result == 499999500000


@pytest.mark.integration
def test_database_connection():
    """
    Integration test - requires database.
    
    Integration tests:
    - Test interaction between components
    - May require external resources
    - Typically slower than unit tests
    """
    # Simulate database connection test
    db_available = True  # In real test, actually check database
    assert db_available is True


@pytest.mark.integration
@pytest.mark.slow
def test_full_database_workflow():
    """
    Slow integration test covering complete workflow.
    
    Combines multiple markers for precise categorization.
    """
    time.sleep(0.5)  # Simulate database operations
    
    # Simulate: insert, query, update, delete
    operations_completed = True
    assert operations_completed is True


@pytest.mark.api
def test_external_api_call():
    """
    Test that calls an external API.
    
    API tests:
    - May require network access
    - May have rate limits
    - Should be run separately in CI/CD
    """
    # Simulate API call
    api_response = {"status": "success"}
    assert api_response["status"] == "success"


@pytest.mark.smoke
def test_application_starts():
    """
    Smoke test - quick validation that basics work.
    
    Smoke tests:
    - Run first in CI/CD pipeline
    - Very fast
    - Check critical functionality
    - Fail fast if something is seriously broken
    """
    app_initialized = True
    assert app_initialized is True


@pytest.mark.smoke
def test_critical_imports():
    """Smoke test - verify critical dependencies are available."""
    try:
        import sys
        import pytest
        import time
        imports_successful = True
    except ImportError:
        imports_successful = False
    
    assert imports_successful is True


# ============================================================================
# COMBINING MARKERS WITH FIXTURES
# ============================================================================

@pytest.fixture
def database_connection():
    """
    Fixture simulating database connection.
    
    Setup: Create connection
    Teardown: Close connection
    """
    print("\n[SETUP] Connecting to database...")
    connection = {"connected": True, "data": []}
    yield connection
    print("\n[TEARDOWN] Closing database connection...")


@pytest.mark.integration
def test_with_database_fixture(database_connection):
    """
    Integration test using database fixture.
    
    The marker helps categorize this test, and the fixture
    provides necessary resources.
    """
    assert database_connection["connected"] is True
    database_connection["data"].append("test_record")
    assert len(database_connection["data"]) == 1


@pytest.fixture
def slow_resource():
    """Fixture that takes time to set up."""
    print("\n[SETUP] Initializing slow resource...")
    time.sleep(0.3)
    resource = {"ready": True}
    yield resource
    print("\n[TEARDOWN] Cleaning up slow resource...")


@pytest.mark.slow
def test_with_slow_fixture(slow_resource):
    """Test marked as slow because it uses a slow fixture."""
    assert slow_resource["ready"] is True


# ============================================================================
# MARKERS AT CLASS LEVEL
# ============================================================================

@pytest.mark.integration
class TestDatabaseOperations:
    """
    All tests in this class are integration tests.
    
    Applying a marker at the class level applies it to all
    test methods in the class automatically.
    """
    
    def test_insert(self):
        """Integration test: Insert operation."""
        result = True  # Simulate insert
        assert result is True
    
    def test_update(self):
        """Integration test: Update operation."""
        result = True  # Simulate update
        assert result is True
    
    def test_delete(self):
        """Integration test: Delete operation."""
        result = True  # Simulate delete
        assert result is True
    
    @pytest.mark.slow
    def test_bulk_operation(self):
        """
        Integration test that is also slow.
        
        This test has both markers:
        - 'integration' from the class
        - 'slow' from the method
        """
        time.sleep(0.5)  # Simulate bulk operation
        assert True


@pytest.mark.unit
class TestCalculatorFunctions:
    """All tests in this class are fast unit tests."""
    
    def test_addition(self):
        """Unit test: Addition."""
        assert 2 + 3 == 5
    
    def test_subtraction(self):
        """Unit test: Subtraction."""
        assert 5 - 3 == 2
    
    def test_multiplication(self):
        """Unit test: Multiplication."""
        assert 3 * 4 == 12
    
    def test_division(self):
        """Unit test: Division."""
        assert 10 / 2 == 5


# ============================================================================
# PARAMETRIZE WITH MARKERS
# ============================================================================

@pytest.mark.parametrize("test_input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
])
@pytest.mark.unit
def test_increment(test_input, expected):
    """
    Parametrized test with custom marker.
    
    Combines parametrize (built-in marker) with custom 'unit' marker.
    This will create 3 test instances, all marked as 'unit'.
    """
    assert test_input + 1 == expected


# ============================================================================
# CONDITIONAL MARKERS
# ============================================================================

import_available = True
try:
    import requests
except ImportError:
    import_available = False


@pytest.mark.skipif(not import_available,
                   reason="requests library not available")
@pytest.mark.api
def test_requires_requests():
    """
    Skip if optional dependency is not available.
    
    Combines skipif (conditional skip) with custom marker (api).
    """
    # This test only runs if requests is installed
    assert import_available is True


# ============================================================================
# HELPER FUNCTIONS (not tests)
# ============================================================================

def new_feature():
    """Placeholder for future feature."""
    raise NotImplementedError("Feature not yet implemented")


class api_client:
    """Mock API client."""
    @staticmethod
    def get(endpoint):
        return type('Response', (), {'status_code': 200})()


# ============================================================================
# USAGE EXAMPLES (in comments)
# ============================================================================

"""
COMMAND LINE EXAMPLES:

# Run all tests
pytest test_markers.py -v

# Run only slow tests
pytest test_markers.py -m slow -v

# Run everything except slow tests
pytest test_markers.py -m "not slow" -v

# Run only unit tests
pytest test_markers.py -m unit -v

# Run fast unit tests only
pytest test_markers.py -m "unit and not slow" -v

# Run integration or API tests
pytest test_markers.py -m "integration or api" -v

# Run smoke tests for quick validation
pytest test_markers.py -m smoke -v

# Show skip reasons
pytest test_markers.py -rs

# Show xfail details
pytest test_markers.py -rx

# List all available markers
pytest test_markers.py --markers

# Verbose output with captured prints
pytest test_markers.py -v -s

# Run specific test class
pytest test_markers.py::TestDatabaseOperations -v

# Combine multiple filters
pytest test_markers.py -m "integration and not slow" -v

TYPICAL DEVELOPMENT WORKFLOW:

1. During active development (fast feedback):
   pytest -m "unit and not slow"

2. Before committing (comprehensive unit tests):
   pytest -m unit

3. Integration testing:
   pytest -m integration

4. Quick smoke test:
   pytest -m smoke

5. Full test suite:
   pytest

CI/CD PIPELINE EXAMPLE:

Stage 1: Smoke Tests (fail fast)
  pytest -m smoke

Stage 2: Fast Unit Tests (parallel)
  pytest -m "unit and not slow" -n auto

Stage 3: All Unit Tests
  pytest -m unit

Stage 4: Integration Tests
  pytest -m integration

Stage 5: Full Suite (nightly)
  pytest
"""
