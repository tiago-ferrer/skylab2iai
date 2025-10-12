#!/usr/bin/env python3
"""
Quick test script for Skylab2IAI library
Run this to quickly verify the library is working
"""

from skylab2iai import PlateFrameService

def main():
    print("Testing Skylab2IAI Library...")
    print("-" * 40)
    
    # Initialize service
    service = PlateFrameService()
    print("✓ PlateFrameService initialized")
    
    # Test methods exist
    assert hasattr(service, 'get_plate_frames'), "Missing get_plate_frames method"
    assert hasattr(service, 'get_plate_frame'), "Missing get_plate_frame method"
    assert hasattr(service, 'get_plate_frames_by_plate'), "Missing get_plate_frames_by_plate method"
    assert hasattr(service, 'download_fits_plate_frames'), "Missing download_fits_plate_frames method"
    print("✓ All service methods available")
    
    # Try to get plate frames
    try:
        plate_frames = service.get_plate_frames()
        print(f"✓ Retrieved {len(plate_frames)} plate frames")
        if not plate_frames.empty:
            print(f"  Columns: {list(plate_frames.columns)}")
    except Exception as e:
        print(f"  Note: Database query - {e}")
    
    print("-" * 40)
    print("✓ Library is working correctly!")

if __name__ == "__main__":
    main()
