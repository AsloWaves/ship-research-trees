---
module_id: EW-007
name: Basic Radio Intercept Receiver
category: support
subcategory: electronic_warfare
era: 1940-1970
slot_type: support
intercept_range: 30
intercept_types: [TBS, voice_radio]
decryption: none
weight: 150
crew_required: 2
tags: [support, electronic_warfare, sigint, intercept, radio, voice]
---

# Basic Radio Intercept Receiver

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | EW-007 |
| **Era** | 1940-1970 |
| **Category** | Electronic Warfare / SIGINT |
| **Weight** | 150 kg |
| **Crew Required** | 2 (operator + linguist) |

## Description

Basic radio intercept receiver capable of monitoring enemy voice radio communications. This system passively listens to TBS (Talk Between Ships) and other short-range voice radio transmissions, allowing intelligence gathering on enemy movements and intentions. The operator must manually tune to enemy frequencies and a linguist is needed to understand foreign language transmissions.

## Effect on Gameplay

**This module enables:**
- Intercept enemy TBS voice communications within range
- Hear enemy voice chat when they use unsecured radio
- Detect when enemies are using radio (even if you can't understand)
- No decryption capability - only intercepts unencrypted voice

**Intelligence Gathered:**
- Enemy voice communications (if using TBS/voice radio)
- Direction to radio source (bearing only)
- Signal strength (indicates approximate range)

## Specifications

| Capability | Performance |
|------------|-------------|
| **Intercept Range** | 30 km (1.5× TBS range) |
| **Frequency Coverage** | 60-80 MHz (TBS band) |
| **Bearing Accuracy** | ±20 degrees |
| **Response Time** | 3-5 seconds to lock signal |
| **Simultaneous Channels** | 1 |
| **Recording** | None (real-time only) |

## What You Can Intercept

| Enemy Comm Type | Intercept Result |
|-----------------|------------------|
| TBS Voice Radio | Full voice audio heard |
| Local Voice Chat | Cannot intercept (too short range) |
| Fleet Radio (HF) | Cannot intercept (wrong frequency) |
| Encrypted Radio | Detect transmission only |
| Signal Light | Cannot intercept |
| Data Link | Cannot intercept |

## Tactical Applications

1. **Fleet Intelligence**: Hear enemy coordination in real-time
2. **Ambush Warning**: Enemy radio chatter reveals their presence
3. **Contact Confirmation**: Verify contact reports with enemy comms
4. **Tactical Advantage**: Know enemy intentions before they act
5. **Language Intelligence**: If you understand the language, know exact plans

## Limitations

- Voice only - no text/data intercept
- Single frequency at a time (must tune manually)
- No decryption - encrypted comms are garbled
- Requires linguist for foreign languages
- Short range compared to HF intercept
- Cannot determine exact location (bearing only)
- Passive only - cannot jam or interfere

## Operator Requirements

The radio intercept operator must:
- Manually scan frequencies to find enemy transmissions
- Maintain lock on active communications
- Report intelligence to bridge
- Work with linguist if enemy speaks different language

**Crew Skills:**
| Skill Level | Effect |
|-------------|--------|
| Basic | Slow tuning, may miss transmissions |
| Trained | Reliable intercept, recognizes common frequencies |
| Expert | Quick tuning, can monitor multiple frequencies rapidly |

## Historical Notes

Radio intercept capabilities emerged during WWI and became critical in WWII. The British Y-Service and American Radio Intelligence monitored Axis communications throughout the war. Even without breaking codes, traffic analysis revealed enemy fleet movements - increased radio chatter indicated impending operations.

Japanese naval codes were famously broken (MAGIC/ULTRA), but even basic radio intercept provided valuable intelligence. At Midway (1942), American radio intercept detected increased Japanese activity, confirming the target before cryptanalysis revealed detailed plans.

## Counter-Measures

Enemies can defeat basic radio intercept by:
- Maintaining radio silence
- Using encrypted communications
- Using signal lights instead of radio
- Speaking in code words
- Using short, burst transmissions
- Switching frequencies rapidly

## Upgrade Path

- [[Radio-Intercept-Standard]] - Intercept HF/VHF fleet radio
- [[SIGINT-Suite]] - Full spectrum intercept + direction finding
- [[Decryption-Module]] - Break enemy encryption
