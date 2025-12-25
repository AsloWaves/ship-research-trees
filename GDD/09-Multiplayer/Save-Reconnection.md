# Save System & Reconnection Handling
**Status**: 📋 PLANNED
**Phase**: Phase 2
**Last Updated**: 2025-12-03

---

## Overview

Fathoms Deep uses a **persistent ship** model where player ships remain in the world even when the player disconnects. Ships only truly "save" when docked at port. This creates meaningful risk for players who log out at sea and reinforces the extraction-based gameplay loop.

---

## Core Philosophy

### "Your Ship Lives in the World"

| Concept | Description |
|---------|-------------|
| **Ships Persist** | Your ship exists in the world 24/7, even when offline |
| **Port = Safety** | Docking at port is the only way to safely save and log out |
| **At-Sea Risk** | Disconnecting at sea leaves your ship vulnerable |
| **No Grace Period** | Ship continues on last input - no temporary protection |

This design reinforces:
- The importance of extraction (getting back to port)
- Risk/reward of venturing far from safe zones
- Consequences for combat logging (ship stays, can still die)
- The living, persistent world feeling

---

## Save Architecture

### When Saves Occur

**Saves ONLY happen when docked at port**:

| Data Type | Save Trigger | Notes |
|-----------|--------------|-------|
| Ship Position | Dock at port | Ship "stored" at port |
| Inventory/Cargo | Dock at port | Cargo secured |
| Ship Health | Dock at port | Damage state saved |
| Crew Status | Dock at port | Casualties recorded |
| Mission Progress | Mission checkpoint OR dock | Checkpoints vary by mission |

### Immediate Saves (Always)

These save instantly regardless of location:
| Data Type | Trigger | Why Immediate |
|-----------|---------|---------------|
| Currency | Any transaction | Prevent duplication |
| Reputation | Any change | Prevent exploit |
| Crew Card Loss | Crew dies | Permadeath is permanent |
| Ship Destruction | Ship sinks | Permadeath is permanent |
| Extraction Complete | Dock + confirm | Prevents disconnect exploit |

### What Happens Without Saving

| Scenario | Result |
|----------|--------|
| Disconnect at sea, ship survives | Reconnect where you left off |
| Disconnect at sea, ship destroyed | Lose ship, spawn at last port |
| Collect loot, disconnect before port | Loot lost if ship destroyed |
| Complete mission, disconnect before port | Progress lost to last checkpoint |

---

## Ship Persistence System

### Disconnected Ship Behavior

When a player disconnects, their ship:

```
Player Disconnects
       │
       ▼
Ship marked as "Autopilot"
       │
       ▼
Ship continues with LAST INPUT
(If moving: keeps moving same direction/speed)
(If stopped: stays stopped)
       │
       ▼
Ship consumes Fuel & Supplies over time
       │
       ├──► Fuel/Supplies available: Ship continues
       │
       └──► Fuel/Supplies depleted: Ship takes damage over time
                    │
                    └──► Ship eventually destroyed
```

### Fuel & Supply Consumption (Offline)

Fuel consumption while offline is based on the ship's engine configuration:

| Engine Setting | Consumption Rate | Notes |
|----------------|-----------------|-------|
| Efficient | Engine's efficient rate | Lowest consumption, slow speed |
| Natural | Engine's natural rate | Balanced consumption |
| Maximum | Engine's max rate | Highest consumption, full speed |

When player disconnects, ship continues at **last throttle setting**:
- Full Ahead: Max consumption rate
- Half Ahead: Natural consumption rate
- All Stop: Minimal/no consumption (drifting)

| Resource | Effect When Empty |
|----------|-------------------|
| Fuel | Ship drifts (no propulsion), continues on momentum then stops |
| Supplies | Crew health degrades, ship takes damage over time |

### Damage Over Time (No Supplies)

When a ship runs out of supplies while player is offline:
- **Hour 1**: 1% hull damage per hour (crew starving)
- **Hour 2+**: 2% hull damage per hour
- **Critical**: At 10% hull, damage accelerates to 5% per hour
- **Destruction**: Ship sinks when hull reaches 0%

This means:
- A fully supplied ship can persist for hours/days offline
- Players must plan supply levels before logging out at sea
- Eventually, abandoned ships will sink

---

## Disconnection Scenarios

### Scenario 1: Logout at Port (Safe)

**Player Action**: Docks at port, uses logout

**Process**:
1. Player docks at port
2. Extraction completes (cargo saved)
3. Ship marked as "Docked"
4. All data saved immediately
5. Player logs out
6. Ship removed from world (stored in port)

**Result**: ✅ Fully safe, all progress saved

---

### Scenario 2: Logout at Sea (Risky)

**Player Action**: Logs out while not at port

**Warning**: "Your ship will remain in the world and may be destroyed. Are you sure?"

**Process**:
1. Player confirms logout
2. Ship continues with last input (throttle/heading)
3. Ship consumes fuel/supplies
4. Ship can be attacked by NPCs or players
5. Ship can run aground, hit obstacles
6. Eventually: Ship destroyed OR player reconnects

**Result**: ⚠️ Ship at risk until player returns or ship destroyed

---

### Scenario 3: Network Disconnect (Unintentional)

**Cause**: Internet drops, crash, power outage

**Detection**: Server stops receiving heartbeat (30 seconds)

**Process**:
1. Server marks player as "Disconnected"
2. Ship continues on last input
3. No AI takeover - ship just drifts
4. Fuel/supplies continue consumption
5. Ship remains vulnerable to attack

**Result**: Same as intentional logout at sea - ship persists

---

### Scenario 4: Disconnect During Combat

**Situation**: Player disconnects while in active combat

**Process**:
1. Ship stops responding (last input continues)
2. Ship does NOT return fire automatically
3. Ship can be destroyed normally
4. If destroyed: Permadeath rules apply

**Anti-Combat-Log Effect**:
- **No escape** - Your ship stays in combat
- **No defense** - Ship won't fight back
- **Full consequences** - Ship can be looted/destroyed
- Combat logging is punished by game mechanics, no penalty system needed

---

### Scenario 5: Server Crash/Restart

**Cause**: Server crashes or scheduled maintenance

**Process**:
1. Server saves all "at port" ships immediately
2. At-sea ships: Position saved to temp storage
3. Server restarts
4. At-port ships: Spawn at their port
5. At-sea ships: Spawn at last known position (may have drifted)

**Data Recovery**:
- Port-docked data: Fully preserved
- At-sea position: Last known (within 60 seconds)
- Pending transactions: Fully preserved

**Communication**:
- Scheduled maintenance: 15-minute warning
- Crash: Notification on reconnect

---

## Reconnection Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    RECONNECTION FLOW                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Player Launches Game                                        │
│         │                                                    │
│         ▼                                                    │
│  Login / Authenticate                                        │
│         │                                                    │
│         ▼                                                    │
│  Check Ship Status                                           │
│         │                                                    │
│    ┌────┼────────────┐                                       │
│    ▼    ▼            ▼                                       │
│  DOCKED  AT SEA    DESTROYED                                 │
│    │      │           │                                      │
│    ▼      ▼           ▼                                      │
│  Spawn   Spawn at   Spawn at                                 │
│  at Port ship's     last port                                │
│          location   (no ship)                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Reconnection States

#### Ship Docked at Port
- Spawn at port, in port UI
- Ship fully available
- All saved data intact

#### Ship At Sea (Survived)
- Spawn in ship at current world position
- Ship may have drifted from disconnect point
- Fuel/supplies reduced by time offline
- Any damage taken while offline is present

#### Ship Destroyed While Offline
- Notification: "Your ship was destroyed while you were away"
- Spawn at last port you departed from
- Loss details shown (what cargo/crew was lost)
- If permadeath tier: Ship gone permanently

---

## Extraction & Saving

### Extraction is Instant-Save

When player docks at port and confirms extraction:

```
Player Docks at Port
       │
       ▼
"Extract" button appears
       │
       ▼
Player confirms extraction
       │
       ▼
INSTANT SAVE triggered
- Cargo → Port storage (SAVED)
- Ship status (SAVED)
- Crew status (SAVED)
- Mission progress (SAVED)
       │
       ▼
Dirty flag cleared
       │
       ▼
Safe to logout
```

### Dirty Flag System

| State | Meaning |
|-------|---------|
| Clean | All data matches last save |
| Dirty | Changes made since last save |
| Saving | Write in progress |
| Confirmed | Save completed successfully |

**Extraction Process**:
1. Player initiates extraction
2. Server marks data as "Saving"
3. Database write executes
4. Server receives confirmation
5. Data marked as "Confirmed" (clean)
6. Player can safely logout

If disconnect during save:
- Server retries write
- Player reconnects to completed save OR
- Player reconnects to pre-extraction state (try again)

---

## Data Integrity

### Preventing Exploits

#### Rollback Exploit Prevention
**Scenario**: Player loses item, disconnects hoping for rollback

**Prevention**:
- Item loss saves immediately (crew death, ship damage)
- Currency changes save immediately
- Disconnecting doesn't stop the save
- No way to "undo" by disconnecting

#### Duplication Exploit Prevention
**Scenario**: Player tries to duplicate items via disconnect

**Prevention**:
- All trades are atomic (complete or fail, never partial)
- Extraction saves are confirmed before success message
- Database transactions prevent partial states

---

## Edge Cases

### Case: Ship Runs Aground While Offline

**Process**:
1. Ship drifting hits land/obstacle
2. Ship stops (grounded)
3. No damage from grounding (just stops)
4. Ship remains at location until player returns

### Case: Ship Enters Dangerous Zone While Offline

**Process**:
1. Drifting ship enters higher-tier zone
2. NPCs in that zone may detect and attack
3. Ship cannot defend itself
4. Ship may be destroyed

### Case: Disconnect During Trade

**Process**:
1. Trade cancelled immediately
2. Items remain with original owners
3. No partial trades possible
4. Other player notified: "Trade partner disconnected"

### Case: Disconnect During Mission

**Process**:
1. Mission timer continues (no pause)
2. Ship drifts (may fail mission by leaving area)
3. Reconnect: Continue mission if still valid
4. If mission failed: Progress to last checkpoint lost

---

## Session Management

### Session Token
- JWT with 24-hour expiration
- One session per account (new login kicks old)
- Stored client-side

### Heartbeat System
- Client heartbeat: Every 10 seconds
- Disconnect detected: 30 seconds without heartbeat
- Ship transition: Active → Autopilot (last input)

---

## Design Decisions (Resolved)

| Question | Decision |
|----------|----------|
| Grace Period? | **NO** - Ship persists on last input immediately |
| Combat Log Penalty? | **NO** - Ship staying vulnerable IS the penalty |
| AI Takeover? | **NO** - Ship just continues last input (dumb) |
| Extraction Instant-Save? | **YES** - With dirty flag confirmation |
| Ship Death Offline? | Spawn at last port departed from |
| Offline Time Limit? | **NO** - Ship dies naturally from supply depletion |
| Fuel Consumption Rate? | **Engine-based** - Uses engine's natural/efficient/max rates |
| NPCs Hunt Idle Ships? | **NO** - NPCs don't actively seek disconnected players |
| Offline Attack Notifications? | **NO** - No email/push notifications |

---

## Implementation Priority

### Phase 2 (Core Functionality)
- [ ] Ship persistence (stays in world)
- [ ] Last-input autopilot
- [ ] Fuel/supply offline consumption
- [ ] Extraction instant-save
- [ ] Reconnection flow

### Phase 3 (Polish)
- [ ] Offline damage over time
- [ ] Destruction notifications
- [ ] Session conflict handling
- [ ] Server restart recovery

---

## Cross-References

- [[09-Multiplayer/Network-Architecture]] - Network layer
- [[09-Multiplayer/Authentication]] - JWT tokens
- [[02-Core-Gameplay/Inventory-System]] - Cargo/extraction
- [[01-Core-Concepts/Extraction-Mechanics]] - Core loop
- [[PLAYER_ACCOUNT_ARCHITECTURE]] - Database schema

---

*Document created: 2025-12-03*
*Refined with persistent ship model*
