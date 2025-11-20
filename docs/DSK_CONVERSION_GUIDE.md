# Converting Original Eamon Adventures

This guide explains how to convert original Apple II Eamon disk images (.DSK files) to JSON format for use with the Linux Eamon engine.

## Quick Start

```bash
./convert_dsk.sh your_adventure.dsk
```

The converted adventure will be saved to `adventures/your_adventure.json` and can be played immediately.

## What the Converter Does

The converter:
1. **Reads Apple II DOS 3.3 disk images** (.dsk, .do formats)
2. **Extracts the DOS 3.3 catalog** to find Eamon data files
3. **Parses Eamon data files**:
   - `EAMON.DESC` - Adventure title, author, intro text
   - `EAMON.ROOM` - Room definitions and connections
   - `EAMON.ARTIFACT` - Items and treasures
   - `EAMON.MONSTER` - NPCs and monsters
   - `EAMON.EFFECT` - Special effects (optional)
4. **Converts to JSON format** compatible with the Linux engine
5. **Saves the playable adventure** to the adventures directory

## Usage

### Basic Conversion

```bash
# Convert a disk image (auto-generates output filename)
./convert_dsk.sh adventure.dsk

# Convert with custom output name
./convert_dsk.sh adventure.dsk my_adventure.json

# Using Python directly
python3 dsk_converter.py adventure.dsk adventures/output.json
```

### Playing Converted Adventures

```bash
# After conversion, play the adventure
./play_adventure.sh your_adventure.json

# Or use the menu system
./play_eamon.sh
```

## Where to Get Eamon .DSK Files

Original Eamon adventures can be found at:

1. **Eamon Adventurer's Guild Online**
   - Website: http://www.eamonag.org/
   - Contains 250+ adventures in .dsk format
   
2. **Internet Archive**
   - Search for "Eamon" in Apple II collections
   
3. **Asimov FTP Archive**
   - Classic Apple II software repository

## Supported Disk Formats

- **.dsk** - Standard DOS 3.3 disk image (140KB)
- **.do** - DOS-ordered disk image
- **140KB files** - Standard Apple II disk size

## Understanding Eamon Data Format

### Original Apple II Format

Eamon adventures on Apple II store data in separate files:

```
EAMON.DESC      - Adventure description and intro
EAMON.ROOM      - Room database (locations, exits, descriptions)
EAMON.ARTIFACT  - Item database (weapons, treasures, objects)
EAMON.MONSTER   - NPC/Monster database (enemies, allies)
EAMON.EFFECT    - Special effects and events
```

### Converted JSON Format

The converter transforms this into a single JSON file:

```json
{
  "title": "Adventure Name",
  "author": "Author Name",
  "intro": "Introduction text...",
  "start_room": 1,
  "rooms": [...],
  "items": [...],
  "monsters": [...],
  "effects": [...]
}
```

## Conversion Limitations

### What Works Well
✅ Room extraction (names, descriptions, exits)
✅ Item extraction (basic properties)
✅ Monster extraction (stats, locations)
✅ Adventure metadata (title, author)

### What May Need Manual Editing
⚠️ **Text formatting** - Some descriptions may need cleanup
⚠️ **Special effects** - Complex BASIC code effects won't convert automatically
⚠️ **Embedded logic** - Custom adventure code needs manual porting
⚠️ **Graphics/sounds** - Not supported in text-only engine

### Known Issues
- Some disk images use non-standard formats
- Corrupted sectors may cause incomplete data
- Very old Eamon versions may have different file structures
- Custom modifications to Eamon may not parse correctly

## Post-Conversion Editing

After conversion, you may want to manually edit the JSON to:

1. **Clean up text** - Fix garbled characters or formatting
2. **Add missing data** - Fill in incomplete descriptions
3. **Balance gameplay** - Adjust difficulty, item values, monster stats
4. **Enhance descriptions** - Expand room/item descriptions
5. **Fix connections** - Correct any broken room exits

Example manual edit:

```bash
# Edit the converted adventure
nano adventures/your_adventure.json

# Test your edits
./play_adventure.sh your_adventure.json
```

## Troubleshooting

### "Error: File not found"
- Check the .dsk file path
- Ensure the file has .dsk or .do extension

### "Failed to load disk image"
- File may be corrupted
- Try re-downloading the disk image
- Check file size (should be ~140KB)

### "No files found on disk"
- Disk may use non-standard format
- Try a different disk image source
- May need ProDOS format support (not yet implemented)

### "Found 0 rooms/items/monsters"
- Data files may be missing from disk
- Adventure may use non-standard file names
- Try manual extraction with an Apple II emulator

### Conversion produces incomplete data
- Some adventures have minimal data
- Use an emulator to verify disk contents
- May need to manually create missing content

## Manual Extraction Alternative

If the converter doesn't work for a specific disk:

1. **Use an Apple II emulator** (AppleWin, linapple)
2. **Boot the disk image**
3. **List the files**: `CATALOG`
4. **Examine the data files** in BASIC
5. **Manually transcribe** to JSON format
6. Use an existing JSON adventure as a template

## Advanced: Handling Special Cases

### ProDOS Disk Images
Currently not supported. The converter only handles DOS 3.3 format.

```bash
# Convert ProDOS to DOS 3.3 using CiderPress or similar tools first
```

### Compressed Disk Images
Decompress first:

```bash
# .DSK.gz files
gunzip adventure.dsk.gz

# .zip files
unzip adventure.zip
```

### Multiple Disk Adventures
Some large adventures span multiple disks. Convert each disk separately and merge the JSON files manually.

## Testing Converted Adventures

Always test converted adventures before distributing:

```bash
# Run the adventure
./play_adventure.sh converted_adventure.json

# Check for:
# - All rooms accessible
# - Items in correct locations  
# - Monsters behave correctly
# - Exits work properly
# - No crashes or errors
```

## Example: Converting "The Beginner's Cave"

```bash
# 1. Download the disk image
wget http://www.eamonag.org/adventures/cave.dsk

# 2. Convert it
./convert_dsk.sh cave.dsk beginners_cave.json

# 3. Play it
./play_adventure.sh beginners_cave.json

# 4. If needed, edit the JSON
nano adventures/beginners_cave.json
```

## Batch Conversion

To convert multiple adventures:

```bash
#!/bin/bash
# Convert all .dsk files in a directory

for dsk in *.dsk; do
    echo "Converting $dsk..."
    ./convert_dsk.sh "$dsk"
done

echo "All conversions complete!"
echo "Adventures saved to adventures/ directory"
```

## Contributing Converted Adventures

If you successfully convert classic Eamon adventures:

1. Test thoroughly
2. Clean up any conversion issues
3. Add proper attribution (original author)
4. Share the JSON files with the community

## Technical Details

### DOS 3.3 Disk Structure
- 35 tracks
- 16 sectors per track
- 256 bytes per sector
- VTOC at track 17, sector 0
- Catalog starts at track 17, sector 1

### File Extraction Process
1. Read VTOC to find catalog location
2. Parse catalog sectors to get file listings
3. Follow track/sector lists to read file data
4. Decode high-bit ASCII text
5. Parse Eamon database records
6. Convert to JSON structure

## Resources

- **Eamon Adventurer's Guild**: http://www.eamonag.org/
- **Eamon Wiki**: Documentation on adventure format
- **DOS 3.3 Documentation**: For disk format details
- **AppleWin Emulator**: For testing original adventures

## Getting Help

If conversion fails:
1. Check this documentation
2. Verify disk image integrity
3. Try an Apple II emulator to inspect the disk
4. Create a manual JSON adventure based on templates
5. Report issues with specific disk images

---

**Note**: This converter is a best-effort tool. Due to the age and variety of Eamon adventures, some manual editing may be required for perfect conversion.
