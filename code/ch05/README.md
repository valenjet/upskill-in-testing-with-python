# Chapter 5: Code Analysis - Code Examples

This directory contains code examples demonstrating code coverage analysis with pytest-cov, linting with flake8, and code formatting with black, as covered in Chapter 5 of "Upskill in Testing with Python".

## Overview

The examples demonstrate:
1. How to measure and improve code coverage using pytest-cov
2. How to identify and fix code style violations using flake8
3. How to automatically format code using black

## Files in This Directory

### Source Code
- **`calculator.py`** - A calculator module with various arithmetic functions, including error handling and edge cases. This serves as the code under test.
- **`example_with_linting_issues.py`** - Python code with common style violations and linting issues that flake8 can detect.
- **`example_clean.py`** - The same code refactored to follow PEP 8 conventions and pass flake8 checks.
- **`example_unformatted.py`** - Code with inconsistent formatting before black processing.
- **`example_formatted.py`** - The same code after black automatic formatting.

### Test Files
- **`test_calculator_basic.py`** - Basic test suite with intentionally incomplete coverage (~69%), demonstrating what happens when you don't test all code paths.
- **`test_calculator_improved.py`** - Comprehensive test suite achieving 100% coverage, including edge cases, error conditions, and parametrized tests.

### Configuration Files
- **`.flake8`** - Configuration file for flake8 with common settings and customizations.
- **`pyproject.toml`** - Configuration file for black with project-specific settings.
- **`pre-commit-config.yaml`** - Pre-commit hook configuration for black.

## Prerequisites

Ensure you have pytest, pytest-cov, flake8, and black installed:

```bash
pip install pytest pytest-cov flake8 black
```

## Running the Examples

### Code Coverage Examples

#### Example 1: Basic Coverage (Incomplete Testing)

Run the basic test suite to see what incomplete coverage looks like:

```bash
pytest test_calculator_basic.py --cov=calculator --cov-report=term-missing
```

**Expected Output:**
```
========================== test session starts ===========================
collected 6 items

test_calculator_basic.py ......                                     [100%]

========================== tests coverage ================================
Name            Stmts   Miss  Cover   Missing
----------------------------------------------
calculator.py      36     11    69%   72, 94, 122, 125, 143, 156-158, 181-183
----------------------------------------------
TOTAL              36     11    69%
========================== 6 passed in 0.03s ==============================
```

**Key Observations:**
- 6 tests pass successfully
- Only 69% coverage achieved
- 11 statements not executed (shown in "Missing" column)
- Missing lines include error handling, edge cases, and untested functions

### Example 2: Improved Coverage (Comprehensive Testing)

Run the improved test suite to see high coverage achievement:

```bash
pytest test_calculator_improved.py --cov=calculator --cov-report=term-missing
```

**Expected Output:**
```
========================== test session starts ===========================
collected 46 items

test_calculator_improved.py ..............................................  [100%]

========================== tests coverage ================================
Name            Stmts   Miss  Cover   Missing
----------------------------------------------
calculator.py      36      0   100%
----------------------------------------------
TOTAL              36      0   100%
========================== 46 passed in 0.09s ==============================
```

**Key Observations:**
- All 46 tests pass
- **100% code coverage** achieved
- Every line and branch in calculator.py is tested
- The comprehensive test suite validates all functionality, edge cases, and error conditions

---

## Linting with flake8

### Example 3: Identifying Code Style Issues

Run flake8 on code with style violations:

```bash
flake8 example_with_linting_issues.py
```

**Expected Output (partial):**
```
example_with_linting_issues.py:6:1: F401 'os' imported but unused
example_with_linting_issues.py:22:21: E231 missing whitespace after ','
example_with_linting_issues.py:24:11: E225 missing whitespace around operator
example_with_linting_issues.py:32:10: E702 multiple statements on one line (semicolon)
example_with_linting_issues.py:35:80: E501 line too long (147 > 79 characters)
example_with_linting_issues.py:38:13: E712 comparison to True should be 'if cond:'
example_with_linting_issues.py:44:5: E722 do not use bare 'except'
example_with_linting_issues.py:85:1: E731 do not assign a lambda expression, use a def
```

**Key Observations:**
- F401: Unused imports waste resources
- E231, E225: Missing whitespace hurts readability
- E501: Long lines are hard to read
- E712: Comparing to True/False is un-Pythonic
- E722: Bare except catches too many exceptions
- E731: Lambdas should be used for anonymous functions only

### Example 4: Clean Code Verification

Run flake8 on properly formatted code:

```bash
flake8 example_clean.py
```

**Expected Output:**
```
(No output - all checks passed!)
```

When flake8 produces no output, it means your code passes all style and quality checks. This is the goal for production code.

### Example 5: Using flake8 Configuration

The `.flake8` file in this directory demonstrates common configuration options:

```bash
# flake8 automatically reads .flake8 in the current directory
flake8 example_clean.py

# You can also specify a config file explicitly
flake8 --config=.flake8 example_clean.py
```

**Configuration Features:**
- Custom line length limits
- Excluded directories and files
- Per-file ignore rules
- Statistics and error counts
- Source code display for errors

---

## Combining Coverage and Linting

For comprehensive code quality, run both coverage analysis and linting:

```bash
# Run tests with coverage
pytest test_calculator_improved.py --cov=calculator --cov-report=term-missing

# Run linting on all Python files
flake8 *.py

# Or combine in a single command
pytest --cov=calculator --cov-report=term-missing && flake8 *.py
```

This ensures your code is both **well-tested** (high coverage) and **well-written** (passes linting).

---

## Code Formatting with black

### Example 6: Checking Code for Formatting Issues

Check if code needs formatting without modifying it:

```bash
black --check example_unformatted.py
```

**Expected Output:**
```
would reformat example_unformatted.py

Oh no! 💥 💔 💥
1 file would be reformatted.
```

The non-zero exit code indicates the file needs formatting. This is useful in CI/CD pipelines.

### Example 7: Viewing Formatting Changes

See what black would change before applying:

```bash
black --diff example_unformatted.py
```

**Expected Output (partial):**
```diff
--- example_unformatted.py      2025-11-07 20:11:38.602651+00:00
+++ example_unformatted.py      2025-11-07 20:22:28.885180+00:00
@@ -1,65 +1,101 @@
 """Example showing code before black formatting."""
 
-def calculate_statistics(data,include_mean=True,include_median=False,include_mode=False):
+def calculate_statistics(
+    data, include_mean=True, include_median=False, include_mode=False
+):
     """Calculate various statistics with poor formatting."""
-    results={}
+    results = {}
```

The diff shows exactly what black will change, including:
- Adding spaces around operators
- Splitting long lines
- Reformatting function signatures

### Example 8: Applying black Formatting

Format the code automatically:

```bash
black example_unformatted.py
```

**Expected Output:**
```
reformatted example_unformatted.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

Now verify the file passes checks:

```bash
black --check example_unformatted.py
```

**Expected Output:**
```
All done! ✨ 🍰 ✨
1 file would be left unchanged.
```

### Example 9: Comparing Formatted vs Unformatted

Compare the two files to see black's impact:

```bash
# Show unformatted (before)
head -20 example_unformatted.py

# Show formatted (after) 
head -20 example_formatted.py
```

Notice the differences in:
- Function signature formatting
- Spacing consistency
- String quote usage (prefers double quotes)
- Dictionary and list formatting

### Example 10: Using black Configuration

The `pyproject.toml` file demonstrates black configuration:

```bash
# black automatically reads pyproject.toml
black --check example_unformatted.py

# Format all Python files in current directory
black .

# Format with specific line length
black --line-length=100 example_unformatted.py
```

---

## Combining All Quality Tools

For comprehensive code quality assurance, use all three tools together:

```bash
# 1. Format code with black
black *.py

# 2. Verify linting with flake8
flake8 *.py

# 3. Run tests with coverage
pytest --cov=calculator --cov-report=term-missing
```

This workflow ensures:
- **Consistent formatting** (black)
- **Style compliance** (flake8)
- **Functional correctness** (pytest)
- **Test coverage** (pytest-cov)

---

## Advanced Examples

### Comparing the Two Approaches

Run both test files together to see combined coverage:

```bash
pytest --cov=calculator --cov-report=term-missing
```

This runs all 52 tests (6 basic + 46 improved) and shows 100% coverage.

## Advanced Coverage Options

### Generate HTML Coverage Report

Create an interactive HTML report for visual coverage analysis:

```bash
pytest --cov=calculator --cov-report=html
```

Then open `htmlcov/index.html` in your browser to see:
- Line-by-line coverage visualization
- Color-coded coverage indicators (green = covered, red = not covered)
- Easy navigation between files
- Coverage statistics per file

### Generate Multiple Report Formats

Combine terminal and HTML reports:

```bash
pytest --cov=calculator --cov-report=term-missing --cov-report=html
```

### Run Tests with Coverage Threshold

Fail the test suite if coverage falls below 80%:

```bash
pytest --cov=calculator --cov-fail-under=80
```

This is useful in CI/CD pipelines to enforce minimum coverage standards.

### Measure Branch Coverage

Include branch coverage in addition to statement coverage:

```bash
pytest --cov=calculator --cov-branch --cov-report=term-missing
```

Branch coverage measures whether both `True` and `False` branches of conditionals are tested.

## What the Examples Demonstrate

### Coverage Gaps in Basic Tests

The basic test suite (`test_calculator_basic.py`) is missing tests for:

1. **Error Conditions**
   - Division by zero
   - Negative exponents in power function
   - Negative numbers in factorial
   - Zero total in percentage calculation

2. **Edge Cases**
   - Zero exponent in power function
   - Factorial of 0 and 1
   - Zero values in various functions

3. **Untested Functions**
   - `is_even()` - not tested at all
   - `absolute_value()` - not tested at all
   - `calculate_percentage()` - not tested at all

### Comprehensive Testing Approach

The improved test suite (`test_calculator_improved.py`) demonstrates:

1. **Systematic Testing**
   - One test class per function
   - Clear test names describing what is tested
   - Docstrings explaining test purpose

2. **Edge Case Coverage**
   - Zero values
   - Negative numbers
   - Boundary conditions

3. **Error Condition Testing**
   - Using `pytest.raises()` to test exceptions
   - Verifying error messages with `match` parameter

4. **Parametrized Tests**
   - Testing multiple inputs efficiently
   - Reducing test duplication

## Learning Objectives

By working through these examples, you will:

1. **Understand code coverage metrics** - Learn what coverage percentages mean and how to interpret them
2. **Identify testing gaps** - Use coverage reports to find untested code paths
3. **Write comprehensive tests** - Develop tests that cover edge cases, errors, and alternate paths
4. **Achieve high coverage** - Systematically improve coverage from 69% to 100%
5. **Use pytest-cov effectively** - Master the tool's features including terminal reports, HTML reports, and coverage thresholds
6. **Recognize code style violations** - Identify common PEP 8 violations and programming errors
7. **Use flake8 for linting** - Run static analysis to improve code quality
8. **Fix linting issues** - Systematically resolve style and quality problems
9. **Configure linting tools** - Customize flake8 for your project's needs
10. **Integrate quality checks** - Combine coverage and linting in your development workflow

## Next Steps

Try these exercises to deepen your understanding:

### Coverage Exercises

1. **Add a new function** to `calculator.py` (e.g., `square_root()` or `modulo()`) and write tests achieving 100% coverage

2. **Intentionally break coverage** by commenting out some tests in `test_calculator_improved.py` and observe how the coverage report changes

3. **Add branch coverage** measurement and see if you can achieve 100% branch coverage

4. **Create a `.coveragerc` file** to customize coverage behavior (exclude certain lines, change report options)

5. **Generate and explore** the HTML coverage report to see the visual representation of coverage

### Linting Exercises

6. **Create your own "messy" code** with various style violations and use flake8 to identify them

7. **Fix issues incrementally** - Take `example_with_linting_issues.py` and fix one error at a time, re-running flake8 after each fix

8. **Experiment with configuration** - Modify `.flake8` to change the maximum line length or ignore specific errors

9. **Integrate with pytest** - Install `pytest-flake8` and run linting checks with your tests

10. **Set up pre-commit hooks** - Configure flake8 to run automatically before commits

### Combined Exercises

11. **Write code with both high coverage and clean style** - Create a small module with tests achieving 100% coverage and zero flake8 violations

12. **Create a quality checklist** - Develop a checklist combining coverage targets and linting standards for your projects

## Troubleshooting

### Coverage Issues

**pytest-cov not recognized**
```bash
pip install pytest-cov
```

**Tests not discovered**
Make sure your test files start with `test_` and test functions start with `test_`.

**Coverage not showing**
Ensure you specify the correct module name with `--cov=calculator` (module name, not filename).

### Linting Issues

**flake8 not recognized**
```bash
pip install flake8
```

**Too many violations to fix at once**
Fix errors in order of severity: F (errors) first, then E (style), then W (warnings).

**Configuration not being read**
Ensure `.flake8` is in the current directory or specify it with `--config=.flake8`.

**False positives**
Use `# noqa: <code>` to suppress specific warnings on individual lines when truly necessary.

## Summary

These examples demonstrate the power of combining multiple code analysis tools:

- **Code Coverage (pytest-cov)**: Measures how much of your code is tested, identifying gaps in your test suite
- **Linting (flake8)**: Checks code style and quality, enforcing PEP 8 standards and catching potential bugs

Coverage metrics provide objective data about which parts of your code are tested, guiding you toward more comprehensive and reliable tests. However, remember that high coverage is a means to an end—the goal is confidence that your code works correctly, not just high percentages.

Similarly, passing flake8 checks ensures your code is readable, maintainable, and follows Python best practices, making collaboration easier and reducing bugs.

Together, these tools form a comprehensive quality assurance strategy that validates both **what your code does** (functionality via tests and coverage) and **how it's written** (quality via linting).
