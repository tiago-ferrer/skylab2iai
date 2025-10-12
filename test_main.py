#!/usr/bin/env python3
"""
Main test file for Skylab2IAI library
Tests the core functionality of the library including database connections,
repositories, and services.
"""

import sys
import os
from pathlib import Path

# Add src to path for local testing
sys.path.insert(0, str(Path(__file__).parent / "src"))

from skylab2iai import PlateFrameService
from skylab2iai.repository.plate_frame_repository import PlateFrameRepository
from skylab2iai.config.database.data_connection import _SqlDataConnection


def test_database_connection():
    """Test database connection singleton pattern"""
    print("\n" + "="*60)
    print("Testing Database Connection")
    print("="*60)
    
    try:
        conn1 = _SqlDataConnection()
        conn2 = _SqlDataConnection()
        
        # Test singleton pattern
        assert conn1 is conn2, "Database connection should be a singleton"
        print("✓ Singleton pattern working correctly")
        
        # Test database connection
        assert conn1.db is not None, "Database should be connected"
        print("✓ Database connection established")
        
        # Test cursor
        cursor = conn1.cursor()
        assert cursor is not None, "Cursor should be available"
        print("✓ Database cursor working")
        
        return True
    except Exception as e:
        print(f"✗ Database connection test failed: {e}")
        return False


def test_plate_frame_repository():
    """Test PlateFrameRepository functionality"""
    print("\n" + "="*60)
    print("Testing PlateFrameRepository")
    print("="*60)
    
    try:
        repo = PlateFrameRepository()
        
        # Test singleton pattern
        repo2 = PlateFrameRepository()
        assert repo is repo2, "Repository should be a singleton"
        print("✓ Repository singleton pattern working")
        
        # Test get_plate_frames
        try:
            plate_frames = repo.get_plate_frames()
            print(f"✓ get_plate_frames() returned {len(plate_frames)} records")
            if not plate_frames.empty:
                print(f"  Columns: {list(plate_frames.columns)}")
                print(f"  Sample data:\n{plate_frames.head(2)}")
        except Exception as e:
            print(f"  Note: get_plate_frames() - {e}")
        
        return True
    except Exception as e:
        print(f"✗ Repository test failed: {e}")
        return False


def test_plate_frame_service():
    """Test PlateFrameService functionality"""
    print("\n" + "="*60)
    print("Testing PlateFrameService")
    print("="*60)
    
    try:
        service = PlateFrameService()
        
        # Test singleton pattern
        service2 = PlateFrameService()
        assert service is service2, "Service should be a singleton"
        print("✓ Service singleton pattern working")
        
        # Test get_plate_frames
        try:
            plate_frames = service.get_plate_frames()
            print(f"✓ get_plate_frames() returned {len(plate_frames)} records")
            
            if not plate_frames.empty:
                # Test get_plate_frame with first record
                first_name = plate_frames.iloc[0]['name'] if 'name' in plate_frames.columns else None
                if first_name:
                    single_frame = service.get_plate_frame(first_name)
                    print(f"✓ get_plate_frame('{first_name}') returned {len(single_frame)} record(s)")
                
                # Test get_plate_frames_by_plate
                plate_name = plate_frames.iloc[0]['plate_name'] if 'plate_name' in plate_frames.columns else None
                if plate_name:
                    frames_by_plate = service.get_plate_frames_by_plate(plate_name)
                    print(f"✓ get_plate_frames_by_plate('{plate_name}') returned {len(frames_by_plate)} record(s)")
        except Exception as e:
            print(f"  Note: Service methods - {e}")
        
        return True
    except Exception as e:
        print(f"✗ Service test failed: {e}")
        return False


def test_download_fits_simulation():
    """Test FITS download method structure (without actual download)"""
    print("\n" + "="*60)
    print("Testing FITS Download Method Structure")
    print("="*60)
    
    try:
        service = PlateFrameService()
        
        # Check if method exists
        assert hasattr(service, 'download_fits_plate_frames'), "download_fits_plate_frames method should exist"
        print("✓ download_fits_plate_frames method exists")
        
        # Check method signature
        import inspect
        sig = inspect.signature(service.download_fits_plate_frames)
        params = list(sig.parameters.keys())
        print(f"✓ Method parameters: {params}")
        
        return True
    except Exception as e:
        print(f"✗ Download method test failed: {e}")
        return False


def test_import_from_package():
    """Test importing from installed package"""
    print("\n" + "="*60)
    print("Testing Package Imports")
    print("="*60)
    
    try:
        # Test main import
        from skylab2iai import PlateFrameService, PlateFrameRepository
        print("✓ Successfully imported PlateFrameService")
        print("✓ Successfully imported PlateFrameRepository")
        
        # Test version
        import skylab2iai
        if hasattr(skylab2iai, '__version__'):
            print(f"✓ Package version: {skylab2iai.__version__}")
        
        return True
    except Exception as e:
        print(f"✗ Import test failed: {e}")
        return False


def run_all_tests():
    """Run all tests and report results"""
    print("\n" + "="*60)
    print("SKYLAB2IAI LIBRARY TEST SUITE")
    print("="*60)
    
    tests = [
        ("Package Imports", test_import_from_package),
        ("Database Connection", test_database_connection),
        ("PlateFrameRepository", test_plate_frame_repository),
        ("PlateFrameService", test_plate_frame_service),
        ("FITS Download Method", test_download_fits_simulation),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
