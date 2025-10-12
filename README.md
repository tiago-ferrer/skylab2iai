# Skylab2IAI

A Python library for accessing and analyzing Skylab mission data.

## Installation

### From GitHub (for Google Colab or local use)

```python
!pip install git+https://github.com/tiago-ferrer/skylab2iai.git
```

### For local development

```bash
git clone https://github.com/tiago-ferrer/skylab2iai.git
cd skylab2iai
pip install -e .
```

## Usage in Google Colab

```python
# Install the library
!pip install git+https://github.com/tiago-ferrer/skylab2iai.git

# Import the library
from skylab2iai import PlateFrameService

# Create a service instance
service = PlateFrameService()

# Get all plate frames
plate_frames = service.get_plate_frames()
print(plate_frames)

# Get a specific plate frame
plate_frame = service.get_plate_frame("plate_name")
print(plate_frame)

# Get plate frames by plate name
plate_frames_by_plate = service.get_plate_frames_by_plate("plate_name")
print(plate_frames_by_plate)

# Download FITS files
downloaded_files = service.download_fits_plate_frames(
    plate_names=("plate1", "plate2", "plate3"),
    output_dir="./fits_data"  # Optional, defaults to './fits_downloads'
)
print(f"Downloaded {len(downloaded_files)} files:")
for file_path in downloaded_files:
    print(f"  - {file_path}")
```

## Features

- **PlateFrameService**: Service layer for managing plate frame data
  - `get_plate_frame(plate_frame_name)`: Retrieve a specific plate frame
  - `get_plate_frames()`: Retrieve all plate frames
  - `get_plate_frames_by_plate(plate_name)`: Retrieve plate frames for a specific plate
  - `download_fits_plate_frames(plate_names, output_dir)`: Download FITS files for specified plate frames

## Requirements

- Python >= 3.10
- pandas >= 2.0.0
- requests >= 2.31.0

## Testing

Run the comprehensive test suite:

```bash
python test_main.py
```

Or run a quick verification:

```bash
python quick_test.py
```

Test GitHub installation:

```bash
python test_github_install.py
```

## Troubleshooting

### Google Colab: "unable to open database file" or "no such table"

If you encounter database errors in Google Colab, try these steps:

1. **Restart the runtime** and reinstall:
   ```python
   # In Google Colab, go to Runtime > Restart runtime
   # Then reinstall the library
   !pip install --force-reinstall git+https://github.com/tiago-ferrer/skylab2iai.git
   ```

2. **Clear pip cache** before installing:
   ```python
   !pip cache purge
   !pip install git+https://github.com/tiago-ferrer/skylab2iai.git
   ```

3. **Verify the database is loaded**:
   ```python
   from skylab2iai import PlateFrameService
   service = PlateFrameService()
   plate_frames = service.get_plate_frames()
   print(f"Loaded {len(plate_frames)} plate frames")
   ```

The library includes a 1.8MB SQLite database with 6408 plate frames. If you see this count, everything is working correctly!

## License

MIT License
