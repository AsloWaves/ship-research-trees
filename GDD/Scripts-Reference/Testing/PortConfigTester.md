# PortConfigTester

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Testing/PortConfigTester.cs` |
| **Namespace** | `WOS.Testing` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 204 |
| **Architecture** | Port configuration validation and testing utility |

## Purpose

Simple validation tool for testing `PortConfigurationSO` functionality. Provides automatic movement testing, zone detection, and manual test methods for port protection zones.

## Configuration

### Test Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `portConfigToTest` | `PortConfigurationSO` | - | Port configuration to validate |
| `testPlayerTransform` | `Transform` | - | Test player position (auto-creates if null) |

### Test Results (Read-Only)

| Field | Type | Description |
|-------|------|-------------|
| `isInProtectionZone` | `bool` | Currently within protection zone |
| `isApproachingBoundary` | `bool` | Approaching protection boundary |
| `distanceFromPort` | `float` | Current distance from port center |

### Automatic Testing

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enableAutoTest` | `bool` | `false` | Automatically move test player in circle |
| `testRadius` | `float` | `1000f` | Circular test path radius |
| `testSpeed` | `float` | `50f` | Movement speed multiplier |

## Key Features

### Automatic Zone Testing

```csharp
// Circular movement pattern
if (enableAutoTest)
{
    testTime += Time.deltaTime * testSpeed * 0.01f;
    float x = Mathf.Cos(testTime) * testRadius;
    float y = Mathf.Sin(testTime) * testRadius;
    testPlayerTransform.position = new Vector3(x, y, 0f);
}

// Automatic logging on zone changes
"Protection zone ENTERED at distance 8500m"
"Approaching protection boundary at distance 9500m"
"Protection zone EXITED at distance 10100m"
```

### Configuration Validation

```csharp
// Validates PortConfigurationSO on Start
bool isValid = portConfig.ValidateConfiguration();
var stats = portConfig.GetPortStats();
// Logs validation results and port statistics
```

## Public API

### Context Menu Methods

#### `TestProtectionZone()`
```csharp
[ContextMenu("Test Protection Zone")]
public void TestProtectionZone()
```

Tests port configuration at multiple distances:
- Center (0m)
- Inside (50% radius)
- Near Boundary (90% radius)
- Just Outside (110% radius)
- Far Outside (200% radius)

**Output Example**:
```
Center: Distance=0m, InZone=True, Approaching=False
Inside: Distance=5000m, InZone=True, Approaching=False
Near Boundary: Distance=9000m, InZone=True, Approaching=True
Just Outside: Distance=11000m, InZone=False, Approaching=False
Far Outside: Distance=20000m, InZone=False, Approaching=False
```

#### `MovePlayerToCenter()`
```csharp
[ContextMenu("Move Test Player to Center")]
public void MovePlayerToCenter()
```

Instantly moves test player to port center.

#### `MovePlayerOutside()`
```csharp
[ContextMenu("Move Test Player Outside")]
public void MovePlayerOutside()
```

Moves test player outside protection zone (150% of radius).

## Usage Examples

### Basic Validation

```csharp
// 1. Create GameObject "PortTester"
// 2. Add PortConfigTester component
// 3. Assign PortConfigurationSO to test
// 4. Press Play
// 5. Right-click component → Test Protection Zone
```

### Automatic Movement Testing

```csharp
// Setup:
// 1. Enable enableAutoTest = true
// 2. Set testRadius = 12000 (for Tier 1 port with 10km radius)
// 3. Set testSpeed = 50
// 4. Press Play

// Result:
// - Test player orbits port in circular path
// - Crosses protection boundaries automatically
// - Logs zone transitions in real-time
```

### Manual Position Testing

```csharp
// Inspector Testing:
// 1. Select PortTester GameObject
// 2. Move testPlayerTransform in Scene view
// 3. Watch Test Results update in real-time
// 4. Check isInProtectionZone / isApproachingBoundary
```

## Integration Points

### Port Configuration

```csharp
// Tests PortConfigurationSO methods:
IsWithinProtectionZone(playerPosition, portPosition)
IsApproachingProtectionBoundary(playerPosition, portPosition)
ValidateConfiguration()
GetPortStats()
```

### DebugManager Integration

```csharp
// All logging uses DebugCategory.Environment
DebugManager.Log(DebugCategory.Environment,
    $"Port config validation: {isValid ? "PASSED" : "FAILED"}", this);
```

## Design Notes

### Auto-Creation of Test Player

```csharp
// If no test player assigned, creates one automatically
GameObject testPlayer = new GameObject("TestPlayer");
var renderer = testPlayer.AddComponent<SpriteRenderer>();
renderer.color = Color.red;
testPlayer.transform.position = new Vector3(1200f, 0f, 0f);
```

### Zone Transition Detection

```csharp
// State tracking for edge detection
bool wasInZone = isInProtectionZone;
bool wasApproaching = isApproachingBoundary;

// Log only on state change (prevents spam)
if (wasInZone != isInProtectionZone)
{
    DebugManager.Log(DebugCategory.Environment,
        $"Protection zone {(isInProtectionZone ? "ENTERED" : "EXITED")}");
}
```

### Visual Debugging

```csharp
// OnDrawGizmosSelected() shows:
Green Circle  → Protection Zone (GDD tier-based radius)
Yellow Circle → Warning Boundary
Green/Red Line → Connection to test player (status color)
Green Sphere  → Test player position (inside zone)
Red Sphere    → Test player position (outside zone)
```

## Troubleshooting

### Issue: No port config assigned
**Solution**: Assign `PortConfigurationSO` in Inspector

### Issue: Test player not created
**Solution**: Check console for errors, ensure scene has valid position

### Issue: Gizmos not visible
**Solution**: Select PortTester GameObject in Hierarchy

### Issue: Auto-test too fast/slow
**Solution**: Adjust `testSpeed` (50 = moderate, 10 = slow, 100 = fast)

## Testing Workflow

### Validation Test Checklist

1. ✅ Port config assigned
2. ✅ Validation passes on Start
3. ✅ Test Protection Zone shows correct results
4. ✅ Zone transitions log correctly
5. ✅ Gizmos display accurate radii

### Common Test Scenarios

#### Scenario 1: Tier 1 Port (10km radius)
```
testRadius = 12000 (120% of radius)
Expected: Player crosses boundary during orbit
```

#### Scenario 2: Tier 2 Port (25km radius)
```
testRadius = 30000 (120% of radius)
Expected: Longer orbit, clear zone transitions
```

#### Scenario 3: Tier 3 Port (50km radius)
```
testRadius = 60000 (120% of radius)
Expected: Very large orbit, extended protection
```

## Related Scripts

- **PortConfigurationSO**: Port configuration definition
- **SimplePortTest**: Full port entry/exit testing system
- **DebugManager**: Centralized logging system
