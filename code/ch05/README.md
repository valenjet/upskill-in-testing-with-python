# Chapter 5: Code Analysis - Code Examples

This directory contains code examples demonstrating code coverage analysis with pytest-cov, linting with flake8, code formatting with black, advanced static analysis with pylint, and type checking with mypy, as covered in Chapter 5 of "Upskill in Testing with Python".

## Overview

The examples demonstrate:
1. How to measure and improve code coverage using pytest-cov
2. How to identify and fix code style violations using flake8
3. How to automatically format code using black
4. How to perform comprehensive static analysis using pylint
5. How to add type hints and perform static type checking with mypy

## Files in This Directory

### Source Code
- **`calculator.py`** - A calculator module with various arithmetic functions, including error handling and edge cases. This serves as the code under test.
- **`example_with_linting_issues.py`** - Python code with common style violations and linting issues that flake8 can detect.
- **`example_clean.py`** - The same code refactored to follow PEP 8 conventions and pass flake8 checks.
- **`example_unformatted.py`** - Code with inconsistent formatting before black processing.
- **`example_formatted.py`** - The same code after black automatic formatting.
- **`example_with_pylint_issues.py`** - Python code with various pylint warnings demonstrating common issues.
- **`example_pylint_clean.py`** - The same functionality refactored to achieve a perfect 10/10 pylint score.
- **`example_without_types.py`** - Code without type hints, demonstrating potential runtime type errors.
- **`example_with_types.py`** - The same code with comprehensive type annotations for static type checking.
- **`example_mypy_errors.py`** - Code with intentional type errors to demonstrate what mypy catches.

### Test Files
- **`test_calculator_basic.py`** - Basic test suite with intentionally incomplete coverage (~69%), demonstrating what happens when you don't test all code paths.
- **`test_calculator_improved.py`** - Comprehensive test suite achieving 100% coverage, including edge cases, error conditions, and parametrized tests.

### Configuration Files
- **`.flake8`** - Configuration file for flake8 with common settings and customizations (black-compatible).
- **`.pylintrc`** - Configuration file for pylint with project-specific settings.
- **`mypy.ini`** - Configuration file for mypy type checking.
- **`pyproject.toml`** - Unified configuration file for black and mypy with project-specific settings.
- **`pre-commit-config.yaml`** - Pre-commit hook configuration for black.

## Prerequisites

Ensure you have pytest, pytest-cov, flake8, black, pylint, and mypy installed:

```bash
pip install pytest pytest-cov flake8 black pylint mypy
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

## Advanced Static Analysis with pylint

### Example 11: Identifying Complex Code Issues

Run pylint on code with various quality issues:

```bash
pylint example_with_pylint_issues.py
```

**Expected Output (partial):**
```
************* Module example_with_pylint_issues
example_with_pylint_issues.py:13:0: C0103: Constant name "myGlobalVar" doesn't conform to UPPER_CASE naming style (invalid-name)
example_with_pylint_issues.py:17:0: R0913: Too many arguments (10/5) (too-many-arguments)
example_with_pylint_issues.py:23:0: R0914: Too many local variables (18/15) (too-many-locals)
example_with_pylint_issues.py:45:0: C0115: Missing class docstring (missing-class-docstring)
example_with_pylint_issues.py:65:0: R0912: Too many branches (13/12) (too-many-branches)
example_with_pylint_issues.py:96:0: R0911: Too many return statements (8/6) (too-many-return-statements)
example_with_pylint_issues.py:119:0: C0103: Function name "CalculateTotal" doesn't conform to snake_case naming style (invalid-name)
example_with_pylint_issues.py:140:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
example_with_pylint_issues.py:152:11: W0718: Catching too general exception Exception (broad-exception-caught)
example_with_pylint_issues.py:7:0: W0611: Unused import sys (unused-import)

------------------------------------------------------------------
Your code has been rated at 6.88/10 (previous run: 6.95/10, -0.08)
```

**Key Observations:**

**Message Categories:**
- **C (Convention)**: Coding standard violations (C0103: naming, C0115: missing docstring)
- **R (Refactor)**: Code structure issues (R0913: too many arguments, R0914: too many locals)
- **W (Warning)**: Potential problems (W0102: dangerous default, W0611: unused import)
- **E (Error)**: Likely bugs (not shown in this example)
- **F (Fatal)**: Prevents analysis (not shown in this example)

**Quality Score:**
- Score: 6.88/10 indicates significant room for improvement
- Each issue reduces the score based on severity

### Example 12: Achieving High Code Quality

Run pylint on properly refactored code:

```bash
pylint example_pylint_clean.py
```

**Expected Output:**
```

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.77/10, +0.23)
```

When pylint produces no messages and a 10/10 score, your code meets high quality standards!

**What Was Fixed:**

1. **Naming Conventions**
   - Changed `myGlobalVar` → `MY_GLOBAL_VAR` (constants)
   - Changed `CalculateTotal` → `calculate_total` (functions)

2. **Function Complexity**
   - Reduced arguments from 10 → 3 (R0913)
   - Simplified logic to reduce local variables (R0914)
   - Replaced long if-elif chains with dictionaries (R0912)
   - Combined return statements (R0911)

3. **Documentation**
   - Added module docstring (C0114)
   - Added class docstrings (C0115)
   - Added function docstrings (C0116)

4. **Best Practices**
   - Changed mutable default `[]` → `None` (W0102)
   - Used specific exception types instead of `Exception` (W0718)
   - Removed unused imports (W0611)
   - Used `is not None` instead of `!= None` (C0121)
   - Used `enumerate()` instead of `range(len())` (C0200)
   - Used context managers for file operations (R1732)

### Example 13: Using pylint Configuration

The `.pylintrc` file demonstrates common configuration options:

```bash
# pylint automatically reads .pylintrc in the current directory
pylint example_with_pylint_issues.py

# You can also specify a config file explicitly
pylint --rcfile=.pylintrc example_with_pylint_issues.py
```

**Configuration Features:**
- Message category control (enable/disable specific checks)
- Code complexity thresholds (max arguments, branches, locals)
- Naming conventions customization
- Output format options (text, json, colorized)
- Plugin loading for framework-specific checks

### Example 14: Comparing flake8 vs pylint

Run both tools on the same code to see the differences:

```bash
# flake8: fast, focused on style
flake8 example_with_pylint_issues.py

# pylint: comprehensive, includes design analysis
pylint example_with_pylint_issues.py
```

**Key Differences:**

| Aspect | flake8 | pylint |
|--------|--------|--------|
| **Speed** | Fast | Slower (more thorough) |
| **Scope** | Style + simple errors | Style + design + complexity |
| **Score** | No score | 0-10 quality score |
| **Messages** | Fewer, focused | More comprehensive |
| **Configuration** | Simple | Extensive options |
| **Use Case** | Quick checks in IDE/CI | Periodic deep analysis |

**Best Practice:** Use **both**!
- Run flake8 frequently for fast feedback
- Run pylint periodically for deep analysis

### Example 15: Integrating pylint with pytest

Create a test that enforces a minimum pylint score:

```bash
# Run pylint as part of your test suite
pytest --pylint --pylint-rcfile=.pylintrc
```

You can also create a custom test (see manuscript for example code).

---

## Combining All Quality Tools

For comprehensive code quality assurance, use all tools together in the recommended order:

```bash
# 1. Format code with black
black *.py

# 2. Verify linting with flake8 (fast checks)
flake8 *.py

# 3. Deep analysis with pylint (thorough checks)
pylint *.py --fail-under=8.0

# 4. Run tests with coverage
pytest --cov=calculator --cov-report=term-missing
```

This workflow ensures:
- **Consistent formatting** (black)
- **Style compliance** (flake8)  
- **Design quality** (pylint)
- **Functional correctness** (pytest)
- **Test coverage** (pytest-cov)

### Quick Quality Check

Run all checks in one command:

```bash
black *.py && flake8 *.py && pylint *.py && pytest --cov=calculator
```

The `&&` operator ensures each step succeeds before continuing.

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
10. **Format code automatically** - Use black for consistent code formatting
11. **Understand pylint messages** - Interpret Convention, Refactor, Warning, and Error categories
12. **Improve code design** - Use pylint feedback to reduce complexity and improve structure
13. **Achieve high quality scores** - Refactor code to reach 8.0+ or 10/10 pylint scores
14. **Configure pylint** - Customize analysis for your project's needs
15. **Integrate quality checks** - Combine coverage, linting, and static analysis in your development workflow

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

### pylint Exercises

11. **Analyze your own code** - Run pylint on a personal project and aim for 8.0+ score

12. **Fix issues systematically** - Start with E/F messages, then W, then R, finally C

13. **Experiment with configuration** - Modify `.pylintrc` to adjust complexity thresholds or disable specific messages

14. **Compare before/after** - Measure the score improvement after refactoring `example_with_pylint_issues.py`

15. **Create quality gates** - Write a test that fails if pylint score drops below threshold

### Combined Exercises

16. **Write code with both high coverage and clean style** - Create a small module with tests achieving 100% coverage and zero flake8 violations

17. **Create a quality checklist** - Develop a checklist combining coverage targets and linting standards for your projects

### Type Checking Examples

#### Example 1: Code Without Type Hints

Examine code without type annotations:

```bash
cat example_without_types.py
```

This code works at runtime but lacks type safety. mypy will provide minimal checking.

#### Example 2: Adding Type Hints

Compare the same code with comprehensive type annotations:

```bash
cat example_with_types.py
```

Notice how type hints make the code more self-documenting and enable static type checking.

#### Example 3: Running mypy

Check for type errors using mypy:

```bash
# Check code with type hints
mypy example_with_types.py

# Should report: Success: no issues found
```

#### Example 4: Catching Type Errors

Run mypy on code with intentional type errors:

```bash
# Check code with type errors
mypy example_mypy_errors.py --show-error-codes

# Shows detailed type errors with error codes
```

#### Example 5: mypy Configuration

Use a configuration file for project-specific settings:

```bash
# Using mypy.ini
mypy --config-file mypy.ini example_with_types.py

# Or using pyproject.toml (automatically detected)
mypy example_with_types.py
```

#### Example 6: Strict Mode

Enable strict type checking for maximum safety:

```bash
mypy --strict example_with_types.py
```

Strict mode requires:
- Type annotations on all functions
- No implicit Optional types
- No Any types
- Comprehensive error checking

#### Example 7: Incremental Typing

For existing projects, adopt mypy gradually:

```bash
# Start with minimal checking
mypy --ignore-missing-imports .

# Add types to one module at a time
mypy --strict new_module.py

# Use type: ignore for legacy code
# my_var = legacy_function()  # type: ignore
```

### Type Checking Exercises

18. **Add type hints to untested code** - Take example_without_types.py and add comprehensive type annotations

19. **Fix type errors** - Correct all the type errors in example_mypy_errors.py

20. **Run mypy on your project** - Install mypy and run it on an existing Python project

21. **Enable strict mode incrementally** - Start with basic mypy checking and gradually increase strictness

22. **Type hint a function** - Take any Python function and add complete type annotations including parameters and return type

23. **Create Protocol types** - Define a Protocol for structural typing (duck typing with type safety)

24. **Use Union and Optional** - Practice using Union types and Optional for functions with multiple input/output types

25. **Configure mypy** - Create a mypy.ini or update pyproject.toml with project-specific type checking rules

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

### pylint Issues

**pylint not recognized**
```bash
pip install pylint
```

**Score seems too low**
Focus on fixing E and F messages first, then W, then R and C. Each category has different impact on score.

**Too many messages**
Start with `--disable=C,R` to focus on warnings and errors, then gradually enable more checks.

**Configuration not being read**
Ensure `.pylintrc` is in the current directory or specify it with `--rcfile=.pylintrc`.

**False positives**
Use `# pylint: disable=message-name` to suppress specific checks on individual lines or blocks when justified.

### mypy Issues

**mypy not recognized**
```bash
pip install mypy
```

**Too many errors in existing code**
Use `# type: ignore` comments temporarily and adopt types gradually. Start with new code.

**Missing type stubs for third-party libraries**
```bash
# Install type stubs for common libraries
pip install types-requests types-redis types-PyYAML

# Or let mypy install them
mypy --install-types
```

**Configuration not being read**
Ensure `mypy.ini` is in the current directory or use `--config-file` flag. Alternatively, add `[tool.mypy]` section to `pyproject.toml`.

**False positives**
Use `# type: ignore[error-code]` to suppress specific type errors when they're incorrect. Document why.

**Can't check third-party library**
Add to mypy configuration:
```ini
[mypy-third_party_module.*]
ignore_missing_imports = True
```

### Integration Issues

**black and flake8 conflict**
Ensure `.flake8` has `max-line-length=88` and `extend-ignore=E203,W503` for black compatibility.

**Tools report different issues**
This is normal! Each tool has a different focus. Use them together for comprehensive quality checks.

## Summary

These examples demonstrate the power of combining multiple code analysis tools:

- **Code Coverage (pytest-cov)**: Measures how much of your code is tested, identifying gaps in your test suite
- **Linting (flake8)**: Checks code style and quality, enforcing PEP 8 standards and catching potential bugs
- **Code Formatting (black)**: Automatically formats code for consistency, eliminating style debates
- **Static Analysis (pylint)**: Performs deep code analysis, detecting design issues, complexity problems, and code smells
- **Type Checking (mypy)**: Validates type correctness through static analysis, catching type-related bugs before runtime

Coverage metrics provide objective data about which parts of your code are tested, guiding you toward more comprehensive and reliable tests. However, remember that high coverage is a means to an end—the goal is confidence that your code works correctly, not just high percentages.

Passing flake8 checks ensures your code is readable and follows Python best practices. Black eliminates formatting debates by applying consistent style automatically. pylint goes deeper, analyzing code structure and complexity to identify design improvements.

Together, these tools form a comprehensive quality assurance strategy that validates both **what your code does** (functionality via tests and coverage) and **how it's written** (quality via linting, formatting, and static analysis).
