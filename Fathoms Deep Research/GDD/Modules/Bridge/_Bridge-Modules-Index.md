---
title: Bridge Modules Index
category: modules
slot_type: bridge
description: Command and control facilities that determine UI features and ship capabilities
last_updated: 2025-12-09
tags: [modules, bridge, command, ui, progression, national]
---

# Bridge Modules

> The Bridge is the most important module choice for gameplay experience. It determines what UI features are available, how much information the player sees, and what command capabilities exist.

## Design Philosophy

Bridge modules represent the evolution of naval command from simple open platforms to sophisticated combat information centers. **The bridge you choose fundamentally changes how you play the game.**

### Bridge Selection Factors

| Factor | Impact | Example |
|--------|--------|---------|
| **Era** | Technology available | CIC requires 1940+ |
| **Ship Type** | Specialized features | Carriers need islands |
| **Nation** | Unique bonuses | Japanese night fighting |
| **Famous** | Historical authenticity | Yamato's tower |

---

## Module Organization

Bridges are organized into four tiers:

```
Tier 1: Generic Era ──────── Technology baseline (what's possible)
    │
Tier 2: Ship-Type ────────── Specialization (optimized for role)
    │
Tier 3: National Variant ─── Flavor & bonuses (national character)
    │
Tier 4: Famous Specific ──── Premium/historical (unique ships)
```

**How to choose:**
1. Start with Generic Era for your time period
2. Apply Ship-Type if you have a specialized vessel
3. Consider National Variant for bonuses and authenticity
4. Use Famous Specific for historical ships

---

## Tier 1: Generic Era Bridges

These define the **technology baseline** - what UI features are possible regardless of ship type or nation.

| Module | ID | Era | Key Feature | UI Level |
|--------|-----|-----|-------------|----------|
| [[Open-Bridge]] | BRG-001 | 1890-1920 | Visual navigation | Basic |
| [[Enclosed-Bridge]] | BRG-002 | 1910-1940 | Weather protection | Basic+ |
| [[Interwar-Standard-Bridge]] | BRG-G04 | 1920-1940 | Gyrocompass, rangefinder | Standard |
| [[Director-Bridge]] | BRG-003 | 1920-1945 | Fire control integration | Enhanced |
| [[Combat-Information-Center]] | BRG-004 | 1940-1970 | **Radar minimap** | Full Radar |
| [[Modern-Bridge]] | BRG-005 | 1970-1990 | Computer integration | Advanced |

### Era Progression Chart

```
1890 ─── Open Bridge ─────────┐
                              │
1910 ─── Enclosed Bridge ─────┤
                              │
1920 ─── Interwar Standard ───┼─── Director Bridge
                              │
1940 ─── CIC ─────────────────┤
                              │
1970 ─── Modern Bridge ───────┘
```

---

## Tier 2: Ship-Type Bridges

Specialized bridges optimized for specific vessel categories.

### Capital Ships

| Module | ID | Era | Best For | Special Feature |
|--------|-----|-----|----------|-----------------|
| [[Battleship-Command-Bridge]] | BRG-T01 | 1900-1960 | BB, BC | Armored option, multi-level |
| [[Heavy-Cruiser-Bridge]] | BRG-T02 | 1920-1970 | CA, CB | Balanced protection |
| [[Light-Cruiser-Bridge]] | BRG-T03 | 1920-1970 | CL, CLAA | AA coordination |
| [[Armored-Conning-Tower]] | BRG-006 | 1890-1920 | Pre-dreadnoughts | 300mm armor |
| [[Flagship-Bridge]] | BRG-015 | 1900+ | Any flagship | Admiral facilities |

### Carriers

| Module | ID | Era | Best For | Special Feature |
|--------|-----|-----|----------|-----------------|
| [[Carrier-Island-WWII]] | BRG-010 | 1922-1960 | CV | Flight control + radar |
| [[Light-Carrier-Island]] | BRG-T09 | 1940-1970 | CVL, CVE | Compact Pri-Fly |
| [[Carrier-Island-Modern]] | BRG-011 | 1960+ | CVN | Full CATCC |

### Destroyers & Escorts

| Module | ID | Era | Best For | Special Feature |
|--------|-----|-----|----------|-----------------|
| [[Destroyer-Bridge]] | BRG-014 | 1900-1970 | DD | Compact, versatile |
| [[Escort-Destroyer-Bridge]] | BRG-T05 | 1940-1970 | DE, DDE, APD | ASW focus |
| [[Corvette-Frigate-Bridge]] | BRG-T07 | 1940-1990 | FF, K, PF | Economical escort |

### Submarines

| Module | ID | Era | Best For | Special Feature |
|--------|-----|-----|----------|-----------------|
| [[Submarine-Conning-Tower]] | BRG-008 | 1914-1945 | SS | Periscope, TDC |
| [[Submarine-Sail]] | BRG-009 | 1955+ | SSN, SSBN | Multiple masts |

### Small Craft

| Module | ID | Era | Best For | Special Feature |
|--------|-----|-----|----------|-----------------|
| [[PT-Boat-Helm]] | BRG-012 | 1935-1970 | PT, MTB, MGB | Minimal, fast |
| [[Monitor-Gunboat-Bridge]] | BRG-T14 | 1890-1970 | M, PG, PR | River/coastal |

### Auxiliary & Special

| Module | ID | Era | Best For | Special Feature |
|--------|-----|-----|----------|-----------------|
| [[Merchant-Bridge]] | BRG-016 | 1890+ | AO, AP, AK | Navigation focus |
| [[Amphibious-Command]] | BRG-017 | 1942+ | AGC, LCC | Joint ops |
| [[Flying-Bridge]] | BRG-007 | 1900-1960 | Any | Maximum visibility |

---

## Tier 3: National Variant Bridges

National variants provide **unique bonuses** reflecting each navy's doctrine and technology.

### Japanese Navy (Night Fighting Focus)

Japan's bridges emphasize superior optics and night combat capability.

| Module | ID | Era | Special Bonus |
|--------|-----|-----|---------------|
| [[Japanese-Pagoda-Early]] | BRG-JP01 | 1920-1935 | +10% visual range |
| [[Pagoda-Bridge]] | BRG-013 | 1920-1945 | +20% night detection |
| [[Japanese-Carrier-Island]] | BRG-JP03 | 1922-1945 | Compact, minimal |
| [[Japanese-Cruiser-Bridge]] | BRG-JP04 | 1925-1945 | Type 93 torpedo coord |
| [[Japanese-Destroyer-Bridge]] | BRG-JP05 | 1930-1945 | Night attack bonus |
| [[Japanese-Submarine-Tower]] | BRG-JP06 | 1930-1945 | Float plane capable |

### Royal Navy (Seamanship & Tradition)

British bridges emphasize professionalism and weather resilience.

| Module | ID | Era | Special Bonus |
|--------|-----|-----|---------------|
| [[British-Tripod-Bridge]] | BRG-UK01 | 1910-1940 | Traditional excellence |
| [[British-Enclosed-Bridge]] | BRG-UK02 | 1920-1945 | Weather resilience |
| [[British-Carrier-Island]] | BRG-UK03 | 1918-1960 | Armored deck option |
| [[British-Destroyer-Bridge]] | BRG-UK04 | 1930-1960 | ASW coordination |
| [[British-Cruiser-Bridge]] | BRG-UK05 | 1920-1960 | Long endurance |
| [[British-Submarine-Tower]] | BRG-UK06 | 1914-1960 | Patrol endurance |

### Kriegsmarine (Engineering & Protection)

German bridges emphasize armor and systematic engineering.

| Module | ID | Era | Special Bonus |
|--------|-----|-----|---------------|
| [[German-Armored-Tower]] | BRG-DE01 | 1935-1945 | Heavy protection |
| [[German-Atlantic-Bridge]] | BRG-DE02 | 1935-1945 | Weather hardened |
| [[German-Destroyer-Bridge]] | BRG-DE03 | 1935-1945 | Torpedo focus |
| [[German-UBoat-Tower-VII]] | BRG-DE04 | 1936-1945 | Classic Atlantic |
| [[German-UBoat-Tower-IX]] | BRG-DE05 | 1938-1945 | Long range |
| [[German-UBoat-Tower-XXI]] | BRG-DE06 | 1944-1945 | Snorkel equipped |

### US Navy (Practical & Radar-Centric)

American bridges emphasize practicality and radar integration.

| Module | ID | Era | Special Bonus |
|--------|-----|-----|---------------|
| [[American-Cage-Mast-Bridge]] | BRG-US01 | 1910-1935 | Pre-radar standard |
| [[American-Radar-Tower-Bridge]] | BRG-US02 | 1942-1960 | Radar optimized |
| [[American-Carrier-Island]] | BRG-US03 | 1927-1960 | Comprehensive |
| [[American-Fletcher-Bridge]] | BRG-US04 | 1942-1970 | DD standard |
| [[American-Cruiser-Bridge]] | BRG-US05 | 1930-1970 | AA excellence |
| [[American-Submarine-Bridge]] | BRG-US06 | 1940-1960 | Pacific patrol |

### Marine Nationale (Style & Innovation)

French bridges feature distinctive design and innovation.

| Module | ID | Era | Special Bonus |
|--------|-----|-----|---------------|
| [[French-Mack-Bridge]] | BRG-FR01 | 1930-1945 | Innovative design |
| [[French-Destroyer-Bridge]] | BRG-FR02 | 1925-1945 | High speed ops |
| [[French-Submarine-Tower]] | BRG-FR03 | 1920-1945 | Long range |

### Regia Marina (Aesthetic & Speed)

Italian bridges emphasize elegance and Mediterranean operations.

| Module | ID | Era | Special Bonus |
|--------|-----|-----|---------------|
| [[Italian-Streamlined-Bridge]] | BRG-IT01 | 1930-1945 | Aesthetic design |
| [[Italian-Destroyer-Bridge]] | BRG-IT02 | 1930-1945 | Speed emphasis |
| [[Italian-Submarine-Tower]] | BRG-IT03 | 1930-1945 | Mediterranean ops |

### Soviet Navy (Rugged & Cold Weather)

Soviet bridges emphasize Arctic operation capability.

| Module | ID | Era | Special Bonus |
|--------|-----|-----|---------------|
| [[Soviet-Enclosed-Bridge]] | BRG-SU01 | 1940-1990 | Arctic resilience |
| [[Soviet-Destroyer-Bridge]] | BRG-SU02 | 1940-1990 | Cold weather |
| [[Soviet-Submarine-Tower]] | BRG-SU03 | 1940-1990 | Under-ice capable |

---

## Tier 4: Famous Ship-Specific Bridges

Premium bridges for specific famous vessels. Maximum historical authenticity.

| Module | ID | Ship(s) | Era | Unique Feature |
|--------|-----|---------|-----|----------------|
| [[Yamato-Command-Tower]] | BRG-SP01 | Yamato, Musashi | 1941-1945 | Largest ever built |
| [[Iowa-Combat-Bridge]] | BRG-SP02 | Iowa-class | 1943-1992 | Radar perfected |
| [[Bismarck-Tower]] | BRG-SP03 | Bismarck, Tirpitz | 1940-1944 | 10.5m rangefinder |
| [[Hood-Compass-Platform]] | BRG-SP04 | HMS Hood | 1920-1941 | Pride of RN |
| [[Enterprise-Island-CV6]] | BRG-SP05 | USS Enterprise | 1938-1947 | Most decorated |
| [[U-96-Tower]] | BRG-SP06 | U-96 | 1940-1945 | Das Boot |
| [[Warspite-Bridge]] | BRG-SP07 | HMS Warspite | 1915-1945 | Grand Old Lady |
| [[Fletcher-DD-445-Bridge]] | BRG-SP08 | USS Fletcher | 1942-1969 | Name ship |
| [[Graf-Spee-Bridge]] | BRG-SP09 | Admiral Graf Spee | 1936-1939 | River Plate |
| [[Mikasa-Bridge]] | BRG-SP10 | Mikasa | 1902-1905 | Tsushima |

---

## UI Features Matrix

### By Generic Era

| Feature | Open | Enclosed | Interwar | Director | CIC | Modern |
|---------|------|----------|----------|----------|-----|--------|
| Compass | Basic | Accurate | Accurate | Accurate | Accurate | Digital |
| Speed | Basic | Basic | Accurate | Accurate | Accurate | Precise |
| Minimap | None | None | None | None | **RADAR** | Enhanced |
| Contacts | Visual | Visual | Visual | Visual | **All** | Auto |
| Lead Ind | None | None | Basic | **YES** | Advanced | Auto |
| Voice | Flags | Flags | Flags | Radio | **Voice** | Encrypt |

### National Bonuses Summary

| Nation | Primary Bonus | Secondary Bonus |
|--------|---------------|-----------------|
| Japan | +20% night detection | Superior optics |
| Britain | Weather resilience | ASW coordination |
| Germany | Armor protection | Engineering reliability |
| USA | Radar integration | Damage control |
| France | Innovation | High speed |
| Italy | Speed | Mediterranean ops |
| Soviet | Arctic operations | Rugged construction |

---

## Quick Reference: Bridge Selection Guide

### By Ship Type

| Building... | Recommended Bridge |
|-------------|-------------------|
| Pre-WWI Battleship | Armored Conning Tower |
| WWI Battleship | British Tripod or German Armored Tower |
| WWII Battleship | National variant (Pagoda/Radar Tower/etc.) |
| WWII Cruiser | National Cruiser Bridge + CIC |
| WWII Destroyer | National Destroyer Bridge + radar |
| WWII Carrier | National Carrier Island |
| WWII Submarine | National Submarine Tower |
| Cold War ship | Modern Bridge |
| Modern ship | Digital Combat Bridge |

### By Playstyle

| Want... | Choose... |
|---------|-----------|
| Maximum information | Modern Bridge + all sensors |
| Historical accuracy | Match era + national variant |
| Challenging gameplay | Open/Enclosed Bridge (no minimap) |
| Night fighting | Japanese Pagoda variants |
| Bad weather ops | British Enclosed or German Atlantic |
| Fleet command | Flagship Bridge |

---

## Module Count Summary

**Total Bridge Modules: 67**

| Category | Count |
|----------|-------|
| Generic Era | 6 |
| Ship-Type | 19 |
| Japanese National | 6 |
| British National | 6 |
| German National | 6 |
| American National | 6 |
| French National | 3 |
| Italian National | 3 |
| Soviet National | 3 |
| Famous Specific | 10 |

---

## Cross-References

- [[../Support/_Support-Modules-Index|Support Modules]] - Detection equipment
- [[../Engines/_Engine-Modules-Index|Engine Modules]] - Power for electronics
- [[../../INDEX|Module System Overview]]

---

*Updated: 2025-12-09 - Expanded from 17 to 67 bridge types with national variants and famous ships*
