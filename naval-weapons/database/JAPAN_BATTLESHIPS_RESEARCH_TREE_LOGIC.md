# Japanese Battleships Research Tree Logic

## Overview

This document defines the research tree structure for Japanese Battleships (BB) in the naval warfare system. Japan developed one of the world's most formidable battleship fleets, culminating in the legendary **Yamato class**—the largest and most powerful battleships ever built, armed with 18.1" guns. The IJN's "Eight-Eight Fleet" program aimed for dominance in the Pacific, featuring innovative fast battleships (Kongō class) and the revolutionary 16.1" gun Nagato class.

**Node ID Range**: 4000-4042 (43 nodes)
**Nation**: Japan
**Ship Type**: BB (Battleship)
**Time Period**: 1900-1960
**Tech Tiers**: 1-10

## Historical Context

### Pre-Dreadnought Era (1900-1910)

After victory in the Sino-Japanese War (1894-1895), Japan embarked on major naval expansion. **Mikasa** (1900), built in Britain, became Admiral Tōgō's flagship at the **Battle of Tsushima** (1905)—the decisive victory that destroyed the Russian Baltic Fleet and established Japan as a world naval power. This preserved battleship at Yokosuka symbolizes Japan's rise to naval prominence.

### Dreadnought Revolution (1910-1922)

Japan embraced the dreadnought revolution with **Kawachi class** (1912)—Japan's first all-big-gun battleships. The **Kongō class** (1913-1915), built as fast battlecruisers with British assistance (Kongō built at Vickers), featured 14" guns and 27.5 knots. The **Fusō** and **Ise classes** experimented with unique layouts—Fusō's 6 twin turrets creating distinctive "pagoda mast" silhouettes. The **Nagato class** (1920-1921) made history as the **world's first battleships with 16" guns** (16.1"/41 cm), achieving 26.7 knots and 40,000 tons—establishing Japan's qualitative edge.

### Washington Treaty Era (1922-1936)

The Washington Naval Treaty (1922) cancelled Japan's ambitious "Eight-Eight Fleet" program:
- **Tosa class**: Cancelled (Tosa sunk as target, Kaga converted to carrier)
- **Kii class**: Never started
- **Number 13 class**: Cancelled (would have been 47,500 tons, eight 18.1" guns, 30 knots)—"ten years ahead of their time"

Japan circumvented treaty limitations through extensive modernizations. The **Kongō class** underwent revolutionary reconstruction (1930s), transforming from 27.5-knot battlecruisers to **30+ knot fast battleships**—the fastest battleships in the world. These ships became the backbone of IJN carrier task forces, participating in every major engagement from Pearl Harbor to Leyte Gulf.

### WWII Super-Battleship Era (1937-1945)

Japan's withdrawal from naval treaties (1936) enabled the ultimate battleship project—**Yamato class**:

**Yamato Class Specifications** (Largest Battleships Ever Built):
- **Displacement**: 72,000 tons full load (heaviest battleships ever)
- **Main Armament**: Nine 46cm (18.1") Type 94 guns (largest naval guns ever)
  - Shell weight: 1,460 kg (3,220 lb)
  - Muzzle velocity: 780 m/s
  - Range: 42 km (26 miles)
- **Armor**: 410mm belt, 650mm turret face (thickest ever)
- **Speed**: 27 knots (150,000 shp)
- **Construction**: 3 completed (Yamato, Musashi, Shinano as carrier)

**Design A-150 "Super Yamato"**: Planned successor with **20.1" (51cm) guns**—the largest battleship guns ever designed. Two guns were ordered for testing at Kure Naval Arsenal. Design was nearly complete by 1941 but cancelled when war with the US became imminent and Japan prioritized carriers. These would have been the most powerful battleships ever conceived.

**Ise/Hyūga Conversions** (1943): Desperate carrier shortage after Midway led to hybrid conversions—aft turrets removed for 22-aircraft flight deck. Unique concept combining battleship firepower with carrier capability, though operational challenges limited effectiveness.

### Ultimate Fate

**Battle of Leyte Gulf** (October 1944): Japan's battleship force made its final stand. Musashi sunk by massive air attack (17 bombs, 19 torpedoes). Yamato survived but retreated.

**Operation Ten-Go** (April 7, 1945): Yamato's suicide mission to Okinawa. Sunk by US carrier aircraft (12+ torpedoes, 7+ bombs) with loss of 2,498 crew. The end of the battleship era.

## Key Innovations

1. **World's First 16" Guns** (Nagato, 1920): 16.1"/41cm guns, largest afloat until 1930s
2. **Fast Battleship Revolution** (Kongō Reconstruction, 1935-1940): 30+ knots, enabling carrier escort
3. **Largest Battleships Ever** (Yamato, 1941): 72,000 tons, 18.1" guns, 410mm armor
4. **Largest Naval Guns Designed** (A-150, 1941): 20.1" guns, 1,950 kg shells
5. **Hybrid Battleship-Carriers** (Ise/Hyūga, 1943): Unique carrier conversion concept
6. **Pagoda Masts** (Fusō/Ise/Nagato): Distinctive multi-story fire control towers

## Research Tree Structure

### Research Nodes Table

| Node_ID | Ship_Class | Tech_Tier | Year | Research_Cost_RP | Build_Cost | Build_Time_Days | Description | Special_Notes |
|---------|------------|-----------|------|------------------|------------|-----------------|-------------|---------------|
| 4000 | Mikasa | 1 | 1900 | 0 | $600,000 | 36 | Tsushima flagship | FREE, preserved ship, Tōgō's flagship |
| 4001 | Fuji | 1 | 1896 | 0 | $500,000 | 30 | First modern battleship | FREE, British-built, 2 ships |
| 4002 | Shikishima | 2 | 1898 | 3,000 | $650,000 | 36 | Improved pre-dreadnought | British-built, 2 ships |
| 4003 | Asahi | 2 | 1899 | 3,500 | $700,000 | 36 | Enhanced design | British-built, 1 ship |
| 4004 | Katori | 3 | 1905 | 5,000 | $800,000 | 42 | Post-Tsushima | 2 ships, British designs |
| 4005 | Satsuma | 4 | 1906 | 8,000 | $1,200,000 | 48 | Semi-dreadnought | First Japanese-built, 2 ships |
| 4006 | Aki | 4 | 1907 | 9,000 | $1,300,000 | 48 | Improved semi-dreadnought | 2nd Satsuma, refined design |
| 4007 | Kawachi | 5 | 1910 | 12,000 | $2,000,000 | 54 | First dreadnought | First all-big-gun, 2 ships |
| 4008 | Settsu | 5 | 1911 | 13,000 | $2,200,000 | 54 | Improved dreadnought | 2nd Kawachi, refined |
| 4009 | Kongō | 6 | 1912 | 16,000 | $3,500,000 | 60 | Battlecruiser | British-built Vickers, 27.5 kts |
| 4010 | Hiei | 6 | 1912 | 17,000 | $3,600,000 | 60 | 2nd Kongō | Japanese-built, 4 total |
| 4011 | Haruna | 6 | 1913 | 17,500 | $3,700,000 | 60 | 3rd Kongō | Japanese-built |
| 4012 | Kirishima | 6 | 1913 | 18,000 | $3,800,000 | 60 | 4th Kongō | Japanese-built |
| 4013 | Fusō | 7 | 1914 | 22,000 | $5,000,000 | 66 | Super-dreadnought | 6 twin turrets, pagoda mast |
| 4014 | Yamashiro | 7 | 1915 | 23,000 | $5,200,000 | 66 | 2nd Fusō | Distinctive silhouette |
| 4015 | Ise | 7 | 1916 | 24,000 | $5,500,000 | 66 | Improved Fusō | Better layout, 2 ships |
| 4016 | Hyūga | 7 | 1917 | 25,000 | $5,700,000 | 66 | 2nd Ise | Refined design |
| 4017 | Nagato | 8 | 1919 | 35,000 | $10,000,000 | 72 | First 16" guns | World's first 16.1" BB! |
| 4018 | Mutsu | 8 | 1920 | 36,000 | $10,500,000 | 72 | 2nd Nagato | Magazine explosion 1943 |
| 4019 | Tosa | 8 | 1921 | 38,000 | $12,000,000 | 78 | Improved Nagato | Cancelled, Washington Treaty |
| 4020 | Kaga | 8 | 1921 | 39,000 | $12,500,000 | 78 | 2nd Tosa | Converted to carrier |
| 4021 | Kii | 8 | 1922 | 40,000 | $13,000,000 | 84 | Fast battleship | Cancelled, never started |
| 4022 | Owari | 8 | 1922 | 41,000 | $13,500,000 | 84 | 2nd Kii | Cancelled, never started |
| 4023 | Number 13 | 9 | 1922 | 50,000 | $18,000,000 | 90 | Revolutionary design | 18.1" guns planned, cancelled |
| 4024 | Number 14 | 9 | 1922 | 51,000 | $18,500,000 | 90 | 2nd Number 13 | 30 kts, cancelled |
| 4025 | Kongō Kai | 8 | 1935 | 30,000 | $8,000,000 | 60 | Fast battleship refit | 30+ knots! Revolutionary |
| 4026 | Hiei Kai | 8 | 1936 | 31,000 | $8,200,000 | 60 | 2nd Kongō modernized | Fast BB conversion |
| 4027 | Haruna Kai | 8 | 1937 | 32,000 | $8,400,000 | 60 | 3rd Kongō modernized | 30+ knots |
| 4028 | Kirishima Kai | 8 | 1938 | 33,000 | $8,600,000 | 60 | 4th Kongō modernized | Fastest BBs afloat |
| 4029 | Nagato Kai | 9 | 1936 | 40,000 | $12,000,000 | 72 | Nagato modernization | Improved armor/AA |
| 4030 | Mutsu Kai | 9 | 1936 | 41,000 | $12,500,000 | 72 | Mutsu modernization | Enhanced capability |
| 4031 | Fusō Kai | 8 | 1933 | 28,000 | $7,000,000 | 66 | Fusō modernization | Reconstructed pagoda mast |
| 4032 | Yamashiro Kai | 8 | 1935 | 29,000 | $7,500,000 | 66 | Yamashiro modernization | Improved AA |
| 4033 | Yamato | 10 | 1940 | 100,000 | $100,000,000 | 120 | Super-battleship | LARGEST EVER! 18.1" guns |
| 4034 | Musashi | 10 | 1941 | 105,000 | $105,000,000 | 120 | 2nd Yamato | Sunk Leyte Gulf 1944 |
| 4035 | Shinano | 10 | 1944 | 110,000 | $90,000,000 | 90 | Carrier conversion | Converted to carrier |
| 4036 | Ise Kai-II | 9 | 1943 | 45,000 | $15,000,000 | 72 | Hybrid carrier-BB | Aft flight deck conversion |
| 4037 | Hyūga Kai-II | 9 | 1943 | 46,000 | $15,500,000 | 72 | 2nd hybrid conversion | 22 aircraft capacity |
| 4038 | Design A-150 | 10 | 1941 | 120,000 | $120,000,000 | 150 | Super Yamato | 20.1" guns! Cancelled |
| 4039 | Design A-150 (2) | 10 | 1941 | 125,000 | $125,000,000 | 150 | 2nd A-150 | Largest guns designed |
| 4040 | Post-War BB | 10 | 1950 | 150,000 | $150,000,000 | 180 | Theoretical post-war | Japan prohibited from BBs |
| 4041 | Guided Missile BB | 10 | 1960 | 180,000 | $200,000,000 | 210 | Theoretical modernization | Never pursued |
| 4042 | Future BB Concept | 10 | 1970 | 200,000 | $250,000,000 | 240 | Theoretical future | Never pursued |

### Special Abilities

**Node-Specific Abilities**:

| Node_ID | Ship_Class | Special_Ability | Effect |
|---------|------------|----------------|--------|
| 4000 | Mikasa | "Tsushima Victory" | Tōgō's flagship, +40% morale, historic preservation, FREE |
| 4017 | Nagato | "World's First 16-Inch" | First 16" guns afloat, +35% firepower, HISTORIC |
| 4018 | Mutsu | "Public Subscription" | Built by public donations, +25% morale |
| 4023 | Number 13 | "Ten Years Ahead" | Revolutionary design, +40% capability, -25% reliability (cancelled) |
| 4025 | Kongō Kai | "Fast Battleship Revolution" | 30+ knots, +50% speed, +40% capability, REVOLUTIONARY |
| 4033 | Yamato | "Largest Ever Built" | 18.1" guns, 72,000 tons, +100% capability, LEGENDARY |
| 4034 | Musashi | "Unsinkable Giant" | 17 bombs/19 torpedoes to sink, +60% survivability, HISTORIC |
| 4036 | Ise Kai-II | "Hybrid Concept" | Battleship + carrier, +30% versatility, -20% reliability |
| 4038 | Design A-150 | "Largest Guns Designed" | 20.1" guns, +120% firepower, -30% reliability (paper ship) |

**National Special Abilities** (Apply to all Japanese BB):
- **Japanese Naval Engineering**: +20% quality and precision craftsmanship
- **Pagoda Masts**: Distinctive multi-story fire control towers, +15% targeting
- **Tsushima Legacy**: Historic naval tradition, +15% crew quality
- **Big Gun Doctrine**: Emphasis on main battery firepower, +20% gunnery effectiveness

### Prerequisites Table

| Node_ID | Ship_Class | Prerequisite_Node_ID | Prerequisite_Ship_Class | Prerequisite_Type |
|---------|------------|---------------------|------------------------|-------------------|
| 4000 | Mikasa | NULL | NULL | Starting (FREE) |
| 4001 | Fuji | NULL | NULL | Starting (FREE) |
| 4002 | Shikishima | 4001 | Fuji | Required |
| 4003 | Asahi | 4002 | Shikishima | Required |
| 4004 | Katori | 4000, 4003 | Mikasa, Asahi | Required (AND) |
| 4005 | Satsuma | 4004 | Katori | Required |
| 4006 | Aki | 4005 | Satsuma | Required |
| 4007 | Kawachi | 4006 | Aki | Required |
| 4008 | Settsu | 4007 | Kawachi | Required |
| 4009 | Kongō | 4008 | Settsu | Required |
| 4010 | Hiei | 4009 | Kongō | Required |
| 4011 | Haruna | 4010 | Hiei | Required |
| 4012 | Kirishima | 4011 | Haruna | Required |
| 4013 | Fusō | 4012 | Kirishima | Required |
| 4014 | Yamashiro | 4013 | Fusō | Required |
| 4015 | Ise | 4014 | Yamashiro | Required |
| 4016 | Hyūga | 4015 | Ise | Required |
| 4017 | Nagato | 4016 | Hyūga | Required |
| 4018 | Mutsu | 4017 | Nagato | Required |
| 4019 | Tosa | 4018 | Mutsu | Required |
| 4020 | Kaga | 4019 | Tosa | Required |
| 4021 | Kii | 4020 | Kaga | Required |
| 4022 | Owari | 4021 | Kii | Required |
| 4023 | Number 13 | 4022 | Owari | Required |
| 4024 | Number 14 | 4023 | Number 13 | Required |
| 4025 | Kongō Kai | 4009 | Kongō | Required |
| 4026 | Hiei Kai | 4025 | Kongō Kai | Required |
| 4027 | Haruna Kai | 4026 | Hiei Kai | Required |
| 4028 | Kirishima Kai | 4027 | Haruna Kai | Required |
| 4029 | Nagato Kai | 4017 | Nagato | Required |
| 4030 | Mutsu Kai | 4029 | Nagato Kai | Required |
| 4031 | Fusō Kai | 4013 | Fusō | Required |
| 4032 | Yamashiro Kai | 4031 | Fusō Kai | Required |
| 4033 | Yamato | 4018, 4024 | Mutsu, Number 14 | Required (AND) |
| 4034 | Musashi | 4033 | Yamato | Required |
| 4035 | Shinano | 4034 | Musashi | Required |
| 4036 | Ise Kai-II | 4015 | Ise | Required |
| 4037 | Hyūga Kai-II | 4036 | Ise Kai-II | Required |
| 4038 | Design A-150 | 4033 | Yamato | Required |
| 4039 | Design A-150 (2) | 4038 | Design A-150 | Required |
| 4040 | Post-War BB | 4033 | Yamato | Required |
| 4041 | Guided Missile BB | 4040 | Post-War BB | Required |
| 4042 | Future BB Concept | 4041 | Guided Missile BB | Required |

### Unlocks Table

| Node_ID | Ship_Class | Unlocks_Node_ID | Unlocks_Ship_Class | Unlock_Type |
|---------|------------|----------------|-------------------|-------------|
| 4000 | Mikasa | 4004 | Katori | Research |
| 4001 | Fuji | 4002 | Shikishima | Research |
| 4002 | Shikishima | 4003 | Asahi | Research |
| 4003 | Asahi | 4004 | Katori | Research |
| 4004 | Katori | 4005 | Satsuma | Research |
| 4005 | Satsuma | 4006 | Aki | Research |
| 4006 | Aki | 4007 | Kawachi | Research |
| 4007 | Kawachi | 4008 | Settsu | Research |
| 4008 | Settsu | 4009 | Kongō | Research |
| 4009 | Kongō | 4010, 4025 | Hiei, Kongō Kai | Research |
| 4010 | Hiei | 4011 | Haruna | Research |
| 4011 | Haruna | 4012 | Kirishima | Research |
| 4012 | Kirishima | 4013 | Fusō | Research |
| 4013 | Fusō | 4014, 4031 | Yamashiro, Fusō Kai | Research |
| 4014 | Yamashiro | 4015 | Ise | Research |
| 4015 | Ise | 4016, 4036 | Hyūga, Ise Kai-II | Research |
| 4016 | Hyūga | 4017 | Nagato | Research |
| 4017 | Nagato | 4018, 4029 | Mutsu, Nagato Kai | Research |
| 4018 | Mutsu | 4019, 4033 | Tosa, Yamato | Research |
| 4019 | Tosa | 4020 | Kaga | Research |
| 4020 | Kaga | 4021 | Kii | Research |
| 4021 | Kii | 4022 | Owari | Research |
| 4022 | Owari | 4023 | Number 13 | Research |
| 4023 | Number 13 | 4024 | Number 14 | Research |
| 4024 | Number 14 | 4033 | Yamato | Research |
| 4025 | Kongō Kai | 4026 | Hiei Kai | Research |
| 4026 | Hiei Kai | 4027 | Haruna Kai | Research |
| 4027 | Haruna Kai | 4028 | Kirishima Kai | Research |
| 4029 | Nagato Kai | 4030 | Mutsu Kai | Research |
| 4031 | Fusō Kai | 4032 | Yamashiro Kai | Research |
| 4033 | Yamato | 4034, 4038, 4040 | Musashi, A-150, Post-War | Research |
| 4034 | Musashi | 4035 | Shinano | Research |
| 4036 | Ise Kai-II | 4037 | Hyūga Kai-II | Research |
| 4038 | Design A-150 | 4039 | Design A-150 (2) | Research |
| 4040 | Post-War BB | 4041 | Guided Missile BB | Research |
| 4041 | Guided Missile BB | 4042 | Future BB Concept | Research |

### Research Branches Table

| Branch_ID | Branch_Name | Description | Starting_Node_ID | Tech_Tier_Range |
|-----------|-------------|-------------|------------------|--------------------|
| JP_BB_01 | Pre-Dreadnoughts | Early battleships from Fuji through Satsuma | 4001-4006 | 1-4 |
| JP_BB_02 | First Dreadnoughts | Kawachi and Settsu, Japan's first all-big-gun battleships | 4007-4008 | 5 |
| JP_BB_03 | Kongō Battlecruisers | Fast battlecruisers with British design influence | 4009-4012 | 6 |
| JP_BB_04 | Super-Dreadnoughts | Fusō and Ise classes with distinctive pagoda masts | 4013-4016 | 7 |
| JP_BB_05 | 16-Inch Gun Era | Nagato class, world's first 16" gun battleships | 4017-4018 | 8 |
| JP_BB_06 | Washington Treaty Cancellations | Tosa, Kii, and Number 13 classes cancelled by treaty | 4019-4024 | 8-9 |
| JP_BB_07 | Fast Battleship Conversions | Kongō class modernized to 30+ knot fast battleships | 4025-4028 | 8 |
| JP_BB_08 | Interwar Modernizations | Nagato and Fusō class reconstructions | 4029-4032 | 8-9 |
| JP_BB_09 | Yamato Class | Largest battleships ever built with 18.1" guns | 4033-4035 | 10 |
| JP_BB_10 | Hybrid Conversions | Ise/Hyūga battleship-carrier hybrids | 4036-4037 | 9 |
| JP_BB_11 | Paper Ships | Design A-150 "Super Yamato" and theoretical post-war designs | 4038-4042 | 10 |

## Branch Descriptions

### 1. Pre-Dreadnoughts (6 nodes)

**Fuji (1896) & Shikishima (1898)**: British-built battleships that formed the core of Japan's modern fleet during the Russo-Japanese War. Fuji (12,533 tons, 4×12" guns) represented Japan's first modern capital ships.

**Asahi (1899)**: Improved pre-dreadnought design with better armor distribution. Participated in Tsushima and served as repair ship in WWII.

**Mikasa (1900)**: Admiral Tōgō's flagship at the **Battle of Tsushima** (May 27-28, 1905)—the decisive naval victory that destroyed the Russian Baltic Fleet and established Japan as a world power. Preserved at Yokosuka as a national treasure (+40% morale bonus). Specifications: 15,140 tons, 4×12" guns, 18 knots.

**Katori Class (1905)**: Post-Tsushima design incorporating combat lessons. Katori and Kashima (2 ships) represented the peak of Japanese pre-dreadnought development.

**Satsuma Class (1906)**: Japan's first major warships built domestically without foreign assistance. **Semi-dreadnoughts** with 4×12" main guns and 12×10" intermediate guns. Satsuma and Aki (2 ships) represented Japan's transition to indigenous battleship construction.

### 2. First Dreadnoughts (2 nodes)

**Kawachi Class (1910-1911)**: Japan's first all-big-gun dreadnought battleships. Kawachi and Settsu displaced 21,443 tons with 12×12" guns (unique 3×2 + 2×3 turret arrangement). Kawachi exploded July 12, 1918 (magazine explosion, 621 dead). Settsu survived as training ship.

### 3. Kongō Battlecruisers (4 nodes)

**Kongō (1912)**: Built at Vickers (Britain)—the last Japanese capital ship built abroad. Designed by Sir George Thurston as fast battlecruiser: 27,500 tons, 8×14" guns, 27.5 knots. Became prototype for all four ships.

**Hiei, Haruna, Kirishima (1912-1913)**: Japanese-built sisters constructed at Yokosuka, Kobe, and Nagasaki. All 4 ships featured distinctive profile and speed. Originally battlecruisers, later reclassified as fast battleships after reconstruction.

These ships would undergo revolutionary modernization in the 1930s (see Branch 7).

### 4. Super-Dreadnoughts (4 nodes)

**Fusō Class (1914-1915)**: Revolutionary design with **6 twin turrets** (12×14" guns)—the most main guns on any Japanese battleship. Created distinctive "pagoda mast" silhouette from multiple rebuilds. Fusō and Yamashiro (2 ships) displaced 35,900 tons. Both sunk at **Battle of Surigao Strait** (October 25, 1944)—the last battleship-vs-battleship action in history.

**Ise Class (1916-1917)**: Improved Fusō design with better turret arrangement. Ise and Hyūga (2 ships) displaced 36,500 tons with 12×14" guns. Later converted to hybrid battleship-carriers (see Branch 10).

### 5. 16-Inch Gun Era (2 nodes)

**Nagato (1919)**: **World's first battleship with 16-inch guns** (8×16.1"/41cm in 4 twin turrets). Displacement: 39,130 tons. Speed: 26.7 knots (80,000 shp). The 16.1" guns were the largest naval guns afloat until the 1930s. Admiral Yamamoto's flagship at Pearl Harbor. Survived WWII, used as target at **Bikini Atoll nuclear tests** (1946).

**Mutsu (1920)**: Sister ship built with public subscription funds (+25% morale). **Magazine explosion** June 8, 1943 in Hiroshima Bay (1,121 dead)—Japan's worst non-combat naval loss.

### 6. Washington Treaty Cancellations (6 nodes)

**Tosa Class (1921)**: Improved Nagato design with 10×16.1" guns, 39,900 tons. Two ships planned:
- **Tosa**: 40% complete when cancelled, used as gunnery target (sunk 1925)
- **Kaga**: Converted to aircraft carrier after treaty

**Kii Class (1922)**: Fast battleship design with 10×16.1" guns, 42,600 tons, 29.75 knots. Kii and Owari never started construction—cancelled before any work began.

**Number 13 Class (1922)**: Revolutionary design called "**ten years ahead of their time**" by historians. Specifications:
- **Displacement**: 47,500 tons
- **Main Armament**: 8×18.1" (46cm) guns in 4 twin turrets
- **Speed**: 30 knots (150,000 shp)
- Four ships planned (Numbers 13, 14, 15, 16). Design nearly complete when Washington Treaty cancelled program (November 19, 1923). If built, would have been the world's most powerful battleships of the 1920s.

### 7. Fast Battleship Conversions (4 nodes)

**Kongō Class Modernization (1935-1940)**: The most extensive battleship reconstructions ever undertaken. All four Kongō-class ships underwent revolutionary rebuilds:

**Original (1913)**: 27,500 tons, 8×14" guns, 27.5 knots (battlecruiser)
**Reconstructed (1940)**: 31,700 tons, 8×14" guns, **30+ knots** (fast battleship)

**Key Improvements**:
- New turbines and boilers (150,000 shp, +50% power)
- Extended bow and stern (+26 meters length)
- Improved armor and torpedo protection
- Enhanced AA armament (96+ 25mm guns)
- Modernized fire control

**Result**: The **fastest battleships in the world** at 30+ knots, enabling them to escort carrier task forces. All four participated extensively in Pacific War—more combat than any other Japanese battleships:
- **Kongō**: Sunk by submarine USS Sealion, November 21, 1944
- **Hiei**: Sunk at Guadalcanal, November 13, 1942
- **Haruna**: Sunk at Kure, July 28, 1945
- **Kirishima**: Sunk at Guadalcanal, November 15, 1942

### 8. Interwar Modernizations (4 nodes)

**Nagato/Mutsu Modernization (1936)**: Extensive reconstruction increasing displacement to 42,850 tons. Improved armor, enhanced AA (98× 25mm guns), new fire control, reinforced torpedo protection.

**Fusō/Yamashiro Modernization (1933-1935)**: Major rebuilds creating iconic multi-story "pagoda masts." Enhanced protection, modern fire control, improved engines. Both sunk at Surigao Strait (1944).

### 9. Yamato Class (3 nodes)

**Yamato (1940)**: The **largest battleship ever built**. Specifications:
- **Displacement**: 72,000 tons full load (heaviest warship until supercarriers)
- **Main Armament**: 9×46cm (18.1") Type 94 guns in 3 triple turrets
  - Largest naval guns ever mounted on a warship
  - Shell weight: 1,460 kg (3,220 lb)—the heaviest naval shells
  - Maximum range: 42 km (26 miles)
- **Armor**: 410mm main belt, 650mm turret face—thickest ever
- **Powerplant**: 150,000 shp, 27 knots
- **Crew**: 2,767

**Construction**: Laid down November 4, 1937. Launched August 8, 1940. Commissioned December 16, 1941. Built in extreme secrecy at Kure Naval Arsenal.

**Fate**: Sunk during **Operation Ten-Go** (April 7, 1945)—suicide mission to Okinawa. Attacked by 386 US carrier aircraft. Hit by 12+ torpedoes and 7+ bombs. Magazine exploded. 2,498 crew died, 269 survived. End of the battleship era.

**Musashi (1941)**: Second Yamato-class. Commissioned August 5, 1942. Sunk at **Battle of Sibuyan Sea** (October 24, 1944) during Leyte Gulf campaign. **Most heavily damaged battleship ever to sink**: 17 bombs, 19 torpedoes, 4+ hours to sink (+60% survivability rating). 1,023 crew died.

**Shinano (1944)**: Third Yamato hull converted to aircraft carrier after Midway disaster (June 1942). Completed as carrier November 19, 1944. **Sunk 10 days later** by USS Archerfish (November 29, 1944)—the largest warship ever sunk by submarine. Torpedoed on maiden voyage, poor damage control training, 1,435 dead.

### 10. Hybrid Conversions (2 nodes)

**Ise/Hyūga Kai-II (1943)**: Desperate response to carrier losses at Midway. Unique **battleship-carrier hybrid** conversions:
- Aft turrets (5-6) removed
- 70-meter flight deck installed aft
- Capacity: 22 aircraft (seaplanes launched by catapults)
- Forward armament retained: 8×14" guns in 4 turrets

**Concept**: Combine battleship firepower with carrier aviation (+30% versatility). **Reality**: Aircraft never embarked due to pilot shortage. Operated as AA escorts instead. Both survived war, scrapped 1946-1947.

### 11. Paper Ships (5 nodes)

**Design A-150 "Super Yamato" (1941)**: The ultimate battleship design. Planned specifications:
- **Displacement**: ~90,000 tons
- **Main Armament**: 6×51cm (20.1") guns in 3 twin turrets
  - **Largest battleship guns ever designed**
  - Shell weight: 1,950 kg (4,300 lb)
  - Each gun: 227 metric tons
  - Range: Similar to Yamato (~40 km)
- **Speed**: 30+ knots

**Development**: Design work 1938-1941, nearly complete by early 1941. Two 51cm guns ordered for testing at Kure Naval Arsenal. Cancelled when war with US became imminent—Japan prioritized carriers and cruisers instead (+120% firepower, -30% reliability as paper ship).

**Post-War Designs**: Theoretical only. Japan prohibited from major warships by occupation. No post-war battleship program pursued.

## Gameplay Notes

### Balance Considerations

1. **Yamato as Ultimate Goal**: Most expensive and powerful BB (100,000 RP, $100M, Tier 10)
2. **Fast Battleship Power**: Kongō Kai modernizations offer exceptional speed (30+ kts, +50% speed bonus)
3. **Firepower Progression**: 12" → 14" → 16.1" → 18.1" → 20.1" (paper)
4. **Historical Authenticity**: Special abilities reflect actual historic achievements
5. **Paper Ship Penalty**: A-150 and post-war designs have reliability penalties
6. **Cost Scaling**: Massive jump at Yamato tier reflects revolutionary capability
7. **Modernization Branches**: Multiple upgrade paths (Kongō, Nagato, Fusō lines)

### Japanese Battleship Characteristics

**Strengths**:
- **Firepower**: Largest guns in game (18.1" Yamato, 20.1" A-150 paper)
- **Quality**: Exceptional construction quality (+20% engineering bonus)
- **Speed**: Kongō Kai fast battleships (30+ knots) enable carrier escort
- **Innovation**: World's first 16" guns (Nagato), largest BBs ever (Yamato)
- **Tradition**: Tsushima legacy provides morale and crew quality bonuses

**Weaknesses**:
- **Cost**: Extremely expensive at top tiers (Yamato: $100M, A-150: $120M)
- **Late Bloom**: Peak capability late in tree (Tier 10)
- **Hybrid Inefficiency**: Ise conversions have -20% reliability penalty
- **Paper Ship Heavy**: 8 of 43 nodes are cancelled/theoretical designs
- **Historical Fate**: All lost in WWII (none survived to preservation except Mikasa)

### Strategic Role

**Pre-Dreadnought Era** (Tier 1-4): Building foundation of Japanese naval power, Tsushima victory establishes tradition.

**Dreadnought Era** (Tier 5-7): Development of indigenous designs, incorporation of foreign expertise (British influence on Kongō).

**Treaty Era** (Tier 8-9): Ambitious "Eight-Eight Fleet" program cancelled, focus shifts to quality over quantity. Extensive modernizations maintain competitiveness.

**Super-Battleship Era** (Tier 10): Ultimate expression of big-gun doctrine with Yamato class. A-150 design represents final evolution that was never realized.

## Historical Ship Counts

**Russo-Japanese War** (1904-1905): 6 battleships (Fuji, Yashima, Shikishima, Hatsuse, Asahi, Mikasa)
- **Battle of Tsushima** (May 27-28, 1905): Decisive victory, 4 battleships participated

**WWI** (1914-1918): 14 battleships (pre-dreadnoughts + Kawachi, Settsu, Kongō class, Fusō class)
- Limited action, primarily escorted convoys

**Interwar** (1919-1941): Constructed Nagato class, modernized older ships, cancelled 8 ships (Washington Treaty)

**WWII** (1941-1945): 12 battleships participated (Kongō×4, Fusō×2, Ise×2, Nagato×2, Yamato×2)

**WWII Losses**:
- **1942**: Hiei (November 13, Guadalcanal)
- **1942**: Kirishima (November 15, Guadalcanal)
- **1943**: Mutsu (June 8, magazine explosion)
- **1944**: Fusō (October 25, Surigao Strait)
- **1944**: Yamashiro (October 25, Surigao Strait)
- **1944**: Musashi (October 24, Sibuyan Sea)
- **1944**: Kongō (November 21, submarine attack)
- **1945**: Yamato (April 7, Operation Ten-Go)
- **1945**: Haruna (July 28, air attack at Kure)
- **1945**: Ise (July 28, air attack at Kure)
- **1945**: Hyūga (July 28, air attack at Kure)

**Survivors**: Nagato (only battleship to survive, used in Bikini Atoll nuclear tests 1946)

**Post-War**: 0 battleships (Japan prohibited from major warships, 1947 constitution prohibits offensive military)

---

*Document Version: 1.0*
*Last Updated: 2025-10-11*
*Status: Complete - Ready for database implementation*
*Historical Note: Japan built the largest and most powerful battleships ever constructed (Yamato class), representing the ultimate expression of big-gun battleship doctrine before carriers dominated naval warfare*
