---
module_id: COM-006
name: Radio TBS (Talk Between Ships)
category: support
subcategory: communications
era: 1942+
nation: USA
slot_type: support
weight: 200
crew_required: 1

# Performance
range: 20                      # km
data_rate: instant
reliability: 90                # percentage
security: none

# Capabilities
voice_capable: true
text_capable: false
data_capable: false            # automated sharing
vision_sharing: true           # shares fog of war

# Requirements
line_of_sight: true
weather_affected: false
crew_required: 1

tags: [communications, voice, radio, wwii, team]
---

# Radio TBS (Talk Between Ships)

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-006 |
| **Era** | 1942+ |
| **Range** | 20 km |
| **Type** | Voice Radio (VHF) |

## Description

Talk Between Ships (TBS) was the US Navy's VHF voice radio system introduced in 1942. Operating on very high frequency (VHF), TBS provided clear, real-time voice communication between ships in a task force. Unlike high-frequency radios that could reach hundreds of miles, TBS was deliberately short-range to reduce interception risk while enabling instant tactical coordination within visual and near-visual range.

TBS revolutionized naval tactics by allowing immediate voice commands during battle. Task force commanders could adjust formations, coordinate attacks, and respond to threats in real-time without the delays of flag signals or Morse code.

## Effect on Multiplayer

**This module enables:**
- Real-time voice communication with allied players
- Vision sharing: **Yes** - Allied radar contacts appear on your displays
- Voice chat: **Yes** - Direct voice communication
- Text messages: No (voice only)
- Quick tactical commands via voice macros
- Coordinated targeting and maneuvers
- Contact reporting in real-time

**The Vision Sharing Mechanic:**

Without TBS:
- You only see YOUR sensor contacts
- Allies appear as dots on map
- No tactical coordination possible

With TBS:
- Allied radar contacts appear on YOUR displays
- Combined sensor coverage
- True fleet operations enabled
- Destroyer scouts for battleship
- Picket ships warn carrier group

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (20 km) |
| Rain/Fog | No effect (radio waves unaffected) |
| Night | No effect (radio works 24/7) |
| Enemy jamming | Can be jammed on frequency |

## Communication Range

| Type | Range | Notes |
|------|-------|-------|
| TBS (VHF) | 20 km | Line of sight, clear voice |
| Beyond horizon | No signal | VHF requires line of sight |
| Antenna height | +5-10 km | Taller masts = longer range |

## Tactical Use

1. **Scouting**: Destroyer shares contacts with battleship
2. **Air Defense**: Picket ships warn carrier group of air raids
3. **Coordination**: Synchronized torpedo attacks
4. **Rescue**: Communicate survivor positions
5. **Formation Changes**: Real-time maneuvering orders
6. **Target Assignment**: "I'll take left ship, you take right"

## Limitations

- Line of sight only (20-30 km maximum)
- Enemy can intercept (no encryption)
- Can be jammed
- Requires operator attention
- Voice discipline required (chatter = confusion)
- Limited channels (crowded frequencies in large battles)
- Does not work beyond horizon

## Historical Notes

TBS was developed by the US Navy in the late 1930s and became operational in 1942. Operating in the 60 MHz band, TBS proved invaluable in the Pacific War. The system enabled complex multi-carrier task force operations that would have been impossible with previous communication methods.

Admiral Spruance could coordinate entire carrier groups during the Battle of the Philippine Sea. TBS allowed fighter directors to vector CAP fighters onto incoming raids, escorts to coordinate ASW sweeps, and screening destroyers to adjust formations instantly based on submarine threats.

The Japanese largely lacked equivalent systems, relying on longer-range HF radio and traditional flag signals. This communications gap contributed to US tactical superiority, particularly in fast-developing night actions and air defense coordination.

## Comparison to Other Systems

**vs Flag Signals:**
- Much faster (instant vs minutes)
- Works at night and in poor visibility
- Beyond visual range (up to 20 km)
- Can be intercepted by enemy

**vs Wireless Telegraph (Morse):**
- Instant (no encoding delay)
- Intuitive (natural speech)
- Better for complex tactical instructions
- Same interception risk

**vs HF Radio:**
- Shorter range (harder to intercept)
- Clearer signal quality
- Better for local tactical coordination
- Cannot reach distant stations

## Upgrade Path

- [[Encrypted-Comms]] - Adds secure encrypted channel (1943+)
- [[Radio-VHF]] - Improved post-war VHF with more channels (1950+)
- [[Radio-UHF]] - UHF tactical radio with frequency hopping (1960+)

## Compatible With

- Director Bridge (basic integration)
- CIC Bridge (full integration with combat information center)
- Modern Bridge (full integration)
- All radar systems (contact sharing)
- Fire Control Directors (targeting coordination)

## Game Balance Notes

TBS is the first "true" fleet coordination tool. It enables the transition from individual ship combat to integrated task force operations. Players with TBS can share radar contacts, coordinate attacks, and function as a unified fighting force. This represents the historical advantage US task forces had in WWII.

The 20 km range limitation keeps TBS tactical rather than strategic. Ships must stay relatively close to maintain communications, encouraging formation play while preventing distant super-coordination.
