---
tags: [script, networking, playfab, gsdk, server, implemented]
script-type: MonoBehaviour (Singleton)
namespace: WOS.Networking.Managers
file-path: Assets/Scripts/Networking/Managers/PlayFabServerManager.cs
status: IMPLEMENTED
size: ~24 KB (831 lines)
feature-group: networking
---

# PlayFabServerManager.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Networking.Managers
**File**: `Assets/Scripts/Networking/Managers/PlayFabServerManager.cs`
**Size**: ~24 KB (831 lines)
**Dependencies**: PlayFab GSDK, Mirror, DebugManager

---

## Purpose
Manages PlayFab Multiplayer Servers (MPS) GSDK integration. Handles server lifecycle, heartbeats, player tracking, and graceful shutdown. Only active when running as a dedicated server on PlayFab infrastructure.

This is the **PlayFab server coordinator** that manages:
- GSDK initialization and heartbeat communication
- Server ready state signaling
- Player connection/disconnection reporting
- Maintenance and shutdown callbacks
- Health monitoring
- Diagnostic logging

---

## Key Components

### Singleton Access
```csharp
public static PlayFabServerManager Instance { get; }
```

### Public Methods
- `OnPlayerConnected(string playerId)` - Report player connection to PlayFab
- `OnPlayerDisconnected(string playerId)` - Report player disconnection
- `IsPlayFabServer()` - Check if running under PlayFab GSDK
- `IsServerReady()` - Check if server has signaled ready
- `GetServerId()` - Get PlayFab server ID
- `GetSessionId()` - Get current session ID

### Static Methods
- `NotifyMirrorSceneChanged(string sceneName)` - Called by WOSNetworkManager on scene change

---

## GSDK Lifecycle

### Step 1: Awake - Environment Detection
```csharp
private void Awake()
{
    // Ensure root GameObject for DontDestroyOnLoad
    if (transform.parent != null)
        transform.SetParent(null);

    DontDestroyOnLoad(gameObject);

    // Check for PlayFab environment
    bool isPlayFabEnvironment = !string.IsNullOrEmpty(
        Environment.GetEnvironmentVariable("GSDK_CONFIG_FILE"));

    if (isPlayFabEnvironment)
    {
        InitializePlayFabServer();
    }
}
```

### Step 2: GSDK Initialization
```csharp
private void InitializePlayFabServer()
{
    // Start GSDK heartbeat communication
    PlayFabMultiplayerAgentAPI.Start();
    isPlayFabServer = true;

    // Register lifecycle callbacks
    PlayFabMultiplayerAgentAPI.OnMaintenanceCallback += OnMaintenance;
    PlayFabMultiplayerAgentAPI.OnShutDownCallback += OnShutdown;
    PlayFabMultiplayerAgentAPI.OnServerActiveCallback += OnServerActive;

    // Start ready coroutine
    StartCoroutine(ReadyForPlayersCoroutine());
}
```

### Step 3: Ready for Players
```csharp
private IEnumerator ReadyForPlayersCoroutine()
{
    // Wait for server initialization (0.5 seconds)
    yield return new WaitForSeconds(readyDelaySeconds);

    // Signal PlayFab that server is ready
    PlayFabMultiplayerAgentAPI.ReadyForPlayers();
    isServerReady = true;
}
```

### Step 4: Server Active
```csharp
private void OnServerActive()
{
    // Server is now accepting connections
    var sessionConfig = PlayFabMultiplayerAgentAPI.GetGameServerConnectionInfo();
    // Log port configuration
}
```

---

## Player Tracking

### OnPlayerConnected
```csharp
public void OnPlayerConnected(string playerId)
{
    if (!isPlayFabServer) return;

    connectedPlayers.Add(new ConnectedPlayer(playerId));
    PlayFabMultiplayerAgentAPI.UpdateConnectedPlayers(connectedPlayers);
}
```

### OnPlayerDisconnected
```csharp
public void OnPlayerDisconnected(string playerId)
{
    if (!isPlayFabServer) return;

    connectedPlayers.RemoveAll(p => p.PlayerId == playerId);
    PlayFabMultiplayerAgentAPI.UpdateConnectedPlayers(connectedPlayers);
}
```

---

## Lifecycle Callbacks

### OnMaintenance
Called when PlayFab schedules maintenance:
```csharp
private void OnMaintenance(DateTime? nextScheduledMaintenanceUtc)
{
    // Log maintenance window
    // Optional: Implement player migration
}
```

### OnShutdown
Called when PlayFab requests server shutdown:
```csharp
private void OnShutdown()
{
    StartCoroutine(GracefulShutdownCoroutine());
}

private IEnumerator GracefulShutdownCoroutine()
{
    // 1. Disconnect all players
    foreach (var conn in NetworkServer.connections.Values)
    {
        conn?.Disconnect();
    }
    yield return new WaitForSeconds(2f);

    // 2. Stop Mirror server
    NetworkManager.singleton.StopServer();
    yield return new WaitForSeconds(1f);

    // 3. Quit application
    Application.Quit();
}
```

---

## Mirror Integration

### Scene Change Notification
Critical for PlayFab to know when server scene has loaded:

```csharp
public static void NotifyMirrorSceneChanged(string sceneName)
{
    if (Instance == null)
    {
        // Fallback: Try to find instance
        Instance = FindFirstObjectByType<PlayFabServerManager>();
    }

    if (Instance.isPlayFabServer && !Instance.isServerReady)
    {
        Instance.HandleMirrorSceneChanged(sceneName);
    }
}

private void HandleMirrorSceneChanged(string sceneName)
{
    // Restart ReadyForPlayers coroutine
    StopCoroutine(nameof(ReadyForPlayersCoroutine));
    StartCoroutine(ReadyForPlayersCoroutine());
}
```

---

## Health Monitoring

### IsServerHealthy (Future GSDK Support)
```csharp
private bool IsServerHealthy()
{
    // Check 1: Mirror server active
    if (!NetworkServer.active) return false;

    // Check 2: Under max capacity
    int currentPlayers = NetworkServer.connections.Count;
    int maxPlayers = NetworkManager.singleton.maxConnections;
    if (currentPlayers >= maxPlayers) return false;

    return true;
}
```

---

## Diagnostic Logging

### Environment Variables
Logs PlayFab environment variables on startup:
- `GSDK_CONFIG_FILE` - GSDK config path
- `PF_SERVER_ID` - Server instance ID
- `PF_REGION` - Deployment region
- `PF_BUILD_ID` - Build ID
- `PF_TITLE_ID` - PlayFab Title ID

### Heartbeat Logging
Periodic (10s) heartbeat state logging:
- Build ID
- Session ID
- Player count
- Network active state
- Ready state

---

## Preprocessor Directives

```csharp
#if ENABLE_PLAYFABSERVER_API
// PlayFab GSDK code
#endif
```

Add `ENABLE_PLAYFABSERVER_API` to Player Settings > Scripting Define Symbols for server builds.

---

## Integration Points

### Dependencies
- **PlayFab.MultiplayerAgent** - GSDK API
- **Mirror** - NetworkServer, NetworkManager
- [[DebugManager]] - Logging

### Used By
- [[WOSNetworkManager]] - Notifies scene changes
- **Server Builds** - Runs on PlayFab VMs

---

## Related Files
- [[WOSNetworkManager]] - Calls NotifyMirrorSceneChanged
- [[AuthenticationManager]] - Player validation
- [[ServerConfig]] - Server configuration

---

## Testing Notes
- Requires GSDK_CONFIG_FILE environment variable
- Use LocalMultiplayerAgent for local testing
- DontDestroyOnLoad requires root GameObject
- 0.5 second delay before ReadyForPlayers

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added scene change notification
- **2025-01**: Added diagnostic logging

