@echo off
REM Script to run tests with coverage on Windows

echo =========================================
echo Running Skylab2IAI Test Suite
echo =========================================
echo.

REM Check if pytest is installed
python -c "import pytest" 2>nul
if errorlevel 1 (
    echo Installing test dependencies...
    pip install -e ".[dev]"
    echo.
)

REM Run tests with coverage
echo Running tests...
pytest --cov=skylab2iai --cov-report=term-missing --cov-report=html --cov-report=xml -v

echo.
echo =========================================
echo Test Summary
echo =========================================
echo Coverage report generated:
echo   - Terminal: see above
echo   - HTML: htmlcov\index.html
echo   - XML: coverage.xml
echo.
echo To view HTML report:
echo   start htmlcov\index.html
echo.
pause
