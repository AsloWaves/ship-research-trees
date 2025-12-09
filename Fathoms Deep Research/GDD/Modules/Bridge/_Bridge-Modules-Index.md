---
title: Bridge Modules Index
category: modules
slot_type: bridge
description: Command and control facilities that determine UI features and ship capabilities
last_updated: 2025-12-09
tags: [modules, bridge, command, ui, progression]
---

# Bridge Modules

> The Bridge is the most important module choice for gameplay experience. It determines what UI features are available, how much information the player sees, and what command capabilities exist.

## Design Philosophy

Bridge modules represent the evolution of naval command from simple open platforms to sophisticated combat information centers. **The bridge you choose fundamentally changes how you play the game.**

| Era | Bridge Type | Player Experience |
|-----|-------------|-------------------|
| 1890-1920 | Open/Armored | Minimal UI, skill-based |
| 1920-1945 | Director | Fire control aids |
| 1940-1970 | CIC | Radar minimap, voice chat |
| 1970+ | Modern | Full automation, data links |

---

## Standard Bridge Progression

These are the core bridge types representing technology evolution:

| Module | ID | Era | Key Feature | Ship Types |
|--------|-----|-----|-------------|------------|
| [[Open-Bridge]] | BRG-001 | 1890-1920 | Visual only | All early ships |
| [[Enclosed-Bridge]] | BRG-002 | 1910-1940 | Weather protection | Interwar ships |
| [[Director-Bridge]] | BRG-003 | 1920-1945 | Fire control integration | Combat ships |
| [[Combat-Information-Center]] | BRG-004 | 1940-1970 | **Radar minimap** | WWII+ warships |
| [[Modern-Bridge]] | BRG-005 | 1970+ | Digital integration | Modern ships |

---

## Specialized Bridge Types

### Capital Ship Bridges

| Module | ID | Era | Key Feature | Best For |
|--------|-----|-----|-------------|----------|
| [[Armored-Conning-Tower]] | BRG-006 | 1890-1920 | 300mm armor, limited view | Pre-dreadnought battleships |
| [[Pagoda-Bridge]] | BRG-013 | 1920-1945 | Excellent optics, night fighting | Japanese battleships |
| [[Flagship-Bridge]] | BRG-015 | 1900+ | Admiral's facilities, fleet command | Any flagship |

### Carrier Bridges

| Module | ID | Era | Key Feature | Best For |
|--------|-----|-----|-------------|----------|
| [[Carrier-Island-WWII]] | BRG-010 | 1922-1960 | Flight control + radar | WWII carriers |
| [[Carrier-Island-Modern]] | BRG-011 | 1960+ | Full air ops integration | Supercarriers |

### Submarine Bridges

| Module | ID | Era | Key Feature | Best For |
|--------|-----|-----|-------------|----------|
| [[Submarine-Conning-Tower]] | BRG-008 | 1914-1945 | Periscope, TDC | WWII submarines |
| [[Submarine-Sail]] | BRG-009 | 1955+ | Multiple masts, deep ops | Nuclear submarines |

### Small Craft & Escorts

| Module | ID | Era | Key Feature | Best For |
|--------|-----|-----|-------------|----------|
| [[PT-Boat-Helm]] | BRG-012 | 1935-1970 | Speed, minimal profile | PT boats, MTBs |
| [[Destroyer-Bridge]] | BRG-014 | 1900-1970 | Compact, flexible | Destroyers, escorts |

### Specialized Operations

| Module | ID | Era | Key Feature | Best For |
|--------|-----|-----|-------------|----------|
| [[Amphibious-Command]] | BRG-017 | 1942+ | Shore coordination | Amphibious ships |
| [[Merchant-Bridge]] | BRG-016 | 1890+ | Navigation focus | Auxiliaries, transports |
| [[Flying-Bridge]] | BRG-007 | 1900-1960 | Maximum visibility | Any ship (auxiliary) |

---

## UI Features by Bridge Type

### Core Navigation

| Feature | Open | Enclosed | Director | CIC | Modern |
|---------|------|----------|----------|-----|--------|
| Compass | Basic | Accurate | Accurate | Accurate | Digital |
| Speed | Basic | Basic | Accurate | Accurate | Precise |
| Heading | Basic | Accurate | Accurate | Accurate | Precise |
| Depth (subs) | Basic | Basic | Basic | Accurate | Precise |

### Combat Features

| Feature | Open | Enclosed | Director | CIC | Modern |
|---------|------|----------|----------|-----|--------|
| Minimap | None | None | None | **RADAR** | Full 3D |
| Contacts | Visual | Visual | Visual | **All radar** | Data link |
| Range | Estimate | Rangefinder | Fire control | Radar | Precise |
| Lead Indicator | None | None | **YES** | Advanced | Automated |

### Communication

| Feature | Open | Enclosed | Director | CIC | Modern |
|---------|------|----------|----------|-----|--------|
| Team Chat | Flags | Flags | Flags/Voice | **Voice** | Encrypted |
| Vision Sharing | None | None | None | **Allied** | Automatic |
| Fleet Orders | Flags | Flags | Flags/Radio | Radio | Data link |

### Detection

| Feature | Open | Enclosed | Director | CIC | Modern |
|---------|------|----------|----------|-----|--------|
| RWR Warning | None | None | None | If installed | Integrated |
| IFF | None | None | None | If installed | Automatic |
| ESM | None | None | None | Basic | Full suite |

---

## Choosing Your Bridge

### For Historical Authenticity
Match bridge to ship era:
- Pre-WWI battleship → Armored Conning Tower
- WWII destroyer → Destroyer Bridge + radar
- WWII carrier → Carrier Island WWII
- Modern frigate → Modern Bridge

### For Maximum Information
Choose the most advanced bridge your ship can mount:
- CIC provides radar minimap
- Modern Bridge adds automation
- Flagship Bridge for fleet command

### For Immersive Challenge
Choose period-appropriate bridges:
- Open Bridge forces visual-only play
- Director Bridge gives fire control without radar
- Experience naval combat as it was fought

---

## Bridge + Module Compatibility

Some support modules require specific bridge levels:

| Module | Minimum Bridge |
|--------|---------------|
| Surface Radar | Director (display) / CIC (minimap) |
| Fire Control Radar | Director |
| Voice Radio | CIC |
| Data Links | Modern |
| IFF Display | CIC |
| ESM Suite | CIC |

---

## Special Considerations

### Submarines
Must use submarine-specific bridges:
- [[Submarine-Conning-Tower]] for WWII subs
- [[Submarine-Sail]] for modern subs
- Unique UI for periscope/sonar operations

### Carriers
Require carrier island bridges:
- [[Carrier-Island-WWII]] for conventional carriers
- [[Carrier-Island-Modern]] for supercarriers
- Adds flight operations UI

### Flagships
Can add [[Flagship-Bridge]] as enhancement:
- Requires base bridge (Director+ recommended)
- Adds fleet command capability
- Admiral's facilities

---

## Historical Context

### Why Bridges Matter

The bridge represents the captain's view of the world. In 1905, Admiral Togo fought Tsushima from Mikasa's open bridge, seeing only what his eyes and lookouts could report. By 1944, Admiral Spruance at Philippine Sea had radar plots showing aircraft hundreds of miles away.

This progression transforms gameplay:
- **1900**: You ARE the lookout - spot contacts yourself
- **1945**: Radar shows you the battlefield - tactical decisions
- **1970+**: Automation handles detection - strategic focus

---

## Module Count

**Total Bridge Modules: 17**

- Standard progression: 5
- Capital ship specialized: 3
- Carrier specialized: 2
- Submarine specialized: 2
- Small craft/escort: 2
- Operations specialized: 3

---

## Cross-References

- [[../Support/_Support-Modules-Index|Support Modules]] - Detection equipment
- [[../Engines/_Engine-Modules-Index|Engine Modules]] - Power for electronics
- [[../../INDEX|Module System Overview]]

---

*Updated: 2025-12-09 - Expanded from 5 to 17 bridge types*
