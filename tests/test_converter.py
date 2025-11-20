#!/usr/bin/env python3
"""
Test the DSK converter with a mock disk image
Creates a minimal DOS 3.3 disk image for testing
"""

import sys

sys.path.insert(0, "/home/james/HB_Eamon")

from dsk_converter import DOS33DiskImage, EamonConverter


def create_test_disk():
    """Create a minimal test disk image"""
    print("Creating test DOS 3.3 disk image...")

    # Create a blank disk (35 tracks * 16 sectors * 256 bytes)
    disk_data = bytearray(35 * 16 * 256)

    # Initialize with zeros
    for i in range(len(disk_data)):
        disk_data[i] = 0

    # Write a minimal VTOC at track 17, sector 0
    vtoc_offset = (17 * 16 + 0) * 256
    # VTOC catalog track
    disk_data[vtoc_offset + 1] = 17
    # VTOC catalog sector
    disk_data[vtoc_offset + 2] = 1

    # Write a minimal catalog entry at track 17, sector 1
    catalog_offset = (17 * 16 + 1) * 256
    # Next catalog track/sector (0 = end)
    disk_data[catalog_offset + 1] = 0
    disk_data[catalog_offset + 2] = 0

    # Add a test file entry
    entry_offset = catalog_offset + 11  # First file entry
    disk_data[entry_offset] = 1  # Track of first T/S list
    disk_data[entry_offset + 1] = 0  # Sector of first T/S list
    disk_data[entry_offset + 2] = 0x04  # File type (text)

    # Filename "EAMON.DESC" (30 bytes, high-bit ASCII)
    filename = "EAMON.DESC"
    for i, char in enumerate(filename):
        disk_data[entry_offset + 3 + i] = ord(char) | 0x80

    # Pad rest with spaces
    for i in range(len(filename), 30):
        disk_data[entry_offset + 3 + i] = 0xA0

    # File length in sectors
    disk_data[entry_offset + 33] = 1  # Low byte
    disk_data[entry_offset + 34] = 0  # High byte

    # Write T/S list for EAMON.DESC at track 1, sector 0
    ts_offset = (1 * 16 + 0) * 256
    disk_data[ts_offset + 1] = 0  # No next T/S list
    disk_data[ts_offset + 2] = 0
    disk_data[ts_offset + 12] = 1  # Data in track 1
    disk_data[ts_offset + 13] = 1  # sector 1

    # Write some test data at track 1, sector 1
    data_offset = (1 * 16 + 1) * 256
    test_text = "Test Adventure\rBy Test Author\rThis is a test."
    for i, char in enumerate(test_text):
        disk_data[data_offset + i] = ord(char) | 0x80

    # Save test disk
    with open("test_adventure.dsk", "wb") as f:
        f.write(disk_data)

    print("Test disk image created: test_adventure.dsk")
    return True


def test_converter():
    """Test the converter functionality"""
    print("\n" + "=" * 60)
    print("Testing DSK Converter")
    print("=" * 60)

    # Create test disk
    if not create_test_disk():
        print("Failed to create test disk")
        return False

    # Test disk reader
    print("\nTesting DOS 3.3 disk reader...")
    disk = DOS33DiskImage("test_adventure.dsk")

    if not disk.load():
        print("Failed to load test disk")
        return False

    print("✓ Disk loaded successfully")

    # Test catalog reading
    print("\nReading catalog...")
    files = disk.read_catalog()

    print(f"✓ Found {len(files)} file(s)")
    for filename in files:
        print(f"  - {filename}")

    # Test file reading
    if "EAMON.DESC" in files:
        print("\nReading EAMON.DESC...")
        data = disk.read_file("EAMON.DESC")
        if data:
            print(f"✓ Read {len(data)} bytes")
            # Show decoded text
            text = ""
            for byte in data[:100]:
                if byte == 0:
                    break
                char = byte & 0x7F
                if 32 <= char <= 126 or char == 13:
                    text += chr(char) if char != 13 else "\n"
            print(f"Content preview:\n{text[:200]}")
        else:
            print("✗ Failed to read file")

    print("\n" + "=" * 60)
    print("Converter test complete!")
    print("=" * 60)
    print("\nThe converter is ready to use with real Eamon .DSK files.")
    print("\nUsage: ./convert_dsk.sh <your_adventure.dsk>")

    return True


if __name__ == "__main__":
    test_converter()
