# PlayFabServerAuthConfig.cs

## Quick Reference

| **File** | PlayFabServerAuthConfig.cs |
|----------|---------------------------|
| **Namespace** | WOS.Networking.Managers |
| **Inheritance** | MonoBehaviour |
| **Lines** | 150 |
| **Architecture** | Server-only authentication configurator, environment variable loader |

---

## Purpose

Configures PlayFab authentication credentials for server builds only. Prevents exposing the DeveloperSecretKey in client builds by loading it from environment variables at runtime.

**Security Model**:
- Server-side only (headless builds or Editor host mode)
- Loads DeveloperSecretKey from environment variables
- Never hardcoded in code or assets
- Auto-detects server mode vs client mode

---

## Configuration

### Compilation Directives

```csharp
#if UNITY_SERVER || UNITY_EDITOR
// Only compiles for server builds and Unity Editor
#endif
```

**Result**:
- ✅ Included in headless server builds
- ✅ Included in Unity Editor (for testing)
- ❌ Excluded from client builds (security)

### Inspector Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enableDebugLogs` | bool | `true` | Enable authentication configuration logging |

---

## Environment Variables

### Priority Order

The service checks environment variables in priority order:

1. **`PF_MPS_SECRET_PLAYFAB_SECRET_KEY`** (PlayFab MPS secrets system)
   - Recommended for production
   - Automatically injected by PlayFab Multiplayer Servers
   - Configured in Game Manager → Multiplayer → Servers → Secrets

2. **`PLAYFAB_SECRET_KEY`** (Local/Docker fallback)
   - For local testing and Docker containers
   - Set manually in environment or Docker Compose

### Setting Environment Variables

**PlayFab MPS (Production)**:
1. Go to PlayFab Game Manager
2. Navigate to Multiplayer → Servers → Secrets
3. Create secret: Name=`PLAYFAB_SECRET_KEY`, Value=`<your-secret-key>`
4. PlayFab automatically exposes as `PF_MPS_SECRET_PLAYFAB_SECRET_KEY`

**Local Testing (Windows)**:
```powershell
$env:PLAYFAB_SECRET_KEY = "YOUR_SECRET_KEY_HERE"
# Start Unity Editor or run server build
```

**Docker Compose**:
```yaml
services:
  game-server:
    image: your-server-image
    environment:
      - PLAYFAB_SECRET_KEY=${PLAYFAB_SECRET_KEY}
```

**Linux/Mac**:
```bash
export PLAYFAB_SECRET_KEY="YOUR_SECRET_KEY_HERE"
# Start Unity Editor or run server build
```

---

## Public API

### Configuration Methods

#### `ShouldConfigureServerAuth()`
Determines if PlayFab server authentication should be configured.

**Returns**: `bool` - True if running as server

**Logic**:
- Always true in headless/batch mode builds (dedicated servers)
- True in Editor if NetworkServer is active (host mode)
- False otherwise (client mode)

#### `ConfigureServerAuthentication()`
Loads DeveloperSecretKey from environment and applies to PlayFab settings.

**Process**:
1. Check if already configured (prevent duplicate configuration)
2. Load secret key from environment variables (priority order)
3. Validate secret key is present
4. Apply to `PlayFabSettings.staticSettings.DeveloperSecretKey`
5. Log success or failure

---

## Lifecycle

### Awake() Flow

```
1. Check if GameObject is root (DontDestroyOnLoad requirement)
   ├─ If not root → Move to root (transform.SetParent(null))
   └─ Apply DontDestroyOnLoad(gameObject)

2. Check if should configure server auth
   ├─ If headless build → Configure immediately
   ├─ If Editor + NetworkServer.active → Configure immediately
   └─ If client mode → Skip (log message)

3. Load environment variable
   ├─ Try PF_MPS_SECRET_PLAYFAB_SECRET_KEY (PlayFab MPS)
   ├─ Try PLAYFAB_SECRET_KEY (Local/Docker)
   └─ If not found → Log error with instructions

4. Apply to PlayFabSettings
   └─ PlayFabSettings.staticSettings.DeveloperSecretKey = secretKey
```

### Start() Flow

```
Double-check configuration in case NetworkServer started after Awake()
├─ If not configured AND ShouldConfigureServerAuth() → Configure
└─ Otherwise → Skip (already configured)
```

### OnDestroy() Flow

```
Clear secret key from memory (security best practice)
└─ PlayFabSettings.staticSettings.DeveloperSecretKey = null
```

---

## DontDestroyOnLoad Fix

### Critical Fix (Lines 22-31)

**Problem**: Unity warning if GameObject is not root
```
DontDestroyOnLoad only works for root GameObjects or components on root GameObjects
```

**Solution**: Auto-move to root before applying DontDestroyOnLoad
```csharp
if (transform.parent != null)
{
    // GameObject is NOT root - move to root
    transform.SetParent(null);
    Debug.Log("GameObject moved to root - parent is now null");
}

// Now safe to apply DontDestroyOnLoad
DontDestroyOnLoad(gameObject);
```

**Why This Matters**:
- Server starts in MainMenu scene, then loads Main scene
- PlayFabServerAuthConfig must persist across scene loads
- If destroyed during scene transition, authentication fails

---

## Error Handling

### Missing Secret Key

```
❌ CRITICAL: No DeveloperSecretKey found in environment!
❌ Server authentication will fail!
❌ For PlayFab MPS: Create secret 'PLAYFAB_SECRET_KEY' in Game Manager → Multiplayer → Servers → Secrets
❌ For Local/Docker: Set PLAYFAB_SECRET_KEY environment variable
❌ Get secret key from: PlayFab Game Manager → Settings → Secret Keys
```

### Already Configured

```csharp
if (isConfigured)
{
    return; // Already configured, skip
}
```

Prevents duplicate configuration if Awake() and Start() both trigger.

---

## Security Best Practices

### What NOT to Do

❌ **Hardcode secret key in code**:
```csharp
// NEVER DO THIS!
PlayFabSettings.staticSettings.DeveloperSecretKey = "ABC123...";
```

❌ **Store in ScriptableObject**:
```csharp
// NEVER DO THIS!
[CreateAssetMenu]
public class PlayFabConfig : ScriptableObject
{
    public string secretKey; // Exposed in Inspector!
}
```

❌ **Commit to version control**:
```
# .gitignore should include:
*.env
secrets.json
```

### What TO Do

✅ **Use environment variables**:
```csharp
string secretKey = System.Environment.GetEnvironmentVariable("PLAYFAB_SECRET_KEY");
```

✅ **PlayFab MPS secrets**:
```
Game Manager → Multiplayer → Servers → Secrets
Name: PLAYFAB_SECRET_KEY
Value: <your-secret-key>
```

✅ **Clear on destroy**:
```csharp
void OnDestroy()
{
    PlayFabSettings.staticSettings.DeveloperSecretKey = null;
}
```

---

## Usage Example

### Complete Server Startup

```csharp
// 1. Add PlayFabServerAuthConfig to scene
// This auto-configures on server startup

// 2. Set environment variable (before starting Unity)
// PowerShell: $env:PLAYFAB_SECRET_KEY = "YOUR_SECRET_KEY"

// 3. Server starts
void Awake()
{
    // PlayFabServerAuthConfig.Awake() runs automatically
    // - Loads secret key from environment
    // - Configures PlayFabSettings
    // - Persists across scene loads
}

// 4. Use PlayFab Server API
void Start()
{
    if (NetworkServer.active)
    {
        // PlayFab Server API calls now work
        PlayFabServerAPI.GetUserData(...);
    }
}
```

---

## Design Notes

### Why Environment Variables?

**Problem**: DeveloperSecretKey is sensitive
- Grants full access to PlayFab title
- Can modify player data, economy, etc.
- Must never be exposed to clients

**Solution**: Environment variables
- Not compiled into builds
- Not visible in decompiled code
- Not committed to version control
- Easy to rotate/change

### PlayFab MPS Integration

**How it works**:
1. Admin creates secret in PlayFab Game Manager
2. PlayFab MPS injects secret as environment variable during container startup
3. PlayFabServerAuthConfig loads secret from environment
4. Server can now call PlayFab Server API

**Naming Convention**:
- PlayFab MPS prefixes secrets with `PF_MPS_SECRET_`
- Secret name: `PLAYFAB_SECRET_KEY`
- Environment variable: `PF_MPS_SECRET_PLAYFAB_SECRET_KEY`

### Server vs Client Detection

**Detection Logic**:
```csharp
bool ShouldConfigureServerAuth()
{
    // Dedicated server builds (headless)
    if (Application.isBatchMode)
        return true;

    // Editor host mode
    #if UNITY_EDITOR
    if (Mirror.NetworkServer.active)
        return true;
    #endif

    // Client mode
    return false;
}
```

**Why This Matters**:
- Clients never load secret key (security)
- Editor can test server mode (host gameplay)
- Dedicated servers always configure (production)

---

## Key Takeaways

1. **Server-Only**: Only configures for server builds, never clients
2. **Environment Variables**: Loads DeveloperSecretKey from environment (never hardcoded)
3. **PlayFab MPS Integration**: Supports PlayFab's secrets system
4. **Scene Persistence**: Uses DontDestroyOnLoad to persist across scene transitions
5. **Security**: Clears secret key from memory on destroy
6. **Auto-Detection**: Automatically detects server mode vs client mode
