---
module_id: EW-010
name: Communications Decryption Module
category: support
subcategory: electronic_warfare
era: 1965+
slot_type: support
decryption_capability: advanced
processing_time: variable
requires: [EW-008, EW-009]
weight: 200
crew_required: 2
tags: [support, electronic_warfare, sigint, decryption, crypto, intelligence]
---

# Communications Decryption Module

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | EW-010 |
| **Era** | 1965+ |
| **Category** | Electronic Warfare / SIGINT |
| **Weight** | 200 kg |
| **Power Draw** | 15 kW |
| **Crew Required** | 2 (cryptanalysts) |
| **Requires** | Radio Intercept Standard (EW-008) or SIGINT Suite (EW-009) |

## Description

Specialized cryptanalysis computer for breaking enemy communications encryption. Works in conjunction with radio intercept systems to decode encrypted transmissions. Effectiveness varies based on encryption strength, intercept volume, and processing time. Critical for gaining full intelligence from intercepted enemy communications.

## Effect on Gameplay

**This module enables:**
- Decrypt intercepted Fleet Radio messages
- Decrypt intercepted Secure Radio (partial)
- Decrypt Data Link transmissions (with SIGINT Suite)
- Convert garbled intercepts to readable intelligence
- Break encryption faster with more intercepts

**Requirements:**
- Must have Radio Intercept Standard (EW-008) OR SIGINT Suite (EW-009)
- Cannot function without intercept system providing raw data

## Specifications

| Capability | Performance |
|------------|-------------|
| **Processing Speed** | Variable by encryption |
| **Encryption Types** | Military tactical, fleet codes |
| **Success Rate** | 60-95% depending on encryption |
| **Queue Capacity** | 50 intercepts |
| **Priority Processing** | Automatic (tactical first) |
| **Memory** | Learns patterns over time |

## Decryption Success Rates

| Encryption Type | Time to Decrypt | Success Rate |
|-----------------|-----------------|--------------|
| Basic Fleet Code | 5-10 seconds | 95% |
| Standard Tactical | 15-30 seconds | 85% |
| Secure Radio | 45-90 seconds | 70% |
| Advanced Military | 2-5 minutes | 50% |
| Data Link (partial) | 30-60 seconds | 60% |
| Modern Encrypted | May be impossible | 10-30% |

## Decryption Process

When encrypted intercept is received:
```
DECRYPTION IN PROGRESS
Source: Fleet Radio intercept from 047°
Encryption: Standard Tactical (Japanese)
Progress: ████████░░ 78%
Estimated completion: 12 seconds

[DECRYPTED - 85% confidence]
"All ships turn to course 270. Increase speed to 25 knots.
Enemy contact bearing 135, range 40 kilometers. Prepare for
surface engagement. Flagship will engage first."
```

## Confidence Levels

Decrypted messages show confidence percentage:

| Confidence | Meaning |
|------------|---------|
| 95-100% | Complete decrypt, highly reliable |
| 80-94% | Good decrypt, minor gaps possible |
| 60-79% | Partial decrypt, key words clear |
| 40-59% | Fragmentary, meaning unclear |
| <40% | Failed decrypt, garbled output |

## Pattern Learning

The Decryption Module improves over time:
- Learns enemy encryption patterns
- Builds codebook from successful decrypts
- Faster processing of similar messages
- Recognizes operator habits

```
Learning_Bonus:
- First intercept from source: Baseline speed
- 5+ intercepts: +20% faster decryption
- 20+ intercepts: +40% faster decryption
- 50+ intercepts: +60% faster, higher success rate
```

## Tactical Applications

1. **Real-Time Intelligence**: Know enemy orders as they're given
2. **Contact Verification**: Confirm sighting reports from enemy comms
3. **Intention Analysis**: Understand enemy plans before execution
4. **Fleet Coordination Intel**: Know how enemy forces will maneuver
5. **Ambush Planning**: Position based on decrypted movements

## Example Decrypted Intelligence

**Scenario:** Enemy fleet detected, encrypted communications intercepted

```
DECRYPTED MESSAGE LOG - Last 5 minutes

14:32:05 [Fleet Radio] - Confidence 92%
"Cruiser Division 5, form screening line ahead of battle force"

14:33:22 [Secure Radio] - Confidence 78%
"[Flagship] reports... contact bearing 180... assess as...
[garbled] ...destroyers. Continue approach."

14:34:18 [Fleet Radio] - Confidence 95%
"All ships battle stations. Weapons free on hostile contacts."

14:35:01 [Secure Radio] - Confidence 65%
"[garbled]...air attack...prepare...launch [garbled]...strike"

ASSESSMENT: Enemy fleet moving to engage. Possible air strike
being prepared. Cruiser screen deploying. High confidence
of imminent surface action.
```

## Integration

Works with intercept systems:

| Paired With | Capability |
|-------------|------------|
| Radio Intercept Basic (EW-007) | Cannot pair - insufficient data |
| Radio Intercept Standard (EW-008) | Decrypt Fleet Radio |
| SIGINT Suite (EW-009) | Decrypt all + Data Link partial |

## Limitations

- Cannot decrypt without intercept system
- Processing time may delay tactical intelligence
- Modern encryption may resist decryption entirely
- Requires enemy to actually transmit
- Cannot break one-time pads
- Heavy computational load

## Counter-Measures by Enemy

Enemies can defeat decryption by:
- Maintaining radio silence
- Frequent key changes
- One-time pad encryption
- Using signal lights instead
- Code words and brevity codes
- Burst transmissions

## Historical Notes

Naval cryptanalysis reached its peak importance in WWII. The Allied breaking of German Enigma (ULTRA) and Japanese JN-25 (MAGIC) codes provided decisive intelligence advantages. The Battle of Midway was won in large part because American cryptanalysts broke Japanese codes and knew the attack was coming.

Modern encryption is far more sophisticated, but the intelligence value of breaking enemy communications remains paramount. The electronic battle between encryptors and cryptanalysts continues as a critical dimension of naval warfare.

## Balance Notes

Decryption is powerful but balanced by:
- Requires expensive supporting modules
- Processing time creates delay
- Success not guaranteed
- Enemies can counter with radio discipline
- Does not help against signal lights
