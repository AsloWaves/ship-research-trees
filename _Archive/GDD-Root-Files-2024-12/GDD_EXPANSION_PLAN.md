# GDD Expansion & Clarification Plan
## WOS2.3 Project - Comprehensive Technical Documentation Enhancement

**Created**: 2025-11-17
**Purpose**: Systematically expand and clarify all GDD sections with script references and implementation details

---

## Expansion Objectives

### Primary Goals
1. **Script Integration**: Map every script to relevant GDD sections
2. **Technical Clarification**: Expand ambiguous technical descriptions with implementation details
3. **Implementation Status**: Add clear indicators of what's implemented vs. planned
4. **Developer Reference**: Create direct links between design and code
5. **Validation**: Ensure GDD accurately reflects current implementation

### What We're Adding to Each Section
- ✅ **Implementation Status Badge**: [IMPLEMENTED], [PARTIAL], [PLANNED], [NOT STARTED]
- 📝 **Script References**: Direct file paths to relevant scripts
- 🔧 **Technical Details**: Expanded technical specifications with code examples
- 🎯 **Implementation Notes**: How the feature is actually implemented
- ⚠️ **Known Gaps**: What's in GDD but not yet in code (or vice versa)
- 🔗 **Cross-References**: Links to related sections and scripts

---

## Section-by-Section Expansion Plan

### 1. Game Overview (Lines 21-159)
**Current State**: High-level vision and core concepts
**Expansion Needed**:
- Add implementation status for core mechanics
- Reference SimpleNavalController.cs and NetworkedNavalController.cs for ship physics
- Add technical specs for 300+ player servers (currently theoretical)
- Clarify extraction mechanics (designed but not yet implemented)
- Add permadeath system status (designed, awaiting economy systems)

**Script References**:
- None directly implemented yet (this is design-only section)

---

### 2. Core Gameplay (Lines 160-1484)
**Current State**: Detailed crew management, ship progression, combat systems
**Expansion Needed**:

#### 2.1 Crew Management System (Lines 162-499)
- **Status**: PLANNED (designed but not implemented)
- **Missing Scripts**: CrewCard.cs, CrewManager.cs, CrewClassification.cs
- **Add**: Implementation architecture plan
- **Add**: Database schema for crew progression
- **Clarify**: Level-up formulas and XP curves

#### 2.2 Ship Control & Physics (Lines 500+)
- **Status**: IMPLEMENTED ✅
- **Script References**:
  - SimpleNavalController.cs (Lines 192-218 of catalog)
  - NetworkedNavalController.cs (Lines 163-188 of catalog)
- **Add**: Detailed physics calculations from code
- **Add**: 8-speed throttle system implementation details
- **Add**: Turning circle calculations
- **Add**: Steerageway implementation

#### 2.3 Navigation System
- **Status**: IMPLEMENTED ✅
- **Script References**:
  - SimpleNavalController.cs - waypoint system
- **Add**: Waypoint data structures
- **Add**: Pathfinding algorithms (if any)

---

### 3. Core Systems Breakdown (Lines 1485-1787)
**Expansion Needed**: Add implementation status for each core system

---

### 4. Carrier Operations System (Lines 1788-2217)
**Status**: PLANNED (designed but not implemented)
**Expansion Needed**:
- Add "NOT STARTED" badges
- Note: No carrier scripts exist yet
- Add implementation priority/timeline
- Add planned script architecture

---

### 5. Surface Ship Combat System (Lines 2218-2678)
**Status**: PARTIAL (physics done, combat not implemented)
**Expansion Needed**:
- Reference SimpleNavalController.cs for movement
- Note missing: Weapons system, damage model, ballistics
- Add planned script architecture for TurretController.cs, ProjectileSystem.cs

---

### 6. Submarine Warfare System (Lines 2679-3421)
**Status**: PLANNED
**Expansion Needed**:
- Add "NOT STARTED" status
- No submarine scripts exist
- Add technical feasibility notes
- Add 2D depth simulation approach

---

### 7. Ship Customization & Module System (Lines 3422-5138)
**Status**: PLANNED (Tetris inventory designed, not implemented)
**Expansion Needed**:
- Add detailed UI wireframes reference
- Note: No module scripts exist yet
- Add drag-and-drop implementation approach (Unity UI system)
- Reference potential Unity Asset Store solutions

---

### 8. Player-Driven Economy & Trading (Lines 5139-5437)
**Status**: PLANNED (Phase 3 priority)
**Expansion Needed**:
- Add database schema for economy
- Add backend API endpoints needed
- Reference LoginController.cs for authentication foundation
- Add marketplace UI requirements

---

### 9. Technology-Driven UI System (Lines 5438-5759)
**Status**: IMPLEMENTED ✅
**Expansion Needed**:
- **HIGH PRIORITY - MAJOR SECTION**
- Add comprehensive script references:
  - MenuManager.cs (Lines 418-437)
  - MainMenuController.cs (Lines 371-388)
  - LoginController.cs (Lines 343-368)
  - JoinMenuController.cs (Lines 313-340)
  - HostMenuController.cs (Lines 269-286)
  - ConnectionMenuController.cs (Lines 224-244)
  - InGameMenuController.cs (Lines 289-312)
  - OptionsMenuController.cs (Lines 441-458)
  - MenuKeyboardNavigation.cs (Lines 392-417)
  - ControlsHelpManager.cs (Lines 247-268)
  - ShipDebugUI.cs (Lines 481-510)
  - ShipDebugUIManager.cs (Lines 512-544)
  - ReadOnlyTextField.cs (Lines 461-478)
- Add screenshots of implemented UI
- Add MUIP (Modern UI Pack) integration details
- Add accessibility compliance details (WCAG 2.1 AA)

---

### 10. Nation Faction System (Lines 5760-6034)
**Status**: PLANNED (designed, not implemented)
**Expansion Needed**:
- Add backend API requirements
- Add reputation algorithm details
- Add database schema for faction relationships
- Note: No faction scripts exist yet

---

### 11. World Design & Map System (Lines 6035-6596)
**Status**: PARTIAL (ocean rendering done, zones not implemented)
**Expansion Needed**:
- Reference OceanChunkManager.cs (Lines 93-117)
- Add biome system implementation details
- Add chunk-based rendering performance metrics
- Note missing: Zone system, port locations, combat areas

---

### 12. Game Structure (Lines 6597-6617)
**Expansion Needed**:
- Add Unity scene structure
- Add asset organization hierarchy
- Reference actual project folder structure

---

### 13. Visual Design & Art Direction (Lines 6618-6769)
**Expansion Needed**:
- Add current asset status (sprites, UI, effects)
- Reference actual sprite sheets/atlases
- Add art pipeline documentation

---

### 14. Audio Design (Lines 6770-6900)
**Status**: NOT STARTED
**Expansion Needed**:
- Add "NOT STARTED" status
- Add audio middleware requirements (FMOD/Wwise vs Unity Audio)
- Add sound asset list

---

### 15. Historical Narrative (Lines 6901-7050)
**Expansion Needed**:
- Add research database references
- Link to Ships database (GB_Ships_Database.md, etc.)
- Add weapon research references

---

### 16. Technical Requirements (Lines 7051-7232)
**Status**: PARTIAL
**Expansion Needed**:
- **HIGH PRIORITY SECTION**
- Add actual tech stack details:
  - Unity 6000.0.55f1 (2D/URP)
  - Mirror Networking v89.8.0 (confirm version)
  - Unity Input System
  - TextMeshPro
  - MUIP (Modern UI Pack)
- Reference ServerConfig.cs (Lines 121-140)
- Reference WOSEdgegapBootstrap.cs (Lines 142-158)
- Reference ChatManager.cs (Lines 69-90)
- Add networking architecture diagram
- Add client-server communication protocol
- Add JWT authentication flow (LoginController.cs)
- Add server deployment requirements
- Add database requirements (MongoDB, PostgreSQL?)

---

### 17. Development Roadmap (Lines 7233-7278)
**Expansion Needed**:
- Update Phase 1 status: COMPLETE ✅
  - Basic ship movement ✅
  - Camera system ✅
  - Ocean rendering ✅
  - Menu system ✅
  - Multiplayer networking ✅
  - Chat system ✅
- Update Phase 2 status: IN PROGRESS 🚧
- Update Phase 3 status: PLANNED
- Add Gantt chart or timeline
- Add current blockers and dependencies

---

### 18. Testing & Validation (Lines 7279-7308)
**Expansion Needed**:
- Add actual test results if any
- Add Unity Test Framework scripts (if they exist)
- Add performance benchmarks (FPS, network latency)
- Add multiplayer stress test results

---

### 19. Camera System (Needs Dedicated Section)
**Status**: IMPLEMENTED ✅
**Missing from GDD**: Dedicated camera section
**Add New Section**:
- Reference CameraController.cs (Lines 14-40)
- Reference SimpleCameraController.cs (Lines 42-66)
- Add camera follow modes (centered vs look-ahead)
- Add zoom system details
- Add camera shake implementation
- Add manual panning controls

---

## Implementation Priority Matrix

### Already Implemented (Document First)
1. **Ship Physics & Controls** - SimpleNavalController.cs, NetworkedNavalController.cs
2. **Camera System** - CameraController.cs, SimpleCameraController.cs
3. **Ocean Rendering** - OceanChunkManager.cs
4. **Menu & UI System** - MenuManager.cs + 12 UI controllers
5. **Networking** - ServerConfig.cs, WOSEdgegapBootstrap.cs
6. **Chat System** - ChatManager.cs
7. **Authentication** - LoginController.cs

### Designed But Not Implemented (Clarify Status)
1. **Crew Management System** - Extensive design, no code
2. **Module/Inventory System** - Tetris inventory designed, no code
3. **Combat Systems** - Turrets, weapons, damage - no code
4. **Economy System** - Detailed design, no code
5. **Faction/Nation System** - Reputation system designed, no code
6. **Carrier Operations** - Full air combat designed, no code
7. **Submarine System** - Depth mechanics designed, no code

### Not Yet Designed (Flag for Future)
1. **AI/Bot System** - No design yet
2. **Mission/Quest System** - Not detailed
3. **Weather System** - Mentioned but not detailed
4. **Port Interaction UI** - Referenced but not designed

---

## Documentation Enhancements

### Code Examples to Add
For each implemented system, add:
```csharp
// Example: Ship throttle calculation
float targetSpeed = ConvertThrottleToSpeed(throttleInput);
// -4 = Full Astern, 0 = Stop, +4 = Full Ahead
```

### Diagrams to Add
1. **System Architecture Diagram** - How all scripts interact
2. **Network Architecture** - Client-server data flow
3. **UI Flow Diagram** - Menu navigation paths
4. **Physics Diagram** - Ship turning circles and momentum
5. **Module System Wireframe** - Tetris inventory UI mockup

### Tables to Add
1. **Script Implementation Matrix** - GDD Section vs Scripts
2. **Feature Completion Status** - What's done vs planned
3. **Performance Benchmarks** - Current FPS, network latency
4. **Asset Inventory** - What sprites/audio/prefabs exist

---

## Quality Assurance Checks

### Validation Tasks
- [ ] Every script is referenced in at least one GDD section
- [ ] Every GDD feature has implementation status badge
- [ ] All code examples are tested and accurate
- [ ] All file paths are verified and correct
- [ ] No contradictions between design and implementation
- [ ] Technical specifications match actual code behavior
- [ ] All placeholders are clearly marked
- [ ] Future features are clearly distinguished from current features

---

## Output Format

### Enhanced Section Template
```markdown
## Section Title [IMPLEMENTATION STATUS]

**Implementation Status**: [IMPLEMENTED ✅ | PARTIAL 🚧 | PLANNED 📋 | NOT STARTED ⭕]
**Script References**:
- `path/to/ScriptName.cs` - Brief description
- `path/to/AnotherScript.cs` - Brief description

### Design Specification
[Original GDD content preserved]

### Technical Implementation
**Current Implementation**:
[How this is actually built in code]

**Key Code Components**:
- ClassName.MethodName() - What it does
- Another key function

**Known Gaps**:
- What's designed but not implemented
- What's implemented differently than designed

**Future Enhancements**:
- Planned improvements
- Technical debt items

### Developer Notes
[Implementation guidance, architecture decisions, etc.]
```

---

## Deliverables

### Primary Output
1. **GDD_Updated-2.md** - Fully expanded GDD with all enhancements
2. **GDD_Implementation_Matrix.md** - Table showing GDD sections vs implemented scripts
3. **GDD_Technical_Supplement.md** - Deep dive technical documentation

### Supporting Documents
1. **SCRIPTS_CATALOG.md** - ✅ Already created
2. **Architecture_Diagrams/** - Folder with visual diagrams
3. **Code_Examples/** - Folder with tested code snippets
4. **Implementation_Status_Report.md** - Summary of what's done vs planned

---

## Success Criteria

### How We Know We're Done
1. ✅ Every script has at least one GDD reference
2. ✅ Every GDD section has implementation status
3. ✅ No ambiguous technical specifications
4. ✅ Clear distinction between design and implementation
5. ✅ Developer can read GDD and know exactly what to build next
6. ✅ All cross-references are valid and helpful
7. ✅ Document is navigable and searchable

---

*End of Expansion Plan - Ready for Implementation*
