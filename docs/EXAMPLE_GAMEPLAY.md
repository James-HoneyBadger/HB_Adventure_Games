# Example Gameplay Session

This document shows what a typical game session looks like.

## Starting the Game

```bash
$ ./play_adventure.sh beginners_cave.json
```

## Sample Gameplay

```
============================================================
                    The Beginner's Cave                     
============================================================

You are standing at the entrance to a mysterious cave. Rumors speak of
treasure and danger within. As a novice adventurer, this seems like the
perfect place to test your skills.

Your quest: explore the cave, defeat any monsters, and return with treasure!


Cave Entrance
-------------
You stand at the mouth of a dark cave. Cool air flows from within.
The entrance is partially concealed by vines and moss. A narrow passage
leads deeper into the darkness to the north.

Obvious exits: north, south

> help

============================================================
EAMON COMMANDS
============================================================

Movement:
  n, north, s, south, e, east, w, west, u, up, d, down

Actions:
  look (l)        - Look around
  get/take <item> - Pick up an item
  drop <item>     - Drop an item
  attack <target> - Attack a monster

Info:
  inventory (i)   - Show what you're carrying
  status          - Show your character stats
  help (h, ?)     - Show this help

Other:
  quit (q)        - Exit the game
============================================================

> north

Dark Corridor
-------------
A narrow, winding corridor stretches before you. The walls are damp
and covered with strange fungus that glows faintly, providing just enough
light to see. You hear the drip of water echoing from somewhere ahead.

Obvious exits: north, south, east

You see:
  - leather armor
  - old map

Present:
  - giant rat (hostile)

> get map
You take the old map.

> get armor
You take the leather armor.

> attack rat

You attack the giant rat!
You hit for 3 damage!
The giant rat hits you for 2 damage!

> attack rat

You attack the giant rat!
You hit for 4 damage!
The giant rat is dead!
You found 5 gold pieces!

> inventory

You are carrying:
  - old map
  - leather armor

Total weight: 9
Gold: 205

> status

Adventurer
----------------------------------------
Health: 10/12
Hardiness: 12
Agility: 12
Charisma: 12
Gold: 205

> east

Storage Chamber
---------------
This appears to be an old storage room. Broken crates and barrels are
scattered about. In the corner, you notice something glinting in the dim light.

Obvious exits: west

You see:
  - rusty sword
  - healing potion

> get sword
You take the rusty sword.

> get potion
You take the healing potion.

> inventory

You are carrying:
  - old map
  - leather armor
  - rusty sword
  - healing potion

Total weight: 15
Gold: 205

> west

Dark Corridor
-------------
(Room description...)

> north

Underground Stream
------------------
A small underground stream cuts across the cave floor here. The water
is clear and cold. A wooden bridge crosses to the north, though it looks
rather rickety. To the west, you see a faint glow.

Obvious exits: south, north, west

> west

Crystal Grotto
--------------
This chamber is filled with beautiful crystals that emit a soft blue glow.
The walls sparkle with thousands of tiny reflections. It's quite peaceful here.

Obvious exits: east

You see:
  - gold coins

> get coins
You take the gold coins.

> inventory

You are carrying:
  - old map
  - leather armor
  - rusty sword
  - healing potion
  - gold coins

Total weight: 16
Gold: 205

> status

Adventurer
----------------------------------------
Health: 10/12
Hardiness: 12
Agility: 12
Charisma: 12
Gold: 255
Weapon: None
Armor: None

> quit

Thanks for playing!
```

## Tips from This Session

1. **Always pick up items** - The map and armor could be useful
2. **Fight monsters** - You gain gold and experience
3. **Explore thoroughly** - Check all directions
4. **Check your status** - Know your health before big fights
5. **Manage inventory** - Keep track of what you have

## Advanced Play

For more challenging gameplay:
- Equip weapons before fighting
- Wear armor for protection
- Save healing potions for emergencies
- Explore all rooms before fighting the boss
- Return to the entrance when ready to leave

## Creating Your Own Adventure

After playing, you might want to create your own! See `README.md` for 
the complete JSON format and guidelines.

---

Enjoy exploring the Wonderful World of Eamon!
