# Naval Missiles Database

**Export Date**: October 10, 2025
**Database Version**: 1.0
**Total Records**: 0 (ready for expansion)

---

## Database Contents

- [Missiles Table](#missiles-table) - Naval missile systems
- [Warheads Table](#warheads-table) - Missile warhead specifications
- [Launch Systems Table](#launch-systems-table) - Missile launcher configurations
- [Targeting Systems Table](#targeting-systems-table) - Guidance and radar systems

---

<a name="missiles-table"></a>
## Missiles Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Missile_ID | INT | Primary key, unique identifier |
| Country | VARCHAR(50) | Nation of origin |
| Designation | VARCHAR(100) | Official designation (e.g., "RIM-66 Standard", "Exocet MM.40", "Harpoon") |
| NATO_Codename | VARCHAR(100) | NATO reporting name (for Soviet/Russian missiles) |
| Type | VARCHAR(50) | SAM, SSM, ASW, ASROC, Cruise, Ballistic |
| Role | VARCHAR(100) | Anti-ship, anti-air, anti-submarine, land-attack |
| Year_Introduced | INT | Year entered service |
| Diameter_IN | DECIMAL(5,2) | Body diameter in inches |
| Length_FT | DECIMAL(6,2) | Total length in feet |
| Wingspan_FT | DECIMAL(6,2) | Wingspan/fin span in feet |
| Weight_LBS | INT | Total launch weight in pounds |
| Warhead_LBS | INT | Warhead weight in pounds |
| Warhead_Type | VARCHAR(50) | HE, Frag, Continuous-rod, Nuclear, etc. |
| Max_Speed_MACH | DECIMAL(4,2) | Maximum speed in Mach |
| Max_Range_NM | INT | Maximum range in nautical miles |
| Min_Range_NM | DECIMAL(5,2) | Minimum engagement range |
| Max_Altitude_FT | INT | Maximum engagement altitude |
| Min_Altitude_FT | INT | Minimum engagement altitude (sea-skimming capability) |
| Propulsion | VARCHAR(100) | Booster/sustainer type |
| Guidance | VARCHAR(200) | Guidance system (radar, IR, GPS, inertial, terminal homing) |
| Launch_Platform | VARCHAR(200) | Compatible ships/submarines |
| Modded | TINYINT | 0 = historical, 1 = fictional/generated |
| Notes | TEXT | Operational history, variants, performance notes |

**Total Entries**: 0 missiles
**Planned Coverage**: 1950-2025
**ID Allocation**:
- USA: 2000-2199 (SAM: 2000-2049, SSM: 2050-2099, Other: 2100-2149, Fictional: 2150-2199)
- British: 2200-2299
- French: 2300-2399
- Soviet/Russian: 2400-2499
- Chinese: 2500-2599
- Israeli: 2600-2649
- Italian: 2650-2699
- German: 2700-2749
- Japanese: 2750-2799
- Other Nations: 2800-2899
- Fictional/Multi-national: 2900-2999

| Missile_ID | Country | Designation | NATO_Codename | Type | Role | Year_Introduced | Diameter_IN | Length_FT | Wingspan_FT | Weight_LBS | Warhead_LBS | Warhead_Type | Max_Speed_MACH | Max_Range_NM | Min_Range_NM | Max_Altitude_FT | Min_Altitude_FT | Propulsion | Guidance | Launch_Platform | Modded | Notes |
|------------|---------|-------------|---------------|------|------|-----------------|-------------|-----------|-------------|------------|-------------|--------------|----------------|--------------|--------------|-----------------|-----------------|------------|----------|-----------------|--------|-------|
| | | | | | | | | | | | | | | | | | | | | | | |

**Example Entries** (for reference - not yet in database):

### USA Surface-to-Air Missiles (SAM)
- **RIM-2 Terrier** - First US naval SAM (1956)
- **RIM-8 Talos** - Long-range beam-riding SAM
- **RIM-24 Tartar** - Medium-range SAM
- **RIM-66 Standard SM-1/SM-2** - Aegis system workhorse
- **RIM-67 Standard ER** - Extended range variant
- **RIM-161 Standard SM-3** - Ballistic missile defense
- **RIM-162 ESSM** - Evolved Sea Sparrow, quad-pack
- **RIM-116 RAM** - Rolling Airframe Missile, CIWS

### USA Surface-to-Surface Missiles (SSM)
- **RGM-6 Regulus** - Early cruise missile (1950s)
- **RGM-15 Regulus II** - Supersonic cruise missile
- **RGM-84 Harpoon** - Standard anti-ship missile
- **BGM-109 Tomahawk** - Long-range land-attack cruise
- **AGM-158C LRASM** - Long-Range Anti-Ship Missile

### USA Anti-Submarine Weapons
- **RUR-5 ASROC** - Anti-Submarine ROCket
- **RUM-139 VL-ASROC** - Vertical launch variant

### British Missiles
- **Sea Slug** - Early beam-riding SAM
- **Sea Dart** - Medium-range SAM (1970s-2010s)
- **Sea Wolf** - Point defense SAM
- **Sea Viper (Aster 15/30)** - Modern SAM system
- **Sea Skua** - Helicopter-launched anti-ship
- **Exocet MM.38** - Licensed French anti-ship missile

### French Missiles
- **MM.38 Exocet** - Ship-launched anti-ship
- **MM.40 Exocet** - Extended range variant
- **AM.39 Exocet** - Air-launched variant
- **Aster 15** - Short-range SAM
- **Aster 30** - Long-range SAM

### Soviet/Russian Missiles
- **P-15 Termit (SS-N-2 Styx)** - First Soviet anti-ship missile
- **P-120 Malakhit (SS-N-9 Siren)** - Submarine-launched
- **P-270 Moskit (SS-N-22 Sunburn)** - Supersonic sea-skimmer
- **P-500 Bazalt (SS-N-12 Sandbox)** - Heavy anti-ship
- **P-700 Granit (SS-N-19 Shipwreck)** - Oscar-class submarine missile
- **P-800 Oniks (SS-N-26 Strobile)** - Modern supersonic
- **3M-54 Kalibr (SS-N-27 Sizzler)** - Cruise missile family
- **S-300F Fort (SA-N-6 Grumble)** - Long-range SAM
- **9M96 (SA-N-21)** - Modern SAM

### Chinese Missiles
- **YJ-83** - Modern anti-ship missile
- **YJ-12** - Supersonic anti-ship
- **YJ-18** - Subsonic/supersonic cruise
- **HQ-9** - Long-range SAM

---

<a name="warheads-table"></a>
## Warheads Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Warhead_ID | INT | Primary key |
| Missile_ID | INT | Foreign key to missiles table |
| Designation | VARCHAR(100) | Warhead designation |
| Type | VARCHAR(50) | HE, HE-Frag, Continuous-rod, Blast-frag, Nuclear, Shaped-charge |
| Weight_LBS | INT | Total warhead weight |
| Explosive_Weight_LBS | INT | Net explosive weight |
| Explosive_Type | VARCHAR(50) | Composition (HBX, PBXN, etc.) |
| Fuze_Type | VARCHAR(100) | Contact, proximity, delayed, laser proximity |
| Blast_Radius_FT | DECIMAL(6,1) | Effective blast radius |
| Fragmentation | VARCHAR(200) | Fragment type and pattern |
| Nuclear_Yield_KT | DECIMAL(5,2) | Nuclear yield in kilotons (if applicable) |
| Penetration_IN | DECIMAL(5,1) | Armor penetration (if shaped charge) |
| Notes | TEXT | Additional information |

| Warhead_ID | Missile_ID | Designation | Type | Weight_LBS | Explosive_Weight_LBS | Explosive_Type | Fuze_Type | Blast_Radius_FT | Fragmentation | Nuclear_Yield_KT | Penetration_IN | Notes |
|------------|------------|-------------|------|------------|----------------------|----------------|-----------|-----------------|---------------|------------------|----------------|-------|
| | | | | | | | | | | | | |

---

<a name="launch-systems-table"></a>
## Launch Systems Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Launcher_ID | INT | Primary key |
| Country | VARCHAR(50) | Nation |
| Designation | VARCHAR(100) | Launcher designation |
| Type | VARCHAR(50) | VLS, Arm launcher, Box launcher, Canister, Silo |
| Missile_Compatibility | VARCHAR(500) | Compatible missile types |
| Cell_Count | INT | Number of cells/rails/tubes |
| Reload_Capable | TINYINT | 1 = at-sea reload, 0 = port reload only |
| Reload_Time_MIN | DECIMAL(5,1) | Reload time per cell/missile |
| Traverse_Rate_DEG_SEC | DECIMAL(5,2) | Traverse rate (for arm launchers) |
| Elevation_Rate_DEG_SEC | DECIMAL(5,2) | Elevation rate (for arm launchers) |
| Fire_Rate_SEC | DECIMAL(5,1) | Time between launches |
| Year_Introduced | INT | Year entered service |
| Weight_TONS | DECIMAL(7,2) | System weight in tons (empty) |
| Dimensions_FT | VARCHAR(100) | Physical dimensions |
| Platform_Type | VARCHAR(200) | Ship classes used on |
| Modded | TINYINT | 0 = historical, 1 = fictional |
| Notes | TEXT | Additional information |

| Launcher_ID | Country | Designation | Type | Missile_Compatibility | Cell_Count | Reload_Capable | Reload_Time_MIN | Traverse_Rate_DEG_SEC | Elevation_Rate_DEG_SEC | Fire_Rate_SEC | Year_Introduced | Weight_TONS | Dimensions_FT | Platform_Type | Modded | Notes |
|-------------|---------|-------------|------|-----------------------|------------|----------------|-----------------|----------------------|----------------------|---------------|-----------------|-------------|---------------|---------------|--------|-------|
| | | | | | | | | | | | | | | | | |

**Example Launcher Systems**:
- **Mk 41 VLS** (USA) - Universal VLS, 8-cell modules, most common modern launcher
- **Mk 57 PVLS** (USA) - Peripheral VLS for DDG-1000
- **Mk 13** (USA) - Single-arm launcher, guided missiles
- **Mk 26** (USA) - Twin-arm launcher, Standard/ASROC
- **Mk 10** (USA) - Twin-arm launcher, Terrier/Talos
- **SYLVER** (French) - Vertical launcher for Aster missiles
- **UKSK** (Russian) - Universal shipborne launcher, cold-launch
- **Mk 48 VLS** (Chinese) - VLS for Type 052D destroyers

---

<a name="targeting-systems-table"></a>
## Targeting Systems Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| System_ID | INT | Primary key |
| Country | VARCHAR(50) | Nation |
| Designation | VARCHAR(100) | System designation |
| Type | VARCHAR(50) | Fire control radar, Search radar, Illuminator, Datalink |
| Frequency_Band | VARCHAR(50) | X-band, S-band, C-band, Ku-band, etc. |
| Max_Range_NM | INT | Maximum detection/tracking range |
| Max_Targets | INT | Simultaneous target tracking capacity |
| Guidance_Channels | INT | Simultaneous missile guidance channels |
| Scan_Rate_RPM | DECIMAL(5,1) | Antenna scan rate |
| Year_Introduced | INT | Year entered service |
| Associated_Missiles | VARCHAR(500) | Compatible missile systems |
| Platform_Type | VARCHAR(200) | Ships/systems used on |
| Modded | TINYINT | 0 = historical, 1 = fictional |
| Notes | TEXT | Additional information |

| System_ID | Country | Designation | Type | Frequency_Band | Max_Range_NM | Max_Targets | Guidance_Channels | Scan_Rate_RPM | Year_Introduced | Associated_Missiles | Platform_Type | Modded | Notes |
|-----------|---------|-------------|------|----------------|--------------|-------------|-------------------|---------------|-----------------|---------------------|---------------|--------|-------|
| | | | | | | | | | | | | | |

**Example Targeting Systems**:
- **AN/SPY-1** (USA) - Aegis phased array radar
- **AN/SPY-3** (USA) - X-band multifunction radar (DDG-1000)
- **AN/SPY-6** (USA) - Next-gen air and missile defense radar
- **AN/SPG-62** (USA) - Standard missile illuminator
- **Type 346** (China) - AESA phased array (Type 052D)
- **Sampson** (UK) - Active electronically scanned array
- **EMPAR** (Italian) - European multifunction phased array
- **Fregat** (Russia) - 3D air search radar

---

## Missile Categories

### By Role
1. **SAM (Surface-to-Air Missile)**
   - Point Defense (0-10 NM): RAM, Sea Wolf, ESSM
   - Medium Range (10-40 NM): Standard SM-1, Sea Dart, Aster 15
   - Long Range (40-100+ NM): Standard SM-2/6, Aster 30, S-300F
   - Ballistic Missile Defense: Standard SM-3, Aster 30 Block 2

2. **SSM (Surface-to-Surface Missile)**
   - Anti-Ship: Harpoon, Exocet, P-270 Moskit, YJ-83
   - Land-Attack Cruise: Tomahawk, Kalibr
   - Supersonic Anti-Ship: BrahMos, P-800 Oniks, YJ-12

3. **ASW (Anti-Submarine Warfare)**
   - Rocket-Delivered: ASROC, VL-ASROC, Ikara
   - Missile-Delivered: MILAS, Type 07

### By Speed
- **Subsonic** (Mach 0.7-0.9): Harpoon, Tomahawk, most cruise missiles
- **Transonic** (Mach 0.9-1.2): Some modern SSMs
- **Supersonic** (Mach 1.5-3.0): Standard SM-2/6, Moskit, BrahMos, YJ-12
- **Hypersonic** (Mach 5+): 3M22 Zircon, future systems

### By Guidance
- **Command Guidance**: Beam-riding (early SAMs like Talos, Sea Slug)
- **Semi-Active Radar Homing (SARH)**: Standard SM-1, Sea Dart, Sparrow
- **Active Radar Homing (ARH)**: Standard SM-2 terminal, ESSM, Harpoon
- **Infrared (IR)**: RAM, Stinger, some ASMs
- **Inertial + GPS**: Tomahawk, Kalibr land-attack
- **Datalink + Terminal Homing**: Most modern SAMs/SSMs

---

## Future Expansion Notes

### Priority Historical Missiles (1950s-1960s)
- Terrier, Talos, Tartar (USA "3T" family)
- Regulus I/II (USA cruise missiles)
- Sea Slug, Sea Cat (UK early SAMs)
- P-15 Styx (Soviet first-generation anti-ship)

### Priority Modern Missiles (1970s-2000s)
- Standard Missile family (SM-1/2/3/6)
- Harpoon, Tomahawk (USA standard weapons)
- Exocet family (French anti-ship)
- P-270, P-700, P-800 (Soviet/Russian supersonic)
- Sea Dart, Sea Wolf (UK)

### Priority Current-Generation (2000s+)
- ESSM, RAM (US point defense)
- Standard SM-3, SM-6 (ballistic missile defense)
- LRASM (stealthy anti-ship)
- Kalibr, Zircon (Russian modern)
- BrahMos (Indo-Russian supersonic)
- YJ-18, YJ-12 (Chinese modern)

---

## Database Status

**Current Status**: Empty - Ready for population
**Target Count**: 400-600 missiles across all nations
**Priority**: Cold War to modern era (1950-2025)

**Major Producers**:
1. USA: Largest variety, Aegis system integration
2. Soviet/Russia: Focus on supersonic, heavy warheads
3. France: Exocet family, export success
4. China: Rapid modernization, indigenous designs
5. Israel: Gabriel series, advanced seekers
6. UK: Sea systems, NATO integration

---

**Last Updated**: October 10, 2025
**Ready for Data Entry**: ✅
