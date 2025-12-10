---
module_id: EW-003
name: Noise Jammer
category: support
subcategory: electronic_warfare
era: 1943-present
slot_type: support
jamming_type: noise
effectiveness: moderate
frequency_coverage: 1-10_GHz
jamming_range: 40_km
weight: 500
crew_required: 2
tags: [support, electronic_warfare, jammer, ecm, countermeasure]
---

# Noise Jammer

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | EW-003 |
| **Era** | 1943-Present |
| **Category** | Electronic Warfare |
| **Weight** | 500 kg |
| **Crew Required** | 2 |

## Description

Electronic countermeasure system that broadcasts high-power noise across radar frequencies to degrade enemy radar effectiveness. Creates a "wall of noise" that reduces detection range and prevents accurate tracking. The workhorse of naval electronic warfare since WWII.

## Effect on Gameplay

When activated, noise jamming significantly reduces the effectiveness of enemy radar systems. Enemies using jammed radar experience reduced detection range, poor tracking accuracy, and difficulty maintaining fire control solutions. However, jamming also reveals your position and direction to anyone with ESM equipment.

## Specifications

| Capability | Performance |
|------------|-------------|
| **Jamming Power** | 1-5 kW ERP |
| **Frequency Coverage** | 1-10 GHz (X-band priority) |
| **Effective Range** | 40 km |
| **Jamming Types** | Spot, Barrage, Swept |
| **Activation Time** | 5 seconds |
| **Burn-through Range** | 8-12 km (enemy still detects) |
| **Power Modes** | Low, Medium, High |

## Jamming Effects on Enemy

### Detection Range
- **-50% to -70%** enemy radar range when jammed
- **Burn-through**: Close targets still visible
- **Sidelobes**: Some angles less effective

### Tracking Accuracy
- **±500m** position error at long range
- **Difficult lock**: Fire control struggles
- **Break-lock**: Easier to escape tracking
- **Missile guidance**: Degraded terminal homing

### Fire Control
- **Reduced hit probability**: Shells scatter more
- **Firing solutions**: Take longer to compute
- **Range finding**: Less accurate
- **Tracking rate**: Slower updates

## Jamming Modes

### Spot Jamming
- Maximum power on single frequency
- Most effective against one radar
- Vulnerable to frequency changes

### Barrage Jamming
- Power spread across frequency range
- Affects multiple radars
- Less effective per radar

### Swept Jamming
- Rapidly sweeps through frequencies
- Good against frequency-agile radars
- Moderate effectiveness

## Tactical Considerations

### When to Jam
- When detected and under fire control radar
- During evasive maneuvers
- To cover withdrawal
- To degrade enemy missile guidance

### When NOT to Jam
- During covert approach (jamming reveals position)
- Against visual-range threats
- When trying to remain undetected
- Against modern ECCM-equipped radars (less effective)

### Costs of Jamming
- **Reveals bearing**: Enemy knows your direction
- **High power draw**: Strains electrical systems
- **Heat signature**: Infrared detection risk
- **Limited duration**: Cannot jam indefinitely

## Limitations

- Does not work against visual, infrared, or passive detection
- Enemy can burn through at close range (8-12 km)
- Reveals your bearing to enemy ESM
- Ineffective against modern ECCM radars (1980s+)
- Frequency-agile radars can avoid jamming
- Home-on-jam missiles can use it for guidance
- High power consumption limits continuous use

## Historical Notes

Radar jamming began in WWII when the British and Germans raced to jam each other's radars. "Window" (chaff) was the first countermeasure, but active noise jamming soon followed. German destroyers used "Aphrodite" jammers against Allied radar, while Allied bombers employed "Carpet" jammers over Europe.

The technology matured in the Cold War as Soviet and NATO forces developed increasingly sophisticated jammers. The AN/SLQ-17 jammer equipped US destroyers in Vietnam, degradating North Vietnamese fire control radars. During the Falklands, British ships used noise jammers against Argentine radars, with mixed results - the close-range engagements often fell within burn-through range.

Modern noise jammers face an uphill battle against ECCM techniques like frequency agility, sidelobe blanking, and high power. The arms race continues as jammers become more sophisticated and radars develop countermeasures to the countermeasures.

## Compatible Systems

- Works best with RWR for threat detection
- Coordinates with chaff launchers
- Integrates with CIC for automated response
- Part of comprehensive EW suite
