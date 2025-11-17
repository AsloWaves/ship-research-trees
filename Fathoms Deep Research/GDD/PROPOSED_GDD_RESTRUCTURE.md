# GDD Restructure Proposal - Obsidian Vault Architecture
## Moving from Monolithic MD to Interconnected Knowledge Graph

**Problem**: 7,357-line GDD is difficult to navigate, maintain, and query
**Solution**: Transform into Obsidian-powered knowledge vault with atomic notes and dynamic linking
**Timeline**: 2-4 hours to restructure, massive long-term benefits

---

## 🎯 Why Obsidian is Perfect for This

### You're Already Using It!
- `.obsidian/` folder exists in your repo
- Your ship research is already in MD format
- You understand the linking paradigm
- Graph view already valuable for ship relationships

### Key Advantages for GDD + Code Documentation:
1. **Bidirectional Linking** - `[[Ship Physics]]` automatically creates backlinks
2. **Graph View** - Visual map of how systems connect
3. **Tags** - Filter by `#implemented`, `#planned`, `#phase1`, `#combat-system`
4. **Dataview Queries** - Auto-generate status dashboards
5. **Canvas** - Visual system architecture diagrams
6. **Templates** - Standardized formats for design docs and script references
7. **Search** - Instant full-text search across all documents
8. **Git-Friendly** - Everything is still just MD files in version control

---

## 📂 Proposed Vault Structure

```
WOS2.3V2 Research/
├── .obsidian/                          # Obsidian config (already exists)
│
├── GDD/
│   ├── 📍 INDEX.md                     # Main navigation hub (YOU START HERE)
│   │
│   ├── 00-Meta/
│   │   ├── GDD-Overview.md             # High-level vision
│   │   ├── Development-Status.md       # Overall project status
│   │   ├── Phase-1-Complete.md         # Phase 1 retrospective
│   │   ├── Phase-2-InProgress.md       # Current phase tracking
│   │   └── Phase-3-Plan.md             # Future phase planning
│   │
│   ├── 01-Core-Concepts/
│   │   ├── Game-Vision.md              # Core fantasy and pillars
│   │   ├── Target-Audience.md          # Player demographics
│   │   ├── Competitive-Positioning.md  # Market analysis
│   │   ├── Extraction-Mechanics.md     # Core loop design
│   │   └── Permadeath-System.md        # Risk/reward tiers
│   │
│   ├── 02-Core-Gameplay/
│   │   ├── Ship-Physics.md             # ✅ IMPLEMENTED
│   │   ├── Ship-Controls.md            # ✅ IMPLEMENTED
│   │   ├── Navigation-System.md        # ✅ IMPLEMENTED
│   │   ├── Crew-Management.md          # 📋 PLANNED
│   │   ├── Crew-Progression.md         # 📋 PLANNED
│   │   ├── Crew-Permadeath.md          # 📋 PLANNED
│   │   └── Combat-Overview.md          # 🚧 PARTIAL
│   │
│   ├── 03-Combat-Systems/
│   │   ├── Surface-Combat.md           # 📋 PLANNED
│   │   ├── Carrier-Operations.md       # 📋 PLANNED
│   │   ├── Submarine-Warfare.md        # 📋 PLANNED
│   │   ├── Damage-Model.md             # 📋 PLANNED
│   │   ├── Ballistics-System.md        # 📋 PLANNED
│   │   └── Weapons-Overview.md         # Links to /Weapons/ folder
│   │
│   ├── 04-Ship-Customization/
│   │   ├── Module-System.md            # 📋 PLANNED (Tetris inventory)
│   │   ├── Armor-Configuration.md      # 📋 PLANNED
│   │   ├── Utility-Modules.md          # 📋 PLANNED
│   │   ├── Technology-Integration.md   # 📋 PLANNED
│   │   └── Ship-Fitting-UI.md          # 📋 PLANNED
│   │
│   ├── 05-UI-Systems/
│   │   ├── UI-Overview.md              # ✅ IMPLEMENTED
│   │   ├── Menu-System.md              # ✅ IMPLEMENTED
│   │   ├── HUD-Design.md               # 🚧 PARTIAL
│   │   ├── Inventory-UI.md             # 📋 PLANNED
│   │   ├── Ship-Fitting-Interface.md   # 📋 PLANNED
│   │   ├── Chat-UI.md                  # ✅ IMPLEMENTED
│   │   └── Accessibility.md            # ✅ IMPLEMENTED (WCAG 2.1 AA)
│   │
│   ├── 06-Multiplayer/
│   │   ├── Network-Architecture.md     # ✅ IMPLEMENTED (Mirror)
│   │   ├── Server-Config.md            # ✅ IMPLEMENTED (Edgegap)
│   │   ├── Client-Prediction.md        # ✅ IMPLEMENTED
│   │   ├── Authentication.md           # ✅ IMPLEMENTED (JWT)
│   │   ├── Chat-System.md              # ✅ IMPLEMENTED
│   │   └── Scalability-Plan.md         # 📋 PLANNED (300+ players)
│   │
│   ├── 07-Economy/
│   │   ├── Economy-Overview.md         # 📋 PLANNED
│   │   ├── Trading-System.md           # 📋 PLANNED
│   │   ├── Market-Dynamics.md          # 📋 PLANNED
│   │   ├── Currency-System.md          # 📋 PLANNED
│   │   └── Loot-Distribution.md        # 📋 PLANNED
│   │
│   ├── 08-World-Design/
│   │   ├── Ocean-Environment.md        # ✅ IMPLEMENTED (chunks)
│   │   ├── Biome-System.md             # ✅ IMPLEMENTED
│   │   ├── Zone-System.md              # 📋 PLANNED (T1-T10)
│   │   ├── Port-Locations.md           # 📋 PLANNED
│   │   ├── Map-Layout.md               # 📋 PLANNED
│   │   └── Weather-System.md           # 📋 PLANNED
│   │
│   ├── 09-Faction-System/
│   │   ├── Nation-Overview.md          # 📋 PLANNED
│   │   ├── Reputation-System.md        # 📋 PLANNED
│   │   ├── Diplomacy-States.md         # 📋 PLANNED
│   │   └── Faction-Missions.md         # 📋 PLANNED
│   │
│   ├── 10-Progression/
│   │   ├── Player-Progression.md       # 📋 PLANNED
│   │   ├── Ship-Unlocks.md             # 📋 PLANNED
│   │   ├── Research-Trees.md           # Links to ship research canvases
│   │   └── Account-System.md           # ✅ IMPLEMENTED
│   │
│   ├── 11-Technical/
│   │   ├── Tech-Stack.md               # ✅ DOCUMENTED
│   │   ├── Performance-Targets.md      # 📋 PLANNED
│   │   ├── Database-Schema.md          # 🚧 PARTIAL
│   │   └── API-Endpoints.md            # 🚧 PARTIAL
│   │
│   └── 12-Art-Audio/
│       ├── Visual-Design.md            # 📋 PLANNED
│       ├── Audio-Design.md             # 📋 PLANNED
│       ├── Asset-Pipeline.md           # 📋 PLANNED
│       └── Historical-Research.md      # ✅ EXTENSIVE (ship database)
│
├── Scripts-Reference/                  # NEW - Code documentation
│   ├── 📍 SCRIPTS-INDEX.md             # All scripts organized by category
│   │
│   ├── Camera/
│   │   ├── SimpleCameraController.md   # ✅ Detailed reference
│   │   └── CameraController.md         # ✅ Detailed reference
│   │
│   ├── Player/
│   │   ├── SimpleNavalController.md    # ✅ Detailed reference
│   │   └── NetworkedNavalController.md # ✅ Detailed reference
│   │
│   ├── UI/
│   │   ├── MenuManager.md
│   │   ├── LoginController.md
│   │   ├── JoinMenuController.md
│   │   ├── ShipDebugUI.md
│   │   └── [... 9 more UI scripts]
│   │
│   ├── Networking/
│   │   ├── ServerConfig.md
│   │   └── WOSEdgegapBootstrap.md
│   │
│   ├── Chat/
│   │   └── ChatManager.md
│   │
│   └── Environment/
│       └── OceanChunkManager.md
│
├── Implementation-Guides/               # NEW - How-to documentation
│   ├── Adding-New-Ship.md
│   ├── Creating-Crew-Cards.md
│   ├── Implementing-Weapons.md
│   ├── Setting-Up-Server.md
│   └── Testing-Multiplayer.md
│
├── Templates/                           # NEW - Standardized formats
│   ├── Design-Document-Template.md
│   ├── Script-Reference-Template.md
│   ├── Feature-Spec-Template.md
│   └── Implementation-Guide-Template.md
│
├── MOCs/                                # Maps of Content (navigation hubs)
│   ├── Implemented-Features.md         # Auto-generated list via Dataview
│   ├── Planned-Features.md             # Auto-generated list via Dataview
│   ├── Phase-1-Features.md             # Auto-generated list via Dataview
│   ├── Combat-Systems-MOC.md           # All combat-related notes
│   ├── UI-Systems-MOC.md               # All UI-related notes
│   └── Script-to-GDD-Map.md            # Links scripts to design docs
│
└── Canvases/                            # Visual diagrams
    ├── System-Architecture.canvas      # How all systems connect
    ├── Network-Architecture.canvas     # Client-server data flow
    ├── UI-Flow.canvas                  # Menu navigation
    └── Combat-Flow.canvas              # Combat sequence diagram
```

---

## 📝 Example Note Structure

### Design Document Example: `Ship-Physics.md`

```markdown
---
tags: [implemented, phase1, core-gameplay, physics]
status: ✅ IMPLEMENTED
phase: Phase 1
priority: HIGH
last-updated: 2025-01-15
---

# Ship Physics System

## Overview
Authentic naval physics simulation with realistic momentum, turning circles, and steerageway mechanics.

## Implementation Status
**Status**: ✅ IMPLEMENTED
**Phase**: Phase 1 Complete
**Scripts**: [[SimpleNavalController]], [[NetworkedNavalController]]

## Design Specification

### 8-Speed Throttle System
Ships use authentic naval throttle commands:
- **-4**: Full Astern (emergency reverse)
- **-2**: Half Astern
- **0**: All Stop
- **+2**: Half Ahead
- **+4**: Full Ahead

### Physics Calculations
- **Momentum**: Based on ship displacement and length
- **Turning Circles**: Speed-dependent turning effectiveness
- **Steerageway**: Minimum speed required for rudder control
- **Drag**: Realistic water resistance

## Technical Implementation

### Scripts
- [[SimpleNavalController]] - Single-player physics (30KB)
- [[NetworkedNavalController]] - Multiplayer physics with client prediction

### Key Features
- Frame-rate independent physics (FixedUpdate)
- Unity.Mathematics for performance
- ScriptableObject configuration (ShipConfigurationSO)
- Waypoint navigation system

### Configuration Parameters
```
Max Speed: 35 knots (configurable)
Acceleration: 2 m/s² (configurable)
Turn Rate: 15°/s at full speed (configurable)
Steerageway Threshold: 3 knots
```

## Integration Points
- **Camera**: [[SimpleCameraController]] follows ship velocity
- **UI**: [[ShipDebugUI]] displays speed/heading/throttle
- **Network**: [[NetworkedNavalController]] syncs position/rotation
- **Environment**: [[OceanChunkManager]] provides ocean depth

## Known Issues
- None currently

## Future Enhancements
- Weather affects ship handling
- Damage affects speed/turning
- Different sea states (calm/rough)

## Cross-References
- [[Navigation-System]] - Waypoint autopilot
- [[Ship-Controls]] - Input handling
- [[Combat-Overview]] - How physics affects combat

## Testing
- ✅ Single-player physics tested
- ✅ Multiplayer sync tested
- ✅ Waypoint navigation tested
- ⭕ Stress test with 300+ ships (pending)

## Changelog
- 2025-01-10: SimpleNavalController implemented
- 2025-01-12: NetworkedNavalController added
- 2025-01-15: Waypoint navigation complete
```

---

### Script Reference Example: `SimpleNavalController.md`

```markdown
---
tags: [script, physics, player, implemented]
script-type: MonoBehaviour
namespace: WOS.Player
file-path: WOS2.3V2 Research/Scripts/Player/SimpleNavalController.cs
status: ✅ IMPLEMENTED
---

# SimpleNavalController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Player
**File**: `Scripts/Player/SimpleNavalController.cs`
**Size**: 30,539 bytes
**Dependencies**: Unity.Mathematics, Input System, ShipConfigurationSO

## Purpose
Single-player naval physics controller with authentic ship handling characteristics. Handles throttle, steering, momentum, and waypoint navigation.

## Implements GDD Features
- [[Ship-Physics]] - Core physics calculations
- [[Ship-Controls]] - 8-speed throttle system
- [[Navigation-System]] - Waypoint autopilot

## Key Components

### Public Methods
- `SetThrottle(float)` - Set throttle (-4 to +4)
- `AddWaypoint(Vector3)` - Add navigation waypoint
- `GetShipStatus()` - Returns ShipStatus struct for UI

### Physics Methods
- `ApplyNavalPhysics()` - Main physics loop (FixedUpdate)
- `CalculateTurningEffectiveness(float speed)` - Speed-based turning
- `CalculateShipResponsiveness()` - Momentum calculations
- `ApplyRudderTurning()` - Rudder physics with steerageway

### Configuration
Uses ScriptableObject `ShipConfigurationSO` for:
- Max speed, acceleration, turn rate
- Ship dimensions (length, displacement)
- Drag coefficients

## Integration Points

### Used By
- [[SimpleCameraController]] - Camera follows ship
- [[ShipDebugUI]] - UI displays ship status
- Future combat systems

### Depends On
- Unity Input System - Keyboard/gamepad input
- Unity.Mathematics - High-performance math
- ShipConfigurationSO - Ship parameters

## Technical Notes

### Performance
- Updates in FixedUpdate (physics timestep)
- Uses Unity.Mathematics (Burst-compatible)
- Zero allocations per frame

### Network Compatibility
- This is the single-player version
- See [[NetworkedNavalController]] for multiplayer

## Example Usage
```csharp
SimpleNavalController ship = GetComponent<SimpleNavalController>();
ship.SetThrottle(4); // Full ahead
ship.AddWaypoint(new Vector3(100, 0, 0));
```

## Related Files
- [[NetworkedNavalController]] - Multiplayer version
- [[Ship-Physics]] - Design document
- ShipConfigurationSO.asset - Example config

## Changelog
- 2025-01-10: Initial implementation
- 2025-01-12: Added waypoint navigation
- 2025-01-15: Optimized physics calculations
```

---

## 🔍 Dataview Queries (Auto-Generated Dashboards)

### Implementation Status Dashboard
Create `MOCs/Implemented-Features.md`:

````markdown
# Implemented Features Dashboard

## ✅ Completed (Phase 1)
```dataview
TABLE status, phase, last-updated
FROM "GDD"
WHERE status = "✅ IMPLEMENTED"
SORT phase ASC
```

## 🚧 In Progress (Phase 2)
```dataview
TABLE status, priority, last-updated
FROM "GDD"
WHERE status = "🚧 PARTIAL"
SORT priority DESC
```

## 📋 Planned Features
```dataview
TABLE phase, priority
FROM "GDD"
WHERE status = "📋 PLANNED"
SORT phase ASC, priority DESC
```

## ⭕ Not Started
```dataview
TABLE priority
FROM "GDD"
WHERE status = "⭕ NOT STARTED"
SORT priority DESC
```
````

---

### Script-to-GDD Mapping
Create `MOCs/Script-to-GDD-Map.md`:

````markdown
# Script to GDD Cross-Reference

## All Scripts
```dataview
TABLE
  file-path AS "Script",
  implements AS "Implements GDD Section",
  status
FROM "Scripts-Reference"
WHERE script-type
SORT implements ASC
```
````

---

## 🏷️ Tagging Strategy

### Status Tags
- `#implemented` - Fully built and tested
- `#partial` - Partially implemented
- `#planned` - Designed but not built
- `#not-started` - No work done yet

### Phase Tags
- `#phase1` - Core systems (COMPLETE)
- `#phase2` - Combat & economy (IN PROGRESS)
- `#phase3` - Advanced features (PLANNED)

### System Tags
- `#physics` - Ship physics and movement
- `#ui` - User interface systems
- `#network` - Multiplayer/networking
- `#combat` - Combat systems
- `#economy` - Trading/economy
- `#crew` - Crew management

### Type Tags
- `#design-doc` - Design specifications
- `#script` - Code documentation
- `#guide` - Implementation how-to
- `#reference` - Quick reference material

---

## 🎨 Templates

### Design Document Template
`Templates/Design-Document-Template.md`:

```markdown
---
tags: [STATUS, PHASE, SYSTEM]
status: [✅ IMPLEMENTED | 🚧 PARTIAL | 📋 PLANNED | ⭕ NOT STARTED]
phase: [Phase 1 | Phase 2 | Phase 3]
priority: [HIGH | MEDIUM | LOW]
last-updated: YYYY-MM-DD
---

# [Feature Name]

## Overview
Brief description of what this feature does and why it exists.

## Implementation Status
**Status**:
**Phase**:
**Scripts**: [[Script1]], [[Script2]]

## Design Specification
Detailed design description without code.

## Technical Implementation
How it's actually built (if implemented).

## Integration Points
- **Depends On**: [[Other System]]
- **Used By**: [[Another System]]

## Known Issues
List any bugs or limitations.

## Future Enhancements
Planned improvements.

## Cross-References
- [[Related Feature 1]]
- [[Related Feature 2]]

## Testing
Test status and results.

## Changelog
Date-based change log.
```

---

## 🚀 Migration Strategy

### Phase 1: Create Structure (1 hour)
1. Create folder structure in `WOS2.3V2 Research/`
2. Create templates
3. Create INDEX.md files
4. Set up Dataview queries

### Phase 2: Migrate Implemented Systems (1 hour)
1. Split out implemented sections first:
   - Ship Physics → `Ship-Physics.md` + `SimpleNavalController.md`
   - Camera → `Camera-System.md` + both camera scripts
   - UI System → `UI-Overview.md` + all UI scripts
   - Networking → `Network-Architecture.md` + network scripts
   - Ocean → `Ocean-Environment.md` + `OceanChunkManager.md`
   - Chat → `Chat-System.md` + `ChatManager.md`

### Phase 3: Migrate Design Sections (1 hour)
2. Split out planned systems:
   - Crew Management → separate files
   - Combat Systems → separate files
   - Economy → separate files
   - Etc.

### Phase 4: Create Cross-Links (30 min)
3. Add [[wiki links]] throughout
4. Create MOC dashboards
5. Test Dataview queries

### Phase 5: Create Canvases (30 min)
6. System Architecture canvas
7. Network flow canvas
8. UI flow canvas

---

## ✅ Benefits of This Approach

### For You (Solo Developer)
- **Find things fast**: Search across all docs instantly
- **See connections**: Graph view shows how systems relate
- **Track progress**: Dataview dashboards show what's done
- **Stay organized**: Atomic notes prevent overwhelming docs
- **Version control**: Still just MD files in git

### For Future Team Members
- **Onboarding**: Start at INDEX.md, explore what interests them
- **Context**: Backlinks show how their work affects other systems
- **Standards**: Templates ensure consistency
- **Discovery**: Graph view reveals system relationships

### For Project Management
- **Status tracking**: Dataview queries show progress automatically
- **Prioritization**: Tag-based filtering shows what's urgent
- **Planning**: Clear view of what's done vs. planned
- **Documentation**: Always up-to-date (living documents)

---

## 🆚 Alternatives Considered

### Option 2: Notion Database
**Pros**: Queryable, collaborative, beautiful UI
**Cons**: Not in git, requires internet, vendor lock-in, costs money
**Verdict**: ❌ Not recommended for solo dev with git workflow

### Option 3: Docusaurus Website
**Pros**: Beautiful docs site, searchable, versioned
**Cons**: Build step required, overkill for internal docs, harder to edit
**Verdict**: 🤔 Maybe for public documentation later

### Option 4: Wiki.js or GitBook
**Pros**: Nice UI, git integration, searchable
**Cons**: Server required, complexity, overkill
**Verdict**: ❌ Too much overhead

### Option 5: Keep Single MD
**Pros**: Simple, no setup
**Cons**: Already unmanageable at 7,357 lines, will only get worse
**Verdict**: ❌ Does not scale

---

## 🎯 Recommendation

**Use Obsidian Vault Structure** because:
1. ✅ You're already using Obsidian
2. ✅ Git-friendly (just MD files)
3. ✅ Powerful linking and search
4. ✅ Dataview for queries
5. ✅ Canvas for visual diagrams
6. ✅ Zero vendor lock-in
7. ✅ Works offline
8. ✅ Free and fast

---

## 📊 Success Metrics

After migration, you should be able to:
- [ ] Find any script's documentation in <10 seconds
- [ ] See all implemented features with one Dataview query
- [ ] Understand system relationships via graph view
- [ ] Navigate from design doc to script and back via links
- [ ] Generate status reports automatically
- [ ] Onboard a new developer in <1 hour
- [ ] Never lose track of what's planned vs. built

---

*Ready to proceed with migration? Or would you like to discuss alternatives?*
