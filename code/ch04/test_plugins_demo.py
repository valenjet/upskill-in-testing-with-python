"""
Demonstration of pytest Plugins

This file demonstrates the usage of popular pytest plugins:
- pytest-timeout: Prevent tests from running indefinitely (optional - tests work without it)
- pytest-mock: Enhanced mocking capabilities (optional)
- Built-in plugins and features (always available)

To run these tests with plugins:
    pytest test_plugins_demo.py
    pytest test_plugins_demo.py -v --timeout=5  # if pytest-timeout installed
    pytest test_plugins_demo.py -n auto  # if pytest-xdist installed
"""

import pytest
import sys
import time

# Check if pytest-timeout is available
try:
    import pytest_timeout
    HAS_TIMEOUT = True
except ImportError:
    HAS_TIMEOUT = False


# ============================================================================
# pytest-timeout Plugin Examples
# ============================================================================
# These tests demonstrate timeout functionality if pytest-timeout is installed
# They will be skipped if the plugin is not available

@pytest.mark.skipif(not HAS_TIMEOUT, reason="pytest-timeout not installed")
@pytest.mark.timeout(2)
def test_completes_within_timeout():
    """Test that completes well within the timeout limit."""
    time.sleep(0.5)
    assert True


@pytest.mark.skipif(not HAS_TIMEOUT, reason="pytest-timeout not installed")
@pytest.mark.timeout(1)
def test_approaches_timeout():
    """Test that takes nearly the full timeout period."""
    time.sleep(0.8)
    assert True


# This test will fail with a timeout error if uncommented
# @pytest.mark.skipif(not HAS_TIMEOUT, reason="pytest-timeout not installed")
# @pytest.mark.timeout(1)
# def test_exceeds_timeout():
#     """This test would timeout and fail."""
#     time.sleep(2)
#     assert True


@pytest.mark.skipif(not HAS_TIMEOUT, reason="pytest-timeout not installed")
@pytest.mark.timeout(5, method="thread")
def test_with_thread_timeout():
    """
    Test using thread-based timeout.
    
    Thread-based timeouts are more reliable but may not interrupt
    certain blocking operations like C extensions.
    """
    for i in range(5):
        time.sleep(0.5)
    assert True


# ============================================================================
# pytest-mock Plugin Examples (if installed)
# ============================================================================

# Uncomment these tests if pytest-mock is installed:
# pip install pytest-mock

# def test_simple_mock(mocker):
#     """Demonstrate basic mocking with pytest-mock."""
#     mock_function = mocker.Mock(return_value=42)
#     result = mock_function()
#     assert result == 42
#     mock_function.assert_called_once()


# def test_patch_with_mocker(mocker):
#     """Demonstrate patching with pytest-mock."""
#     mocker.patch('time.sleep', return_value=None)
#     # Now time.sleep() does nothing
#     start = time.time()
#     time.sleep(10)  # This won't actually sleep
#     elapsed = time.time() - start
#     assert elapsed < 0.1  # Virtually instant


# def test_spy_function(mocker):
#     """Demonstrate spy functionality."""
#     spy = mocker.spy(time, 'sleep')
#     time.sleep(0.1)
#     spy.assert_called_once_with(0.1)


# ============================================================================
# Parallel Execution Examples (pytest-xdist)
# ============================================================================

@pytest.mark.parametrize("value", range(10))
def test_parallel_safe(value):
    """
    Test that can safely run in parallel.
    
    This test has no side effects and doesn't depend on shared state,
    making it ideal for parallel execution with pytest-xdist.
    
    Run with: pytest -n auto test_plugins_demo.py
    """
    result = value * 2
    assert result == value + value


def test_parallel_with_fixture(tmp_path):
    """
    Test using tmp_path fixture in parallel execution.
    
    Each worker gets its own tmp_path, so parallel execution is safe.
    """
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello from parallel test")
    assert test_file.read_text() == "Hello from parallel test"


# Mark tests that should not run in parallel
@pytest.mark.xdist_group(name="sequential")
def test_requires_sequential_1():
    """
    Test that should run sequentially with others in the same group.
    
    Use xdist_group when tests share resources or have ordering requirements.
    """
    assert True


@pytest.mark.xdist_group(name="sequential")
def test_requires_sequential_2():
    """Another test in the sequential group."""
    assert True


# ============================================================================
# Built-in pytest Features (no plugins required)
# ============================================================================

def test_with_capsys(capsys):
    """
    Demonstrate capsys fixture for capturing stdout/stderr.
    
    This is a built-in pytest fixture, no plugin needed.
    """
    print("Hello, World!")
    print("Error message", file=__import__('sys').stderr)
    
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
    assert "Error message" in captured.err


def test_with_tmp_path(tmp_path):
    """
    Demonstrate tmp_path fixture for temporary directories.
    
    This is a built-in pytest fixture, no plugin needed.
    """
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")
    
    assert test_file.exists()
    assert test_file.read_text() == "Test content"


def test_with_monkeypatch(monkeypatch):
    """
    Demonstrate monkeypatch fixture for modifying environment.
    
    This is a built-in pytest fixture, no plugin needed.
    """
    # Set an environment variable
    monkeypatch.setenv("TEST_VAR", "test_value")
    
    import os
    assert os.getenv("TEST_VAR") == "test_value"
    
    # Modify an attribute
    class MyClass:
        value = 10
    
    monkeypatch.setattr(MyClass, "value", 42)
    assert MyClass.value == 42


# ============================================================================
# Combining Multiple Plugin Features
# ============================================================================

# Note: These tests demonstrate the concepts even without plugins installed
# With pytest-timeout installed, each test would have its own timeout

@pytest.mark.parametrize("duration", [0.1, 0.2, 0.3])
def test_combining_timeout_and_parametrize(duration):
    """
    Test combining timeout marker with parametrization.
    
    Each parametrized test would have its own timeout if pytest-timeout is installed.
    Without the plugin, tests still run normally.
    """
    time.sleep(duration)
    assert duration < 1.0


def test_timeout_with_fixtures(tmp_path, capsys):
    """
    Test combining timeout with multiple fixtures.
    
    This test works with or without pytest-timeout installed.
    """
    test_file = tmp_path / "output.txt"
    print(f"Writing to {test_file}")
    test_file.write_text("Test data")
    
    captured = capsys.readouterr()
    assert "Writing to" in captured.out
    assert test_file.exists()


# ============================================================================
# Plugin Configuration Examples
# ============================================================================

# These tests demonstrate behavior affected by pytest.ini configuration

@pytest.mark.slow
def test_marked_as_slow():
    """
    Test marked as slow (marker defined in pytest.ini).
    
    Run slow tests: pytest -m slow
    Skip slow tests: pytest -m "not slow"
    """
    time.sleep(1)
    assert True


@pytest.mark.integration
def test_marked_as_integration():
    """
    Test marked as integration (marker defined in pytest.ini).
    
    Run integration tests: pytest -m integration
    """
    assert True


# ============================================================================
# Demonstrating Test Output and Reporting
# ============================================================================

def test_verbose_output():
    """
    Test to demonstrate verbose output options.
    
    Run with: pytest -v test_plugins_demo.py
    Run with: pytest -vv test_plugins_demo.py
    """
    assert 1 + 1 == 2


def test_with_detailed_failure():
    """
    Test that demonstrates detailed failure reporting.
    
    Uncomment to see pytest's detailed assertion introspection.
    """
    data = {"name": "Alice", "age": 30, "city": "Boston"}
    assert "name" in data
    assert data["name"] == "Alice"
    # Uncomment to see detailed failure:
    # assert data["age"] == 25  # Will show full dict and highlight difference


@pytest.mark.skipif(not HAS_TIMEOUT, reason="pytest-timeout 2.0+ required")
def test_requires_timeout_plugin():
    """
    Test that only runs if pytest-timeout plugin is installed.
    Demonstrates conditional test execution based on plugin availability.
    """
    assert HAS_TIMEOUT is True


# ============================================================================
# Performance Testing (demonstrates pytest-benchmark if installed)
# ============================================================================

# Uncomment if pytest-benchmark is installed:
# pip install pytest-benchmark

# def test_performance_example(benchmark):
#     """Benchmark a function's performance."""
#     def function_to_benchmark():
#         return sum(range(1000))
#     
#     result = benchmark(function_to_benchmark)
#     assert result == 499500


# ============================================================================
# Helper Notes
# ============================================================================

"""
Common Plugin Commands:

1. Run with timeout for all tests:
   pytest --timeout=30

2. Run tests in parallel:
   pytest -n auto
   pytest -n 4  # Use 4 workers

3. Run with coverage:
   pytest --cov=myproject --cov-report=html

4. Combine multiple plugins:
   pytest -n auto --timeout=60 --cov=myproject

5. Show installed plugins:
   pytest --version

6. List all available fixtures:
   pytest --fixtures

7. Run with detailed output:
   pytest -vv --tb=long

8. Generate HTML report (requires pytest-html):
   pytest --html=report.html --self-contained-html
"""
