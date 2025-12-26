---
tags: [index, scripts, reference]
---

# Scripts Reference Index
## All Unity C# Scripts in Fathoms Deep Project

**Total Scripts**: 151 C# files
**Total Size**: ~1.2 MB
**Documentation Status**: **100% COMPLETE** (151/151 documented)
**Last Updated**: 2025-12-20

---

## 📊 Documentation Status

### ✅ Fully Documented (84/84 - 100%)
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

### Networking System (12 scripts) ✅ COMPLETE
> **Feature Group**: `networking` | **UPDATED Phase 4**

#### Core Network Managers (4 scripts)
- [[WOSNetworkManager]] - Custom Mirror NetworkManager for WOS multiplayer ✅
- [[ServerConfig]] - Server address configuration with auto-switching (ScriptableObject) ✅
- [[PlayFabServerManager]] - PlayFab GSDK integration for dedicated servers ✅
- [[AuthenticationManager]] - Client-side PlayFab authentication ✅

#### PlayFab Services (3 scripts)
- [[PlayFabShipService]] - Ship collection persistence via PlayFab User Data API ✅
- [[PlayFabCrewService]] - Crew card persistence via PlayFab User Data API ✅
- [[PlayFabInventoryService]] - Inventory, port storage, wallet persistence ✅

#### Server Discovery (3 scripts)
- [[ServerBrowserManager]] - Secure server browser with health checks ✅
- [[VercelServerDiscovery]] - Vercel serverless server discovery ✅
- [[PlayFabCloudScriptDiscovery]] - Native CloudScript server discovery ✅

#### Data Classes (2 scripts)
- [[CargoGrid]] - Tetris-style inventory grid with O(1) collision detection ✅
- [[ItemData]] - Item instance data supporting equipment, cargo, containers, crew ✅

**Purpose**: Server-authoritative multiplayer with PlayFab MPS integration, session authentication, and persistent player data

**Key Features**:
- Server-authoritative networking (Mirror)
- PlayFab Multiplayer Servers (MPS) deployment
- Session ticket authentication
- Optimistic locking for data persistence
- Tetris-style inventory system
- Port warehouse and ship cargo management
- Player wallet and currency system
- Auto-switching between localhost and production

**Integration Flow**:
```
WOSNetworkManager (network orchestrator)
  ├─ AuthenticationManager (session validation)
  │    └─ PlayFab Client API (login/register)
  ├─ PlayFabServerManager (GSDK lifecycle)
  │    └─ PlayFab Server API (heartbeat, player tracking)
  └─ ServerConfig (address configuration)

PlayFab Services (data persistence)
  ├─ PlayFabShipService (ship collections)
  ├─ PlayFabCrewService (crew cards)
  └─ PlayFabInventoryService (cargo, loadouts, wallet)
       └─ CargoGrid + ItemData (inventory data structures)

Server Discovery
  ├─ ServerBrowserManager (server list + health)
  ├─ VercelServerDiscovery (Vercel API)
  └─ PlayFabCloudScriptDiscovery (CloudScript)
```

---

### Inventory System (14 scripts) ✅ COMPLETE
> **Feature Group**: `inventory` | **NEW in Phase 5**

#### Core Data Classes (6 scripts)
- [[InventoryManager]] - Client-side inventory orchestrator (Singleton) ✅
- [[ShipInventory]] - Ship cargo wrapper with performance penalties ✅
- [[PortInventory]] - Port warehouse with tier-based capacity ✅
- [[WalletInventory]] - Container inventory for wallets/chests ✅
- [[ItemDatabase]] - Runtime item definition manager (Singleton) ✅
- [[ItemDefinitionSO]] - ScriptableObject for item properties ✅

#### Validation (4 scripts)
- [[HardCapWeightManager]] - Ship cargo hard cap weight enforcement ✅
- [[SlotMatchingValidator]] - Equipment slot dimension/weight validation ✅
- [[IHardCapWeightSystem]] - Interface for hard cap weight system ✅
- [[ISlotMatchingValidator]] - Interface for slot matching validation ✅

#### Networking & Services (3 scripts)
- [[InventoryNetworkBehaviour]] - Mirror NetworkBehaviour for inventory sync ✅
- [[InventoryAPIService]] - Client-side REST API service ✅
- [[LocalInventoryService]] - Mock inventory service for testing ✅

#### Testing (1 script)
- [[InventorySystemTest]] - Comprehensive test suite (72 tests) ✅

**Purpose**: Complete inventory system with Tetris-style cargo grids, weight-based ship performance, tier-based port capacity, and container support

**Key Features**:
- Tetris-style cargo grid with O(1) collision detection
- Weight-based ship performance penalties (speed, turn, acceleration)
- Hard cap weight system (100% = cannot add or undock)
- Tier-based port warehouse capacity (T1-3: 500, T4-7: 750, T8-10: 1000 cells)
- Slot-matching validation for equipment (exact dimension match)
- Container system (wallets, chests) with 1-level nesting
- Currency operations and stack management
- Network synchronization via Mirror
- Mock service for offline testing

**GDD Specifications**:
| Feature | Specification |
|---------|---------------|
| Ship Speed at 100% Cargo | 0.7x multiplier |
| Ship Turn at 100% Cargo | 0.8x multiplier |
| Ship Accel at 100% Cargo | 0.6x multiplier |
| Hard Cap | Cannot exceed 100% weight |
| Crew Weight Formula | Sailor_Count × 0.1 × (1 + Level/100) |

**Integration Flow**:
```
InventoryManager (client orchestrator)
  ├─ ShipInventory (cargo wrapper)
  │    ├─ CargoGrid (Tetris grid)
  │    └─ HardCapWeightManager (weight enforcement)
  ├─ PortInventory (warehouse wrapper)
  │    └─ CargoGrid (no weight limit)
  └─ WalletInventory (container wrapper)
       └─ CargoGrid (nested grid)

InventoryNetworkBehaviour (Mirror sync)
  ├─ ServerInventoryManager (server-side)
  └─ PlayFabInventoryService (persistence)

Validation System
  ├─ SlotMatchingValidator (equipment slots)
  └─ HardCapWeightManager (cargo weight)
```

---

### Port System (15 scripts) ✅ COMPLETE
> **Feature Group**: `port` | **NEW in Phase 6**

#### Core (4 scripts)
- [[PortEnums]] - Nationality and PortPlayerState enums ✅
- [[PortSceneStateHolder]] - ScriptableObject for scene transition state persistence ✅
- [[PortDefinitionSO]] - Master port configuration (services, layout, tiers) ✅
- [[PortTransitionManager]] - Scene transitions with loading screen integration ✅

#### Ocean Scene (4 scripts)
- [[PortZoneManager]] - AoP/AoI zone management with buoy spawning ✅
- [[PortZoneTrigger]] - Individual zone trigger detection ✅
- [[PortBuoyLight]] - 2D light buoys with nationality-based animations ✅
- [[PortVisualStyleSO]] - Nationality-specific visual theming ✅

#### Harbor Scene (4 scripts)
- [[HarborSceneManager]] - Harbor setup from PortDefinitionSO ✅
- [[DockingSquareController]] - Individual dock trigger with occupancy ✅
- [[ExitZoneController]] - Harbor exit zone trigger ✅
- [[DockingSquareData]] - Dock configuration data structure ✅

#### Player & UI (3 scripts)
- [[PlayerPortStateController]] - Player state machine (Ocean→Harbor→Docked) ✅
- [[PortInteractionUI]] - Context-sensitive interaction prompts ✅
- [[FittingRestrictionManager]] - Equipment fitting port-only restrictions ✅

**Purpose**: Complete port system with ocean zones (AoP/AoI), harbor scenes, docking, and nationality-based theming

**Key Features**:
- Area of Protection (AoP) - Combat-free outer zone
- Area of Interaction (AoI) - Port entry zone
- SO-driven harbor configuration (single scene, multiple ports)
- Server-authoritative zone detection
- Auto-docking and undocking animations
- Loading screen integration for scene transitions
- Nationality-based visual theming (US, UK, Japan, Germany, Neutral)
- URP 2D lighting for buoys with animations

**State Machine Flow**:
```
Ocean_Normal → Ocean_InAoP → Ocean_InAoI
    ↓ (press E)
Harbor_Sailing → Harbor_InDockZone → Harbor_AutoDocking → Harbor_Docked
    ↓ (press E to undock)
Harbor_Undocking → Harbor_Sailing → Harbor_AtExitZone
    ↓ (press E)
Ocean_InAoI
```

**Integration Flow**:
```
PortZoneManager (ocean zones)
  ├─ PortZoneTrigger (zone detection)
  ├─ PortBuoyLight (visual indicators)
  └─ PortVisualStyleSO (nationality theming)

HarborSceneManager (harbor setup)
  ├─ DockingSquareController (dock triggers)
  ├─ ExitZoneController (exit trigger)
  └─ PortDefinitionSO (configuration)

PlayerPortStateController (player state)
  ├─ PortSceneStateHolder (state persistence)
  └─ PortTransitionManager (scene loading)

FittingRestrictionManager (fitting rules)
  └─ Port-only equipment modification
```

---

### Ships System (3 scripts) ✅ COMPLETE
> **Feature Group**: `ships` | **NEW in Phase 7**

#### ScriptableObjects (1 script)
- [[ShipDefinitionSO]] - Master ship configuration (stats, slots, armor, economics) ✅

#### Data Classes (1 script)
- [[ShipProgressionData]] - Comprehensive enums, data classes, armor system ✅

#### Controllers (1 script)
- [[FleetManager]] - Server-authoritative fleet management (NetworkBehaviour Singleton) ✅

**Purpose**: Complete ship progression system with 16 ship classes, 10 tiers, 7 nations, Navy Field-style armor, and permadeath mechanics

**Key Features**:
- 16 ship classes (Destroyer → Dreadnought, Carriers, Submarines, Support)
- 10 tiers (T1-T10) with scaling permadeath risk (0% → 40%)
- 7 nations (USN, RN, IJN, KM, MN, RM, VMF)
- 9-zone Navy Field-style armor (3 deck, 3 belt, 3 structural)
- 6 armor types (RHA, FaceHardened, KruppCemented, TerniSteel, DucolSteel, STS)
- Insurance system (levels 1-3 reduce permadeath risk by 25/50/75%)
- Turret and module slot configuration with crew requirements
- Tetris-style cargo grid per ship
- Server-authoritative fleet management
- Ship unlocking, purchasing, repair, and insurance

**GDD Specifications**:
| Feature | Specification |
|---------|---------------|
| Permadeath T1-T2 | 0% risk |
| Permadeath T3 | 5% risk |
| Permadeath T10 | 40% risk |
| Insurance Level 1 | 25% risk reduction, 60% refund |
| Insurance Level 2 | 50% risk reduction, 70% refund |
| Insurance Level 3 | 75% risk reduction, 80% refund |

**Integration Flow**:
```
ShipDefinitionSO (ship configuration)
  ├─ Identity (ID, name, icon, prefab)
  ├─ Classification (class, tier, nation)
  ├─ Physical (displacement, length, beam)
  ├─ Survivability (health, torpedo protection)
  ├─ ArmorConfiguration (9 zones)
  ├─ Mobility (speed, turning, rudder)
  ├─ Slots (turrets, modules, cargo)
  └─ Economics (prices, repair, insurance)

ShipProgressionData (enums & data classes)
  ├─ Enums (ShipClass, ShipTier, ShipNation, etc.)
  ├─ ShipInstanceData (individual ship state)
  ├─ PlayerFleet (player's ship collection)
  ├─ ArmorConfiguration (9-zone system)
  └─ ShipUpgrade (upgrade system)

FleetManager (server-authoritative)
  ├─ InitializeFleet() (grant starter ships)
  ├─ CmdUnlockShip() / CmdPurchaseShip()
  ├─ CmdSetActiveShip() (ship selection)
  ├─ ProcessShipDestruction() (permadeath)
  ├─ CmdRepairShip() (repair system)
  └─ CmdPurchaseInsurance() (insurance)
```

---

### Chat System (10 scripts) ✅ COMPLETE
> **Feature Group**: `chat` | **UPDATED Phase 9**

#### Core (1 script)
- [[ChatManager]] - Server-authoritative chat system with spam protection ✅

#### Data Classes (2 scripts)
- [[ChatMessage]] - Message struct with 7 channels and priority system ✅
- [[ChatCommandMessage]] - NetworkMessage for client→server chat ✅

#### Client Components (3 scripts)
- [[ChatHistory]] - Per-channel message storage with unread tracking ✅
- [[ChatCommands]] - Client-side /help, /clear, /roll commands ✅
- [[MentionSystem]] - @mention detection with regex and highlighting ✅

#### Chat Handlers (3 scripts)
- [[SystemMessageHandler]] - Join/leave/combat notifications ✅
- [[PartyChatHandler]] - Party-specific chat routing ✅
- [[PortChatHandler]] - Port-specific chat routing ✅

#### Detection (1 script)
- [[ChatProximityDetector]] - Physics2D proximity detection for chat ✅

**Purpose**: Complete multiplayer chat with channels, spam protection, profanity filtering, mentions, and server-authoritative routing

**Key Features**:
- 7 channels (World, Local, Proximity, Party, Port, Nation, System)
- Spam protection (3 messages/5 seconds, exponential backoff)
- Profanity filtering with configurable word list
- @mention detection with sound notifications
- /help, /clear, /roll commands with rate limiting
- Server-authoritative routing for party/port chat

---

### Voice System (6 scripts) ✅ COMPLETE
> **Feature Group**: `voice` | **NEW in Phase 9**

#### Core (2 scripts)
- [[OdinManager]] - Odin voice chat singleton and room management ✅
- [[VoiceNetworkHandler]] - Mirror NetworkBehaviour for voice synchronization ✅

#### Handlers (3 scripts)
- [[PartyVoiceHandler]] - Party voice room lifecycle management ✅
- [[ProximityVoiceHandler]] - 3D spatial proximity voice with falloff ✅
- [[VoiceChannelKeyHandler]] - PTT keybinds (V=proximity, B=party) ✅

#### Configuration (1 script)
- [[VoiceSettingsData]] - ScriptableObject for voice configuration ✅

**Purpose**: Odin-based voice chat with party and proximity channels, 3D spatial audio, and configurable PTT keybinds

**Key Features**:
- Push-to-talk (V=proximity, B=party)
- 3D spatial audio with distance falloff
- Party voice rooms (auto-join/leave)
- Configurable microphone device selection
- Volume controls and noise suppression

---

### Party System (2 scripts) ✅ COMPLETE
> **Feature Group**: `party` | **NEW in Phase 9**

- [[PartyData]] - Party data structures (4-player parties, roles, invitations) ✅
- [[PartyManager]] - Server-authoritative party management (NetworkBehaviour Singleton) ✅

**Purpose**: 4-player party system with invitations, roles, and voice integration

**Key Features**:
- 4-player party limit
- Leader and member roles
- Invitation system with 30s expiry
- Party voice channel integration
- Ready check system

---

### Guild System (2 scripts) ✅ COMPLETE
> **Feature Group**: `guild` | **NEW in Phase 9**

- [[GuildData]] - Guild data structures (ranks, permissions, treasury) ✅
- [[GuildManager]] - Server-authoritative guild management (NetworkBehaviour Singleton) ✅

**Purpose**: Guild system with ranks, permissions, treasury, and member management

**Key Features**:
- 6 guild ranks (Recruit → Fleet Admiral)
- 8 permission types
- Guild treasury with transaction history
- Promotion/demotion system
- Member limits by guild level

---

### Nations System (2 scripts) ✅ COMPLETE
> **Feature Group**: `nations` | **NEW in Phase 9**

- [[NationData]] - Nation data structures (7 nations, bonuses, reputation) ✅
- [[NationManager]] - Server-authoritative nation management (NetworkBehaviour Singleton) ✅

**Purpose**: 7-nation system with unique bonuses, reputation, and allegiance mechanics

**Key Features**:
- 7 nations (USN, RN, IJN, KM, MN, RM, VMF)
- Unique nation bonuses (speed, accuracy, armor, etc.)
- Reputation system (-100 to +100)
- Monthly allegiance changes
- Nation-specific tech trees

---

### Audio System (4 scripts) ✅ COMPLETE
> **Feature Group**: `audio` | **NEW in Phase 9**

- [[FMODAudioInitializer]] - FMOD system initialization singleton ✅
- [[FMODAudioDeviceManager]] - FMOD device enumeration and switching ✅
- [[FMODAudioSettings]] - Static utility for audio PlayerPrefs ✅
- [[WindowsAudioDeviceManager]] - Windows WASAPI fallback for device enumeration ✅

**Purpose**: FMOD audio integration with runtime device selection and settings persistence

**Key Features**:
- Runtime audio device switching
- FMOD Studio integration
- PlayerPrefs persistence for settings
- Windows WASAPI COM interop fallback
- Volume controls (Master, Music, SFX, Voice)

---

### Research System (4 scripts) ✅ COMPLETE
> **Feature Group**: `research` | **NEW in Phase 9**

#### ScriptableObjects (3 scripts)
- [[ResearchNodeSO]] - Individual research node definition ✅
- [[ResearchTreeSO]] - Tech tree container with tier progression ✅
- [[ResearchDatabaseSO]] - Master database with global settings ✅

#### Controllers (1 script)
- [[ResearchManager]] - Server-authoritative research management (NetworkBehaviour) ✅

**Purpose**: Tech tree research system with prerequisites, tiers, XP/credit costs, and premium features

**Key Features**:
- 10 tier progression system
- Prerequisites (AND/OR logic)
- XP and credit costs
- Free XP pool (5% of research XP)
- Premium instant research option
- Research slot management (3 base, +2 premium)
- Nation-specific tech trees

**Integration Flow**:
```
ResearchDatabaseSO (global configuration)
  ├─ ResearchTreeSO (nation trees)
  │    └─ ResearchNodeSO (individual nodes)
  └─ ResearchManager (server authority)
       ├─ CmdStartResearch()
       ├─ CmdCompleteResearch()
       ├─ CmdInstantCompleteResearch()
       └─ CmdCancelResearch()
```

---

### Moderation System (1 script) ✅ COMPLETE
> **Feature Group**: `moderation` | **NEW in Phase 9**

- [[ModerationManager]] - Server-authoritative moderation (mutes, bans, reports, chat logging) ✅

**Purpose**: Server-side moderation with mutes, bans, auto-mute, player reports, and chat logging

**Key Features**:
- Timed mute system with auto-unmute
- Account ban system
- Violation tracking with auto-mute threshold (3 violations)
- Chat logging with 24h retention
- Player report submission
- Server-authoritative (no client access to moderation state)

---

### Environment (13 scripts) ✅ COMPLETE
> **Feature Group**: `environment` | **UPDATED Phase 10**

#### Ocean System (4 scripts)
- [[OceanChunkManager]] - Infinite ocean chunk system ✅
- [[OceanTileController]] - Individual tile animation and culling ✅
- [[OceanTileColorBlender]] - Neighbor-based tile color blending ✅
- [[OceanColorForcer]] - Emergency color override debugging ✅

#### LOD & Performance (2 scripts)
- [[EnvironmentLODManager]] - Central LOD orchestration ✅
- [[OceanCullingDebugger]] - Runtime culling debug tool ✅
- [[OceanDebugQuickSetup]] - Quick fix for culling issues ✅

#### Wake Effects (4 scripts)
- [[ShipWakeController]] - Ship wake with particle velocity compensation ✅
- [[CustomWakeSpawner]] - Ship-specific wake spawning with pooling ✅
- [[CustomWakeParticle]] - Individual wake particle physics ✅
- [[SimpleWakeSprite]] - Simple sprite-based wake component ✅

#### Ambient Effects (3 scripts)
- [[WaveEffectSpawner]] - Ambient wave effect spawning ✅
- [[WaveEffect]] - Individual wave animation ✅
- [[HarborEffects]] - Harbor ambient effects with URP 2D lighting ✅

**Purpose**: Chunk-based ocean rendering with LOD, wake effects, and ambient environmental visuals

**Key Features**:
- Infinite ocean chunk spawning with camera-following
- Dynamic LOD based on frame performance
- Ship-specific wake effects using ship displacement/length/beam
- Object pooling for particle effects
- MaterialPropertyBlock for shader optimization
- URP 2D Light2D for harbor lighting
- Time of day cycle effects

---

### 🚢 Loading Screen System (5 scripts) ✅ COMPLETE
> **Feature Group**: `loading-screen` | **NEW in Phase 2**

- [[LoadingScreenManager]] - Core loading screen orchestrator (singleton) ✅
- [[LoadingScreenConfigSO]] - Configuration ScriptableObject ✅
- [[LoadingSpinnerController]] - Maritime-themed spinner animation ✅
- [[LoadingTipsController]] - Rotating tips with fade transitions ✅
- [[PortTransitionManager]] - Harbor/ocean scene transitions ✅

**Purpose**: Professional loading screen system with fade transitions, progress tracking, tips, and scene transition coordination

**Key Features**:
- Fade to/from black transitions
- Milestone-based progress bar animation
- Ocean chunk loading integration
- Rotating naval-themed tips
- Maritime spinner animation (ship wheel, compass)
- Ambient music and completion sounds
- ScriptableObject-based configuration

**Integration Flow**:
```
LoadingScreenManager (orchestrator)
  ├─ LoadingScreenConfigSO (settings)
  ├─ LoadingTipsController (tips display)
  ├─ LoadingSpinnerController (animation)
  └─ PortTransitionManager (scene coordination)
       └─ OceanChunkManager (chunk loading events)
```

---

### Combat System (14 scripts) COMPLETE
> **Feature Group**: `combat` | **NEW in Phase 3**

#### Controllers (6 scripts)
- [[WeaponController]] - Server-authoritative weapon management (NetworkBehaviour)
- [[TargetingSystem]] - Target acquisition, tracking, fire control (NetworkBehaviour)
- [[BallisticsCalculator]] - Trajectory and hit calculations (Static Class)
- [[ProjectileManager]] - Projectile spawning and physics (NetworkBehaviour Singleton)
- [[TurretRotator]] - Individual turret rotation control (MonoBehaviour)
- [[TorpedoController]] - Torpedo tube management (NetworkBehaviour)

#### Data Classes (3 scripts)
- [[WeaponData]] - Weapon enums and state structures
- [[BallisticsData]] - Ballistics constants and profiles
- [[CombatNetworkSerializers]] - Mirror network serializers

#### ScriptableObjects (3 scripts)
- [[WeaponDefinitionSO]] - Gun weapon configuration assets
- [[AmmunitionDefinitionSO]] - Shell/ammo type definitions
- [[TorpedoDefinitionSO]] - Torpedo weapon configuration

#### Visuals (2 scripts)
- [[ProjectileVisual]] - Client-side shell rendering
- [[TorpedoVisual]] - Client-side torpedo rendering

**Purpose**: Server-authoritative naval combat with realistic ballistics, armor penetration, and damage systems

**Key Features**:
- Server-authoritative projectile physics
- Realistic ballistics with gravity and drag
- Armor penetration mechanics (AP, HE, SAP)
- Ricochet and overpenetration simulation
- Fire and flooding damage effects
- Torpedo guidance systems (straight, homing, pattern)
- Crew efficiency modifiers
- Environmental conditions (weather, sea state)

**Integration Flow**:
```
WeaponController (ship weapon management)
  ├─ TargetingSystem (target lock/tracking)
  │    └─ BallisticsCalculator (firing solutions)
  ├─ TurretRotator (individual turret control)
  └─ ProjectileManager (projectile physics)
       ├─ ProjectileVisual (client rendering)
       └─ TorpedoVisual (torpedo rendering)

TorpedoController (torpedo management)
  └─ ProjectileManager.SpawnTorpedo()
```

**Data Flow**:
```
WeaponDefinitionSO → BallisticProfile → BallisticsCalculator
AmmunitionDefinitionSO → Damage modifiers → HitResult
TorpedoDefinitionSO → TorpedoController → ProjectileManager
```

---

### Crew System (2 scripts) ✅ COMPLETE
> **Feature Group**: `crew` | **NEW in Phase 8**

- [[CrewData]] - Crew member data structures, roles, and specializations ✅
- [[CrewController]] - Server-authoritative crew management (NetworkBehaviour) ✅

**Purpose**: Crew member management with roles, skills, and combat efficiency modifiers

**Key Features**:
- 8 crew roles (Captain, Executive Officer, Weapons, Navigation, Engineering, Medical, Damage Control, Aviation)
- 5 specializations per role
- Experience and leveling system (1-100)
- Efficiency modifiers affecting ship performance
- Fatigue and morale tracking
- Server-authoritative crew assignment

**Integration Flow**:
```
CrewData (enums & data classes)
  ├─ CrewRole (8 roles)
  ├─ CrewSpecialization (5 per role)
  ├─ CrewMember (individual crew)
  ├─ CrewAssignment (position assignment)
  └─ CrewRoster (ship roster)

CrewController (NetworkBehaviour)
  ├─ CmdAssignCrew()
  ├─ CmdTransferCrew()
  └─ CalculateEfficiency()
```

---

### Damage System (3 scripts) ✅ COMPLETE
> **Feature Group**: `damage` | **NEW in Phase 8**

- [[DamageData]] - Damage types, repair states, and damage model data ✅
- [[DamageController]] - Server-authoritative damage processing (NetworkBehaviour) ✅
- [[DamageModel]] - Ship compartment damage model (MonoBehaviour) ✅

**Purpose**: Comprehensive ship damage system with compartmentalized damage, fire, flooding, and repair mechanics

**Key Features**:
- 9 damage types (Kinetic, Explosive, Fire, Flooding, Collision, etc.)
- Compartmentalized damage model (19 compartments)
- Fire and flooding systems with spread mechanics
- Progressive system damage
- Damage control crew efficiency
- Server-authoritative damage processing

**Integration Flow**:
```
DamageData (enums & data classes)
  ├─ DamageType (9 types)
  ├─ CompartmentType (19 compartments)
  ├─ DamageState (health tracking)
  └─ RepairTask (repair queue)

DamageController (NetworkBehaviour)
  ├─ ApplyDamage()
  ├─ ProcessFireSpread()
  ├─ ProcessFlooding()
  └─ ProcessRepairs()

DamageModel (MonoBehaviour)
  ├─ Compartment configuration
  └─ Visual damage states
```

---

### Submarines System (3 scripts) ✅ COMPLETE
> **Feature Group**: `submarines` | **NEW in Phase 8**

- [[SubmarineData]] - Submarine-specific data structures and enums ✅
- [[SubmarineController]] - Server-authoritative submarine operations (NetworkBehaviour) ✅
- [[SonarSystem]] - Active/passive sonar detection (NetworkBehaviour) ✅

**Purpose**: Complete submarine simulation with depth control, oxygen management, and sonar detection

**Key Features**:
- 4 depth levels (Periscope, Shallow, Medium, Deep)
- Oxygen consumption and CO2 buildup
- Active and passive sonar modes
- Convergence zone detection (long-range)
- Layer depth effects on detection
- Battery management for silent running
- Torpedo tube management

**Integration Flow**:
```
SubmarineData (enums & data classes)
  ├─ SubmarineDepth (4 levels)
  ├─ SonarMode (Active, Passive, Off)
  ├─ SubmarineState (systems state)
  └─ OxygenState (life support)

SubmarineController (NetworkBehaviour)
  ├─ CmdSetDepth()
  ├─ UpdateOxygen()
  ├─ UpdateBattery()
  └─ CmdFireTorpedo()

SonarSystem (NetworkBehaviour)
  ├─ ProcessActiveSonar()
  ├─ ProcessPassiveSonar()
  └─ DetectContacts()
```

---

### Carriers System (2 scripts) ✅ COMPLETE
> **Feature Group**: `carriers` | **NEW in Phase 8**

- [[CarrierData]] - Aircraft, squadron, and air wing data structures ✅
- [[CarrierController]] - Server-authoritative carrier operations (NetworkBehaviour) ✅

**Purpose**: Aircraft carrier flight operations with squadrons, air wings, and strike coordination

**Key Features**:
- 10 aircraft types (Fighter, Dive Bomber, Torpedo Bomber, Scout, etc.)
- Squadron organization with missions
- Air wing management
- Flight deck operations (launch/recovery queues)
- Elevator systems for hangar access
- Strike coordination with 8 phases
- Weather effects on flight ops

**Integration Flow**:
```
CarrierData (enums & data classes)
  ├─ AircraftType (10 types)
  ├─ AircraftState (6 states)
  ├─ SquadronMission (7 missions)
  ├─ AirWing (wing organization)
  └─ FlightDeck (operations)

CarrierController (NetworkBehaviour)
  ├─ CmdLaunchAircraft()
  ├─ CmdRecoverAircraft()
  ├─ ProcessLaunchQueue()
  ├─ CoordinateStrike()
  └─ UpdateHangar()
```

---

### Modules System (5 scripts) ✅ COMPLETE
> **Feature Group**: `modules` | **NEW in Phase 8**

#### Data Classes (2 scripts)
- [[ModuleData]] - Module enums, categories, and data structures ✅
- [[ModuleNetworkSerializers]] - Custom Mirror network serializers ✅

#### Controllers (2 scripts)
- [[ModuleController]] - Server-authoritative module management (NetworkBehaviour Singleton) ✅
- [[GenericEquipmentMount]] - Visual equipment mounting (MonoBehaviour) ✅

#### ScriptableObjects (1 script)
- [[ModuleDefinitionSO]] - Module configuration ScriptableObject ✅

**Purpose**: Ship module system with 22 categories, quality tiers, stat modifiers, and upgrade progression

**Key Features**:
- 22 module categories (Engine, Radar, Sonar, Fire Control, etc.)
- 7 slot types (Engine, Turret, Electronics, Hull, Deck, Special, Consumable)
- 5 quality tiers (Standard 1.0x → Prototype 1.6x)
- 26 stat types with modifiers
- Active and conditional effects
- Upgrade levels (0-5)
- Custom network serializers for Mirror

**Quality Tier Multipliers**:
| Tier | Multiplier |
|------|------------|
| Standard | 1.0x |
| Improved | 1.15x |
| Advanced | 1.3x |
| Experimental | 1.45x |
| Prototype | 1.6x |

**Integration Flow**:
```
ModuleDefinitionSO (configuration)
  ├─ Base stats and requirements
  ├─ Stat modifiers
  └─ Effects (active/conditional)

ModuleController (NetworkBehaviour)
  ├─ CmdEquipModule()
  ├─ CmdUnequipModule()
  ├─ CmdUpgradeModule()
  └─ CalculateStatModifiers()

GenericEquipmentMount (visuals)
  └─ Turret/launcher mount rendering
```

---

### Economy System (4 scripts) ✅ COMPLETE
> **Feature Group**: `economy` | **NEW in Phase 8**

- [[EconomyData]] - Economy data structures (wallet, market, contracts, auctions) ✅
- [[MarketController]] - Server-authoritative market and trading (NetworkBehaviour Singleton) ✅
- [[ContractManager]] - Mission and contract system (NetworkBehaviour Singleton) ✅
- [[WalletManager]] - Player currency management (NetworkBehaviour Singleton) ✅

**Purpose**: Complete economy system with market trading, contracts, and combat rewards

**Key Features**:
- Wallet with transaction history
- Market prices with supply/demand dynamics (0.5x-2x)
- Player listings with fees (2% listing, 5% transaction)
- 18 contract objective types
- 5 contract difficulty tiers
- Combat rewards (0.5 credits/damage, 2x kill bonus)
- Rate limiting (60 transactions/min)

**Combat Reward Formula**:
```
baseReward = damage * 0.5
if (isKill) baseReward *= 2
tierMultiplier = 1 + (targetTier * 0.2)
finalReward = baseReward * tierMultiplier
```

**Integration Flow**:
```
EconomyData (data structures)
  ├─ PlayerWallet (currency, transactions)
  ├─ MarketData (prices, listings)
  └─ ContractData (objectives, rewards)

WalletManager (currency)
  ├─ AddCurrency() / DeductCurrency()
  ├─ Rate limiting
  └─ Combat rewards

MarketController (trading)
  ├─ CmdBuyItem() / CmdSellItem()
  ├─ Supply/demand price adjustment
  └─ Player listings

ContractManager (missions)
  ├─ GenerateContracts()
  ├─ CmdAcceptContract()
  └─ ProcessObjectiveProgress()
```

---

### Permadeath System (3 scripts) ✅ COMPLETE
> **Feature Group**: `permadeath` | **NEW in Phase 8**

- [[PermadeathData]] - Death penalty, insurance, and salvage data structures ✅
- [[ExtractionController]] - Server-authoritative extraction point management (NetworkBehaviour Singleton) ✅
- [[PermadeathManager]] - Death processing, insurance, salvage (NetworkBehaviour Singleton) ✅

**Purpose**: Permadeath system with risk zones, insurance, extraction, and salvage mechanics

**Key Features**:
- 6 risk zones (Safe → Hardcore with 0% → 100% penalties)
- 5 death types (Combat, Environmental, Scuttled, etc.)
- Insurance tiers (Basic 25% → Full 100%)
- Extraction points with cooldowns
- Salvageable wrecks with decay
- Respawn cooldowns
- Player death statistics

**Risk Zone Penalties**:
| Zone | Death Penalty |
|------|---------------|
| Safe | 0% |
| Low | 10% |
| Medium | 25% |
| High | 50% |
| Extreme | 75% |
| Hardcore | 100% |

**Integration Flow**:
```
PermadeathData (data structures)
  ├─ DeathPenalty (loss calculation)
  ├─ InsurancePolicy (coverage)
  ├─ SalvageableWreck (recovery)
  └─ RiskZoneConfig (zone settings)

PermadeathManager (death processing)
  ├─ ProcessDeath()
  ├─ ProcessInsuranceClaim()
  ├─ CreateSalvageableWreck()
  └─ CmdRequestRespawn()

ExtractionController (extraction)
  ├─ CmdRequestExtraction()
  ├─ UpdateExtractionProgress()
  └─ CalculateExtractionBonus()
```

---

### World System (3 scripts) ✅ COMPLETE
> **Feature Group**: `world` | **NEW in Phase 8**

- [[WorldData]] - Zone, faction, and weather data structures ✅
- [[ZoneManager]] - Server-authoritative zone management (NetworkBehaviour Singleton) ✅
- [[WeatherSystem]] - Server-authoritative weather simulation (NetworkBehaviour Singleton) ✅

**Purpose**: World systems including zones, faction control, and dynamic weather with combat effects

**Key Features**:
- 14 zone types (Port, Shipping, Combat, Resource, etc.)
- 6 danger levels with tier restrictions
- 12 factions with standing system (-3 to +3)
- Dynamic faction control (Neutral → Contested → Occupied)
- Weather conditions (9 types) with combat modifiers
- Sea states (Douglas scale 0-8)
- Time of day cycle (1 real min = 1 game hour)
- Zone events (10 event types)

**Weather Combat Modifiers**:
| Condition | Accuracy | Detection | Speed | Aircraft |
|-----------|----------|-----------|-------|----------|
| Clear | 100% | 100% | 100% | 100% |
| Storm | 70% | 15% | 88% | 20% |
| Hurricane | 55% | 5% | 79% | 0% |

**Integration Flow**:
```
WorldData (data structures)
  ├─ ZoneDefinition (zone config)
  ├─ FactionDefinition (faction config)
  ├─ ZoneWeatherState (weather effects)
  └─ ActiveZoneEvent (events)

ZoneManager (zones)
  ├─ CmdRequestZoneTransition()
  ├─ UpdateZoneControl()
  ├─ ReportCombatActivity()
  └─ StartZoneEvent()

WeatherSystem (weather)
  ├─ UpdateGameTime()
  ├─ UpdateWeather()
  ├─ GetAccuracyModifier()
  └─ GetAircraftModifier()
```

---

## Quick Search

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
- **Largest**: LoadingScreenManager.md (56 KB), NetworkedNavalController.md (35 KB)
- **Smallest**: ReadOnlyTextField.md, HostMenuController.md (~3-4 KB)
- **Average**: ~15-20 KB per script reference

### By Complexity
- **High Complexity**: NetworkedNavalController, SimpleNavalController, LoginController, LoadingScreenManager
- **Medium Complexity**: MenuManager, ChatManager, OceanChunkManager, PortTransitionManager
- **Low Complexity**: ReadOnlyTextField, OptionsMenuController, LoadingSpinnerController

### By System
- **Core Gameplay**: 4 scripts (Camera × 2, Player × 2)
- **Combat System**: 14 scripts (Controllers × 6, Data × 3, SOs × 3, Visuals × 2)
- **UI Systems**: 13 scripts (Menu controllers + utilities)
- **Loading Screen**: 5 scripts (Manager, Config, Tips, Spinner, Transitions)
- **Networking**: 12 scripts (Network managers × 4, PlayFab services × 3, Discovery × 3, Data × 2)
- **Inventory System**: 14 scripts (Core × 6, Validation × 4, Networking × 3, Testing × 1)
- **Port System**: 15 scripts (Core × 4, Ocean × 4, Harbor × 4, Player/UI × 3)
- **Ships System**: 3 scripts (ScriptableObjects × 1, Data × 1, Controllers × 1)
- **Crew System**: 2 scripts (Data × 1, Controllers × 1)
- **Damage System**: 3 scripts (Data × 1, Controllers × 1, Model × 1)
- **Submarines System**: 3 scripts (Data × 1, Controllers × 1, Sonar × 1)
- **Carriers System**: 2 scripts (Data × 1, Controllers × 1)
- **Modules System**: 5 scripts (Data × 2, Controllers × 2, SOs × 1)
- **Economy System**: 4 scripts (Data × 1, Controllers × 3)
- **Permadeath System**: 3 scripts (Data × 1, Controllers × 2)
- **World System**: 3 scripts (Data × 1, Controllers × 2)
- **Chat System**: 10 scripts (Core × 1, Data × 2, Client × 3, Handlers × 3, Detection × 1)
- **Voice System**: 6 scripts (Core × 2, Handlers × 3, Config × 1)
- **Party System**: 2 scripts (Data × 1, Controllers × 1)
- **Guild System**: 2 scripts (Data × 1, Controllers × 1)
- **Nations System**: 2 scripts (Data × 1, Controllers × 1)
- **Audio System**: 4 scripts (FMOD integration × 4)
- **Research System**: 4 scripts (ScriptableObjects × 3, Controllers × 1)
- **Moderation System**: 1 script (Server-side moderation)
- **Environment**: 13 scripts (Ocean × 4, LOD × 3, Wake × 4, Ambient × 3)

---

## 🎯 Documentation Coverage by GDD Section

### Implemented Systems (100% Documented)
- **[[Ship-Physics]]**: SimpleNavalController, NetworkedNavalController
- **[[Camera-System]]**: SimpleCameraController, CameraController
- **[[Surface-Combat]]**: WeaponController, TargetingSystem, BallisticsCalculator, ProjectileManager, TurretRotator
- **[[Submarine-Warfare]]**: TorpedoController, TorpedoDefinitionSO
- **Combat Data**: WeaponData, BallisticsData, CombatNetworkSerializers
- **Combat Assets**: WeaponDefinitionSO, AmmunitionDefinitionSO, TorpedoDefinitionSO
- **Combat Visuals**: ProjectileVisual, TorpedoVisual
- **[[UI-Overview]]**: 18 UI scripts (13 menu + 5 loading)
- **[[Menu-System]]**: MenuManager + 7 menu controllers
- **Loading Screen System**: LoadingScreenManager, LoadingScreenConfigSO, LoadingSpinnerController, LoadingTipsController, PortTransitionManager
- **[[Network-Architecture]]**: ServerConfig, WOSEdgegapBootstrap
- **[[Chat-System]]**: ChatManager
- **[[Authentication]]**: LoginController
- **[[Ocean-Environment]]**: OceanChunkManager
- **[[Inventory-System]]**: InventoryManager, ShipInventory, PortInventory, WalletInventory, ItemDatabase
- **[[Cargo-System]]**: CargoGrid, HardCapWeightManager, SlotMatchingValidator
- **[[Equipment-Slots]]**: SlotMatchingValidator, ISlotMatchingValidator
- **[[Port-Trading]]**: PortInventory, InventoryAPIService
- **[[Port-System]]**: PortZoneManager, HarborSceneManager, PlayerPortStateController, PortDefinitionSO
- **[[Port-Docking]]**: DockingSquareController, DockingSquareData, ExitZoneController
- **[[Port-Zones]]**: PortZoneTrigger, PortBuoyLight, PortVisualStyleSO
- **[[Scene-Transitions]]**: PortTransitionManager, PortSceneStateHolder
- **[[Fitting-Restrictions]]**: FittingRestrictionManager
- **[[Ship-Progression]]**: ShipDefinitionSO, ShipProgressionData, FleetManager
- **[[Ship-Classes]]**: ShipProgressionData (ShipClass, ShipTier, ShipNation enums)
- **[[Fleet-Management]]**: FleetManager (ship unlocking, purchasing, permadeath)
- **[[Armor-System]]**: ShipProgressionData (ArmorConfiguration, ArmorType, ArmorZoneType)
- **[[Permadeath]]**: FleetManager (ProcessShipDestruction, insurance system)

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

## Completion Status

### Documentation Progress
- **Phase 1 Scripts**: 21/21 COMPLETE (100%)
- **Phase 2 Scripts**: 5/5 COMPLETE (100%) - Loading Screen System
- **Phase 3 Scripts**: 14/14 COMPLETE (100%) - Combat System
- **Phase 4 Scripts**: 12/12 COMPLETE (100%) - Networking System
- **Phase 5 Scripts**: 14/14 COMPLETE (100%) - Inventory System
- **Phase 6 Scripts**: 15/15 COMPLETE (100%) - Port System
- **Phase 7 Scripts**: 3/3 COMPLETE (100%) - Ships System
- **Phase 8 Scripts**: 25/25 COMPLETE (100%) - Advanced Systems (Crew, Damage, Submarines, Carriers, Modules, Economy, Permadeath, World)
- **Phase 9 Scripts**: 30/30 COMPLETE (100%) - Social & Communication Systems (Voice, Party, Guild, Nations, Audio, Chat expansion, Research, Moderation)
- **Phase 10 Scripts**: 12/12 COMPLETE (100%) - Environment System Expansion (Ocean, LOD, Wake, Ambient)

### Quality Metrics
- ✅ All scripts have comprehensive references
- ✅ Consistent template usage
- ✅ Proper cross-referencing
- ✅ Code examples throughout
- ✅ Performance notes included
- ✅ Testing coverage documented
- ✅ Feature group tagging (`loading-screen`)

---

## 📈 Usage Statistics

### Documentation Size
- **Total**: ~620 KB of script documentation
- **Average**: ~16 KB per script reference
- **Range**: 3 KB (smallest) to 56 KB (largest)

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

**Status**: **ALL SCRIPTS DOCUMENTED!** (139/139 - 100% Complete)
**Maintainer**: Updated automatically via Dataview
**Last Milestone**: 2025-12-20 - Phase 9 Social & Communication Systems (30 scripts) documented

### Recent Additions
- **2025-12-20**: Added Phase 9 Social & Communication Systems documentation (30 scripts)
  - Voice System (6): OdinManager, VoiceNetworkHandler, PartyVoiceHandler, ProximityVoiceHandler, VoiceChannelKeyHandler, VoiceSettingsData
  - Party System (2): PartyData, PartyManager
  - Guild System (2): GuildData, GuildManager
  - Nations System (2): NationData, NationManager
  - Audio System (4): FMODAudioInitializer, FMODAudioDeviceManager, FMODAudioSettings, WindowsAudioDeviceManager
  - Chat Expansion (9): ChatMessage, ChatCommandMessage, ChatHistory, MentionSystem, SystemMessageHandler, PartyChatHandler, PortChatHandler, ChatCommands, ChatProximityDetector
  - Research System (4): ResearchNodeSO, ResearchTreeSO, ResearchDatabaseSO, ResearchManager
  - Moderation System (1): ModerationManager
- **2025-12-20**: Added Phase 8 Advanced Systems documentation (25 scripts)
  - Crew System (2): CrewData, CrewController
  - Damage System (3): DamageData, DamageController, DamageModel
  - Submarines System (3): SubmarineData, SubmarineController, SonarSystem
  - Carriers System (2): CarrierData, CarrierController
  - Modules System (5): ModuleData, ModuleNetworkSerializers, ModuleController, GenericEquipmentMount, ModuleDefinitionSO
  - Economy System (4): EconomyData, MarketController, ContractManager, WalletManager
  - Permadeath System (3): PermadeathData, ExtractionController, PermadeathManager
  - World System (3): WorldData, ZoneManager, WeatherSystem
- **2025-12-19**: Added Ships System documentation (3 scripts)
  - ScriptableObjects: ShipDefinitionSO (master ship configuration)
  - Data: ShipProgressionData (enums, data classes, armor system)
  - Controllers: FleetManager (fleet management, permadeath, insurance)
- **2025-12-19**: Added Port System documentation (15 scripts)
  - Core: PortEnums, PortSceneStateHolder, PortDefinitionSO, PortTransitionManager
  - Ocean: PortZoneManager, PortZoneTrigger, PortBuoyLight, PortVisualStyleSO
  - Harbor: HarborSceneManager, DockingSquareController, ExitZoneController, DockingSquareData
  - Player/UI: PlayerPortStateController, PortInteractionUI, FittingRestrictionManager
- **2025-12-19**: Added Inventory System documentation (14 scripts)
  - Core: InventoryManager, ShipInventory, PortInventory, WalletInventory, ItemDatabase, ItemDefinitionSO
  - Validation: HardCapWeightManager, SlotMatchingValidator, IHardCapWeightSystem, ISlotMatchingValidator
  - Networking: InventoryNetworkBehaviour, InventoryAPIService, LocalInventoryService
  - Testing: InventorySystemTest
- **2025-12-19**: Added Networking System documentation (12 scripts)
  - Core Managers: WOSNetworkManager, ServerConfig, PlayFabServerManager, AuthenticationManager
  - PlayFab Services: PlayFabShipService, PlayFabCrewService, PlayFabInventoryService
  - Server Discovery: ServerBrowserManager, VercelServerDiscovery, PlayFabCloudScriptDiscovery
  - Data Classes: CargoGrid, ItemData
- **2025-12-19**: Added Combat System documentation (14 scripts)
  - Controllers: WeaponController, TargetingSystem, BallisticsCalculator, ProjectileManager, TurretRotator, TorpedoController
  - Data: WeaponData, BallisticsData, CombatNetworkSerializers
  - ScriptableObjects: WeaponDefinitionSO, AmmunitionDefinitionSO, TorpedoDefinitionSO
  - Visuals: ProjectileVisual, TorpedoVisual
- **2025-12-19**: Added Loading Screen System documentation (5 scripts)
  - LoadingScreenManager.md - Core orchestrator
  - LoadingScreenConfigSO.md - Configuration asset
  - LoadingSpinnerController.md - Spinner animation
  - LoadingTipsController.md - Tips display
  - PortTransitionManager.md - Scene transitions
