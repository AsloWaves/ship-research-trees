---
tags: [script, networking, vercel, discovery, implemented]
script-type: MonoBehaviour
namespace: WOS.Networking
file-path: Assets/Scripts/Networking/VercelServerDiscovery.cs
status: IMPLEMENTED
size: ~6 KB (207 lines)
feature-group: networking
---

# VercelServerDiscovery.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Networking
**File**: `Assets/Scripts/Networking/VercelServerDiscovery.cs`
**Size**: ~6 KB (207 lines)
**Dependencies**: UnityWebRequest, ServerConnectionInfo

---

## Purpose
Discovers active PlayFab MPS servers using Vercel Serverless Function. Directly calls Vercel API endpoint to query PlayFab infrastructure for available game servers by build alias.

**Migration**: Azure Functions → Vercel (complete)

---

## Architecture

```
Unity Client → Vercel Serverless → PlayFab MPS API
```

- Client calls Vercel endpoint with build alias
- Vercel function queries PlayFab for active servers
- Returns server connection info (IP, port, session ID)

---

## Configuration

### Inspector Fields
```csharp
[Header("Vercel Configuration")]
vercelApiUrl (string): Vercel function URL

[Header("Discovery Configuration")]
buildAlias (string, "production"): Build to search ("production", "latest", "beta")
requestTimeout (float, 10): Request timeout seconds
maxRetries (int, 3): Retry attempts
retryDelay (float, 2): Base delay between retries
enableDebugLogs (bool, true): Enable debug logging
```

### API Endpoint Format
```
GET {vercelApiUrl}/api/GetServerByAlias?buildAlias={alias}
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
- Returns early if discovery already in progress
- Starts coroutine with retry logic
- Fires OnServerDiscovered or OnDiscoveryFailed

---

## Retry Logic

Uses exponential backoff:
```
Attempt 1: Immediate
Attempt 2: retryDelay × 2^0 = 2s
Attempt 3: retryDelay × 2^1 = 4s
```

**Flow**:
1. Make request with timeout
2. On success → parse response → fire event
3. On failure → wait with backoff → retry
4. After max retries → fire OnDiscoveryFailed

---

## Response Structure

### VercelServerResponse
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

### ServerConnectionInfo (Output)
```csharp
public string ip;
public int port;
public string sessionId;
public string region;
public string buildId;
public string state;
```

---

## Validation

Before firing OnServerDiscovered:
- Response not null
- `success == true`
- IP not empty
- Port > 0

---

## Error Handling

- Request timeout → retry with backoff
- Network error → retry with backoff
- Parse error → fire OnDiscoveryFailed (no retry)
- Invalid response → fire OnDiscoveryFailed

---

## Integration Points

### Used By
- [[ServerBrowserManager]] - Primary discovery method
- [[JoinMenuController]] - Quick join flow

### Related
- [[PlayFabCloudScriptDiscovery]] - Alternative discovery method
- [[ServerConnectionInfo]] - Shared data structure

---

## Logging

Uses DebugManager with emojis:
- 🔍 Starting discovery
- 📡 Calling API
- 🔄 Retry attempt
- ⏳ Waiting for retry
- ✅ Success
- ⚠️ Warning
- ❌ Error

---

## Related Files
- [[PlayFabCloudScriptDiscovery]] - CloudScript alternative
- [[ServerBrowserManager]] - Server list management
- [[ServerConnectionInfo]] - Connection data

---

## Testing Notes
- Vercel cold start may take a few seconds
- Build alias must match PlayFab build configuration
- API requires no authentication (public endpoint)
- Timeout includes cold start time

---

## Changelog
- **2024-12**: Initial implementation (Azure Functions)
- **2025-01**: Migrated to Vercel Serverless
- **2025-01**: Added exponential backoff retry

