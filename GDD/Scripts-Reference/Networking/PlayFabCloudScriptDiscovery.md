---
tags: [script, networking, playfab, cloudscript, discovery, implemented]
script-type: MonoBehaviour
namespace: WOS.Networking
file-path: Assets/Scripts/Networking/PlayFabCloudScriptDiscovery.cs
status: IMPLEMENTED
size: ~5 KB (190 lines)
feature-group: networking
---

# PlayFabCloudScriptDiscovery.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Networking
**File**: `Assets/Scripts/Networking/PlayFabCloudScriptDiscovery.cs`
**Size**: ~5 KB (190 lines)
**Dependencies**: PlayFab Client SDK

---

## Purpose
Discovers active PlayFab MPS servers using native PlayFab CloudScript. Calls a CloudScript function that queries MPS infrastructure server-side. No external backend required.

---

## Architecture

```
Unity Client → PlayFab CloudScript → PlayFab MPS API
```

- Client executes CloudScript function
- CloudScript runs server-side in PlayFab
- Queries MPS for active servers
- Returns connection info to client

---

## Configuration

### Inspector Fields
```csharp
[Header("Discovery Configuration")]
buildAlias (string, "latest"): Build to search ("latest", "stable", "beta")
enableDebugLogs (bool, true): Enable debug logging
```

---

## CloudScript Function

**Function Name**: `GetServerByAlias`

**Parameters**:
```javascript
{ buildAlias: "latest" }
```

**Expected Return**:
```json
{
    "success": true,
    "ip": "123.45.67.89",
    "port": 7777,
    "sessionId": "abc-123",
    "region": "EastUS",
    "buildId": "build-xyz",
    "state": "Active"
}
```

---

## Events

```csharp
public Action<ServerConnectionInfo> OnServerDiscovered;
public Action<string> OnDiscoveryFailed;
```

---

## Public Methods

### DiscoverServer
Initiates server discovery.

```csharp
public void DiscoverServer()
```

**Behavior**:
- Returns early if discovery in progress
- Executes CloudScript function
- Handles success/error callbacks
- Fires appropriate event

---

## Execution Flow

```
1. DiscoverServer() called
2. ExecuteCloudScriptRequest created
3. PlayFabClientAPI.ExecuteCloudScript()
4. OnCloudScriptSuccess() or OnCloudScriptError()
5. Parse result → validate → fire event
```

---

## Response Handling

### Success Path
1. Check `result.Error` for CloudScript execution errors
2. Check `result.FunctionResult` not null
3. Parse JSON to `CloudScriptServerResult`
4. Validate `success == true`
5. Validate IP and port
6. Create `ServerConnectionInfo`
7. Fire `OnServerDiscovered`

### Error Path
- CloudScript execution error → fire OnDiscoveryFailed
- Null result → fire OnDiscoveryFailed
- API error → log details and fire OnDiscoveryFailed

---

## Data Classes

### CloudScriptServerResult
```csharp
public bool success;
public string error;
public string ip;
public int port;
public string sessionId;
public string region;
public string state;
public string buildId;
public string vmId;
```

### ServerConnectionInfo
```csharp
public string ip;
public int port;
public string sessionId;
public string region;
public string buildId;
public string state;
```

---

## Debug Logging

When `enableDebugLogs` is true, logs:
- CloudScript execution time
- API requests issued
- CloudScript logs (if any)
- Server details on success
- Error details on failure

---

## PlayFab Integration

Uses `PlayFabClientAPI.ExecuteCloudScript()`:
```csharp
var request = new ExecuteCloudScriptRequest
{
    FunctionName = "GetServerByAlias",
    FunctionParameter = new { buildAlias = buildAlias },
    GeneratePlayStreamEvent = false  // No analytics events
};
```

---

## Comparison with VercelServerDiscovery

| Feature | CloudScript | Vercel |
|---------|-------------|--------|
| Backend | PlayFab (built-in) | External Vercel |
| Setup | CloudScript only | Vercel + Code |
| Auth | PlayFab session | None |
| Cost | PlayFab limits | Vercel limits |
| Latency | Higher | Lower |
| Retry | None built-in | Exponential backoff |

---

## Integration Points

### Used By
- [[ServerBrowserManager]] - Alternative discovery
- Main menu quick join

### Dependencies
- PlayFab Client SDK
- Active PlayFab session

---

## Related Files
- [[VercelServerDiscovery]] - HTTP-based alternative
- [[ServerBrowserManager]] - Server list management
- [[AuthenticationManager]] - Required for PlayFab session

---

## Testing Notes
- Requires authenticated PlayFab session
- CloudScript must be deployed to PlayFab
- No retry logic (single attempt)
- GeneratePlayStreamEvent disabled to reduce noise

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added detailed logging
- **2025-01**: Disabled PlayStream events

