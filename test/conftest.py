"""Pytest configuration and fixtures."""
import pytest

from skylab2iai import Skylab2iaiCatalog
from skylab2iai.storage.plate import _SkylabPlateStorage
from skylab2iai.storage.sql_connection import _SqlStorage


@pytest.fixture(autouse=True)
def reset_singletons():
    """Reset all singleton instances before each test."""

    # Store original instances
    original_sql = _SqlStorage._instance
    original_plate = _SkylabPlateStorage._instance
    original_catalog = Skylab2iaiCatalog._instance
    
    # Reset for test
    _SqlStorage._instance = None
    _SkylabPlateStorage._instance = None
    Skylab2iaiCatalog._instance = None
    
    yield
    
    # Restore after test (optional, but good practice)
    _SqlStorage._instance = original_sql
    _SkylabPlateStorage._instance = original_plate
    Skylab2iaiCatalog._instance = original_catalog
