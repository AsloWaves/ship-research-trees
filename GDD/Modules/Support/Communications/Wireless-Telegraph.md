---
module_id: SUP-011
name: Wireless Telegraph
category: support
subcategory: communication
era: 1900-1950
slot_type: support
weight: 500
crew_required: 2
tags: [support, communication, radio, morse, early]
---

# Wireless Telegraph

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | SUP-011 |
| **Era** | 1900-1950 |
| **Category** | Communication |
| **Weight** | 500 kg |
| **Crew Required** | 2 (operator + assistant) |

## Description

Long-range radio communication using Morse code. Enabled over-the-horizon communication for the first time in naval history. Ships could coordinate without visual contact and receive orders from shore stations.

## Effect on UI

When installed with Enclosed Bridge+:
- **Text Chat**: Enabled (with delay)
- **Message Delay**: 5-15 seconds (encoding/decoding)
- **Range**: Unlimited (HF can reach worldwide)

## Fog of War Effect

Basic information sharing:
```
Link Type:            Text messages (delayed)
Contact Sharing:      Manual reports only
Position Updates:     By coordinates
Real-time:            No (Morse code delay)
```

**Not as good as voice**, but first radio capability.

## Communication Speed

| Operator Skill | Words/Minute | Delay |
|----------------|--------------|-------|
| Basic | 10 WPM | 15 sec |
| Trained | 20 WPM | 10 sec |
| Expert | 30+ WPM | 5 sec |

## Message Types

Typical naval messages:
- Contact reports ("Enemy battleship bearing 045, range 20000")
- Position reports
- Orders from flagship
- Distress signals

## Limitations

- Not real-time (Morse encoding)
- Requires trained operators
- Can be intercepted
- Can be direction-found (enemy locates you)
- Atmospheric interference possible

## Historical Notes

Wireless telegraphy transformed naval warfare. At Jutland (1916), Jellicoe received contact reports from cruiser screens, allowing fleet deployment before visual contact. However, the British also intercepted German signals, providing intelligence advantages. The tradeoff: transmitting reveals your presence.

## Security Note

**Enemy can:**
- Intercept your messages
- Direction-find your position
- Decode messages (if not encrypted)

## Upgrade Path

→ [[Voice-Radio]] (1930+)
→ [[Encrypted-Comms]] (1940+)

## Compatible With

- Enclosed Bridge+
- All WWII+ bridges
- Essential for fleet operations
