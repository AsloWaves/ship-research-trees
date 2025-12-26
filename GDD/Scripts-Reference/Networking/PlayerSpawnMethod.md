# PlayerSpawnMethod.cs

## Quick Reference

| **File** | PlayerSpawnMethod.cs |
|----------|---------------------|
| **Namespace** | WOS.Networking |
| **Type** | Enum |
| **Lines** | 15 |
| **Architecture** | Spawn configuration enum |

---

## Purpose

Defines spawn method for players joining the server. Controls where players initially appear when connecting to the game world.

**GDD Rule**: Players should start in Port, not open ocean.

---

## Enum Values

```csharp
public enum PlayerSpawnMethod
{
    Random,      // Randomly select from available ocean spawn points
    RoundRobin,  // Cycle through ocean spawn points sequentially
    Specific,    // Use a specific spawn point
    PortSpawn    // Spawn in port (GDD default - players start in port)
}
```

### Value Descriptions

| Value | Description | Use Case |
|-------|-------------|----------|
| `Random` | Randomly select from available ocean spawn points | Open world PvP zones |
| `RoundRobin` | Cycle through ocean spawn points sequentially | Distributed ocean spawning |
| `Specific` | Use a specific spawn point | Tutorial, special events |
| `PortSpawn` | Spawn in port (GDD default) | **Default starting location** |

---

## Usage

### In WOSNetworkManager

```csharp
public class WOSNetworkManager : NetworkManager
{
    [SerializeField] private PlayerSpawnMethod spawnMethod = PlayerSpawnMethod.PortSpawn;

    public override void OnServerAddPlayer(NetworkConnectionToClient conn)
    {
        Vector3 spawnPosition;
        Quaternion spawnRotation;

        switch (spawnMethod)
        {
            case PlayerSpawnMethod.PortSpawn:
                spawnPosition = GetPortSpawnPosition();
                spawnRotation = GetPortSpawnRotation();
                break;

            case PlayerSpawnMethod.Random:
                spawnPosition = GetRandomOceanSpawnPosition();
                spawnRotation = Quaternion.identity;
                break;

            case PlayerSpawnMethod.RoundRobin:
                spawnPosition = GetNextOceanSpawnPosition();
                spawnRotation = Quaternion.identity;
                break;

            case PlayerSpawnMethod.Specific:
                spawnPosition = specificSpawnPoint.position;
                spawnRotation = specificSpawnPoint.rotation;
                break;

            default:
                spawnPosition = Vector3.zero;
                spawnRotation = Quaternion.identity;
                break;
        }

        GameObject player = Instantiate(playerPrefab, spawnPosition, spawnRotation);
        NetworkServer.AddPlayerForConnection(conn, player);
    }
}
```

---

## Design Notes

### GDD Compliance

**Game Design Document Rule**: Players start in Port, not open ocean.

**Rationale**:
- Safe starting environment (no immediate combat)
- Tutorial and onboarding opportunity
- Social hub for new players
- Prevents new players from spawning in dangerous areas

### Spawn Method Selection

| Spawn Method | Player Safety | Tutorial Support | PvP Risk | Social Interaction |
|--------------|--------------|------------------|----------|-------------------|
| `PortSpawn` | ✅ High | ✅ Yes | ❌ None | ✅ High |
| `Random` | ❌ Low | ❌ No | ✅ High | ❌ Low |
| `RoundRobin` | ❌ Low | ❌ No | ✅ Medium | ❌ Low |
| `Specific` | ⚠️ Variable | ✅ Yes | ⚠️ Variable | ⚠️ Variable |

### Recommended Configuration

**Default**: `PlayerSpawnMethod.PortSpawn`

**Exceptions**:
- PvP events: `Random` or `RoundRobin`
- Tutorial zones: `Specific`
- Special game modes: Custom spawn logic

---

## Integration Points

### PortZone System

When using `PortSpawn`, integrate with PortZone system:

```csharp
private Vector3 GetPortSpawnPosition()
{
    // Find available port spawn point
    var portZone = PortZone.GetDefaultSpawnPort();
    if (portZone != null)
    {
        return portZone.GetSpawnPosition();
    }

    // Fallback to default position
    return Vector3.zero;
}
```

### Spawn Point Management

When using `Random` or `RoundRobin`, manage spawn points:

```csharp
[SerializeField] private Transform[] oceanSpawnPoints;
private int currentSpawnIndex = 0;

private Vector3 GetRandomOceanSpawnPosition()
{
    int index = Random.Range(0, oceanSpawnPoints.Length);
    return oceanSpawnPoints[index].position;
}

private Vector3 GetNextOceanSpawnPosition()
{
    Vector3 position = oceanSpawnPoints[currentSpawnIndex].position;
    currentSpawnIndex = (currentSpawnIndex + 1) % oceanSpawnPoints.Length;
    return position;
}
```

---

## Key Takeaways

1. **GDD Default**: `PortSpawn` is the recommended default (safe starting environment)
2. **Flexible Options**: Supports ocean spawning for PvP and special events
3. **Simple Enum**: Easy to configure in Inspector
4. **Integration Ready**: Works with PortZone system and custom spawn logic
