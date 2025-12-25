---
tags: [script, networking, multiplayer, implemented, phase1]
script-type: ScriptableObject
namespace: WOS.Networking
file-path: WOS2.3V2 Research/Scripts/Networking/ServerConfig.cs
status: ✅ IMPLEMENTED
size: Unknown
---

# ServerConfig.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Networking
**File**: `Scripts/Networking/ServerConfig.cs`
**Dependencies**: UnityEngine

---

## Purpose
Centralized server configuration ScriptableObject that stores Edgegap server IP addresses and automatically switches between localhost (Unity Editor) and production IP (builds) for seamless development-to-production workflow.

**Primary Use Case**: Eliminates manual server configuration changes between testing and deployment.

---

## Implements GDD Features
- [[Network-Architecture]] - Server address configuration and environment management
- [[Network-Architecture]] - Edgegap Integration (Section 6.5)

---

## Key Components

### Public Properties
```csharp
string productionServerIP         // Edgegap-assigned IP address (Inspector field)
int serverPort                    // Network port (default: 7777)
int healthPort                    // Health check port for Edgegap monitoring
```

### Public Methods
```csharp
GetServerIP()        // Returns appropriate IP (auto-detects Editor/Production)
GetServerPort()      // Returns configured port number
GetFullAddress()     // Returns complete "IP:port" string
IsUsingLocalServer() // Returns true if running on localhost (Editor)
GetServerType()      // Returns "Development" or "Production" for display
GetHealthPort()      // Returns health check port for Edgegap monitoring
```

---

## Configuration

### Inspector Fields
```csharp
[Header("Production Server (Edgegap)")]
productionServerIP: string = ""          // Set via Edgegap dashboard
                                         // Example: "123.45.67.89"

[Header("Port Configuration")]
serverPort: int = 7777                   // Mirror default port
healthPort: int = 8080                   // Edgegap health check port

[Header("Advanced")]
enableDebugLogging: bool = false         // Log server config on startup
```

### ScriptableObject Asset Location
- **Path**: `Assets/ScriptableObjects/Networking/ServerConfig.asset`
- **Creation**: Right-click → Create → WOS → Networking → Server Config
- **Usage**: Assign to NetworkManager or WOSEdgegapBootstrap

---

## Integration Points

### Dependencies (What This Needs)
- **UnityEngine** - Core Unity functionality
- **Application.isEditor** - Platform detection

### Used By (What Uses This)
- [[WOSEdgegapBootstrap]] - Validates server configuration on startup
- **NetworkManager** - Retrieves server address for connections
- **UI Systems** - Displays server type (Dev/Production) in menus
- **Debug Tools** - Shows connection info in debug panels

---

## Technical Details

### Auto-Detection Logic

The core feature is automatic environment detection:

```csharp
public string GetServerIP() {
    #if UNITY_EDITOR
        // Unity Editor: Always use localhost for testing
        return "127.0.0.1";
    #else
        // Production Build: Use Edgegap IP from Inspector
        return productionServerIP;
    #endif
}
```

**Why This Works**:
- Developers test on localhost without changing config
- Production builds automatically use Edgegap servers
- No manual switching = fewer deployment errors
- Same ScriptableObject works in both environments

---

### Environment Switching

**Unity Editor (Development)**:
```
GetServerIP():          "127.0.0.1" (automatic)
GetServerPort():        7777
GetFullAddress():       "127.0.0.1:7777"
IsUsingLocalServer():   true
GetServerType():        "Development"
```

**Production Build**:
```
GetServerIP():          "123.45.67.89" (from Inspector)
GetServerPort():        7777
GetFullAddress():       "123.45.67.89:7777"
IsUsingLocalServer():   false
GetServerType():        "Production"
```

---

### Health Check Integration

Edgegap requires health monitoring to ensure server is responsive:

```csharp
GetHealthPort() {
    return healthPort; // Default: 8080
}
```

**Usage by Edgegap**:
- Edgegap pings `http://[serverIP]:[healthPort]/health`
- If no response, server is marked as unhealthy
- Unhealthy servers are restarted or replaced
- Ensures players never connect to broken servers

---

## Performance Considerations

**Update Frequency**: None - ScriptableObject (data-only, no runtime logic)
**Memory Allocations**: Zero at runtime (string fields are static)
**CPU Cost**: Negligible (simple getter methods)
**Network Impact**: None (configuration only, not transmitted)

---

## How It Works

### Initialization
```
1. ScriptableObject is loaded with project
2. Inspector fields read from asset file
3. No runtime initialization needed (data is pre-configured)
```

### Runtime Usage
```csharp
// Example: NetworkManager startup
void Start() {
    // Get reference to ServerConfig asset
    ServerConfig config = Resources.Load<ServerConfig>("ServerConfig");

    // Use auto-detected address
    string address = config.GetFullAddress();

    // Connect to appropriate server
    networkManager.networkAddress = config.GetServerIP();
    networkManager.transport.port = config.GetServerPort();

    // Log for debugging
    Debug.Log($"Connecting to {config.GetServerType()} server: {address}");
}
```

---

## Example Usage

### Basic Configuration
```csharp
// Assign in Inspector or load at runtime
ServerConfig config = Resources.Load<ServerConfig>("ServerConfig");

// Get auto-detected address
string ip = config.GetServerIP();           // "127.0.0.1" or Edgegap IP
int port = config.GetServerPort();          // 7777
string fullAddress = config.GetFullAddress(); // "127.0.0.1:7777"

// Check environment
if (config.IsUsingLocalServer()) {
    Debug.Log("Running on localhost (Development)");
} else {
    Debug.Log($"Connected to production: {config.GetServerType()}");
}
```

### UI Display
```csharp
// Show server info in main menu
void UpdateServerStatusUI() {
    ServerConfig config = serverConfigReference;

    serverTypeText.text = config.GetServerType(); // "Development" or "Production"
    serverAddressText.text = config.GetFullAddress();

    // Color-code for visibility
    if (config.IsUsingLocalServer()) {
        statusIndicator.color = Color.yellow; // Dev = Yellow
    } else {
        statusIndicator.color = Color.green;  // Prod = Green
    }
}
```

### Validation in Bootstrap
```csharp
// WOSEdgegapBootstrap uses this to validate config
void ValidateServerConfiguration() {
    ServerConfig config = serverConfig;

    // Check if production IP is set
    if (!config.IsUsingLocalServer()) {
        string ip = config.GetServerIP();

        if (string.IsNullOrEmpty(ip)) {
            Debug.LogError("Production build requires Edgegap IP in ServerConfig!");
            return;
        }

        // Validate IP format
        if (!IsValidIP(ip)) {
            Debug.LogError($"Invalid IP address in ServerConfig: {ip}");
        }
    }

    Debug.Log($"Server config valid: {config.GetFullAddress()}");
}
```

---

## Configuration Workflow

### For Developers (Local Testing)
```
1. Create ServerConfig asset
2. Leave productionServerIP blank (or set to any value)
3. Run in Unity Editor
4. Automatically uses 127.0.0.1 (no configuration needed)
```

### For Production Deployment
```
1. Deploy server to Edgegap
2. Edgegap provides IP address (e.g., "123.45.67.89")
3. Open ServerConfig asset in Inspector
4. Set productionServerIP = "123.45.67.89"
5. Build game
6. Builds automatically connect to Edgegap server
```

### For Multiple Environments
```
Option A: Multiple ScriptableObject Assets
- ServerConfig_Dev.asset (local testing)
- ServerConfig_Staging.asset (staging server)
- ServerConfig_Production.asset (live server)
- Swap asset reference before building

Option B: Build-Time Configuration
- Use #define symbols (STAGING, PRODUCTION)
- ServerConfig checks symbols and returns appropriate IP
- Requires code modification (less flexible)
```

---

## Related Files
- [[WOSEdgegapBootstrap]] - Validates this config on startup
- [[Network-Architecture]] - Design documentation
- **NetworkManager** - Uses server address for connections
- ServerConfig.asset - Default ScriptableObject asset instance

---

## Testing Notes

### Tested Scenarios
- ✅ Editor auto-detection (always returns 127.0.0.1)
- ✅ Production build with valid Edgegap IP
- ✅ GetFullAddress() formatting ("IP:port")
- ✅ IsUsingLocalServer() returns correct bool
- ✅ Health port configuration

### Edge Cases
- ⚠️ Production build with empty IP (caught by WOSEdgegapBootstrap)
- ⚠️ Invalid IP format (no validation in ServerConfig itself)
- ✅ Port conflicts (handled by Mirror transport layer)

### Test Commands
```csharp
// Test in Unity Console
ServerConfig config = Resources.Load<ServerConfig>("ServerConfig");
Debug.Log($"IP: {config.GetServerIP()}");
Debug.Log($"Port: {config.GetServerPort()}");
Debug.Log($"Full: {config.GetFullAddress()}");
Debug.Log($"IsLocal: {config.IsUsingLocalServer()}");
Debug.Log($"Type: {config.GetServerType()}");
```

---

## Known Issues & Limitations

### No IP Validation
- ServerConfig doesn't validate IP format
- Invalid IPs cause connection failures at runtime
- **Workaround**: WOSEdgegapBootstrap performs validation
- **Future**: Add IP validation method to ServerConfig

### Hardcoded Port
- Port 7777 is common but not universal
- If Edgegap assigns different port, must change in Inspector
- **Future**: Support dynamic port assignment from Edgegap API

### Single Server Only
- Only stores one production IP
- No support for multiple servers or load balancing
- **Phase 2**: Add support for server pools

### No Encryption Config
- No fields for SSL/TLS configuration
- **Phase 2**: Add encryption settings when implementing secure transport

---

## Future Enhancements

### Phase 2 Improvements
- [ ] Add IP address format validation
- [ ] Support multiple server regions (Americas, Europe, Asia)
- [ ] Add server latency display (ping test)
- [ ] Support dynamic port assignment from Edgegap

### Phase 3 Improvements
- [ ] Server load balancing (multiple IPs)
- [ ] SSL/TLS certificate configuration
- [ ] Server status API integration (uptime, player count)
- [ ] Automatic failover to backup servers

---

## Best Practices

### Asset Management
```
✅ DO: Commit ServerConfig.asset to version control
✅ DO: Use meaningful productionServerIP (even if unused in Editor)
✅ DO: Document which Edgegap deployment the IP belongs to
❌ DON'T: Hardcode IPs in scripts (always use ServerConfig)
❌ DON'T: Change productionServerIP without testing
```

### Security Considerations
```
⚠️ CAUTION: ServerConfig.asset is in version control
⚠️ CAUTION: productionServerIP is visible to anyone with project access
✅ SAFE: IP address alone is not a security risk (server validates all actions)
❌ NEVER: Store passwords, API keys, or secrets in ServerConfig
```

### Testing Workflow
```
1. Develop on localhost (automatic in Editor)
2. Test multiplayer using Editor-to-Editor (both use 127.0.0.1)
3. Deploy to Edgegap staging environment
4. Update ServerConfig with staging IP
5. Build and test against staging
6. Deploy to production Edgegap
7. Update ServerConfig with production IP
8. Build final production client
```

---

## Changelog
- **2025-01-XX**: Initial implementation with auto-detection
- **2025-01-XX**: Added health port for Edgegap monitoring
- **2025-01-XX**: Added GetServerType() for UI display
- **2025-11-17**: Documentation created

---

**Status**: ✅ Production-ready and actively used
**Maintenance**: Stable, minimal changes expected
**Future**: Phase 2 will add validation and multi-region support
