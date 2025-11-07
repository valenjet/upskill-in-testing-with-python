# Chapter 4 Solutions: Testing Frameworks

This directory contains exercises and solutions for Chapter 4: Testing Frameworks.

## Overview

These exercises will help you practice:
- Using pytest markers (built-in and custom)
- Creating and organizing fixtures
- Working with conftest.py for shared fixtures
- Applying testing framework concepts to real scenarios

## Prerequisites

- Complete reading Chapter 4
- Have pytest installed (`pip install pytest`)
- Familiarity with basic pytest usage from Chapters 1-3

## Exercises

### Exercise 1: Working with Markers

**File:** `test_markers_exercise.py`

**Learning Objectives:**
- Understand and use built-in pytest markers
- Create custom markers for test organization
- Run tests selectively using marker expressions

**Instructions:**
1. Complete the TODOs in `test_markers_exercise.py`
2. Register your custom markers in `pytest.ini`
3. Practice running tests with different marker expressions:
   ```bash
   pytest test_markers_exercise.py -m "unit"
   pytest test_markers_exercise.py -m "integration"
   pytest test_markers_exercise.py -m "slow"
   pytest test_markers_exercise.py -m "unit and not slow"
   ```

**Hints:**
- Use `@pytest.mark.skip` for tests that should be skipped
- Use `@pytest.mark.skipif` for conditional skipping
- Use `@pytest.mark.xfail` for tests expected to fail
- Custom markers are just decorators: `@pytest.mark.your_marker_name`

**Solution:** `test_markers_solution.py`

---

### Exercise 2: Creating and Using Fixtures

**File:** `test_fixtures_exercise.py`

**Learning Objectives:**
- Create fixtures with different scopes
- Use fixture factories for test data generation
- Understand fixture setup and teardown
- Compose fixtures (use fixtures within fixtures)

**Instructions:**
1. Complete the TODOs in `test_fixtures_exercise.py`
2. Implement fixtures with appropriate scopes (function, module, session)
3. Create a fixture factory that can generate multiple test objects
4. Use fixtures in your test functions

**Hints:**
- Use `@pytest.fixture` decorator
- Specify scope with `@pytest.fixture(scope="module")`
- For cleanup, use `yield` in fixtures
- Fixture factories can return functions that create objects

**Solution:** `test_fixtures_solution.py`

---

### Exercise 3: Organizing Tests with conftest.py

**File:** `conftest_exercise.py` (rename to `conftest.py` when ready to use)

**Learning Objectives:**
- Understand conftest.py purpose and discovery
- Share fixtures across multiple test files
- Organize fixtures by scope and purpose
- Use autouse fixtures appropriately

**Instructions:**
1. Review the TODOs in `conftest_exercise.py`
2. Implement shared fixtures for common test scenarios
3. Rename the file to `conftest.py` to make it active
4. Create test files that use these shared fixtures
5. Observe how pytest discovers and uses the fixtures automatically

**Hints:**
- Place conftest.py in the directory containing your tests
- Fixtures defined in conftest.py are automatically available to all tests
- Use `autouse=True` for fixtures that should run for every test
- Session-scoped fixtures in conftest.py run once for the entire test session

**Solution:** `conftest_solution.py`

---

## Running the Exercises

### Individual Exercise
```bash
cd sols/ch04
pytest test_markers_exercise.py -v
```

### All Exercises
```bash
cd sols/ch04
pytest -v
```

### With Coverage
```bash
cd sols/ch04
pytest --cov=. --cov-report=html
```

### Run Only Solutions (to verify)
```bash
cd sols/ch04
pytest test_markers_solution.py test_fixtures_solution.py -v
```

## Expected Results

### Exercise 1 (Markers)
- Should have mix of passed, skipped, and xfailed tests
- Different marker selections should run different subsets

### Exercise 2 (Fixtures)
- All tests should pass
- Should demonstrate different fixture scopes
- Should show fixture reuse and composition

### Exercise 3 (conftest.py)
- Fixtures available across multiple test files
- Proper setup and teardown behavior
- Session/module scopes working correctly

## Troubleshooting

### Markers not recognized
- Ensure markers are registered in `pytest.ini`
- Check the markers list with: `pytest --markers`

### Fixtures not found
- Verify conftest.py is in the correct directory
- Check fixture names match usage in tests
- Ensure no typos in fixture names

### Import errors
- Make sure you're running pytest from the correct directory
- Check that __init__.py files exist if needed

## Additional Practice

After completing these exercises, try:

1. **Combine concepts**: Create a test suite that uses custom markers AND shared fixtures
2. **Refactor existing tests**: Take tests from Chapters 1-3 and organize them with markers
3. **Build a test framework**: Create a conftest.py with fixtures for a small application
4. **Explore plugins**: Install pytest-xdist and run tests in parallel
5. **Create custom markers**: Design a marker system for your own projects (e.g., @pytest.mark.database, @pytest.mark.api)

## Resources

- pytest documentation: https://docs.pytest.org
- Markers: https://docs.pytest.org/en/stable/how-to/mark.html
- Fixtures: https://docs.pytest.org/en/stable/how-to/fixtures.html
- conftest.py: https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py

## Next Steps

After completing Chapter 4 exercises:
- Move on to Chapter 5: Code Analysis
- Practice integrating coverage analysis with pytest-cov
- Learn about code quality tools and CI/CD integration
