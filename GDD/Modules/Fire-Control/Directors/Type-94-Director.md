---
module_id: FCS-DIR-002
name: Type 94 Director
category: fire-control
subcategory: director
type: main-battery
era: 1939
nation: Japan
manufacturer: Nippon Kogaku (Nikon)

# Physical
weight_kg: 15000
height_m: 3.2
crew: 10
armored: true
armor_mm: 50

# Optical
rangefinder_base_m: 15.0
rangefinder_type: coincidence
magnification: 25x
optical_range_km: 45

# Tracking
elevation_range: -5 to +45
train_rate_deg_s: 4
elevation_rate_deg_s: 3
stabilization: 2-axis

tags: [director, main-battery, japan, wwii, yamato, excellent-optics, optical-peak]
---

# Type 94 Director

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 94 Hoiban (Fire Director) |
| **Nation** | Imperial Japan |
| **Era** | 1939-1945 |
| **Type** | Main Battery (Surface Only) |
| **Manufacturer** | Nippon Kogaku (Nikon) |

## Description

The Type 94 Director was Japan's ultimate expression of optical fire control technology, featuring the largest optical rangefinder ever mounted on a warship. With a 15-meter base length, it could measure ranges to battleship-sized targets at distances exceeding 40km - farther than most radar systems of the era.

**Key Innovation**: 15-meter base rangefinder - the largest naval rangefinder ever built, giving Japan theoretical ranging superiority in daylight surface actions.

## Physical Specifications

| Specification | Value |
|--------------|-------|
| Weight | 15,000 kg (33,000 lbs) |
| Height | 3.2 m (10.5 ft) |
| Crew | 10 |
| Armor | 50mm hardened steel |
| Rangefinder | 15m coincidence type |
| Magnification | 25x (ranging), 12x (tracking) |

## Optical Performance

| Parameter | Value |
|-----------|-------|
| Rangefinder Base | 15m (49.2 ft) - LARGEST EVER |
| Optical Range (Battleship) | 45,000m (49,000 yards) |
| Optical Range (Cruiser) | 38,000m (41,500 yards) |
| Optical Range (Destroyer) | 32,000m (35,000 yards) |
| Bearing Accuracy | ±0.05° |
| Range Accuracy | ±30m at 30km |

## Why 15 Meters?

Rangefinder accuracy is proportional to base length. Japan, knowing they would face numerically superior US forces, sought quality advantages through optical superiority.

**Range Accuracy Formula**: Error ∝ (Range²) / (Base Length × Magnification)

A 15m rangefinder at 30km achieves accuracy that a 4.5m rangefinder would only achieve at 17km.

## Tracking Performance

| Parameter | Value |
|-----------|-------|
| Elevation Range | -5° to +45° |
| Train Rate | 4°/sec |
| Elevation Rate | 3°/sec |
| Stabilization | 2-axis (roll, pitch) |
| Tracking Type | Continuous optical |

## Integration

The Type 94 connected to:
- **Type 94 Shagekiban** (Fire Control Computer) - Mechanical ballistic calculator
- **Type 21 Radar** (late war) - Air search only, not integrated for fire control
- **460mm Main Battery** - Yamato's 18.1" guns
- **Stable Vertical** - Gyroscopic reference

**Data Transmission**: Mechanical shaft and electrical synchro system.

## Crew Stations

| Station | Role |
|---------|------|
| Director Officer | Command, mode selection |
| Chief Rangefinder | Range measurement supervision |
| Rangefinder Operators (2) | Coincidence ranging |
| Bearing Tracker | Horizontal tracking |
| Elevation Tracker | Vertical tracking |
| Spotters (2) | Fall of shot observation |
| Computers (2) | Manual calculations backup |

## Optical Superiority Doctrine

Japan's entire surface warfare doctrine centered on optical superiority:

1. **First Sight**: 15m rangefinders detect enemies first
2. **First Accurate Range**: Precise range at extreme distance
3. **First Effective Salvo**: Hit before enemy can range you
4. **Night Fighting**: Where Japan's optical training excelled

This doctrine worked brilliantly until radar matured.

## Combat Record

**Battle of Savo Island (August 1942)**
Japanese cruisers using Type 94 and Type 98 directors devastated Allied forces at night. Optical fire control achieved hits at 8,000+ meters in darkness while Allied radar-equipped ships failed to respond effectively.

**Battle of Guadalcanal (November 1942)**
Kirishima's Type 94 director achieved initial hits on USS South Dakota at night - before American radar fire control proved decisive as battle progressed.

**Battle of Leyte Gulf (October 1944)**
Yamato's Type 94 directors ranged targets at extreme distance, but smoke and air attacks prevented effective use of Japan's optical superiority.

## Limitations

### Night/Weather
Despite Japanese training excellence, the Type 94 was fundamentally limited:
- Rain degrades optics significantly
- Smoke renders rangefinders useless
- Night requires searchlights or star shells

### Radar Integration
Japan never successfully integrated radar with the Type 94:
- Type 21/22 radars were air search only
- Type 32 fire control radar came too late
- Operators trained for optical, resisted radar

### Tracking Speed
At 4°/sec, the Type 94 couldn't track aircraft:
- Fine for battleship engagements
- Useless against dive bombers
- Separate AA directors required

## Game Statistics

| Stat | Value | Notes |
|------|-------|-------|
| Accuracy Bonus | +45% | Daylight surface |
| Range Bonus | +20% | Optical ranging |
| Night Penalty | -40% | Without radar |
| Weather Penalty | -50% | Rain/smoke |
| Tracking Speed | Slow | 4°/sec train |
| AA Capability | None | Surface only |

## Advantages
- Longest-range optical fire control ever
- Exceptional daylight accuracy
- Superior bearing precision
- Heavy armor protection
- Proven Japanese optical quality

## Disadvantages
- Massive size and weight
- Slow tracking rates
- No radar integration
- Useless in poor visibility
- Surface targets only
- Complex, fragile optics

## Ships Equipped
- Yamato (2 main, 2 secondary)
- Musashi (2 main, 2 secondary)
- Shinano (planned, never installed)

## Paper Design: Type 94 Kai

A proposed upgrade with radar integration was designed but never implemented:
- Type 32 radar slaved to optical director
- Combined ranging (optical primary, radar backup)
- Estimated 1946 deployment
- Cancelled due to war's end

## Cross-References
- [[Computers/Type-94-Computer|Type 94 Shagekiban]]
- [[/GDD/Modules/Support/Detection-Radar/Radar-FC-Type94|Type 94 Radar (planned)]]
- [[/GDD/04-Ships/Japan/Battleships/Yamato-Class|Yamato-Class Battleships]]

---
*The Type 94 Director represents the absolute peak of naval optical fire control - a technology Japan perfected just as radar made it obsolete.*
