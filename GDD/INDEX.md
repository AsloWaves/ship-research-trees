---
tags: [index, navigation, gdd]
---

# 🎮 Fathoms Deep - Game Design Document & Technical Reference
## Navigation Hub - START HERE

**Project**: Fathoms Deep - Tactical Naval MMO
**Version**: 0.3.0-alpha (Phase 3 Development)
**Engine**: Unity 6000.0.55f1 (2D/URP)
**Last Updated**: 2025-12-24

---

## 🚀 Quick Start

### New to the Project?
1. Read [[GDD-Overview]] - High-level vision
2. Check [[Development-Status]] - Current progress
3. Browse [[Implemented-Features]] - What's already built
4. Review [[Phase-2-InProgress]] - What we're working on

### Looking for Something Specific?
- **Design Documentation** → Browse sections below
- **Script Documentation** → [[SCRIPTS-INDEX]]
- **Implementation Guides** → [[Implementation-Guides/INDEX]]
- **Status Dashboards** → [[MOCs/Implemented-Features]]

---

## 📋 Documentation Sections

### 00 - Meta & Project Management
- [[00-Meta/GDD-Overview|GDD Overview]] - Core vision and goals
- [[00-Meta/Development-Status|Development Status]] - Current state
- [[00-Meta/Phase-1-Complete|Phase 1 Complete]] ✅ - Completed features
- [[00-Meta/Phase-2-InProgress|Phase 2 In Progress]] 🚧 - Current work
- [[00-Meta/Phase-3-Plan|Phase 3 Plan]] 📋 - Future roadmap

### 01 - Core Concepts
- [[01-Core-Concepts/Game-Vision|Game Vision]] - The player fantasy
- [[01-Core-Concepts/Target-Audience|Target Audience]] - Who we're building for
- [[01-Core-Concepts/Competitive-Positioning|Competitive Positioning]] - Market fit
- [[01-Core-Concepts/Extraction-Mechanics|Extraction Mechanics]] 📋 - Core loop
- [[01-Core-Concepts/Permadeath-System|Permadeath System]] 📋 - Risk/reward

### 02 - Core Gameplay
- [[02-Core-Gameplay/Ship-Physics|Ship Physics]] ✅ **IMPLEMENTED**
- [[02-Core-Gameplay/Camera-System|Camera System]] ✅ **IMPLEMENTED**
- [[02-Core-Gameplay/Inventory-System|Inventory System]] 📋 PLANNED
- [[02-Core-Gameplay/Mission-System|Mission System]] 📋 PLANNED
- [[02-Core-Gameplay/Mission-Examples|Mission Examples]] 📋 PLANNED
- [[02-Core-Gameplay/Crew-Management|Crew Management]] 📋 PLANNED
- [[02-Core-Gameplay/Crew-Progression|Crew Progression]] 📋 PLANNED
- [[02-Core-Gameplay/Crew-Permadeath|Crew Permadeath]] 📋 PLANNED
- [[02-Core-Gameplay/Crew-Skills|Crew Skills]] 📋 PLANNED
- [[02-Core-Gameplay/AI-NPC-System|AI & NPC System]] 📋 PLANNED

### 03 - Combat Systems
- [[03-Combat-Systems/Combat-Overview|Combat Overview]] 🚧 PARTIAL
- [[03-Combat-Systems/Firing-Solution-System|Firing Solution System]] ✅ **DOCUMENTED**
- [[03-Combat-Systems/Detection-System|Detection System]] ✅ **DOCUMENTED**
- [[03-Combat-Systems/Ballistics-Gunnery-Mechanics|Ballistics & Gunnery]] ✅ **DOCUMENTED**
- [[03-Combat-Systems/Surface-Combat|Surface Combat]] 📋 PLANNED
- [[03-Combat-Systems/Carrier-Operations|Carrier Operations]] 📋 PLANNED
- [[03-Combat-Systems/Submarine-Warfare|Submarine Warfare]] 📋 PLANNED
- [[03-Combat-Systems/Damage-Model|Damage Model]] 📋 PLANNED

### 04 - Ships (Research + Customization)
- [[04-Ships/USA/|USA Ships]] - 247 ships ✅ **RESEARCH DATA**
- [[04-Ships/Germany/|Germany Ships]] - 223 ships ✅ **RESEARCH DATA**
- [[04-Ships/Great-Britain/|Great Britain Ships]] - 188 ships ✅ **RESEARCH DATA**
- [[04-Ships/Japan/|Japan Ships]] - 160 ships ✅ **RESEARCH DATA**
- [[04-Ships/Module-System|Module System]] 📋 PLANNED
- [[04-Ships/Armor-Configuration|Armor Configuration]] 📋 PLANNED
- [[04-Ships/Ship-Fitting-UI|Ship Fitting UI]] 📋 PLANNED

### 05 - Aircraft (Research + Modules)
- [[05-Aircraft/USA/|USA Aircraft]] - 178 aircraft ✅ **RESEARCH DATA**
- [[05-Aircraft/Great-Britain/|Great Britain Aircraft]] - 92 aircraft ✅ **RESEARCH DATA**
- [[05-Aircraft/Japan/|Japan Aircraft]] - 88 aircraft ✅ **RESEARCH DATA**
- [[05-Aircraft/Germany/|Germany Aircraft]] - 75 aircraft ✅ **RESEARCH DATA**
- [[05-Aircraft/Research-Trees/|Research Trees]] 📋 PLANNED

### 06 - Weapons (Research + Modules)
- [[06-Weapons/Naval-Weapons/Naval-Guns/|Naval Guns]] - 372 guns, 2,857 turrets ✅ **RESEARCH DATA**
- [[06-Weapons/Naval-Weapons/Torpedoes/|Torpedoes]] - 234 torpedoes ✅ **RESEARCH DATA**
- [[06-Weapons/Naval-Weapons/Missiles/|Missiles]] - 202 missiles ✅ **RESEARCH DATA**
- [[06-Weapons/Naval-Weapons/Bombs/|Bombs]] - 107 bombs ✅ **RESEARCH DATA**
- [[06-Weapons/Aircraft-Weapons/|Aircraft Weapons]] ✅ **RESEARCH DATA**

### 07 - Economy & Trading
- [[07-Economy/Economy-Overview|Economy Overview]] 📋 PLANNED
- [[07-Economy/Trading-System|Trading System]] 📋 PLANNED
- [[07-Economy/Market-Dynamics|Market Dynamics]] 📋 PLANNED
- [[07-Economy/Resources/|Resources]] - 257 resource types ✅ **DESIGNED**

### 08 - UI Systems
- [[08-UI-Systems/UI-Overview|UI Overview]] ✅ **IMPLEMENTED**
- [[08-UI-Systems/Menu-System|Menu System]] ✅ **IMPLEMENTED**
- [[08-UI-Systems/Settings-Options|Settings & Options]] 📋 PLANNED
- [[08-UI-Systems/Controls|Controls Reference]] 📋 PLANNED
- [[08-UI-Systems/HUD-Design|HUD Design]] 🚧 PARTIAL
- [[08-UI-Systems/Accessibility|Accessibility]] ✅ **IMPLEMENTED** (WCAG 2.1 AA)

### 09 - Multiplayer & Networking
- [[09-Multiplayer/Network-Architecture|Network Architecture]] ✅ **IMPLEMENTED**
- [[09-Multiplayer/Authentication|Authentication]] ✅ **IMPLEMENTED** (JWT)
- [[09-Multiplayer/Chat-System|Chat System]] ✅ **IMPLEMENTED**
- [[09-Multiplayer/Squadron-Guild-System|Squadron & Guild System]] 📋 PLANNED
- [[09-Multiplayer/Save-Reconnection|Save & Reconnection]] 📋 PLANNED
- [[09-Multiplayer/Scalability-Plan|Scalability Plan]] 📋 PLANNED (300+ players)

### 10 - World Design
- [[10-World-Design/Ocean-Environment|Ocean Environment]] ✅ **IMPLEMENTED**
- [[10-World-Design/Biome-System|Biome System]] ✅ **IMPLEMENTED**
- [[10-World-Design/Zone-System|Zone System]] 📋 PLANNED (T1-T10 tiers)
- [[10-World-Design/Port-Locations|Port Locations]] 📋 PLANNED
- [[10-World-Design/Map-Layout|Map Layout]] 📋 PLANNED
- [[10-World-Design/Weather-System|Weather System]] 📋 PLANNED

### 11 - Factions & Nations
- [[11-Factions/Nation-Overview|Nation Overview]] 📋 PLANNED
- [[11-Factions/Reputation-System|Reputation System]] 📋 PLANNED
- [[11-Factions/Diplomacy-States|Diplomacy States]] 📋 PLANNED
- [[11-Factions/Faction-Missions|Faction Missions]] 📋 PLANNED

### 12 - Progression & Research
- [[12-Progression/Player-Progression|Player Progression]] 📋 PLANNED
- [[12-Progression/Ship-Unlocks|Ship Unlocks]] 📋 PLANNED
- [[12-Progression/Research-Trees|Research Trees]] 📋 DESIGNED
- [[12-Progression/Account-System|Account System]] ✅ **IMPLEMENTED**

### 13 - Technical Documentation
- [[13-Technical/Tech-Stack|Tech Stack]] ✅ **DOCUMENTED**
- [[13-Technical/Performance-Targets|Performance Targets]] 📋 PLANNED
- [[13-Technical/Database-Schema|Database Schema]] 🚧 PARTIAL
- [[13-Technical/API-Endpoints|API Endpoints]] 🚧 PARTIAL
- [[13-Technical/Network-Protocol|Network Protocol]] ✅ **DOCUMENTED**

### 14 - Art & Audio
- [[14-Art-Audio/Visual-Design|Visual Design]] 📋 PLANNED
- [[14-Art-Audio/Audio-Design|Audio Design]] ⭕ NOT STARTED
- [[14-Art-Audio/Asset-Pipeline|Asset Pipeline]] 📋 PLANNED
- [[14-Art-Audio/Historical-Research|Historical Research]] ✅ **EXTENSIVE**

---

## 💻 Script Documentation

### Script Reference Library
**[[Scripts-Reference/SCRIPTS-INDEX|Complete Script Index]]** - All 21 C# scripts documented

#### Quick Links by Category
- **Camera**: [[SimpleCameraController]], [[CameraController]]
- **Player**: [[SimpleNavalController]], [[NetworkedNavalController]]
- **UI**: [[MenuManager]], [[LoginController]], [[JoinMenuController]], +10 more
- **Networking**: [[ServerConfig]], [[WOSEdgegapBootstrap]]
- **Chat**: [[ChatManager]]
- **Environment**: [[OceanChunkManager]]

---

## 📊 Status Dashboards (MOCs)

### Auto-Generated Reports
- [[MOCs/Implemented-Features|✅ Implemented Features]] - All completed systems
- [[MOCs/Planned-Features|📋 Planned Features]] - Future development
- [[MOCs/Phase-1-Features|Phase 1 Summary]] - Foundation complete
- [[MOCs/Script-to-GDD-Map|Script ↔ GDD Cross-Reference]]
- [[00-Meta/Script-GDD-Comparison|🔄 Script-GDD Comparison]] - Implementation gap analysis ✅ NEW

### System-Specific MOCs
- [[MOCs/Combat-Systems-MOC|Combat Systems Hub]] - All combat-related docs
- [[MOCs/UI-Systems-MOC|UI Systems Hub]] - All UI-related docs
- [[MOCs/Network-Systems-MOC|Network Systems Hub]] - All multiplayer docs

---

## 🛠️ Implementation Guides

- [[Implementation-Guides/Adding-New-Ship|Adding a New Ship]]
- [[Implementation-Guides/Creating-Crew-Cards|Creating Crew Cards]]
- [[Implementation-Guides/Implementing-Weapons|Implementing Weapons]]
- [[Implementation-Guides/Setting-Up-Server|Setting Up Edgegap Server]]
- [[Implementation-Guides/Testing-Multiplayer|Testing Multiplayer Locally]]

---

## 🎨 Visual Diagrams (Canvas)

- [[Canvases/System-Architecture|System Architecture]] - How everything connects
- [[Canvases/Network-Architecture|Network Architecture]] - Client-server flow
- [[Canvases/UI-Flow|UI Flow]] - Menu navigation
- [[Canvases/Combat-Flow|Combat Flow]] - Combat sequence

---

## 🔍 Quick Search Tips

### By Status
- Search `status:implemented` - All completed features
- Search `status:planned` - All future features
- Search `status:partial` - In-progress work

### By Phase
- Search `phase:1` - Foundation (complete)
- Search `phase:2` - Combat & Economy (current)
- Search `phase:3` - Advanced features (future)

### By System
- Search `#physics` - Ship movement
- Search `#ui` - User interface
- Search `#network` - Multiplayer
- Search `#combat` - Combat systems
- Search `#script` - Code documentation

---

## 📈 Project Statistics

### Implementation Progress
- **Phase 1**: ✅ **COMPLETE** - Core systems functional
- **Phase 2**: 🚧 **IN PROGRESS** - Combat & economy
- **Phase 3**: 📋 **PLANNED** - Advanced features

### Code Status
- **Total Scripts**: 21 C# files (~180KB code)
- **Implemented Systems**: Camera, Physics, UI, Networking, Chat, Ocean
- **Lines of Code**: ~8,000-10,000 (estimated)

### Documentation Status
- **Design Docs**: Migrating from monolithic GDD
- **Script Docs**: In progress
- **Guides**: To be created
- **Diagrams**: To be created

---

## 🔗 External Resources

### Project Links
- **GitHub**: [AsloWaves/ship-research-trees](https://github.com/AsloWaves/ship-research-trees)
- **Unity Version**: 6000.0.55f1
- **Mirror Networking**: Documentation

### Ship & Weapon Research
- [[Ships/INDEX|Ship Database]] - Historical ship data
- [[Weapons/INDEX|Weapon Database]] - Historical weapons
- [[Aircraft/INDEX|Aircraft Database]] - Historical aircraft

### Module Database
- [[Modules/INDEX|Module Database]] - All ship modules
- [[Modules/Weapons/_Weapons-Overview|Weapons]] - Guns, torpedoes, missiles
- [[Modules/Engines/_Engines-Overview|Engines]] - Propulsion systems
- [[Modules/Sensors/_Sensors-Overview|Sensors]] - Radar, sonar, optics
- [[Modules/Fire-Control/_Fire-Control-Overview|Fire Control]] - Targeting systems
- [[Modules/Utilities/_Utilities-Overview|Utilities]] - Damage control, repair
- [[Modules/Aircraft/_Aircraft-Overview|Aircraft]] - Carrier operations
- [[Modules/Communications/_Communications-Overview|Communications]] - Radio, signals
- [[Modules/Auxiliary/_Auxiliary-Overview|Auxiliary]] - Generators, pumps

---

## 📝 Document Templates

Creating new documentation? Use these templates:
- [[Templates/Design-Document-Template|Design Document Template]]
- [[Templates/Script-Reference-Template|Script Reference Template]]
- [[Templates/Implementation-Guide-Template|Implementation Guide Template]]

---

## 🎯 Common Workflows

### I want to understand how [System] works
1. Find system in sections above
2. Read design doc (GDD folder)
3. Check script references (Scripts-Reference folder)
4. Review implementation guide if available

### I want to implement a new feature
1. Check if design doc exists
2. Review related implemented systems
3. Follow implementation guide
4. Update documentation when complete

### I want to see project status
1. Check [[Development-Status]]
2. Browse [[MOCs/Implemented-Features]]
3. Review current phase doc

---

**Last Updated**: 2025-12-24
**Maintained By**: Project lead + Claude Code
**Questions?** Start with the relevant section above or use Obsidian search
