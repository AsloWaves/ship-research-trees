---
tags: [script, networking, server-browser, implemented]
script-type: MonoBehaviour
namespace: WOS.Networking
file-path: Assets/Scripts/Networking/ServerBrowserManager.cs
status: IMPLEMENTED
size: ~14 KB (503 lines)
feature-group: networking
---

# ServerBrowserManager.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Networking
**File**: `Assets/Scripts/Networking/ServerBrowserManager.cs`
**Size**: ~14 KB (503 lines)
**Dependencies**: UnityWebRequest, ServerConfig

---

## Purpose
Secure server browser that fetches server list from backend API. Backend handles API communication with tokens server-side. Provides server list with player counts, ping, health status, and automatic best server selection.

**Security**: No API tokens in Unity client.

---

## Architecture

```
Unity Client → Your Backend API → Edgegap/PlayFab API
              ↓
         Server List with Health Status
```

---

## Configuration

### Inspector Fields
```csharp
[Header("Backend Configuration")]
backendApiUrl (string): Backend API URL (NOT Edgegap)
fallbackConfig (ServerConfig): Fallback if backend unavailable

[Header("Local Testing")]
skipBackendForLocalTesting (bool): Disable network calls for UI testing

[Header("Settings")]
apiTimeout (float, 10): Normal request timeout
coldStartTimeout (float, 90): First request timeout (serverless wake)
maxRetries (int, 3): Retry attempts
retryDelay (float, 5): Base retry delay
autoRefreshInterval (float, 30): Auto-refresh seconds (0 = manual)
```

---

## Events

```csharp
public event Action<List<ServerInfo>> OnServersUpdated;
public event Action<string> OnError;
public event Action<string> OnStatusUpdate;  // UI status messages
```

---

## Public Methods

### RefreshServers
Fetches server list from backend.

```csharp
public void RefreshServers(bool forceRefresh = false)
```

### GetBestServer
Returns healthiest server with most players and lowest ping.

```csharp
public ServerInfo GetBestServer()
```

### GetAllServers
Returns copy of server list.

```csharp
public List<ServerInfo> GetAllServers()
```

### GetServerById
Gets specific server by ID.

```csharp
public ServerInfo GetServerById(string serverId)
```

---

## Server Discovery Flow

```
1. Build API URL: {backendApiUrl}/api/servers
2. Make request with timeout (longer for first request)
3. On success → parse JSON → update server list → fire event
4. On failure → retry with exponential backoff
5. After max retries → try fallback config
```

---

## Cold Start Handling

First request uses longer timeout for serverless cold start:
- Normal timeout: 10s
- Cold start timeout: 90s

Status messages inform user:
- "Waking up server... (attempt 1/3)"
- "Server may be waking up from sleep (can take 30-60s)"

---

## Retry Logic

Exponential backoff:
```
Attempt 1: Immediate
Attempt 2: 5s delay (retryDelay × 2^0)
Attempt 3: 10s delay (retryDelay × 2^1)
```

---

## Fallback System

When backend unavailable after all retries:

```csharp
private IEnumerator TryFallbackConfig()
```

1. Check fallbackConfig assigned
2. Create ServerInfo from ServerConfig
3. Validate health via HTTP endpoint
4. Add to server list if healthy
5. Fire OnServersUpdated or OnError

---

## Health Validation

Validates fallback server health:

```csharp
private IEnumerator ValidateServerHealth(ServerInfo server)
```

**Endpoint**: `http://{ip}:{healthPort}/health`

**Parses**:
- Player count
- Max players
- Response time (ping)

---

## Auto-Refresh

When `autoRefreshInterval > 0`:
- Initial fetch on Start()
- Refresh every N seconds
- Runs in coroutine loop

---

## Data Models

### ServerInfo
```csharp
public string serverId;
public string serverName;
public string ipAddress;
public int port;
public int healthPort;
public string region;
public string city;
public string country;
public int currentPlayers;
public int maxPlayers;
public int pingMs;
public bool isHealthy;
public string status;
public string[] tags;
```

**Methods**:
- `GetConnectionAddress()` → "IP:Port"
- `GetDisplayName()` → "City (5/100 players) - 45ms"

### ServerListResponse
```csharp
public List<ServerInfo> servers;
```

Wrapper for JSON array deserialization.

### HealthCheckResponse
```csharp
public string status;
public string server;
public int players;
public int maxPlayers;
public int uptime;
public long timestamp;
```

---

## Local Testing Mode

When `skipBackendForLocalTesting = true`:
- Skips all backend/server checks
- Logs that testing mode is active
- Useful for UI development without server

---

## Best Server Selection

```csharp
public ServerInfo GetBestServer()
```

Selection criteria (backend pre-sorts):
1. Health (healthy first)
2. Player count (most players = active)
3. Ping (lowest latency)

---

## Status Tracking

```csharp
[SerializeField] private bool isFetching;
[SerializeField] private int serversFound;
[SerializeField] private int healthyServers;
[SerializeField] private string lastError;
```

Visible in Inspector for debugging.

---

## Integration Points

### Dependencies
- [[ServerConfig]] - Fallback configuration
- Backend API (external)

### Used By
- [[JoinMenuController]] - Server selection UI
- Main menu systems

---

## Logging

Uses DebugManager with emojis:
- 🌐 Initialization
- 🔄 Fetching
- ⏳ Cold start / retry waiting
- ✅ Success
- ⚠️ Warning
- ❌ Error
- ⏭️ Skipped (testing mode)
- 🎯 Best server selection
- ℹ️ Info

---

## Related Files
- [[VercelServerDiscovery]] - Individual server discovery
- [[PlayFabCloudScriptDiscovery]] - CloudScript discovery
- [[ServerConfig]] - Fallback configuration
- [[JoinMenuController]] - UI integration

---

## Testing Notes
- Backend cold start can take 30-60s
- Fallback requires ServerConfig in Inspector
- Auto-refresh runs in background
- skipBackendForLocalTesting for UI work
- Health check on port 8080 default

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added cold start handling
- **2025-01**: Added exponential backoff retry
- **2025-01**: Added local testing mode
- **2025-01**: Added health validation for fallback

