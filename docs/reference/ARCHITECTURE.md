# Architecture Guide

## Overview

The Adventure Construction Set has been refactored into a **modular, event-driven architecture** that emphasizes:

- **Loose coupling** through events and dependency injection
- **Extensibility** via a plugin system
- **Maintainability** with clear separation of concerns
- **Testability** through service abstraction

## Architecture Layers

```
┌─────────────────────────────────────────┐
│           User Interface (UI)           │
│  Graphical IDE                           │
└──────────────┬──────────────────────────┘
               │
┌──────────────┴──────────────────────────┐
│        Engine (Orchestration)           │
│  Plugin management, game loop           │
└──────────────┬──────────────────────────┘
               │
┌──────────────┴──────────────────────────┐
│          Plugin System                  │
│  Achievement, Combat, NPC, etc.         │
└──────────────┬──────────────────────────┘
               │
┌──────────────┴──────────────────────────┐
│     Core Infrastructure                 │
│  EventBus, GameState, Services          │
└─────────────────────────────────────────┘
```

## Directory Structure

```
HB_Adventure_Games/
├── core/                    # Core engine components
│   ├── __init__.py
│   ├── base_plugin.py      # Plugin base class and interfaces
│   ├── event_bus.py        # Event system
│   ├── game_state.py       # Centralized state management
│   ├── engine.py           # Main orchestration layer
│   └── services.py         # Service registry
│
├── systems/                 # Plugin implementations
│   ├── __init__.py
│   ├── achievements.py     # Achievement system plugin
│   ├── combat.py           # Combat system plugin
│   ├── npc.py              # NPC/dialogue plugin
│   └── ...                 # Other game systems
│
├── utils/                   # Shared services
│   ├── __init__.py
│   ├── config_service.py   # Configuration management
│   ├── io_service.py       # File I/O operations
│   └── data_service.py     # Entity data management
│
├── ui/                      # User interfaces
│   ├── __init__.py
│   ├── ide.py              # Graphical IDE
│   └── accessibility.py    # Accessibility features
│
├── plugins/                 # User-installable plugins
│   └── custom_plugins/     # Third-party extensions
│
├── config/                  # Configuration files
│   ├── engine.yaml         # Engine settings
│   └── plugins/            # Plugin configurations
│
└── tests/                   # Test suite
    ├── unit/               # Unit tests
    ├── integration/        # Integration tests
    └── fixtures/           # Test data
```

## Core Components

### 1. Engine (`core/engine.py`)

The **Engine** is the main orchestrator that:
- Manages plugin lifecycle (register, initialize, enable/disable)
- Coordinates the game loop
- Manages state transitions
- Provides event publishing interface

```python
from core import Engine
from systems import AchievementPlugin

engine = Engine()
engine.register_plugin(AchievementPlugin())
engine.initialize()
engine.load_adventure('my_adventure.json')
engine.run()
```

### 2. EventBus (`core/event_bus.py`)

The **EventBus** enables loose coupling through publish-subscribe pattern:

**Benefits:**
- Plugins don't need direct references to each other
- Easy to add/remove features
- Clear event flow
- Support for cancellable events

**Events:**
```python
# Publishing events
event_bus.publish('game.move', {
    'from_room': 1,
    'to_room': 2,
    'player': player_data
})

# Subscribing to events  
def on_move(event):
    print(f"Player moved to room {event.data['to_room']}")
    
event_bus.subscribe('game.move', on_move)
```

**Common Events:**
- `engine.initialized` - Engine ready
- `game.start` - Game begins
- `game.move` - Player movement
- `command.input` - Player command entered
- `combat.start` - Combat initiated
- `item.pickup` - Item collected
- `achievement.unlocked` - Achievement earned

### 3. GameState (`core/game_state.py`)

**GameState** is a centralized data container:
- Single source of truth for game data
- Easy to serialize/deserialize (save/load)
- Plugin-specific data storage
- Global flags and turn counter

```python
# Access player data
player = state.player
player.gold += 100

# Plugin data
state.set_plugin_data('achievements', 'total_unlocked', 5)
unlocked = state.get_plugin_data('achievements', 'total_unlocked', 0)

# Flags
state.set_flag('dragon_defeated', True)
if state.get_flag('dragon_defeated'):
    print("The dragon is gone!")
```

### 4. BasePlugin (`core/base_plugin.py`)

All game systems extend **BasePlugin**:

```python
from core import BasePlugin, PluginMetadata, PluginPriority

class MyPlugin(BasePlugin):
    def __init__(self):
        metadata = PluginMetadata(
            name="my_plugin",
            version="1.0",
            priority=PluginPriority.NORMAL
        )
        super().__init__(metadata)
        
    def initialize(self, state, event_bus, services):
        super().initialize(state, event_bus, services)
        # Setup code here
        
    def get_event_subscriptions(self):
        return {
            'game.move': self.on_move,
            'combat.start': self.on_combat,
        }
        
    def on_move(self, event):
        # Handle movement
        pass
        
    def on_combat(self, event):
        # Handle combat
        pass
```

### 5. Services (`core/services.py`, `utils/`)

**Services** provide shared functionality:

**ConfigService** - Settings management
```python
config = services.get('config')
theme = config.get('ui.theme', 'dark')
config.set_plugin_config('my_plugin', 'enabled', True)
```

**IOService** - File operations
```python
io = services.get('io')
adventure = io.load_adventure('forest_quest')
io.save_game('slot1', game_state)
```

**DataService** - Entity management
```python
data = services.get('data')
room = data.get_room(5)
items_here = data.find_items_by_location(5)
```

## Plugin System

### Plugin Lifecycle

1. **Registration** - `engine.register_plugin(plugin)`
2. **Initialization** - Plugin receives state, event_bus, services
3. **Event Subscription** - Plugin handlers registered with event bus
4. **Activation** - `plugin.on_enable()` called
5. **Operation** - Plugin handles events during gameplay
6. **Deactivation** - `plugin.on_disable()` called
7. **Shutdown** - `plugin.shutdown()` for cleanup

### Plugin Priority

Plugins execute in priority order:
- **CRITICAL (0)** - Core systems (state, I/O)
- **HIGH (10)** - Game logic (combat, items)
- **NORMAL (50)** - Features (achievements, journal)
- **LOW (100)** - UI/UX (tutorial, accessibility)

### Creating a Plugin

See `PLUGIN_GUIDE.md` for detailed examples.

## Event-Driven Communication

### Why Events?

**Before (Tight Coupling):**
```python
class Engine:
    def move(self):
        # Directly call all systems
        self.achievements.track_movement()
        self.journal.log_movement()
        self.tutorial.check_hints()
        self.npc.update_context()
        # Adding features requires modifying Engine
```

**After (Loose Coupling):**
```python
class Engine:
    def move(self):
        # Just publish event
        self.event_bus.publish('game.move', {'room': new_room})
        # Plugins handle it independently
```

### Event Flow Example

```
Player Command "go north"
         ↓
[Engine processes command]
         ↓
engine.event_bus.publish('game.move', {data})
         ↓
    ┌────┴────┬────────┬─────────┬─────────┐
    ↓         ↓        ↓         ↓         ↓
 Journal  Achievement NPC    Tutorial Environment
  logs      tracks    updates  checks    updates
 movement   stats    context   hints     time
```

## Benefits of This Architecture

### 1. **Modularity**
- Each system is self-contained
- Can enable/disable features independently
- Clear boundaries and responsibilities

### 2. **Extensibility**
- Add new plugins without modifying core
- Third-party developers can extend
- Plugin dependencies managed automatically

### 3. **Maintainability**
- Small, focused modules
- Clear interfaces
- Easy to locate and fix bugs

### 4. **Testability**
- Mock services for unit tests
- Test plugins in isolation
- Inject test data easily

### 5. **Flexibility**
- Swap implementations (e.g., database vs file I/O)
- Different UIs use same engine
- Hot-reload plugins during development

## Migration from Old Architecture

The original monolithic `acs_engine.py` has been refactored:

**Old:**
- 1025 lines in single file
- Tight coupling between features
- Hard to test individual systems
- Difficult to add features

**New:**
- Core engine: ~250 lines
- Each plugin: ~200-400 lines
- Clear interfaces
- Easy to extend

## Next Steps

1. **Converting Existing Systems** - See `systems/` directory
2. **Creating New Plugins** - See `PLUGIN_GUIDE.md`
3. **UI Development** - See `ui/` directory
4. **Contributing** - See `CONTRIBUTING.md`

## Resources

- **API Documentation** - See docstrings in code
- **Plugin Examples** - See `systems/` directory
- **Configuration** - See `config/` directory
- **Testing** - See `tests/` directory
