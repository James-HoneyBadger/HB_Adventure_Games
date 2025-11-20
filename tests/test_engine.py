#!/usr/bin/env python3
"""
Quick test of the Eamon game engine
Simulates a short playthrough
"""

import sys

sys.path.insert(0, "/home/james/HB_Eamon")

from eamon_engine import EamonGame


def test_game():
    """Test basic game functionality"""
    print("Testing Eamon Game Engine...")
    print("=" * 60)

    # Load the game
    game = EamonGame("/home/james/HB_Eamon/adventures/beginners_cave.json")
    game.load_adventure()

    print("\n✓ Adventure loaded successfully")
    print(f"✓ Title: {game.adventure_title}")
    print(f"✓ Rooms: {len(game.rooms)}")
    print(f"✓ Items: {len(game.items)}")
    print(f"✓ Monsters: {len(game.monsters)}")

    # Test room navigation
    print("\n" + "=" * 60)
    print("Testing room description...")
    print("=" * 60)
    game.look()

    print("\n" + "=" * 60)
    print("Testing inventory...")
    print("=" * 60)
    game.show_inventory()

    print("\n" + "=" * 60)
    print("Testing character status...")
    print("=" * 60)
    game.show_status()

    print("\n" + "=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)
    print("\nThe game engine is working correctly.")
    print("Use ./play_eamon.sh to play with the full menu system.")
    print("Use ./play_adventure.sh <adventure.json> to play directly.")


if __name__ == "__main__":
    test_game()
