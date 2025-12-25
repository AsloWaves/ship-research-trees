# Electronic Warfare Modules

Electronic Warfare (EW) systems provide detection of enemy emissions, active countermeasures, and protection against radar-guided threats. These modules are essential for modern naval combat, providing layered defense against anti-ship missiles and enabling effective operation in hostile electromagnetic environments.

## Module Categories

### Radar Warning Receivers (RWR)
Detection systems that alert when enemy radar illuminates your ship:
- **RWR-Basic.md** (EW-001): Basic radar warning, bearing and threat type, 1942+
- **RWR-Advanced.md** (EW-002): Advanced identification with threat library, 1960+
- **Radar-Warning-Receiver.md** (SUP-018): Legacy integrated RWR system

### Electronic Support Measures (ESM)
Passive detection and analysis of enemy emissions:
- **ESM-Suite.md**: Passive electronic intelligence gathering

### Active Jamming Systems
Electronic countermeasures that degrade enemy radar effectiveness:
- **Jammer-Noise.md** (EW-003): Noise jamming to mask ship, 1943+
- **Jammer-Deceptive.md** (EW-004): DRFM-based false targets, 1960+
- **Radar-Jammer.md**: Legacy jammer system

### Expendable Countermeasures
Chaff and flare systems for missile defense:
- **Chaff-Launcher.md** (EW-005/EWR-002): Rapid-blooming chaff for missile seduction, 1943+

### Integrated Systems
Comprehensive EW suites combining multiple capabilities:
- **ECM-Suite.md** (EW-006/EWR-004): Fully integrated detection, jamming, and control, 1970+

### Signals Intelligence (SIGINT)
Passive radio intercept and cryptanalysis systems:
- **Radio-Intercept-Basic.md** (EW-007): Basic TBS voice intercept, 30km range, 1940-1970
- **Radio-Intercept-Standard.md** (EW-008): HF/VHF fleet radio intercept + direction finding, 75km, 1942-1980
- **SIGINT-Suite.md** (EW-009): Full-spectrum intercept, data link detection, traffic analysis, 150km, 1960+
- **Decryption-Module.md** (EW-010): Cryptanalysis computer for breaking enemy codes, requires EW-008/009, 1965+

## Technology Evolution

### WWII Era (1942-1945)
- Basic radar warning receivers
- Simple noise jammers
- Chaff (Window/Düppel) introduction
- Manual operation, limited effectiveness
- **Basic radio intercept** (TBS voice monitoring)
- Traffic analysis reveals enemy activity patterns

### Early Cold War (1950-1970)
- Improved RWR with better classification
- More powerful jammers
- Automated chaff launchers
- Beginning of integrated systems
- **Standard radio intercept** (HF/VHF fleet radio)
- Direction finding enables triangulation
- Cryptanalysis of tactical codes

### Modern Era (1970-Present)
- Advanced threat libraries (1000+ emitters)
- DRFM-based deceptive jamming
- Fully automated ECM suites
- AI-assisted threat prioritization
- Network-centric EW coordination
- **Full-spectrum SIGINT** (all radio + data link detection)
- Advanced decryption capabilities
- Automated traffic analysis and pattern recognition

## Tactical Considerations

### Detection vs. Stealth
- RWR provides warning but is passive (no emissions)
- Active jamming reveals your position
- Balance between protection and stealth
- EMCON discipline critical

### Layered Defense
1. **ESM**: Long-range passive detection (300+ km)
2. **RWR**: Immediate threat warning (<1 second)
3. **Jamming**: Degrade enemy radar tracking
4. **Chaff**: Seduce missile seekers
5. **Hard Kill**: CIWS/SAM as last resort

### Power Management
EW systems are power-hungry:
- ECM Suite: 150 kW
- Deceptive Jammer: 75 kW
- Noise Jammer: 50 kW
- Plan electrical load carefully

### Ammunition Discipline
- Chaff is expendable (48 rounds typical)
- Use judiciously - you can run out
- Automatic modes may waste ammunition
- Manual control for conservation

## Integration with Combat Systems

Modern EW systems integrate with:
- **Combat Information Center**: Centralized threat display
- **Weapons Systems**: Cue hard-kill defenses
- **Navigation**: Automated evasive maneuvers
- **Communications**: Network threat sharing
- **Damage Control**: Coordinate with ship systems

## Historical Examples

### WWII
- German Metox RWR on U-boats
- Allied Window chaff over Germany
- Japanese lack of effective EW (disadvantage)

### Falklands War (1982)
- HMS Ambuscade seduced Exocet with chaff
- British ECM suites provided critical protection
- Stark reminder of EW importance

### Modern Conflicts
- Gulf War ECM effectiveness against Iraqi radars
- USS Cole could have benefited from better EW posture
- Continuous EW/ECCM arms race

## Design Philosophy

**Progressive Capability**: Players should start with basic systems (RWR, simple chaff) and progress to integrated suites as technology and resources allow.

**Player Agency**: Balance automation (fast response) with manual control (tactical flexibility and ammunition conservation).

**Cost vs. Benefit**: Advanced systems are expensive and power-hungry but dramatically improve survivability against modern threats.

**Historical Authenticity**: Systems should reflect actual capabilities and limitations of their era.

## Module Selection Guide

### Early Ships (Pre-1940)
- No EW systems available
- Rely on visual detection and evasion

### WWII Era (1942-1950)
- Basic RWR essential for radar threats
- Chaff launchers for missile defense (late-war)
- Simple noise jammers if available
- **Radio Intercept Basic (EW-007)**: Monitor enemy TBS voice
- Traffic analysis reveals enemy activity

### Cold War (1950-1970)
- Advanced RWR for threat identification
- Noise and deceptive jammers
- Automated chaff launchers
- Begin integrating systems
- **Radio Intercept Standard (EW-008)**: HF/VHF intercept + DF
- **Decryption Module (EW-010)**: Break enemy tactical codes

### Modern Era (1970+)
- Integrated ECM Suite recommended
- Full-spectrum protection
- Automated response critical
- Network with task force
- **SIGINT Suite (EW-009)**: Full-spectrum intercept
- Detect Data Link usage (know enemy has coordinated sensors)

## SIGINT Limitations

**What SIGINT Systems CANNOT Intercept:**
- Visual signals (signal lamps, flags, semaphore)
- Laser communication (future systems)
- Physical messages (courier)
- Actions (enemy maneuvers)

**Counter-SIGINT for Enemies:**
Ships being monitored by SIGINT can:
- Maintain radio silence
- Use signal lamps for secure coordination
- Use pre-arranged code words
- Switch to burst transmissions
- Employ frequency hopping (modern era)
- Use one-time pad encryption (unbreakable)

## Future Additions

Potential future EW modules:
- Infrared countermeasures (flares, DIRCM)
- Communications jamming
- GPS/navigation jamming
- Cyber warfare capabilities
- AI-driven adaptive EW
- Directed energy weapons (lasers)

---

**Note**: Some modules exist in multiple versions (legacy vs. new). The numbered EW-### modules represent the latest standardized versions with consistent formatting and game balance.
