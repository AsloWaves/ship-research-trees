---
tags: [script, networking, validation, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.Networking
file-path: WOS2.3V2 Research/Scripts/Networking/WOSEdgegapBootstrap.cs
status: ✅ IMPLEMENTED
size: 1.7 KB
---

# WOSEdgegapBootstrap.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Networking
**File**: `Scripts/Networking/WOSEdgegapBootstrap.cs`
**Size**: 1.7 KB
**Dependencies**: UnityEngine, Mirror (NetworkManager)

---

## Purpose
Standalone validation script that checks server configuration and port mappings for Edgegap deployment without requiring the Edgegap plugin.

**Primary Use Case**: Optional configuration validator that ensures Mirror transport settings and NetworkManager address configuration are correct for Edgegap cloud deployment.

**Key Distinction**: This script is NOT required for the server to function - it's a debugging and validation tool that logs warnings if configuration issues are detected.

---

## Implements GDD Features
- [[Network-Architecture]] - Edgegap Deployment validation (Section 6.5)
- [[Server-Config]] - Server configuration validation

---

## Key Components

### Inspector Fields
```csharp
[Header("FD Configuration")]
expectedPort: ushort = 7777              // Expected port (must match Edgegap mapping)
expectedProtocol: string = "UDP"         // Transport protocol (UDP for KCP, TCP for Telepathy)

[Header("Debug")]
verboseLogging: bool = true              // Enable detailed validation logs
```

### Public Methods
- None (validation happens automatically on Awake)

### Key Private Methods
- `ValidateServerConfiguration()` - Checks Mirror transport and NetworkManager settings
- `Log(string message)` - Conditional logging based on verboseLogging flag

---

## Configuration

### Inspector Setup
```
1. Attach to GameObject in first scene (typically MainMenu)
2. Configure expectedPort to match Edgegap port mapping (default: 7777)
3. Set expectedProtocol based on Mirror transport:
   - "UDP" for KCP Transport
   - "TCP" for Telepathy Transport
4. Enable verboseLogging for debugging (disable for production)
```

### Edgegap Requirements
```
Edgegap Port Mapping:
- Port: 7777 (must match expectedPort)
- Protocol: TCP or UDP (must match transport)
- Name: "game" (Edgegap dashboard)

NetworkManager Configuration:
- networkAddress: "localhost" or "0.0.0.0"
- Transport: Properly configured with matching port
```

---

## Integration Points

### Dependencies (What This Needs)
- **UnityEngine** - MonoBehaviour base, logging
- **Mirror** - NetworkManager access, transport validation
- **NetworkManager** - Validates address and transport configuration

### Used By (What Uses This)
- **Edgegap Deployments** - Validates cloud server configuration
- **Development Workflow** - Catches configuration errors before deployment
- **Debug/QA** - Verifies correct setup in test environments

---

## Technical Details

### Validation Checks Performed
```
1. Mirror Transport Configuration:
   - Port matches expectedPort (7777)
   - Protocol matches expectedProtocol (UDP/TCP)
   - Transport is properly assigned to NetworkManager

2. NetworkManager Address:
   - networkAddress is set to "localhost" or "0.0.0.0"
   - Address is appropriate for server hosting

3. Edgegap Port Mapping:
   - Expected port is documented and logged
   - Protocol mismatch warnings (if any)
```

### Standalone Operation
**Why No Edgegap Plugin Required**:
- Script only validates Mirror settings (built into Unity)
- No Edgegap SDK/plugin classes referenced
- Works in Editor and builds without additional dependencies
- Logs configuration state for manual verification

**Benefit**: Developers without Edgegap plugin can still prepare correct configuration.

---

## How It Works

### Initialization
```csharp
void Awake() {
    // Step 1: Log startup
    Log("🌊 WOSEdgegapBootstrap initialized");

    // Step 2: Validate configuration immediately
    ValidateServerConfiguration();

    // Script does nothing else after validation
    // NetworkManager handles actual networking
}
```

### Validation Process
```
1. Find NetworkManager in scene
   ├─ If not found → Log error and exit
   └─ If found → Continue to step 2

2. Check Transport Configuration
   ├─ Get Transport from NetworkManager
   ├─ Verify port matches expectedPort
   ├─ Check protocol matches expectedProtocol
   └─ Log warning if mismatch detected

3. Verify NetworkManager Address
   ├─ Check networkAddress field
   ├─ Validate it's "localhost" or "0.0.0.0"
   └─ Log warning if incorrect

4. Log Validation Summary
   ├─ Report all checks passed ✅
   └─ OR list configuration issues ⚠️
```

### Logging System
```csharp
void Log(string message) {
    if (verboseLogging) {
        Debug.Log($"[WOSEdgegapBootstrap] {message}");
    }
}

// Conditional logging prevents console spam in production
// Enable verboseLogging in Inspector when debugging
```

---

## Example Usage

### Typical Setup
```csharp
// 1. Create GameObject in MainMenu scene
GameObject bootstrapObj = new GameObject("EdgegapBootstrap");

// 2. Add WOSEdgegapBootstrap component
WOSEdgegapBootstrap bootstrap = bootstrapObj.AddComponent<WOSEdgegapBootstrap>();

// 3. Configure in Inspector
bootstrap.expectedPort = 7777;          // Match Edgegap port mapping
bootstrap.expectedProtocol = "UDP";     // Match transport (KCP = UDP, Telepathy = TCP)
bootstrap.verboseLogging = true;        // Enable for debugging

// 4. Run game - validation happens automatically
// Check Console for warnings or confirmation
```

### Expected Console Output (Success)
```
[WOSEdgegapBootstrap] 🌊 WOSEdgegapBootstrap initialized
[WOSEdgegapBootstrap] ✅ NetworkManager found
[WOSEdgegapBootstrap] ✅ Transport configured: KCP Transport (UDP)
[WOSEdgegapBootstrap] ✅ Port matches expected: 7777
[WOSEdgegapBootstrap] ✅ NetworkManager address: 0.0.0.0
[WOSEdgegapBootstrap] ✅ Server configuration valid for Edgegap deployment
```

### Expected Console Output (Configuration Issue)
```
[WOSEdgegapBootstrap] 🌊 WOSEdgegapBootstrap initialized
[WOSEdgegapBootstrap] ✅ NetworkManager found
[WOSEdgegapBootstrap] ⚠️ Transport configured: Telepathy (TCP)
[WOSEdgegapBootstrap] ⚠️ Expected protocol: UDP
[WOSEdgegapBootstrap] ⚠️ WARNING: Protocol mismatch! Update expectedProtocol to "TCP" or switch to KCP transport
[WOSEdgegapBootstrap] ✅ Port matches expected: 7777
[WOSEdgegapBootstrap] ⚠️ NetworkManager address: 127.0.0.1
[WOSEdgegapBootstrap] ⚠️ WARNING: Address should be "localhost" or "0.0.0.0" for Edgegap hosting
[WOSEdgegapBootstrap] ⚠️ Configuration issues detected - review warnings above
```

---

## Validation Scenarios

### Scenario 1: Development Testing (Editor)
```
Configuration:
- NetworkManager.networkAddress = "localhost"
- Transport: KCP (port 7777)
- expectedPort: 7777
- expectedProtocol: "UDP"

Result: ✅ All checks pass
Action: Continue development
```

### Scenario 2: Pre-Deployment Check
```
Configuration:
- NetworkManager.networkAddress = "0.0.0.0"
- Transport: Telepathy (port 7777)
- expectedPort: 7777
- expectedProtocol: "UDP"

Result: ⚠️ Protocol mismatch (Telepathy is TCP, not UDP)
Action: Either change expectedProtocol to "TCP" or switch to KCP transport
```

### Scenario 3: Production Build
```
Configuration:
- NetworkManager.networkAddress = "0.0.0.0"
- Transport: KCP (port 7777)
- expectedPort: 7777
- expectedProtocol: "UDP"
- verboseLogging: false

Result: ✅ All checks pass (no console output in production)
Action: Deploy to Edgegap
```

---

## Related Files
- [[ServerConfig]] - ServerConfig.cs provides Edgegap IP configuration
- [[Network-Architecture]] - Overall network design documentation
- **NetworkManager** - Mirror's core networking manager (validated by this script)
- **Transport** - Mirror transport layer (KCP or Telepathy)

---

## Testing Notes

### Tested Scenarios
- ✅ Correct configuration (all validation passes)
- ✅ Port mismatch detection
- ✅ Protocol mismatch detection (UDP vs TCP)
- ✅ NetworkManager address validation
- ✅ Missing NetworkManager handling

### Edge Cases
- ⚠️ **No NetworkManager in scene**: Script logs error and exits gracefully
- ⚠️ **Multiple NetworkManagers**: Script validates first found instance
- ⚠️ **Custom transport**: May not detect protocol correctly (only checks common transports)

### Manual Testing Steps
```
1. Attach script to GameObject in MainMenu scene
2. Set expectedPort to intentionally wrong value (e.g., 8888)
3. Enter Play mode
4. Verify warning appears: "Port mismatch detected"
5. Correct expectedPort to 7777
6. Enter Play mode
7. Verify success message: "Server configuration valid"
```

---

## Known Issues & Limitations

### Limited Transport Detection
**Issue**: Script may not correctly identify all transport types
- Only checks common transports (KCP, Telepathy)
- Custom transports require manual verification
- **Workaround**: Use verboseLogging to verify transport name

### No Automatic Correction
**Issue**: Script only logs warnings, doesn't fix configuration
- Developer must manually adjust settings
- No runtime configuration changes
- **By Design**: Validation-only tool (prevents unexpected behavior)

### Single-Scene Validation
**Issue**: Only runs in scene where it's placed
- If NetworkManager is in different scene, validation fails
- **Workaround**: Place in same scene as NetworkManager (typically MainMenu)

### No Edgegap API Integration
**Issue**: Cannot verify Edgegap cloud-side port mappings
- Only validates local Unity configuration
- Actual Edgegap port mapping must be checked in dashboard
- **Future**: Phase 2 may add Edgegap API validation

---

## Best Practices

### Development Workflow
```
✅ DO: Enable verboseLogging during development
✅ DO: Attach to first scene with NetworkManager
✅ DO: Keep expectedPort synchronized with Edgegap port mapping
✅ DO: Verify console output before building
❌ DON'T: Rely on this script for production monitoring
❌ DON'T: Use as replacement for proper testing
```

### Deployment Checklist
```
Pre-Deployment:
1. ✅ Run game in Editor with bootstrap attached
2. ✅ Verify all validation checks pass
3. ✅ Confirm Edgegap port mapping matches expectedPort
4. ✅ Test connection to Edgegap server
5. ✅ Disable verboseLogging for production build
6. ✅ Build and deploy

Post-Deployment:
1. ✅ Test client connection to deployed server
2. ✅ Verify port mapping works correctly
3. ✅ Monitor Edgegap dashboard for server health
```

### When to Use This Script
```
✅ USE WHEN:
- Setting up Edgegap for first time
- Debugging connection issues
- Verifying configuration before deployment
- Training new developers on network setup

❌ DON'T USE WHEN:
- Production runtime monitoring (use proper monitoring tools)
- Automatic configuration fixes (script is validation-only)
- Performance-critical code paths (validation is one-time startup cost)
```

---

## Integration with ServerConfig

While WOSEdgegapBootstrap validates **transport and port settings**, [[ServerConfig]] handles **IP address management**:

```
WOSEdgegapBootstrap:
- ✅ Validates port matches Edgegap mapping
- ✅ Checks transport protocol (UDP/TCP)
- ✅ Verifies NetworkManager address format
- ❌ Does NOT provide IP addresses

ServerConfig:
- ✅ Provides production Edgegap IP address
- ✅ Auto-switches between localhost (Editor) and production
- ✅ Returns full address string (IP:port)
- ❌ Does NOT validate port mappings

Together: Complete configuration validation + management
```

### Complementary Usage
```csharp
// Bootstrap validates settings
WOSEdgegapBootstrap bootstrap = GetComponent<WOSEdgegapBootstrap>();
// Logs warnings if port/transport misconfigured

// ServerConfig provides IP
ServerConfig config = Resources.Load<ServerConfig>("ServerConfig");
string serverIP = config.GetServerIP(); // Auto-detects Editor vs Production

// NetworkManager uses both
networkManager.networkAddress = serverIP;
networkManager.transport.port = bootstrap.expectedPort; // Already validated
```

---

## Changelog
- **2025-01-XX**: Initial implementation with basic validation
- **2025-01-XX**: Added protocol mismatch detection
- **2025-01-XX**: Added verbose logging toggle
- **2025-11-17**: Documentation created

---

**Status**: ✅ Production-ready (optional validation tool)
**Maintenance**: Stable, minimal changes expected
**Future**: May add Edgegap API validation in Phase 2
