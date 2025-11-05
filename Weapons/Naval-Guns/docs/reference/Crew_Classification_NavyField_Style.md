# WOS2.3 Crew Classification System - Navy Field Style

## 📋 System Architecture

**Design Philosophy**: Linear tier progression for role-specific sailors, matching Navy Field's proven crew system.

**Core Principles**:
- **Linear Progression**: Each sailor type advances through 5 tiers (no branching)
- **Role Specificity**: Distinct sailor types for different weapons/systems
- **Level Gates**: Higher tiers unlock at specific crew card levels
- **Passive Bonuses**: All benefits are passive stat improvements (no activated abilities)
- **Universal Compatibility**: Crew cards transfer freely between ships, no retraining

---

## 🎯 Tier Progression Framework

### **Universal Tier Structure**

All sailor types follow this progression:

| Tier | Name Pattern | Level Req | Cost | Cumulative Cost | Performance Bonus |
|------|-------------|-----------|------|-----------------|-------------------|
| **Tier 1** | [Role] | Level 1 | 500₡ | 500₡ | Baseline (100%) |
| **Tier 2** | Veteran [Role] | Level 30 | 50,000₡ | 50,500₡ | +15% performance |
| **Tier 3** | Expert [Role] | Level 70 | 250,000₡ | 300,500₡ | +35% performance |
| **Tier 4** | Master [Role] | Level 120 | 1,000,000₡ | 1,300,500₡ | +60% performance |
| **Tier 5** | Supreme [Role] | Level 180 | 3,500,000₡ | 4,800,500₡ | +100% performance |

**Design Rationale**:
- Tier 2: Accessible mid-game upgrade (~50 hours investment)
- Tier 3: Serious commitment (~150 hours, competitive tier)
- Tier 4: Elite tier player investment (~300 hours)
- Tier 5: Endgame mastery (~500+ hours, server elite)

---

## 🔫 GUNNERY DIVISION

### **1. Light Gunner** (4"-5" Guns - Destroyers, Light Cruisers)

**Role**: Operates rapid-fire light naval guns (4"-5" caliber)

| Tier | Name | Level | Cost | Accuracy | Reload Speed | Range |
|------|------|-------|------|----------|--------------|-------|
| 1 | Light Gunner | 1 | 500₡ | Base | Base | Base |
| 2 | Veteran Light Gunner | 30 | 50,000₡ | +8% | +10% | +5% |
| 3 | Expert Light Gunner | 70 | 250,000₡ | +18% | +22% | +10% |
| 4 | Master Light Gunner | 120 | 1,000,000₡ | +32% | +40% | +18% |
| 5 | Supreme Light Gunner | 180 | 3,500,000₡ | +50% | +65% | +28% |

**Placement**: Destroyer main batteries, cruiser secondary batteries
**Best For**: Fast-firing destroyers, sustained DPS builds

---

### **2. Medium Gunner** (6"-8" Guns - Cruisers)

**Role**: Operates medium-caliber naval guns (6"-8" caliber)

| Tier | Name | Level | Cost | Accuracy | Reload Speed | Penetration |
|------|------|-------|------|----------|--------------|-------------|
| 1 | Medium Gunner | 1 | 500₡ | Base | Base | Base |
| 2 | Veteran Medium Gunner | 30 | 50,000₡ | +10% | +8% | +12% |
| 3 | Expert Medium Gunner | 70 | 250,000₡ | +22% | +18% | +25% |
| 4 | Master Medium Gunner | 120 | 1,000,000₡ | +38% | +32% | +42% |
| 5 | Supreme Medium Gunner | 180 | 3,500,000₡ | +60% | +50% | +65% |

**Placement**: Cruiser main batteries (6"-8" guns)
**Best For**: Heavy cruisers, balanced combat platforms

---

### **3. Heavy Gunner** (10"-14" Guns - Battlecruisers, Battleships)

**Role**: Operates heavy-caliber naval guns (10"-14" caliber)

| Tier | Name | Level | Cost | Accuracy | Damage | Penetration | Reload |
|------|------|-------|------|----------|--------|-------------|--------|
| 1 | Heavy Gunner | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Heavy Gunner | 30 | 50,000₡ | +12% | +10% | +15% | +5% |
| 3 | Expert Heavy Gunner | 70 | 250,000₡ | +25% | +22% | +32% | +12% |
| 4 | Master Heavy Gunner | 120 | 1,000,000₡ | +42% | +38% | +55% | +22% |
| 5 | Supreme Heavy Gunner | 180 | 3,500,000₡ | +65% | +60% | +85% | +35% |

**Placement**: Battleship main batteries (12"-14" guns)
**Best For**: Standard battleships, heavy cruisers

---

### **4. Super Heavy Gunner** (16"-20" Guns - Super Battleships)

**Role**: Operates super-heavy naval guns (16"-20"+ caliber)

| Tier | Name | Level | Cost | Accuracy | Damage | Penetration | Citadel Dmg |
|------|------|-------|------|----------|--------|-------------|-------------|
| 1 | Super Heavy Gunner | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran SH Gunner | 30 | 50,000₡ | +15% | +12% | +18% | +10% |
| 3 | Expert SH Gunner | 70 | 250,000₡ | +32% | +25% | +38% | +22% |
| 4 | Master SH Gunner | 120 | 1,000,000₡ | +55% | +42% | +65% | +38% |
| 5 | Supreme SH Gunner | 180 | 3,500,000₡ | +85% | +65% | +100% | +60% |

**Placement**: Super battleship main batteries (16"-20" guns)
**Best For**: T7-T10 capital ships, devastating firepower
**Special Note**: Level 180 Supreme SH Gunner = 4.8M₡ investment, potentially lost to permadeath

---

## 🚀 TORPEDO DIVISION

### **5. Torpedo Man** (Standard Torpedoes - All Ships)

**Role**: Operates torpedo tubes, launches torpedoes

| Tier | Name | Level | Cost | Accuracy | Reload | Range | Speed |
|------|------|-------|------|----------|--------|-------|-------|
| 1 | Torpedo Man | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Torpedo Man | 30 | 50,000₡ | +8% | +12% | +10% | +8% |
| 3 | Expert Torpedo Man | 70 | 250,000₡ | +18% | +25% | +22% | +18% |
| 4 | Master Torpedo Man | 120 | 1,000,000₡ | +32% | +42% | +38% | +32% |
| 5 | Supreme Torpedo Man | 180 | 3,500,000₡ | +50% | +65% | +60% | +50% |

**Placement**: Destroyer torpedo tubes, submarine torpedo rooms
**Best For**: Torpedo-focused destroyers, submarine attacks

---

### **6. Heavy Torpedo Specialist** (Long Lance, Advanced Torpedoes)

**Role**: Operates advanced/heavy torpedo systems

| Tier | Name | Level | Cost | Accuracy | Damage | Range | Detection |
|------|------|-------|------|----------|--------|-------|-----------|
| 1 | Heavy Torpedo Spec | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran HT Spec | 30 | 50,000₡ | +12% | +15% | +18% | -8% |
| 3 | Expert HT Spec | 70 | 250,000₡ | +25% | +32% | +38% | -18% |
| 4 | Master HT Spec | 120 | 1,000,000₡ | +42% | +55% | +65% | -32% |
| 5 | Supreme HT Spec | 180 | 3,500,000₡ | +65% | +85% | +100% | -50% |

**Placement**: Japanese Long Lance torpedoes, advanced torpedo systems
**Best For**: Stealth torpedo attacks, maximum damage builds
**Special**: Detection reduction = harder for enemies to spot torpedoes

---

## 🎯 ANTI-AIRCRAFT DIVISION

### **7. AA Gunner** (Anti-Aircraft Weapons)

**Role**: Operates AA batteries, shoots down aircraft

| Tier | Name | Level | Cost | AA Damage | AA Range | Detection | Flak Density |
|------|------|-------|------|-----------|----------|-----------|--------------|
| 1 | AA Gunner | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran AA Gunner | 30 | 50,000₡ | +15% | +10% | +12% | +10% |
| 3 | Expert AA Gunner | 70 | 250,000₡ | +35% | +22% | +25% | +22% |
| 4 | Master AA Gunner | 120 | 1,000,000₡ | +60% | +38% | +42% | +38% |
| 5 | Supreme AA Gunner | 180 | 3,500,000₡ | +100% | +60% | +65% | +60% |

**Placement**: All AA battery positions
**Best For**: Carrier escorts, AA-focused cruisers
**Special**: Supreme AA Gunner can nearly double AA effectiveness

---

## ⚙️ ENGINEERING DIVISION

### **8. Engineer** (Engine Room, Propulsion Systems)

**Role**: Operates engines, manages power output

| Tier | Name | Level | Cost | Max Speed | Accel | Fuel Eff | Emergency Power |
|------|------|-------|------|-----------|-------|----------|-----------------|
| 1 | Engineer | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Engineer | 30 | 50,000₡ | +8% | +12% | +10% | +15% |
| 3 | Expert Engineer | 70 | 250,000₡ | +18% | +25% | +22% | +32% |
| 4 | Master Engineer | 120 | 1,000,000₡ | +32% | +42% | +38% | +55% |
| 5 | Supreme Engineer | 180 | 3,500,000₡ | +50% | +65% | +60% | +85% |

**Placement**: Engine room positions
**Best For**: All ship classes
**Special**: Emergency Power = speed boost capability duration/effectiveness

---

### **9. Damage Control Specialist** (Fire Fighting, Flooding Control)

**Role**: Manages damage control, fights fires/floods

| Tier | Name | Level | Cost | Fire Suppression | Flood Control | Repair Speed | Module Repair |
|------|------|-------|------|------------------|---------------|--------------|---------------|
| 1 | Damage Control | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran DC | 30 | 50,000₡ | +15% | +15% | +12% | +10% |
| 3 | Expert DC | 70 | 250,000₡ | +35% | +35% | +25% | +22% |
| 4 | Master DC | 120 | 1,000,000₡ | +60% | +60% | +42% | +38% |
| 5 | Supreme DC | 180 | 3,500,000₡ | +100% | +100% | +65% | +60% |

**Placement**: Damage control stations
**Best For**: Survivability-focused builds, solo operations
**Critical**: Supreme DC can extinguish fires/floods 2x faster = survival difference

---

### **10. Repairer** (Hull Repair, Structural Damage)

**Role**: Repairs hull damage during and after combat

| Tier | Name | Level | Cost | Repair Speed | HP Restored | Efficiency | Cost Reduction |
|------|------|-------|------|--------------|-------------|------------|----------------|
| 1 | Repairer | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Repairer | 30 | 50,000₡ | +12% | +10% | +15% | -8% |
| 3 | Expert Repairer | 70 | 250,000₡ | +25% | +22% | +32% | -18% |
| 4 | Master Repairer | 120 | 1,000,000₡ | +42% | +38% | +55% | -32% |
| 5 | Supreme Repairer | 180 | 3,500,000₡ | +65% | +60% | +85% | -50% |

**Placement**: Repair stations
**Best For**: Long operations, extended combat missions
**Economic**: Cost Reduction = lower repair bills at port

---

### **11. Restorer** (Repair Effectiveness Multiplier)

**Role**: Increases effectiveness of repairs performed by Repairers

| Tier | Name | Level | Cost | Repair Multiplier | Max HP Restore | Permanent Repair | Module Restoration |
|------|------|-------|------|-------------------|----------------|------------------|--------------------|
| 1 | Restorer | 1 | 500₡ | Base (1.0x) | Base (50%) | Base (70%) | Base |
| 2 | Veteran Restorer | 30 | 50,000₡ | 1.15x | 60% | 75% | +10% |
| 3 | Expert Restorer | 70 | 250,000₡ | 1.35x | 72% | 82% | +22% |
| 4 | Master Restorer | 120 | 1,000,000₡ | 1.60x | 85% | 90% | +38% |
| 5 | Supreme Restorer | 180 | 3,500,000₡ | 2.00x | 100% | 100% | +60% |

**Placement**: Works with Repairer (synergy position)
**Best For**: Combined with Master/Supreme Repairer for maximum survivability
**Critical**: Supreme Restorer allows 100% HP restoration (normally capped at 50%)

---

### **12. Medic** (Crew Casualty Recovery)

**Role**: Reduces crew casualties, stabilizes wounded sailors

| Tier | Name | Level | Cost | Casualty Reduction | Sailor Recovery | Card Protection | Death Prevention |
|------|------|-------|------|-------------------|-----------------|-----------------|------------------|
| 1 | Medic | 1 | 500₡ | -5% | Base | Base | Base |
| 2 | Veteran Medic | 30 | 50,000₡ | -12% | +10% | +8% | +5% |
| 3 | Expert Medic | 70 | 250,000₡ | -22% | +22% | +18% | +12% |
| 4 | Master Medic | 120 | 1,000,000₡ | -35% | +38% | +32% | +22% |
| 5 | Supreme Medic | 180 | 3,500,000₡ | -50% | +60% | +50% | +35% |

**Placement**: Medical bay
**Best For**: High-tier permadeath zones (T8-T10)
**Critical**: Reduces crew card sailor casualties = less replenishment cost
**Special**: Death Prevention = slight chance to save crew card from permadeath (5-35%)

---

## ✈️ AVIATION DIVISION

### **13. Scout Pilot** (Reconnaissance Aircraft)

**Role**: Operates scout/reconnaissance aircraft

| Tier | Name | Level | Cost | Detection Range | Speed | Survivability | Intel Quality |
|------|------|-------|------|-----------------|-------|---------------|---------------|
| 1 | Scout Pilot | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Scout | 30 | 50,000₡ | +15% | +10% | +12% | +15% |
| 3 | Expert Scout | 70 | 250,000₡ | +35% | +22% | +25% | +32% |
| 4 | Master Scout | 120 | 1,000,000₡ | +60% | +38% | +42% | +55% |
| 5 | Supreme Scout | 180 | 3,500,000₡ | +100% | +60% | +65% | +85% |

**Placement**: Carrier scout squadrons
**Best For**: Fleet reconnaissance, target acquisition

---

### **14. Fighter Pilot** (Air Superiority Fighter Aircraft)

**Role**: Operates fighter aircraft, air-to-air combat

| Tier | Name | Level | Cost | A2A Damage | Dogfight | Survivability | Intercept Speed |
|------|------|-------|------|------------|----------|---------------|-----------------|
| 1 | Fighter Pilot | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Fighter | 30 | 50,000₡ | +12% | +15% | +10% | +12% |
| 3 | Expert Fighter | 70 | 250,000₡ | +25% | +32% | +22% | +25% |
| 4 | Master Fighter | 120 | 1,000,000₡ | +42% | +55% | +38% | +42% |
| 5 | Supreme Fighter | 180 | 3,500,000₡ | +65% | +85% | +60% | +65% |

**Placement**: Carrier fighter squadrons
**Best For**: Air superiority, bomber escort

---

### **15. Dive Bomber Pilot** (Dive Bombing Aircraft)

**Role**: Operates dive bombers, precision attacks

| Tier | Name | Level | Cost | Bomb Accuracy | Damage | Citadel Hit | Survivability |
|------|------|-------|------|---------------|--------|-------------|---------------|
| 1 | Dive Bomber Pilot | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran DB Pilot | 30 | 50,000₡ | +15% | +12% | +10% | +8% |
| 3 | Expert DB Pilot | 70 | 250,000₡ | +32% | +25% | +22% | +18% |
| 4 | Master DB Pilot | 120 | 1,000,000₡ | +55% | +42% | +38% | +32% |
| 5 | Supreme DB Pilot | 180 | 3,500,000₡ | +85% | +65% | +60% | +50% |

**Placement**: Carrier dive bomber squadrons
**Best For**: Precision strikes on capital ships

---

### **16. Torpedo Bomber Pilot** (Torpedo Bombing Aircraft)

**Role**: Operates torpedo bombers, anti-ship strikes

| Tier | Name | Level | Cost | Torpedo Acc | Damage | Flood Chance | Survivability |
|------|------|-------|------|-------------|--------|--------------|---------------|
| 1 | Torp Bomber Pilot | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran TB Pilot | 30 | 50,000₡ | +12% | +15% | +12% | +8% |
| 3 | Expert TB Pilot | 70 | 250,000₡ | +25% | +32% | +25% | +18% |
| 4 | Master TB Pilot | 120 | 1,000,000₡ | +42% | +55% | +42% | +32% |
| 5 | Supreme TB Pilot | 180 | 3,500,000₡ | +65% | +85% | +65% | +50% |

**Placement**: Carrier torpedo bomber squadrons
**Best For**: Devastating strikes, flooding damage

---

### **17. Seaman** (Deck Crew, Aircraft Handler)

**Role**: Supports aviation operations, faster launch/recovery

| Tier | Name | Level | Cost | Launch Speed | Recovery Speed | Repair Speed | Efficiency |
|------|------|-------|------|--------------|----------------|--------------|------------|
| 1 | Seaman | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Seaman | 30 | 50,000₡ | +15% | +15% | +12% | +10% |
| 3 | Expert Seaman | 70 | 250,000₡ | +32% | +32% | +25% | +22% |
| 4 | Master Seaman | 120 | 1,000,000₡ | +55% | +55% | +42% | +38% |
| 5 | Supreme Seaman | 180 | 3,500,000₡ | +85% | +85% | +65% | +60% |

**Placement**: Carrier deck operations
**Best For**: Carrier efficiency builds
**Critical**: Faster launch = more strikes per engagement

---

## 🔱 SUBMARINE DIVISION

### **18. Planesman** (Submarine Depth Control, Oxygen Management)

**Role**: Controls submarine depth, manages oxygen systems

| Tier | Name | Level | Cost | Dive Speed | Surface Speed | Oxygen Cap | O2 Efficiency |
|------|------|-------|------|-----------|---------------|------------|---------------|
| 1 | Planesman | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Planesman | 30 | 50,000₡ | +12% | +15% | +15% | +12% |
| 3 | Expert Planesman | 70 | 250,000₡ | +25% | +32% | +32% | +25% |
| 4 | Master Planesman | 120 | 1,000,000₡ | +42% | +55% | +55% | +42% |
| 5 | Supreme Planesman | 180 | 3,500,000₡ | +65% | +85% | +85% | +65% |

**Placement**: Submarine depth control station
**Best For**: All submarines
**Critical**: Oxygen capacity = longer submerged operations

---

### **19. Sonarman** (Submarine Detection, Underwater Awareness)

**Role**: Operates sonar, detects enemy submarines and ships

| Tier | Name | Level | Cost | Detection Range | Accuracy | Sub Detection | Stealth |
|------|------|-------|------|-----------------|----------|---------------|---------|
| 1 | Sonarman | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Sonarman | 30 | 50,000₡ | +18% | +12% | +20% | +10% |
| 3 | Expert Sonarman | 70 | 250,000₡ | +38% | +25% | +42% | +22% |
| 4 | Master Sonarman | 120 | 1,000,000₡ | +65% | +42% | +70% | +38% |
| 5 | Supreme Sonarman | 180 | 3,500,000₡ | +100% | +65% | +110% | +60% |

**Placement**: Submarine sonar station
**Best For**: Submarine warfare
**Critical**: Sub Detection = critical for hunting enemy subs

---

## 🎖️ COMMAND DIVISION

### **20. Bridge Officer** (Ship Command, Overall Coordination)

**Role**: Ship captain, overall coordination and command

| Tier | Name | Level | Cost | Ship Bonus | Crew Morale | Coordination | Response Time |
|------|------|-------|------|------------|-------------|--------------|---------------|
| 1 | Bridge Officer | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran BO | 30 | 50,000₡ | +5% | +8% | +10% | +8% |
| 3 | Expert BO | 70 | 250,000₡ | +12% | +18% | +22% | +18% |
| 4 | Master BO | 120 | 1,000,000₡ | +22% | +32% | +38% | +32% |
| 5 | Supreme BO | 180 | 3,500,000₡ | +35% | +50% | +60% | +50% |

**Placement**: Bridge command position
**Best For**: All ships (mandatory position)
**Special**: Ship Bonus applies small buff to ALL systems
**Note**: Supreme Bridge Officer = 35% ship-wide performance boost

---

### **21. Radio Officer** (Communications, Fleet Coordination)

**Role**: Manages communications, fleet coordination

| Tier | Name | Level | Cost | Comms Range | Intel Sharing | Fleet Bonus | Detection |
|------|------|-------|------|-------------|---------------|-------------|-----------|
| 1 | Radio Officer | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Radio | 30 | 50,000₡ | +12% | +15% | +8% | +10% |
| 3 | Expert Radio | 70 | 250,000₡ | +25% | +32% | +18% | +22% |
| 4 | Master Radio | 120 | 1,000,000₡ | +42% | +55% | +32% | +38% |
| 5 | Supreme Radio | 180 | 3,500,000₡ | +65% | +85% | +50% | +60% |

**Placement**: Radio room
**Best For**: Fleet operations, squadron play
**Special**: Fleet Bonus = buffs to nearby allied ships

---

### **22. Helmsman** (Ship Maneuvering, Evasion)

**Role**: Controls ship steering, evasive maneuvers

| Tier | Name | Level | Cost | Turn Rate | Evasion | Positioning | Stability |
|------|------|-------|------|-----------|---------|-------------|-----------|
| 1 | Helmsman | 1 | 500₡ | Base | Base | Base | Base |
| 2 | Veteran Helmsman | 30 | 50,000₡ | +10% | +12% | +12% | +8% |
| 3 | Expert Helmsman | 70 | 250,000₡ | +22% | +25% | +25% | +18% |
| 4 | Master Helmsman | 120 | 1,000,000₡ | +38% | +42% | +42% | +32% |
| 5 | Supreme Helmsman | 180 | 3,500,000₡ | +60% | +65% | +65% | +50% |

**Placement**: Helm station
**Best For**: All ships
**Critical**: Evasion = reduces incoming hit probability
**Special**: Supreme Helmsman can dodge shells much more effectively

---

## 📊 Economic Analysis

### **Single Crew Card - Full Progression**

| Tier | Level | Cost This Tier | Cumulative | Hours Investment |
|------|-------|---------------|------------|------------------|
| 1 | 1 | 500₡ | 500₡ | 0 hours (starting) |
| 2 | 30 | 50,000₡ | 50,500₡ | 60-80 hours |
| 3 | 70 | 250,000₡ | 300,500₡ | 150-180 hours |
| 4 | 120 | 1,000,000₡ | 1,300,500₡ | 280-320 hours |
| 5 | 180 | 3,500,000₡ | 4,800,500₡ | 500-600 hours |

---

### **Full Ship Crew - T8 Battleship Example**

**6 Crew Positions** (all Supreme Tier 5):

1. Supreme Super Heavy Gunner (Main Battery) - 4,800,500₡
2. Supreme Medium Gunner (Secondary Battery) - 4,800,500₡
3. Supreme AA Gunner (AA Batteries) - 4,800,500₡
4. Supreme Engineer (Engine Room) - 4,800,500₡
5. Supreme Damage Control (DC Station) - 4,800,500₡
6. Supreme Bridge Officer (Bridge) - 4,800,500₡

**Total Investment**: **28,803,000₡ + 3,000-3,600 hours**

**Risk**: T8 permadeath = 30% chance to lose entire crew investment

---

### **Realistic Progression - Balanced Player**

**T5 Cruiser** (competitive mid-tier):

1. Expert Medium Gunner (Main) - Level 70, 300,500₡
2. Veteran AA Gunner (AA) - Level 30, 50,500₡
3. Expert Engineer (Engine) - Level 70, 300,500₡
4. Veteran Damage Control (DC) - Level 30, 50,500₡
5. Veteran Bridge Officer (Bridge) - Level 30, 50,500₡

**Total**: **752,500₡ + ~400 hours**
**Result**: Competitive T5 platform without massive risk

---

## 🎯 Strategic Crew Building

### **Early Game Strategy** (T1-T3)

**Recommended**:
- 4-5 Tier 1 crew cards (2,000-2,500₡)
- Focus on leveling to 30 for Tier 2 upgrades
- Prioritize: 1 Gunner, 1 Engineer, 1 Damage Control, 1 Bridge Officer
- **Cost**: ~200,000₡ for Tier 2 upgrades (affordable from T2-T3 earnings)

---

### **Mid Game Strategy** (T4-T6)

**Recommended**:
- Progress primary crew to Tier 3 (Level 70)
- Focus on combat positions: Gunner, AA, Engineer
- **Investment**: 750,000-1,200,000₡
- **Result**: Competitive in T5-T6 zones

---

### **Late Game Strategy** (T7-T9)

**Recommended**:
- Select 2-3 critical positions for Tier 4 (Master)
- Main gunner, Engineer, Damage Control as priorities
- **Investment**: 3,000,000-6,000,000₡
- **Risk Management**: Consider backup Tier 3 crew for permadeath zones

---

### **Endgame Strategy** (T10)

**Elite Path**:
- Full Tier 5 crew = 28.8M₡ + 3,000+ hours
- **Risk**: T10 = 100% permadeath, total loss guaranteed on death
- Only for dedicated endgame players or cautious T9 operations

**Realistic Path**:
- Mix of Tier 4-5 crew for critical positions
- Tier 3 crew for less critical roles
- **Investment**: 15-20M₡
- **Risk**: More affordable losses

---

## 🎮 Crew Synergies

### **Survivability Build**

- Supreme Repairer (65% faster repairs)
- Supreme Restorer (2.0x repair effectiveness, 100% HP recovery)
- Supreme Damage Control (2x fire/flood suppression)
- Supreme Medic (-50% crew casualties)

**Result**: Nearly unkillable ship with elite damage control

---

### **Maximum Firepower Build**

- Supreme Super Heavy Gunner (85% more damage, 100% penetration)
- Supreme Bridge Officer (35% ship-wide bonus)
- Supreme Engineer (85% emergency power boost)
- Supreme Helmsman (65% better positioning)

**Result**: Devastating salvos with perfect positioning

---

### **Carrier Air Superiority Build**

- Supreme Fighter Pilot (85% dogfight bonus)
- Supreme Scout Pilot (100% detection range)
- Supreme Seaman (85% faster launch/recovery)
- Supreme AA Gunner (100% AA damage)

**Result**: Dominate airspace, rapid sortie cycling

---

## ✅ Design Validation

### **Navy Field Alignment**

✅ **Linear Tier Progression**: 5 tiers per sailor type, no branching
✅ **Role Specificity**: 22 distinct sailor types (vs. 7 broad classifications)
✅ **Level Gates**: Clear progression (30/70/120/180)
✅ **Passive Bonuses**: All stat-based, no activated abilities
✅ **Granular Support**: Repairer ≠ Restorer ≠ Medic (separate roles)
✅ **Aviation Division**: Scout, Fighter, Dive Bomber, Torpedo Bomber, Seamen
✅ **Submarine Specialists**: Planesman, Sonarman
✅ **Economic Progression**: Matches ship tier progression timelines

---

### **WOS2.3 Integration**

✅ **Permadeath Integration**: High-tier crew = high risk in T8-T10 zones
✅ **Economic Balance**: Tier upgrades aligned with mission earnings
✅ **Time Investment**: 500-600 hours for Supreme = matches T1-T10 ship progression
✅ **Universal Compatibility**: All crew transfers freely between ships
✅ **Strategic Depth**: 22 sailor types × 5 tiers = 110 total crew cards possible
✅ **Player Identity**: Crew composition defines playstyle (firepower vs survivability vs aviation)

---

## 📋 Summary

**Complete Navy Field-Style System**:
- ✅ 22 distinct sailor types across 7 divisions
- ✅ 5-tier linear progression (no branching)
- ✅ Level gates: 1/30/70/120/180
- ✅ Cost progression: 500₡ → 50K → 250K → 1M → 3.5M (4.8M total)
- ✅ Time investment: 500-600 hours per Supreme crew card
- ✅ Passive stat bonuses only (no activated abilities)
- ✅ Full economic integration with ship progression
- ✅ Permadeath risk scaling (T8 = 30%, T10 = 100%)

**Ready for implementation and balancing**

---

*Document Version: 2.0 - Navy Field Style Redesign*
*Created: 2025-10-05*
*Next: Turret module research trees and ammunition economics*
