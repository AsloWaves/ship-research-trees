---
tags: [script, networking, mirror, core, implemented]
script-type: NetworkManager
namespace: WOS.Networking
file-path: Assets/Scripts/Networking/WOSNetworkManager.cs
status: IMPLEMENTED
size: ~18 KB (612 lines)
feature-group: networking
---

# WOSNetworkManager.cs

## Quick Reference
**Type**: NetworkManager (Mirror)
**Namespace**: WOS.Networking
**File**: `Assets/Scripts/Networking/WOSNetworkManager.cs`
**Size**: ~18 KB (612 lines)
**Dependencies**: Mirror, KcpTransport, PlayFabServerManager

---

## Purpose
Custom Mirror NetworkManager for WOS multiplayer. Extends Mirror's base NetworkManager with WOS-specific features including PlayFab integration, scene management, and player lifecycle handling.

This is the **central networking orchestrator** that manages:
- Server and client connection lifecycle
- Player spawning and despawning
- Scene transitions with Mirror active
- PlayFab GSDK integration callbacks
- Transport configuration (KCP)
- Connection authentication flow

---

## Key Components

### Singleton Access
```csharp
public static WOSNetworkManager Instance => singleton as WOSNetworkManager;
```

### Public Properties
```csharp
public bool IsServerOnly { get; }      // Running as dedicated server
public bool IsClientOnly { get; }      // Running as client
public bool IsHost { get; }            // Running as host (server + client)
public int PlayerCount { get; }        // Current connected players
```

### Public Methods
- `StartGameServer()` - Start as dedicated server
- `StartGameClient(string address, ushort port)` - Connect to server
- `StartGameHost()` - Start as host
- `DisconnectAndReturnToMenu()` - Clean disconnect with scene change
- `GetPlayerByNetId(uint netId)` - Get player by network ID

---

## Configuration

### Inspector Fields
```
[Header("Scene Configuration")]
mainMenuScene (string): Scene to load on disconnect
oceanScene (string): Main gameplay scene
harborScene (string): Port/harbor scene

[Header("Server Settings")]
maxConnections (int, 100): Maximum simultaneous players
serverTickRate (int, 60): Server update rate

[Header("Transport")]
kcpTransport (KcpTransport): KCP transport reference

[Header("Player Management")]
playerPrefab (GameObject): Player ship prefab

[Header("Debug")]
enableDebugLogs (bool): Enable networking debug logs
```

---

## Server Lifecycle

### OnStartServer
```csharp
public override void OnStartServer()
{
    base.OnStartServer();

    // Notify PlayFab GSDK if running on PlayFab infrastructure
    PlayFabServerManager.NotifyMirrorSceneChanged(SceneManager.GetActiveScene().name);

    // Register server message handlers
    NetworkServer.RegisterHandler<AuthRequestMessage>(OnAuthRequest);

    DebugManager.Log(DebugCategory.Networking,
        $"[WOSNetworkManager] Server started on port {transport.ServerUri().Port}");
}
```

### OnStopServer
```csharp
public override void OnStopServer()
{
    // Save all player data before shutdown
    SaveAllPlayerData();

    // Clear player registry
    connectedPlayers.Clear();

    base.OnStopServer();
}
```

---

## Client Lifecycle

### OnClientConnect
```csharp
public override void OnClientConnect()
{
    base.OnClientConnect();

    // Send authentication request with PlayFab session ticket
    var authRequest = new AuthRequestMessage
    {
        PlayFabId = AuthenticationManager.Instance.PlayFabId,
        SessionTicket = AuthenticationManager.Instance.SessionTicket
    };
    NetworkClient.Send(authRequest);
}
```

### OnClientDisconnect
```csharp
public override void OnClientDisconnect()
{
    base.OnClientDisconnect();

    // Return to main menu on disconnect
    SceneManager.LoadScene(mainMenuScene);
}
```

---

## Player Spawning

### OnServerAddPlayer
```csharp
public override void OnServerAddPlayer(NetworkConnectionToClient conn)
{
    // Get player's PlayFab data
    string playFabId = connectionPlayFabIds[conn.connectionId];

    // Load player ship data
    var shipData = await PlayFabShipService.Instance.LoadShipCollection(playFabId);

    // Spawn player ship
    GameObject player = Instantiate(playerPrefab, GetSpawnPosition(), Quaternion.identity);
    NetworkServer.AddPlayerForConnection(conn, player);

    // Initialize player systems
    var shipManager = player.GetComponent<PlayerShipManager>();
    shipManager.InitializeFromData(shipData);

    // Report to PlayFab GSDK
    PlayFabServerManager.Instance?.OnPlayerConnected(playFabId);
}
```

### OnServerDisconnect
```csharp
public override void OnServerDisconnect(NetworkConnectionToClient conn)
{
    // Save player data before removing
    var player = conn.identity?.GetComponent<PlayerShipManager>();
    if (player != null)
    {
        player.SaveAllData();
    }

    // Report to PlayFab GSDK
    PlayFabServerManager.Instance?.OnPlayerDisconnected(playFabId);

    base.OnServerDisconnect(conn);
}
```

---

## Scene Management

### ServerChangeScene
Override to notify PlayFab GSDK of scene changes:

```csharp
public override void ServerChangeScene(string newSceneName)
{
    base.ServerChangeScene(newSceneName);

    // Notify PlayFab GSDK (critical for ReadyForPlayers)
    PlayFabServerManager.NotifyMirrorSceneChanged(newSceneName);
}
```

---

## Authentication Flow

### Server-Side Validation
```csharp
private void OnAuthRequest(NetworkConnectionToClient conn, AuthRequestMessage msg)
{
    // Validate session ticket with PlayFab
    AuthenticationManager.Instance.ValidateSessionTicket(msg.SessionTicket,
        success =>
        {
            if (success)
            {
                // Store mapping and allow player to spawn
                connectionPlayFabIds[conn.connectionId] = msg.PlayFabId;
                OnServerReady(conn);
            }
            else
            {
                // Reject connection
                conn.Disconnect();
            }
        });
}
```

---

## Transport Configuration

Uses KCP (UDP-based reliable transport):
```csharp
private void ConfigureTransport()
{
    if (kcpTransport == null) return;

    kcpTransport.Port = serverConfig.GetServerPort();
    kcpTransport.DualMode = true;  // IPv4 + IPv6
    kcpTransport.NoDelay = true;   // Low latency
    kcpTransport.Interval = 10;    // 10ms update interval
}
```

---

## Integration Points

### Dependencies
- **Mirror** - NetworkManager base class
- **KcpTransport** - UDP transport layer
- [[PlayFabServerManager]] - GSDK lifecycle
- [[AuthenticationManager]] - Session validation

### Used By
- **MainMenu** - Connection initiation
- [[PlayerShipManager]] - Player lifecycle
- [[ServerBrowserManager]] - Server discovery

---

## Network Messages

### AuthRequestMessage
```csharp
public struct AuthRequestMessage : NetworkMessage
{
    public string PlayFabId;
    public string SessionTicket;
}
```

### AuthResponseMessage
```csharp
public struct AuthResponseMessage : NetworkMessage
{
    public bool Success;
    public string ErrorMessage;
}
```

---

## Related Files
- [[ServerConfig]] - Server address configuration
- [[PlayFabServerManager]] - PlayFab GSDK integration
- [[AuthenticationManager]] - Client authentication
- [[PlayerSpawnMethod]] - Spawn position logic

---

## Testing Notes
- Use H key in Editor for DevHostStarter
- ServerChangeScene notifies PlayFab GSDK
- KCP transport for reliable UDP
- Max 100 connections default

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added PlayFab GSDK integration
- **2025-01**: Added authentication flow

