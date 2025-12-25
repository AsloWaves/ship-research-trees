# Ship Database Index

**Section**: 04-Ship-Customization
**Status**: IN DEVELOPMENT
**Last Updated**: 2025-12-08

---

## Overview

This database contains all historical ship classes that serve as the foundation for in-game vessels. Ships are organized by nation and type, with each entry containing historical specifications that inform game balance and capabilities.

> **Design Philosophy**: Ships in Fathoms Deep are designed to be as close as possible to their historical counterparts. These research files provide the authentic foundation for ship statistics, capabilities, and behaviors.

---

## Quick Navigation

### By Nation

| Nation | Battleships | Carriers | Cruisers | Destroyers | Submarines | Auxiliaries |
|--------|-------------|----------|----------|------------|------------|-------------|
| [[_USA-Ships\|United States]] | 12 | 24 | 47 | 119 | 73 | 45 |
| [[_UK-Ships\|Great Britain]] | 15 | 11 | 62 | 144 | 58 | 38 |
| [[_Japan-Ships\|Japan]] | 12 | 20 | 44 | 126 | 65 | 32 |
| [[_Germany-Ships\|Germany]] | 4 | 2 | 8 | 40 | 167 | 28 |

---

## Ships by Type

### Capital Ships

#### Battleships
| Class | Nation | Ships | Displacement | Main Armament | Speed | Link |
|-------|--------|-------|--------------|---------------|-------|------|
| Iowa | USA | 4 | 45,000t | 9× 16"/50 | 33 kn | [[Iowa-Class]] |
| Yamato | Japan | 3 | 65,000t | 9× 18.1"/45 | 27 kn | [[Yamato-Class]] |
| King George V | UK | 5 | 36,727t | 10× 14"/45 | 28 kn | [[King-George-V-Class]] |
| Bismarck | Germany | 2 | 41,700t | 8× 15"/52 | 30 kn | [[Bismarck-Class]] |

#### Aircraft Carriers
| Class | Nation | Ships | Displacement | Aircraft | Speed | Link |
|-------|--------|-------|--------------|----------|-------|------|
| Essex | USA | 24 | 27,100t | 90-100 | 33 kn | [[Essex-Class]] |
| Illustrious | UK | 4 | 23,000t | 36-57 | 30 kn | [[Illustrious-Class]] |
| Shokaku | Japan | 2 | 25,675t | 72-84 | 34 kn | [[Shokaku-Class]] |

---

### Escort Vessels

#### Destroyers
| Class | Nation | Ships | Displacement | Main Armament | Speed | Torpedoes | Link |
|-------|--------|-------|--------------|---------------|-------|-----------|------|
| Fletcher | USA | 175 | 2,050t | 5× 5"/38 | 36.5 kn | 10× 21" | [[Fletcher-Class]] |
| Kagero | Japan | 19 | 2,033t | 6× 127mm/50 | 35.5 kn | 8× 24" | [[Kagero-Class]] |
| Tribal | UK | 27 | 1,870t | 8× 4.7"/45 | 36 kn | 4× 21" | [[Tribal-Class]] |
| Z23 | Germany | 8 | 2,600t | 5× 15cm/48 | 36 kn | 8× 21" | [[Z23-Class]] |

#### Submarines
| Class | Nation | Boats | Displacement | Torpedo Tubes | Speed (S/D) | Range | Link |
|-------|--------|-------|--------------|---------------|-------------|-------|------|
| Gato | USA | 77 | 1,525t | 10× 21" | 20/9 kn | 11,000 nm | [[Gato-Class]] |
| Type VIIC | Germany | 593 | 769t | 5× 53.3cm | 17.7/7.6 kn | 8,500 nm | [[Type-VIIC-Submarine]] |
| I-400 | Japan | 3 | 5,223t | 8× 21" | 18.7/6.5 kn | 37,500 nm | [[I-400-Class]] |

---

## Game Integration Notes

### Tier Placement Guidelines

| Tier | Era | Example Classes |
|------|-----|-----------------|
| 1-2 | Pre-WWI / Early WWI | Pre-dreadnoughts, early destroyers |
| 3-4 | WWI | Dreadnoughts, early submarines |
| 5-6 | Interwar | Treaty cruisers, fleet carriers |
| 7-8 | Early WWII | Fast battleships, fleet destroyers |
| 9-10 | Late WWII | Iowa, Yamato, advanced submarines |

### Balance Considerations

- Historical specifications provide baseline stats
- Game balance may require adjustments (documented in each ship file)
- Module slots determined by historical refit potential
- Crew requirements scaled for gameplay

---

## Related Documentation

- [[Ship-Customization-Overview]] - Module system and upgrades
- [[Combat-System]] - How ship stats affect combat
- [[Economy-Overview]] - Ship acquisition and maintenance costs
- [[_Weapons-Overview]] - Available armament options

---

## File Statistics

- **Total Ship Classes**: 818
- **Nations Covered**: 4 major + auxiliaries
- **Documentation Status**: Research phase complete, game integration ongoing
