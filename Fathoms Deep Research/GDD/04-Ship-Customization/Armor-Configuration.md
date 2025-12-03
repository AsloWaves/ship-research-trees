# Armor Configuration System

**Status**: 📋 PLANNED (Phase 2/3 feature)
**Tags**: [planned, phase2, ship-customization, armor, navy-field-inspired]
**Priority**: HIGH (core combat mechanic)
**Related Systems**: [Module System](Module-System.md), [Combat System](../02-Core-Systems/Combat-System.md), [Ship Fitting UI](Ship-Fitting-UI.md)

---

## Overview

**Navy Field-Inspired Armor System:**

Fathoms Deep uses a detailed armor configuration interface allowing precise thickness adjustment for multiple armor zones. Armor thickness directly affects penetration mechanics and damage mitigation.

**Design Philosophy:**
- **Granular Control**: Players adjust armor thickness per zone in 0.1" increments
- **Material Variety**: Multiple armor types with distinct protection profiles and weight characteristics
- **Real-Time Feedback**: Instant weight, speed, and cost calculations
- **Historical Authenticity**: Armor types based on real naval steel specifications
- **Strategic Trade-offs**: Balance protection vs. speed vs. cost

---

## Armor Interface Design

### Armor Configuration Screen

**Visual Layout:**
- **Visual Schematic**: Side and top-down view of ship showing armor zones
- **9 Armor Zones**: 3 deck zones, 3 side belt zones, 3 structural zones
- **Dual Input Methods**:
  - **Dropdown Menu**: Select armor type (material)
  - **Manual Entry**: Input exact thickness in inches (0.1" increments)
  - **Slider Control**: Quick adjustment with fine-tuning capability
- **Real-Time Feedback**: Weight, speed, cost calculations update instantly
- **MM Equivalents**: Shows millimeter conversion next to inch values

---

## Armor Zone Configuration (9 Total Zones)

### Deck Armor (Horizontal Protection)

**3 Deck Zones:**
1. **Forward Deck** - [Armor Type] [Thickness in inches (mm)]
2. **Center Deck** - [Armor Type] [Thickness in inches (mm)]
3. **Aft Deck** - [Armor Type] [Thickness in inches (mm)]

**Purpose:**
- Protection against plunging fire at long ranges
- Defense against dive bombers and high-angle attacks
- Magazine and machinery protection from above

### Side Belt Armor (Vertical Protection)

**3 Belt Zones:**
4. **Forward Belt** - [Armor Type] [Thickness in inches (mm)]
5. **Center Belt** - [Armor Type] [Thickness in inches (mm)]
6. **Aft Belt** - [Armor Type] [Thickness in inches (mm)]

**Purpose:**
- Primary protection against flat-trajectory gunfire
- Critical for close-range and medium-range combat
- Engine room and magazine protection from broadsides

### Structural Armor (Critical Components)

**3 Structural Zones:**
7. **Conning Tower** - [Armor Type] [Thickness in inches (mm)]
8. **Main Turrets** - [Armor Type] [Thickness in inches (mm)]
9. **Secondary Turrets** - [Armor Type] [Thickness in inches (mm)]

**Note**: Tertiary/AA turrets are unarmored and not configurable.

**Purpose:**
- Command and control protection (Conning Tower)
- Main battery survivability (Main Turrets)
- Secondary armament protection (Secondary Turrets)

---

## Armor Type Options (Dropdown Selection)

### Rolled Homogeneous Armor (RHA) - Standard

- **Protection Coefficient**: 1.0 (baseline)
- **Weight per Inch**: 40 tons/inch (baseline)
- **Cost Multiplier**: 1.0x
- **Availability**: Universal, all nations
- **Best Use**: Balanced protection, general-purpose
- **Historical Context**: Standard naval armor, widely available

### Face-Hardened Armor - AP-Focused

- **Protection Coefficient**: 1.3 vs AP shells, 0.8 vs HE shells
- **Weight per Inch**: 45 tons/inch (heavier)
- **Cost Multiplier**: 1.4x
- **Availability**: Common
- **Best Use**: Battleship duels, AP-heavy combat zones
- **Drawback**: Brittle vs HE, vulnerable to fire damage
- **Historical Context**: Early 20th century armor technology

### Krupp Cemented Armor - German Specialty

- **Protection Coefficient**: 1.4 vs AP shells, 1.1 vs HE shells
- **Weight per Inch**: 50 tons/inch (very heavy)
- **Cost Multiplier**: 2.0x
- **Availability**: German ports (expensive elsewhere)
- **Best Use**: Premium protection, high-stakes operations
- **Drawback**: Expensive, very heavy (speed penalty)
- **Historical Context**: Premium German armor steel, superior quality

### Terni Steel - Italian Specialty

- **Protection Coefficient**: 0.9 vs AP shells, 1.2 vs HE shells
- **Weight per Inch**: 32 tons/inch (lighter)
- **Cost Multiplier**: 1.2x
- **Availability**: Italian ports, Mediterranean region
- **Best Use**: Cruisers, speed-focused builds
- **Advantage**: Lighter weight, good HE resistance
- **Historical Context**: Italian naval armor, lighter but effective

### Ducol Steel - British Specialty

- **Protection Coefficient**: 0.85 vs AP shells, 1.0 vs HE shells
- **Weight per Inch**: 28 tons/inch (very light)
- **Cost Multiplier**: 1.1x
- **Availability**: British ports, Commonwealth
- **Best Use**: Destroyers, speed-critical ships
- **Advantage**: Minimal weight penalty, good for light ships
- **Historical Context**: British D-class (Ducol) steel, lightweight

### Special Treatment Steel (STS) - US Specialty

- **Protection Coefficient**: 1.15 vs AP shells, 1.15 vs HE shells
- **Weight per Inch**: 42 tons/inch (moderate)
- **Cost Multiplier**: 1.8x
- **Availability**: US ports (expensive elsewhere)
- **Best Use**: All-around protection, balanced builds
- **Advantage**: Excellent general-purpose protection
- **Historical Context**: US Navy premium armor, well-rounded performance

---

## Armor Thickness Configuration

### Input Methods

**Manual Entry**: Type exact value (e.g., "10.5" for 10.5 inches / 266.7mm)
**Slider**: Drag to adjust in 0.5" increments, fine-tune with arrow keys (0.1" per click)
**Increment Buttons**: +/- 0.1" buttons for precise adjustment
**Display Format**: "10.5" (266.7mm)" - inches primary, millimeters in parentheses

### Ship Class Armor Limits

| Ship Class | Maximum Deck | Maximum Belt | Maximum Turret | Maximum Conning Tower |
|------------|-------------|--------------|----------------|---------------------|
| Destroyer | 0.5" (12.7mm) | 2.0" (50.8mm) | 1.0" (25.4mm) | 0.5" (12.7mm) |
| Light Cruiser | 2.0" (50.8mm) | 4.0" (101.6mm) | 3.0" (76.2mm) | 2.0" (50.8mm) |
| Heavy Cruiser | 3.0" (76.2mm) | 8.0" (203.2mm) | 6.0" (152.4mm) | 4.0" (101.6mm) |
| Battleship | 7.0" (177.8mm) | 18.0" (457.2mm) | 17.0" (431.8mm) | 12.0" (304.8mm) |
| Carrier | 3.0" (76.2mm) | 4.0" (101.6mm) | N/A | 2.0" (50.8mm) |

**Notes:**
- Limits based on historical ship construction capabilities
- Exceeding limits requires special research unlocks or blueprint modifications
- Carriers have no turret armor (no main battery)

---

## Armor Weight & Performance Impact

### Weight Calculation Formula

```
Zone Weight = Thickness (inches) × Armor Type Weight Multiplier × Zone Size Factor

Example (Iowa Battleship Center Belt):
- Thickness: 12.1" (307.3mm) RHA
- RHA Weight: 40 tons/inch
- Zone Size Factor: 45 (large zone)
- Total Weight: 12.1 × 40 × 45 = 21,780 tons for center belt alone
```

**Zone Size Factors by Ship Class:**

| Ship Class | Deck Zones | Belt Zones | Turret Zones | Conning Tower |
|------------|-----------|-----------|--------------|---------------|
| Destroyer | 5-8 | 8-12 | 2-4 | 1 |
| Light Cruiser | 12-18 | 20-28 | 4-8 | 2 |
| Heavy Cruiser | 18-25 | 30-40 | 8-12 | 3 |
| Battleship | 30-50 | 40-60 | 12-20 | 5 |

### Performance Impact

**Armor Weight Performance Impact** (permanent ship weight, separate from cargo weight penalties in [[Inventory-System]]):

**Speed Reduction:**
Total armor weight affects max speed:
- **Light armor (0-500 tons)**: No penalty
- **Moderate armor (500-2000 tons)**: -1 to -3 knots
- **Heavy armor (2000-5000 tons)**: -3 to -6 knots
- **Extreme armor (5000+ tons)**: -6 to -12 knots

**Speed Reduction Formula:**
```
Speed Penalty (knots) = (Total Armor Weight / 1000) × Ship Speed Penalty Coefficient

Ship Speed Penalty Coefficients:
- Destroyer: 0.5 (light hull, high sensitivity)
- Cruiser: 0.3 (moderate hull)
- Battleship: 0.15 (heavy hull, low sensitivity)
- Carrier: 0.25 (large hull, moderate sensitivity)
```

**Fuel Consumption:**
- Heavier ships consume more fuel per km traveled
- Fuel consumption increase proportional to total weight
- Formula: `Fuel/km = Base Consumption × (1 + Total Weight / Max Displacement × 0.3)`

**Maneuverability:**
- Turn rate reduced proportional to total weight
- Heavier armor = slower turning radius
- Formula: `Turn Rate = Base Turn Rate × (1 - Total Weight / Max Displacement × 0.2)`

**Note**: Armor weight contributes to total hull weight percentage equally with turrets, modules, crew, and cargo. Graduated penalties apply based on total weight percentage (50-80% minor, 80-95% moderate, 95-100% heavy penalties). **HARD CAP at 100%** - ships cannot undock when overweight.

---

## Armor Cost Calculation

### Cost Formula

```
Zone Cost = Base Cost × Thickness² × Armor Type Multiplier

Example (12" Belt RHA):
- Base Cost: ₡10,000 per zone
- Thickness: 12 inches
- Armor Type: RHA (1.0x multiplier)
- Total: ₡10,000 × 144 × 1.0 = ₡1,440,000 for one belt zone
```

**Base Costs by Zone Type:**
- Deck Armor: ₡8,000 per zone
- Belt Armor: ₡10,000 per zone
- Turret Armor: ₡12,000 per zone
- Conning Tower: ₡15,000 per zone

**Armor Type Cost Multipliers:**
- RHA: 1.0x (baseline)
- Face-Hardened: 1.4x
- Krupp Cemented: 2.0x
- Terni Steel: 1.2x
- Ducol Steel: 1.1x
- STS: 1.8x

---

## Armor Acquisition Methods

### Base Armor (Inherent to Ship Design)

- Ships come with historical armor configuration by default
- Can be modified freely at any friendly port
- Default armor provides baseline protection
- Players can strip armor to reduce weight (not recommended for combat)

### Armor Upgrades (Unlocked via Research)

**Basic Armor Schemes**: Default, available immediately
**Improved Armor Schemes**: Unlock via ship research tree (e.g., "Iowa Modernized Armor Scheme")
**Special Armor Types**: Unlock specific armor materials (Krupp, STS) via nation research
**Blueprint-Based Schemes**: Find/earn special armor configurations (historical refits, experimental designs)

### Armor Configuration Constraints

**Weight Budget**: Total armor + modules + crew + cargo ≤ ship maximum displacement (**HARD CAP at 100%** per [[Inventory-System]])
- **All Weight Types Equal**: Armor, turrets, modules, crew, and cargo ALL contribute equally to total hull weight percentage
- **Cargo Weight**: Variable load (ammunition, fuel, loot) subject to graduated penalties (50-80% minor, 80-95% moderate, 95-100% heavy)
- **Hard Cap System**: Ships **cannot exceed 100% weight** - applies at port (cannot undock) AND at sea (cannot pick up cargo that would exceed cap)
- **Armor adds to total weight** just like any other equipment - does NOT reduce cargo grid cell count

**Ship Class Limits**: Cannot exceed max thickness per ship class
**Historical Accuracy Mode** (Optional Toggle): Restricts armor to historically plausible ranges

**Validation Warnings:**
- Red: At or exceeds 100% weight limit (HARD CAP - cannot undock) or ship class maximum
- Orange: Near weight limit (95-100% capacity) - heavy penalties active
- Yellow: Moderate weight (80-95% capacity) - moderate penalties active
- Green: Valid configuration within optimal limits (<80% capacity)

---

## Example Armor Configurations

### T3 Fletcher-class Destroyer (Speed Build)

```
Armor Type: Ducol Steel (lightweight British steel)
Forward Deck: 0.2" (5.1mm)
Center Deck: 0.3" (7.6mm)
Aft Deck: 0.2" (5.1mm)
Forward Belt: 0.5" (12.7mm)
Center Belt: 1.0" (25.4mm)
Aft Belt: 0.5" (12.7mm)
Conning Tower: 0.5" (12.7mm)
Main Turrets: 0.5" (12.7mm)
Secondary Turrets: 0" (unarmored)

Total Armor Weight: 285 tons
Speed Impact: No penalty (under 500 tons)
Total Cost: ₡125,000
```

**Strategic Analysis:**
- Minimal armor for maximum speed
- Relies on agility over protection
- Cost-effective for early-tier operations
- Vulnerable to any direct hits

### T8 Iowa-class Battleship (Balanced Build)

```
Armor Type: Special Treatment Steel (US premium armor)
Forward Deck: 4.0" (101.6mm)
Center Deck: 6.0" (152.4mm)
Aft Deck: 4.0" (101.6mm)
Forward Belt: 10.0" (254.0mm)
Center Belt: 12.1" (307.3mm)
Aft Belt: 10.0" (254.0mm)
Conning Tower: 7.25" (184.2mm)
Main Turrets: 17.0" (431.8mm)
Secondary Turrets: 2.5" (63.5mm)

Total Armor Weight: 4,850 tons
Speed Impact: -5 knots (from base 33 knots to 28 knots)
Total Cost: ₡8,500,000
```

**Strategic Analysis:**
- Historically accurate Iowa-class armor scheme
- Balanced protection across all zones
- Moderate speed penalty acceptable for survivability
- Premium armor type provides excellent all-around defense

### T10 Yamato-class Battleship (Maximum Protection Build)

```
Armor Type: Krupp Cemented Armor (German premium, ultimate protection)
Forward Deck: 7.0" (177.8mm)
Center Deck: 7.0" (177.8mm)
Aft Deck: 7.0" (177.8mm)
Forward Belt: 16.0" (406.4mm)
Center Belt: 18.0" (457.2mm) [MAXIMUM]
Aft Belt: 16.0" (406.4mm)
Conning Tower: 12.0" (304.8mm)
Main Turrets: 17.0" (431.8mm)
Secondary Turrets: 3.0" (76.2mm)

Total Armor Weight: 7,200 tons
Speed Impact: -10 knots (from base 27 knots to 17 knots)
Total Cost: ₡18,500,000
Strategic Trade-off: Maximum survivability, severe speed penalty
```

**Strategic Analysis:**
- Pushing maximum armor limits
- Designed to tank hits in high-tier combat zones
- Severe speed penalty limits tactical flexibility
- Extremely expensive but nearly impenetrable
- Best for permadeath zones where survival is critical

### T6 Heavy Cruiser (Anti-HE Build)

```
Armor Type: Terni Steel (Italian HE-resistant armor)
Forward Deck: 2.0" (50.8mm)
Center Deck: 3.0" (76.2mm)
Aft Deck: 2.0" (50.8mm)
Forward Belt: 6.0" (152.4mm)
Center Belt: 8.0" (203.2mm) [MAXIMUM for Heavy Cruiser]
Aft Belt: 6.0" (152.4mm)
Conning Tower: 4.0" (101.6mm)
Main Turrets: 6.0" (152.4mm)
Secondary Turrets: 1.5" (38.1mm)

Total Armor Weight: 1,850 tons
Speed Impact: -2 knots (from base 32 knots to 30 knots)
Total Cost: ₡2,800,000
Strategic Trade-off: Excellent HE protection, lighter weight, moderate AP protection
```

**Strategic Analysis:**
- Specialized for countering HE-heavy enemies (destroyers, light cruisers)
- Terni steel's lighter weight preserves cruiser speed
- Good protection-to-weight ratio
- Cost-effective for mid-tier operations

---

## Armor Damage & Repair

### Armor Degradation

**Armor does NOT degrade permanently:**
- Armor thickness is static configuration, not consumable
- Damage reduces module/hull HP, not armor thickness itself
- Armor provides damage reduction based on penetration mechanics

**Penetration Mechanics:**
```
Penetration Check = Incoming Shell Penetration Power vs. Armor Thickness × Protection Coefficient

Result:
- Penetration > Armor: Full damage to internal modules/hull
- Penetration = Armor: 50% damage reduction
- Penetration < Armor: Ricochet or minimal damage (10-20% damage)
```

### Armor Reconfiguration

**At-Port Armor Changes:**
- Free to reconfigure armor at any friendly port
- Installation time: 30 minutes - 2 hours depending on extent of changes
- Cost only applies to new armor (adding thickness or changing material)
- Removing armor is free (weight reduction)

**Example Reconfiguration:**
```
Scenario: Player wants to increase center belt from 10" to 12" RHA

Current Configuration:
- Center Belt: 10.0" RHA
- Cost: ₡1,000,000 (already paid)
- Weight: 18,000 tons

New Configuration:
- Center Belt: 12.0" RHA
- Additional Cost: ₡(12² - 10²) × ₡10,000 = ₡440,000
- Additional Weight: 3,600 tons
- Installation Time: 45 minutes

Total New Stats:
- Center Belt: 12.0" RHA
- Total Cost: ₡1,440,000 (cumulative)
- Total Weight: 21,600 tons
```

---

## Strategic Armor Considerations

### Combat Zone Optimization

**Low-Tier Zones (T1-T3):**
- Minimal armor recommended (speed > protection)
- Focus on agility and firepower
- Armor cost exceeds benefit at low tiers

**Mid-Tier Zones (T4-T6):**
- Balanced armor configurations
- Protect critical areas (center belt, main turrets)
- Cost-effective armor types (RHA, Terni Steel)

**High-Tier Zones (T7-T9):**
- Heavy armor essential for survival
- Premium armor types provide edge
- Speed penalties acceptable for protection

**Permadeath Zones (T10+):**
- Maximum armor recommended
- Krupp or STS armor types preferred
- Survival > speed in extreme danger zones

### Armor Meta Strategies

**Turtle Build (Maximum Protection):**
- All zones at maximum thickness
- Premium armor types
- Accept severe speed penalties
- Best for: Tanking damage, zone control, permadeath survival

**Speed Demon (Lightweight):**
- Minimal armor, Ducol Steel preferred
- Prioritize engines over protection
- Rely on agility and positioning
- Best for: Hit-and-run tactics, extraction missions, kiting

**Balanced Brawler (Medium Armor):**
- Critical zones armored (center belt, main turrets)
- Moderate armor elsewhere
- Balance speed and protection
- Best for: General combat, versatile operations

**Asymmetric Armor (Specialized):**
- Heavy armor on engagement side (port or starboard)
- Light armor on opposite side
- Tactical positioning required
- Best for: Experienced players, specific combat scenarios

---

## UI Integration

See [Ship-Fitting-UI.md](Ship-Fitting-UI.md) for complete armor configuration interface design, including:
- Visual schematic views (side profile, top-down)
- Real-time stat feedback
- Color-coded heat maps
- Armor scheme presets
- Validation warnings
- Quick-apply historical configurations

---

## Summary

**Complete Armor Configuration System Includes:**

✅ **9-Zone Armor System**: Deck (3), Belt (3), Structural (3) with independent configuration
✅ **6 Armor Types**: RHA, Face-Hardened, Krupp, Terni, Ducol, STS with distinct characteristics
✅ **Granular Control**: 0.1" thickness increments with inch/mm dual display
✅ **Real-Time Feedback**: Weight, speed, cost calculations update instantly
✅ **Strategic Trade-offs**: Balance protection vs. speed vs. cost
✅ **Ship Class Limits**: Historical constraints prevent unrealistic configurations
✅ **Multiple Acquisition Paths**: Default, research, blueprints, special schemes

**Integration Points:**
- Module System: Armor weight impacts module fitting capacity
- Combat System: Penetration mechanics use armor thickness
- Ship Fitting UI: Complete visual interface for armor configuration
- Economy System: Armor costs drive significant credit expenditure

---

**End of Armor Configuration System Specification**
