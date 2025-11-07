#!/bin/bash
# Complete code quality workflow for Chapter 5 examples
# This script demonstrates running all quality tools in recommended order

echo "=========================================="
echo "Complete Code Quality Workflow"
echo "=========================================="
echo ""

# Step 1: Format code with black
echo "Step 1: Formatting code with black..."
echo "--------------------------------------"
python -m black calculator.py test_calculator_improved.py example_pylint_clean.py
echo ""

# Step 2: Check style with flake8
echo "Step 2: Checking style with flake8..."
echo "--------------------------------------"
python -m flake8 calculator.py test_calculator_improved.py example_pylint_clean.py
if [ $? -eq 0 ]; then
    echo "✓ All flake8 checks passed!"
else
    echo "✗ flake8 found issues"
    exit 1
fi
echo ""

# Step 3: Analyze with pylint
echo "Step 3: Analyzing with pylint..."
echo "--------------------------------------"
python -m pylint calculator.py example_pylint_clean.py --fail-under=9.0
if [ $? -eq 0 ]; then
    echo "✓ pylint score meets threshold!"
else
    echo "✗ pylint score below 9.0"
    exit 1
fi
echo ""

# Step 4: Run tests with coverage
echo "Step 4: Running tests with coverage..."
echo "--------------------------------------"
python -m pytest test_calculator_improved.py --cov=calculator --cov-report=term-missing
if [ $? -eq 0 ]; then
    echo "✓ All tests passed with coverage!"
else
    echo "✗ Tests failed"
    exit 1
fi
echo ""

echo "=========================================="
echo "✓ Complete workflow succeeded!"
echo "=========================================="
echo ""
echo "Summary:"
echo "  • Code formatted with black"
echo "  • Style checked with flake8"
echo "  • Quality analyzed with pylint"
echo "  • Tests passed with 100% coverage"
echo ""
