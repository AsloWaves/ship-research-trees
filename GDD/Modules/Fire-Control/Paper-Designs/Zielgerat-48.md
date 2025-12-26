---
module_id: FCS-PAP-001
name: Zielgerät 48
category: fire-control
subcategory: paper-design
type: analog-computer
era: 1945
nation: Germany
manufacturer: Rheinmetall (designed)
status: never_built

# Physical (projected)
weight_kg: 2800
crew: 4
power_requirements: 380V 3-phase

# Capabilities (projected)
max_range_m: 45000
radar_integration: full
automatic_tracking: true
target_types: [surface, aircraft]

tags: [computer, paper-design, germany, advanced, never-built, 1945]
---

# Zielgerät 48 (Paper Design)

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Zielgerät 48 |
| **Nation** | Germany |
| **Era** | 1945 (never completed) |
| **Type** | Advanced Analog Computer |
| **Status** | PAPER DESIGN - Never Built |

## Description

The Zielgerät 48 was an advanced fire control computer designed in the closing months of WWII. It represented a dramatic leap beyond Germany's operational systems, incorporating full radar integration and automatic target tracking - features Germany had failed to implement in production systems.

**Design Goal**: Close the fire control gap with American and British systems.

## Why It Was Never Built

1. **Too Late**: Design finalized February 1945
2. **No Resources**: German industry collapsing
3. **No Platforms**: Capital ships sunk or inactive
4. **Allied Bombing**: Production facilities destroyed

## Projected Specifications

| Specification | Value | Notes |
|--------------|-------|-------|
| Weight | 2,800 kg | Heavier than Basisgerät |
| Crew | 4 | Reduced from 6 |
| Power | 380V 3-phase | All-electric drive |
| Range Capability | 45,000m | Extended range |
| Target Types | Surface + Aircraft | Dual-purpose |

## Key Innovations

### 1. Full Radar Integration
Unlike operational German systems, the Zielgerät 48 was designed FROM THE START for radar input:

```
┌──────────────┐     ┌──────────────┐
│  FuMO 213    │────▶│  ZIELGERÄT   │
│  FC Radar    │     │     48       │
└──────────────┘     └──────────────┘
        ▲                   │
        │                   ▼
┌──────────────┐     ┌──────────────┐
│   Target     │     │  Gun Orders  │
│   Auto-Track │◀────│  Continuous  │
└──────────────┘     └──────────────┘
```

### 2. Automatic Rate Finding
The system would automatically determine target course and speed:
- Radar tracks target position
- Computer calculates rate of change
- No operator estimation required
- Continuous automatic updating

This was the feature Germany most lacked in actual combat.

### 3. Dual-Purpose Capability
Designed to engage both:
- Surface ships (like Basisgerät)
- Aircraft (unlike any German operational system)

The same computer would handle both, switching modes based on target type.

### 4. Electronic Prediction
Analog electronic circuits would compute:
- Future target position
- Time of flight corrections
- Wind drift compensation
- Convergence for multiple mounts

## Comparison: What Germany Had vs. What They Designed

| Feature | Basisgerät C/38K | Zielgerät 48 |
|---------|-----------------|--------------|
| Radar Integration | None | Full |
| Rate Finding | Manual | Automatic |
| Target Types | Surface only | Dual-purpose |
| Crew | 6 | 4 |
| Update Speed | 10 sec | 0.5 sec |
| Night Capability | None | Full |

## Technical Details

### Projected Components
1. **Radar Interface Unit** - Converts FuMO 213 signals
2. **Electronic Rate Solver** - Vacuum tube circuits
3. **Mechanical Integrators** - Proven German technology
4. **Servo Amplifiers** - Power gun mount drives
5. **Ballistic Cams** - Interchangeable for gun types

### Projected Performance
| Metric | Value |
|--------|-------|
| Solution Time (initial) | 8 seconds |
| Solution Update | 0.5 seconds |
| Range Accuracy | ±25m at 30km |
| Bearing Accuracy | ±0.08° |
| Elevation Accuracy | ±0.1° |

## Why This Matters for Game Design

The Zielgerät 48 represents:
1. **What Germany COULD have had** - if war lasted longer
2. **The cost of late radar adoption** - years of development wasted
3. **Paper design limitations** - theoretical specs, unproven in combat

### Game Implementation Options

**Option A: "What-If" Premium Module**
- Available for late-war German ships
- Significant accuracy bonus
- Historical note: never actually existed

**Option B: Research Unlock**
- End of German FC research tree
- Demonstrates where technology was heading
- Requires late-war radar as prerequisite

## Historical Context

### German Fire Control Problems

By 1944, German naval officers knew their fire control was inferior:
- British achieved radar fire control 1941
- Americans achieved it 1942
- Germans still using optical primary 1944

The Zielgerät 48 was an attempt to catch up in one leap.

### Allied Intelligence

Post-war, Allied technical intelligence teams (CIOS, BIOS) found Zielgerät 48 documents at Rheinmetall. Reports noted:
- "Ambitious design"
- "Would have closed gap with Allied systems"
- "Production impossible given 1945 conditions"

## Similar Paper Designs

| Design | Nation | Status | Notes |
|--------|--------|--------|-------|
| Zielgerät 48 | Germany | Never built | This document |
| Type 5 FCS | Japan | Prototype | Tested, not deployed |
| STAAG Mk II | UK | Post-war | Completed after WWII |
| Mk 68 GFCS | USA | Post-war | Evolved from WWII designs |

## Game Statistics

| Stat | Value | Notes |
|------|-------|-------|
| Accuracy Bonus | +42% | Surface |
| AA Accuracy | +35% | Dual-purpose |
| Radar Integration | Full | Automatic |
| Night Capability | Full | Radar-directed |
| Status | Paper Design | Never combat-tested |

## Acquisition

**If Implemented**:
- Requires: German FC research completed
- Requires: FuMO 213 radar equipped
- Cost: Premium (never-built system)
- Historical Accuracy Note: Displayed on equipment

## Cross-References
- [[Computers/Basisgerat-C38K|Basisgerät C/38K (Operational System)]]
- [[Directors/Kommandogerat-C38K|Kommandogerät C/38K]]
- [[/GDD/Modules/Support/Detection-Radar/Radar-FC-FuMO27|FuMO Radars]]

---
*The Zielgerät 48 stands as a monument to "what might have been" - German engineering excellence arriving too late to change the outcome of the war.*
