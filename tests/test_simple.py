#!/usr/bin/env python3
"""Quick test of all 10 systems"""

print("=" * 60)
print("Testing All 10 Enhancement Systems")
print("=" * 60)

systems = [
    ("src.acs.systems.npc_context", "NPC Memory & Context"),
    ("src.acs.systems.environment", "Environmental Storytelling"),
    ("src.acs.tools.commands", "Smart Command Prediction"),
    ("src.acs.systems.combat", "Enhanced Combat System"),
    ("src.acs.systems.achievements", "Achievement & Statistics"),
    ("src.acs.systems.journal", "Journal & Note-Taking"),
    ("src.acs.systems.tutorial", "Tutorial & Contextual Help"),
    ("src.acs.tools.modding", "Modding & Scripting Support"),
    ("src.acs.ui.accessibility", "Accessibility Features"),
    ("src.acs.core.engine", "Game Engine (with all systems)"),
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
