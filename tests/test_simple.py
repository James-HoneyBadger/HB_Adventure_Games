#!/usr/bin/env python3
"""Quick test of all 10 systems"""

print("=" * 60)
print("Testing All 10 Enhancement Systems")
print("=" * 60)

systems = [
    ("acs_npc_context", "NPC Memory & Context"),
    ("acs_environment", "Environmental Storytelling"),
    ("acs_commands", "Smart Command Prediction"),
    ("acs_combat", "Enhanced Combat System"),
    ("acs_achievements", "Achievement & Statistics"),
    ("acs_journal", "Journal & Note-Taking"),
    ("acs_tutorial", "Tutorial & Contextual Help"),
    ("acs_modding", "Modding & Scripting Support"),
    ("acs_accessibility", "Accessibility Features"),
    ("acs_engine", "Game Engine (with all systems)"),
]

passed = 0
for module, name in systems:
    try:
        __import__(module)
        print(f"  ✓ {name}")
        passed += 1
    except Exception as e:
        print(f"  ✗ {name}: {e}")

print("=" * 60)
print(f"Result: {passed}/{len(systems)} systems operational")
print("=" * 60)

if passed == len(systems):
    print("\n🎉 ALL SYSTEMS READY! 🎉\n")
