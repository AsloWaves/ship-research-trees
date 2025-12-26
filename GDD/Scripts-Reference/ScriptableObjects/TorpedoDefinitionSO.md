# TorpedoDefinitionSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Items/TorpedoDefinitionSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Items` |
| **Inheritance** | `EquipmentDefinitionSO` → `ScriptableObject` |
| **Implements** | `IVisualMount` |
| **Lines** | 254 |

---

## Purpose

Torpedo launcher equipment configuration with tube geometry, guidance systems, and launch mechanics. Torpedoes are submarine/destroyer primary weapons with high damage but limited range and speed.

---

## Torpedo Classification

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `torpedoType` | `TorpedoType` | `Surface` | Type of torpedo system |

### TorpedoType Values
- **Surface**: Surface ship launcher (destroyers, cruisers)
- **Submarine**: Submarine tubes (bow/stern)
- **Aerial**: Air-dropped torpedo (carrier aircraft)

---

## Torpedo Specifications

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `caliber` | `float` | 12-30 inches | 21 | Torpedo caliber (standard: 21", Long Lance: 24") |
| `tubes` | `int` | 1-12 | 4 | Number of torpedo tubes |
| `damageMJ` | `int` | 10-5,000 MJ | 500 | Damage per torpedo in megajoules (MJ) |
| `maxRangeMiles` | `float` | 1-25 nm | 10 | Maximum torpedo range in nautical miles |
| `torpedoSpeedKnots` | `float` | 20-70 knots | 40 | Torpedo speed in knots |

**Salvo Damage**: `damageMJ × tubes` (total damage if all torpedoes hit)

---

## Launcher Properties

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `reloadTime` | `float` | 30-600 seconds | 120 | Reload time per tube in seconds |
| `launchInterval` | `float` | 0.5-10 seconds | 2 | Time between individual tube launches |
| `rotationSpeed` | `float` | 0-45 deg/sec | 15 | Launcher rotation speed (0 for fixed launchers) |
| `isRotatable` | `bool` | - | `true` | Can this launcher rotate? (false for submarine bow tubes) |

**Salvo Time**: `(tubes - 1) × launchInterval` (time to launch all torpedoes)

---

## Torpedo Guidance

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `hasGuidance` | `bool` | - | `false` | Does this torpedo have guidance system? |
| `guidanceType` | `TorpedoGuidanceType` | Enum | `None` | Guidance type (if equipped) |
| `homingAngle` | `float` | 0-90 degrees | 30 | Homing angle for guided torpedoes |

### TorpedoGuidanceType Values
- **None**: Unguided, straight-running torpedo
- **Passive**: Passive acoustic homing (detects noise)
- **Active**: Active acoustic homing (emits sonar pings)
- **WireGuided**: Wire-guided (player controlled)
- **PatternRunning**: Pattern-running (zigzag or circle search)

---

## Crew Requirements

| Property | Type | Range | Default |
|----------|------|-------|---------|
| `minimumCrewLevel` | `int` | 1-200 | 1 |
| `optimalCrewSize` | `int` | 2-30 | 8 |

---

## Launcher Geometry

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `launcherCenter` | `Vector3` | (0,0,0) | Center/pivot point in local space |
| `tubeExitPoints` | `Vector3[]` | [(0,0,1)] | Tube exit points for each torpedo |
| `minElevation` | `float` | -15° | Minimum elevation (depression) |
| `maxElevation` | `float` | 10° | Maximum elevation |

**Auto-Sync**: `SyncTubePointsWithCount()` ensures array matches tube count.

**Default Spacing**: 0.3m between tubes (wider than gun barrels)

---

## Visual Settings

| Property | Type | Range | Default |
|----------|------|---------|---------|
| `visualScale` | `float` | 0.1-5.0 | 1.0 |
| `visualOffset` | `Vector3` | - | (0,0,0) |

---

## Key Methods

### Get Salvo Damage
```csharp
public int GetSalvoDamageMJ()
```
Returns total damage if all torpedoes hit: `damageMJ × tubes`

### Get Max Range (Meters)
```csharp
public float GetMaxRangeMeters()
```
Converts range from nautical miles to meters (1 nm = 1852 m)

### Get Torpedo Speed (m/s)
```csharp
public float GetTorpedoSpeedMS()
```
Converts speed from knots to m/s (1 knot = 0.5144 m/s)

### Get Salvo Time
```csharp
public float GetSalvoTime()
```
Time to launch all torpedoes: `(tubes - 1) × launchInterval`

### Sync Tube Points
```csharp
public void SyncTubePointsWithCount()
```
Auto-generates tube exit points to match tube count.

---

## Historical Examples

### 21-inch Mark 15 (USA - Standard)
```
Caliber: 21 inches
Tubes: 5 (quintuple mount)
Damage: 500 MJ
Range: 10 nm @ 40 knots
Guidance: None
```

### Type 93 "Long Lance" (Japan)
```
Caliber: 24 inches (610mm)
Tubes: 8-12
Damage: 800 MJ
Range: 20 nm @ 48 knots
Guidance: None (oxygen-fueled, long range)
```

### Mark 48 (USA - Modern Submarine)
```
Caliber: 21 inches
Tubes: 4-6
Damage: 1,200 MJ
Range: 25 nm @ 55 knots
Guidance: Active/Passive Acoustic Homing
```

---

## IVisualMount Implementation

Implements `IVisualMount` for generic equipment rendering:
- **CanRotate**: Returns `isRotatable`
- **RotationSpeed**: Returns `rotationSpeed` (0 if not rotatable)
- **ExitPointCount**: Returns `tubes`

---

## Usage Example

```csharp
TorpedoDefinitionSO torpedoLauncher = // from database

// Get salvo damage
int totalDamage = torpedoLauncher.GetSalvoDamageMJ();
Debug.Log($"Salvo damage: {totalDamage} MJ");

// Calculate salvo launch time
float salvoTime = torpedoLauncher.GetSalvoTime();
Debug.Log($"Salvo takes {salvoTime} seconds");

// Get range in meters
float range = torpedoLauncher.GetMaxRangeMeters();
Debug.Log($"Max range: {range}m");

// Check if launcher can rotate
if (torpedoLauncher.isRotatable)
{
    Debug.Log($"Rotation speed: {torpedoLauncher.rotationSpeed}°/sec");
}
```

---

## Create via Unity Menu

**Path**: `Create > WOS > Equipment > Torpedo Launcher`

**Order**: 2

**Default Filename**: `Torpedo_T1_21inch`
