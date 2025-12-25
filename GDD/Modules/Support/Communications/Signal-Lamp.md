---
module_id: COM-002
name: Signal Lamp (Aldis Lamp)
category: support
subcategory: communications
era: 1890+
nation: Universal
slot_type: support
weight: 25
crew_required: 1

# Performance
range: 15                      # km (Basic), 20 km (Advanced)
data_rate: medium
reliability: 85                # percentage
security: visual_only          # Cannot be intercepted electronically

# Beam Characteristics
beam_width_basic: 35           # degrees - wider beam, easier to see from sides
beam_width_advanced: 15        # degrees - narrow beam, more directional

# Capabilities
voice_capable: false
text_capable: true
data_capable: false            # automated sharing
vision_sharing: false          # manual text reports only
electronic_intercept: impossible  # SIGINT cannot intercept visual signals

# Requirements
line_of_sight: true
weather_affected: true

tags: [communications, visual, lamp, morse, universal, secure]
---

# Signal Lamp (Aldis Lamp)

## Overview
| Attribute | Basic Signal Lamp | Advanced Signal Lamp |
|-----------|-------------------|----------------------|
| **Module ID** | COM-002 | COM-002A |
| **Era** | 1890+ | 1940+ |
| **Range** | 15 km | 20 km |
| **Beam Width** | 35° cone | 15° cone |
| **Type** | Visual Signaling | Directional Visual |

## Description

The signal lamp (commonly called Aldis lamp after its inventor) uses a focused beam of light to transmit Morse code messages between ships. A trigger mechanism interrupts the light beam to create dots and dashes. Unlike flag signals limited to daylight, signal lamps work at night and in low visibility. The focused beam can reach much farther than flags (up to 15-20 km) and is harder for distant observers to intercept.

Signal lamps became standard naval equipment from the 1890s onward. They enabled night operations and provided backup communication when radio silence was required. The simple, reliable technology remains in use today as an emergency communication method and for covert operations.

**Critical Security Feature:** Signal lamps transmit via visible light, making them **completely immune to electronic interception**. SIGINT systems, radio intercept equipment, and decryption modules cannot detect or decode signal lamp communications. Only visual observation can intercept these messages.

## Effect on Multiplayer

**This module enables:**
- Text-based communication with allies (line of sight)
- Vision sharing: **No** - Manual contact reports only
- Voice chat: No - Text messages via Morse
- Text messages: **Yes** - Delayed by Morse encoding (5-10 seconds)
- Contact reporting via text
- Useful for radio silence operations
- **Complete immunity to electronic interception**

**Limited Coordination:**
Signal lamps provide point-to-point communication with visible allies. Messages are sent via Morse code, requiring operator skill. The focused beam means only the intended recipient sees the message (unlike flag signals visible to all nearby ships).

## Directional Beam Mechanics

Signal lamps project light in a cone. The beam width determines who can see the transmission:

### Basic Signal Lamp (COM-002)
```
Beam Width: 35° cone

         Target Ship
            △
           /|\
          / | \
         /  |  \
        / 35° |  \
       /    |    \
      /_____|_____\
         Sender

Enemy ships within the 35° cone may visually spot
the flashing light. Ships outside the cone cannot.
```

**Basic Lamp Characteristics:**
- Wider beam easier to aim (more forgiving)
- Can be spotted from sides more easily
- Best for daylight operations when light is less visible
- Sufficient for most tactical communication

### Advanced Signal Lamp (COM-002A)
```
Beam Width: 15° cone

         Target Ship
            △
            |
           /|\
          / | \
         /15°|  \
         \___|___/
         Sender

Narrow beam is much harder to intercept.
Ships must be almost directly behind target to see.
```

**Advanced Lamp Characteristics:**
- Narrow beam requires more precise aiming
- Extremely difficult to intercept from flanks
- Longer range (20 km vs 15 km) due to focused light
- Ideal for covert operations and night actions
- Requires 1940s-era optics technology

### Visual Interception Rules

Enemy ships CAN intercept signal lamp messages IF:
1. They are within the beam cone (35° or 15°)
2. They are within range (15 km or 20 km)
3. They have line of sight to the sender
4. Weather/visibility allows observation
5. They have a crew member watching that direction

**Interception Probability by Position:**
| Position Relative to Beam | Basic (35°) | Advanced (15°) |
|---------------------------|-------------|----------------|
| Directly in beam path | 90% | 90% |
| Edge of beam cone | 60% | 40% |
| Just outside cone | 10% | 5% |
| Well outside cone | 0% | 0% |
| Behind sender | 0% | 0% |

### Secure vs. Radio Comparison

| Security Aspect | Signal Lamp | Radio (TBS/Fleet) |
|-----------------|-------------|-------------------|
| Electronic intercept | **IMPOSSIBLE** | Can be intercepted |
| Direction finding | Cannot track | Reveals position |
| Decryption | N/A (visual) | Can be decoded |
| Visual intercept | Within beam only | N/A |
| Counter-measure | Stay out of cone | Radio silence |

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
8. **SIGINT-Proof Communication**: Immune to radio intercept systems

### When to Use Signal Lamp vs Radio

| Situation | Recommended |
|-----------|-------------|
| Enemy has SIGINT capability | **Signal Lamp** |
| Need to maintain stealth | **Signal Lamp** |
| Long range coordination (>20 km) | Radio |
| Multi-ship broadcast | Radio |
| Speed is critical | Radio |
| Night covert operations | **Advanced Signal Lamp** |
| Enemy between you and target | Radio (lamp may be intercepted) |

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
- **SIGINT-proof** (radio can be intercepted)

**vs Encrypted Radio (UHF):**
- Shorter range
- Slower
- Cannot be electronically intercepted at all
- Encrypted radio still reveals you're transmitting
- Signal lamp reveals nothing to electronic sensors

## Upgrade Path

- [[Signal-Lamp-Advanced]] (COM-002A) - Narrow beam (15°) for covert operations (1940+)
- [[Wireless-HF]] - Long-range wireless telegraph (1910+)
- [[Radio-TBS]] - Voice radio for instant communication (1942+)

## Counter-SIGINT Value

In an era where SIGINT capabilities are increasingly common, signal lamps provide a completely secure communication channel:

| SIGINT System | Can Intercept Radio? | Can Intercept Signal Lamp? |
|---------------|---------------------|---------------------------|
| Radio Intercept Basic (EW-007) | TBS voice only | **NO** |
| Radio Intercept Standard (EW-008) | HF/VHF fleet radio | **NO** |
| SIGINT Suite (EW-009) | All radio + Data Link detection | **NO** |
| Decryption Module (EW-010) | Can decode encrypted radio | **NO** |

Signal lamps are the **only** communication method completely immune to electronic warfare interception. This makes them invaluable for:
- Coordinating attacks without revealing intentions
- Operating near enemy SIGINT platforms
- Maintaining tactical surprise
- Emergency communication when radio is compromised
