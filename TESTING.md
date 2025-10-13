# Testing Documentation

## Overview

This document provides comprehensive information about the test suite for Skylab2IAI.

## Test Coverage

The test suite aims for **100% code coverage** across all modules:

### Modules Tested
- ✅ `skylab2iai/__init__.py` - Package initialization and exports
- ✅ `skylab2iai/catalog/__init__.py` - Catalog module exports
- ✅ `skylab2iai/catalog/catalog.py` - Main catalog API
- ✅ `skylab2iai/storage/sql_connection.py` - Database connection singleton
- ✅ `skylab2iai/storage/plate_frame.py` - Plate frame storage and queries

## Test Files

### Unit Tests
1. **`test_init.py`** (7 tests)
   - Package version validation
   - Export verification
   - Import functionality

2. **`test_sql_connection.py`** (7 tests)
   - Singleton pattern
   - Database connection initialization
   - Cursor functionality
   - Database schema validation

3. **`test_plate_frame.py`** (14 tests)
   - Singleton pattern
   - CRUD operations
   - SQL injection prevention
   - DELETE/UPDATE/INSERT blocking
   - Custom query execution

4. **`test_catalog.py`** (20 tests)
   - Singleton pattern
   - Repository initialization
   - Query methods
   - FITS download workflows
   - Error handling
   - HTTP error handling
   - Multiple frame downloads
   - Custom query downloads

### Integration Tests
5. **`test_integration.py`** (9 tests)
   - End-to-end workflows
   - Query and retrieve operations
   - Download workflows
   - Data consistency
   - Error handling
   - Read-only database verification

### Configuration
6. **`conftest.py`**
   - Pytest fixtures
   - Singleton reset between tests
   - Test environment setup

## Running Tests

### Quick Start
```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=skylab2iai --cov-report=term-missing
```

### Using Helper Scripts
```bash
# Unix/macOS
./run_tests.sh

# Windows
run_tests.bat
```

### Specific Test Runs
```bash
# Run specific file
pytest test/test_catalog.py

# Run specific class
pytest test/test_catalog.py::TestSkylab2iaiCatalog

# Run specific test
pytest test/test_catalog.py::TestSkylab2iaiCatalog::test_singleton_pattern

# Run with verbose output
pytest -v

# Run with output capture disabled (see print statements)
pytest -s
```

## Coverage Reports

### Terminal Report
```bash
pytest --cov=skylab2iai --cov-report=term-missing
```

### HTML Report
```bash
pytest --cov=skylab2iai --cov-report=html
open htmlcov/index.html  # macOS
start htmlcov/index.html # Windows
```

### XML Report (for CI/CD)
```bash
pytest --cov=skylab2iai --cov-report=xml
```

## Test Categories

### 1. Singleton Pattern Tests
Verify that singleton classes return the same instance:
- `_SqlStorage`
- `_SkylabPlateStorage`
- `Skylab2iaiCatalog`

### 2. Database Tests
- Connection initialization
- Query execution
- Data retrieval
- Schema validation

### 3. Security Tests
- SQL injection prevention
- DELETE operation blocking
- UPDATE operation blocking
- INSERT operation blocking

### 4. API Tests
- All public methods
- Parameter validation
- Return type verification
- Error handling

### 5. Mock Tests
- HTTP requests (using `unittest.mock`)
- File system operations
- Network error scenarios

### 6. Integration Tests
- Complete workflows
- Multi-step operations
- Data consistency
- Cross-module interactions

## Continuous Integration

### GitHub Actions Workflows

#### Test Workflow (`.github/workflows/test.yml`)
- Runs on: push to main/develop, pull requests
- Matrix testing:
  - OS: Ubuntu, macOS, Windows
  - Python: 3.10, 3.11, 3.12
- Generates coverage reports
- Uploads to Codecov

#### Publish Workflow (`.github/workflows/publish.yml`)
- Runs on: PR merge to main
- Auto-bumps version
- Runs tests before publishing
- Publishes to PyPI

## Writing New Tests

### Test Structure
```python
class TestNewFeature:
    """Test suite for new feature."""
    
    def test_basic_functionality(self):
        """Test basic use case."""
        # Arrange
        catalog = Skylab2iaiCatalog()
        
        # Act
        result = catalog.new_method()
        
        # Assert
        assert result is not None
        assert isinstance(result, ExpectedType)
    
    def test_error_handling(self):
        """Test error cases."""
        catalog = Skylab2iaiCatalog()
        
        with pytest.raises(ExpectedException):
            catalog.new_method(invalid_input)
    
    @patch('module.requests.get')
    def test_with_mock(self, mock_get):
        """Test with mocked external dependency."""
        mock_get.return_value = Mock(status_code=200)
        
        catalog = Skylab2iaiCatalog()
        result = catalog.method_using_requests()
        
        assert result is not None
        mock_get.assert_called_once()
```

### Best Practices
1. **One assertion per test** (when possible)
2. **Use descriptive test names**
3. **Follow AAA pattern** (Arrange, Act, Assert)
4. **Mock external dependencies**
5. **Test edge cases and error conditions**
6. **Use fixtures for common setup**
7. **Keep tests independent**
8. **Clean up resources** (use temp directories)

## Test Data

Tests use the real embedded SQLite database (`skylab-data.db`) which contains:
- 6408 plate frames
- Real metadata
- LINK_FTS URLs for FITS downloads

No test data fixtures are needed as the embedded database provides sufficient data for testing.

## Troubleshooting

### Tests Failing Locally
1. Ensure dev dependencies are installed: `pip install -e ".[dev]"`
2. Check Python version: `python --version` (requires >=3.10)
3. Clear pytest cache: `pytest --cache-clear`
4. Verify database exists: `ls src/skylab2iai/storage/skylab-data.db`

### Coverage Not 100%
1. Run with missing lines report: `pytest --cov=skylab2iai --cov-report=term-missing`
2. Check HTML report for details: `pytest --cov=skylab2iai --cov-report=html`
3. Add tests for uncovered lines
4. Ensure all code paths are tested (if/else, try/except)

### Import Errors in Tests
1. Install package in editable mode: `pip install -e .`
2. Check PYTHONPATH includes src directory
3. Verify package structure is correct

## Maintenance

### When Adding New Features
1. Write tests first (TDD approach)
2. Ensure 100% coverage of new code
3. Update this documentation
4. Run full test suite before committing

### When Fixing Bugs
1. Write a test that reproduces the bug
2. Fix the bug
3. Verify test passes
4. Add regression test to prevent recurrence

### Regular Maintenance
- Review and update tests quarterly
- Keep dependencies up to date
- Monitor CI/CD pipeline health
- Update documentation as needed

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
- [unittest.mock documentation](https://docs.python.org/3/library/unittest.mock.html)
- [Test README](test/README.md)

## Contact

For questions about testing:
- Open an issue on GitHub
- Contact: ferrertiago@gmail.com
