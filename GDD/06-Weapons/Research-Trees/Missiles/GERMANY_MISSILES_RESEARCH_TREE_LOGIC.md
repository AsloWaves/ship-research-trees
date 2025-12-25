# German Missiles Research Tree Logic

**Tech Branch**: Missiles
**Nation**: German
**Era**: 1969-2025
**Node Count**: 26 nodes

## Categories
1. **SAM** (Surface-to-Air Missiles): 12 nodes
2. **SSM** (Surface-to-Surface/Anti-Ship Missiles): 10 nodes
3. **ASW** (Anti-Submarine Warfare Missiles): 4 nodes

## Research Tree Structure

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 2300 | German | RIM-24B Tartar (German) | SAM | 1969 | Missiles | Missile | 0 | 0 | 0 | 0 | 1 | | 2301 | 0 |
| 2301 | German | RIM-66A Standard MR (German) | SAM | 1975 | Missiles | Missile | 3500 | 80 | 20 | 52 | 0 | 2300 | 2302 | 0 |
| 2302 | German | SM-1MR Block VI (German) | SAM | 1990 | Missiles | Missile | 5000 | 115 | 25 | 70 | 0 | 2301 | 2310 | 0 |
| 2310 | German | RAM Block 0 (German) | SAM | 1992 | Missiles | Missile | 0 | 0 | 0 | 0 | 1 | | 2311 | 0 |
| 2311 | German | RAM Block 1 | SAM | 2000 | Missiles | Missile | 3000 | 70 | 12 | 48 | 0 | 2310 | 2312 | 0 |
| 2312 | German | RAM Block 2 | SAM | 2015 | Missiles | Missile | 4000 | 90 | 15 | 58 | 0 | 2311 | 2313 | 0 |
| 2313 | German | RAM Block 2A | SAM | 2020 | Missiles | Missile | 4500 | 105 | 17 | 65 | 0 | 2312 | | 0 |
| 2314 | German | Sea Sparrow NATO | SAM | 1976 | Missiles | Missile | 0 | 0 | 0 | 0 | 1 | | 2315 | 0 |
| 2315 | German | ESSM Block I (German) | SAM | 2005 | Missiles | Missile | 4000 | 90 | 18 | 55 | 0 | 2314 | 2316 | 0 |
| 2316 | German | ESSM Block II (German) | SAM | 2020 | Missiles | Missile | 5000 | 115 | 20 | 65 | 0 | 2315 | | 0 |
| 2317 | German | IRIS-T SLM | SAM | 2014 | Missiles | Missile | 5500 | 130 | 22 | 75 | 0 | 2312,2315 | 2318 | 0 |
| 2318 | German | IRIS-T SLM Block II | SAM | 2022 | Missiles | Missile | 6500 | 155 | 24 | 85 | 0 | 2317 | | 0 |
| 2340 | German | MM38 Exocet (German) | SSM | 1977 | Missiles | Missile | 0 | 0 | 0 | 0 | 1 | | 2341 | 0 |
| 2341 | German | MM40 Exocet Block 2 | SSM | 1992 | Missiles | Missile | 5000 | 115 | 24 | 65 | 0 | 2340 | 2342 | 0 |
| 2342 | German | MM40 Block 3 (German) | SSM | 2010 | Missiles | Missile | 6000 | 140 | 28 | 78 | 0 | 2341 | 2343 | 0 |
| 2343 | German | RGM-84 Harpoon (German) | SSM | 1985 | Missiles | Missile | 5500 | 125 | 26 | 70 | 0 | 2341 | 2344 | 0 |
| 2344 | German | Harpoon Block II (German) | SSM | 2000 | Missiles | Missile | 6500 | 150 | 28 | 82 | 0 | 2343 | 2345 | 0 |
| 2345 | German | NSM (German) | SSM | 2017 | Missiles | Missile | 8000 | 185 | 32 | 100 | 0 | 2344 | 2346 | 0 |
| 2346 | German | NSM Block II | SSM | 2023 | Missiles | Missile | 9000 | 210 | 35 | 112 | 0 | 2345 | | 0 |
| 2347 | German | Kormoran Mk 1 | SSM | 1977 | Missiles | Missile | 3000 | 70 | 18 | 42 | 0 | 2340 | 2348 | 0 |
| 2348 | German | Kormoran Mk 2 | SSM | 1991 | Missiles | Missile | 3500 | 80 | 20 | 48 | 0 | 2347 | 2349 | 0 |
| 2349 | German | IDAS (Sub-Launched) | SSM | 2008 | Missiles | Missile | 4500 | 105 | 22 | 60 | 0 | 2348 | | 0 |
| 2360 | German | VL-ASROC (German) | ASW | 1995 | Missiles | Missile | 0 | 0 | 0 | 0 | 1 | | 2361 | 0 |
| 2361 | German | VL-ASROC Block II (German) | ASW | 2010 | Missiles | Missile | 5500 | 125 | 26 | 68 | 0 | 2360 | 2362 | 0 |
| 2362 | German | RUM-139C (NATO) | ASW | 2022 | Missiles | Missile | 6500 | 150 | 28 | 78 | 0 | 2361 | | 0 |
| 2363 | German | Sea Urchin (License) | ASW | 2012 | Missiles | Missile | 4500 | 105 | 22 | 58 | 0 | 2361 | 2362 | 0 |

## Research Prerequisites Logic

### SAM Systems Evolution
1. **US Technology Transfer** (1969-1990)
   - Tartar (2300): US missile for German frigates
   - Standard MR (2301-2302): Adams-class destroyers

2. **NATO Point Defense** (1992-2020)
   - RAM (2310): German-US collaboration → Block 1/2/2A
   - Sea Sparrow/ESSM (2314-2316): NATO Sea Sparrow Consortium

3. **Indigenous Development** (2014-2022)
   - IRIS-T SLM (2317): German air-to-air adapted for naval use
   - Diehl Defence technology

### SSM Systems Evolution
1. **European Collaboration** (1977-2010)
   - Exocet MM38/40 (2340-2342): French partnership
   - Kormoran (2347-2348): German anti-ship missiles
   - Harpoon (2343-2344): US technology transfer

2. **Modern Anti-Ship** (2017-2023)
   - NSM (2345-2346): Norwegian Naval Strike Missile partnership
   - IDAS (2349): Submarine-launched multirole

### ASW Systems Evolution
1. **NATO ASW** (1995-2022)
   - VL-ASROC German variants (2360-2362)
   - Sea Urchin license production (2363)

## Nation Progression Logic

**Starting Technologies** (1969):
- RIM-24B Tartar (Node 2300): US-supplied SAM → Standard MR progression
- RAM Block 0 (Node 2310): German-US CIWS development
- Sea Sparrow NATO (Node 2314): NATO consortium membership
- MM38 Exocet (Node 2340): European anti-ship capability
- VL-ASROC (Node 2360): NATO ASW capability

**Technology Convergence Points**:
- Node 2302 (SM-1MR): US technology mature → enables indigenous development
- Node 2317 (IRIS-T SLM): Converges RAM and ESSM lines into German system
- Node 2345 (NSM): Converges Exocet and Harpoon lines

**High-Cost Nodes** (Research Cost >8000):
- NSM German (8000): Modern stealth anti-ship
- NSM Block II (9000): Advanced networking and range

**International Partnerships**:
- **US**: Tartar, Standard, RAM, Harpoon, ASROC systems
- **France**: Exocet family
- **Norway**: NSM variants
- **UK**: Sea Urchin license
- **NATO**: ESSM consortium

**Tree Depth**: 9 generations (1969-2025, average 6.2 years/generation)

**Technology Philosophy**:
- Heavy reliance on NATO partnerships and technology transfer
- Focus on proven systems over indigenous development
- Late-period indigenous capabilities (IRIS-T, IDAS)
- Emphasis on defensive systems and point defense
