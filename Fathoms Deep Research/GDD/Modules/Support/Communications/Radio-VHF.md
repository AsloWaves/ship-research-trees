---
module_id: COM-007
name: Radio VHF (Post-War)
category: support
subcategory: communications
era: 1950+
nation: Universal
slot_type: support
weight: 150
power_draw: 3
crew_required: 1

# Performance
range: 50                      # km
data_rate: instant
reliability: 95                # percentage
security: low

# Capabilities
voice_capable: true
text_capable: false
data_capable: false            # automated sharing
vision_sharing: true           # shares fog of war

# Requirements
line_of_sight: true
weather_affected: false
crew_required: 1

tags: [communications, voice, radio, vhf, post-war]
---

# Radio VHF (Post-War)

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-007 |
| **Era** | 1950+ |
| **Range** | 50 km |
| **Type** | Voice Radio (VHF) |

## Description

Post-war VHF (Very High Frequency) radio systems improved on WWII-era TBS with better reliability, multiple channels, and clearer signal quality. Operating in the 30-300 MHz range, these systems provide line-of-sight voice communication with excellent clarity. Solid-state electronics (replacing vacuum tubes) made post-war VHF lighter, more reliable, and more power-efficient than earlier systems.

Multiple channel capability allows different tactical nets - one for fleet-wide communication, another for destroyer division coordination, a third for air defense coordination. Squelch circuits eliminate static when no transmission occurs, and improved modulation provides clearer voice quality even in challenging conditions.

## Effect on Multiplayer

**This module enables:**
- Real-time voice communication with allied players
- Vision sharing: **Yes** - Allied radar contacts appear on your displays
- Voice chat: **Yes** - Clear, multi-channel voice communication
- Text messages: No (voice only)
- Multiple channels for different tactical nets
- Quick tactical commands via voice macros
- Coordinated targeting and maneuvers
- Contact reporting in real-time

**Advanced Fleet Coordination:**

Post-war VHF improves on WWII TBS with:
- Multiple channels (separate nets for different purposes)
- Better clarity (clearer voice quality)
- Longer range (improved electronics, better antennas)
- Higher reliability (solid-state electronics)

**Multi-Channel Operation:**
- Channel 1: Fleet-wide tactical net
- Channel 2: Destroyer division coordination
- Channel 3: Air defense coordination
- Channel 4: Logistics/administrative
- Players can switch channels or monitor multiple

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (50 km) |
| Rain/Fog | No effect (radio waves unaffected) |
| Night | No effect (radio works 24/7) |
| Enemy jamming | Can be jammed on specific frequencies |
| Beyond horizon | No signal (line of sight required) |
| Antenna height | +10-15 km (taller masts = longer range) |

## Communication Range

| Configuration | Range | Notes |
|---------------|-------|-------|
| Standard VHF | 50 km | Line of sight, shipboard antenna |
| Extended antenna | 65 km | Taller mast, better propagation |
| Aircraft relay | 200+ km | Aircraft extends range |
| Surface duct | 100+ km | Rare atmospheric conditions |

## Channel Organization

Typical multi-channel setup:
- **Tactical Net**: Fleet-wide coordination
- **Division Net**: Small unit coordination
- **Air Control**: Fighter direction, ASW coordination
- **Administrative**: Logistics, non-tactical traffic
- **Emergency**: Guard frequency for distress

Players can assign team channels to different purposes and switch as needed.

## Tactical Use

1. **Fleet Coordination**: Multi-ship tactical operations
2. **Division Tactics**: Destroyer squadron coordination
3. **Air Defense**: Fighter direction and coordination
4. **ASW Operations**: Coordinated submarine hunting
5. **Amphibious Ops**: Shore bombardment coordination
6. **Rescue Operations**: SAR coordination
7. **Formation Changes**: Real-time maneuvering

## Advantages Over WWII TBS

**Better Technology:**
- Solid-state electronics (no vacuum tubes)
- Multiple channels (was single channel)
- Better selectivity (less interference)
- Improved modulation (clearer voice)
- Lower power consumption
- Higher reliability
- Smaller, lighter equipment

**Tactical Benefits:**
- Can separate nets by function
- Less frequency congestion
- Better frequency management
- Clearer communications in crowded nets

## Limitations

- Line of sight only (50-65 km maximum)
- Enemy can intercept (no encryption standard)
- Can be jammed per channel
- Requires operator attention
- Multiple channels require discipline
- Does not work beyond horizon
- Crowded frequencies in large battles

## Historical Notes

Post-war VHF development focused on reliability and capability. The Korean War demonstrated the need for better tactical coordination, and Vietnam emphasized multi-channel capability for complex operations involving air, surface, and shore coordination.

The transition from vacuum tubes to transistors (1960s) revolutionized tactical radio. Solid-state radios were smaller, lighter, more reliable, and used less power. A destroyer's radio room that required multiple racks of equipment in 1945 could be replaced by compact units by 1965.

NATO standardization in the 1950s-60s ensured allied forces could communicate effectively. Standard frequencies, protocols, and equipment allowed multi-national task forces to coordinate seamlessly. This proved valuable during Cold War deployments where US, British, Canadian, and other allied ships operated together.

The development of frequency-synthesized radios (1970s) allowed instant channel changes without manual tuning, making multi-channel operations practical. Modern VHF can access hundreds of frequencies, though line-of-sight limitations remain.

## Comparison to Other Systems

**vs WWII TBS:**
- Better reliability (solid-state vs tubes)
- Multiple channels (vs single channel)
- Longer range (better electronics)
- Clearer audio (improved modulation)
- Lower weight and power

**vs UHF Radio:**
- Longer range (VHF propagates better)
- Less secure (UHF has more secure modes)
- More congested frequencies
- Better for long-range tactical coordination

**vs HF Radio:**
- Shorter range (VHF vs HF beyond horizon)
- Much clearer audio
- Better for tactical vs strategic
- Line of sight vs over-horizon

**vs Data Link:**
- Voice only (data link automated)
- Faster for simple messages
- More intuitive (natural speech)
- Cannot share complex tactical pictures

## Upgrade Path

- [[Radio-UHF]] - UHF tactical radio with secure modes (1960+)
- [[Encrypted-Comms]] - Add secure voice encryption (1970+)
- [[DataLink-Link11]] - Add automated data sharing (1960+)
- [[Radio-SATCOM]] - Add beyond line-of-sight capability (1970+)

## Compatible With

- Director Bridge (basic integration)
- CIC Bridge (full integration with combat information center)
- Modern Bridge (full integration)
- All radar systems (contact sharing)
- Fire Control Directors (targeting coordination)
- Data Link systems (voice + data)

## Multi-Channel Tactics

**Effective Channel Management:**

Fleet operations might use:
- **Channel 1 (Tactical)**: Commander coordinates all ships
- **Channel 2 (Screen)**: Destroyers coordinate ASW screen
- **Channel 3 (Air Defense)**: CAP coordination
- **Channel 4 (Logistics)**: Replenishment coordination

Players monitor primary channel continuously, switch to secondary as needed. Modern radios can monitor two channels (primary + guard).

**Channel Discipline:**
- Use correct channel for traffic type
- Keep messages brief and clear
- Use voice procedures (over, out, etc.)
- Switch to administrative channel for non-tactical traffic
- Emergency calls on guard frequency

## Game Balance Notes

Post-war VHF improves on WWII TBS without fundamentally changing the tactical communication model. The key upgrade is multiple channels, allowing players to organize communication effectively. A destroyer division can coordinate on their channel without cluttering the fleet-wide tactical net.

The 50 km range (vs 20 km for TBS) reflects improved electronics and antennas. This allows better coordination of dispersed forces while maintaining the line-of-sight limitation that keeps tactical radio from becoming strategic radio.

Multi-channel operation creates interesting gameplay. Players must decide which channel to monitor, when to switch channels, and how to organize team communication. A task force commander might assign:
- Channel 1: All ships (fleet orders)
- Channel 2: Destroyers (screen coordination)
- Channel 3: Cruisers (gunfire support)
- Channel 4: Carriers (air operations)

This allows specialized communication without everyone hearing everything, reducing noise and improving coordination. However, it requires discipline - using the wrong channel or missing traffic on your assigned channel can cause problems.
