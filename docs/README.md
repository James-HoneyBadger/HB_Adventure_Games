# Adventure Construction Set

A Python-based text adventure creation system with full backward compatibility with the classic **Eamon** format and Apple II DSK files.

## 🎉 NEW: 10 Major Enhancements Complete!

The Adventure Construction Set now includes **10 comprehensive enhancement systems** that transform it into a modern, feature-rich game development platform:

1. **NPC Memory & Context** - NPCs with emotions, relationships, and conversation memory
2. **Advanced Party Commands** - AI stances, waiting mechanics, sophisticated party management
3. **Environmental Storytelling** - Dynamic time/weather, hidden objects, ambient descriptions
4. **Smart Command Prediction** - Typo correction, history, context-aware suggestions
5. **Enhanced Combat System** - Tactical positioning, status effects, intelligent enemy AI
6. **Achievement & Statistics** - 40+ stats tracked, 12+ achievements with 6 categories
7. **Journal & Note-Taking** - Auto-logging, manual notes, quest hints, search
8. **Tutorial & Contextual Help** - Progressive discovery, adaptive learning
9. **Modding & Scripting Support** - Python scripts, event hooks, custom commands
10. **Accessibility Features** - 5 difficulty levels, screen reader support, color schemes

**Total:** 3,205 lines of new functionality across 10 modules, all with 100% backward compatibility!

See [IMPLEMENTATION_COMPLETE.md](IMPLEMENTATION_COMPLETE.md) for full details.

## Overview

Adventure Construction Set is a modern system for creating and playing text-based adventure games. It provides both classic gameplay mechanics and powerful new features, while maintaining 100% compatibility with the original Eamon adventure format from 1980.

This project brings classic adventure gaming to modern systems with:
- Pure Python implementation (no emulator needed)
- Classic Eamon-compatible gameplay mechanics
- Easy-to-create adventures using JSON format
- Multiple included adventures showcasing features
- **Converter to import original Apple II Eamon .DSK disk images**
- **Full graphical IDE for creating and editing adventures**
- **Play adventures directly in the IDE** - test without leaving the editor!
- **Enhanced features**: puzzles, quests, dialogue, equipment, character progression
- **Backward compatible** - all original Eamon adventures work unchanged

## What is Eamon?

Eamon (Exciting Adventure Master's Organization) was a pioneering text adventure system created by Donald Brown in 1980 for the Apple II. This system maintains full compatibility with the original format while adding modern enhancements.

## Installation

### Requirements
- Python 3.6 or higher
- Linux, macOS, or Windows (with WSL or native Python)

### Quick Start

1. Clone or download this repository
2. Navigate to the directory:
   ```bash
   cd HB_Eamon
   ```
3. Make scripts executable (Linux/macOS):
   ```bash
   chmod +x *.sh
   ```

## How to Play

### Method 1: Main Menu (Recommended)

Launch the main menu to see all available adventures:

```bash
./play_eamon.sh
```

Or directly with Python:

```bash
python3 eamon_launcher.py
```

### Method 2: Direct Play

Play a specific adventure directly:

```bash
./play_adventure.sh beginners_cave.json
```

Or with Python:

```bash
python3 eamon_engine.py adventures/beginners_cave.json
```

## Game Commands

### Movement
- `n, north` - Go north
- `s, south` - Go south  
- `e, east` - Go east
- `w, west` - Go west
- `u, up` - Go up
- `d, down` - Go down

### Actions
- `look` or `l` - Look around the current room
- `get <item>` or `take <item>` - Pick up an item
- `drop <item>` - Drop an item from inventory
- `attack <monster>` - Attack a monster/NPC
- `inventory` or `i` - Show your inventory
- `status` - Show your character stats

### Other
- `help` or `?` - Show help
- `quit` or `q` - Exit the game

## Included Adventures

### 1. The Beginner's Cave
*by Donald Brown*

A classic introductory adventure perfect for new players. Explore a mysterious cave, fight monsters, and find treasure. Great for learning the game mechanics.

**Difficulty:** Easy  
**Recommended for:** First-time players

### 2. The Lair of Mutants
*by Jim Jacobson*

Investigate an abandoned laboratory beneath the city where horrible experiments created mutant creatures. Can you survive the horrors within?

**Difficulty:** Medium  
**Recommended for:** Experienced players

## Converting Original Eamon Adventures

**NEW!** You can now import original Apple II Eamon adventures from .DSK disk images!

### Quick Conversion

```bash
./convert_dsk.sh your_adventure.dsk
```

The converted adventure will be saved to the `adventures/` directory and ready to play.

### Where to Get Eamon .DSK Files

- **Eamon Adventurer's Guild**: http://www.eamonag.org/ (250+ adventures)
- **Internet Archive**: Search for "Eamon" in Apple II collections
- Classic Apple II software repositories

### Conversion Details

The converter:
- Reads DOS 3.3 disk images (.dsk, .do formats)
- Extracts Eamon data files (DESC, ROOM, ARTIFACT, MONSTER)
- Converts to JSON format compatible with this engine
- Preserves original adventure content and metadata

For complete conversion documentation, see `DSK_CONVERSION_GUIDE.md`.

### Example

```bash
# Download an original Eamon adventure
wget http://www.eamonag.org/adventures/beginner.dsk

# Convert it
./convert_dsk.sh beginner.dsk

# Play it
./play_adventure.sh beginner.json
```

**Note**: Some manual editing may be needed for optimal results. See the conversion guide for details.

## Creating Your Own Adventures

### Method 1: Use the GUI IDE (Recommended)

Launch the Adventure Construction Set IDE:

```bash
./launch_ide.sh
```

The IDE provides:
- **Visual editing** of rooms, items, and monsters
- **Real-time testing** (press F5 to test your adventure)
- **Import DSK files** for editing original Eamon adventures
- **Enhanced features**: Add puzzles, quests, dialogue, equipment
- **Validation tools** to catch errors
- **JSON preview** to see the generated data
- **Play tab** to test adventures without leaving the editor

See `IDE_GUIDE.md` and `ENHANCED_FEATURES_GUIDE.md` for complete documentation.

### Method 2: Edit JSON Directly

Adventures are defined in JSON format. Here's a minimal example:

```json
{
  "title": "My Adventure",
  "author": "Your Name",
  "intro": "Welcome to my adventure!",
  "start_room": 1,
  "rooms": [
    {
      "id": 1,
      "name": "Starting Room",
      "description": "You are in a room.",
      "exits": {"north": 2}
    }
  ],
  "items": [],
  "monsters": [],
  "effects": []
}
```

### Adventure File Structure

- **title**: Name of your adventure
- **author**: Your name
- **intro**: Text shown when adventure starts
- **start_room**: Room ID where player begins
- **rooms**: Array of room objects
- **items**: Array of item objects
- **monsters**: Array of monster/NPC objects
- **effects**: Special events (advanced)

### Room Object
```json
{
  "id": 1,
  "name": "Room Name",
  "description": "Room description",
  "exits": {
    "north": 2,
    "south": 1,
    "east": 3
  },
  "is_dark": false
}
```

### Item Object
```json
{
  "id": 1,
  "name": "sword",
  "description": "A sharp sword",
  "type": "weapon",
  "weight": 5,
  "value": 50,
  "is_weapon": true,
  "weapon_type": 5,
  "weapon_dice": 2,
  "weapon_sides": 6,
  "is_takeable": true,
  "location": 1
}
```

**Weapon types:**
1. Axe
2. Bow
3. Club
4. Spear
5. Sword

### Monster Object
```json
{
  "id": 1,
  "name": "goblin",
  "description": "A nasty goblin",
  "room_id": 2,
  "hardiness": 10,
  "agility": 12,
  "friendliness": "hostile",
  "courage": 100,
  "weapon_id": null,
  "armor_worn": 0,
  "gold": 15
}
```

**Friendliness values:**
- `friendly` - Won't attack
- `neutral` - May or may not attack
- `hostile` - Will attack on sight

## File Structure

```
HB_Eamon/
├── eamon_engine.py       # Core game engine
├── eamon_launcher.py     # Main menu launcher
├── play_eamon.sh         # Shell script for main menu
├── play_adventure.sh     # Shell script for direct play
├── README.md            # This file
└── adventures/          # Adventure files
    ├── beginners_cave.json
    └── lair_of_mutants.json
```

## Gameplay Tips

1. **Always explore thoroughly** - Check all directions and pick up items
2. **Read item descriptions** - They often contain clues
3. **Save healing potions** for tough fights
4. **Better weapons make combat easier** - Equip the best weapon you find
5. **Some monsters are friendly** - Don't attack everything on sight!
6. **Watch your health** - Retreat if you're getting low

## Advanced Features

### Combat System
- Weapon damage is calculated using dice rolls (e.g., 2d6 = two 6-sided dice)
- Higher agility gives you better chance to hit
- Armor reduces damage taken
- Monster courage affects whether they flee or fight

### Character Stats
- **Hardiness**: Health/hit points
- **Agility**: Combat effectiveness and dodging
- **Charisma**: Affects NPC reactions (future feature)

## Troubleshooting

**Problem:** Scripts won't run  
**Solution:** Make sure they're executable: `chmod +x *.sh`

**Problem:** "python3: command not found"  
**Solution:** Install Python 3 for your distribution:
- Ubuntu/Debian: `sudo apt install python3`
- Fedora: `sudo dnf install python3`
- Arch: `sudo pacman -S python`

**Problem:** IDE won't launch  
**Solution:** Install tkinter:
- Ubuntu/Debian: `sudo apt install python3-tk`
- Fedora: `sudo dnf install python3-tkinter`
- Arch: `sudo pacman -S tk`

**Problem:** Adventure won't load  
**Solution:** Check that the JSON file is valid. Use a JSON validator online or run:
```bash
python3 -m json.tool adventures/your_adventure.json
```

## Contributing

Want to contribute an adventure? Create a JSON file following the format above and submit it!

### Adventure Guidelines
- Make sure all room IDs are unique
- Test thoroughly before submitting
- Include interesting descriptions
- Balance difficulty appropriately
- Give items meaningful descriptions

## Credits

- **Adventure Construction Set**: Modern text adventure creation system
- **Original Eamon System**: Donald Brown (1980) - Full backward compatibility maintained
- **Engine**: Python 3 implementation with classic and enhanced features
- **Enhanced Features**: Puzzles, quests, dialogue, equipment, character progression

## License

This is an open adventure creation system with full backward compatibility with the classic Eamon format. Original Eamon adventures may have their own copyright - please respect original authors' wishes.

## Additional Resources

- **Enhanced Features Guide**: See `ENHANCED_FEATURES_GUIDE.md` for new capabilities
- **IDE Guide**: See `IDE_GUIDE.md` for complete GUI editor documentation
- **DSK Conversion**: See `DSK_CONVERSION_GUIDE.md` for importing original Eamon adventures
- **Quick Start**: See `QUICKSTART.md` for fast setup
- Original Eamon adventures: http://www.eamonag.org/ (250+ adventures)
- Eamon Wiki: Various fan sites document the extensive Eamon universe

---

**Create amazing text adventures with the Adventure Construction Set!**
**Fully compatible with 40+ years of Eamon adventures!**

For questions or issues, please open an issue on the project repository.
