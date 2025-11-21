#!/usr/bin/env python3
"""
Detailed parser verification script.
Tests each command with multiple variations and edge cases.
"""

from src.acs.core.parser import NaturalLanguageParser


def test_movement_commands():
    """Test all movement-related commands"""
    parser = NaturalLanguageParser()

    print("=" * 70)
    print("MOVEMENT COMMANDS TEST")
    print("=" * 70)

    tests = [
        # Basic directions
        ("north", {"action": "move", "direction": "north"}),
        ("go north", {"action": "move", "direction": "north"}),
        (
            "north",
            {"action": "move", "direction": "north"},
        ),
        (
            "n",
            {"action": "move", "direction": "north"},
        ),
        (
            "south",
            {"action": "move", "direction": "south"},
        ),
        (
            "s",
            {"action": "move", "direction": "south"},
        ),
        (
            "east",
            {"action": "move", "direction": "east"},
        ),
        (
            "e",
            {"action": "move", "direction": "east"},
        ),
        (
            "west",
            {"action": "move", "direction": "west"},
        ),
        (
            "w",
            {"action": "move", "direction": "west"},
        ),
        (
            "northeast",
            {"action": "move", "direction": "northeast"},
        ),
        (
            "ne",
            {"action": "move", "direction": "northeast"},
        ),
        (
            "northwest",
            {"action": "move", "direction": "northwest"},
        ),
        (
            "nw",
            {"action": "move", "direction": "northwest"},
        ),
        (
            "southeast",
            {"action": "move", "direction": "southeast"},
        ),
        (
            "se",
            {"action": "move", "direction": "southeast"},
        ),
        (
            "southwest",
            {"action": "move", "direction": "southwest"},
        ),
        (
            "sw",
            {"action": "move", "direction": "southwest"},
        ),
        # Northeast, etc
        ("northeast", {"action": "move", "direction": "northeast"}),
        ("ne", {"action": "move", "direction": "northeast"}),
        ("northwest", {"action": "move", "direction": "northwest"}),
        ("nw", {"action": "move", "direction": "northwest"}),
        ("southeast", {"action": "move", "direction": "southeast"}),
        ("se", {"action": "move", "direction": "southeast"}),
        ("southwest", {"action": "move", "direction": "southwest"}),
        ("sw", {"action": "move", "direction": "southwest"}),
        # Enter/exit
        ("enter cave", {"action": "move"}),
        ("exit building", {"action": "move"}),
        ("go in", {"action": "move"}),
        ("go out", {"action": "move"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")
        if "direction" in expected:
            matches = matches and result.get("direction") == expected["direction"]

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "direction" in result:
                direction = result["direction"]
                print(f" ({direction})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Movement command parsing regressions detected."


def test_observation_commands():
    """Test look, examine, read, search commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("OBSERVATION COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("look", {"action": "look"}),
        ("l", {"action": "look"}),
        ("look around", {"action": "look"}),
        ("examine sword", {"action": "look", "target": "sword"}),
        ("inspect door", {"action": "look", "target": "door"}),
        ("check chest", {"action": "look", "target": "chest"}),
        ("read book", {"action": "read", "target": "book"}),
        ("read the scroll", {"action": "read", "target": "the scroll"}),
        ("search", {"action": "search"}),
        ("search room", {"action": "search"}),
        ("look for treasure", {"action": "search"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Observation command parsing regressions detected."


def test_item_commands():
    """Test get, drop, put commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("ITEM MANAGEMENT COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("get sword", {"action": "get", "target": "sword"}),
        ("take sword", {"action": "get", "target": "sword"}),
        ("grab the golden key", {"action": "get", "target": "the golden key"}),
        ("pick up coins", {"action": "get", "target": "coins"}),
        ("drop shield", {"action": "drop", "target": "shield"}),
        ("put down torch", {"action": "drop", "target": "torch"}),
        ("leave the heavy armor", {"action": "drop"}),
        ("put gem in bag", {"action": "put"}),
        ("place book on table", {"action": "put"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Item command parsing regressions detected."


def test_inventory_commands():
    """Test inventory and equipment commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("INVENTORY & EQUIPMENT COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("inventory", {"action": "inventory"}),
        ("i", {"action": "inventory"}),
        ("inv", {"action": "inventory"}),
        ("items", {"action": "inventory"}),
        ("what am i carrying", {"action": "inventory"}),
        ("equip sword", {"action": "equip", "target": "sword"}),
        ("wear helmet", {"action": "equip", "target": "helmet"}),
        ("wield axe", {"action": "equip", "target": "axe"}),
        ("unequip shield", {"action": "unequip", "target": "shield"}),
        ("remove armor", {"action": "unequip", "target": "armor"}),
        ("take off boots", {"action": "unequip", "target": "boots"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Inventory command parsing regressions detected."


def test_combat_commands():
    """Test attack and flee commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("COMBAT COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("attack goblin", {"action": "attack", "target": "goblin"}),
        ("fight orc", {"action": "attack", "target": "orc"}),
        ("kill dragon", {"action": "attack", "target": "dragon"}),
        ("hit the troll", {"action": "attack", "target": "the troll"}),
        ("strike zombie", {"action": "attack", "target": "zombie"}),
        ("flee", {"action": "flee"}),
        ("run away", {"action": "flee"}),
        ("escape", {"action": "flee"}),
        ("retreat", {"action": "flee"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Combat command parsing regressions detected."


def test_interaction_commands():
    """Test talk, give, trade commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("INTERACTION COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("talk to merchant", {"action": "talk", "target": "merchant"}),
        ("speak to guard", {"action": "talk", "target": "guard"}),
        ("chat with wizard", {"action": "talk", "target": "wizard"}),
        ("ask the old man", {"action": "talk", "target": "the old man"}),
        ("give gold to merchant", {"action": "give"}),
        ("offer sword to knight", {"action": "give"}),
        ("hand key to guard", {"action": "give"}),
        ("trade with merchant", {"action": "trade", "target": "merchant"}),
        ("barter with shopkeeper", {"action": "trade"}),
        ("buy sword", {"action": "trade", "target": "sword"}),
        ("sell shield", {"action": "trade", "target": "shield"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Interaction command parsing regressions detected."


def test_consumption_commands():
    """Test eat, drink, use commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("CONSUMPTION COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("eat bread", {"action": "eat", "target": "bread"}),
        ("consume apple", {"action": "eat", "target": "apple"}),
        ("devour meat", {"action": "eat", "target": "meat"}),
        ("drink potion", {"action": "drink", "target": "potion"}),
        ("sip water", {"action": "drink", "target": "water"}),
        ("quaff the healing potion", {"action": "drink"}),
        ("use key", {"action": "use", "target": "key"}),
        ("utilize rope", {"action": "use", "target": "rope"}),
        ("activate lever", {"action": "use", "target": "lever"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Consumption command parsing regressions detected."


def test_environment_commands():
    """Test open and close commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("ENVIRONMENT COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("open door", {"action": "open", "target": "door"}),
        ("unlock chest", {"action": "open", "target": "chest"}),
        ("open the treasure box", {"action": "open"}),
        ("close door", {"action": "close", "target": "door"}),
        ("shut window", {"action": "close", "target": "window"}),
        ("lock gate", {"action": "close", "target": "gate"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Environment command parsing regressions detected."


def test_information_commands():
    """Test status, help, quests commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("INFORMATION COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("status", {"action": "status"}),
        ("stats", {"action": "status"}),
        ("condition", {"action": "status"}),
        ("health", {"action": "status"}),
        ("help", {"action": "help"}),
        ("?", {"action": "help"}),
        ("commands", {"action": "help"}),
        ("quests", {"action": "quests"}),
        ("missions", {"action": "quests"}),
        ("objectives", {"action": "quests"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}")
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Information command parsing regressions detected."


def test_party_commands():
    """Test party management commands"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("PARTY COMMANDS TEST")
    print("=" * 70)

    tests = [
        ("recruit fighter", {"action": "recruit", "target": "fighter"}),
        ("hire wizard", {"action": "recruit", "target": "wizard"}),
        ("invite thief to party", {"action": "recruit"}),
        ("dismiss bob", {"action": "dismiss", "target": "bob"}),
        ("fire guard", {"action": "dismiss", "target": "guard"}),
        ("party", {"action": "party"}),
        ("companions", {"action": "party"}),
        ("group", {"action": "party"}),
        ("order bob to attack goblin", {"action": "party_order"}),
        ("tell alice to defend", {"action": "party_order"}),
        ("command charlie to flee", {"action": "party_order"}),
        ("gather", {"action": "gather"}),
        ("regroup", {"action": "gather"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")

        if matches:
            print(f"✓ '{command}' -> {action}", end="")
            if "target" in result:
                print(f" (target: {result.get('target', 'N/A')})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Party command parsing regressions detected."


def test_edge_cases():
    """Test edge cases and special scenarios"""
    parser = NaturalLanguageParser()

    print("\n" + "=" * 70)
    print("EDGE CASES TEST")
    print("=" * 70)

    tests = [
        # Empty/whitespace
        ("", {"action": None}),
        ("   ", {"action": None}),
        # Questions
        ("where am i", {"action": "question"}),
        ("what am i carrying", {"action": "inventory"}),
        ("who is here", {"action": "question"}),
        # Multi-word items
        ("get ancient rusty sword", {"action": "get"}),
        ("take the old worn shield", {"action": "get"}),
        # Case insensitivity
        ("NORTH", {"action": "move", "direction": "north"}),
        ("Attack GOBLIN", {"action": "attack"}),
        ("InVeNtOrY", {"action": "inventory"}),
        # Unknown verbs should default to examine
        ("poke stick", {"action": "look"}),
        ("random gibberish", {"action": "look"}),
    ]

    passed = 0
    failed = 0

    for command, expected in tests:
        result = parser.parse_sentence(command)
        action = result.get("action")
        matches = action == expected.get("action")
        if "direction" in expected:
            matches = matches and result.get("direction") == expected["direction"]

        if matches:
            safe_action = action or "None"
            print(f"✓ '{command}' -> {safe_action}", end="")
            if "direction" in result:
                print(f" ({result['direction']})")
            else:
                print()
            passed += 1
        else:
            print(f"✗ '{command}' -> Expected {expected}, got {result}")
            failed += 1

    print(f"\nPassed: {passed}/{len(tests)}")
    if failed > 0:
        print(f"Failed: {failed}")
    assert failed == 0, "Parser edge-case regressions detected."


def main():
    """Run all parser tests"""
    print("\n" + "=" * 70)
    print("COMPREHENSIVE PARSER VERIFICATION TEST SUITE")
    print("=" * 70)

    total_passed = 0
    total_failed = 0

    # Run all test suites
    test_suites = [
        test_movement_commands,
        test_observation_commands,
        test_item_commands,
        test_inventory_commands,
        test_combat_commands,
        test_interaction_commands,
        test_consumption_commands,
        test_environment_commands,
        test_information_commands,
        test_party_commands,
        test_edge_cases,
    ]

    for test_suite in test_suites:
        passed, failed = test_suite()
        total_passed += passed
        total_failed += failed

    # Final summary
    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)
    print(f"Total tests run:    {total_passed + total_failed}")
    print(f"✓ Passed:           {total_passed}")
    print(f"✗ Failed:           {total_failed}")
    total_tests = total_passed + total_failed
    success_rate = (total_passed / total_tests * 100) if total_tests else 0.0
    print(f"Success rate:       {success_rate:.1f}%")
    print("=" * 70 + "\n")

    if total_failed == 0:
        print("🎉 ALL TESTS PASSED! Parser is working perfectly!")
    else:
        print(f"⚠️  {total_failed} tests failed - review failures above")


if __name__ == "__main__":
    main()
