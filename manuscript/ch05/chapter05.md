# Chapter 5: Code Analysis

### Enhancing Software Quality through Systematic Evaluation

Code analysis encompasses a structured approach to enhancing software quality, leveraging both static and dynamic methodologies to scrutinize and refine code. This process is integral to continuous improvement, enabling developers to identify and rectify issues efficiently.

#### The Cycle of Software Improvement

Software improvement unfolds in a cyclical three-phase process: _Analyze_, _Improve_, and _Monitor_. This model fosters a continuous loop of assessment and enhancement:

1. **Analyze**: This initial stage focuses on understanding the current state of the software by examining the code and system behavior. It involves:
   - **Static Analysis**: Evaluating the code without execution, inspecting source code, binaries, or other components for potential issues.
   - **Dynamic Analysis**: Assessing the system during runtime to capture performance metrics, memory usage, and other operational data.

2. **Improve**: Actions derived from the analysis phase are implemented here, including source code modifications, architectural adjustments, and design improvements. This phase aims to address identified shortcomings through tuning, refactoring, and remediation efforts.

3. **Monitor**: Ongoing review processes, both formal and informal, ensure continuous oversight. Monitoring involves evaluating system performance and functionality against established metrics to identify deviations requiring analysis. Effective monitoring blends manual examination with automated assessments to maintain and enhance software quality continuously.

#### Integration with Build Pipelines

The concept of Application Lifecycle Management (ALM) encapsulates key facets of software development, including requirements, design, coding, testing, deployment, maintenance, and project management. These elements recur throughout the development process, with code analysis tools and techniques playing a pivotal role at various stages.

#### Static and Dynamic Analysis with pytest

In Python, the pytest framework can be augmented with plugins and tools to facilitate both static and dynamic code analysis:

- **Static Analysis in Python**: Tools like `flake8`, `pylint`, and `mypy` offer comprehensive static code analysis, checking for syntax errors, stylistic issues, and type checks, respectively.
  
- **Dynamic Analysis with pytest**: By leveraging pytest for dynamic analysis, developers can write tests that not only validate functionality but also monitor performance and other runtime behaviors.

#### Example: Basic Static Analysis with flake8

```python
# Example Python code snippet
def add(a, b):
    return a + b  # Intentionally simple for illustration

# flake8 can be run from the command line to analyze this code:
# flake8 example.py
```




### Static Analysis in Software Development

Static analysis is a critical component of software quality assurance, examining code and assemblies without executing the program. This analysis helps ensure code adherence to coding standards and evaluates modules for compliance with good coding practices. When discrepancies are found, static analysis tools generate a list of violations, guiding developers to areas requiring attention.

#### Static vs. Dynamic Analysis

- **Static Analysis**: Evaluates the software in a non-running state, focusing on source code and modules to assess compliance with coding standards and architectural guidelines.
  
- **Dynamic Analysis**: Involves analyzing the software during execution, capturing performance metrics and other runtime behaviors to identify potential issues.

#### Improvement Through Analysis

> Thoroughly Analyze Modules Using Static Analysis

The improvement phase of code analysis involves making code and architectural enhancements suggested by the analysis phase. This includes tuning, refactoring, and addressing design or dependency issues.

#### Monitoring Software Quality

> Fail the Build for Violations of Required Rules

Monitoring, an ongoing phase, involves reviewing code and system performance to ensure continued adherence to project objectives. This can include both formal reviews and automated testing, leveraging continuous integration (CI) processes to maintain software quality.

#### Integration with Application Lifecycle Management (ALM)

Static and dynamic analysis tools play a significant role across the ALM stages, supporting developers and team leaders in ensuring that development efforts align with design objectives and project standards.

#### Static Analysis Tools

In Python development, static analysis objectives can be achieved using tools like `flake8` and `pylint` for code style and quality checks. Use `mypy` for type checking, complemented by dynamic testing with the pytest framework.

#### Example: Static Analysis with flake8

```python
```

Static analysis is indispensable for maintaining high code quality, facilitating a systematic approach to software development that incorporates analysis, improvement, and monitoring. Leverage tools like `flake8` or `mypy` to ensure software is built to high standards of readability, performance, and maintainability. Combine static analysis tools with dynamic testing to form a robust foundation for continuous software improvement.


### Duplicate Code Finders

> Find and Address Any Inappropriate Duplication of Code

Code analysis is able to find code duplication.

#### Identifying and Addressing Duplicate Code

Duplicate code can significantly hinder maintainability and readability. Tools designed to identify such redundancies help in distinguishing between the benign and the problematic duplications, guiding developers towards meaningful refactoring opportunities. Effective use of these tools requires a judicious approach to avoid inappropriate generalization that could lead to a diluted domain model and increased complexity.

#### Manual Code Reviews: Beyond Automation

While automated tools provide significant insights, the value of manual code reviews cannot be overstated. These reviews bring human judgment, experience, and a deeper understanding of design intentions to the forefront, facilitating knowledge transfer and fostering a culture of continuous improvement.

#### Architectural and Design Analysis

Software architecture and design form the blueprint of any system. Static analysis tools that focus on architectural integrity help reveal deviations from planned designs, enabling teams to make informed decisions about aligning the actual software structure with its intended design or adapting the design to reflect better choices discovered during development.

#### Utilizing Code Metrics for Informed Decision Making

Code metrics offer quantitative insights into various aspects of the code base, such as complexity and adherence to best practices. Tools integrated into development environments like Visual Studio enable teams to monitor these metrics continuously, aiding in the identification of areas requiring attention.

#### Quality Assurance Metrics: A Holistic View

Quality Assurance (QA) metrics provide a holistic view of software quality, linking defects to specific modules, requirements, or aspects of the system. Analyzing these metrics helps pinpoint error-prone areas, guiding targeted improvements and contributing to the overall robustness of the software.

#### Example: Code Duplication Analysis in Python

Tools like `flake8` can be leveraged to enforce coding standards and identify potential code smells that could indicate duplication.

```python
```

#### Implementing Manual Code Reviews and Metrics Analysis

Manual code reviews in Python benefit from the same principles as in other languages, focusing on design adherence, coding standards, and best practices. Tools like `radon` can provide code metrics, while `bandit` offers insights into security vulnerabilities, complementing the manual review process.

#### Static Analysis: Summary

Code analysis, encompassing automated tools and manual reviews, forms a critical component of the software development lifecycle. By continuously monitoring code quality, architectural alignment, and system behavior, development teams can ensure that their software not only meets the current requirements but is also poised for future enhancements. The principles of effective code analysis guide the goal of delivering high-quality, maintainable, and robust software solutions.



### Dynamic Analysis

Dynamic analysis plays a crucial role in understanding software behavior by executing the program under various conditions to gather runtime information. This approach complements static analysis by providing insights into performance, memory usage, test coverage, and internal state during execution, answering critical questions about the software's operational characteristics.

#### Objectives of Dynamic Analysis

Dynamic analysis aims to uncover details about the software that can only be observed during its execution, such as:
- Execution hot-spots and performance bottlenecks.
- Memory consumption patterns and optimization opportunities.
- Areas of code not exercised by unit tests.
- Application state prior to exceptions or failures.
- Database interactions and efficiencies.

#### Tools and Practices

In the Python ecosystem, dynamic analysis can leverage several tools and practices to enhance software quality:

- **Code Coverage**: Tools like `pytest-cov` integrate with pytest to measure the extent of code executed during automated tests, helping identify untested code paths.
- **Performance Profiling**: Python provides the built-in modules `cProfile` and `profile`[^1] for profiling software performance, identifying slow functions, and understanding call stacks.
- **Query Profiling**: Libraries such as `sqlalchemy` offer mechanisms to log and analyze database queries, aiding in the optimization of database interactions.
- **Logging**: Python's built-in `logging` module supports configurable, level-based logging to monitor application behavior and troubleshoot issues effectively.


### Measuring Code Coverage with pytest-cov

Code coverage is one of the most actionable metrics in dynamic analysis, revealing which parts of your codebase are executed during testing and, equally important, which parts are not. The `pytest-cov` plugin seamlessly integrates coverage measurement into your pytest workflow, providing clear insights into test effectiveness.

#### Understanding Code Coverage

Code coverage measures the percentage of your code that is executed when your test suite runs. It answers a fundamental question: "Are we testing what we think we're testing?" Coverage analysis identifies:

- **Untested code paths**: Functions, branches, or exception handlers never executed during tests
- **Dead code**: Code that may no longer be necessary or reachable
- **Test gaps**: Areas of functionality that lack validation
- **Risk areas**: Critical code without test protection

Coverage is typically measured in several dimensions:

- **Statement Coverage**: The percentage of code statements executed
- **Branch Coverage**: The percentage of conditional branches (if/else) executed
- **Function Coverage**: The percentage of functions called during testing

For most Python projects, statement coverage provides a practical starting point, with branch coverage offering additional rigor for critical codebases.

#### Installing and Configuring pytest-cov

The `pytest-cov` plugin is a wrapper around the `coverage.py` library, designed specifically for pytest integration. Install it using pip:

```bash
pip install pytest-cov
```

Once installed, `pytest-cov` works seamlessly with your existing pytest setup—no configuration file is required for basic usage, though customization options are available through a `.coveragerc` file or `pyproject.toml` for advanced scenarios.

#### Running Coverage Analysis

The most straightforward way to measure coverage is by adding the `--cov` flag to your pytest command, followed by the module or package name you want to analyze:

```bash
pytest --cov=calculator
```

This command runs your tests and measures coverage for the `calculator` module. The output displays a summary showing the percentage of code covered.

For more detailed insights, use the `--cov-report` option to specify the report format:

```bash
pytest --cov=calculator --cov-report=term-missing
```

The `term-missing` report format shows which specific lines were not executed during testing, making it easy to identify coverage gaps.

#### Example: Measuring Coverage

Let's examine a practical example using a calculator module with various arithmetic functions. First, consider a basic test suite with incomplete coverage:

##### Listing 5-1: `test_calculator_basic.py` - Limited Test Coverage

```python
"""
Basic test suite for calculator module with incomplete coverage.
"""

import pytest
from calculator import (
    add, subtract, multiply, divide, power, 
    factorial, is_even, absolute_value, calculate_percentage
)


class TestBasicArithmetic:
    """Test basic arithmetic operations."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(4, 5) == 20
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5


class TestPowerAndFactorial:
    """Test power and factorial functions."""
    
    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2, 3) == 8
    
    def test_factorial_positive_number(self):
        """Test factorial with positive number."""
        assert factorial(5) == 120
```

Running coverage on this basic test suite reveals significant gaps:

```bash
$ pytest test_calculator_basic.py --cov=calculator --cov-report=term-missing

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

The report indicates **69% coverage** with 11 statements not executed (shown in the "Missing" column). While all six tests pass, nearly a third of the calculator's code remains untested.

#### Interpreting Coverage Reports

Understanding coverage reports is crucial for making informed decisions about where to add tests. Let's decode the output:

- **Stmts**: Total number of executable statements in the file
- **Miss**: Number of statements not executed during testing
- **Cover**: Percentage of statements executed (Stmts - Miss) / Stmts
- **Missing**: Specific line numbers that were not executed

In the example above, lines 72, 94, 122, 125, 143, and 156-158, 181-183 were never executed. These likely represent:

- Error handling code (exceptions for divide by zero, negative factorials)
- Edge cases (zero exponents, factorial of 0 or 1)
- Untested functions (is_even, absolute_value, calculate_percentage)

This information guides your testing efforts, highlighting precisely where additional tests are needed.

#### Improving Coverage: A Systematic Approach

Coverage gaps point to opportunities for better testing. A comprehensive test suite addresses:

1. **Happy paths**: Normal, expected usage (already covered in basic tests)
2. **Edge cases**: Boundary conditions like zero, negative numbers, empty inputs
3. **Error conditions**: Invalid inputs that should raise exceptions
4. **Alternate paths**: Different branches through conditional logic

##### Listing 5-2: `test_calculator_improved.py` - Comprehensive Test Coverage

```python
"""
Comprehensive test suite with high coverage.
"""

import pytest
from calculator import (
    add, subtract, multiply, divide, power, 
    factorial, is_even, absolute_value, calculate_percentage
)


class TestDivision:
    """Comprehensive tests for division."""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestPower:
    """Comprehensive tests for power function."""
    
    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2, 3) == 8
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        assert power(5, 0) == 1
    
    def test_power_negative_exponent_raises_error(self):
        """Test that negative exponent raises ValueError."""
        with pytest.raises(ValueError, match="Negative exponents not supported"):
            power(2, -1)


class TestFactorial:
    """Comprehensive tests for factorial function."""
    
    def test_factorial_positive_numbers(self):
        """Test factorial with positive numbers."""
        assert factorial(5) == 120
    
    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1
    
    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial(1) == 1
    
    def test_factorial_negative_raises_error(self):
        """Test that negative factorial raises ValueError."""
        with pytest.raises(ValueError, match="Factorial not defined for negative"):
            factorial(-1)


class TestIsEven:
    """Comprehensive tests for is_even function."""
    
    def test_even_numbers(self):
        """Test that even numbers return True."""
        assert is_even(2) is True
        assert is_even(0) is True
    
    def test_odd_numbers(self):
        """Test that odd numbers return False."""
        assert is_even(1) is False
        assert is_even(3) is False


class TestAbsoluteValue:
    """Comprehensive tests for absolute_value function."""
    
    def test_positive_numbers(self):
        """Test absolute value of positive numbers."""
        assert absolute_value(5) == 5
    
    def test_negative_numbers(self):
        """Test absolute value of negative numbers."""
        assert absolute_value(-5) == 5
    
    def test_zero(self):
        """Test absolute value of zero."""
        assert absolute_value(0) == 0


class TestCalculatePercentage:
    """Comprehensive tests for calculate_percentage function."""
    
    def test_basic_percentage(self):
        """Test basic percentage calculations."""
        assert calculate_percentage(25, 100) == 25.0
    
    def test_zero_total_raises_error(self):
        """Test that zero total raises ValueError."""
        with pytest.raises(ValueError, match="Total cannot be zero"):
            calculate_percentage(50, 0)
```

Running the improved test suite demonstrates the impact of systematic testing:

```bash
$ pytest test_calculator_improved.py --cov=calculator --cov-report=term-missing

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

The improved test suite achieves **100% coverage**, testing all 36 statements across 46 test cases. Every code path, including error conditions and edge cases, is now validated.

#### Coverage Goals and Best Practices

While 100% coverage is achievable in our example, it's not always practical or necessary for every project. Consider these guidelines:

**Recommended Coverage Targets:**

- **New projects**: Aim for 80-90% coverage to establish good testing habits
- **Critical code**: Strive for 95-100% coverage for security, financial, or safety-critical modules
- **Legacy code**: Start with 60-70% and incrementally improve
- **Utilities and helpers**: Target 90%+ due to their wide reuse

**Coverage Best Practices:**

1. **Coverage is necessary but not sufficient**: High coverage doesn't guarantee correct behavior—tests must validate expected outcomes, not just execute code
2. **Focus on meaningful tests**: Don't write tests solely to increase coverage percentages; test behavior and requirements
3. **Use coverage to find gaps**: Let coverage guide where to add tests, not dictate your testing strategy
4. **Test the critical paths first**: Prioritize coverage for business logic, error handling, and security-related code
5. **Don't obsess over 100%**: Some code (like defensive programming checks, certain exception handlers) may not warrant testing
6. **Combine with other metrics**: Use coverage alongside code review, complexity analysis, and mutation testing

#### Excluding Code from Coverage

Sometimes it's appropriate to exclude certain code from coverage measurement. Common exclusions include:

- Debug-only code
- Platform-specific code not running in your test environment
- Defensive programming that's difficult to trigger
- Code explicitly marked as untestable

Use inline comments to exclude specific lines:

```python
def complex_function():
    try:
        # Normal operation
        return perform_operation()
    except ImportError:  # pragma: no cover
        # Fallback for missing optional dependency
        return fallback_operation()
```

Or configure exclusions in a `.coveragerc` file:

```ini
[run]
omit = 
    */tests/*
    */migrations/*
    */__init__.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
```

#### Advanced Coverage Features

The `pytest-cov` plugin offers several advanced options:

**HTML Reports**: Generate visual, line-by-line coverage reports:

```bash
pytest --cov=calculator --cov-report=html
```

This creates an `htmlcov/` directory containing interactive reports you can open in a browser.

**Multiple Report Formats**: Combine multiple report types:

```bash
pytest --cov=calculator --cov-report=term-missing --cov-report=html
```

**Coverage Thresholds**: Fail builds if coverage drops below a threshold:

```bash
pytest --cov=calculator --cov-fail-under=80
```

**Branch Coverage**: Measure branch coverage in addition to statement coverage:

```bash
pytest --cov=calculator --cov-branch
```

#### Coverage in Practice: A Workflow

Integrate coverage analysis into your development workflow:

1. **During Development**: Run coverage locally to verify new tests cover new code
2. **Before Committing**: Check that changes maintain or improve overall coverage
3. **In CI/CD**: Automate coverage measurement and enforce minimum thresholds
4. **In Code Review**: Review coverage reports to identify undertested areas
5. **Periodic Audits**: Regularly review low-coverage modules for testing opportunities

Coverage measurement transforms testing from guesswork into data-driven quality assurance, providing clear visibility into how thoroughly your code is validated.


### Ensuring Code Quality with flake8

While code coverage tells you _how much_ of your code is tested, static analysis tools like flake8 tell you _how well_ your code is written. flake8 is a popular Python linting tool that checks your code for style violations, programming errors, and code complexity issues. It combines three tools: PyFlakes (logical errors), pycodestyle (PEP 8 style checks), and McCabe (complexity checks).

#### Why Linting Matters

Code quality encompasses more than just functionality. Consistent, readable code following established conventions:

- **Reduces bugs**: Many style violations indicate potential logic errors
- **Improves maintainability**: Consistent formatting makes code easier to understand
- **Facilitates collaboration**: Team members can read and modify each other's code more easily
- **Catches errors early**: Identifies issues before they reach production
- **Enforces best practices**: Ensures adherence to Python's PEP 8 style guide

#### Installing flake8

Install flake8 using pip:

```bash
pip install flake8
```

flake8 requires Python 3.6 or higher and integrates seamlessly with existing Python projects. No additional configuration is required to start using it.

#### Running flake8

The simplest way to run flake8 is to point it at a file or directory:

```bash
# Check a single file
flake8 myfile.py

# Check all Python files in a directory
flake8 myproject/

# Check specific files
flake8 file1.py file2.py file3.py
```

Let's examine a Python file with common style violations to see flake8 in action.

##### Listing 5-6: `example_with_linting_issues.py` - Code with Style Violations

```python
"""
Example module demonstrating common linting issues that flake8 can detect.
"""

import os
import sys
import math
import json
import random


MyGlobalVariable = 100
another_WEIRD_variable = 200


def calculateTotal(x,y,z):  # Missing spaces after commas
    """Calculate total with poor formatting."""
    result=x+y+z  # Missing spaces around operators
    return result


def ProcessData( data ):  # Extra spaces, wrong naming
    """Process data with various style issues."""
    
    # Multiple statements on one line
    x = 1; y = 2; z = 3
    
    # Line too long
    very_long_variable_name = "This is a string that when combined with the variable name makes the line way too long and exceeds 79 characters"
    
    # Comparison to True (should use 'if data:' instead)
    if data == True:
        return "yes"
    
    # Using bare except
    try:
        result = int(data)
    except:  # Bare except clause
        result = 0
    
    return result


class  myClass:  # Wrong class name, extra space
    """Example class with style issues."""
    
    def __init__(self,value):  # Missing space after comma
        self.value=value
        
    def getValue(self):  # Should be snake_case
        return self.value


# Lambda when def would be better
multiply = lambda x, y: x * y


def check_status(status):
    """Check status with incorrect comparison."""
    if status is "active":  # Should use == for strings
        return True
    return False
```

Running flake8 on this file reveals numerous issues:

```bash
$ flake8 example_with_linting_issues.py

example_with_linting_issues.py:6:1: F401 'os' imported but unused
example_with_linting_issues.py:7:1: F401 'sys' imported but unused
example_with_linting_issues.py:9:1: F401 'json' imported but unused
example_with_linting_issues.py:10:1: F401 'random' imported but unused
example_with_linting_issues.py:22:1: E303 too many blank lines (3)
example_with_linting_issues.py:22:21: E231 missing whitespace after ','
example_with_linting_issues.py:22:23: E231 missing whitespace after ','
example_with_linting_issues.py:24:11: E225 missing whitespace around operator
example_with_linting_issues.py:28:17: E201 whitespace after '('
example_with_linting_issues.py:28:22: E202 whitespace before ')'
example_with_linting_issues.py:32:10: E702 multiple statements on one line (semicolon)
example_with_linting_issues.py:32:17: E702 multiple statements on one line (semicolon)
example_with_linting_issues.py:35:80: E501 line too long (147 > 79 characters)
example_with_linting_issues.py:38:13: E712 comparison to True should be 'if cond is True:' or 'if cond:'
example_with_linting_issues.py:44:5: E722 do not use bare 'except'
example_with_linting_issues.py:50:6: E271 multiple spaces after keyword
example_with_linting_issues.py:85:1: E731 do not assign a lambda expression, use a def
example_with_linting_issues.py:91:8: F632 use ==/!= to compare constant literals (str, bytes, int, float, tuple)
example_with_linting_issues.py:114:31: W292 no newline at end of file
```

#### Understanding flake8 Error Codes

flake8 reports violations using standardized error codes that indicate the type and severity of the issue:

**Error Code Prefixes:**
- **E**: pycodestyle errors (PEP 8 violations)
- **W**: pycodestyle warnings (style warnings)
- **F**: PyFlakes errors (logical/programming errors)
- **C**: McCabe complexity warnings

**Common Error Codes:**

| Code | Description | Example Fix |
|------|-------------|-------------|
| E231 | Missing whitespace after comma | `func(a,b)` → `func(a, b)` |
| E225 | Missing whitespace around operator | `x=1` → `x = 1` |
| E501 | Line too long (>79 characters) | Split line or use parentheses |
| E302 | Expected 2 blank lines | Add blank lines between functions |
| E303 | Too many blank lines | Remove extra blank lines |
| E712 | Comparison to True/False | `if x == True:` → `if x:` |
| E722 | Bare except clause | `except:` → `except ValueError:` |
| E731 | Lambda assignment | Use `def` for named functions |
| F401 | Module imported but unused | Remove unused import |
| F841 | Local variable assigned but unused | Remove or use the variable |
| F632 | Use ==/!= for comparison | `is "text"` → `== "text"` |
| W292 | No newline at end of file | Add newline at end |

#### Fixing Linting Issues

Let's fix the violations systematically. Here's the corrected version:

##### Listing 5-7: `example_clean.py` - Code Following PEP 8

```python
"""
Example module demonstrating clean, PEP 8 compliant code.
"""

import math


# Constants use UPPERCASE naming
GLOBAL_VARIABLE = 100
ANOTHER_GLOBAL_VARIABLE = 200


def calculate_total(x, y, z):
    """
    Calculate total with proper formatting.

    Args:
        x: First number
        y: Second number
        z: Third number

    Returns:
        Sum of x, y, and z
    """
    result = x + y + z
    return result


def process_data(data):
    """
    Process data with proper style.

    Args:
        data: Data to process

    Returns:
        Processed result
    """
    # Separate statements on different lines
    x = 1
    y = 2
    z = 3

    # Split long lines appropriately
    very_long_variable_name = (
        "This string is split across multiple lines "
        "to keep line length under 79 characters"
    )

    # Use truthiness directly (Pythonic)
    if data:
        return "yes"

    # Specify exception type
    try:
        result = int(data)
    except (ValueError, TypeError):
        result = 0

    return result


class MyClass:
    """Example class following PEP 8 conventions."""

    def __init__(self, value):
        """Initialize with a value."""
        self.value = value

    def get_value(self):
        """Get the current value."""
        return self.value


# Use def instead of lambda for named functions
def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def check_status(status):
    """Check if status is active."""
    if status == "active":  # Use == for value comparison
        return True
    return False
```

Running flake8 on the cleaned code:

```bash
$ flake8 example_clean.py

# No output - all checks passed!
```

When flake8 produces no output, it means your code passes all checks. This is the goal: clean, PEP 8-compliant code.

#### Configuring flake8

While flake8 works well with default settings, you can customize its behavior using a configuration file. Create a `.flake8` file in your project root:

##### Listing 5-8: `.flake8` - Configuration File

```ini
[flake8]
# Maximum line length
max-line-length = 79

# Ignore specific errors (use sparingly)
ignore = 
    # Ignore specific codes if needed
    # E203,  # whitespace before ':'
    # W503,  # line break before binary operator

# Exclude directories from checking
exclude =
    .git,
    __pycache__,
    .pytest_cache,
    *.pyc,
    .venv,
    venv,
    env,
    build,
    dist

# Per-file ignores (for specific cases)
per-file-ignores =
    # Allow unused imports in __init__.py
    __init__.py: F401

# Show source code for each error
show-source = True

# Count errors and show statistics
count = True
statistics = True
```

Common configuration options:

- **max-line-length**: Override the default 79 character limit (use cautiously)
- **ignore**: Skip specific error codes (avoid overusing)
- **exclude**: Directories and files to skip
- **per-file-ignores**: File-specific exceptions
- **max-complexity**: Set McCabe complexity threshold (default: 10)

#### Integrating flake8 with Your Workflow

##### Running flake8 with pytest

You can integrate flake8 checks into your pytest workflow using the pytest-flake8 plugin:

```bash
# Install the plugin
pip install pytest-flake8

# Run tests and flake8 checks together
pytest --flake8
```

This ensures code quality checks run alongside your tests, catching style issues early in development.

##### Pre-commit Hooks

Set up flake8 to run automatically before commits:

```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
# Then run:
pre-commit install
```

##### Continuous Integration

Add flake8 to your CI pipeline:

```yaml
# Example GitHub Actions workflow
- name: Lint with flake8
  run: |
    pip install flake8
    flake8 src/ tests/ --count --show-source --statistics
```

#### Best Practices for Linting

1. **Run Early and Often**: Check code before committing
2. **Fix Issues Promptly**: Don't accumulate technical debt
3. **Understand Violations**: Learn why each rule exists
4. **Configure Thoughtfully**: Customize only when necessary
5. **Team Consensus**: Agree on standards as a team
6. **Gradual Adoption**: For existing projects, fix issues incrementally
7. **Document Exceptions**: Comment why you ignore specific warnings
8. **Combine with Other Tools**: Use flake8 alongside black, pylint, mypy

#### Common Pitfalls and Solutions

**Problem**: Too many line length violations
**Solution**: Use implicit line continuation with parentheses:

```python
# Instead of:
result = some_function(arg1, arg2, arg3, arg4, arg5, arg6)  # E501

# Use:
result = some_function(
    arg1, arg2, arg3, 
    arg4, arg5, arg6
)
```

**Problem**: Unused imports flagged
**Solution**: Remove them or use `# noqa: F401` if needed for __init__.py:

```python
from .module import MyClass  # noqa: F401
```

**Problem**: Lambda assignments flagged
**Solution**: Use def for named functions:

```python
# Instead of:
square = lambda x: x ** 2  # E731

# Use:
def square(x):
    return x ** 2
```

#### flake8 Summary

flake8 enforces code quality standards automatically, catching style violations and potential bugs before they cause problems. By integrating flake8 into your development workflow alongside pytest, you ensure both functional correctness (through tests) and code quality (through linting).

Key takeaways:
- flake8 checks for PEP 8 compliance, logical errors, and complexity
- Error codes indicate the type and severity of violations
- Configuration files allow project-specific customization
- Integration with pytest and CI ensures consistent code quality
- Regular linting improves code maintainability and reduces bugs

Combined with coverage analysis from pytest-cov, flake8 forms part of a comprehensive quality assurance strategy that validates both what your code does and how it's written.


### Automating Code Formatting with black

While flake8 identifies style violations and requires manual fixes, black takes a different approach: it automatically reformats your code to conform to a consistent style. black is an opinionated, uncompromising code formatter that eliminates debates about formatting by enforcing a single, deterministic style across your entire codebase.

#### The Philosophy of black

black's philosophy is simple but powerful: **"Any color you like, as long as it's black."** This approach, borrowed from Henry Ford's famous quote about the Model T, reflects black's core principle—it gives you no choices about code style. While this might seem restrictive, it offers significant benefits:

- **Eliminates bikeshedding**: No more debates about formatting preferences
- **Reduces cognitive load**: Focus on logic, not aesthetics
- **Ensures consistency**: All code looks the same, regardless of author
- **Saves time**: Automatic formatting is faster than manual editing
- **Improves collaboration**: Uniform style across the entire team
- **Reduces diff noise**: Formatting changes don't clutter code reviews

black's formatting choices are deliberately designed to optimize for readability and vertical space efficiency. The result is code that's easy to scan and understand, even if it doesn't match your personal preferences.

#### Installing black

Install black using pip:

```bash
pip install black
```

black requires Python 3.6+ and works with code written for Python 3.6 through the latest version. For specific Python version support, use:

```bash
# Format code targeting a specific Python version
black --target-version py39 myfile.py
```

#### Running black

black is designed to be simple to use. Point it at a file or directory, and it reformats everything:

```bash
# Format a single file
black myfile.py

# Format all Python files in a directory
black myproject/

# Format specific files
black file1.py file2.py file3.py

# Check what would be changed without modifying files
black --check myproject/

# Show a diff of what would change
black --diff myproject/
```

The `--check` flag is particularly useful in CI/CD pipelines—it exits with a non-zero status if any files would be reformatted, allowing you to enforce formatting in automated checks.

#### black in Action

Let's see black transform poorly formatted code. Consider this example with inconsistent spacing, line lengths, and formatting:

##### Listing 5-9: `example_unformatted.py` - Code Before black

```python
"""Example showing code before black formatting."""

def calculate_statistics(data,include_mean=True,include_median=False,include_mode=False):
    """Calculate various statistics with poor formatting."""
    results={}
    
    if include_mean:
        results['mean']=sum(data)/len(data)
    
    if include_median:
        sorted_data=sorted(data)
        n=len(sorted_data)
        if n%2==0:
            results['median']=(sorted_data[n//2-1]+sorted_data[n//2])/2
        else:
            results['median']=sorted_data[n//2]
    
    if include_mode:
        from collections import Counter
        counts=Counter(data)
        results['mode']=counts.most_common(1)[0][0]
    
    return results


class DataProcessor:
    """Process data with inconsistent formatting."""
    
    def __init__(self,data,normalize=False,remove_outliers=True,outlier_threshold=3.0):
        self.data=data
        self.normalize=normalize
        self.remove_outliers=remove_outliers
        self.outlier_threshold=outlier_threshold
    
    def process(self):
        """Process the data."""
        result=self.data[:]
        
        if self.remove_outliers:
            mean=sum(result)/len(result)
            std_dev=(sum((x-mean)**2 for x in result)/len(result))**0.5
            result=[x for x in result if abs(x-mean)<=self.outlier_threshold*std_dev]
        
        if self.normalize:
            min_val,max_val=min(result),max(result)
            result=[(x-min_val)/(max_val-min_val) for x in result]
        
        return result


def complex_function_with_long_arguments(argument_one,argument_two,argument_three,argument_four,argument_five,argument_six):
    """Function with too many arguments on one line."""
    return argument_one+argument_two+argument_three+argument_four+argument_five+argument_six


# Dictionary with inconsistent formatting
config={'database':{'host':'localhost','port':5432,'username':'admin','password':'secret'},'cache':{'enabled':True,'ttl':3600},'logging':{'level':'INFO','format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s'}}


# List comprehension that's too long
def example_with_long_comprehension():
    """Example function with a long list comprehension."""
    data_source = []
    filtered_and_transformed_data=[x*2 for x in data_source if x>0 and x<100 and x%2==0]
    return filtered_and_transformed_data
```

Now let's run black on this file:

```bash
$ black example_unformatted.py

reformatted example_unformatted.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

##### Listing 5-10: `example_formatted.py` - Code After black

```python
"""Example showing code after black formatting."""

from collections import Counter


def calculate_statistics(
    data, include_mean=True, include_median=False, include_mode=False
):
    """Calculate various statistics with proper formatting."""
    results = {}

    if include_mean:
        results["mean"] = sum(data) / len(data)

    if include_median:
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            results["median"] = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            results["median"] = sorted_data[n // 2]

    if include_mode:
        counts = Counter(data)
        results["mode"] = counts.most_common(1)[0][0]

    return results


class DataProcessor:
    """Process data with consistent formatting."""

    def __init__(
        self,
        data,
        normalize=False,
        remove_outliers=True,
        outlier_threshold=3.0,
    ):
        self.data = data
        self.normalize = normalize
        self.remove_outliers = remove_outliers
        self.outlier_threshold = outlier_threshold

    def process(self):
        """Process the data."""
        result = self.data[:]

        if self.remove_outliers:
            mean = sum(result) / len(result)
            std_dev = (sum((x - mean) ** 2 for x in result) / len(result)) ** 0.5
            result = [
                x for x in result if abs(x - mean) <= self.outlier_threshold * std_dev
            ]

        if self.normalize:
            min_val, max_val = min(result), max(result)
            result = [(x - min_val) / (max_val - min_val) for x in result]

        return result


def complex_function_with_long_arguments(
    argument_one,
    argument_two,
    argument_three,
    argument_four,
    argument_five,
    argument_six,
):
    """Function with arguments properly split across lines."""
    return (
        argument_one
        + argument_two
        + argument_three
        + argument_four
        + argument_five
        + argument_six
    )


# Dictionary with proper formatting
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secret",
    },
    "cache": {"enabled": True, "ttl": 3600},
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    },
}


# List comprehension properly formatted
def example_with_long_comprehension():
    """Example function with a properly formatted list comprehension."""
    data_source = []
    filtered_and_transformed_data = [
        x * 2 for x in data_source if x > 0 and x < 100 and x % 2 == 0
    ]
    return filtered_and_transformed_data
```

Notice how black has:

- Added consistent spacing around operators (`=`, `+`, `-`, etc.)
- Split long function signatures across multiple lines
- Formatted dictionaries and lists for readability
- Added proper spacing in expressions
- Reorganized imports (moved `Counter` import to the top)
- Applied consistent string quote style (double quotes)
- Ensured proper vertical spacing between functions and classes

#### Key black Formatting Rules

Understanding black's key formatting decisions helps you write code that's already black-compliant:

**Line Length:**
- Default maximum: 88 characters (slightly longer than PEP 8's 79)
- Optimized for modern displays and readability
- Configurable via `--line-length` option

**String Quotes:**
- Prefers double quotes (`"`) over single quotes (`'`)
- Uses whichever requires fewer escapes
- Normalizes triple-quoted strings

**Function Arguments:**
- Keeps short signatures on one line
- Splits long signatures with one argument per line
- Trailing commas for multi-line signatures

**Collections (Lists, Dicts, Sets):**
- Short collections stay on one line
- Long collections split with one element per line
- Trailing commas when split across lines

**Operators:**
- Consistent spacing around binary operators
- Line breaks before operators in multi-line expressions

**Imports:**
- Groups imports by type (standard library, third-party, local)
- Alphabetizes within groups
- Removes unused imports (when combined with other tools)

#### Configuring black

While black is intentionally opinionated, it does offer minimal configuration options. Create a `pyproject.toml` file in your project root:

##### Listing 5-11: `pyproject.toml` - black Configuration

```toml
[tool.black]
line-length = 88
target-version = ['py39', 'py310', 'py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

Configuration options:

- **line-length**: Maximum line length (default: 88)
- **target-version**: Python versions to target
- **include**: Regex pattern for files to format
- **exclude**: Files/directories to skip
- **extend-exclude**: Additional exclusions beyond defaults

**Note:** black intentionally limits configuration to prevent fragmentation of code styles across projects.

#### Integrating black with flake8

black and flake8 can conflict on certain style rules. To use them together, configure flake8 to ignore black-compatible rules:

##### Listing 5-12: `.flake8` - Configuration for black Compatibility

```ini
[flake8]
max-line-length = 88
extend-ignore = E203, E501, W503
exclude =
    .git,
    __pycache__,
    .pytest_cache,
    *.pyc,
    .venv,
    venv,
    build,
    dist
```

**Ignored rules:**
- **E203**: Whitespace before ':' (conflicts with black's slice formatting)
- **E501**: Line too long (black handles line length)
- **W503**: Line break before binary operator (black's preferred style)

#### black in Your Development Workflow

##### Formatting Before Committing

Run black on modified files before committing:

```bash
# Format all changed files
git diff --name-only --diff-filter=ACMRTU | grep '\.py$' | xargs black

# Or use git hooks (see pre-commit integration below)
```

##### IDE Integration

Most modern IDEs support black integration:

**VS Code:**
Install the Python extension, then configure in settings.json:

```json
{
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "88"],
  "editor.formatOnSave": true
}
```

**PyCharm:**
Configure as an external tool or use the "BlackConnect" plugin for real-time formatting.

##### Pre-commit Hook Integration

Automate black formatting with pre-commit hooks:

##### Listing 5-13: `.pre-commit-config.yaml` - black Pre-commit Hook

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1  # Use the latest stable version
    hooks:
      - id: black
        language_version: python3.11
        args: ['--line-length=88']
```

Install and activate:

```bash
pip install pre-commit
pre-commit install
```

Now black runs automatically on staged files before each commit.

##### CI/CD Integration

Enforce black formatting in continuous integration:

##### Listing 5-14: GitHub Actions Workflow with black

```yaml
name: Code Quality

on: [push, pull_request]

jobs:
  format-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install black
        run: pip install black
      
      - name: Check formatting with black
        run: black --check --diff .
```

The `--check` flag ensures the build fails if any files aren't formatted, while `--diff` shows what would change.

#### black vs Other Formatters

Python has several code formatters. Here's how black compares:

| Feature | black | autopep8 | yapf |
|---------|-------|----------|------|
| **Philosophy** | Uncompromising | PEP 8 compliant | Configurable |
| **Configuration** | Minimal | Moderate | Extensive |
| **Stability** | Deterministic | Deterministic | Deterministic |
| **Speed** | Fast | Fast | Moderate |
| **Adoption** | High (growing) | High | Moderate |
| **Best For** | Teams wanting consistency | PEP 8 compliance | Custom style |

**black's advantages:**
- Zero configuration needed
- Eliminates style debates
- Growing ecosystem support
- Fast and reliable

**When to choose alternatives:**
- You need extensive customization (yapf)
- You must strictly follow PEP 8's 79-character limit (autopep8)
- You're working with an established codebase with a different style

#### Best Practices for Using black

1. **Adopt Early**: Introduce black at project start to avoid large reformatting commits
2. **Format Everything**: Apply black to the entire codebase consistently
3. **Use in CI**: Enforce formatting in your build pipeline
4. **Combine with Linters**: Use black for formatting, flake8/pylint for style/quality
5. **Educate the Team**: Ensure everyone understands black's philosophy and benefits
6. **Format on Save**: Enable IDE integration for real-time formatting
7. **Document the Choice**: Add black configuration to your project's README
8. **Version Control**: Commit `.blackrc` or pyproject.toml configuration

#### Handling Legacy Codebases

Introducing black to an existing project requires care:

1. **Branch Strategy**: Create a dedicated "black formatting" branch
2. **Format in One Commit**: Reformat the entire codebase in a single commit
3. **Document the Change**: Clear commit message explaining the reformatting
4. **Merge Carefully**: Coordinate with the team to minimize merge conflicts
5. **Git Blame Workaround**: Use `git blame --ignore-rev` to skip the formatting commit

Create a `.git-blame-ignore-revs` file listing the formatting commit:

```
# black code formatting - 2025-11-07
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
```

Then configure git:

```bash
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

#### Common Questions About black

**Q: Can I customize black's formatting?**
A: black intentionally offers minimal configuration. The line length and target Python version are configurable, but most formatting decisions are fixed.

**Q: What if I disagree with black's choices?**
A: black's philosophy is that consistency matters more than personal preference. The time saved not debating formatting outweighs any style differences.

**Q: Does black slow down my workflow?**
A: No—black is very fast, typically formatting an entire project in seconds. IDE integration makes it seamless.

**Q: Can I disable black for specific code sections?**
A: Yes, use `# fmt: off` and `# fmt: on` comments:

```python
# fmt: off
matrix = [[1,  2,  3],
          [4,  5,  6],
          [7,  8,  9]]
# fmt: on
```

Use this sparingly—only when manual formatting enhances readability.

**Q: How does black handle comments?**
A: black preserves comments and docstrings, reformatting their surrounding code while maintaining comment placement.

#### black Summary

black represents a paradigm shift in code formatting: instead of debating style choices, let a tool enforce consistency automatically. By eliminating formatting decisions, black allows developers to focus on what matters—writing correct, maintainable code.

Key benefits:
- **Consistency**: Uniform style across all code
- **Speed**: Automatic formatting is faster than manual editing
- **Simplicity**: Minimal configuration, maximum result
- **Integration**: Works seamlessly with modern development tools
- **Adoption**: Growing standard in the Python community

When combined with pytest-cov (coverage), flake8 (linting), and mypy (type checking), black completes a comprehensive code quality toolkit. Together, these tools ensure your code is not only functional and tested but also consistently formatted and maintainable.


### Advanced Static Analysis with pylint

While flake8 focuses on style consistency and simple error detection, pylint offers a more comprehensive static analysis experience. pylint examines your code for a wider range of issues including code smells, design problems, and potential bugs. It provides detailed feedback through a scoring system and categorizes issues by severity, making it an excellent tool for maintaining high code quality standards.

#### What pylint Offers Beyond flake8

pylint provides deeper analysis than flake8:

- **Code Quality Metrics**: Assigns a quality score (0-10) to your code
- **Broader Issue Detection**: Finds design problems, code smells, and complex issues
- **Refactoring Suggestions**: Identifies opportunities to improve code structure
- **Detailed Categories**: Organizes messages by type (Convention, Refactor, Warning, Error)
- **Customizable Standards**: Extensive configuration options to match team preferences
- **Plugin Architecture**: Extensible with custom checkers

#### Understanding pylint Message Categories

pylint categorizes issues into five types:

- **C (Convention)**: Coding standard violations (naming, docstrings, formatting)
- **R (Refactor)**: Code that could be improved or simplified (complexity, design)
- **W (Warning)**: Potential problems that might cause bugs (unused variables, dangerous defaults)
- **E (Error)**: Likely bugs or errors in the code (undefined variables, import errors)
- **F (Fatal)**: Errors that prevent pylint from continuing analysis

Each message has a unique identifier (e.g., C0103, R0913, W0612, E1101) that you can use for configuration.

#### Installing and Running pylint

Install pylint using pip:

```bash
$ pip install pylint
```

Run pylint on a file or directory:

```bash
$ pylint mymodule.py

$ pylint mypackage/

$ pylint .
```

#### Example: Running pylint on Problem Code

Let's examine `example_with_pylint_issues.py`, which contains various issues pylint will detect:

```bash
$ cd code/ch05
$ pylint example_with_pylint_issues.py
```

pylint will produce extensive output. Here's a sample of what you might see:

```
************* Module example_with_pylint_issues
example_with_pylint_issues.py:1:0: C0114: Missing module docstring (missing-module-docstring)
example_with_pylint_issues.py:14:0: C0103: Constant name "myGlobalVar" doesn't conform to UPPER_CASE naming style (invalid-name)
example_with_pylint_issues.py:18:0: R0913: Too many arguments (10/5) (too-many-arguments)
example_with_pylint_issues.py:25:0: R0914: Too many local variables (16/15) (too-many-locals)
example_with_pylint_issues.py:50:0: C0115: Missing class docstring (missing-class-docstring)
example_with_pylint_issues.py:53:4: C0116: Missing function or method docstring (missing-function-docstring)
example_with_pylint_issues.py:58:4: R0201: Method could be a function (no-self-use)
example_with_pylint_issues.py:63:4: W0613: Unused argument 'debug' (unused-argument)
example_with_pylint_issues.py:71:0: R0912: Too many branches (13/12) (too-many-branches)
example_with_pylint_issues.py:95:0: R0911: Too many return statements (8/6) (too-many-returns)
example_with_pylint_issues.py:8:0: W0611: Unused import time (unused-import)
example_with_pylint_issues.py:116:0: C0103: Function name "CalculateTotal" doesn't conform to snake_case naming style (invalid-name)
example_with_pylint_issues.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
example_with_pylint_issues.py:125:0: C0103: Function name "add" doesn't conform to snake_case naming style (invalid-name)
example_with_pylint_issues.py:130:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
example_with_pylint_issues.py:139:0: W0703: Catching too general exception Exception (broad-except)

------------------------------------------------------------------
Your code has been rated at 4.12/10 (previous run: 4.12/10, +0.00)
```

The output shows:
- **Location**: File, line number, and column
- **Message ID**: Code like C0103, R0913, W0613
- **Message**: Description of the issue
- **Symbol**: Short name in parentheses
- **Score**: Overall code quality rating (out of 10)

#### Common pylint Messages and How to Address Them

##### C0103: invalid-name

Variables, functions, and classes should follow Python naming conventions:

```python
# Bad
myGlobalVar = 42
def CalculateTotal(items):
    pass

# Good
MY_GLOBAL_VAR = 42
def calculate_total(items):
    pass
```

##### C0114, C0115, C0116: Missing Docstrings

All modules, classes, and functions should have docstrings:

```python
# Bad
def add(a, b):
    return a + b

# Good
def add(a, b):
    """Add two numbers and return the result."""
    return a + b
```

##### R0913: too-many-arguments

Functions should have a reasonable number of parameters (default max: 5):

```python
# Bad
def process_data(name, age, email, phone, address, city, state, zip):
    pass

# Good - use a dataclass or dictionary
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int
    email: str
    phone: str
    address: str
    city: str
    state: str
    zip_code: str

def process_data(user: UserData):
    pass
```

##### R0914: too-many-locals

Functions with too many local variables are hard to understand:

```python
# Bad - 16 local variables
def calculate_complex_result(x, y):
    var1 = x + y
    var2 = x - y
    # ... 14 more variables
    return var16

# Good - break into smaller functions
def calculate_sum_diff(x, y):
    return x + y, x - y

def calculate_products(x, y):
    return x * y, x / y if y != 0 else 0
```

##### R0912: too-many-branches

Functions with excessive conditionals should be refactored:

```python
# Bad - 13 branches
def complex_conditional(status_code):
    if status_code == 200:
        return "OK"
    elif status_code == 201:
        return "Created"
    # ... 11 more branches

# Good - use a dictionary
HTTP_STATUS_MESSAGES = {
    200: "OK",
    201: "Created",
    204: "No Content",
    # ... more mappings
}

def get_status_message(status_code):
    """Get HTTP status message for a status code."""
    return HTTP_STATUS_MESSAGES.get(status_code, "Unknown")
```

##### W0102: dangerous-default-value

Mutable default arguments can cause unexpected behavior:

```python
# Bad
def append_to_list(item, target_list=[]):
    target_list.append(item)
    return target_list

# Good
def append_to_list(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

##### W0611: unused-import

Remove imports that aren't used:

```python
# Bad
import time  # Never used in the code

# Good - only import what you need
import sys
import os
```

##### W0703: broad-except

Catch specific exceptions instead of broad Exception:

```python
# Bad
try:
    result = risky_operation()
except Exception:
    return None

# Good
try:
    result = risky_operation()
except (ValueError, KeyError) as e:
    logger.error(f"Operation failed: {e}")
    return None
```

#### Configuring pylint

Create a `.pylintrc` file to customize pylint's behavior:

```bash
$ pylint --generate-rcfile > .pylintrc
```

This generates a comprehensive configuration file. Here are key sections to customize:

##### Listing 5-11: `.pylintrc` - Essential Configuration

```ini
[MASTER]
# Use multiple processes to speed up Pylint
jobs=1

[MESSAGES CONTROL]
# Disable specific messages
disable=
    C0111,  # missing-docstring
    R0903,  # too-few-public-methods

[FORMAT]
# Maximum line length (88 matches black)
max-line-length=88

[DESIGN]
# Maximum number of arguments
max-args=5

# Maximum number of branches
max-branches=12

# Maximum number of local variables
max-locals=15
```

Common configuration options:

- **max-line-length**: Set to 88 to match black's default
- **max-args**: Adjust maximum function arguments (default: 5)
- **max-locals**: Maximum local variables in a function (default: 15)
- **max-branches**: Maximum branches in a function (default: 12)
- **disable**: List of message IDs to disable

#### Disabling Specific pylint Checks

Disable checks at different scopes:

**Disable globally** in `.pylintrc`:

```ini
[MESSAGES CONTROL]
disable=C0103,R0903
```

**Disable for entire file** at the top:

```python
# pylint: disable=invalid-name,missing-docstring
```

**Disable for specific line**:

```python
myVariable = 42  # pylint: disable=invalid-name
```

**Disable for code block**:

```python
# pylint: disable=too-many-locals
def complex_function():
    # ... lots of local variables
    pass
# pylint: enable=too-many-locals
```

Use disabling judiciously—understanding and fixing issues is usually better than suppressing them.

#### pylint vs flake8: When to Use Each

**Use flake8 when:**
- You want fast, focused checks on style and simple errors
- You're starting with linting and want quick wins
- You need minimal configuration
- You want to run checks quickly in CI/CD

**Use pylint when:**
- You want comprehensive code analysis
- You need refactoring suggestions and design feedback
- You want detailed code quality metrics
- You're maintaining large codebases with high quality standards
- You want to catch complex issues and code smells

**Best practice**: Use both! Run flake8 for quick feedback during development, and run pylint periodically for deeper analysis.

#### Integrating pylint with pytest

You can run pylint checks as part of your test suite. Create a test file:

##### Listing 5-12: `test_pylint.py` - Running pylint in Tests

```python
"""Test that runs pylint on the codebase."""

import subprocess
import sys


def test_pylint_score():
    """Ensure pylint score meets minimum threshold."""
    result = subprocess.run(
        ["pylint", "calculator.py"],
        capture_output=True,
        text=True,
        check=False
    )
    
    # Extract score from output
    for line in result.stdout.split('\n'):
        if 'Your code has been rated at' in line:
            # Parse: "Your code has been rated at 8.50/10"
            score_str = line.split('at ')[1].split('/')[0]
            score = float(score_str)
            
            # Require minimum score of 8.0
            assert score >= 8.0, f"pylint score {score} below minimum 8.0"
            print(f"✓ pylint score: {score}/10")
            return
    
    # If we couldn't parse the score, fail the test
    pytest.fail("Could not determine pylint score")


def test_pylint_no_errors():
    """Ensure no pylint errors (E) or fatal (F) messages."""
    result = subprocess.run(
        ["pylint", "calculator.py"],
        capture_output=True,
        text=True,
        check=False
    )
    
    # Check for error or fatal messages
    errors = []
    for line in result.stdout.split('\n'):
        if ':E' in line or ':F' in line:
            errors.append(line)
    
    assert not errors, f"Found pylint errors:\n" + "\n".join(errors)
```

#### Running pylint in CI/CD

Add pylint checks to your GitHub Actions workflow:

```yaml
- name: Run pylint
  run: |
    pip install pylint
    pylint src/ --fail-under=8.0
```

The `--fail-under` flag causes pylint to exit with an error if the score is below the threshold.

#### Example: Refactored Code with High Quality Score

After systematically addressing pylint feedback, you can achieve excellent scores. The file `example_pylint_clean.py` demonstrates the same functionality as `example_with_pylint_issues.py` but refactored to address all warnings:

```bash
$ pylint example_pylint_clean.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10
```

A perfect 10/10 score indicates the code meets high quality standards. The refactored version demonstrates:

**Naming Improvements:**
- `myGlobalVar` → `MY_GLOBAL_VAR` (proper constant naming)
- `CalculateTotal` → `calculate_total` (snake_case for functions)

**Design Simplifications:**
- Reduced function arguments from 10 to 3 parameters
- Replaced long if-elif chains with dictionary lookups
- Combined multiple return statements into single conditional expressions
- Broke complex functions into smaller, focused units

**Documentation Added:**
- Module-level docstring explaining purpose
- Class and function docstrings with Args/Returns sections
- Clear descriptions of behavior and intent

**Best Practice Fixes:**
- Changed mutable defaults `[]` to `None` with initialization
- Used specific exception types instead of broad `Exception`
- Removed unused imports
- Applied `enumerate()` instead of `range(len())`
- Used context managers (`with`) for file operations
- Fixed None comparisons (`is not None` vs `!= None`)

The transformation from 6.88/10 to 10.00/10 demonstrates how pylint guidance improves code maintainability, readability, and adherence to Python best practices.

#### Best Practices for Using pylint

1. **Start Gradually**: Don't expect a perfect 10/10 score immediately
2. **Set Realistic Thresholds**: Start with a minimum score of 7.0-8.0
3. **Disable Selectively**: Disable messages that don't apply to your project
4. **Focus on Errors First**: Fix E and F messages before addressing C and R
5. **Configure Once**: Create a `.pylintrc` that matches your team's standards
6. **Review Regularly**: Run pylint periodically, not just in CI/CD
7. **Balance with Pragmatism**: Sometimes breaking a rule is justified—document why
8. **Combine with Other Tools**: Use alongside flake8, black, and mypy

#### Common pylint Configuration Patterns

For **Django projects**, disable false positives:

```ini
[MESSAGES CONTROL]
disable=
    C5121,  # no-member (Django models)
    R0901,  # too-many-ancestors (Django class-based views)

load-plugins=pylint_django
```

For **test files**, relax some restrictions:

```ini
[MESSAGES CONTROL]
disable=
    C0116,  # missing-function-docstring
    R0913,  # too-many-arguments (test fixtures)
```

For **scripts and small modules**:

```ini
[DESIGN]
min-public-methods=1
max-module-lines=500
```

#### pylint Summary

pylint is a powerful tool for maintaining high code quality through comprehensive static analysis. While it can be strict, its detailed feedback helps identify real issues and improvement opportunities.

Key advantages:
- **Comprehensive Analysis**: Goes beyond style to detect design issues
- **Quality Metrics**: Provides actionable scores and categorized feedback
- **Highly Configurable**: Adapts to team standards and project needs
- **Refactoring Guide**: Suggests improvements to code structure
- **Educational**: Teaches Python best practices and conventions

Use pylint as part of a comprehensive quality toolkit alongside pytest-cov, flake8, black, and mypy. Together, these tools ensure your code is tested, consistent, maintainable, and high-quality.


##### Listing 5-?: Performance Profiling with `cProfile`

```python
import cProfile

from application import Application

def main():
    # Function to be profiled
    application.get_by_id(73)

if __name__ == "__main__":
    cProfile.run('main()', 'profile_stats')

# Analyze the output using pstats module
import pstats
p = pstats.Stats('profile_stats')
p.sort_stats('time').print_stats()
```

This example demonstrates using `cProfile` to profile a Python application, identifying performance-critical sections that may benefit from optimization.

#### Incorporating Dynamic Analysis into Development

Incorporating dynamic analysis into the development process requires regular and systematic execution of tests under varied conditions, monitoring performance, and analyzing runtime behavior. It's a proactive measure to ensure software performance and reliability meet the expectations without waiting for issues to manifest in production environments.

#### Dynamic Analysis: Summary

Dynamic analysis is a key aspect of a comprehensive software testing strategy, providing critical insights into the runtime behavior of applications. By integrating dynamic analysis tools and practices, developers can proactively identify and address potential issues, ensuring that the software delivers optimal performance and reliability. In the Python development landscape, leveraging tools like `pytest-cov`, `cProfile`, and the `logging` module, among others, facilitates a robust approach to dynamic analysis, complementing static analysis efforts and contributing to the overall quality of the software development lifecycle.


### Chapter Summary

This chapter presented a structured framework for advancing software quality. It is the _Analyze_, _Improve_, and _Monitor_ cycle. This conceptual model lays the groundwork for continuous improvement within software development processes. We delved into two principal facets of code analysis, static analysis and dynamic analysis, each offering unique insights into software construction and behavior.

#### Static Analysis: A Closer Look at Code Quality

Static analysis serves as a foundational step in the software improvement cycle, offering a lens through which the construction quality of software is evaluated without the need to execute the program. This approach scrutinizes source code and assemblies to ensure adherence to coding standards and best practices, aiding in the identification of potential issues that could compromise software quality.

#### Dynamic Analysis: Understanding Runtime Behavior

Dynamic analysis complements static analysis by examining the software in action. Through techniques such as sampling and instrumentation, dynamic analysis captures valuable data about the software's performance, memory usage, and overall behavior during execution. This process is instrumental in uncovering areas of the code that may not be adequately tested and identifying opportunities for optimization.

#### Python Development

The principles of code analysis apply universally across software development environments, including Python. The transition to Python emphasizes the adaptability of these practices, with tools like pytest for dynamic analysis and various linters and type checkers for static analysis playing crucial roles in maintaining and improving software quality.

#### Integration with Application Lifecycle Management (ALM)

Code analysis is integral to Application Lifecycle Management (ALM), encompassing security analysis, adherence to recommended patterns, and best practices. The application of rigorous code analysis techniques is essential for active analysis, targeted improvements, and ongoing monitoring, ensuring that software development aligns with both technical and business objectives.

#### Conclusion

This chapter highlighted the significance of a methodical approach to code analysis within the broader context of software development. By embracing the Analyze, Improve, and Monitor cycle, developers can ensure their software not only meets current standards but is also positioned for future enhancements and growth. Incorporating these tools underscores the versatility and universal applicability of these concepts, demonstrating their value in fostering software excellence across diverse development ecosystems.



[^1]: More info on [cProfile and profile](https://docs.python.org/3/library/profile.html)

[Continue to Chapter 6](../ch06/chapter06.md)
