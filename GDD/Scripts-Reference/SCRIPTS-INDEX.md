---
tags: [index, scripts, reference]
---

# 💻 Scripts Reference Index
## All Unity C# Scripts in Fathoms Deep Project

**Total Scripts**: 21 C# files
**Total Size**: ~180 KB
**Documentation Status**: ✅ **100% COMPLETE** (21/21 documented)
**Last Updated**: 2025-11-17

---

## 📊 Documentation Status

### ✅ Fully Documented (21/21 - 100%)
All scripts now have comprehensive reference documentation!

---

## 📁 Scripts by Category

### Camera (2 scripts) ✅ COMPLETE
- [[SimpleCameraController]] - Primary gameplay camera (multiplayer-aware) ✅
- [[CameraController]] - Advanced camera with shake effects ✅

**Purpose**: Tactical camera system with follow modes, zoom, and look-ahead

---

### Player / Ship Physics (2 scripts) ✅ COMPLETE
- [[SimpleNavalController]] - Single-player ship physics ✅
- [[NetworkedNavalController]] - Multiplayer ship physics with client prediction ✅

**Purpose**: Realistic naval physics with 8-speed throttle, turning circles, waypoint navigation

---

### UI - Menu Controllers (6 scripts) ✅ COMPLETE
- [[MenuManager]] - Menu panel management and navigation ✅
- [[MainMenuController]] - Main menu (Play, Options, Quit) ✅
- [[LoginController]] - Authentication with JWT ✅
- [[ConnectionMenuController]] - Connection panel (Host/Join routing) ✅
- [[JoinMenuController]] - Server browser and join ✅
- [[HostMenuController]] - Host server panel ✅
- [[InGameMenuController]] - Pause/ESC menu ✅
- [[OptionsMenuController]] - Settings menu (placeholder) ✅

**Purpose**: Complete menu navigation system with authentication

---

### UI - Utility & Accessibility (5 scripts) ✅ COMPLETE
- [[MenuKeyboardNavigation]] - WCAG 2.1 AA accessibility ✅
- [[ControlsHelpManager]] - F1 help panel ✅
- [[ShipDebugUI]] - Debug telemetry panel (legacy) ✅
- [[ShipDebugUIManager]] - Advanced 6-panel debug system ✅
- [[ReadOnlyTextField]] - Text field utility ✅

**Purpose**: Accessibility, debugging, and UI utilities

---

### Networking (2 scripts) ✅ COMPLETE
- [[ServerConfig]] - Edgegap server configuration ✅
- [[WOSEdgegapBootstrap]] - Server validation ✅

**Purpose**: Mirror networking + Edgegap deployment integration

---

### Chat (1 script) ✅ COMPLETE
- [[ChatManager]] - Server-authoritative chat system ✅

**Purpose**: Multiplayer text chat with spam protection and profanity filtering

---

### Environment (1 script) ✅ COMPLETE
- [[OceanChunkManager]] - Infinite ocean chunk system ✅

**Purpose**: Chunk-based ocean rendering with biome variations

---

## 🔍 Quick Search

### By Category
```dataview
TABLE
  file.folder as "Category",
  length(rows) as "Scripts"
FROM "Scripts-Reference"
WHERE script-type
GROUP BY file.folder
SORT file.folder ASC
```

### All Scripts Alphabetically
```dataview
TABLE
  size as "Size",
  namespace as "Namespace",
  status as "Status"
FROM "Scripts-Reference"
WHERE script-type
SORT file.name ASC
```

---

## 📊 Script Statistics

### By Size
- **Largest**: LoginController.md (31 KB) - NetworkedNavalController.md (35 KB)
- **Smallest**: ReadOnlyTextField.md, HostMenuController.md (~3-4 KB)
- **Average**: ~15-20 KB per script reference

### By Complexity
- **High Complexity**: NetworkedNavalController, SimpleNavalController, LoginController
- **Medium Complexity**: MenuManager, ChatManager, OceanChunkManager
- **Low Complexity**: ReadOnlyTextField, OptionsMenuController, MainMenuController

### By System
- **Core Gameplay**: 4 scripts (Camera × 2, Player × 2)
- **UI Systems**: 13 scripts (Menu controllers + utilities)
- **Networking**: 3 scripts (Server config, bootstrap, chat)
- **Environment**: 1 script (Ocean chunks)

---

## 🎯 Documentation Coverage by GDD Section

### Implemented Systems (100% Documented)
- **[[Ship-Physics]]**: SimpleNavalController ✅, NetworkedNavalController ✅
- **[[Camera-System]]**: SimpleCameraController ✅, CameraController ✅
- **[[UI-Overview]]**: 13 UI scripts ✅
- **[[Menu-System]]**: MenuManager ✅ + 7 menu controllers ✅
- **[[Network-Architecture]]**: ServerConfig ✅, WOSEdgegapBootstrap ✅
- **[[Chat-System]]**: ChatManager ✅
- **[[Authentication]]**: LoginController ✅
- **[[Ocean-Environment]]**: OceanChunkManager ✅

---

## 🔗 Related Documentation
- [[INDEX]] - Main GDD navigation
- [[Implemented-Features]] - What's working right now
- [[Development-Status]] - Overall project status
- [[13-Technical/Tech-Stack]] - Technology overview

---

## 📋 Documentation Quality Standards

Every script reference includes:
1. ✅ Quick reference (type, namespace, file path, size)
2. ✅ Purpose and role in the game
3. ✅ GDD features implemented
4. ✅ Key components (properties, methods, classes)
5. ✅ Configuration parameters (Inspector fields)
6. ✅ Integration points (dependencies, consumers)
7. ✅ Technical details (performance, algorithms)
8. ✅ Example usage with code snippets
9. ✅ Testing notes and edge cases
10. ✅ Related files and cross-references
11. ✅ Changelog

---

## 📝 Script Documentation Template

Creating new script documentation? Use [[Templates/Script-Reference-Template]]

**Standard Format**:
- Frontmatter with tags and metadata
- Quick reference section
- Purpose and GDD mapping
- Technical deep-dive
- Code examples
- Integration documentation
- Testing and changelog

---

## 🎉 Completion Status

### Documentation Progress
- **Phase 1 Scripts**: ✅ 21/21 COMPLETE (100%)
- **Phase 2 Scripts**: Not yet implemented
- **Phase 3 Scripts**: Not yet implemented

### Quality Metrics
- ✅ All scripts have comprehensive references
- ✅ Consistent template usage
- ✅ Proper cross-referencing
- ✅ Code examples throughout
- ✅ Performance notes included
- ✅ Testing coverage documented

---

## 📈 Usage Statistics

### Documentation Size
- **Total**: ~380 KB of script documentation
- **Average**: ~18 KB per script reference
- **Range**: 3 KB (smallest) to 35 KB (largest)

### Cross-References
- **Wiki Links**: 300+ cross-references to GDD docs
- **Backlinks**: Every script linked from design docs
- **Integration Mapping**: Complete dependency graphs

---

## 🚀 Next Steps

With all scripts documented:
- ✅ Complete reference for all Phase 1 code
- ✅ Foundation for Phase 2 development
- ✅ Onboarding documentation ready
- ✅ Maintenance documentation in place

**Future**: Document new scripts as Phase 2 features are implemented

---

**Status**: 🎉 **ALL SCRIPTS DOCUMENTED!** (21/21 - 100% Complete)
**Maintainer**: Updated automatically via Dataview
**Last Milestone**: 2025-11-17 - Complete documentation coverage achieved
