"""
Solution: Working with pytest Markers

This is the complete solution for the markers exercise.
Run this file with: pytest test_markers_solution.py -v

Try different marker expressions:
    pytest test_markers_solution.py -m "unit"
    pytest test_markers_solution.py -m "integration"
    pytest test_markers_solution.py -m "slow"
    pytest test_markers_solution.py -m "unit and not slow"
"""

import pytest
import sys
import time


# =============================================================================
# PART 1: Built-in Markers
# =============================================================================

def test_basic_addition():
    """A simple passing test"""
    assert 1 + 1 == 2


@pytest.mark.skip(reason="Feature not implemented yet")
def test_feature_not_implemented():
    """This feature isn't implemented yet"""
    assert False  # This would fail if run


@pytest.mark.skipif(sys.platform == "win32", reason="Unix-specific test")
def test_unix_specific_feature():
    """This only works on Unix-like systems"""
    import os
    assert os.path.exists('/tmp')


@pytest.mark.xfail(reason="Known bug: division by zero not handled")
def test_known_bug():
    """There's a known bug in this function"""
    result = divide_by_zero(10, 0)  # This will raise an exception
    assert result == 0


def divide_by_zero(a, b):
    """Helper function with a bug"""
    return a / b  # No zero check!


# =============================================================================
# PART 2: Custom Markers
# =============================================================================

@pytest.mark.unit
def test_string_concatenation():
    """Unit test: tests a single function in isolation"""
    result = "hello" + " " + "world"
    assert result == "hello world"


@pytest.mark.integration
def test_file_read_write(tmp_path):
    """Integration test: tests multiple components together"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("integration test")
    content = test_file.read_text()
    assert content == "integration test"


@pytest.mark.slow
def test_time_consuming_operation():
    """Slow test: takes significant time to run"""
    time.sleep(0.5)  # Simulate slow operation
    assert True


@pytest.mark.unit
@pytest.mark.slow
def test_complex_calculation():
    """Unit test that happens to be slow"""
    result = sum(range(1000000))  # Slow calculation
    assert result > 0


# =============================================================================
# PART 3: Combining Markers
# =============================================================================

@pytest.mark.unit
@pytest.mark.smoke
def test_basic_functionality():
    """Smoke test: quick check that basic operations work"""
    assert 2 * 2 == 4
    assert "test".upper() == "TEST"


@pytest.mark.integration
@pytest.mark.database
def test_database_connection():
    """Integration test: database operations"""
    # Simulate database connection check
    db_connected = True  # In real test, this would check actual connection
    assert db_connected is True


# =============================================================================
# PART 4: Parametrize with Markers
# =============================================================================

@pytest.mark.unit
@pytest.mark.parametrize("input_val,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
])
def test_square_numbers(input_val, expected):
    """Parametrized unit test"""
    result = input_val ** 2
    assert result == expected


# =============================================================================
# PART 5: Class-based Tests with Markers
# =============================================================================

@pytest.mark.calculator
class TestCalculator:
    """Group of related calculator tests"""
    
    @pytest.mark.unit
    def test_add(self):
        assert 2 + 3 == 5
    
    @pytest.mark.unit
    def test_subtract(self):
        assert 5 - 3 == 2
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_multiply_large_numbers(self):
        result = 123456789 * 987654321
        assert result > 0


# =============================================================================
# BONUS CHALLENGE
# =============================================================================

@pytest.mark.api
class TestAPI:
    """API-related tests"""
    
    @pytest.mark.unit
    def test_get_request(self):
        """Test GET request handling"""
        # Simulate API GET request
        response = {"status": 200, "data": "success"}
        assert response["status"] == 200
    
    @pytest.mark.integration
    def test_post_request(self):
        """Test POST request handling"""
        # Simulate API POST request
        request_data = {"name": "test", "value": 123}
        response = {"status": 201, "id": 1}
        assert response["status"] == 201
    
    @pytest.mark.integration
    @pytest.mark.slow
    def test_delete_request(self):
        """Test DELETE request with cleanup"""
        # Simulate slow DELETE operation
        time.sleep(0.3)
        response = {"status": 204}
        assert response["status"] == 204


# =============================================================================
# Additional Examples
# =============================================================================

@pytest.mark.unit
@pytest.mark.parametrize("text,expected", [
    ("hello", "HELLO"),
    ("World", "WORLD"),
    ("PyTest", "PYTEST"),
])
def test_string_upper(text, expected):
    """Parametrized test with marker"""
    assert text.upper() == expected


@pytest.mark.integration
@pytest.mark.smoke
def test_system_health():
    """Integration smoke test for system health"""
    # Check multiple system components
    components = {
        "database": True,
        "cache": True,
        "api": True,
    }
    assert all(components.values()), "All system components should be healthy"


@pytest.mark.xfail(reason="Feature under development")
@pytest.mark.unit
def test_future_feature():
    """Test for a feature being developed"""
    # This test documents expected behavior
    result = future_function()
    assert result == "expected"


def future_function():
    """Function not yet implemented"""
    raise NotImplementedError("Coming soon!")
