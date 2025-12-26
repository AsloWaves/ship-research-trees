---
tags: [script, networking, scriptableobject, configuration, implemented]
script-type: ScriptableObject
namespace: WOS.Networking
file-path: Assets/Scripts/Networking/ServerConfig.cs
status: IMPLEMENTED
size: ~4 KB (140 lines)
feature-group: networking
---

# ServerConfig.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Networking
**File**: `Assets/Scripts/Networking/ServerConfig.cs`
**Size**: ~4 KB (140 lines)
**Dependencies**: None
**Asset Menu**: `WOS/Networking/Server Configuration`

---

## Purpose
Server configuration asset storing connection details. Automatically switches between localhost (Editor) and production (builds) for seamless development workflow.

---

## Configuration Fields

### Production Server
```
serverAddress (string): Production server IP:port (e.g., "172.234.24.224:31139")
healthPort (int, 8080): Health check port for server status
```

### Local Testing
```
useLocalhostInEditor (bool, true): Use localhost when in Unity Editor
localServerAddress (string, "localhost:7777"): Local server address
useLocalInventory (bool, false): Use local file storage instead of PlayFab
```

### Display Info
```
serverLocation (string): Server location for UI display (e.g., "Chicago, Illinois")
showServerInfo (bool, true): Show deployment info in UI
```

---

## Public Methods

### GetServerIP
Returns IP without port, auto-switches for Editor.
```csharp
public string GetServerIP()
{
    string activeAddress = GetActiveAddress();
    int colonIndex = activeAddress.IndexOf(':');
    return colonIndex > 0
        ? activeAddress.Substring(0, colonIndex)
        : activeAddress;
}
```

### GetServerPort
Returns port as ushort, defaults to 7777.

### GetFullAddress
Returns complete IP:port string.

### IsUsingLocalServer
Checks if currently using local server.
```csharp
public bool IsUsingLocalServer()
{
#if UNITY_EDITOR
    return useLocalhostInEditor;
#else
    return false;
#endif
}
```

### GetServerType
Returns server type string for display.
```csharp
public string GetServerType()
{
#if UNITY_EDITOR
    if (useLocalhostInEditor) return "Local Test Server";
#endif
    return "Edgegap Production";
}
```

### GetHealthPort
Returns health check port (different in Editor vs build).

---

## Auto-Switching Logic

The `GetActiveAddress()` private method handles environment detection:

```csharp
private string GetActiveAddress()
{
#if UNITY_EDITOR
    if (useLocalhostInEditor)
    {
        return localServerAddress;  // "localhost:7777"
    }
#endif
    return serverAddress;  // Production address
}
```

This enables:
- **In Editor**: Connects to localhost for quick testing
- **In Build**: Connects to production server
- **No code changes needed** between development and deployment

---

## Asset Location
```
Assets/Resources/ServerConfigs/ServerConfig.asset
```

Loaded at runtime via:
```csharp
var config = Resources.Load<ServerConfig>("ServerConfigs/ServerConfig");
```

---

## Integration Points

### Used By
- [[WOSNetworkManager]] - Gets connection address
- [[JoinMenuController]] - Displays server info
- [[ServerBrowserManager]] - Health check endpoint

---

## Development Workflow

| Environment | Address | Health Port | Inventory |
|-------------|---------|-------------|-----------|
| Unity Editor | localhost:7777 | 8080 | PlayFab (or local if enabled) |
| Development Build | Production IP | Configured | PlayFab |
| Production Build | Production IP | Configured | PlayFab |

---

## Related Files
- [[WOSNetworkManager]] - Uses for connection
- [[JoinMenuController]] - Displays server info
- [[ServerBrowserManager]] - Server discovery

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added useLocalInventory flag
- **2025-01**: Added health port configuration

