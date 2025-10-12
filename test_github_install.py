#!/usr/bin/env python3
"""
Test script to verify the library works after installing from GitHub.
This simulates what happens in Google Colab.
"""

import sys

def test_github_install():
    """Test that the library works after GitHub installation"""
    print("Testing Skylab2IAI after GitHub installation...")
    print("=" * 60)
    
    try:
        # Import the library
        from skylab2iai import PlateFrameService
        print("✓ Successfully imported PlateFrameService")
        
        # Initialize service (this will test database connection)
        service = PlateFrameService()
        print("✓ PlateFrameService initialized successfully")
        
        # Try to get plate frames (this will test database access)
        plate_frames = service.get_plate_frames()
        print(f"✓ Retrieved {len(plate_frames)} plate frames from database")
        
        if not plate_frames.empty:
            print(f"✓ Database columns: {list(plate_frames.columns)}")
            print(f"✓ Sample record: {plate_frames.iloc[0]['NAME']}")
        
        print("=" * 60)
        print("✅ All tests passed! Library is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_github_install()
    sys.exit(0 if success else 1)
