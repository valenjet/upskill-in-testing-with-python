"""
Exercise: Working with pytest Markers

Complete the TODOs below to practice using pytest markers.
Run this file with: pytest test_markers_exercise.py -v

Try different marker expressions:
    pytest test_markers_exercise.py -m "unit"
    pytest test_markers_exercise.py -m "integration"
    pytest test_markers_exercise.py -m "slow"
    pytest test_markers_exercise.py -m "unit and not slow"
"""

import pytest
import time


# =============================================================================
# PART 1: Built-in Markers
# =============================================================================

def test_basic_addition():
    """A simple passing test"""
    assert 1 + 1 == 2


# TODO: Mark this test to skip it unconditionally
# Hint: Use @pytest.mark.skip with a reason
def test_feature_not_implemented():
    """This feature isn't implemented yet"""
    assert False  # This would fail if run


# TODO: Mark this test to skip only on Windows
# Hint: Use @pytest.mark.skipif with sys.platform
# You'll need to import sys at the top of the file
def test_unix_specific_feature():
    """This only works on Unix-like systems"""
    import os
    assert os.path.exists('/tmp')


# TODO: Mark this test as expected to fail
# Hint: Use @pytest.mark.xfail with a reason
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

# TODO: Add a custom marker @pytest.mark.unit to this test
def test_string_concatenation():
    """Unit test: tests a single function in isolation"""
    result = "hello" + " " + "world"
    assert result == "hello world"


# TODO: Add a custom marker @pytest.mark.integration to this test
def test_file_read_write(tmp_path):
    """Integration test: tests multiple components together"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("integration test")
    content = test_file.read_text()
    assert content == "integration test"


# TODO: Add a custom marker @pytest.mark.slow to this test
def test_time_consuming_operation():
    """Slow test: takes significant time to run"""
    time.sleep(0.5)  # Simulate slow operation
    assert True


# TODO: Add TWO custom markers to this test: @pytest.mark.unit and @pytest.mark.slow
def test_complex_calculation():
    """Unit test that happens to be slow"""
    result = sum(range(1000000))  # Slow calculation
    assert result > 0


# =============================================================================
# PART 3: Combining Markers
# =============================================================================

# TODO: Add markers @pytest.mark.unit and @pytest.mark.smoke
# Smoke tests are quick tests that verify basic functionality
def test_basic_functionality():
    """Smoke test: quick check that basic operations work"""
    assert 2 * 2 == 4
    assert "test".upper() == "TEST"


# TODO: Add markers @pytest.mark.integration and @pytest.mark.database
# Database tests interact with a database
def test_database_connection():
    """Integration test: database operations"""
    # Simulate database connection check
    db_connected = True  # In real test, this would check actual connection
    assert db_connected is True


# =============================================================================
# PART 4: Parametrize with Markers
# =============================================================================

# TODO: Add @pytest.mark.parametrize to test multiple cases
# Test these input/output pairs: (2, 4), (3, 9), (4, 16), (5, 25)
# Also add @pytest.mark.unit marker
def test_square_numbers(input_val, expected):
    """Parametrized unit test"""
    result = input_val ** 2
    assert result == expected


# =============================================================================
# PART 5: Class-based Tests with Markers
# =============================================================================

# TODO: Add @pytest.mark.calculator marker to the entire class
class TestCalculator:
    """Group of related calculator tests"""
    
    # TODO: Add @pytest.mark.unit to this test
    def test_add(self):
        assert 2 + 3 == 5
    
    # TODO: Add @pytest.mark.unit to this test
    def test_subtract(self):
        assert 5 - 3 == 2
    
    # TODO: Add @pytest.mark.unit and @pytest.mark.slow to this test
    def test_multiply_large_numbers(self):
        result = 123456789 * 987654321
        assert result > 0


# =============================================================================
# BONUS CHALLENGE
# =============================================================================

# TODO: Create a test class called TestAPI with @pytest.mark.api marker
# Add 3 tests inside:
# 1. test_get_request - marked with @pytest.mark.unit
# 2. test_post_request - marked with @pytest.mark.integration
# 3. test_delete_request - marked with @pytest.mark.integration and @pytest.mark.slow

# Your code here:


# =============================================================================
# Don't forget to create pytest.ini to register your custom markers!
# =============================================================================

"""
Create a pytest.ini file with this content:

[pytest]
markers =
    unit: Unit tests - test individual components in isolation
    integration: Integration tests - test multiple components together
    slow: Tests that take significant time to run
    smoke: Quick smoke tests for basic functionality
    database: Tests that interact with a database
    calculator: Calculator-related tests
    api: API-related tests
"""
