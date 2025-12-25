---
module_id: EW-004
name: Deceptive Jammer
category: support
subcategory: electronic_warfare
era: 1960-present
slot_type: support
jamming_type: deceptive
effectiveness: high
techniques: range_gate_pull-off_velocity_gate_pull-off_false_targets
frequency_coverage: 2-18_GHz
weight: 650
crew_required: 2
tags: [support, electronic_warfare, jammer, ecm, deception, modern]
---

# Deceptive Jammer

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | EW-004 |
| **Era** | 1960-Present |
| **Category** | Electronic Warfare |
| **Weight** | 650 kg |
| **Crew Required** | 2 |

## Description

Advanced electronic countermeasure system that deceives enemy radar rather than simply masking it. Creates false targets, distorts range and velocity data, and manipulates tracking systems. Far more sophisticated and effective than noise jamming against modern threats.

## Effect on Gameplay

Deceptive jamming actively misleads enemy systems rather than just degrading them. Enemy radars see false targets, incorrect range data, or impossible velocities. Missiles lose lock or guide to false positions. Fire control solutions become worthless. Unlike noise jamming, deceptive techniques work even at close range and against ECCM-equipped systems.

## Specifications

| Capability | Performance |
|------------|-------------|
| **Jamming Power** | 2-10 kW ERP |
| **Frequency Coverage** | 2-18 GHz (full threat spectrum) |
| **Effective Range** | Line-of-sight |
| **Response Time** | 0.5 seconds |
| **False Targets** | Up to 10 simultaneous |
| **Processing Power** | Digital RF memory (DRFM) |
| **Techniques** | 8+ deception modes |

## Deception Techniques

### Range Gate Pull-Off (RGPO)
- Gradually shifts apparent range
- Missile tracks false range
- Ship disappears from tracking gate
- **Effect**: Missile misses by 500-2000m

### Velocity Gate Pull-Off (VGPO)
- Manipulates Doppler shift
- False velocity reading
- Tracking filter loses lock
- **Effect**: Enemy fire control breaks lock

### False Target Generation
- Creates phantom ships
- Multiple false returns
- Confuses targeting priority
- **Effect**: Enemy wastes weapons on ghosts

### Inverse Gain Jamming
- Exploits radar AGC (automatic gain control)
- Appears stronger, then weaker
- Causes tracking instability
- **Effect**: Radar cannot maintain stable track

### Cross-Eye Jamming
- Two antennas create phase difference
- Angular deception
- Appears to be at different bearing
- **Effect**: Fire control aims at wrong angle

### Cover Pulse Jamming
- Hides ship's return with false pulses
- Enemy cannot distinguish real echo
- Works against pulse-Doppler radars
- **Effect**: Lost in clutter of false returns

## Tactical Applications

### Missile Defense
Most effective against radar-guided missiles:
- **Semi-Active Missiles**: Break radar illumination lock
- **Active Radar Missiles**: Seduce terminal seeker
- **Command Guided**: Corrupt tracking data
- **Success Rate**: 60-80% break-lock vs. non-ECCM missiles

### Fire Control Disruption
- Prevents accurate ranging
- Breaks tracking loops
- Forces manual tracking (less accurate)
- Degrades hit probability by 70-90%

### Multi-Ship Coordination
- Coordinate deception across task force
- One ship creates false targets, others jam tracking
- Overwhelming enemy processing capacity
- Layered defense

## Advantages Over Noise Jamming

1. **Works at close range**: No burn-through problem
2. **Lower power**: More efficient
3. **ECCM resistant**: Harder to counter
4. **Precise effects**: Controlled deception vs. brute force
5. **Multi-threat**: Engages multiple radars simultaneously
6. **Less detectable**: Looks more like clutter than jamming

## Limitations

- Requires sophisticated threat analysis
- DRFM systems are complex and expensive
- Some radars have anti-deception features
- Must "learn" enemy radar before effective jamming
- Limited effectiveness against imaging radars
- Newest radars (2000s+) have advanced ECCM
- Requires frequent software updates for new threats
- Does not work against IR, visual, or passive sensors

## Historical Notes

Deceptive jamming emerged in the 1960s as radar technology became sophisticated enough to be fooled rather than simply overpowered. The Vietnam War saw early applications, with US aircraft using RGPO techniques against SAM radars. The technology proved far more effective than noise jamming against modern pulse-Doppler radars.

The development of Digital RF Memory (DRFM) in the 1980s revolutionized deceptive jamming. DRFM systems could capture radar pulses, modify them, and retransmit convincing false returns. The AN/SLQ-32(V)3 incorporating DRFM became standard on US Navy carriers and high-value ships, providing protection against anti-ship missiles.

During Operation Desert Storm, deceptive jamming proved highly effective against Iraqi radars. False targets created by DRFM systems confused air defense networks and protected ships from Silkworm missile attacks. Modern systems like the AN/SLQ-32(V)6 represent the state of the art, with sophisticated AI-driven deception algorithms that adapt in real-time to enemy radar characteristics.

The arms race continues as radar designers implement counter-deception features and jammer designers develop more sophisticated techniques. The latest DRFM systems can simultaneously jam multiple threats with different techniques while maintaining a database of radar characteristics for rapid response.
