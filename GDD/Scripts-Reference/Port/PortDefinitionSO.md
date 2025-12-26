---
tags: [script, port, scriptableobject, configuration, implemented]
script-type: ScriptableObject
namespace: WOS.ScriptableObjects.Port
file-path: Assets/Scripts/ScriptableObjects/Port/PortDefinitionSO.cs
status: IMPLEMENTED
size: ~289 lines
feature-group: port
---

# PortDefinitionSO.cs

## Quick Reference
**Type**: ScriptableObject (Port Configuration)
**Namespace**: WOS.ScriptableObjects.Port
**File**: `Assets/Scripts/ScriptableObjects/Port/PortDefinitionSO.cs`
**Size**: ~289 lines
**Create**: `Create > WOS > Port > Port Definition`
**Dependencies**: PortVisualStyleSO, Nationality enum

---

## Purpose
Master configuration ScriptableObject for individual ports. Defines port identity, services, ocean zone configuration, harbor layout, and visual theming. Single harbor scene loads different PortDefinitionSO assets to create unique ports.

---

## Configuration Sections

### Identity

```csharp
[Header("Identity")]
public string PortId;           // Unique identifier (e.g., "port_new_york")
public string PortName;         // Display name (e.g., "New York Harbor")
public Nationality Nationality; // Nation for visual theming
[Range(1, 10)]
public int PortTier = 1;        // Tier affects storage, services, safe zone
```

### Port Tiers

| Tier | Storage Height | AoP Radius | Services |
|------|----------------|------------|----------|
| T1 | 10 rows | 50 units | Basic |
| T2 | 15 rows | 75 units | + Trading |
| T3 | 20 rows | 100 units | + Fitting |
| T4 | 25 rows | 125 units | + Crew Hiring |
| T5 | 30 rows | 150 units | + Banking |
| T6-T10 | +5 rows each | +25 each | Full services |

---

### Services Configuration

```csharp
[Header("Services")]
public bool HasRepair = true;       // Ship repair available
public bool HasTrading = true;      // Buy/sell cargo
public bool HasStorage = true;      // Port warehouse access
public bool HasFitting = true;      // Equipment installation
public bool HasCrewHiring = true;   // Recruit crew members
public bool HasBanking = true;      // Currency exchange, loans
public bool HasMissions = true;     // Mission board access

[Header("Service Modifiers")]
[Range(0.5f, 2.0f)]
public float RepairCostMultiplier = 1.0f;
[Range(0.5f, 2.0f)]
public float TradePriceMultiplier = 1.0f;
```

---

### Ocean Configuration

```csharp
[Header("Ocean Position")]
public Vector2 OceanPosition;           // World position on ocean map
public float AoPRadiusOverride = 0f;    // Custom AoP radius (0 = use tier default)
public float AoIRadius = 50f;           // Area of Interaction radius

[Header("Approach Markers")]
[Range(0, 8)]
public int BuoyCount = 4;               // Number of approach buoys
public float BuoySpacing = 20f;         // Distance between buoys
public Color BuoyLightColor = Color.green;
```

### Zone Radius Calculation

```csharp
public float GetAoPRadius()
{
    if (AoPRadiusOverride > 0f) return AoPRadiusOverride;
    return 50f + (PortTier - 1) * 25f; // T1=50, T2=75, T3=100...
}

public float GetAoIRadius()
{
    return AoIRadius > 0f ? AoIRadius : GetAoPRadius() * 0.5f;
}
```

---

### Harbor Layout

```csharp
[Header("Harbor Layout")]
public Vector2 HarborSpawnPosition;     // Where player spawns in harbor
public float HarborSpawnRotation = 0f;  // Initial facing direction

[Header("Docking Squares")]
public DockingSquareData[] DockingSquares;  // Array of dock positions

[Header("Exit Zone")]
public Vector2 ExitZonePosition;        // Position of exit trigger
public float ExitZoneRadius = 10f;      // Size of exit trigger
```

### DockingSquareData Structure

```csharp
[System.Serializable]
public struct DockingSquareData
{
    public Vector2 Position;
    public float Rotation;
    public Vector2 Size;
    public bool IsLargeDock;  // For capital ships
}
```

---

### Visual Configuration

```csharp
[Header("Visual Style")]
public PortVisualStyleSO VisualStyle;   // Nationality-specific assets

[Header("Buildings")]
public BuildingPlacement[] Buildings;    // Harbor building positions

[Header("Decorations")]
public DecorationPlacement[] Decorations; // Props, crates, NPCs
```

---

## Validation Methods

```csharp
public bool ValidateConfiguration()
{
    bool valid = true;

    if (string.IsNullOrEmpty(PortId))
    {
        Debug.LogError($"Port {PortName}: Missing PortId");
        valid = false;
    }

    if (DockingSquares == null || DockingSquares.Length == 0)
    {
        Debug.LogError($"Port {PortName}: No docking squares defined");
        valid = false;
    }

    if (VisualStyle == null)
    {
        Debug.LogWarning($"Port {PortName}: No visual style assigned");
    }

    return valid;
}
```

---

## Usage Example

```csharp
// In HarborSceneManager
[SerializeField] private PortSceneStateHolder stateHolder;

private void Start()
{
    var portDef = stateHolder.CurrentPort;

    // Spawn visual elements
    SpawnBuildings(portDef.Buildings, portDef.VisualStyle);
    SpawnDocks(portDef.DockingSquares);
    SpawnExitZone(portDef.ExitZonePosition, portDef.ExitZoneRadius);

    // Configure services UI
    SetupServiceButtons(portDef);
}
```

---

## Integration Points

### Dependencies
- [[PortVisualStyleSO]] - Visual assets
- [[PortEnums]] - Nationality enum

### Used By
- [[HarborSceneManager]] - Spawns harbor content
- [[PortSceneStateHolder]] - Stores current port reference
- [[PlayerPortStateController]] - Zone radius checks
- [[PortZoneManager]] - Ocean zone setup

---

## Related Files
- [[PortVisualStyleSO]] - Nationality visual assets
- [[HarborSceneManager]] - Scene setup
- [[PortEnums]] - Nationality enum

---

## Design Notes
- Single scene, multiple configurations pattern
- Tier-based defaults with override capability
- Modular service flags for port variety
- Visual style separation from gameplay config
- Validation catches configuration errors early

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added service multipliers
- **2025-01**: Added buoy configuration
- **2025-01**: Added validation methods

