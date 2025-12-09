---
module_id: COM-005
name: Wireless Telegraph (VLF)
category: support
subcategory: communications
era: 1920+
nation: Universal
slot_type: support
weight: 800
power_draw: 50
crew_required: 3

# Performance
range: 2000                    # km (can penetrate water)
data_rate: very_slow
reliability: 95                # percentage
security: low

# Capabilities
voice_capable: false
text_capable: true
data_capable: false            # automated sharing
vision_sharing: false          # manual text reports only

# Requirements
line_of_sight: false
weather_affected: false
crew_required: 3

tags: [communications, wireless, vlf, submarine, long-range]
---

# Wireless Telegraph (VLF)

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-005 |
| **Era** | 1920+ |
| **Range** | 2000+ km |
| **Type** | Wireless Telegraph (Very Low Frequency) |

## Description

Very Low Frequency (VLF) wireless telegraphy operates at 3-30 kHz, using wavelengths of 10-100 kilometers. Unlike higher frequencies, VLF waves can penetrate seawater to depths of 10-20 meters, making them the only practical method for communicating with submerged submarines. VLF signals also propagate reliably around the Earth's curvature, providing global coverage from powerful shore stations.

The extremely long wavelengths require massive antenna systems - shore stations use antenna arrays kilometers long, while ships require long trailing wire antennas. VLF is very slow (1-5 words per minute) due to the low frequency, but offers unmatched reliability and water penetration. This makes VLF essential for submarine command and control.

## Effect on Multiplayer

**This module enables:**
- Long-range text communication (2000+ km)
- Vision sharing: **No** - Manual contact reports only
- Voice chat: No - Text messages only
- Text messages: **Yes** - Very slow (30-60 seconds per message)
- Submarine reception while submerged (10-20 m depth)
- Orders from shore command
- Strategic-level coordination

**Submarine Communication:**
VLF is the primary method for shore commands to contact submerged submarines. Submarines must raise a trailing wire antenna to periscope depth to receive messages. They typically receive orders but do not transmit (to avoid detection).

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (2000+ km) |
| Rain/Fog | No effect (unaffected by weather) |
| Night | No effect (24/7 operation) |
| Enemy jamming | Difficult to jam (extremely powerful signals) |
| Atmospheric storms | Minimal effect (VLF very stable) |
| Solar activity | Minimal effect compared to HF |
| Water penetration | 10-20 m depth |

## Communication Speed

| Message Type | Transmission Time |
|--------------|------------------|
| Short code word | 30 seconds |
| Brief message (10 words) | 2-3 minutes |
| Complex order (50 words) | 10-15 minutes |

VLF is the slowest communication method but offers unmatched range and reliability.

Transmission rate: 1-5 words per minute
Reception: Continuous monitoring required
Submarine depth limit: 10-20 meters (deeper = no signal)

## Message Types

VLF messages are extremely brief due to low data rate:
- **Code Words**: "EXECUTE ORDER BRAVO" (preset plans)
- **Position Updates**: "PROCEED TO GRID 34N120W"
- **Target Assignments**: "CONVOY DEPARTING TRUK"
- **Status Requests**: "REPORT POSITION"
- **Emergency Orders**: "RETURN BASE IMMEDIATELY"

Complex tactical coordination is impractical - VLF is for strategic orders only.

## Tactical Use

1. **Submarine Command**: Orders to submarine fleet from shore
2. **Strategic Coordination**: Fleet-wide strategic orders
3. **Emergency Broadcast**: Critical alerts to all ships
4. **Weather/Intelligence**: Shore-to-ship information
5. **Position Reports**: Long-range position updates
6. **Code Word Orders**: Execute preplanned operations
7. **Global Reach**: Contact ships across oceans

## Submarine Operations

**Receiving VLF (Submarine):**
- Must raise trailing wire antenna to 10-20 m depth
- Can maintain depth control while receiving
- Typically receive-only (don't transmit to avoid detection)
- Monitor continuously for traffic
- Surface to transmit responses via HF

**Security Trade-off:**
Submarines prefer to receive VLF orders without transmitting responses. Transmitting reveals position to direction-finding stations. One-way communication (shore to submarine) maintains stealth.

## Limitations

- Extremely slow data rate (1-5 words/minute)
- Requires massive antenna systems
- Very high power requirement (50 kW+)
- Heavy equipment (800+ kg)
- Large crew requirement (3 operators)
- Cannot carry complex tactical information
- Limited to simple text messages
- Submarines must stay shallow (10-20 m) to receive

## Historical Notes

VLF communication emerged in the 1920s as navies sought ways to command dispersed submarine fleets. The long wavelengths could penetrate seawater, solving the fundamental problem of submarine communication. Shore stations with antenna arrays 10-30 km long transmitted orders that submarines could receive while submerged.

During WWII, Germany used VLF extensively to coordinate U-boat wolfpacks. BdU (U-boat Command) transmitted daily position updates and target assignments. Allied forces also used VLF, though their submarine doctrine emphasized more independent operation.

The Cold War saw massive VLF investments. The US Navy's Project Sanguine proposed a 6,000-square-mile antenna array in Wisconsin to ensure communication with ballistic missile submarines (SSBNs) even during nuclear war. Modern versions include TACAMO aircraft trailing 5-mile-long antennas to relay VLF messages to submarines.

VLF's main limitation - extremely low data rate - means messages must be brief. Code words and preset plans allow complex orders to be transmitted with minimal bandwidth. "Execute Order Alpha" might trigger a detailed operational plan previously loaded into the submarine's safe.

## Comparison to Other Systems

**vs HF Radio:**
- Much longer range (VLF more reliable)
- Penetrates water (HF cannot)
- Much slower (1 WPM vs 20 WPM)
- More stable (less atmospheric interference)
- Harder to jam
- Requires much larger antenna

**vs Voice Radio:**
- Much longer range
- Penetrates water
- Extremely slow vs instant
- Cannot carry voice
- One-way practical (sub doesn't transmit)
- Strategic vs tactical

**vs Satellite Communications:**
- Penetrates water (SATCOM requires antenna above water)
- More reliable in nuclear warfare (no satellites to destroy)
- Much slower
- 1960-1980s: VLF still superior for submarines
- 1990+: SATCOM better for surface ships

## Antenna Requirements

**Shore Stations:**
- Antenna length: 10-30 km arrays
- Power: 1-2 MW transmitters
- Coverage: Global or hemisphere
- Examples: NAA Cutler, Maine (1 million watts)

**Ship-Based:**
- Trailing wire antenna: 500-2000 m
- Requires large power system
- Heavy winch/handling equipment
- Impractical for small ships

**Submarine:**
- Trailing wire antenna: 200-500 m
- Deployed at periscope depth
- Must maintain depth to receive
- Cannot dive deep while receiving

## Upgrade Path

- [[Radio-SATCOM]] - Satellite communications for modern era (1960+)
- [[DataLink-Link11]] - Automated data sharing (1960+)
- [[Encrypted-Comms]] - Add encryption (though speed already limits complexity)

## Compatible With

- Command Bridge or better
- Essential for:
  - Submarines (receive only)
  - Flagship vessels (command fleet)
  - Capital ships with large power systems
- Not practical for:
  - Small ships (weight/power)
  - Fast maneuver vessels (antenna handling)

## Game Balance Notes

VLF represents strategic-level communication - slow but ultra-reliable with global range. It's not for tactical coordination (too slow) but for strategic orders from shore or fleet command. The 30-60 second message delay makes it unsuitable for combat coordination but perfect for "proceed to waypoint" or "execute plan" orders.

The submarine penetration mechanic is VLF's unique feature. Submarines can receive orders while remaining hidden at periscope depth, maintaining stealth while staying in command loop. This enables submarine fleet coordination without requiring dangerous surface exposure.

The high weight (800 kg) and power (50 kW) requirements limit VLF to larger ships and submarines. Small craft cannot carry VLF transmitters, only receive equipment (which is lighter). This creates a command hierarchy where flagships and shore stations broadcast to the fleet.

Players commanding submarines would receive VLF messages as periodic text orders: "PROCEED GRID 45N" or "CONVOY ROUTE SENT" with navigation waypoints. They can acknowledge by surfacing and using HF radio, or remain silent to maintain stealth (one-way communication preferred for SSBNs).
