---
module_id: COM-003
name: Flag Semaphore
category: support
subcategory: communications
era: 1890+
nation: Universal
slot_type: support
weight: 10
crew_required: 1

# Performance
range: 3                       # km
data_rate: fast
reliability: 90                # percentage
security: none

# Capabilities
voice_capable: false
text_capable: true
data_capable: false            # automated sharing
vision_sharing: false          # manual text reports only

# Requirements
line_of_sight: true
weather_affected: true
crew_required: 1

tags: [communications, visual, flags, semaphore, fast]
---

# Flag Semaphore

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-003 |
| **Era** | 1890+ |
| **Range** | 3 km |
| **Type** | Visual Signaling |

## Description

Flag semaphore uses two handheld flags held in specific positions to represent letters and numbers. Unlike International Code signals that hoist flags on halyards, semaphore signals are made by a signalman holding flags at arm's length in various positions. Each position represents a different letter, allowing rapid letter-by-letter spelling of messages.

Semaphore is the fastest visual communication method, with skilled operators achieving 25-30 words per minute - comparable to Morse code but requiring no equipment beyond two flags. However, the short range (3 km maximum) and requirement for the signalman to be visible limit its use to close-range tactical situations.

## Effect on Multiplayer

**This module enables:**
- Very fast text communication with visible allies
- Vision sharing: **No** - Manual contact reports only
- Voice chat: No - Visual semaphore only
- Text messages: **Yes** - Very fast (3-5 seconds per message)
- Quick tactical updates
- Useful for brief, urgent messages

**Fast but Short Range:**
Semaphore is the fastest visual signaling method, ideal for short, urgent messages between ships in formation. "Turn now!" or "Enemy sighted!" can be transmitted faster than by any other pre-radio method.

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (3 km) |
| Rain/Fog | Reduced to 1 km |
| Night | Ineffective (cannot see flag positions) |
| Enemy jamming | Cannot be jammed |
| Wind | Can make signaling difficult |
| Bright sunlight | May reduce contrast visibility |

## Communication Speed

| Operator Skill | Words/Minute | Message Delay |
|----------------|--------------|---------------|
| Basic | 10 WPM | 8 seconds |
| Trained | 20 WPM | 5 seconds |
| Expert | 30 WPM | 3 seconds |

Semaphore is the fastest visual signaling method, approaching Morse code speeds for short messages.

## Message Types

Best for short, urgent messages:
- **Immediate Orders**: "TURN 15 RIGHT"
- **Alerts**: "TORPEDO STARBOARD"
- **Status**: "READY"
- **Confirmations**: "UNDERSTOOD"
- **Quick Reports**: "ENEMY AHEAD 5000"

Less effective for long complex messages (use signal flags or wireless instead).

## Tactical Use

1. **Formation Changes**: Instant maneuvering orders to nearby ships
2. **Combat Alerts**: Quick warnings during engagement
3. **Acknowledgments**: Confirm receipt of orders
4. **Status Updates**: Brief status reports
5. **Close Coordination**: Destroyer division tactics
6. **Backup to Radio**: When radio is jammed or failed
7. **Training Exercise**: Communication during peacetime drills

## Advantages

- Fastest visual signaling method
- No power required
- Extremely lightweight (just two flags)
- Cannot be jammed electronically
- Very simple equipment
- Easy to repair (just replace flags)
- Standard naval skill
- Faster than flag hoists or signal lamps for short messages

## Limitations

- Very short range (3 km maximum)
- Daylight only (cannot see positions at night)
- Requires line of sight
- Weather dependent
- One ship at a time (signalman can only face one direction)
- Signalman must be visible (exposed on deck)
- Tiring for operator (holding flags extended)
- Enemy can read signals
- Impractical for long messages

## Historical Notes

Flag semaphore was developed in the late 1700s for land telegraphy and adapted for naval use in the 1800s. The system uses positions based on clock positions, with the signalman's body as the center. Two flags in different positions spell out letters rapidly.

The Royal Navy standardized semaphore training for all deck personnel. During fleet exercises, destroyers could receive maneuvering orders from the flagship faster than by flag hoist. The system remained useful throughout the 20th century for close-range communication during radio silence or equipment failure.

Semaphore's main disadvantage - short range - limited its tactical impact. It worked well for destroyer divisions operating close together but couldn't coordinate widely dispersed fleet units. The advent of wireless telegraph (1900+) and voice radio (1940+) made semaphore obsolete for primary communication, though it remained a backup skill.

## Comparison to Other Systems

**vs Flag Signals:**
- Much faster (3 seconds vs 15-30 seconds)
- Much shorter range (3 km vs 5-10 km)
- Better for urgent messages
- Worse for preset complex orders
- Requires skilled operator actively signaling

**vs Signal Lamp:**
- Slightly faster for short messages
- Much shorter range (3 km vs 15 km)
- Daylight only (lamp works at night)
- Less tiring (lamp vs holding flags)
- No power required

**vs Wireless Telegraph:**
- Same speed for short messages
- Much shorter range (3 km vs 500 km)
- No interception risk (radio gives away position)
- Line of sight required
- No equipment weight

## Upgrade Path

- [[Signal-Lamp]] - For night operations (1890+)
- [[Wireless-HF]] - For long-range communication (1910+)
- [[Radio-TBS]] - For instant voice coordination (1942+)

## Compatible With

- All bridge types (all eras)
- Useful as backup communication on any vessel
- Particularly valuable for:
  - Small craft (destroyers, PT boats)
  - Formation operations
  - Training exercises
  - Radio silence operations

## Game Balance Notes

Semaphore fills a niche as the fastest visual signaling but with very limited range. It's ideal for close-formation destroyer divisions or quick tactical updates during engagement. The 3-second transmission time for expert operators makes it competitive with radio for brief messages like "Turn now!" or "Torpedo warning!"

The daylight limitation and short range keep semaphore from competing with radio systems. It's a specialized tool for specific situations rather than primary communication. Players might use semaphore when:
- Radio is jammed
- Maintaining radio silence
- Very close formation maneuvers
- Quick acknowledgments needed
- Emergency backup communication

The system rewards skilled operators with faster message speeds, creating a minor skill-based gameplay element. However, the range limitation ensures semaphore remains situational rather than dominant.
