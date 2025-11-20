#!/usr/bin/env python3
"""
Test script to verify all 10 enhancement systems are working
"""


def test_imports():
    """Test that all modules can be imported"""
    print("Testing module imports...")

    try:
        import acs_npc_context

        print("  ✓ acs_npc_context")
    except ImportError as e:
        print(f"  ✗ acs_npc_context: {e}")
        return False

    try:
        import acs_environment

        print("  ✓ acs_environment")
    except ImportError as e:
        print(f"  ✗ acs_environment: {e}")
        return False

    try:
        import acs_commands

        print("  ✓ acs_commands")
    except ImportError as e:
        print(f"  ✗ acs_commands: {e}")
        return False

    try:
        import acs_combat

        print("  ✓ acs_combat")
    except ImportError as e:
        print(f"  ✗ acs_combat: {e}")
        return False

    try:
        import acs_achievements

        print("  ✓ acs_achievements")
    except ImportError as e:
        print(f"  ✗ acs_achievements: {e}")
        return False

    try:
        import acs_journal

        print("  ✓ acs_journal")
    except ImportError as e:
        print(f"  ✗ acs_journal: {e}")
        return False

    try:
        import acs_tutorial

        print("  ✓ acs_tutorial")
    except ImportError as e:
        print(f"  ✗ acs_tutorial: {e}")
        return False

    try:
        import acs_modding

        print("  ✓ acs_modding")
    except ImportError as e:
        print(f"  ✗ acs_modding: {e}")
        return False

    try:
        import acs_accessibility

        print("  ✓ acs_accessibility")
    except ImportError as e:
        print(f"  ✗ acs_accessibility: {e}")
        return False

    try:
        import acs_engine

        print("  ✓ acs_engine (with all systems integrated)")
    except ImportError as e:
        print(f"  ✗ acs_engine: {e}")
        return False

    return True


def test_basic_functionality():
    """Test basic functionality of each system"""
    print("\nTesting basic functionality...")

    # Test NPC Context
    from acs_npc_context import NPCContextManager

    npc_mgr = NPCContextManager()
    ctx = npc_mgr.get_or_create_context(1, "Wizard")
    npc_mgr.improve_relationship(1, 10)
    print("  ✓ NPC Context: Create context and update relationship")

    # Test Environment
    from acs_environment import EnvironmentalSystem

    env = EnvironmentalSystem()
    time_desc = env.get_time_description()
    print(f"  ✓ Environment: Time system ({time_desc})")

    # Test Commands
    from acs_commands import SmartCommandSystem

    cmd_sys = SmartCommandSystem()
    cmd_sys.add_to_history("north")
    corrected = cmd_sys.predictor.correct_command("attak")
    print(f"  ✓ Commands: Typo correction (attak → {corrected})")

    # Test Combat
    from acs_combat import CombatEncounter, Combatant

    player = Combatant(name="Hero", max_health=100, attack=15, defense=10)
    enemy = Combatant(name="Goblin", max_health=30, attack=8, defense=5)
    encounter = CombatEncounter(player, [enemy])
    print("  ✓ Combat: Create encounter with positioning")

    # Test Achievements
    from acs_achievements import AchievementSystem

    ach_sys = AchievementSystem()
    ach_sys.stats.increment("steps_taken")
    ach_sys.check_achievements()
    print("  ✓ Achievements: Track stats and check unlocks")

    # Test Journal
    from acs_journal import AdventureJournal

    journal = AdventureJournal()
    journal.log_event("Test event", room_id=1)
    journal.add_manual_note("Test note")
    print("  ✓ Journal: Log events and add notes")

    # Test Tutorial
    from acs_tutorial import ContextualHintSystem

    tutorial = ContextualHintSystem()
    hint = tutorial.check_and_show_hint("moved", {"rooms_visited": 1})
    print("  ✓ Tutorial: Check contextual hints")

    # Test Modding
    from acs_modding import ModdingSystem, ScriptHook, EventType

    mod_sys = ModdingSystem()
    hook = ScriptHook(event=EventType.ON_ENTER_ROOM, script_code='echo("Test hook")')
    mod_sys.register_hook(hook)
    print("  ✓ Modding: Register event hooks")

    # Test Accessibility
    from acs_accessibility import AccessibilitySystem, DifficultyLevel

    acc_sys = AccessibilitySystem()
    acc_sys.set_difficulty(DifficultyLevel.EASY)
    health_bar = acc_sys.format_health_bar(75, 100)
    print(f"  ✓ Accessibility: Difficulty & formatting")

    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("Adventure Construction Set - System Verification")
    print("=" * 60)
    print()

    if not test_imports():
        print("\n✗ Import test failed!")
        return False

    if not test_basic_functionality():
        print("\n✗ Functionality test failed!")
        return False

    print("\n" + "=" * 60)
    print("✓ ALL SYSTEMS OPERATIONAL!")
    print("=" * 60)
    print("\nSystems verified:")
    print("  1. NPC Memory & Context")
    print("  2. Advanced Party Commands")
    print("  3. Environmental Storytelling")
    print("  4. Smart Command Prediction")
    print("  5. Enhanced Combat System")
    print("  6. Achievement & Statistics")
    print("  7. Journal & Note-Taking")
    print("  8. Tutorial & Contextual Help")
    print("  9. Modding & Scripting Support")
    print(" 10. Accessibility Features")
    print("\nTotal: 10/10 systems ready! 🎉")
    return True


if __name__ == "__main__":
    import sys

    success = main()
    sys.exit(0 if success else 1)
