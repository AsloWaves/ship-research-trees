# AI & NPC Ship System
**Status**: 📋 PLANNED
**Phase**: Phase 2-3
**Last Updated**: 2025-12-03

---

## Overview

AI-controlled ships populate the world alongside players, creating a living ocean with faction patrols, merchant convoys, and mission-specific encounters. The AI system is deeply integrated with the **Faction/Political System** and **Mission System**.

---

## AI Ship Categories

### 1. Faction Military Ships
**Purpose**: Enforce faction control, respond to reputation-based aggression

| Faction | Ship Types | Patrol Zones | Aggression Triggers |
|---------|-----------|--------------|---------------------|
| United States | DD, CL, CA, BB | Pacific, Atlantic Safe Zones | Rep < -50, Contraband, Hostile Flag |
| Great Britain | DD, CL, CA, CV | Atlantic, Mediterranean | Rep < -50, Piracy Witnessed |
| Japan | DD, CL, CA, BB | Pacific, Home Waters | Rep < -50, Faction War |
| Germany | DD, CL, CA, U-boat | Atlantic, North Sea | Rep < -50, Allied Ships |
| Pirates | Various captured | Contested Zones | Opportunity-based |

### 2. Merchant/Civilian Ships
**Purpose**: Economic targets, escort mission objectives, trade route traffic

- **Cargo Ships**: Slow, valuable cargo, minimal armament
- **Tankers**: Oil/fuel transport, high value
- **Passenger Liners**: Protected status, severe rep penalty for attacking
- **Fishing Vessels**: Common in coastal zones, low value

### 3. Mission-Spawned Ships
**Purpose**: Specific mission objectives (escort targets, assassination targets, reinforcements)

- Spawned by Mission System when player accepts mission
- Despawn on mission completion/failure
- Can have scripted behaviors (flee, patrol route, rendezvous)

---

## AI Behavior System

### Behavior States

```
┌─────────────────────────────────────────────────────────────┐
│                      AI STATE MACHINE                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   IDLE ──────► PATROL ──────► ALERT ──────► COMBAT          │
│     │            │              │             │              │
│     │            │              │             │              │
│     └────────────┴──────────────┴─────────────┘              │
│                         │                                    │
│                         ▼                                    │
│                      FLEE / RETREAT                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### State Descriptions

#### IDLE
- Ship stationary at port or anchor
- Minimal awareness
- Triggered to PATROL by schedule or event

#### PATROL
- Following predetermined route or random patrol pattern
- Detection radius active
- Checks player reputation on detection

#### ALERT
- Player detected, evaluating threat
- Broadcasts to nearby friendly ships
- Decision: COMBAT, FLEE, or return to PATROL

#### COMBAT
- Engaging hostile target
- Uses ship's weapon loadout
- Calls for reinforcements if available

#### FLEE/RETREAT
- Health below threshold OR outmatched
- Attempts to reach friendly port/reinforcements
- Ships fight to the death or escape - no surrender/capture mechanic

---

## Detection & Awareness

### Detection Factors

| Factor | Effect | Notes |
|--------|--------|-------|
| Distance | Base detection range | Varies by ship type (DD fast, BB slow) |
| Ship Size | +/- detection range | Larger ships easier to spot |
| Speed | + detection if moving fast | Engine noise, wake |
| Weather | - detection in storms | Visibility reduction |
| Technology Era | + with radar | T6+ ships have radar detection |
| Submarine Depth | - detection when submerged | Periscope depth still visible |

### Detection Ranges (Baseline)

| AI Ship Type | Visual Range | Radar Range (T6+) |
|--------------|--------------|-------------------|
| Patrol Boat | 5 km | 10 km |
| Destroyer | 8 km | 15 km |
| Cruiser | 10 km | 20 km |
| Battleship | 12 km | 25 km |
| Carrier | 10 km + Aircraft | 30 km |

---

## Reputation-Based Behavior

### Reputation Thresholds (per faction)

| Rep Range | AI Response | Notes |
|-----------|-------------|-------|
| +75 to +100 | Friendly | May offer escort, trade benefits |
| +25 to +74 | Neutral-Positive | Ignores player, allows passage |
| -24 to +24 | Neutral | Basic checks, suspicious |
| -25 to -49 | Suspicious | Increased patrols, may inspect |
| -50 to -74 | Hostile | Will engage on sight |
| -75 to -100 | Kill on Sight | Priority target, calls reinforcements |

### Cross-Faction Awareness
- Attacking Faction A ships while Faction B watches affects Faction B rep
- Allied factions share intel (US/GB share hostile player info)
- Enemy factions don't share (attacking Japan doesn't alert US)

---

## Combat AI

### Engagement Rules

1. **Target Priority**:
   - Threats to self (attacking ships first)
   - Mission objectives
   - Highest-value targets
   - Nearest hostile

2. **Weapon Usage**:
   - Main guns: Optimal range based on ship config
   - Torpedoes: Destroyer/Submarine behavior
   - Aircraft: Carrier launches based on threat level

3. **Maneuvering**:
   - Maintain optimal weapon range
   - Avoid collision
   - Present broadside for maximum firepower
   - Destroyers: Torpedo runs then retreat
   - Battleships: Tanking damage, sustained fire

### Difficulty Scaling

| Zone Tier | AI Accuracy | AI Reaction Time | Reinforcement Speed |
|-----------|-------------|------------------|---------------------|
| T1-T3 | 40% | Slow (2s) | None |
| T4-T5 | 55% | Medium (1.5s) | Slow |
| T6-T7 | 70% | Fast (1s) | Medium |
| T8-T9 | 85% | Very Fast (0.5s) | Fast |
| T10 | 95% | Instant | Immediate |

---

## Spawning & Population

### Zone Population Density

| Zone Type | Military Ships | Merchant Ships | Pirate Ships |
|-----------|---------------|----------------|--------------|
| Safe Zone (T1-T3) | High | High | None |
| Contested (T4-T6) | Medium | Medium | Low |
| Dangerous (T7-T9) | Low | Low | Medium |
| Lawless (T10) | Rare | Rare | High |

### Spawn Rules

1. **Persistence**: AI ships persist in world, don't despawn when player leaves
2. **Respawn Timer**: Destroyed ships respawn after cooldown (5-30 min based on type)
3. **Convoy System**: Merchant convoys spawn on schedule, follow trade routes
4. **Reinforcement Spawns**: Called ships spawn from nearest faction port

---

## Mission System Integration

### AI Roles in Missions

| Mission Type | AI Role | Behavior |
|--------------|---------|----------|
| Escort | Escort Target | Follow player, call for help if attacked |
| Hunt | Hunt Target | Flee when player detected, fight if cornered |
| Patrol | Enemy Patrol | Standard patrol, attacks on sight |
| Intercept | Interception Force | Spawns to chase player |
| Blockade | Blockade Ships | Holds position, inspects all ships |

### Scripted Behaviors
- **Waypoint Following**: Follow predetermined path
- **Player Following**: Escort behavior
- **Area Defense**: Hold position, engage hostiles
- **Flee to Point**: Run to specific location

---

## NPC Crew Simulation

NPC ships have simulated crew for damage calculations. To optimize server performance, NPC crew uses a **simplified numerical model** rather than the full crew card system used by players.

### Simplified Crew Model

| Property | Description | Example |
|----------|-------------|---------|
| Crew Count | Total sailors aboard | 1,200 |
| Crew Quality | Effectiveness multiplier (0.5-1.5) | 1.0 (average) |
| Casualty Count | Sailors lost to damage | 150 |
| Efficiency | (Crew Count - Casualties) / Crew Count × Quality | 87.5% |

### Crew Efficiency Effects

| Efficiency | Effect on Ship |
|------------|----------------|
| 100-80% | Full performance |
| 79-60% | -10% reload speed, -5% accuracy |
| 59-40% | -25% reload speed, -15% accuracy, -10% speed |
| 39-20% | -50% reload speed, -30% accuracy, -25% speed |
| Below 20% | Ship attempts to flee, minimal combat effectiveness |

### Crew Quality by Zone Tier

| Zone Tier | Crew Quality Range | Notes |
|-----------|-------------------|-------|
| T1-T3 | 0.6-0.8 | Green crews, training ships |
| T4-T5 | 0.8-1.0 | Standard crews |
| T6-T7 | 1.0-1.2 | Veteran crews |
| T8-T9 | 1.2-1.4 | Elite crews |
| T10 | 1.3-1.5 | Ace crews |

### Why Simplified?
- Full crew card simulation for 50+ NPC ships would strain server
- Players don't see NPC crew details - only effects matter
- Numerical approach allows quick damage calculation
- Can be expanded later if performance allows

---

## Group Coordination System

NPC ships within communication range coordinate their actions through a **Fleet Brain** system.

### Fleet Formation Detection

When multiple NPC ships are within 5km of each other and share faction alignment:
- They form a temporary "fleet" with shared awareness
- One ship designated as **Fleet Leader** (highest tier/largest ship)
- Fleet Leader makes strategic decisions for the group

### Coordinated Behaviors

#### Attack Coordination
```
Fleet detects hostile player
    │
    ▼
Fleet Leader evaluates:
- Total fleet firepower vs target
- Fleet health status
- Reinforcement availability
    │
    ├─► ATTACK: Fleet engages
    │     ├─ Assign primary target
    │     ├─ Split targets if multiple hostiles
    │     └─ Destroyers: Torpedo approach
    │         Cruisers: Gun engagement
    │         Battleships: Anchor position
    │
    └─► FLEE: Fleet retreats together
          ├─ Slowest ship sets pace
          ├─ Escorts screen rear
          └─ Head to nearest friendly port
```

#### Target Assignment
| Situation | Coordination |
|-----------|--------------|
| Single hostile | All ships focus fire |
| Multiple hostiles | Split by threat level - BBs target BBs, DDs target DDs |
| Protecting convoy | Escorts engage, merchants flee |
| Overwhelming odds | Fighting retreat, covering fire |

#### Communication Calls
- **Contact Report**: "Hostile detected at [position]" - Alerts nearby friendlies
- **Engage Order**: Fleet Leader commands attack
- **Retreat Order**: Fleet Leader commands withdrawal
- **Reinforcement Request**: Calls to nearby patrol routes or ports

---

## Specialized AI Brains

### Carrier AI Brain

Carriers require fundamentally different decision-making due to aircraft operations.

#### Carrier Behavior Priorities
1. **Stay at range** - Avoid gun engagements, maintain 20+ km from hostiles
2. **Manage aircraft** - Launch, recover, rearm cycles
3. **Protect self** - Flee if hostile closes distance

#### Aircraft Management

```
┌─────────────────────────────────────────────────────────────┐
│                    CARRIER AI CYCLE                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ASSESS THREAT ──► LAUNCH APPROPRIATE SQUADRONS             │
│       │                    │                                 │
│       │            ┌───────┴───────┐                        │
│       │            ▼               ▼                        │
│       │        STRIKE          DEFENSE                      │
│       │      (vs Surface)    (vs Aircraft)                  │
│       │            │               │                        │
│       │            └───────┬───────┘                        │
│       │                    ▼                                │
│       │            RECOVERY & REARM                         │
│       │                    │                                │
│       └────────────────────┘                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### Squadron Deployment Logic

| Threat Type | Response |
|-------------|----------|
| Surface ships approaching | Launch torpedo bombers + dive bombers |
| Enemy aircraft inbound | Launch fighters for CAP |
| Submarine detected | Launch ASW aircraft (if available) |
| No threat | Maintain minimal CAP, conserve aircraft |

#### Self-Preservation
- If hostile within 15km: Maximum evasion, launch all remaining aircraft
- If hostile within 10km: Emergency speed, call for escort support
- Carriers NEVER close distance to engage

---

### Submarine AI Brain

Submarines operate on stealth and ambush tactics with depth management.

#### Submarine Behavior Priorities
1. **Remain undetected** - Depth management is survival
2. **Ambush attacks** - Strike from concealment
3. **Escape after attack** - Dive deep, evade pursuit

#### Depth States

| Depth State | Detection Risk | Attack Capability | Speed |
|-------------|---------------|-------------------|-------|
| Surface | Very High | Deck gun + Torpedoes | Full |
| Periscope (5-15m) | Medium | Torpedoes only | 75% |
| Shallow (15-50m) | Low | Torpedoes only | 50% |
| Deep (50m+) | Very Low | None (reloading) | 25% |

#### Hunt Cycle

```
PATROL (Periscope) ──► DETECT TARGET ──► APPROACH (Shallow)
                                              │
                                              ▼
                      ESCAPE (Deep) ◄── ATTACK (Periscope)
                           │
                           ▼
                      RELOAD ──► Return to PATROL
```

#### Decision Factors

| Factor | Submarine Response |
|--------|-------------------|
| Destroyer detected | DIVE DEEP immediately, evade |
| Merchant alone | Approach submerged, attack |
| Convoy with escorts | Stalk, wait for opportunity |
| Aircraft overhead | Emergency dive |
| Damaged | Flee to deep water |
| Low torpedoes | Return to port |

#### Anti-Submarine Evasion
- When depth charged: Random course changes, silent running
- When pinged (sonar): Go deep, reduce speed
- After attack: Immediate deep dive, flee area

---

## Technical Considerations

### Performance Targets
- **Max Active AI Ships**: 50 within player view
- **Behavior Update Rate**: 0.5s (not every frame)
- **Pathfinding**: Simple waypoint-based (no complex A*)
- **LOD System**: Distant ships simplified behavior

### Network Sync
- AI ships are server-authoritative
- Position/rotation synced to clients
- Combat decisions made server-side
- Clients receive result, not decision process

---

## Design Decisions (Resolved)

| Question | Decision |
|----------|----------|
| Ship Capture? | **NO** - Players cannot capture NPC ships. Loot from wreckage only. |
| AI Crew? | **YES** - Simplified numerical model for performance (see NPC Crew Simulation) |
| Convoy Coordination? | **YES** - Fleet Brain system coordinates attack/flee decisions |
| Carrier AI? | **YES** - Specialized brain focusing on aircraft management and range-keeping |
| Submarine AI? | **YES** - Specialized brain focusing on depth management and ambush tactics |

---

## Additional Design Decisions

| Question | Decision |
|----------|----------|
| Crew Casualty Loot? | **NO** - NPC ships don't drop dog tags/documents |
| Fleet Size Limit? | **30 ships max** per coordinated fleet |
| AI Repair at Port? | **NO** - NPCs despawn at port, respawn fresh when needed |
| Pirate AI Different? | **YES** - See Pirate AI section below |

---

## Pirate AI Behavior

Pirates behave differently from faction military ships.

### Key Differences

| Behavior | Faction Military | Pirates |
|----------|-----------------|---------|
| Patrol Pattern | Fixed routes, zone defense | Roaming, opportunistic |
| Target Selection | Rep-based, follow orders | Prey on weak, avoid strong |
| Coordination | Fleet Brain, military tactics | Loose packs, less organized |
| Retreat Trigger | Low health, outnumbered | Any significant resistance |
| Aggression | Only vs hostiles | Attack anyone not pirate |

### Pirate Targeting Logic

```
Pirate detects potential target
       │
       ▼
Evaluate target strength vs self
       │
       ├──► Target WEAKER: Engage aggressively
       │
       ├──► Target EQUAL: Engage cautiously, ready to flee
       │
       └──► Target STRONGER: Avoid, look for other prey
```

### Pirate Pack Behavior
- Pirates loosely group (not strict Fleet Brain)
- Share target info but don't coordinate attacks
- Each pirate decides individually to engage or flee
- Will "pile on" weak targets if nearby
- Scatter when facing organized resistance

### Pirate Spawn Zones
- Common in T7-T10 (lawless zones)
- Rare in T4-T6 (contested, faction patrols)
- Never in T1-T3 (faction-controlled safe zones)

---

## NPC Lifecycle

### Spawn → Active → Despawn

```
NPC SPAWNS (outside port, on patrol route)
       │
       ▼
NPC ACTIVE (patrolling, engaging, fleeing)
       │
       ├──► Reaches port → DESPAWN (removed from world)
       │
       └──► Destroyed → RESPAWN TIMER starts
                              │
                              ▼
                        Timer expires → NEW NPC SPAWNS
```

### Key Points
- NPCs only exist when "at sea"
- Reaching port = mission complete, NPC despawns
- No port repairs - fresh NPC spawns later
- Respawn timers vary by ship type (5-30 min)
- Spawn points: Patrol route starts, port exits, mission triggers

---

## Implementation Priority

### Phase 2 (Combat Foundation)
- [ ] Basic patrol behavior (state machine)
- [ ] Detection system (visual + radar)
- [ ] Combat engagement (targeting, firing)
- [ ] Reputation-based aggression
- [ ] NPC crew damage model

### Phase 3 (Advanced AI)
- [ ] Group coordination (Fleet Brain)
- [ ] Carrier AI brain
- [ ] Submarine AI brain
- [ ] Mission system spawning
- [ ] Convoy system
- [ ] Reinforcement calling

---

## Cross-References

- [[11-Factions/Nation-Overview]] - Faction relationships
- [[11-Factions/Reputation-System]] - Rep thresholds
- [[02-Core-Gameplay/Mission-System]] - Mission integration
- [[03-Combat-Systems/Combat-Overview]] - Combat mechanics
- [[10-World-Design/Zone-System]] - Zone tier definitions

---

*Document created: 2025-12-03*
*To be refined through discussion*
