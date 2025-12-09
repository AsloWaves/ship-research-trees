---
module_id: COM-002
name: Signal Lamp (Aldis Lamp)
category: support
subcategory: communications
era: 1890+
nation: Universal
slot_type: support
weight: 25
power_draw: 0.5
crew_required: 1

# Performance
range: 15                      # km
data_rate: medium
reliability: 85                # percentage
security: none

# Capabilities
voice_capable: false
text_capable: true
data_capable: false            # automated sharing
vision_sharing: false          # manual text reports only

# Requirements
line_of_sight: true
weather_affected: true

tags: [communications, visual, lamp, morse, universal]
---

# Signal Lamp (Aldis Lamp)

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-002 |
| **Era** | 1890+ |
| **Range** | 15 km |
| **Type** | Visual Signaling |

## Description

The signal lamp (commonly called Aldis lamp after its inventor) uses a focused beam of light to transmit Morse code messages between ships. A trigger mechanism interrupts the light beam to create dots and dashes. Unlike flag signals limited to daylight, signal lamps work at night and in low visibility. The focused beam can reach much farther than flags (up to 15 km) and is harder for distant observers to intercept.

Signal lamps became standard naval equipment from the 1890s onward. They enabled night operations and provided backup communication when radio silence was required. The simple, reliable technology remains in use today as an emergency communication method and for covert operations.

## Effect on Multiplayer

**This module enables:**
- Text-based communication with allies (line of sight)
- Vision sharing: **No** - Manual contact reports only
- Voice chat: No - Text messages via Morse
- Text messages: **Yes** - Delayed by Morse encoding (5-10 seconds)
- Contact reporting via text
- Useful for radio silence operations

**Limited Coordination:**
Signal lamps provide point-to-point communication with visible allies. Messages are sent via Morse code, requiring operator skill. The focused beam means only the intended recipient sees the message (unlike flag signals visible to all nearby ships).

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (15 km) |
| Rain/Fog | Reduced to 3-5 km |
| Night | Full range (actually better visibility) |
| Enemy jamming | Cannot be jammed electronically |
| Daylight | Harder to see in bright sunlight |
| Darkness | Easier to see, full brightness usable |

## Communication Speed

| Operator Skill | Words/Minute | Message Delay |
|----------------|--------------|---------------|
| Basic | 8 WPM | 10 seconds |
| Trained | 15 WPM | 7 seconds |
| Expert | 25 WPM | 5 seconds |

Signal lamps are slightly faster than flags but slower than wireless telegraph due to the manual trigger operation.

## Message Types

Typical signal lamp messages:
- **Contact Reports**: "ENEMY AHEAD"
- **Formation Orders**: "TURN TOGETHER 15 DEGREES"
- **Status Updates**: "READY FOR ACTION"
- **Night Challenges**: "IDENTIFY YOURSELF"
- **Distress**: "REQUIRE ASSISTANCE"
- **Covert Messages**: Point-to-point, hard to intercept

## Tactical Use

1. **Night Operations**: Primary visual communication after dark
2. **Radio Silence**: Communicate without breaking radio silence
3. **Covert Operations**: Focused beam harder to intercept than radio
4. **Challenge/Reply**: Identify ships at night
5. **Local Coordination**: Quick messages to nearby ships
6. **Emergency Communication**: When radio fails or is jammed
7. **Backup System**: Always available, no power dependency

## Limitations

- Requires line of sight
- Weather dependent (fog/rain reduces range)
- One ship at a time (point-to-point only)
- Slower than voice radio
- Requires trained Morse operator
- Must aim lamp at recipient ship
- Enemy can see bright light (reveals position)
- Difficult in bright sunlight

## Historical Notes

Arthur Cyril Webb Aldis invented the portable signal lamp in 1867, but practical naval versions emerged in the 1890s. The Aldis lamp became standard equipment on all warships, used for everything from routine messages to challenge/reply identification at night.

During WWI and WWII, signal lamps were essential for night operations when radio silence was required. Destroyers on convoy escort used lamps to communicate with merchant ships without alerting U-boats. At the Second Battle of Guadalcanal (1942), USS Washington used a signal lamp to warn USS South Dakota of approaching Japanese ships.

Signal lamps remained relevant even after radio became common. They provide silent communication, cannot be jammed, and work when all else fails. Modern navies still carry signal lamps as backup and for covert operations.

## Comparison to Other Systems

**vs Flag Signals:**
- Works at night (flags do not)
- Longer range (15 km vs 5 km)
- Works in lower visibility
- Slightly slower (trigger mechanism)
- Point-to-point (more secure)

**vs Wireless Telegraph:**
- Maintains radio silence
- Cannot be jammed electronically
- Shorter range (15 km vs 500+ km)
- Line of sight required
- Similar speed (both Morse)

**vs Voice Radio:**
- Much shorter range
- Slower (Morse encoding)
- Cannot be jammed
- Maintains radio silence
- More covert

## Upgrade Path

- [[Wireless-HF]] - Long-range wireless telegraph (1910+)
- [[Radio-TBS]] - Voice radio for instant communication (1942+)
