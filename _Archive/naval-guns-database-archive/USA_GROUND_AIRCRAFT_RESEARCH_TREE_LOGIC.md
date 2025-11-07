# USA Ground Aircraft Research Tree Logic

**Tech Branch**: Ground Aircraft
**Nation**: USA
**Era**: 1940-2025
**Node Count**: ~180 nodes

## Categories
1. **Fighters**: 50 nodes
2. **Bombers**: 35 nodes
3. **Attack/Strike**: 30 nodes
4. **Transport**: 20 nodes
5. **Reconnaissance**: 15 nodes
6. **Helicopters**: 25 nodes
7. **UAVs**: 5 nodes

## Research Tree Structure (Condensed)

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 4000 | USA | P-38 Lightning | Fighter | 1941 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4001 | 0 |
| 4001 | USA | P-38J Lightning | Fighter | 1943 | Ground Aircraft | Aircraft | 2500 | 60 | 15 | 25 | 0 | 4000 | 4002 | 0 |
| 4002 | USA | P-47 Thunderbolt | Fighter | 1942 | Ground Aircraft | Aircraft | 2800 | 65 | 18 | 28 | 0 | 4001 | 4003 | 0 |
| 4003 | USA | P-47D Thunderbolt | Fighter | 1944 | Ground Aircraft | Aircraft | 3200 | 75 | 20 | 32 | 0 | 4002 | 4004 | 0 |
| 4004 | USA | P-51 Mustang | Fighter | 1943 | Ground Aircraft | Aircraft | 3500 | 80 | 22 | 35 | 0 | 4003 | 4010 | 0 |
| 4010 | USA | P-80 Shooting Star | Jet Fighter | 1945 | Ground Aircraft | Aircraft | 4500 | 105 | 28 | 48 | 0 | 4004 | 4011 | 0 |
| 4011 | USA | F-84 Thunderjet | Jet Fighter | 1947 | Ground Aircraft | Aircraft | 5000 | 115 | 30 | 52 | 0 | 4010 | 4012 | 0 |
| 4012 | USA | F-86 Sabre | Jet Fighter | 1949 | Ground Aircraft | Aircraft | 5500 | 125 | 32 | 58 | 0 | 4011 | 4013 | 0 |
| 4013 | USA | F-100 Super Sabre | Jet Fighter | 1954 | Ground Aircraft | Aircraft | 6500 | 150 | 38 | 68 | 0 | 4012 | 4014,4020 | 0 |
| 4014 | USA | F-104 Starfighter | Interceptor | 1958 | Ground Aircraft | Aircraft | 7000 | 165 | 40 | 75 | 0 | 4013 | 4015 | 0 |
| 4015 | USA | F-105 Thunderchief | Strike | 1958 | Ground Aircraft | Aircraft | 7500 | 175 | 42 | 82 | 0 | 4014 | 4016 | 0 |
| 4016 | USA | F-111 Aardvark | Strike | 1967 | Ground Aircraft | Aircraft | 10000 | 235 | 52 | 115 | 0 | 4015 | 4030 | 0 |
| 4020 | USA | F-4C Phantom II | Multi-Role | 1963 | Ground Aircraft | Aircraft | 9000 | 210 | 48 | 98 | 0 | 4013 | 4021 | 0 |
| 4021 | USA | F-4E Phantom II | Multi-Role | 1967 | Ground Aircraft | Aircraft | 9500 | 220 | 50 | 105 | 0 | 4020 | 4022,4030 | 0 |
| 4022 | USA | F-5 Freedom Fighter | Export Fighter | 1963 | Ground Aircraft | Aircraft | 4500 | 105 | 25 | 55 | 0 | 4020 | 4023 | 0 |
| 4023 | USA | F-5E Tiger II | Export Fighter | 1972 | Ground Aircraft | Aircraft | 5000 | 115 | 28 | 62 | 0 | 4022 | 4040 | 0 |
| 4030 | USA | F-15A Eagle | Air Superiority | 1976 | Ground Aircraft | Aircraft | 12000 | 280 | 55 | 135 | 0 | 4021,4016 | 4031 | 0 |
| 4031 | USA | F-15C Eagle | Air Superiority | 1979 | Ground Aircraft | Aircraft | 13000 | 300 | 58 | 145 | 0 | 4030 | 4032 | 0 |
| 4032 | USA | F-15E Strike Eagle | Multi-Role | 1988 | Ground Aircraft | Aircraft | 14000 | 320 | 60 | 155 | 0 | 4031 | 4033 | 0 |
| 4033 | USA | F-15EX Eagle II | Multi-Role | 2021 | Ground Aircraft | Aircraft | 16000 | 375 | 65 | 180 | 0 | 4032 | 4050 | 0 |
| 4040 | USA | F-16A Fighting Falcon | Multi-Role | 1978 | Ground Aircraft | Aircraft | 9000 | 210 | 42 | 108 | 0 | 4023,4030 | 4041 | 0 |
| 4041 | USA | F-16C Block 30 | Multi-Role | 1984 | Ground Aircraft | Aircraft | 10000 | 235 | 45 | 120 | 0 | 4040 | 4042 | 0 |
| 4042 | USA | F-16C Block 52 | Multi-Role | 1991 | Ground Aircraft | Aircraft | 11000 | 260 | 48 | 132 | 0 | 4041 | 4043 | 0 |
| 4043 | USA | F-16V Viper | Multi-Role | 2015 | Ground Aircraft | Aircraft | 12500 | 290 | 52 | 152 | 0 | 4042 | 4050 | 0 |
| 4050 | USA | F-22A Raptor | Stealth Fighter | 2005 | Ground Aircraft | Aircraft | 20000 | 470 | 72 | 225 | 0 | 4033,4043 | 4051 | 0 |
| 4051 | USA | F-35A Lightning II | Stealth Multi-Role | 2016 | Ground Aircraft | Aircraft | 22000 | 510 | 75 | 245 | 0 | 4050 | | 0 |
| 4060 | USA | B-17 Flying Fortress | Heavy Bomber | 1941 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4061 | 0 |
| 4061 | USA | B-17G Flying Fortress | Heavy Bomber | 1943 | Ground Aircraft | Aircraft | 3500 | 80 | 22 | 35 | 0 | 4060 | 4062 | 0 |
| 4062 | USA | B-24 Liberator | Heavy Bomber | 1941 | Ground Aircraft | Aircraft | 3500 | 80 | 22 | 35 | 0 | 4061 | 4063 | 0 |
| 4063 | USA | B-29 Superfortress | Heavy Bomber | 1944 | Ground Aircraft | Aircraft | 5000 | 115 | 32 | 55 | 0 | 4062 | 4070 | 0 |
| 4070 | USA | B-36 Peacemaker | Strategic Bomber | 1949 | Ground Aircraft | Aircraft | 8000 | 185 | 48 | 92 | 0 | 4063 | 4071 | 0 |
| 4071 | USA | B-47 Stratojet | Strategic Bomber | 1951 | Ground Aircraft | Aircraft | 7500 | 175 | 45 | 88 | 0 | 4070 | 4072 | 0 |
| 4072 | USA | B-52 Stratofortress | Strategic Bomber | 1955 | Ground Aircraft | Aircraft | 10000 | 235 | 55 | 115 | 0 | 4071 | 4073 | 0 |
| 4073 | USA | B-52H Stratofortress | Strategic Bomber | 1961 | Ground Aircraft | Aircraft | 11000 | 260 | 58 | 125 | 0 | 4072 | 4080 | 0 |
| 4074 | USA | B-58 Hustler | Supersonic Bomber | 1960 | Ground Aircraft | Aircraft | 9000 | 210 | 50 | 105 | 0 | 4072 | 4075 | 0 |
| 4075 | USA | FB-111A | Strategic Bomber | 1969 | Ground Aircraft | Aircraft | 10500 | 245 | 52 | 118 | 0 | 4074,4016 | 4080 | 0 |
| 4080 | USA | B-1B Lancer | Strategic Bomber | 1986 | Ground Aircraft | Aircraft | 15000 | 350 | 65 | 165 | 0 | 4073,4075 | 4081 | 0 |
| 4081 | USA | B-2A Spirit | Stealth Bomber | 1997 | Ground Aircraft | Aircraft | 25000 | 580 | 85 | 280 | 0 | 4080 | 4082 | 0 |
| 4082 | USA | B-21 Raider | Stealth Bomber | 2025 | Ground Aircraft | Aircraft | 28000 | 650 | 90 | 310 | 0 | 4081 | | 0 |
| 4090 | USA | A-10A Thunderbolt II | Close Air Support | 1977 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4091 | 0 |
| 4091 | USA | A-10C Thunderbolt II | Close Air Support | 2007 | Ground Aircraft | Aircraft | 8000 | 185 | 42 | 108 | 0 | 4090 | | 0 |
| 4092 | USA | AC-130H Spectre | Gunship | 1972 | Ground Aircraft | Aircraft | 7500 | 175 | 42 | 98 | 0 | 4090 | 4093 | 0 |
| 4093 | USA | AC-130U Spooky | Gunship | 1995 | Ground Aircraft | Aircraft | 9000 | 210 | 48 | 122 | 0 | 4092 | 4094 | 0 |
| 4094 | USA | AC-130J Ghostrider | Gunship | 2015 | Ground Aircraft | Aircraft | 11000 | 260 | 52 | 145 | 0 | 4093 | | 0 |
| 4100 | USA | C-47 Skytrain | Transport | 1941 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4101 | 0 |
| 4101 | USA | C-54 Skymaster | Transport | 1942 | Ground Aircraft | Aircraft | 2500 | 60 | 18 | 28 | 0 | 4100 | 4102 | 0 |
| 4102 | USA | C-119 Flying Boxcar | Transport | 1950 | Ground Aircraft | Aircraft | 3500 | 80 | 22 | 42 | 0 | 4101 | 4103 | 0 |
| 4103 | USA | C-130A Hercules | Transport | 1956 | Ground Aircraft | Aircraft | 5000 | 115 | 32 | 62 | 0 | 4102 | 4104 | 0 |
| 4104 | USA | C-130H Hercules | Transport | 1974 | Ground Aircraft | Aircraft | 6000 | 140 | 38 | 78 | 0 | 4103 | 4105 | 0 |
| 4105 | USA | C-130J Super Hercules | Transport | 1999 | Ground Aircraft | Aircraft | 8000 | 185 | 45 | 108 | 0 | 4104 | 4110 | 0 |
| 4110 | USA | C-141 Starlifter | Strategic Transport | 1965 | Ground Aircraft | Aircraft | 8000 | 185 | 48 | 95 | 0 | 4104 | 4111 | 0 |
| 4111 | USA | C-5A Galaxy | Strategic Transport | 1970 | Ground Aircraft | Aircraft | 12000 | 280 | 62 | 135 | 0 | 4110 | 4112 | 0 |
| 4112 | USA | C-5M Super Galaxy | Strategic Transport | 2009 | Ground Aircraft | Aircraft | 14000 | 325 | 68 | 165 | 0 | 4111 | 4113 | 0 |
| 4113 | USA | C-17 Globemaster III | Strategic Transport | 1995 | Ground Aircraft | Aircraft | 13000 | 305 | 65 | 155 | 0 | 4111 | 4105 | 0 |
| 4120 | USA | UH-1 Iroquois | Utility Helo | 1959 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4121 | 0 |
| 4121 | USA | UH-1H Huey | Utility Helo | 1967 | Ground Aircraft | Aircraft | 3000 | 70 | 18 | 42 | 0 | 4120 | 4122,4130 | 0 |
| 4122 | USA | UH-60A Black Hawk | Utility Helo | 1979 | Ground Aircraft | Aircraft | 5000 | 115 | 28 | 68 | 0 | 4121 | 4123 | 0 |
| 4123 | USA | UH-60M Black Hawk | Utility Helo | 2006 | Ground Aircraft | Aircraft | 6500 | 150 | 32 | 88 | 0 | 4122 | | 0 |
| 4130 | USA | AH-1 Cobra | Attack Helo | 1967 | Ground Aircraft | Aircraft | 4000 | 90 | 22 | 52 | 0 | 4121 | 4131 | 0 |
| 4131 | USA | AH-64A Apache | Attack Helo | 1986 | Ground Aircraft | Aircraft | 8000 | 185 | 42 | 105 | 0 | 4130 | 4132 | 0 |
| 4132 | USA | AH-64D Longbow Apache | Attack Helo | 1997 | Ground Aircraft | Aircraft | 9500 | 220 | 48 | 128 | 0 | 4131 | 4133 | 0 |
| 4133 | USA | AH-64E Guardian | Attack Helo | 2011 | Ground Aircraft | Aircraft | 11000 | 260 | 52 | 145 | 0 | 4132 | | 0 |
| 4140 | USA | CH-47A Chinook | Heavy Transport Helo | 1962 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4141 | 0 |
| 4141 | USA | CH-47D Chinook | Heavy Transport Helo | 1982 | Ground Aircraft | Aircraft | 5500 | 125 | 32 | 72 | 0 | 4140 | 4142 | 0 |
| 4142 | USA | CH-47F Chinook | Heavy Transport Helo | 2007 | Ground Aircraft | Aircraft | 7000 | 165 | 38 | 95 | 0 | 4141 | | 0 |
| 4150 | USA | U-2A Dragon Lady | Reconnaissance | 1957 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4151 | 0 |
| 4151 | USA | U-2R Dragon Lady | Reconnaissance | 1967 | Ground Aircraft | Aircraft | 7000 | 165 | 38 | 88 | 0 | 4150 | 4152 | 0 |
| 4152 | USA | SR-71 Blackbird | Reconnaissance | 1966 | Ground Aircraft | Aircraft | 12000 | 280 | 58 | 145 | 0 | 4151 | 4153 | 0 |
| 4153 | USA | RQ-4 Global Hawk | UAV Recon | 2001 | Ground Aircraft | Aircraft | 10000 | 235 | 45 | 135 | 0 | 4152 | 4154 | 0 |
| 4154 | USA | MQ-9 Reaper | UAV Attack | 2007 | Ground Aircraft | Aircraft | 8000 | 185 | 38 | 108 | 0 | 4153 | 4155 | 0 |
| 4155 | USA | MQ-9B Sky Guardian | UAV Multi-Role | 2020 | Ground Aircraft | Aircraft | 9000 | 210 | 42 | 125 | 0 | 4154 | | 0 |
| 4160 | USA | KC-135 Stratotanker | Tanker | 1957 | Ground Aircraft | Aircraft | 6000 | 140 | 38 | 72 | 0 | 4072 | 4161 | 0 |
| 4161 | USA | KC-10 Extender | Tanker | 1981 | Ground Aircraft | Aircraft | 9000 | 210 | 52 | 118 | 0 | 4160 | 4162 | 0 |
| 4162 | USA | KC-46 Pegasus | Tanker | 2019 | Ground Aircraft | Aircraft | 11000 | 260 | 58 | 145 | 0 | 4161 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940s):
- P-38 Lightning (Node 4000): WWII fighter → jet age
- B-17 Flying Fortress (Node 4060): Heavy bomber → strategic bombers
- A-10 Thunderbolt II (Node 4090): Close air support lineage
- C-47 Skytrain (Node 4100): Transport → strategic airlift
- UH-1 Iroquois (Node 4120): Utility helicopter → attack/transport
- CH-47 Chinook (Node 4140): Heavy lift helicopter
- U-2 Dragon Lady (Node 4150): High-altitude reconnaissance

**Technology Convergence Points**:
- Node 4030 (F-15 Eagle): Unifies F-4 and F-111 lines into air superiority
- Node 4050 (F-22 Raptor): 5th generation stealth
- Node 4080 (B-1B Lancer): Modern strategic bomber
- Node 4105 (C-130J): Modern tactical transport

**High-Cost Nodes** (Research Cost >20000):
- F-22A Raptor (20000): 5th gen stealth fighter
- F-35A Lightning II (22000): 5th gen multi-role
- B-2A Spirit (25000): Stealth strategic bomber
- B-21 Raider (28000): Next-gen stealth bomber

**Tree Depth**: 14 generations (1941-2025)
