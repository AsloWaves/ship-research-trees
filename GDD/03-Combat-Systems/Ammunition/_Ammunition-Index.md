# Ammunition Index

**Section**: 03-Combat-Systems
**Status**: IN DEVELOPMENT
**Last Updated**: 2025-12-08

---

## Overview

This section catalogs all naval ammunition types available in Fathoms Deep. Ammunition selection significantly affects combat effectiveness - choosing the right shell type for the situation can mean the difference between a devastating citadel hit and a harmless bounce.

> **Design Philosophy**: Ammunition is a tactical resource. Players must balance their loadouts between different shell types, manage supply, and make real-time decisions about what to fire and when.

---

## Ammunition Categories

### Naval Shells
High-velocity projectiles fired from main and secondary batteries.

| Category | Caliber Range | Purpose | Index |
|----------|---------------|---------|-------|
| Battleship Shells | 14"-18.1" | Anti-capital ship | [[Naval-Shells/_BB-Shells-Index]] |
| Cruiser Shells | 6"-8" | Anti-cruiser, versatile | [[Naval-Shells/_CA-Shells-Index]] |
| Destroyer Shells | 4"-5" | Anti-DD, utility | [[Naval-Shells/_DD-Shells-Index]] |
| Secondary Shells | 4"-6" | Close defense | [[Naval-Shells/_Secondary-Index]] |

### Torpedoes
Self-propelled underwater weapons for devastating attacks.

| Type | Launch Platform | Range Class | Index |
|------|-----------------|-------------|-------|
| Surface-Launched | Destroyers, Cruisers | Long-range | [[Torpedoes/_Surface-Torpedoes]] |
| Submarine Torpedoes | Submarines | Medium-range | [[Torpedoes/_Sub-Torpedoes]] |
| Aerial Torpedoes | Aircraft | Short-range | [[Torpedoes/_Aerial-Torpedoes]] |

### Aerial Ordnance
Bombs and rockets delivered by aircraft.

| Type | Delivery Method | Target Type | Index |
|------|-----------------|-------------|-------|
| Bombs | Level/Dive | Ships, Installations | [[Aerial-Ordnance/_Bombs-Index]] |
| Rockets | Attack Run | Soft targets | [[Aerial-Ordnance/_Rockets-Index]] |

### Depth Charges & Mines
Anti-submarine and area denial weapons.

| Type | Deployment | Purpose | Index |
|------|------------|---------|-------|
| Depth Charges | Dropped/Thrown | ASW | [[ASW/_Depth-Charges-Index]] |
| Mines | Laid | Area denial | [[Mines/_Mines-Index]] |

---

## Shell Types Quick Reference

### Armor-Piercing (AP)
| Shell | Caliber | Weight | Penetration | Best Use |
|-------|---------|--------|-------------|----------|
| [[16-inch-AP-Mark-8]] | 16" | 2,700 lb | 760mm @ 0m | Battleship citadels |
| [[8-inch-AP-Mark-21]] | 8" | 335 lb | 380mm @ 0m | Heavy cruisers |
| [[5-inch-AP-Common]] | 5" | 55 lb | 127mm @ 0m | Light armor |

### High-Explosive (HE)
| Shell | Caliber | Filler | Fire % | Best Use |
|-------|---------|--------|--------|----------|
| [[16-inch-HC-Mark-13]] | 16" | 153.6 lb | 36% | Soft targets, fires |
| [[8-inch-HE-Mark-25]] | 8" | 19.5 lb | 14% | Destroyers, superstructure |
| [[5-inch-HE-AAC]] | 5" | 7.5 lb | 5% | General purpose |

### Semi-Armor-Piercing (SAP)
| Shell | Caliber | Penetration | Damage | Best Use |
|-------|---------|-------------|--------|----------|
| [[6-inch-SAP-Mark-35]] | 6" | 45mm | 3,200 | Cruiser broadside |
| [[5-inch-SAP-Common]] | 5" | 32mm | 1,800 | Destroyer internals |

---

## Torpedo Quick Reference

### Surface-Launched
| Torpedo | Nation | Diameter | Range | Speed | Damage | Link |
|---------|--------|----------|-------|-------|--------|------|
| Type 93 "Long Lance" | Japan | 610mm | 40,000m | 36 kn | 21,600 | [[Type-93-Torpedo]] |
| Mark 15 | USA | 533mm | 13,700m | 26.5 kn | 16,633 | [[Mark-15-Torpedo]] |
| Mark 21" VII | UK | 533mm | 13,700m | 35 kn | 16,000 | [[Mark-VII-Torpedo]] |
| G7a T1 | Germany | 533mm | 12,500m | 30 kn | 14,500 | [[G7a-Torpedo]] |

### Submarine Torpedoes
| Torpedo | Nation | Range | Speed | Special | Link |
|---------|--------|-------|-------|---------|------|
| Mark 14 | USA | 9,150m | 31 kn | Magnetic fuze | [[Mark-14-Torpedo]] |
| Type 95 | Japan | 9,000m | 49 kn | Oxygen propulsion | [[Type-95-Torpedo]] |
| G7e T2 | Germany | 5,000m | 30 kn | Electric (wakeless) | [[G7e-Torpedo]] |

---

## Game Mechanics

### Shell Selection Strategy

| Target Type | Recommended Shell | Reason |
|-------------|-------------------|--------|
| Battleship broadside | AP | Citadel penetration |
| Angled battleship | HE | Damage without bouncing |
| Cruiser at range | AP | Clean penetrations |
| Destroyer | HE | Overpens with AP |
| Superstructure | HE | Module damage, fires |

### Ammunition Management

| Factor | Impact |
|--------|--------|
| **Loadout Planning** | Choose shell mix before battle |
| **Magazine Capacity** | Limited total ammunition |
| **Reload Time** | Switching shell types takes time |
| **Supply Ships** | Can resupply at sea (limited) |

### Torpedo Tactics

| Situation | Recommendation |
|-----------|----------------|
| Long-range ambush | Long Lance (Japan) |
| Close-range brawl | Fast, short-range torpedoes |
| Submarine attack | Electric for stealth |
| Mass assault | Spread patterns |

---

## Nation Characteristics

### United States
- Balanced shell performance
- Mark 14 torpedo issues (early war)
- Excellent HE for dual-purpose guns

### Japan
- Type 93 "Long Lance" - best surface torpedo
- Limited AA shell effectiveness
- Oxygen torpedoes leave no wake

### Great Britain
- Good all-around shells
- Reliable torpedoes
- SAP shells available

### Germany
- Effective armor-piercing shells
- G7e electric torpedoes (no wake)
- Magnetic mine detonators

---

## Related Documentation

- [[_Main-Guns-Index]] - Gun specifications
- [[Combat-System]] - How ammunition affects combat
- [[Damage-Model]] - Penetration and damage mechanics
- [[Resources]] - Ammunition as economic resource

---

## File Statistics

- **Total Ammunition Types**: 89
- **Shell Types**: 52
- **Torpedo Types**: 24
- **Other Ordnance**: 13
