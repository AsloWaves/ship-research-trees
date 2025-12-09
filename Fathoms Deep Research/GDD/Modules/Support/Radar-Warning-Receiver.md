---
module_id: SUP-018
name: Radar Warning Receiver (RWR)
category: support
subcategory: electronic_warfare
era: 1942-present
slot_type: support
weight: 100
power_draw: 5
crew_required: 1
tags: [support, ew, detection, warning, countermeasure]
---

# Radar Warning Receiver (RWR)

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | SUP-018 |
| **Era** | 1942-Present |
| **Category** | Electronic Warfare |
| **Weight** | 100 kg |
| **Power Draw** | 5 kW |
| **Crew Required** | 1 |

## Description

Detects when enemy radar is scanning you. The RWR picks up radar transmissions and alerts the crew that they've been detected. Critical for knowing when you've lost the element of surprise.

## Effect on UI

When installed with CIC+:
- **"DETECTED" Warning**: Flashes when radar hits you
- **Bearing to Radar**: Direction of threat
- **Radar Type**: Classification (search, fire control)
- **Threat Priority**: Fire control = high priority

## Effect on Fog of War

**Know when you're visible!**

```
Detection:            Instant when radar hits you
Range:                2x enemy radar range
Information:          Bearing, type, threat level
Response Time:        <1 second warning
```

## Warning Types

| Alert | Meaning | Urgency |
|-------|---------|---------|
| SEARCH | Enemy search radar | Low - they're looking |
| TRACKING | Being tracked | Medium - they see you |
| LOCK | Fire control radar | HIGH - weapons incoming |

## Tactical Use

1. **Ambush Awareness**: Know if you're spotted
2. **Evasion**: Break contact before attack
3. **Jammer Timing**: Know when to activate ECM
4. **Threat Direction**: Bearing to threat

## Without RWR

Ships without this module:
- No warning of detection
- Cannot know if ambush is set
- Surprised by radar-guided attacks
- Vulnerable to beyond-visual-range attacks

## Limitations

- Only detects ACTIVE radar (not passive sensors)
- Cannot detect visual observation
- Does not provide range to threat
- May give false alerts (friendly radar)

## Historical Notes

RWR technology emerged when radar became a threat. German U-boats developed Metox receivers to detect Allied radar - critical for survival. Surface ships adopted similar systems. Modern RWRs can identify specific radar types and prioritize threats automatically.

## Countermeasure Chain

1. **RWR detects** enemy radar
2. **Jammer activated** to disrupt
3. **Chaff deployed** if needed
4. **Evasive maneuvers** initiated

## Compatible With

- CIC Bridge (full integration)
- Modern Bridge (threat display)
- Essential for WWII+ surface combat
