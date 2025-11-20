# Playing Adventures in the IDE

The Adventure IDE now includes an integrated game player! You can create, edit, and play your adventures all in one window.

## How to Use the Play Tab

### 1. Open or Create an Adventure

First, make sure you have an adventure loaded:
- Open an existing adventure (Ctrl+O)
- Or create a new one and add some rooms, items, and monsters

### 2. Switch to the Play Tab

Click on the **"Play Adventure"** tab in the IDE.

You'll see:
- A large game output area (with retro green-on-black terminal style)
- A command input field at the bottom
- Control buttons: Start Game, Restart, Clear Output

### 3. Start Playing

Click the **"▶ Start Game"** button to begin playing your current adventure.

The game will:
- Display the adventure title and introduction
- Show your starting room description
- Wait for your commands

### 4. Enter Commands

Type commands in the command field and press **Enter** or click **"Send Command"**.

**Available Commands:**
- `n, s, e, w, u, d` - Move north/south/east/west/up/down
- `look` or `l` - Look around the current room
- `get <item>` - Pick up an item
- `drop <item>` - Drop an item
- `attack <monster>` - Attack a monster
- `inventory` or `i` - Show your inventory
- `status` - Show character stats
- `help` - Show available commands
- `quit` - End the game

### 5. Control Buttons

**▶ Start Game** - Starts the loaded adventure from the beginning

**⟳ Restart** - Restarts the current game from the beginning

**⏸ Clear Output** - Clears the game display (doesn't affect game state)

## Workflow Example

### Quick Test Workflow

1. **Edit** your adventure in the other tabs (Rooms, Items, Monsters)
2. **Switch** to Play Adventure tab
3. **Click** "▶ Start Game"
4. **Play** through to test your changes
5. **Switch back** to edit tabs if you find issues
6. **Restart** the game to test fixes

### Full Development Cycle

```
Create/Edit → Play Test → Find Issues → Edit Again → Play Test → Save
```

No need to save before testing - the Play tab automatically uses your current edits!

## Features

### Real-time Testing
- Test without saving
- Instant feedback on your changes
- No need to switch between applications

### Integrated Experience
- All in one window
- Easy to switch between editing and playing
- See your creation come to life immediately

### Retro Terminal Look
- Green text on black background
- Monospace font (Courier)
- Classic adventure game feel

## Tips

### Testing Strategy
1. **Start small** - Test individual rooms first
2. **Check exits** - Make sure room connections work
3. **Test items** - Verify you can pick up and drop items
4. **Fight monsters** - Check combat balance
5. **Complete playthrough** - Test the entire adventure end-to-end

### Quick Testing
- Use `look` command frequently to see room descriptions
- Try `inventory` to verify item handling
- Use `status` to check your character stats
- Test all directions (n/s/e/w/u/d) to verify exits

### Debugging
If something doesn't work:
1. **Check the output** - Error messages appear in the game display
2. **Verify room IDs** - Make sure exits point to existing rooms
3. **Check start_room** - Ensure it's set to a valid room ID
4. **Use Validate** - Go to Tools → Validate Adventure

## Keyboard Shortcuts

- **Enter** in command field - Send command
- **F5** (from any tab) - Test in external window (old method)
- **Ctrl+S** - Save your adventure

## Comparison: Play Tab vs External Testing

### Play Tab (New)
✅ Play inside the IDE
✅ No window switching
✅ Quick iteration
✅ See changes instantly
✅ Retro terminal look

### External Testing (F5)
✅ Full-screen experience
✅ Separate window
✅ More traditional
✅ Run from command line

**Both methods work!** Choose what you prefer.

## Example Session

```
> Start Game (click button)

============================================================
  THE BEGINNER'S CAVE
============================================================

You have heard rumors of a mysterious cave filled with
treasure and danger. You stand at the entrance, ready
to explore its depths.

============================================================

You are in the entrance to a dark cave. Rough stone walls
surround you. There are exits to the north and east.

> n

You enter a large cavern. Stalactites hang from the ceiling
like stone teeth. A rusty sword lies on the ground.
Exits: south, east

> get sword

You pick up the rusty sword.

> inventory

You are carrying:
  - rusty sword (weapon)

> e

You enter a narrow tunnel. Something moves in the shadows...
A goblin blocks your path!
Exits: west

> attack goblin

You swing the rusty sword at the goblin!
You hit for 8 damage!
The goblin attacks back...
[combat continues...]
```

## Troubleshooting

### "Please start the game first"
- Click "▶ Start Game" button before entering commands

### No output appears
- Make sure your adventure has rooms defined
- Check that start_room is set correctly
- Verify adventure has a title

### Game won't start
- Go to Tools → Validate Adventure to check for errors
- Make sure at least one room exists
- Check that room IDs are valid

### Commands don't work
- Make sure the game is running (started)
- Check command spelling
- Try `help` command to see available commands

## Advanced Features

### Playing Other Adventures
1. Open any adventure JSON file (Ctrl+O)
2. Switch to Play Adventure tab
3. Click "▶ Start Game"
4. Explore someone else's creation!

### Testing Imported Adventures
1. Import a DSK file (Tools → Import DSK File)
2. Switch to Play Adventure tab
3. Click "▶ Start Game"
4. Experience interactive fiction adventures!

### Rapid Prototyping
1. Create a basic room structure
2. Test immediately in Play tab
3. Add more content
4. Test again
5. Repeat until satisfied

## Why This is Useful

### For Developers
- **Instant feedback** on your design decisions
- **Quick iteration** without file saving
- **Easier debugging** with immediate testing
- **Better workflow** - edit and play in one place

### For Players
- **Try before you commit** - test adventures before saving
- **Explore modifications** - change things and see what happens
- **Learn by doing** - understand adventure structure by playing

### For Everyone
- **All-in-one tool** - no need for multiple programs
- **Faster creation** - reduce time between idea and testing
- **More fun** - see your creation come alive instantly!

---

**Ready to play?** Open the IDE, switch to the Play Adventure tab, and click "▶ Start Game"!

Enjoy creating and playing your adventures!
