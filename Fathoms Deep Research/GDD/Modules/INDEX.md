---
title: Module System Index
category: modules
description: Ship equipment organized by slot type
last_updated: 2025-12-09
tags: [modules, index, slots, progression]
---

# Module System

> Modules are equipment that can be installed in ship slots to provide capabilities, improve performance, and unlock UI features. This is a comprehensive system covering 1890-present naval technology.

## Slot Types

Ships have different slot types that accept specific module categories:

| Slot Type | Purpose | Quantity | Key Impact |
|-----------|---------|----------|------------|
| **Bridge** | Command & Control | 1 per ship | Determines UI features available |
| **Engine** | Propulsion | Ship-specific | Speed, range, acceleration |
| **Support** | Detection, Comms, DC | Ship-specific | Fog of War, team coordination |
| **Turret** | Weapons | Ship-specific | Combat capability |
| **Aircraft** | Aviation | Carriers only | Air operations |

---

## Module Summary

| Category | Modules | Key Feature |
|----------|---------|-------------|
| Bridge | 5 types | UI feature unlocks by era |
| Engine | 17 variants | Speed + efficiency trade-offs |
| Support - Visual | 10 variants | Base detection, rangefinding |
| Support - Radar | 12 variants | Electronic detection with cone/sweep |
| Support - Sonar | 14 variants | Underwater detection patterns |
| Support - Comms | 12 variants | Team coordination, vision sharing |
| Support - EW | 6 variants | Countermeasures, threat warning |
| Support - DC | 6 variants | Damage repair, survivability |
| Support - Special | 8 variants | Aviation, ASW, utility |
| **Total** | **~90 modules** | |

---

## Bridge Modules (5)

The Bridge determines what UI features are available. **This is the most impactful module choice.**

| Module | Era | UI Features Unlocked |
|--------|-----|---------------------|
| [[Bridge/Open-Bridge\|Open Bridge]] | 1890-1920 | Visual only, no minimap, no targeting aids |
| [[Bridge/Enclosed-Bridge\|Enclosed Bridge]] | 1910-1940 | +Gyrocompass, +rangefinder display |
| [[Bridge/Director-Bridge\|Director Bridge]] | 1920-1945 | +Fire control, +lead indicator, +range display |
| [[Bridge/Combat-Information-Center\|CIC]] | 1940-1970 | **+Radar minimap, +voice comms, +vision sharing** |
| [[Bridge/Modern-Bridge\|Modern Bridge]] | 1970+ | +GPS, +automation, +data links, +full HUD |

→ [[Bridge/_Bridge-Modules-Index|Full Bridge Documentation]]

---

## Engine Modules (17)

Propulsion systems determining speed, acceleration, range, and fuel efficiency.

### By Technology
| Category | Modules | Era | Character |
|----------|---------|-----|-----------|
| **Reciprocating** | 4 variants | 1880-1920 | Slow, reliable, coal-fired |
| **Steam Turbine** | 5 variants | 1906-1960 | High power, oil-fired, WWII standard |
| **Diesel** | 3 variants | 1910+ | Efficient, excellent range, submarine standard |
| **Modern** | 5 variants | 1950+ | Gas turbine, combined, nuclear |

### Highlights
| Module | Power | Key Feature |
|--------|-------|-------------|
| Triple-Expansion | 5-25k SHP | Pre-dreadnought workhorse |
| Geared-Turbine-Heavy | 150k SHP | WWII battleship standard |
| Turbo-Electric | 60k SHP | USA specialty, instant reverse |
| MAN-Diesel | 6k SHP | German U-boat excellence |
| CODAG | Variable | Diesel cruise + gas sprint |
| Nuclear-Carrier | 280k SHP | Unlimited range |

→ [[Engines/_Engine-Modules-Index|Full Engine Documentation]]

---

## Support Modules (~56)

Flexible equipment filling generic "Support Slots" - mix and match based on role.

### Detection - Visual (10)
*Baseline detection using human observation and optics*

| Module | Era | Range | Notes |
|--------|-----|-------|-------|
| Lookout-Basic | 1890+ | 8km | Naked eye, 360° |
| Lookout-Binocular | 1900+ | 15km | 7x50 magnification |
| Lookout-Crow-Nest | 1890+ | +20% | Elevated position |
| Rangefinder-9m | 1920+ | 25km | Battleship standard |
| Searchlight-60inch | 1920+ | 8km beam | Night illumination |

### Detection - Radar (12)
*Electronic detection with cone/sweep mechanics*

| Type | Nations | Variants | Key Stats |
|------|---------|----------|-----------|
| Surface Search | USA/UK/Japan/Germany | 4 | 20-35km, rotating/sector |
| Air Search | USA/UK/Japan/Germany | 4 | 60-120km, rotating |
| Fire Control | USA/UK/Japan/Germany | 4 | 12-18km, directional |

**Cone/Sweep Mechanics:**
- **Rotating 360°**: Full coverage, 4-15 second updates
- **Sector Scan**: Focused arc, faster updates, blind spots
- **Directional**: Manual aim, continuous tracking, single target

→ [[Support/Detection-Radar/README|Radar Systems Documentation]]

### Detection - Sonar (14)
*Underwater detection for ASW operations*

| Type | Pattern | Variants | Key Stats |
|------|---------|----------|-----------|
| Passive (Hydrophones) | Omnidirectional | 4 | 3-5km, bearing only |
| Active (Searchlight) | Manual aim | 3 | 1.5-2.5km, 15-25° cone |
| Active (Scanning) | Auto sweep | 4 | 2.5-4km, 120-180° arc |
| Modern | Omni/Towed | 3 | 8-30km, advanced |

**Passive vs Active**: Passive = stealthy (bearing only), Active = reveals position (range + bearing)

→ [[Support/Detection-Sonar/README|Sonar Systems Documentation]]

### Communications (12)
*Team coordination and vision sharing*

| Type | Era | Effect |
|------|-----|--------|
| Signal Flags | 1890+ | Visual messages, 5km |
| Signal Lamp | 1890+ | Night capable, 15km |
| Wireless Telegraph | 1910+ | Text chat (delayed) |
| Voice Radio (TBS) | 1942+ | **Voice chat enabled** |
| Data Links | 1960+ | **Automatic vision sharing** |

→ [[Support/Communications/README|Communications Documentation]]

### Electronic Warfare (6)
*Detect threats, disrupt enemies*

| Module | Era | Effect |
|--------|-----|--------|
| RWR Basic | 1942+ | Know when radar detects you |
| RWR Advanced | 1960+ | Identify radar type |
| Noise Jammer | 1943+ | Degrades enemy radar |
| Chaff Launcher | 1943+ | Creates false contacts |

→ [[Support/Electronic-Warfare/README|EW Documentation]]

### Damage Control (6)
*Survivability and repair*

| Module | Era | Effect |
|--------|-----|--------|
| DC Basic | 1900+ | +10% repair speed |
| DC Center | 1940+ | +25% repair, damage UI |
| DC Advanced | 1960+ | +40% repair, automation |

→ [[Support/Damage-Control/README|Damage Control Documentation]]

### Special Systems (8)
*Unique capabilities*

| Module | Era | Capability |
|--------|-----|------------|
| Floatplane Catapult | 1920-1950 | Scout aircraft |
| Helicopter Hangar | 1960+ | ASW helicopter |
| Depth Charge Rack | 1915+ | ASW weapons |
| Hedgehog Launcher | 1942+ | Ahead-throwing ASW |

→ [[Support/Special/README|Special Systems Documentation]]

→ [[Support/_Support-Modules-Index|Complete Support Module Index]]

---

## Weapons Modules

Turret slot equipment - covered in separate documentation.

| Category | Description |
|----------|-------------|
| Main Guns | Primary armament (5" to 18") |
| Secondary Guns | Anti-surface secondaries |
| Anti-Aircraft | AA guns and mounts |
| Torpedoes | Surface and submarine tubes |
| Missiles | Guided missiles (modern) |

→ [[Weapons/Main-Guns/_Complete-Guns-Index|Complete Guns Index]]

---

## Aircraft Modules

Carrier and aviation ship equipment.

| Category | Description |
|----------|-------------|
| Hangars | Aircraft storage capacity |
| Flight Deck | Launch/recovery operations |
| Squadrons | Aircraft type assignments |

→ [[Aircraft/_Complete-Aircraft-Index|Complete Aircraft Index]]

---

## Era Progression

Technology eras gate what modules are available:

| Era | Years | Key Unlocks | UI Experience |
|-----|-------|-------------|---------------|
| **Pre-Radio** | 1890-1905 | Open Bridge, Triple Expansion, Lookouts, Flags | Minimal - visual only |
| **Dreadnought** | 1906-1918 | Enclosed Bridge, Turbines, Wireless, Hydrophone | +Compass, +range display |
| **Interwar** | 1919-1935 | Director Bridge, Fire Control, Floatplanes | +Lead indicator, +spotting |
| **WWII** | 1936-1945 | **CIC, Radar, Sonar, Voice Radio** | **+Minimap, +voice chat** |
| **Cold War** | 1946-1970 | Gas Turbines, Nuclear, Missiles, ECM | +EW displays |
| **Modern** | 1970+ | Digital systems, GPS, Automation, Data Links | Full modern HUD |

---

## Fog of War Integration

Modules directly affect what each player can see:

| Module Type | Effect on Fog of War |
|-------------|---------------------|
| **Detection** | Expands YOUR visibility circle |
| **Communications** | SHARES visibility with allies |
| **Electronic Warfare** | DISRUPTS enemy visibility |
| **Bridge Tier** | Determines what info is DISPLAYED |

**Key Insight**: Two players with identical detection but different bridges will see the SAME contacts but have DIFFERENT information about them.

---

## National Characteristics

| Nation | Strengths | Notable Modules |
|--------|-----------|-----------------|
| **USA** | Radar, fire control | SG Radar, Mk 37 FC, Turbo-Electric |
| **UK** | Early radar, ASDIC | Type 271, ASDIC Type 144, Geared Turbine |
| **Germany** | Submarines, diesels | GHG Hydrophone, MAN Diesel, FuMO radars |
| **Japan** | Optics, torpedoes | Type 93 Hydrophone, 15m Rangefinder |

---

## Cross-References

- [[/GDD/04-Ship-Customization/Module-System|Module System Mechanics]]
- [[/GDD/05-UI-Systems/HUD-Elements|HUD Elements by Era]]
- [[/GDD/04-Ship-Customization/Ship-Database/_Complete-Ships-Index|Ships Index]]

---

*Updated: 2025-12-09 - Expanded to ~90 modules with national variants and cone/sweep mechanics*
