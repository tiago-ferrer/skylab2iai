#!/bin/bash
# Script to run tests with coverage

set -e

echo "========================================="
echo "Running Skylab2IAI Test Suite"
echo "========================================="
echo ""

# Check if pytest is installed
if ! python -c "import pytest" 2>/dev/null; then
    echo "Installing test dependencies..."
    pip install -e ".[dev]"
    echo ""
fi

# Run tests with coverage
echo "Running tests..."
pytest --cov=skylab2iai \
       --cov-report=term-missing \
       --cov-report=html \
       --cov-report=xml \
       -v

echo ""
echo "========================================="
echo "Test Summary"
echo "========================================="
echo "Coverage report generated:"
echo "  - Terminal: see above"
echo "  - HTML: htmlcov/index.html"
echo "  - XML: coverage.xml"
echo ""
echo "To view HTML report:"
echo "  open htmlcov/index.html"
echo ""
