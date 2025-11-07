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
# Converting missile research nodes to detailed database entries
# Estimating specifications based on type, year, and country
| 2000 | USA | RIM-2 Terrier | SAM | 1956 | 13.5 | 15.0 | 8000 | 137 | 2.39 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2001 | USA | RIM-2C Terrier BT-3 | SAM | 1958 | 13.5 | 15.0 | 8000 | 137 | 2.41 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2002 | USA | RIM-2D Terrier HT-3 | SAM | 1961 | 13.5 | 15.0 | 8000 | 137 | 2.44 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2003 | USA | RIM-2E Terrier (Nuclear) | SAM | 1962 | 13.5 | 15.0 | 8000 | Nuclear | 2.45 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2004 | USA | RIM-2F Terrier Mod 7 | SAM | 1966 | 13.5 | 15.0 | 8000 | 137 | 2.49 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2005 | USA | RIM-67A Standard MR | SAM | 1967 | 13.5 | 21.5 | 8000 | 137 | 2.50 | 79.5 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2006 | USA | RIM-67B Standard ER Block I | SAM | 1974 | 13.5 | 21.5 | 8000 | 137 | 2.57 | 90.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2007 | USA | RIM-67C Standard ER Block II | SAM | 1981 | 13.5 | 21.5 | 8000 | 147.5 | 2.64 | 100.5 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2008 | USA | RIM-67D Standard ER Block IV | SAM | 1992 | 13.5 | 21.5 | 8000 | 164 | 2.75 | 117.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2009 | USA | RIM-156A SM-2ER Block IV | SAM | 2000 | 13.5 | 21.5 | 8000 | 176 | 2.50 | 129.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2010 | USA | RIM-8 Talos | SAM | 1959 | 30.0 | 21.0 | 8000 | 306 | 2.50 | 65.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2011 | USA | RIM-8A Talos Beam Rider | SAM | 1960 | 30.0 | 21.0 | 8000 | 308 | 2.50 | 66.0 | Beam-riding | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2012 | USA | RIM-8B Talos Semi-Active | SAM | 1963 | 30.0 | 21.0 | 8000 | 314 | 2.50 | 69.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2013 | USA | RIM-8D Talos ARM | SAM | 1968 | 30.0 | 21.0 | 8000 | 324 | 2.50 | 74.0 | Passive radar homing (anti-radiation) | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2014 | USA | RIM-8E Talos (Nuclear) | SAM | 1965 | 30.0 | 21.0 | 8000 | Nuclear | 2.50 | 71.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2015 | USA | RIM-24 Tartar | SAM | 1963 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2016 | USA | RIM-24A Tartar Beam Rider | SAM | 1964 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Beam-riding | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2017 | USA | RIM-24B Tartar Mod 0 | SAM | 1967 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2018 | USA | RIM-24C Tartar Mod 1 | SAM | 1970 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2019 | USA | RIM-66A Standard MR Block I | SAM | 1971 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2020 | USA | RIM-66B Standard MR Block II | SAM | 1978 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 45.6 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2021 | USA | RIM-66C Standard MR Block III | SAM | 1983 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 49.6 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2022 | USA | RIM-66E SM-1MR Block VI | SAM | 1990 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 55.2 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2023 | USA | RIM-66M SM-1MR Block VIA | SAM | 1995 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 59.2 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2024 | USA | RIM-161A SM-3 Block IA | SAM | 2005 | 13.5 | 21.5 | 8000 | 0 | 8.00 | 300.0 | Inertial + kinetic kill vehicle | Three-stage solid fuel + KKV thrusters | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2025 | USA | RIM-174A Standard ERAM | SAM | 2008 | 13.5 | 21.5 | 8000 | 188 | 2.91 | 141.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2026 | USA | RIM-161B SM-3 Block IB | SAM | 2009 | 13.5 | 21.9 | 8000 | 0 | 8.40 | 340.0 | Inertial + kinetic kill vehicle | Three-stage solid fuel + KKV thrusters | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2027 | USA | RIM-174B Standard ERAM Block II | SAM | 2015 | 13.5 | 21.5 | 8000 | 198.5 | 2.98 | 151.5 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2028 | USA | RIM-161C SM-3 Block IIA | SAM | 2015 | 13.5 | 22.5 | 8000 | 0 | 9.00 | 400.0 | Inertial + kinetic kill vehicle | Three-stage solid fuel + KKV thrusters | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2029 | USA | RIM-174C Standard ERAM Block III | SAM | 2020 | 13.5 | 21.5 | 8000 | 206 | 3.03 | 159.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2030 | USA | RIM-161D SM-3 Block IIB | SAM | 2025 | 13.5 | 23.5 | 8000 | 0 | 10.00 | 500.0 | Inertial + kinetic kill vehicle | Three-stage solid fuel + KKV thrusters | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2031 | USA | RIM-7 Sea Sparrow | SAM | 1969 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 8.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2032 | USA | RIM-7E Sea Sparrow Mk 2 | SAM | 1976 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 10.1 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2033 | USA | RIM-7M Sea Sparrow Mk 5 | SAM | 1983 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 12.2 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2034 | USA | RIM-162A ESSM Block I | SAM | 2004 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 27.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2035 | USA | RIM-162B ESSM Block II | SAM | 2020 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 27.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2040 | USA | RGM-6 Regulus I | SSM | 1955 | 54.0 | 15.0 | 8000 | 3000 | 0.70 | 500.0 | Radio command guidance | Turbofan jet engine + booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2041 | USA | RGM-6D Regulus I (Nuclear) | SSM | 1956 | 54.0 | 33.0 | 8000 | Nuclear | 0.70 | 500.0 | Radio command guidance | Turbofan jet engine + booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2042 | USA | RGM-15 Regulus II | SSM | 1958 | 54.0 | 57.5 | 8000 | 3000 | 0.70 | 500.0 | Radio command guidance | Turbofan jet engine + booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2043 | USA | RGM-84A Harpoon Block 1A | SSM | 1977 | 13.5 | 12.5 | 7973 | 488 | 0.85 | 60.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2044 | USA | RGM-84C Harpoon Block 1B | SSM | 1982 | 13.5 | 12.6 | 8000 | 488 | 0.85 | 60.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2045 | USA | RGM-84D Harpoon Block 1C | SSM | 1984 | 13.5 | 12.6 | 8000 | 488 | 0.85 | 60.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2046 | USA | RGM-84F Harpoon Block II | SSM | 1998 | 13.5 | 12.8 | 8000 | 488 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2047 | USA | RGM-84L Harpoon Block II+ | SSM | 2008 | 13.5 | 13.0 | 8000 | 488 | 0.85 | 150.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2048 | USA | RGM-84N Harpoon Block II ER | SSM | 2016 | 13.5 | 13.1 | 8000 | 488 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2049 | USA | AGM-119 Penguin Mk 2 | SSM | 1989 | 11.0 | 9.8 | 4150 | 265 | 0.80 | 21.0 | Infrared homing | Solid-fuel rocket motor | Surface ships | Helicopters, patrol boats | 1 | 0 |
| 2050 | USA | AGM-119B Penguin Mk 3 | SSM | 1995 | 11.0 | 9.8 | 4150 | 265 | 0.80 | 21.0 | Infrared homing | Solid-fuel rocket motor | Surface ships | Helicopters, patrol boats | 1 | 0 |
| 2051 | USA | RGM-109A Tomahawk TLAM-A | SSM | 1983 | 20.4 | 18.3 | 8000 | 1000 | 0.70 | 675.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2052 | USA | RGM-109B Tomahawk TASM | SSM | 1987 | 20.4 | 18.4 | 8000 | 1000 | 0.70 | 775.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2053 | USA | RGM-109C Tomahawk TLAM-C | SSM | 1993 | 20.4 | 18.5 | 8000 | 1000 | 0.70 | 925.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2054 | USA | RGM-109E Tomahawk TLAM-E | SSM | 2004 | 20.4 | 18.7 | 8000 | 1000 | 0.70 | 1200.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2055 | USA | RGM-109H Tomahawk TLAM-N | SSM | 2007 | 20.4 | 18.8 | 8000 | 1000 | 0.70 | 1275.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2056 | USA | RGM-109J Tomahawk Block IV | SSM | 2010 | 20.4 | 18.8 | 8000 | 1000 | 0.70 | 1350.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2057 | USA | RGM-109K Tomahawk Block V | SSM | 2019 | 20.4 | 19.0 | 8000 | 1000 | 0.70 | 1550.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2058 | USA | RGM-109L Tomahawk Block VA | SSM | 2021 | 20.4 | 19.1 | 8000 | 1000 | 0.70 | 1550.0 | INS + GPS + TERCOM + DSMAC | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2059 | USA | AGM-158C LRASM | SSM | 2018 | 17.7 | 14.1 | 8000 | 1000 | 0.85 | 300.0 | Passive RF + active radar + infrared + data-link | Turbofan jet engine | Surface ships | Surface ships, VLS | 1 | 0 |
| 2060 | USA | AGM-158C-2 LRASM Block II | SSM | 2024 | 17.7 | 14.1 | 8000 | 1000 | 0.85 | 300.0 | Passive RF + active radar + infrared + data-link | Turbofan jet engine | Surface ships | Surface ships, VLS | 1 | 0 |
| 2061 | USA | RUR-4 Weapon Alpha | ASW | 1951 | 7.2 | 7.2 | 1306 | 96 | 1.00 | 0.4 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor | Submarines | Surface ships, VLS | 1 | 0 |
| 2062 | USA | RUR-5 ASROC | ASW | 1961 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 5.4 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2063 | USA | RUR-5A ASROC Mod 4 | ASW | 1971 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 5.9 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2064 | USA | RUR-5B ASROC (Nuclear) | ASW | 1962 | 12.8 | 14.8 | 8000 | Nuclear | 1.00 | 5.5 | Inertial + nuclear depth charge | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2065 | USA | RUM-139A VL-ASROC | ASW | 1993 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 7.0 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2066 | USA | RUM-139B VL-ASROC Block II | ASW | 2008 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 7.8 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2067 | USA | RUM-139C VL-ASROC Block III | ASW | 2020 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 8.4 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2068 | USA | UUM-44A SUBROC | ASW | 1965 | 21.0 | 20.5 | 8000 | Nuclear | 1.00 | 30.0 | Inertial + nuclear depth charge | Solid-fuel rocket motor + torpedo payload | Submarines | Submarines | 1 | 0 |
| 2069 | USA | UUM-44B SUBROC Mod 1 | ASW | 1972 | 21.0 | 20.5 | 8000 | Nuclear | 1.00 | 30.0 | Inertial + nuclear depth charge | Solid-fuel rocket motor + torpedo payload | Submarines | Submarines | 1 | 0 |
| 2070 | USA | UUM-125A Sea Lance | ASW | 1988 | 21.0 | 20.0 | 8000 | 96 | 1.00 | 30.0 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Submarines | 1 | 0 |
| 2071 | USA | RIM-116A RAM Block 0 | CIWS | 1992 | 5.0 | 9.2 | 804 | 25 | 2.00 | 5.0 | Passive RF + infrared homing | Solid-fuel rocket motor | Anti-ship missiles, aircraft | Surface ships, VLS | 1 | 0 |
| 2072 | USA | RIM-116B RAM Block 1 | CIWS | 2000 | 5.0 | 9.2 | 804 | 25 | 2.00 | 5.0 | Passive RF + infrared homing | Solid-fuel rocket motor | Anti-ship missiles, aircraft | Surface ships, VLS | 1 | 0 |
| 2073 | USA | RIM-116C RAM Block 2 | CIWS | 2015 | 5.0 | 9.2 | 804 | 25 | 2.00 | 5.0 | Passive RF + infrared homing | Solid-fuel rocket motor | Anti-ship missiles, aircraft | Surface ships, VLS | 1 | 0 |
| 2074 | USA | RIM-116D RAM Block 2A | CIWS | 2020 | 5.0 | 9.2 | 804 | 25 | 2.00 | 5.0 | Passive RF + infrared homing | Solid-fuel rocket motor | Anti-ship missiles, aircraft | Surface ships, VLS | 1 | 0 |
| 2075 | USA | Mk 108 Weapon Alfa Rocket | ASW | 1959 | 7.2 | 7.2 | 1306 | 96 | 1.00 | 0.4 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor | Submarines | Surface ships, VLS | 1 | 0 |
| 2076 | USA | Mk 112 ASROC Rocket | ASW | 1963 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 5.5 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor | Submarines | Surface ships, VLS | 1 | 0 |
| 2077 | USA | Mk 113 ASROC Rocket Mod 7 | ASW | 1968 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 5.8 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor | Submarines | Surface ships, VLS | 1 | 0 |
| 2078 | USA | RIM-7P Sea Sparrow CIWS | CIWS | 1980 | 8.0 | 12.0 | 2688 | 25 | 2.00 | 5.0 | Semi-active radar homing | Solid-fuel rocket motor | Anti-ship missiles, aircraft | Surface ships, VLS | 1 | 0 |
| 2079 | USA | SM-6 Block IA Dual I | SAM | 2013 | 13.5 | 21.5 | 8000 | 140 | 3.50 | 130.0 | Active radar homing + semi-active | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2080 | USA | SM-6 Block IB Dual II | SAM | 2017 | 13.5 | 21.5 | 8000 | 140 | 3.50 | 150.0 | Active radar homing + semi-active | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2090 | USA | BGM-109G GLCM (Nuclear) | Cruise | 1983 | 13.5 | 15.0 | 8000 | 500 | 0.70 | 675.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2091 | USA | AGM-86C CALCM | Cruise | 1996 | 20.4 | 20.8 | 8000 | 3000 | 0.70 | 1000.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2092 | USA | AGM-86D CALCM Block II | Cruise | 2002 | 20.4 | 20.8 | 8000 | 3000 | 0.70 | 1150.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2093 | USA | AGM-154A JSOW | Cruise | 1999 | 13.0 | 13.3 | 7866 | 500 | 0.70 | 1075.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2094 | USA | AGM-154C JSOW-C | Cruise | 2005 | 13.0 | 13.3 | 7866 | 500 | 0.70 | 1225.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2095 | USA | AGM-154E JSOW-E | Cruise | 2015 | 13.0 | 13.3 | 7866 | 500 | 0.70 | 1475.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2096 | USA | AGM-129A ACM | Cruise | 1990 | 20.4 | 20.8 | 8000 | Nuclear | 0.70 | 850.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2097 | USA | AGM-129B ACM (Stealth) | Cruise | 1993 | 20.4 | 20.8 | 8000 | Nuclear | 0.70 | 925.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2098 | USA | BGM-109A Gryphon | Cruise | 1984 | 20.4 | 15.0 | 8000 | 500 | 0.70 | 700.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2099 | USA | BGM-109B Gryphon Mod 1 | Cruise | 1987 | 20.4 | 15.0 | 8000 | 500 | 0.70 | 775.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2100 | USA | AGM-158A JASSM | Cruise | 2003 | 20.4 | 14.0 | 8000 | 1000 | 0.70 | 1175.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2101 | USA | AGM-158B JASSM-ER | Cruise | 2014 | 20.4 | 14.0 | 8000 | 1000 | 0.70 | 1450.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2102 | USA | Conventional Prompt Strike | Hypersonic | 2022 | 13.5 | 14.8 | 8000 | 200 | 2.00 | 50.0 | Active radar homing | Solid-fuel rocket motor | Various | Surface ships | 1 | 0 |
| 2103 | USA | CPS Block II | Hypersonic | 2025 | 13.5 | 14.8 | 8000 | 200 | 2.00 | 50.0 | Active radar homing | Solid-fuel rocket motor | Various | Surface ships | 1 | 0 |
| 2104 | USA | SSM-N-8A Regulus (Sub) | Cruise | 1954 | 54.0 | 15.0 | 8000 | 3000 | 0.70 | -50.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2105 | USA | SSM-N-8B Regulus (Improved) | Cruise | 1957 | 54.0 | 15.0 | 8000 | 3000 | 0.70 | 25.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2106 | USA | RIM-85A Talos ARM | SAM | 1969 | 30.0 | 21.0 | 8000 | 326 | 2.50 | 75.0 | Passive radar homing (anti-radiation) | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2107 | USA | AGM-78 Standard ARM | SAM | 1968 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2108 | USA | AGM-78D Standard ARM Mod 5 | SAM | 1975 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2109 | USA | RIM-8G Talos ARM Mk 5 | SAM | 1972 | 30.0 | 21.0 | 8000 | 332 | 2.50 | 78.0 | Passive radar homing (anti-radiation) | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2200 | British | Sea Slug Mk 1 | SAM | 1961 | 30.0 | 15.0 | 8000 | 310 | 2.50 | 18.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2201 | British | Sea Slug Mk 2 | SAM | 1967 | 30.0 | 15.0 | 8000 | 322 | 2.50 | 21.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2202 | British | Sea Slug Mk 3 (Nuclear) | SAM | 1970 | 30.0 | 15.0 | 8000 | Nuclear | 2.50 | 22.5 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2210 | British | Sea Dart GWS.30 | SAM | 1973 | 13.5 | 14.5 | 8000 | 65 | 3.00 | 30.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2211 | British | Sea Dart Mod 1 | SAM | 1978 | 13.5 | 14.5 | 8000 | 65 | 3.00 | 36.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2212 | British | Sea Dart Mod 2 | SAM | 1985 | 13.5 | 14.5 | 8000 | 65 | 3.00 | 44.4 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2213 | British | Sea Dart Mod 3 | SAM | 1995 | 13.5 | 14.5 | 8000 | 65 | 3.00 | 56.4 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2214 | British | Sea Viper Aster 15 | SAM | 2009 | 13.5 | 13.1 | 8000 | 33 | 4.50 | 60.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2215 | British | Sea Viper Aster 30 | SAM | 2011 | 13.5 | 15.6 | 8000 | 33 | 4.50 | 60.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2216 | British | Sea Viper Block 1NT | SAM | 2020 | 13.5 | 13.1 | 8000 | 33 | 4.50 | 60.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2220 | British | Sea Wolf GWS.25 | SAM | 1979 | 8.0 | 6.3 | 1411 | 33 | 2.50 | 3.2 | Active radar homing | Solid-fuel boost + sustain motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2221 | British | Sea Wolf GWS.26 VLS | SAM | 1990 | 8.0 | 6.3 | 1411 | 33 | 2.72 | 4.8 | Active radar homing | Solid-fuel boost + sustain motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2222 | British | Sea Wolf Mod 1 | SAM | 1995 | 8.0 | 6.3 | 1411 | 33 | 2.82 | 5.6 | Active radar homing | Solid-fuel boost + sustain motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2223 | British | CAMM (Sea Ceptor) | SAM | 2016 | 8.0 | 10.3 | 2307 | 33 | 3.24 | 13.5 | Active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2224 | British | CAMM-ER | SAM | 2021 | 8.0 | 14.1 | 3158 | 33 | 3.34 | 30.0 | Active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2230 | British | Bloodhound Mk I | SAM | 1958 | 8.0 | 24.9 | 5577 | 137 | 2.50 | 45.0 | Semi-active radar homing | Ramjet + boosters | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2231 | British | Bloodhound Mk II | SAM | 1964 | 8.0 | 24.9 | 5577 | 137 | 2.50 | 45.0 | Semi-active radar homing | Ramjet + boosters | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2232 | British | Bloodhound Mk III | SAM | 1972 | 8.0 | 24.9 | 5577 | 137 | 2.50 | 45.0 | Semi-active radar homing | Ramjet + boosters | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2240 | British | MM38 Exocet | SSM | 1975 | 13.5 | 15.0 | 8000 | 364 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2241 | British | MM40 Exocet Block 1 | SSM | 1981 | 13.5 | 15.0 | 8000 | 364 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2242 | British | MM40 Exocet Block 2 | SSM | 1992 | 13.5 | 15.0 | 8000 | 364 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2243 | British | MM40 Exocet Block 3 | SSM | 2008 | 13.5 | 15.0 | 8000 | 364 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2244 | British | MM40 Block 3C | SSM | 2015 | 13.5 | 15.0 | 8000 | 500 | 0.85 | 75.0 | Active radar homing | Turbojet + booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2245 | British | Sea Venom ANL | SSM | 2020 | 7.0 | 8.5 | 1457 | 66 | 0.80 | 11.0 | Semi-active laser homing | Solid-fuel rocket motor | Surface ships | Helicopters, patrol boats | 1 | 0 |
| 2246 | British | Sea Skua CL834 | SSM | 1982 | 11.0 | 8.9 | 3769 | 66 | 0.80 | 8.0 | Infrared homing | Solid-fuel rocket motor | Surface ships | Helicopters, patrol boats | 1 | 0 |
| 2247 | British | Sea Skua Mk 2 | SSM | 1990 | 11.0 | 8.9 | 3769 | 66 | 0.80 | 8.0 | Infrared homing | Solid-fuel rocket motor | Surface ships | Helicopters, patrol boats | 1 | 0 |
| 2248 | British | Martlet (Sea Venom Light) | SSM | 2021 | 7.0 | 5.2 | 891 | 6.6 | 0.80 | 4.0 | Semi-active laser homing | Solid-fuel rocket motor | Surface ships | Helicopters, patrol boats | 1 | 0 |
| 2249 | British | Storm Shadow | Cruise | 2002 | 20.4 | 16.8 | 8000 | 880 | 0.70 | 1150.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2250 | British | Storm Shadow Block II | Cruise | 2015 | 20.4 | 16.8 | 8000 | 880 | 0.70 | 1475.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2251 | British | Tomahawk Block IV (UK) | Cruise | 2008 | 20.4 | 18.8 | 8000 | 1000 | 0.70 | 1300.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2252 | British | Tomahawk Block V (UK) | Cruise | 2021 | 20.4 | 19.1 | 8000 | 1000 | 0.70 | 1550.0 | INS + GPS + TERCOM | Turbofan jet engine + booster | Land targets, surface ships | Surface ships, submarines, VLS | 1 | 0 |
| 2260 | British | Ikara GWS.40 | ASW | 1968 | 17.7 | 11.3 | 8000 | 96 | 1.00 | 10.8 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2261 | British | Ikara Mod 1 | ASW | 1973 | 17.7 | 11.3 | 8000 | 96 | 1.00 | 11.8 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2262 | British | Ikara Mod 2 | ASW | 1978 | 17.7 | 11.3 | 8000 | 96 | 1.00 | 12.8 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2263 | British | Stingray ASW Missile | ASW | 1989 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 10.0 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2264 | British | Sea Urchin ASW | ASW | 2005 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 10.0 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2265 | British | Sea Spear ASW | ASW | 2020 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 10.0 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2300 | German | RIM-24B Tartar (German) | SAM | 1969 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2301 | German | RIM-66A Standard MR (German) | SAM | 1975 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 43.2 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2302 | German | SM-1MR Block VI (German) | SAM | 1990 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 55.2 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2310 | German | RAM Block 0 (German) | SAM | 1992 | 5.0 | 9.2 | 804 | 25 | 2.00 | 5.4 | Passive RF + infrared homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2311 | German | RAM Block 1 | SAM | 2000 | 5.0 | 9.2 | 804 | 25 | 2.00 | 7.0 | Passive RF + infrared homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2312 | German | RAM Block 2 | SAM | 2015 | 5.0 | 9.2 | 804 | 25 | 2.00 | 10.0 | Passive RF + infrared homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2313 | German | RAM Block 2A | SAM | 2020 | 5.0 | 9.2 | 804 | 25 | 2.00 | 11.0 | Passive RF + infrared homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2314 | German | Sea Sparrow NATO | SAM | 1976 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 10.1 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2315 | German | ESSM Block I (German) | SAM | 2005 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 27.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2316 | German | ESSM Block II (German) | SAM | 2020 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 27.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2317 | German | IRIS-T SLM | SAM | 2014 | 6.0 | 9.7 | 1222 | 25 | 3.00 | 22.0 | Infrared imaging homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2318 | German | IRIS-T SLM Block II | SAM | 2022 | 6.0 | 9.7 | 1222 | 25 | 3.00 | 22.0 | Infrared imaging homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2340 | German | MM38 Exocet (German) | SSM | 1977 | 13.5 | 15.0 | 8000 | 364 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2341 | German | MM40 Exocet Block 2 | SSM | 1992 | 13.5 | 15.0 | 8000 | 364 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2342 | German | MM40 Block 3 (German) | SSM | 2010 | 13.5 | 15.0 | 8000 | 500 | 0.85 | 75.0 | Active radar homing | Turbojet + booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2343 | German | RGM-84 Harpoon (German) | SSM | 1985 | 13.5 | 12.6 | 8000 | 488 | 0.85 | 60.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2344 | German | Harpoon Block II (German) | SSM | 2000 | 13.5 | 12.8 | 8000 | 488 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2345 | German | NSM (German) | SSM | 2017 | 17.7 | 13.0 | 8000 | 276 | 0.95 | 100.0 | Inertial + GPS + imaging infrared + data-link | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2346 | German | NSM Block II | SSM | 2023 | 17.7 | 13.0 | 8000 | 276 | 0.95 | 100.0 | Inertial + GPS + imaging infrared + data-link | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2347 | German | Kormoran Mk 1 | SSM | 1977 | 11.0 | 14.6 | 6183 | 363 | 0.80 | 16.0 | Inertial + active radar homing | Solid-fuel rocket motor | Surface ships | Surface ships, VLS | 1 | 0 |
| 2348 | German | Kormoran Mk 2 | SSM | 1991 | 11.0 | 14.6 | 6183 | 363 | 0.80 | 16.0 | Inertial + active radar homing | Solid-fuel rocket motor | Surface ships | Surface ships, VLS | 1 | 0 |
| 2349 | German | IDAS (Sub-Launched) | SSM | 2008 | 11.0 | 15.0 | 6352 | 500 | 0.85 | 11.0 | Fiber-optic guidance | Solid-fuel rocket motor | Surface ships | Submarines | 1 | 0 |
| 2360 | German | VL-ASROC (German) | ASW | 1995 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 7.1 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2361 | German | VL-ASROC Block II (German) | ASW | 2010 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 7.9 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2362 | German | RUM-139C (NATO) | ASW | 2022 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 10.0 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2363 | German | Sea Urchin (License) | ASW | 2012 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 10.0 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2400 | Japanese | RIM-24 Tartar (JMSDF) | SAM | 1970 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 40.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2401 | Japanese | RIM-66A Standard MR (JMSDF) | SAM | 1978 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 45.6 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2402 | Japanese | SM-1MR Block VI (JMSDF) | SAM | 1990 | 13.5 | 14.8 | 8000 | 137 | 2.50 | 55.2 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2403 | Japanese | Type 03 Chū-SAM Kai | SAM | 2003 | 13.5 | 15.0 | 8000 | 150 | 3.00 | 27.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2404 | Japanese | Type 03 Mod 4 | SAM | 2010 | 13.5 | 15.3 | 8000 | 150 | 3.14 | 34.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2405 | Japanese | Type 03 Mod 5 (AESA) | SAM | 2017 | 13.5 | 15.7 | 8000 | 150 | 3.28 | 41.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2406 | Japanese | Type 03 Mod 6 | SAM | 2024 | 13.5 | 16.1 | 8000 | 150 | 3.42 | 48.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2410 | Japanese | Type 07 VLS SAM | SAM | 2007 | 13.5 | 16.0 | 8000 | 150 | 3.08 | 32.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2411 | Japanese | Type 07 Mod 2 | SAM | 2015 | 13.5 | 16.3 | 8000 | 150 | 3.24 | 44.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2412 | Japanese | Type 07 Mod 3 (AESA) | SAM | 2022 | 13.5 | 16.6 | 8000 | 150 | 3.38 | 54.5 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2420 | Japanese | RIM-7 Sea Sparrow (JMSDF) | SAM | 1981 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 11.6 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2421 | Japanese | RIM-7M Sea Sparrow (JMSDF) | SAM | 1988 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 13.7 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2422 | Japanese | ESSM Block I (JMSDF) | SAM | 2008 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 27.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2423 | Japanese | ESSM Block II (JMSDF) | SAM | 2021 | 8.0 | 12.0 | 2688 | 86 | 4.00 | 27.0 | Semi-active radar homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2424 | Japanese | Type 91 Kai-MANPAD (Naval) | SAM | 1995 | 6.0 | 14.8 | 1864 | 137 | 2.50 | 40.0 | Infrared imaging homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2425 | Japanese | Type 93 SAM (Naval Adaptation) | SAM | 2008 | 6.0 | 14.8 | 1864 | 137 | 2.50 | 40.0 | Infrared imaging homing | Solid-fuel rocket motor | Aircraft, cruise missiles, ballistic missiles | Surface ships, VLS | 1 | 0 |
| 2440 | Japanese | SSM-1 Type 88 | SSM | 1988 | 13.5 | 16.4 | 8000 | 330 | 0.85 | 100.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2441 | Japanese | SSM-1A Type 88 Mod 1 | SSM | 1993 | 13.5 | 16.4 | 8000 | 330 | 0.85 | 100.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2442 | Japanese | SSM-1B Type 90 | SSM | 1998 | 13.5 | 16.4 | 8000 | 330 | 0.85 | 100.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2443 | Japanese | Type 12 SSM Block 0 | SSM | 2012 | 13.5 | 18.0 | 8000 | 440 | 0.90 | 108.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2444 | Japanese | Type 12 SSM Block 1 | SSM | 2018 | 13.5 | 18.3 | 8000 | 440 | 0.96 | 400.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2445 | Japanese | Type 12 SSM Block 2 | SSM | 2023 | 13.5 | 18.6 | 8000 | 440 | 1.01 | 540.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2446 | Japanese | ASM-1C | SSM | 1987 | 13.5 | 13.1 | 8000 | 330 | 0.85 | 27.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Aircraft, helicopters | 1 | 0 |
| 2447 | Japanese | ASM-2 | SSM | 1995 | 13.5 | 13.1 | 8000 | 330 | 0.85 | 48.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Aircraft, helicopters | 1 | 0 |
| 2448 | Japanese | ASM-3 | SSM | 2016 | 13.5 | 19.7 | 8000 | 400 | 3.00 | 81.0 | Inertial + active radar homing + ramjet | Integral rocket ramjet + booster | Surface ships | Aircraft, helicopters | 1 | 0 |
| 2449 | Japanese | ASM-3A (Extended Range) | SSM | 2022 | 13.5 | 19.7 | 8000 | 400 | 3.00 | 81.0 | Inertial + active radar homing + ramjet | Integral rocket ramjet + booster | Surface ships | Aircraft, helicopters | 1 | 0 |
| 2450 | Japanese | RGM-84 Harpoon (JMSDF) | SSM | 1982 | 13.5 | 12.6 | 8000 | 488 | 0.85 | 60.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2451 | Japanese | Harpoon Block II (JMSDF) | SSM | 2005 | 13.5 | 12.9 | 8000 | 488 | 0.85 | 75.0 | Active radar homing + inertial | Turbojet + solid-fuel booster | Surface ships | Surface ships, VLS | 1 | 0 |
| 2460 | Japanese | RUR-5 ASROC (JMSDF) | ASW | 1977 | 12.8 | 14.8 | 8000 | 96 | 1.00 | 6.2 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2461 | Japanese | Type 07 VLA | ASW | 2007 | 12.8 | 16.3 | 8000 | 96 | 1.00 | 16.2 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2462 | Japanese | Type 07 VLA Mod 2 | ASW | 2018 | 12.8 | 16.5 | 8000 | 96 | 1.00 | 19.5 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
| 2463 | Japanese | Type 07 VLA Mod 3 | ASW | 2024 | 12.8 | 16.6 | 8000 | 96 | 1.00 | 21.3 | Inertial + acoustic homing torpedo | Solid-fuel rocket motor + torpedo payload | Submarines | Surface ships, VLS | 1 | 0 |
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
