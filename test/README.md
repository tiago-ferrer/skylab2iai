# Test Suite for Skylab2IAI

This directory contains comprehensive tests for the Skylab2IAI library.

## Setup

Install the package with development dependencies:

```bash
pip install -e ".[dev]"
```

Or install test dependencies manually:

```bash
pip install pytest pytest-cov pytest-mock
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run with coverage report
```bash
pytest --cov=skylab2iai --cov-report=term-missing
```

### Run specific test file
```bash
pytest test/test_catalog.py
```

### Run specific test class
```bash
pytest test/test_catalog.py::TestSkylab2iaiCatalog
```

### Run specific test method
```bash
pytest test/test_catalog.py::TestSkylab2iaiCatalog::test_singleton_pattern
```

### Generate HTML coverage report
```bash
pytest --cov=skylab2iai --cov-report=html
# Open htmlcov/index.html in browser
```

## Test Structure

- **`test_init.py`**: Tests for package initialization and exports
- **`test_sql_connection.py`**: Tests for SQL connection singleton
- **`test_plate_frame.py`**: Tests for plate frame storage and queries
- **`test_catalog.py`**: Tests for main catalog API
- **`test_integration.py`**: End-to-end integration tests
- **`conftest.py`**: Pytest configuration and fixtures

## Coverage Goals

The test suite aims for 100% code coverage across all modules:

- ✅ `skylab2iai/__init__.py`
- ✅ `skylab2iai/catalog/__init__.py`
- ✅ `skylab2iai/catalog/catalog.py`
- ✅ `skylab2iai/storage/sql_connection.py`
- ✅ `skylab2iai/storage/plate_frame.py`

## Test Categories

### Unit Tests
- Singleton pattern implementation
- Database connection management
- Query methods
- SQL injection prevention
- Error handling

### Integration Tests
- Complete workflows
- Data consistency
- Multi-instance behavior
- Download workflows (mocked)

### Mock Tests
- HTTP requests for FITS downloads
- File system operations
- Network error handling

## Continuous Integration

Tests are automatically run on:
- Pull requests
- Commits to main branch
- Before PyPI publication

## Writing New Tests

When adding new features:

1. Add unit tests in the appropriate test file
2. Add integration tests if the feature involves multiple components
3. Ensure all edge cases are covered
4. Mock external dependencies (HTTP, file system)
5. Run coverage report to verify 100% coverage

Example test structure:

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
    
    def test_error_handling(self):
        """Test error cases."""
        catalog = Skylab2iaiCatalog()
        
        with pytest.raises(ExpectedException):
            catalog.new_method(invalid_input)
```

## Notes

- All tests use the real embedded SQLite database
- Singleton instances are reset between tests via `conftest.py`
- HTTP requests are mocked to avoid external dependencies
- Temporary directories are used for file operations
