---
module_id: COM-004
name: Wireless Telegraph (HF)
category: support
subcategory: communications
era: 1910+
nation: Universal
slot_type: support
weight: 500
crew_required: 2

# Performance
range: 500                     # km (can reach 2000+ km in good conditions)
data_rate: slow
reliability: 75                # percentage (atmospheric dependent)
security: low

# Capabilities
voice_capable: false
text_capable: true
data_capable: false            # automated sharing
vision_sharing: false          # manual text reports only

# Requirements
line_of_sight: false
weather_affected: true
crew_required: 2

tags: [communications, wireless, morse, hf, early]
---

# Wireless Telegraph (HF)

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-004 |
| **Era** | 1910+ |
| **Range** | 500+ km |
| **Type** | Wireless Telegraph (Morse Code) |

## Description

High Frequency (HF) wireless telegraphy using Morse code enabled the first over-the-horizon naval communications. Ships could coordinate without visual contact and receive orders from shore stations hundreds or thousands of miles away. The system uses long-wave and medium-wave radio frequencies that bounce off the ionosphere, allowing global communication with sufficient power.

Unlike visual signals limited to a few miles, HF radio transformed naval strategy by enabling fleet-wide coordination and strategic command from shore. However, the technology requires skilled operators to encode and decode Morse code, creating significant message delays compared to later voice systems.

## Effect on Multiplayer

**This module enables:**
- Text-based communication with allies (with delay)
- Vision sharing: **No** - Manual contact reports only
- Voice chat: No - Text messages only
- Text messages: **Yes** - Delayed by Morse encoding (5-15 seconds)
- Contact reporting via text coordinates
- Orders from fleet command (shore/flagship)

**Limited Coordination:**
Unlike voice radio, wireless telegraph does not provide automatic vision sharing. Players must manually type contact reports ("Enemy battleship bearing 045, range 20000 yards"). This simulates the slower, more deliberate communication of the pre-voice era.

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (500+ km) |
| Rain/Fog | No direct effect |
| Night | Improved range (ionosphere skip) |
| Enemy jamming | Can be jammed on frequency |
| Atmospheric storms | Severe interference possible |
| Solar activity | Can disrupt ionosphere propagation |

## Communication Speed

| Operator Skill | Words/Minute | Message Delay |
|----------------|--------------|---------------|
| Basic | 10 WPM | 15 seconds |
| Trained | 20 WPM | 10 seconds |
| Expert | 30+ WPM | 5 seconds |

Typical messages:
- Contact report: 10-15 seconds
- Position update: 5-10 seconds
- Complex orders: 30-60 seconds

## Message Types

Standard naval wireless messages:
- **Contact Reports**: "ENEMY BATTLESHIP BEARING 045 RANGE 20000"
- **Position Reports**: "MY POSITION 34N 120W COURSE 270 SPEED 15"
- **Orders from Flagship**: "FORM LINE AHEAD COURSE 180"
- **Distress Signals**: "SOS TORPEDOED SINKING POSITION..."
- **Intelligence Reports**: "ENEMY FLEET SIGHTED..."

## Tactical Use

1. **Long-Range Coordination**: Contact ships beyond visual range
2. **Shore Communication**: Receive strategic orders from command
3. **Fleet Deployment**: Coordinate rendezvous points
4. **Intelligence Sharing**: Report enemy movements to fleet
5. **Radio Silence**: Maintain by receiving only (direction finding risk)
6. **Backup Communication**: When other systems fail

## Limitations

- Not real-time (Morse encoding delay)
- Requires two trained operators
- Can be intercepted by enemy (security risk)
- Can be direction-found (reveals your position)
- Atmospheric interference possible
- Cannot share sensor contacts automatically
- Slower than voice for complex messages
- Enemy can jam frequency
- Requires significant power

## Historical Notes

Wireless telegraphy transformed naval warfare starting around 1900. At the Battle of Jutland (1916), Admiral Jellicoe received wireless contact reports from cruiser screens, allowing the Grand Fleet to deploy before visual contact with the German High Seas Fleet. The British also intercepted German wireless signals, providing crucial intelligence advantages through Room 40's decryption efforts.

However, wireless was a double-edged sword. Transmitting revealed your presence. Direction-finding stations could locate transmitting ships, and enemy cryptanalysts could decode messages. Admiral Togo used wireless intercepts to locate the Russian fleet before Tsushima (1905).

The technology improved throughout WWI and WWII. By 1940, HF wireless could reliably reach across oceans. U-boats reported convoy positions to headquarters, which coordinated wolf pack attacks. Allied intelligence intercepted these signals, enabling Ultra decrypts that turned the tide of the Battle of the Atlantic.

## Security Considerations

**Enemy Can:**
- Intercept your messages (unless encrypted)
- Use direction-finding to locate your position
- Decode messages (if not encrypted or cipher is broken)
- Jam your frequency

**Radio Silence:**
Fleets often maintained radio silence, receiving orders but not transmitting, to avoid detection. This limited coordination but preserved stealth.

## Comparison to Other Systems

**vs Flag Signals:**
- Much longer range (500+ km vs 5 km)
- Works at night and in any visibility
- Beyond visual range
- Much slower than visual flag reading
- Can be intercepted

**vs Voice Radio:**
- Longer range (HF travels further than VHF)
- Much slower (Morse encoding)
- More complex to use
- Same interception risk
- Better for long-distance communication

**vs Modern Data Links:**
- No automated data sharing
- Manual message composition
- Operator skill dependent
- Cannot share sensor pictures

## Upgrade Path

- [[Radio-TBS]] - VHF voice radio for local tactical communication (1942+)
- [[Radio-VHF]] - Post-war VHF voice systems (1950+)
- [[Encrypted-Comms]] - Add encryption to prevent interception (1940+)
- [[Wireless-VLF]] - Very low frequency for submarine communication (1920+)

## Compatible With

- Enclosed Bridge or better
- All bridge types from 1900+ era
- Essential for WWI/early WWII fleet operations
- Code Room (for encryption/decryption)
- Direction Finding Equipment (for locating enemy transmitters)

## Game Balance Notes

Wireless Telegraph represents the transition from visual-only to electronic communication. It's slower than voice radio but enables coordination beyond visual range. The message delay (5-15 seconds) encourages players to use concise, preset messages rather than extended conversation.

The interception and direction-finding mechanics create risk/reward decisions: Do you break radio silence to report a contact, knowing the enemy might locate you? This simulates the communication dilemmas faced by WWI and WWII commanders.

The system does not provide automatic vision sharing, requiring players to manually communicate what they see. This creates a gameplay distinction from later voice radio systems and rewards clear communication skills.
