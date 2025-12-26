# TurretDefinitionSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Items/TurretDefinitionSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Items` |
| **Inheritance** | `EquipmentDefinitionSO` → `ScriptableObject` |
| **Implements** | `IVisualMount` (generic equipment mount system) |
| **Lines** | 284 |
| **Architecture** | Configuration-Driven Design |

---

## Purpose

Defines turret/gun equipment configurations for naval vessels. Configures firepower stats, ammunition, crew requirements, and 3D geometry for visual rendering. Turrets are the primary offensive weapons on surface ships.

**Key Features**:
- Realistic naval gun specifications (0.5" to 24" caliber)
- Multiple turret categories (Main Battery, Secondary, AA, Dual Purpose)
- Configurable barrel geometry and muzzle positions
- Rotation and elevation mechanics
- Crew skill requirements
- Historical designation support

---

## Turret Classification

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `turretCategory` | `TurretCategory` | `Main` | Category of turret (Main/Secondary/DualPurpose/AA) |
| `turretType` | `TurretType` | `Main` | Legacy turret type (for backwards compatibility) |

### TurretCategory Values
- **Main**: Primary armament (8"-16" battleship guns)
- **Secondary**: Medium-range defense (5"-6" guns)
- **DualPurpose**: Anti-ship and anti-aircraft (5"/38 Mark 12)
- **AA**: Anti-aircraft only (40mm Bofors, 20mm Oerlikon)

---

## Firepower Stats

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `caliber` | `float` | 0.5-24 inches | 5 | Gun caliber in inches (0.5" MG to 20" Iowa class) |
| `barrels` | `int` | 1-12 | 2 | Number of gun barrels in turret |
| `damageKJ` | `int` | 1-5,000 KJ | 50 | Damage per shell in kilojoules (KJ) |
| `rateOfFire` | `float` | 0.5-1,200 RPM | 10 | Rate of fire (rounds per minute) |

**Damage Per Minute Calculation**:
```csharp
DPM = damageKJ × barrels × rateOfFire
```

**Example**: 5" dual-barrel turret at 10 RPM → `50 × 2 × 10 = 1,000 KJ/min`

---

## Ammunition

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `primaryShellType` | `ShellType` | Enum | `AP` | Primary shell type (AP, HE, SAP) |
| `secondaryShellType` | `ShellType` | Enum | `HE` | Secondary shell type (for dual-capable guns) |
| `supportsVTFuse` | `bool` | - | `false` | Can use VT (proximity) fuse shells for AA |
| `maxRangeMiles` | `float` | 0.5-50 nautical miles | 15 | Maximum firing range in nautical miles |
| `magazineCapacity` | `int` | 1-2,000 shells | 100 | Magazine capacity (total shells) |
| `reloadTime` | `float` | 0.1-120 seconds | 5 | Reload time in seconds |

### ShellType Values
- **AP** (Armor Piercing): High penetration, low blast damage
- **HE** (High Explosive): High blast damage, low penetration
- **SAP** (Semi-Armor Piercing): Balanced penetration and damage
- **VT Fuse**: Proximity-fused shells for anti-aircraft work

---

## Accuracy & Precision

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `baseAccuracy` | `float` | 0-100% | 70 | Base accuracy percentage |
| `rotationSpeed` | `float` | 1-180 deg/sec | 20 | Turret rotation speed (degrees per second) |
| `elevationSpeed` | `float` | 1-90 deg/sec | 10 | Gun elevation/depression speed (degrees per second) |

---

## Crew Requirements

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `minimumCrewLevel` | `int` | 1-200 | 1 | Minimum crew level required to operate effectively |
| `optimalCrewSize` | `int` | 2-100 sailors | 15 | Optimal crew size for this turret |

Higher-level crew improves accuracy, reload speed, and damage output.

---

## Turret Geometry

### Center & Pivot
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `turretCenter` | `Vector3` | `(0,0,0)` | Center/pivot point of the turret in local space |
| `elevationPivotOffset` | `Vector3` | `(0,0,0)` | Elevation pivot offset from turret center |

### Muzzle Exit Points
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `muzzleExitPoints` | `Vector3[]` | `[(0,0,1)]` | Muzzle exit points for each barrel in local space (relative to turret center) |

**Auto-Sync**: `SyncMuzzlePointsWithBarrels()` ensures array length matches barrel count.

**Default Spacing**: Barrels are spaced horizontally based on caliber:
```csharp
spacing = caliber × 0.01f meters
offset = (barrelIndex - (barrels-1)/2) × spacing
defaultPosition = Vector3(offset, 0, 1f)
```

### Elevation Limits
| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `minElevation` | `float` | -30° to 0° | -5° | Minimum elevation angle (negative = depression) |
| `maxElevation` | `float` | 0° to 90° | 45° | Maximum elevation angle |

**Note**: Rotation limits (firing arcs) are defined by the ship's mount/hardpoint, not the turret itself. The same turret can have different arcs based on ship position.

---

## Visual Settings

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `visualScale` | `float` | 0.1-5.0 | 1.0 | Scale multiplier for visual sprite (1.0 = normal size) |
| `visualOffset` | `Vector3` | - | `(0,0,0)` | Offset for visual sprite from turret center |

---

## Key Methods

### Calculate Damage Per Minute
```csharp
public float GetDamagePerMinuteKJ()
```
Returns: `damageKJ × barrels × rateOfFire`

Used for balance comparison and DPS calculations.

### Get Muzzle World Position
```csharp
public Vector3 GetMuzzleWorldPosition(int barrelIndex, Transform turretTransform, float currentElevation = 0f)
```
Gets the world-space position of a specific barrel's muzzle, accounting for:
- Turret transform (rotation, position)
- Barrel index (which barrel)
- Current elevation angle

**Parameters**:
- `barrelIndex`: Which barrel (0-based)
- `turretTransform`: Transform of the turret GameObject
- `currentElevation`: Current elevation angle in degrees

**Returns**: World position of muzzle exit point

### Get All Muzzle Positions
```csharp
public Vector3[] GetAllMuzzleWorldPositions(Transform turretTransform, float currentElevation = 0f)
```
Returns world positions for all barrels at once.

### Get Muzzle Direction
```csharp
public Vector3 GetMuzzleDirection(Transform turretTransform, float currentElevation = 0f)
```
Gets the firing direction for the turret in world space.

### Sync Muzzle Points
```csharp
public void SyncMuzzlePointsWithBarrels()
```
Auto-generates muzzle exit points to match barrel count. Called automatically in `OnValidate()`.

### Get Max Range (Meters)
```csharp
public float GetMaxRangeMeters()
```
Converts max range from nautical miles to meters (1 nm = 1852 m).

### Get Turret Type String
```csharp
public string GetTurretTypeString()
```
Returns human-readable turret type:
- Main → "Main Battery"
- Secondary → "Secondary Battery"
- AA → "Anti-Aircraft"

---

## IVisualMount Implementation

Turrets implement `IVisualMount` for generic equipment mount rendering:

```csharp
public interface IVisualMount
{
    WeaponMountData GetMountData();
    int ExitPointCount { get; }
    Sprite GetVisualSprite();
    bool CanRotate { get; }
    float RotationSpeed { get; }
}
```

### Implementation
- **GetMountData()**: Returns `WeaponMountData` struct with geometry
- **ExitPointCount**: Returns `barrels` count
- **GetVisualSprite()**: Returns `icon` sprite from base class
- **CanRotate**: Returns `true` (turrets can rotate)
- **RotationSpeed**: Returns `rotationSpeed` value

---

## Auto-Generated Values (OnValidate)

### Equipment ID
**Format**: `{turretType}Battery_T{tier}_{caliber}inch`

**Example**: `MainBattery_T5_16inch`

### Equipment Name
**Format**: `{caliber}" {turretType} Turret (T{tier})`

**Example**: `16" Main Battery Turret (T5)`

---

## Historical Examples

### 5"/38 Mark 12 (USA - Most Produced Naval Gun)
```
Caliber: 5 inches
Barrels: 1
Tier: 3-5
Category: DualPurpose
Damage: 150 KJ
Rate of Fire: 15 RPM
Max Range: 18 miles
Supports VT Fuse: Yes
Crew Size: 15
```

### 16"/50 Mark 7 (Iowa-class Battleship)
```
Caliber: 16 inches
Barrels: 3 (triple turret)
Tier: 7
Category: Main
Damage: 3,500 KJ
Rate of Fire: 2 RPM
Max Range: 24 miles
Magazine: 120 shells
Crew Size: 90
```

### 40mm Bofors (Anti-Aircraft)
```
Caliber: 1.575 inches
Barrels: 4 (quad mount)
Tier: 3
Category: AA
Damage: 20 KJ
Rate of Fire: 120 RPM
Max Range: 5 miles
Crew Size: 7
```

---

## Usage Example

```csharp
// Create via Unity menu: Create > WOS > Equipment > Turret
TurretDefinitionSO turret = // reference from Inspector or database

// Get damage per minute
float dpm = turret.GetDamagePerMinuteKJ();
Debug.Log($"Turret DPM: {dpm} KJ/min");

// Get muzzle positions for all barrels
Transform turretObj = // turret GameObject transform
float elevation = 15f; // 15 degrees elevation
Vector3[] muzzles = turret.GetAllMuzzleWorldPositions(turretObj, elevation);

foreach (var muzzle in muzzles)
{
    Debug.Log($"Muzzle position: {muzzle}");
}

// Check if crew level is sufficient
int crewLevel = 50;
if (crewLevel >= turret.minimumCrewLevel)
{
    Debug.Log("Crew is qualified to operate this turret");
}

// Get max range in meters for physics
float maxRange = turret.GetMaxRangeMeters();
Debug.Log($"Max range: {maxRange}m");
```

---

## Integration Points

### Used By
- **CombatTurretController.cs** - Turret combat mechanics and firing logic
- **GenericEquipmentMount.cs** - Visual turret rendering system
- **EquipmentPanel.cs** - Inventory UI for turret management
- **ItemDatabaseSO.cs** - Master equipment database
- **EquipmentDatabaseSO.cs** - Specialized equipment database

### Related Systems
- **EquipmentDefinitionSO** - Base class for all equipment
- **TorpedoDefinitionSO** - Torpedo launcher equivalent
- **ModuleDefinitionSO** - Module equipment (fire control, radar)
- **IVisualMount** - Generic visual mount interface
- **WeaponMountData** - Geometry data structure

---

## Design Notes

### Turret vs Ship Mount Separation

Turrets define intrinsic properties (caliber, barrels, damage) while **ship mounts** define positioning and firing arcs. This allows:

1. **Reusability**: Same turret can be mounted on multiple ships
2. **Historical Accuracy**: Same gun (5"/38 Mark 12) used on destroyers, cruisers, battleships
3. **Flexible Placement**: Different firing arcs based on ship position (bow, stern, broadside)

Example: 5"/38 Mark 12 turret
- **On destroyer bow**: 270° firing arc (forward)
- **On battleship sides**: 180° firing arc (broadside only)
- **On carrier stern**: 120° firing arc (aft defense)

### Caliber Range Design

**0.5" to 24"** covers full spectrum of naval weapons:
- **0.5"-1"**: Machine guns and autocannons
- **1"-3"**: Light anti-aircraft guns
- **3"-5"**: Destroyer main guns, cruiser secondaries
- **5"-8"**: Heavy cruiser guns, dual-purpose weapons
- **8"-16"**: Battleship main batteries
- **16"-24"**: Super-heavy battleship guns (Yamato 18.1", proposed 20"+ designs)

### Damage Scaling

Damage in **kilojoules (KJ)** represents kinetic energy of shell:
- Small caliber (0.5"): ~5-10 KJ
- Medium (5"): ~100-200 KJ
- Large (16"): ~3,000-5,000 KJ

This allows realistic damage modeling where larger guns have exponentially higher damage but much slower rate of fire.

### VT Fuse Support

VT (Variable Time) proximity fuses were a major advancement in WWII AA warfare. Turrets that support VT fuse get significant anti-aircraft bonuses when using VT-fused shells.

---

## Create via Unity Menu

**Path**: `Create > WOS > Equipment > Turret`

**Order**: 1

**Default Filename**: `Turret_T1_5inch`
