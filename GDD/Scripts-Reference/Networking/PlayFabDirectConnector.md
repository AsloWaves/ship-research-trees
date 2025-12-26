# PlayFabDirectConnector.cs

## Quick Reference

| **File** | PlayFabDirectConnector.cs |
|----------|--------------------------|
| **Namespace** | WOS.Networking |
| **Inheritance** | MonoBehaviour |
| **Lines** | 388 |
| **Architecture** | PlayFab Multiplayer Servers integration, KCP transport |

---

## Purpose

Direct connection to persistent PlayFab Multiplayer servers without auto-scaling matchmaking. Designed for persistent world MMO where servers are manually started/stopped.

**Use Case**:
- Admin manually deploys server to PlayFab (using Docker deployment script)
- Server runs persistently until manually stopped
- Clients query PlayFab to find the server IP and port
- Clients connect directly via Mirror/KCP

**Not for**:
- Auto-scaling matchmaking (use PlayFabMatchmaker instead)
- Session-based games with automatic server allocation

---

## Configuration

### Inspector Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `buildId` | string | `5d44ce16-261c-428b-83a2-e209cfa3b21e` | PlayFab Build ID from Game Manager |
| `buildAlias` | string | `` | Build Alias (e.g., 'latest', 'production') |
| `region` | string | `East US` | Preferred region (must match PlayFab region name exactly) |
| `enableDebugLogs` | bool | `true` | Enable verbose debug logging |

### Region Names

**Important**: Region name must match PlayFab exactly (case-sensitive with spaces):
- ✅ `East US`
- ❌ `EastUS` (won't work)
- ❌ `east us` (won't work)

---

## Public API

### Connection Methods

#### `FindAndConnectToServer()`
Finds and connects to a running server by querying PlayFab.

**Process**:
1. Query PlayFab for running servers (Build ID or Build Alias)
2. Find first Active or StandingBy server
3. Get server details (IP, ports)
4. Configure KCP transport with server IP and port
5. Start Mirror client connection

**Example**:
```csharp
PlayFabDirectConnector connector = GetComponent<PlayFabDirectConnector>();
connector.OnServerFound += (ip, port) =>
{
    Debug.Log($"Server found: {ip}:{port}");
};
connector.OnConnectionFailed += (error) =>
{
    Debug.LogError($"Connection failed: {error}");
};

connector.FindAndConnectToServer();
```

#### `CancelSearch()`
Cancels ongoing server search.

### Configuration Methods

#### `GetBuildId()` / `SetBuildId(string newBuildId)`
Gets/sets the PlayFab Build ID.

#### `GetBuildAlias()` / `SetBuildAlias(string newAlias)`
Gets/sets the Build Alias.

#### `GetRegion()` / `SetRegion(string newRegion)`
Gets/sets the preferred region.

#### `IsSearching()`
Returns `bool` - True if server search is in progress.

---

## Events

### `OnServerFound(string ip, int port)`
Fired when a running server is found.

**Parameters**:
- `ip` - Server IPv4 address
- `port` - Game port number

### `OnConnectionFailed(string errorMessage)`
Fired when server search or connection fails.

**Parameters**:
- `errorMessage` - Human-readable error description

---

## PlayFab Integration

### Server Discovery Workflow

```
1. Client calls FindAndConnectToServer()
   ↓
2. PlayFabMultiplayerAPI.ListMultiplayerServers(buildId, region)
   ↓
3. Parse response: Find Active or StandingBy servers
   ↓
4. PlayFabMultiplayerAPI.GetMultiplayerServerDetails(serverId)
   ↓
5. Extract IP and port from server details
   ↓
6. Configure KCP transport and connect via Mirror
```

### Server State Priority

When multiple servers are found, preference order:
1. **Active** servers (already has session, persistent world)
2. **StandingBy** servers (if no Active servers found)

**Other states ignored**:
- Terminating
- Terminated
- Unhealthy

### Port Selection

Port selection priority:
1. Port named `game_port`
2. Any UDP port
3. First port in list (fallback)

---

## Configuration Setup

### PlayFab Game Manager Setup

1. **Create Build**:
   - Go to PlayFab Game Manager → Multiplayer → Servers → Builds
   - Create new build with your server Docker container
   - Note the Build ID (e.g., `5d44ce16-261c-428b-83a2-e209cfa3b21e`)

2. **Configure Ports**:
   - Add port mapping: Name=`game_port`, Number=`7777`, Protocol=`UDP`
   - This is your Mirror/KCP game port

3. **Deploy Server**:
   - Manually allocate server in desired region
   - Server will show as "StandingBy" or "Active"

4. **Client Setup**:
   - Set `buildId` in PlayFabDirectConnector Inspector
   - Set `region` to match server deployment (exact spelling)
   - Build client with PlayFab Client SDK

### Scripting Define Symbols

**Required**: Add `ENABLE_PLAYFABCLIENT_API` to Scripting Define Symbols in Player Settings.

Without this symbol:
- PlayFab Client SDK is disabled
- FindAndConnectToServer() will log error and fail

---

## Debug Logging

When `enableDebugLogs = true`, detailed logs are generated:

```
[PlayFabDirectConnector] 🔍 DEBUG: ===== QUERY RUNNING SERVERS =====
[PlayFabDirectConnector] 🔍 Timestamp: 2025-01-15 14:30:00.123 UTC
[PlayFabDirectConnector] 🔍 Build ID: 5d44ce16-261c-428b-83a2-e209cfa3b21e
[PlayFabDirectConnector] 🔍 Region: East US
[PlayFabDirectConnector] 🔍 Querying PlayFab for running servers...
[PlayFabDirectConnector] 🔍 Query completed in 250.50ms
[PlayFabDirectConnector] 🔍 Found 2 server(s)
[PlayFabDirectConnector] ✅ Selected Active server: SERVER_ID_HERE
[PlayFabDirectConnector] 🔍 IPv4 Address: 40.112.72.123
[PlayFabDirectConnector] 🔍 Ports (1):
[PlayFabDirectConnector] 🔍   game_port = 7777 (Protocol: UDP)
[PlayFabDirectConnector] ✅ Connecting to: 40.112.72.123:7777
```

---

## Error Handling

### Common Errors

**No servers found**:
```
⚠️ No servers found for this build/region!
⚠️ Make sure:
⚠️   1. Server is running in PlayFab Game Manager
⚠️   2. Build ID matches deployed server
⚠️   3. Region matches (case-sensitive with spaces!)
```

**PlayFab SDK not available**:
```
❌ PlayFab Client SDK not available. Install PlayFab SDK and add ENABLE_PLAYFABCLIENT_API to Scripting Define Symbols.
```

**Invalid server details**:
```
❌ Server details missing IP or ports!
```

---

## Usage Example

### Complete Connection Flow

```csharp
using UnityEngine;
using WOS.Networking;

public class DirectConnectionExample : MonoBehaviour
{
    private PlayFabDirectConnector connector;

    void Start()
    {
        connector = GetComponent<PlayFabDirectConnector>();

        // Subscribe to events
        connector.OnServerFound += HandleServerFound;
        connector.OnConnectionFailed += HandleConnectionFailed;

        // Configure (optional, can also set in Inspector)
        connector.SetBuildId("5d44ce16-261c-428b-83a2-e209cfa3b21e");
        connector.SetRegion("East US");

        // Start search
        connector.FindAndConnectToServer();
    }

    private void HandleServerFound(string ip, int port)
    {
        Debug.Log($"Connecting to server: {ip}:{port}");
        // Mirror NetworkManager will handle the actual connection
    }

    private void HandleConnectionFailed(string error)
    {
        Debug.LogError($"Failed to find server: {error}");
        // Show error UI to player
    }

    void OnDestroy()
    {
        if (connector != null)
        {
            connector.OnServerFound -= HandleServerFound;
            connector.OnConnectionFailed -= HandleConnectionFailed;
        }
    }
}
```

---

## Design Notes

### Persistent World Architecture

This connector is designed for persistent world MMO gameplay:

**Traditional Matchmaking** (not this):
```
Client requests match → PlayFab allocates server → Client connects → Session ends → Server terminated
```

**Persistent World** (this):
```
Admin deploys server → Server runs 24/7 → Clients query and connect → Server persists player data
```

### vs. PlayFabMatchmaker

| Feature | PlayFabDirectConnector | PlayFabMatchmaker |
|---------|----------------------|------------------|
| **Use Case** | Persistent world MMO | Session-based games |
| **Server Lifecycle** | Manually started/stopped | Auto-allocated per match |
| **Player Count** | Massive (100+) | Small groups (2-32) |
| **Server Persistence** | Runs 24/7 | Terminates after session |
| **Cost Model** | Fixed hourly rate | Pay per session |

### KCP Transport Integration

The connector automatically configures KCP transport:

```csharp
var kcpTransport = networkManager.GetComponent<kcp2k.KcpTransport>();
if (kcpTransport != null)
{
    kcpTransport.Port = (ushort)port; // Set from PlayFab server details
}
networkManager.networkAddress = ip; // Set from PlayFab server details
networkManager.StartClient(); // Start Mirror client connection
```

**Port Configuration**:
- Server must expose UDP port (default 7777)
- PlayFab port mapping: `game_port` → `7777` (UDP)
- KCP transport configured automatically from PlayFab response

---

## Key Takeaways

1. **Persistent Servers**: Designed for manually-deployed, long-running servers
2. **Direct Connection**: No matchmaking, clients query and connect directly
3. **PlayFab Integration**: Uses PlayFab Multiplayer Servers API for discovery
4. **Region-Specific**: Clients connect to servers in specific regions
5. **KCP Transport**: Automatically configures Mirror's KCP transport
6. **Debug-Friendly**: Comprehensive logging for troubleshooting connections
