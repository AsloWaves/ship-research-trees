# Naval Torpedoes Database

**Export Date**: October 10, 2025
**Database Version**: 1.0
**Total Records**: 0 (ready for expansion)

---

## Database Contents

- [Torpedoes Table](#torpedoes-table) - Naval torpedo systems
- [Torpedo Warheads Table](#torpedo-warheads-table) - Warhead specifications
- [Launch Systems Table](#launch-systems-table) - Torpedo tube and launcher configurations

---

<a name="torpedoes-table"></a>
## Torpedoes Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Torpedo_ID | INT | Primary key, unique identifier |
| Country | VARCHAR(50) | Nation of origin (USA, British, German, Japanese, etc.) |
| Designation | VARCHAR(100) | Official designation/mark (e.g., "Mark 48 Mod 7", "Type 93", "G7es") |
| Type | VARCHAR(50) | Torpedo type (Steam, Electric, Wakeless, Acoustic, Wire-guided, Homing) |
| Year_Introduced | INT | Year entered service |
| Diameter_IN | DECIMAL(5,2) | Diameter in inches |
| Length_FT | DECIMAL(6,2) | Total length in feet |
| Weight_LBS | DECIMAL(8,2) | Total weight in pounds |
| Warhead_LBS | DECIMAL(7,2) | Warhead weight in pounds |
| Warhead_Type | VARCHAR(50) | Explosive type (TNT, Torpex, HBX, etc.) |
| Max_Speed_KTS | DECIMAL(5,1) | Maximum speed in knots |
| Max_Range_YDS | INT | Maximum range in yards |
| Running_Depth_FT | VARCHAR(50) | Operating depth range (e.g., "10-40") |
| Propulsion | VARCHAR(100) | Propulsion system (steam turbine, electric motor, etc.) |
| Guidance | VARCHAR(100) | Guidance system (straight-running, acoustic, wire, active/passive sonar) |
| Launch_Platform | VARCHAR(200) | Compatible platforms (surface ships, submarines, aircraft) |
| Modded | TINYINT | 0 = historical, 1 = fictional/generated |
| Notes | TEXT | Additional information, ships used, performance notes |

**Total Entries**: 0 torpedoes
**Planned Coverage**: 1890-1990
**ID Allocation**:
- USA: 1000-1099
- British: 1100-1199
- German: 1200-1299
- Japanese: 1300-1399
- Soviet: 1400-1499
- French: 1500-1599
- Italian: 1600-1699

| Torpedo_ID | Country | Designation | Type | Year_Introduced | Diameter_IN | Length_FT | Weight_LBS | Warhead_LBS | Warhead_Type | Max_Speed_KTS | Max_Range_YDS | Running_Depth_FT | Propulsion | Guidance | Launch_Platform | Modded | Notes |
|------------|---------|-------------|------|-----------------|-------------|-----------|------------|-------------|--------------|---------------|---------------|------------------|------------|----------|-----------------|--------|-------|
| | | | | | | | | | | | | | | | | | |

**Example Entries** (for reference - not yet in database):

### USA Torpedoes
- **Mark 48 Mod 7** - Modern wire-guided acoustic homing torpedo, submarines
- **Mark 14** - WWII submarine torpedo (infamous for detonator problems)
- **Mark 15** - WWII surface ship torpedo
- **Mark 13** - WWII air-launched torpedo

### British Torpedoes
- **Mark VIII** - WWI/WWII submarine torpedo
- **Mark IX** - WWII surface ship torpedo
- **Mark XII** - Destroyer torpedo
- **Spearfish** - Modern wire-guided heavyweight

### German Torpedoes
- **G7a (TI)** - Steam torpedo, WWI/WWII
- **G7e (TII)** - Electric torpedo, wakeless
- **G7es (TIII)** - Pattern-running torpedo
- **Zaunkönig (T5)** - Acoustic homing torpedo

### Japanese Torpedoes
- **Type 93 "Long Lance"** - Oxygen-fueled, longest range torpedo of WWII
- **Type 95** - Submarine torpedo
- **Type 91** - Air-launched torpedo (Pearl Harbor)
- **Type 97** - Destroyer torpedo

---

<a name="torpedo-warheads-table"></a>
## Torpedo Warheads Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Warhead_ID | INT | Primary key |
| Torpedo_ID | INT | Foreign key to torpedoes table |
| Designation | VARCHAR(100) | Warhead designation |
| Explosive_Type | VARCHAR(50) | TNT, Torpex, HBX-3, Composition B, etc. |
| Weight_LBS | DECIMAL(7,2) | Total warhead weight |
| Explosive_Weight_LBS | DECIMAL(7,2) | Net explosive weight |
| TNT_Equivalent_LBS | DECIMAL(7,2) | TNT equivalent for comparison |
| Fuze_Type | VARCHAR(100) | Contact, magnetic, acoustic, proximity |
| Blast_Radius_FT | DECIMAL(6,1) | Effective blast radius |
| Armor_Penetration_IN | DECIMAL(5,1) | Armor penetration capability |
| Notes | TEXT | Additional information |

| Warhead_ID | Torpedo_ID | Designation | Explosive_Type | Weight_LBS | Explosive_Weight_LBS | TNT_Equivalent_LBS | Fuze_Type | Blast_Radius_FT | Armor_Penetration_IN | Notes |
|------------|------------|-------------|----------------|------------|----------------------|-------------------|-----------|-----------------|----------------------|-------|
| | | | | | | | | | | |

---

<a name="launch-systems-table"></a>
## Launch Systems Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Launcher_ID | INT | Primary key |
| Country | VARCHAR(50) | Nation |
| Designation | VARCHAR(100) | Launcher designation |
| Type | VARCHAR(50) | Fixed tubes, trainable tubes, drop chutes, aircraft rack |
| Torpedo_Diameter_IN | DECIMAL(5,2) | Compatible torpedo diameter |
| Tube_Count | INT | Number of tubes/rails in mount |
| Reload_Time_MIN | DECIMAL(5,1) | Reload time in minutes |
| Traverse_Range_DEG | INT | Traverse range (null for fixed/drop) |
| Platform_Type | VARCHAR(100) | Surface ship, submarine, aircraft |
| Year_Introduced | INT | Year entered service |
| Weight_TONS | DECIMAL(6,2) | System weight in tons |
| Modded | TINYINT | 0 = historical, 1 = fictional |
| Notes | TEXT | Ships/platforms used on |

| Launcher_ID | Country | Designation | Type | Torpedo_Diameter_IN | Tube_Count | Reload_Time_MIN | Traverse_Range_DEG | Platform_Type | Year_Introduced | Weight_TONS | Modded | Notes |
|-------------|---------|-------------|------|---------------------|------------|-----------------|-------------------|---------------|-----------------|-------------|--------|-------|
| | | | | | | | | | | | | |

---

## Future Expansion Notes

### Historical Priority Torpedoes
1. **USA**: Mark 48, Mark 46, Mark 14, Mark 15, Mark 13 (air), Mark 37
2. **British**: Mark VIII, Mark IX, Spearfish, Tigerfish, Stingray
3. **German**: G7a, G7e, T5 Zaunkönig, T11, G7es
4. **Japanese**: Type 93 Long Lance, Type 95, Type 91 (air), Type 89
5. **Soviet**: Type 53, Type 65, VA-111 Shkval, SET-65

### Torpedo Categories
- **Heavyweight** (21"-24"): Submarine-launched, long range, large warheads
- **Lightweight** (12"-18"): ASW, air-launched, shorter range
- **Midweight** (16"-19"): Versatile, surface/sub launch
- **Supercavitating** (Modern): Extremely high speed, rocket-propelled

### Propulsion Types
- **Steam**: Wet-heater, alcohol/oxygen (early WWI-WWII)
- **Electric**: Battery-powered, wakeless (WWII onward)
- **Oxygen**: Pure oxygen fuel (Japanese Type 93)
- **Thermal**: Otto fuel, monopropellant (modern)
- **Rocket**: Supercavitating torpedoes (Shkval)

### Guidance Systems
- **Straight-running**: Gyroscope, no homing
- **Pattern-running**: Circular/zigzag search patterns
- **Acoustic Passive**: Homes on target noise
- **Acoustic Active**: Active sonar pinging
- **Wire-guided**: Controlled from launch platform
- **Wake-homing**: Follows ship wake signature

---

## Database Status

**Current Status**: Empty - Ready for population
**Target Count**: 300-500 torpedoes across all nations
**Priority**: Historical WWII and modern systems

---

**Last Updated**: October 10, 2025
**Ready for Data Entry**: ✅
