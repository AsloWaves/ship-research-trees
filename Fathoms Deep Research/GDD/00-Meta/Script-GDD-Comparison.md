---
tags: [meta, comparison, implementation-status, scripts]
status: 🔄 LIVING DOCUMENT
last-updated: 2025-12-11
related: [[Phase-2-InProgress]], [[TODO]], [[INDEX]]
---

# Script-to-GDD Comparison & Gap Analysis
## WOS2.3_V2 Implementation Status vs GDD Design

**Purpose**: Track implementation progress of GDD-documented mechanics in the Unity codebase
**Script Location**: `C:\WOS2.3_V2\Assets\Scripts\`
**Total Scripts**: ~170 C# files

---

## Quick Status Dashboard

| System Category | GDD Status | Script Status | Gap Level |
|-----------------|------------|---------------|-----------|
| **Ship Physics** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Camera System** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Crew Management** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Tetris Inventory** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Research/Unlock** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **UI/Menus** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Authentication** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Chat System** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Networking** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Voice Chat** | ✅ Documented | ✅ Implemented | ✅ ALIGNED |
| **Surface Combat** | ✅ Documented | 🚧 Partial | ⚠️ GAP |
| **Damage Model** | ✅ Documented | 📋 Planned | ❌ MISSING |
| **Carrier Operations** | ✅ Documented | 📋 Planned | ❌ MISSING |
| **Submarine Warfare** | ✅ Documented | 📋 Planned | ❌ MISSING |
| **Economy/Trading** | ✅ Documented | 🚧 Foundation | ⚠️ GAP |
| **Permadeath** | ✅ Documented | 📋 Planned | ❌ MISSING |
| **Mission System** | ✅ Documented | 📋 Planned | ❌ MISSING |
| **Faction/Nations** | ✅ Documented | 🚧 Foundation | ⚠️ GAP |

---

## SECTION 1: FULLY IMPLEMENTED SYSTEMS

### 1.1 Crew Management System ✅

**GDD Document**: [[Crew-Management]], [[Crew-Progression]], [[Crew-Module-Mechanics]]

**Script Implementation**: `Assets/Scripts/Player/CrewManager.cs` (807 lines)

| GDD Feature | Script Implementation | Status |
|-------------|----------------------|--------|
| Navy Field-style crew cards | `CrewCard` class with full data model | ✅ Complete |
| Crew assignment to positions | `CmdAssignCrew()`, `CmdUnassignCrew()` | ✅ Complete |
| Classification validation | `ValidateCrewAssignment()` checks classification match | ✅ Complete |
| Level requirements | Min level check in validation | ✅ Complete |
| Weight-based constraints | `CrewWeight` calculation, ship weight limit check | ✅ Complete |
| XP progression system | `AddCombatXP()`, `CrewXPCalculator` | ✅ Complete |
| Level-up mechanics | `AddXP()` returns levels gained, `RecalculateStats()` | ✅ Complete |
| Sailor casualties | `ApplyCombatCasualties()`, tier-based rates | ✅ Complete |
| Crew recruitment | `CmdRecruitCrew()` with credit cost | ✅ Complete |
| PlayFab persistence | `SaveCrewCardsToPlayFab()`, `LoadCrewCardsFromPlayFab()` | ✅ Complete |

**Supporting Scripts**:
- `Assets/Scripts/Player/Data/CrewData.cs` - CrewCard data structure
- `Assets/Scripts/Networking/Managers/PlayFabCrewService.cs` - Backend persistence

**Alignment Notes**: Script implementation closely follows GDD specifications. Crew weight, classification system, and XP formulas match documented design.

---

### 1.2 Tetris Inventory System ✅

**GDD Document**: [[Tetris-Fitting-Mechanics]], [[Inventory-System]]

**Script Implementation**: `Assets/Scripts/Networking/Data/CargoGrid.cs` (795 lines)

| GDD Feature | Script Implementation | Status |
|-------------|----------------------|--------|
| 2D grid storage | `Cells[y][x]` array, `Width`/`Height` properties | ✅ Complete |
| Item placement validation | `CanPlaceItem()` with bounds and collision check | ✅ Complete |
| Item rotation (0°, 90°, 180°, 270°) | `RotateItem()`, `RotateItemTo()`, `CanRotateItem()` | ✅ Complete |
| Auto-placement | `FindFirstAvailablePosition()`, `AutoPlaceItem()` | ✅ Complete |
| Auto-placement with rotation | `AutoPlaceItemWithRotation()` tries all rotations | ✅ Complete |
| Weight management | `GetTotalWeight()`, `CanAcceptWeight()`, `MaxWeight` | ✅ Complete |
| Item stacking | `MergeWithExistingStacks()`, `SplitStack()` | ✅ Complete |
| Grid compaction | `CompactGrid()` with largest-first algorithm | ✅ Complete |
| Inventory types | `InventoryType` enum: ShipCargo, PortWarehouse, Wallet, CrewQuarters | ✅ Complete |
| Item filtering | `GetEquipmentItems()`, `GetCargoItems()`, `GetCrewCards()` | ✅ Complete |

**Supporting Scripts**:
- `Assets/Scripts/Networking/Data/ItemData.cs` - Item data structure with Size, Position, Rotation
- `Assets/Scripts/Inventory/Core/ShipInventory.cs` - Ship-specific inventory
- `Assets/Scripts/Inventory/Core/PortInventory.cs` - Port storage
- `Assets/Scripts/Inventory/Core/WalletInventory.cs` - Container items

**Alignment Notes**: Excellent alignment with GDD. Implements EFT-style Tetris grid as specified. Weight system matches documented formulas.

---

### 1.3 Research & Unlock System ✅

**GDD Document**: [[Research-Unlock-System]]

**Script Implementation**: `Assets/Scripts/Networking/Managers/ResearchManager.cs` (449 lines)

| GDD Feature | Script Implementation | Status |
|-------------|----------------------|--------|
| Research progress tracking | `ResearchProgressData`, `playerResearchProgress` cache | ✅ Complete |
| Start/complete/cancel research | `CmdStartResearch()`, `CmdCompleteResearch()`, `CmdCancelResearch()` | ✅ Complete |
| Prerequisites validation | `PrerequisitesMet()` check | ✅ Complete |
| XP and credit costs | `CalculateXPCost()`, `CalculateCreditCost()` | ✅ Complete |
| Time-based completion | `completionTime`, `IsComplete()`, `GetTimeRemaining()` | ✅ Complete |
| Instant completion (premium) | `CmdInstantCompleteResearch()` with premium currency | ✅ Complete |
| Auto-completion processing | `ProcessAllCompletedResearch()` on timer | ✅ Complete |
| Unlock types | `UnlockType` enum: Ship, Turret, Engine, Module, Crew, Technology, Ability | ✅ Complete |
| Research slots | `CanStartResearch()` with max slots | ✅ Complete |

**Supporting Scripts**:
- `Assets/Scripts/Player/Data/ResearchProgressData.cs` - Research state data
- `Assets/Scripts/ScriptableObjects/Research/ResearchNodeSO.cs` - Research node definitions
- `Assets/Scripts/ScriptableObjects/Database/ResearchDatabaseSO.cs` - Research tree database

**Alignment Notes**: Implements War Thunder-style research as documented. Time-gated with premium acceleration option.

---

### 1.4 UI & Menu Systems ✅

**GDD Document**: [[UI-Overview]], [[Menu-System]]

**Script Implementation**: `Assets/Scripts/UI/` (20+ scripts)

| GDD Feature | Script Implementation | Status |
|-------------|----------------------|--------|
| Panel-based navigation | `MenuManager.cs` with history stack | ✅ Complete |
| Login/Registration | `LoginController.cs`, `RegisterController.cs` | ✅ Complete |
| Server browser | `JoinMenuController.cs` with Vercel/PlayFab discovery | ✅ Complete |
| In-game menu (ESC) | `InGameMenuController.cs` | ✅ Complete |
| Settings panels | `VoiceSettingsPanel.cs` (1745 lines!), `GraphicsSettingsPanel.cs` | ✅ Complete |
| Chat panel (7 tabs) | `ChatPanel.cs` - System, Proximity, World, Port, Party, Nation, Guild | ✅ Complete |
| Party panel | `PartyPanel.cs` with member list, kick, invite | ✅ Complete |
| Keyboard navigation (WCAG) | `MenuKeyboardNavigation.cs` | ✅ Complete |
| Controls help (F1) | `ControlsHelpManager.cs` | ✅ Complete |

**Alignment Notes**: UI implementation exceeds GDD documentation. Voice settings particularly comprehensive.

---

### 1.5 Networking & Multiplayer ✅

**GDD Document**: [[Network-Architecture]], [[Authentication]]

**Script Implementation**: `Assets/Scripts/Networking/` (25+ scripts)

| GDD Feature | Script Implementation | Status |
|-------------|----------------------|--------|
| Mirror framework | `WOSNetworkManager.cs` extends NetworkManager | ✅ Complete |
| Server-authoritative | All game logic uses `[Server]` attributes | ✅ Complete |
| PlayFab authentication | `AuthenticationManager.cs`, `PlayFabServerManager.cs` | ✅ Complete |
| JWT tokens | Handled via PlayFab session tickets | ✅ Complete |
| Server discovery | `VercelServerDiscovery.cs`, `PlayFabCloudScriptDiscovery.cs` | ✅ Complete |
| Health endpoints | `ServerHealthEndpoint.cs` | ✅ Complete |
| Account management | `AccountManager.cs` | ✅ Complete |
| Auto-save system | `AutoSaveSystem.cs` | ✅ Complete |

**Supporting Scripts**:
- `Assets/Scripts/Networking/Messages/InventoryMessages.cs` - Network message types
- `Assets/Scripts/Networking/ServerConfig.cs` - Server configuration
- `Assets/Scripts/Player/NetworkedNavalController.cs` - Networked ship control

---

### 1.6 Chat System ✅

**GDD Document**: [[Chat-System]]

**Script Implementation**: `Assets/Scripts/Chat/` (10 scripts)

| GDD Feature | Script Implementation | Status |
|-------------|----------------------|--------|
| Multi-channel chat | `ChatManager.cs` with 7 channels | ✅ Complete |
| Proximity chat | `ProximityDetector.cs` | ✅ Complete |
| Party chat | `PartyChatHandler.cs` | ✅ Complete |
| Port chat | `PortChatHandler.cs` | ✅ Complete |
| Chat commands | `ChatCommands.cs` (/roll, /help, etc.) | ✅ Complete |
| Mention system | `MentionSystem.cs` | ✅ Complete |
| Message history | `ChatHistory.cs` | ✅ Complete |
| System messages | `SystemMessageHandler.cs` | ✅ Complete |

---

### 1.7 Voice Chat ✅

**GDD Document**: Referenced in [[Chat-System]]

**Script Implementation**: `Assets/Scripts/Voice/` + `VoiceSettingsPanel.cs`

| Feature | Script Implementation | Status |
|---------|----------------------|--------|
| Odin SDK integration | Voice handlers via Odin | ✅ Complete |
| Push-to-talk | Configurable in settings | ✅ Complete |
| Voice activation | Alternative to PTT | ✅ Complete |
| 5 voice channels | Proximity, Party, Guild, Nation, Port | ✅ Complete |
| Per-channel volume | Individual volume controls | ✅ Complete |
| Noise suppression | Audio processing options | ✅ Complete |
| Echo cancellation | Audio processing options | ✅ Complete |
| Audio ducking | Reduces game audio during voice | ✅ Complete |
| Microphone test | Level indicator in settings | ✅ Complete |

---

## SECTION 2: PARTIALLY IMPLEMENTED SYSTEMS

### 2.1 Ship Equipment System 🚧

**GDD Document**: [[Module-System]], [[Module-Dependencies]]

**Script Implementation**: `Assets/Scripts/Player/ShipEquipmentManager.cs`

| GDD Feature | Script Status | Notes |
|-------------|---------------|-------|
| Equipment slots | 🚧 Partial | Basic structure exists |
| Module installation | 🚧 Partial | Needs time-based mechanics |
| Module-crew pairing | 🚧 Partial | Crew assignment exists separately |
| Hardpoint system | 📋 Planned | Visual 3D positioning not implemented |
| Quality variance (70-130%) | 📋 Planned | Not yet implemented |
| Installation/repair times | 📋 Planned | Not yet implemented |

**Supporting Scripts**:
- `Assets/Scripts/Player/Data/EquipmentData.cs` - Equipment data structure
- `Assets/Scripts/Player/Data/ShipLoadout.cs` - Ship loadout configuration

---

### 2.2 Nations/Factions 🚧

**GDD Document**: [[Nation-Overview]], [[Reputation-System]]

**Script Implementation**: `Assets/Scripts/Nations/` (2 scripts)

| GDD Feature | Script Status | Notes |
|-------------|---------------|-------|
| Nation data | ✅ Complete | `NationData.cs` |
| Nation manager | 🚧 Partial | `NationManager.cs` - basic structure |
| 4 playable nations | 📋 Planned | Data structures need population |
| Nation bonuses | 📋 Planned | Not implemented |
| Reputation system | 📋 Planned | Not implemented |
| Diplomatic states | 📋 Planned | Not implemented |

---

### 2.3 Party/Guild System 🚧

**GDD Document**: [[Squadron-Guild-System]]

**Script Implementation**: `Assets/Scripts/Party/`, `Assets/Scripts/Guild/`

| GDD Feature | Script Status | Notes |
|-------------|---------------|-------|
| Party creation | ✅ Complete | `PartyManager.cs` |
| Party data | ✅ Complete | `PartyData.cs` |
| Guild data | 🚧 Partial | `GuildData.cs` |
| Guild manager | 🚧 Partial | `GuildManager.cs` |
| Guild hierarchy | 📋 Planned | Not implemented |
| Shared resources | 📋 Planned | Not implemented |

---

### 2.4 Economy Foundation 🚧

**GDD Document**: [[Economy-Overview]], [[Market-Dynamics]]

**Script Implementation**: `Assets/Scripts/Economy/` (needs investigation)

| GDD Feature | Script Status | Notes |
|-------------|---------------|-------|
| Credits currency | 🚧 Partial | Basic structure |
| Wallet system | ✅ Complete | `WalletInventory.cs` |
| Trading UI | 🚧 Partial | UI foundation exists |
| Market dynamics | 📋 Planned | Not implemented |
| Resource Points | 📋 Planned | Not implemented |
| Black Market | 📋 Planned | Not implemented |

---

## SECTION 3: NOT YET IMPLEMENTED SYSTEMS

### 3.1 Combat Systems ❌

**GDD Document**: [[Combat-Overview]], [[Surface-Combat]], [[Damage-Model]]

| GDD Feature | Script Status | Priority |
|-------------|---------------|----------|
| Gunnery mechanics | ❌ Not implemented | HIGH |
| Projectile physics | ❌ Not implemented | HIGH |
| Damage calculation | ❌ Not implemented | HIGH |
| Armor penetration | ❌ Not implemented | HIGH |
| Fire/flooding | ❌ Not implemented | HIGH |
| Torpedo mechanics | ❌ Not implemented | MEDIUM |
| Detection system | ❌ Not implemented | MEDIUM |

---

### 3.2 Carrier Operations ❌

**GDD Document**: [[Carrier-Operations]]

| GDD Feature | Script Status | Priority |
|-------------|---------------|----------|
| Aircraft launch/recovery | ❌ Not implemented | MEDIUM |
| Wing management | ❌ Not implemented | MEDIUM |
| Air strikes | ❌ Not implemented | MEDIUM |
| CAP (Combat Air Patrol) | ❌ Not implemented | MEDIUM |

---

### 3.3 Submarine Warfare ❌

**GDD Document**: [[Submarine-Warfare]]

| GDD Feature | Script Status | Priority |
|-------------|---------------|----------|
| Depth mechanics | ❌ Not implemented | MEDIUM |
| Sonar systems | ❌ Not implemented | MEDIUM |
| Silent running | ❌ Not implemented | MEDIUM |
| Depth charges | ❌ Not implemented | MEDIUM |

---

### 3.4 Permadeath System ❌

**GDD Document**: [[Permadeath-System]], [[Crew-Permadeath]]

| GDD Feature | Script Status | Priority |
|-------------|---------------|----------|
| Ship permadeath (T6+) | ❌ Not implemented | HIGH |
| Crew card permadeath | ❌ Not implemented | HIGH |
| Tier-based risk rates | ❌ Not implemented | HIGH |
| Retrieval window | ❌ Not implemented | MEDIUM |

---

### 3.5 Mission System ❌

**GDD Document**: [[Mission-System]] (1812 lines of design!)

| GDD Feature | Script Status | Priority |
|-------------|---------------|----------|
| 17 mission categories | ❌ Not implemented | HIGH |
| Mission board | ❌ Not implemented | HIGH |
| Mission rewards | ❌ Not implemented | HIGH |
| Agent reputation | ❌ Not implemented | MEDIUM |
| Daily/weekly objectives | ❌ Not implemented | MEDIUM |

---

## SECTION 4: SCRIPT INVENTORY BY FOLDER

### Player Scripts (9 files)
```
Assets/Scripts/Player/
├── CrewManager.cs              ✅ Complete (807 lines)
├── NetworkedNavalController.cs ✅ Complete
├── PlayerShipManager.cs        🚧 Partial
├── ShipEquipmentManager.cs     🚧 Partial
└── Data/
    ├── CrewData.cs             ✅ Complete
    ├── EquipmentData.cs        🚧 Partial
    ├── PlayerShipData.cs       🚧 Partial
    ├── ResearchProgressData.cs ✅ Complete
    └── ShipLoadout.cs          🚧 Partial
```

### Inventory Scripts (10 files)
```
Assets/Scripts/Inventory/
├── InventoryManager.cs         🚧 Partial
├── InventoryAPIService.cs      🚧 Partial
├── ItemDatabase.cs             ✅ Complete
├── LocalInventoryService.cs    🚧 Partial
├── Core/
│   ├── PortInventory.cs        ✅ Complete
│   ├── ShipInventory.cs        ✅ Complete
│   └── WalletInventory.cs      ✅ Complete
├── Items/
│   └── ItemDefinitionSO.cs     ✅ Complete
├── Networking/
│   └── InventoryNetworkBehaviour.cs 🚧 Partial
└── Testing/
    └── InventorySystemTest.cs  ✅ Complete
```

### Networking Scripts (25+ files)
```
Assets/Scripts/Networking/
├── Data/
│   ├── AuthenticationData.cs   ✅ Complete
│   ├── CargoGrid.cs            ✅ Complete (795 lines!)
│   ├── ItemData.cs             ✅ Complete
│   └── ItemDefinition.cs       ✅ Complete
├── Managers/
│   ├── AccountManager.cs       ✅ Complete
│   ├── AuthenticationManager.cs ✅ Complete
│   ├── AutoSaveSystem.cs       ✅ Complete
│   ├── PlayFabCrewService.cs   ✅ Complete
│   ├── PlayFabInventoryService.cs ✅ Complete
│   ├── PlayFabShipService.cs   🚧 Partial
│   ├── PlayFabSocialService.cs 🚧 Partial
│   ├── ResearchManager.cs      ✅ Complete (449 lines)
│   ├── ServerInventoryManager.cs 🚧 Partial
│   └── SocialDataManager.cs    🚧 Partial
├── WOSNetworkManager.cs        ✅ Complete
├── ServerConfig.cs             ✅ Complete
└── [+ 10 more files]
```

### UI Scripts (20+ files)
```
Assets/Scripts/UI/
├── MenuManager.cs              ✅ Complete
├── LoginController.cs          ✅ Complete
├── RegisterController.cs       ✅ Complete
├── JoinMenuController.cs       ✅ Complete
├── InGameMenuController.cs     ✅ Complete
├── OptionsMenuController.cs    ✅ Complete
├── ChatPanel.cs                ✅ Complete
├── PartyPanel.cs               ✅ Complete
├── VoiceSettingsPanel.cs       ✅ Complete (1745 lines!)
├── GraphicsSettingsPanel.cs    ✅ Complete
├── ControlsHelpManager.cs      ✅ Complete
└── [+ 10 more files]
```

### Chat Scripts (10 files)
```
Assets/Scripts/Chat/
├── ChatManager.cs              ✅ Complete
├── ChatCommands.cs             ✅ Complete
├── ChatHistory.cs              ✅ Complete
├── ChatMessage.cs              ✅ Complete
├── MentionSystem.cs            ✅ Complete
├── PartyChatHandler.cs         ✅ Complete
├── PortChatHandler.cs          ✅ Complete
├── ProximityDetector.cs        ✅ Complete
├── SystemMessageHandler.cs     ✅ Complete
└── ChatCommandMessage.cs       ✅ Complete
```

### Environment Scripts (15 files)
```
Assets/Scripts/Environment/
├── OceanChunkManager.cs        ✅ Complete
├── OceanTileController.cs      ✅ Complete
├── OceanTileColorBlender.cs    ✅ Complete
├── ShipWakeController.cs       ✅ Complete
├── WaveEffect.cs               ✅ Complete
├── WaveEffectSpawner.cs        ✅ Complete
├── HarborEffects.cs            ✅ Complete
├── EnvironmentLODManager.cs    ✅ Complete
└── [+ 7 more files]
```

---

## SECTION 5: PRIORITY GAP ANALYSIS

### Critical Gaps (Phase 2 Blockers)

1. **Combat System** - No gunnery, damage, or projectile mechanics
   - Blocks: Core gameplay loop
   - Estimate: Major development effort

2. **Permadeath Implementation** - Tier-based risk not coded
   - Blocks: Extraction gameplay tension
   - Estimate: Medium effort (logic exists in crew, needs ship)

3. **Mission System** - No mission framework
   - Blocks: Structured gameplay, progression
   - Estimate: Major development effort

### High Priority Gaps

4. **Module Installation Times** - Equipment manager needs time-based mechanics
5. **Quality Variance System** - 70-130% module quality not implemented
6. **Detection System** - Fog of war, radar, sonar mechanics

### Medium Priority Gaps

7. **Carrier Operations** - Aircraft subsystem
8. **Submarine Mechanics** - Depth and stealth
9. **Full Economy** - Market dynamics, trading routes
10. **Nation Bonuses** - Faction-specific mechanics

---

## SECTION 6: RECOMMENDATIONS

### Immediate Actions

1. **Review Module-System alignment** - ShipEquipmentManager.cs needs updates:
   - Add installation time mechanics
   - Add quality variance (70-130%)
   - Add repair time mechanics

2. **Implement Permadeath hooks** - CrewManager has casualty system, needs:
   - T6+ ship destruction triggers
   - Crew card permadeath rolls
   - Retrieval window timer

3. **Start Combat Foundation** - Create new scripts:
   - `DamageManager.cs` - HP and damage calculation
   - `ProjectileManager.cs` - Ballistics simulation
   - `GunneryController.cs` - Turret targeting

### Script Updates Needed

| Script | Update Required |
|--------|-----------------|
| `ShipEquipmentManager.cs` | Add installation times, quality variance |
| `CrewManager.cs` | Add permadeath integration |
| `NationManager.cs` | Add nation bonuses, reputation |
| `PlayerShipManager.cs` | Add tier-based permadeath |

---

## Changelog

- **2025-12-11**: Initial comparison document created from comprehensive codebase analysis
