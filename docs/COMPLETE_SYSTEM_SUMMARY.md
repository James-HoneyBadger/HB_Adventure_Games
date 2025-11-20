# Eamon Adventures - Complete System Summary

## System Overview

This is a complete recreation of the classic Eamon (Exciting Adventure Master's Organization) text adventure system for Linux, featuring a modern Python implementation, graphical IDE, and compatibility tools for importing original Apple II adventures.

## What's Included

### Core Game Engine
- **File**: `eamon_engine.py` (550 lines)
- **Features**:
  - Full text parser for natural language commands
  - Dice-based combat system with weapons and armor
  - Room navigation with 6-direction movement
  - Inventory management
  - NPC/monster interaction system
  - JSON-based adventure loading
  - Save/restore game state

### Graphical IDE
- **File**: `eamon_ide.py` (~1000 lines)
- **Launch**: `./launch_ide.sh`
- **Features**:
  - Visual adventure editor with tabbed interface
  - Real-time editing of rooms, items, monsters
  - Built-in game testing (F5 key)
  - DSK file import integration
  - Validation tools
  - JSON preview and export
  - Keyboard shortcuts (Ctrl+N/O/S)
  - Menu system for all operations

### DSK Converter
- **File**: `dsk_converter.py` (600 lines)
- **Launch**: `./convert_dsk.sh adventure.dsk`
- **Features**:
  - Reads DOS 3.3 disk images (.dsk, .do)
  - Parses Apple II file system (35 tracks, 16 sectors)
  - Extracts Eamon data files (DESC, ROOM, ARTIFACT, MONSTER)
  - Converts binary data to JSON format
  - Preserves original adventure content
  - Handles multiple disk formats

### Adventure Launcher
- **File**: `eamon_launcher.py` (130 lines)
- **Launch**: `./play_eamon.sh`
- **Features**:
  - Menu-based adventure selection
  - Auto-discovery of adventures
  - Adventure metadata display
  - Easy launch interface

### Included Adventures
1. **The Beginner's Cave** (beginners_cave.json)
   - 9 rooms, 8 items, 4 monsters
   - Classic introductory adventure
   - Good for learning the system

2. **The Lair of Mutants** (lair_of_mutants.json)
   - 9 rooms, 9 items, 5 monsters
   - Medium difficulty
   - Laboratory horror theme

## Directory Structure

```
HB_Eamon/
├── eamon_engine.py              # Core game engine
├── eamon_launcher.py            # Adventure menu system
├── eamon_ide.py                 # Graphical IDE
├── dsk_converter.py             # DSK file converter
├── test_engine.py               # Engine test suite
├── test_converter.py            # Converter test suite
│
├── launch_ide.sh                # IDE launcher
├── play_eamon.sh                # Menu launcher
├── play_adventure.sh            # Direct adventure launcher
├── convert_dsk.sh               # DSK conversion script
├── list_adventures.sh           # List available adventures
├── verify_installation.sh       # System verification
├── demo.sh                      # Complete demonstration
│
├── README.md                    # Main documentation
├── IDE_GUIDE.md                 # GUI IDE user guide
├── DSK_CONVERSION_GUIDE.md      # Import guide
├── QUICKSTART.md                # Quick start guide
├── EXAMPLE_GAMEPLAY.md          # Sample game session
├── PROJECT_SUMMARY.md           # Technical overview
├── INDEX.md                     # File navigation
├── START_HERE.txt               # 60-second quickstart
├── DSK_CONVERTER_QUICKREF.txt   # Conversion reference
│
└── adventures/
    ├── beginners_cave.json      # Starter adventure
    └── lair_of_mutants.json     # Medium adventure
```

## Quick Start Guide

### 1. Install (One-Time Setup)

```bash
cd /home/james/HB_Eamon
chmod +x *.sh
```

### 2. Play Adventures

**Option A: Use Menu**
```bash
./play_eamon.sh
```

**Option B: Direct Play**
```bash
./play_adventure.sh beginners_cave.json
```

### 3. Create Adventures

**Option A: Use GUI IDE (Recommended)**
```bash
./launch_ide.sh
```

**Option B: Edit JSON**
- See examples in adventures/ directory
- Copy and modify existing adventures

### 4. Import Original Adventures

```bash
./convert_dsk.sh original_adventure.dsk
./play_adventure.sh original_adventure.json
```

## System Requirements

- **Python**: 3.6 or higher
- **OS**: Linux (tested), macOS, Windows (with WSL)
- **For IDE**: python3-tk/tkinter package
- **Disk space**: ~1 MB for system, varies for adventures

## Key Commands

### In Game
- `n/s/e/w/u/d` - Movement
- `look` - Examine room
- `get/drop item` - Inventory management
- `attack monster` - Combat
- `inventory` - Show items
- `status` - Character stats
- `help` - Show commands
- `quit` - Exit

### In IDE
- `Ctrl+N` - New adventure
- `Ctrl+O` - Open adventure
- `Ctrl+S` - Save adventure
- `F5` - Test adventure

## Technical Details

### Game Engine Architecture
- **Class**: `EamonGame`
- **Adventure format**: JSON
- **Data structures**: Rooms, items, monsters with properties
- **Combat**: Dice-based (d4, d6, d8, d20)
- **Parser**: Command + target word extraction
- **State**: Inventory, location, monster status

### IDE Architecture
- **Framework**: tkinter (cross-platform GUI)
- **Design**: Tabbed interface with 5 tabs
- **Tabs**: Info, Rooms, Items, Monsters, Preview
- **Editors**: List-based selection with property forms
- **Integration**: Calls game engine for testing

### Converter Architecture
- **Disk parser**: DOS 3.3 filesystem reader
- **Sector layout**: 35 tracks × 16 sectors × 256 bytes
- **Data extraction**: Binary struct unpacking
- **File types**: Eamon DESC, ROOM, ARTIFACT, MONSTER
- **Output**: JSON matching game engine format

## Features Comparison

| Feature | Original Eamon | This System |
|---------|---------------|-------------|
| Platform | Apple II | Linux/Modern OS |
| Language | Applesoft BASIC | Python 3 |
| Data format | Binary files | JSON |
| Editor | Line-based BASIC | GUI IDE |
| Combat | Dice-based | Same system |
| Adventures | 250+ available | Compatible via converter |
| Extensibility | BASIC programming | Python + JSON |

## Workflows

### Creating an Adventure from Scratch

1. Launch IDE: `./launch_ide.sh`
2. File → New Adventure
3. Fill in adventure info (title, author, intro)
4. Create rooms with descriptions and exits
5. Add items (weapons, treasures, keys)
6. Add monsters (enemies, NPCs)
7. Press F5 to test
8. Save with Ctrl+S
9. Play: `./play_adventure.sh your_adventure.json`

### Converting an Original Adventure

1. Download .DSK file from eamonag.org
2. Convert: `./convert_dsk.sh adventure.dsk`
3. (Optional) Edit in IDE: `./launch_ide.sh`
4. Test: `./play_adventure.sh adventure.json`
5. Refine as needed

### Testing and Validation

1. **In IDE**: Tools → Validate Adventure
2. **Command line**: `python3 -m json.tool adventures/file.json`
3. **Play test**: Press F5 in IDE or use play script
4. **Check logs**: Terminal output shows errors

## Performance Characteristics

- **Load time**: <1 second for typical adventure
- **Memory**: ~10-20 MB for game engine
- **Disk I/O**: Minimal (reads JSON on load)
- **Conversion time**: 1-2 seconds for .DSK file
- **IDE startup**: 1-2 seconds

## Known Limitations

### Game Engine
- No multiplayer support (original was single-player)
- Basic combat AI (monsters attack/flee based on courage)
- Simple text parser (2-word commands)
- No graphics (text-only, as per original)

### DSK Converter
- Requires valid DOS 3.3 disk images
- Some custom adventures may need manual edits
- Non-standard Eamon formats not supported
- Disk errors may prevent reading

### IDE
- Requires tkinter (separate install on some systems)
- Large adventures (100+ rooms) may be slow to edit
- No undo/redo yet
- Single-window interface

## Future Enhancement Ideas

- Multi-adventure campaigns
- Character persistence across adventures
- Enhanced combat system
- Sound effects
- More sophisticated AI
- Multiplayer networking
- Web-based version
- Mobile ports

## Troubleshooting

### IDE Won't Launch
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

### Converter Fails
- Check .DSK file is valid DOS 3.3 format
- Try with known-good file first
- Check file size (should be ~140KB)

### Game Crashes
- Validate JSON: `python3 -m json.tool file.json`
- Check room IDs are valid
- Verify start_room exists

## Getting Help

1. **Documentation**: Check README.md, IDE_GUIDE.md, DSK_CONVERSION_GUIDE.md
2. **Examples**: Study included adventures
3. **Testing**: Use validation tools and test suite
4. **Community**: Eamon Adventurer's Guild (eamonag.org)

## Resources

- **Original Eamon**: http://www.eamonag.org/ (250+ adventures)
- **Apple II DSK files**: Internet Archive, Apple II repositories
- **Python docs**: https://docs.python.org/3/
- **tkinter guide**: https://docs.python.org/3/library/tkinter.html

## Version Information

- **System version**: 1.0 Complete
- **Engine version**: 1.0
- **Converter version**: 1.0
- **IDE version**: 1.0
- **Python required**: 3.6+
- **Last updated**: 2024

## Credits

- **Original Eamon**: Donald Brown (1980)
- **Linux Port**: HB_Eamon Project (2024)
- **Engine**: Pure Python 3 implementation
- **Adventures**: Various authors (credited in files)

## File Sizes

- eamon_engine.py: ~25 KB
- eamon_ide.py: ~40 KB
- dsk_converter.py: ~30 KB
- eamon_launcher.py: ~6 KB
- Documentation: ~100 KB total
- Adventures: ~10-30 KB each

Total system size: ~250 KB (excluding adventures)

## Testing Status

✅ Game engine: Fully tested, working
✅ Adventure launcher: Tested, functional
✅ DSK converter: Tested with sample files
✅ IDE: Launched successfully, ready for use
✅ Scripts: All executable and working
✅ Documentation: Complete and comprehensive

## Success Metrics

This system successfully provides:
- ✅ Complete Linux-compatible Eamon implementation
- ✅ No emulator required
- ✅ Modern development tools (IDE)
- ✅ Original adventure compatibility (via converter)
- ✅ Easy adventure creation
- ✅ Comprehensive documentation
- ✅ Working examples
- ✅ Test suites

## Next Steps for Users

1. **New players**: Run `./play_eamon.sh` and try Beginner's Cave
2. **Adventure creators**: Run `./launch_ide.sh` and create your first adventure
3. **Classic fans**: Download .DSK files and use `./convert_dsk.sh` to import them
4. **Developers**: Read the source code and extend the system

---

**System Status: COMPLETE AND READY TO USE**

All components are implemented, tested, and documented. The system is fully functional and ready for playing, creating, and importing Eamon adventures on Linux and other modern operating systems.
