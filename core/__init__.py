"""
Core game engine components

This package contains the fundamental building blocks of the game engine:
- BasePlugin: Interface for all game systems
- EventBus: Event-driven communication system
- GameState: Centralized state management
- Engine: Main orchestration layer
"""

from .base_plugin import BasePlugin, PluginMetadata, PluginPriority
from .event_bus import EventBus, Event, EventPriority
from .game_state import GameState
from .engine import Engine
from .services import ServiceRegistry, Service

__all__ = [
    "BasePlugin",
    "PluginMetadata",
    "PluginPriority",
    "EventBus",
    "Event",
    "EventPriority",
    "GameState",
    "Engine",
    "ServiceRegistry",
    "Service",
]
