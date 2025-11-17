---
tags: [implemented, phase1, multiplayer, network]
status: ✅ IMPLEMENTED
phase: Phase 1
priority: HIGH
last-updated: 2025-11-17
---

# Network Architecture

## Overview
Fathoms Deep uses Mirror Networking framework for authoritative server architecture with client-side prediction. The system features Edgegap cloud deployment integration, automatic server configuration switching between Editor and production environments, and robust client-server synchronization for naval combat gameplay.

## Implementation Status
**Status**: ✅ **IMPLEMENTED** (Core networking complete)
**Phase**: Phase 1 Complete
**Scripts**: [[ServerConfig]], [[WOSEdgegapBootstrap]], [[NetworkedNavalController]]
**Priority**: HIGH - Foundation for all multiplayer features

---

## Design Specification

### Core Architecture

#### Client-Server Model ✅
- **Architecture**: Authoritative dedicated server
- **Framework**: Mirror Networking (open-source Unity networking)
- **Authority**: Server validates all gameplay actions
- **Prediction**: Client-side prediction for smooth ship movement
- **Synchronization**: NetworkTransform for position/rotation sync

#### Server Authority
The server has final authority over all game state:
- **Ship Movement**: Validated by server, synced to clients
- **Combat**: Damage calculations server-side only
- **Chat**: Messages routed through server with validation
- **Spawn/Despawn**: Server controls all object lifecycle
- **Game State**: Economy, missions, faction standing all server-authoritative

#### Client Prediction
To maintain responsiveness, clients predict their own actions:
- **Ship Controls**: Player ship responds immediately to input
- **Physics**: Client simulates movement while awaiting server confirmation
- **Reconciliation**: Server corrections applied smoothly via NetworkTransform
- **Result**: No input lag despite network latency

---

### Deployment Architecture

#### Edgegap Cloud Integration ✅
**Provider**: Edgegap (low-latency edge computing)
**Purpose**: Automatic server deployment to player-nearest data centers

**Key Features**:
- **Edge Computing**: Servers deployed to closest geographic location
- **Auto-Scaling**: Spin up/down servers based on player demand
- **Health Monitoring**: Automatic health checks and failover
- **Global Coverage**: Multi-region support for worldwide players

#### Environment Management ✅
The system automatically switches between development and production:

**Unity Editor (Development)**:
- Server IP: `127.0.0.1` (localhost)
- Port: `7777` (Mirror default)
- Purpose: Local testing without cloud deployment
- Auto-detection: ServerConfig checks `Application.isEditor`

**Production Builds**:
- Server IP: Edgegap-assigned IP (configured in ServerConfig asset)
- Port: `7777` (or configured value)
- Purpose: Live multiplayer sessions
- Validation: WOSEdgegapBootstrap checks configuration on startup

---

## Technical Implementation

### Mirror Networking Framework

#### Why Mirror?
- **Open Source**: Free, community-driven, no licensing costs
- **Unity Native**: Built specifically for Unity, seamless integration
- **Performance**: Low latency, optimized for fast-paced gameplay
- **Authority**: Server-authoritative by design
- **Features**: NetworkTransform, Commands/ClientRpc, SyncVars built-in
- **Community**: Large user base, active development, extensive documentation

#### Core Mirror Components

**NetworkManager**:
- Manages server/client lifecycle
- Handles player spawning/despawning
- Controls scene transitions
- Maintains connection list

**NetworkIdentity**:
- Unique ID for networked objects
- Required on all synced GameObjects
- Identifies local vs. remote players
- Handles authority assignments

**NetworkBehaviour**:
- Base class for networked scripts
- Provides [Command], [ClientRpc], [Server] attributes
- SyncVar automatic synchronization
- isLocalPlayer, isServer, isClient flags

**NetworkTransform**:
- Automatic position/rotation sync
- Interpolation for smooth movement
- Authority-based updates
- Client prediction support

---

### Server Configuration System

#### ServerConfig.cs (ScriptableObject)
**File**: [[ServerConfig]]
**Purpose**: Centralized server address configuration with auto-switching

**Key Methods**:
```csharp
GetServerIP()        // Returns IP (auto-detects Editor vs. Production)
GetServerPort()      // Returns port number (default: 7777)
GetFullAddress()     // Returns "IP:port" string
IsUsingLocalServer() // Check if running on localhost
GetServerType()      // Returns "Development" or "Production"
GetHealthPort()      // Returns health check port for Edgegap
```

**Configuration**:
```
Development (Unity Editor):
- IP: 127.0.0.1 (automatic)
- Port: 7777
- No Edgegap connection

Production (Builds):
- IP: [Configured Edgegap IP]
- Port: 7777 (or custom)
- Edgegap health monitoring enabled
```

**Auto-Detection Logic**:
```csharp
public string GetServerIP() {
    #if UNITY_EDITOR
        return "127.0.0.1"; // Always localhost in Editor
    #else
        return productionServerIP; // Edgegap IP in builds
    #endif
}
```

---

#### WOSEdgegapBootstrap.cs
**File**: [[WOSEdgegapBootstrap]]
**Purpose**: Validation script that checks server configuration on startup

**Key Responsibilities**:
- Validates Mirror NetworkManager is configured
- Checks ServerConfig asset exists and is valid
- Verifies Edgegap settings in production builds
- Logs warnings for missing/invalid configuration
- Prevents startup if critical errors detected

**Validation Checks**:
```
1. NetworkManager present in scene?
2. ServerConfig ScriptableObject assigned?
3. Production build has valid Edgegap IP?
4. Health check port configured?
5. Mirror transport settings correct?
```

---

### Client-Side Prediction

#### NetworkedNavalController.cs
**File**: [[NetworkedNavalController]]
**Purpose**: Networked ship movement with client-side prediction

**Prediction Flow**:
```
Client Input:
1. Player presses forward arrow
2. NetworkedNavalController immediately applies throttle locally
3. Ship responds instantly on client (no lag)
4. Client sends [Command] to server with input state

Server Processing:
5. Server receives command
6. Server validates input (anti-cheat checks)
7. Server applies same throttle to authoritative ship instance
8. Server's NetworkTransform syncs position to all clients

Reconciliation:
9. Client receives server's authoritative position
10. NetworkTransform smoothly corrects any prediction errors
11. Player sees continuous smooth movement (no rubber-banding)
```

**Why This Works**:
- Most predictions are correct (player knows their own input)
- Small corrections are interpolated smoothly
- Result: Feels responsive like single-player despite network latency

---

### Network Commands & RPCs

#### Mirror Attributes

**[Command] - Client to Server**:
```csharp
[Command]
void CmdSetThrottle(int throttleLevel) {
    // Runs on SERVER when client calls it
    // Validates input, applies to authoritative state
}
```

**[ClientRpc] - Server to Clients**:
```csharp
[ClientRpc]
void RpcShowExplosion(Vector3 position) {
    // Runs on ALL CLIENTS when server calls it
    // Used for visual effects, sounds, UI updates
}
```

**[Server] - Server-Only Methods**:
```csharp
[Server]
void DealDamage(NetworkIdentity target, float damage) {
    // Only runs on SERVER
    // Used for authoritative gameplay logic
}
```

**[SyncVar] - Automatic Synchronization**:
```csharp
[SyncVar]
int currentThrottle; // Automatically synced to all clients
```

---

## Integration Points

### Dependencies
- **Unity Networking**: Mirror Networking package
- **Edgegap SDK**: (Optional) For advanced deployment features
- **System.Net**: For health check endpoints
- **UnityEngine.Networking**: For transport layer

### Used By
- **All Networked Systems**: Chat, combat, movement, spawning
- **Player Controllers**: [[NetworkedNavalController]]
- **Chat System**: [[ChatManager]]
- **Combat Systems**: Weapon firing, damage calculation
- **Economy**: Server-authoritative transactions
- **Authentication**: Player login/validation

### API for Other Systems
```csharp
// Get server address
string address = ServerConfig.GetFullAddress();

// Check if local or production
bool isLocal = ServerConfig.IsUsingLocalServer();

// Start server/client (from NetworkManager)
NetworkManager.singleton.StartServer();
NetworkManager.singleton.StartClient();
NetworkManager.singleton.StartHost(); // Server + Client

// Check network state
bool isServer = NetworkServer.active;
bool isClient = NetworkClient.active;
```

---

## Network Performance

### Optimization Strategies

**Bandwidth Efficiency**:
- Only sync essential state (position, rotation, health)
- Use SyncVars sparingly (they update every network tick)
- Compress rotation to 16-bit precision
- Delta compression for position updates

**Latency Mitigation**:
- Client-side prediction (ship movement)
- Interpolation (remote players)
- Server reconciliation (correction smoothing)
- Fast tick rate (30-60 Hz)

**Scalability**:
- Server authoritative (no peer-to-peer complexity)
- Dedicated servers (better performance than player-hosted)
- Edgegap edge computing (lower latency worldwide)
- Interest management (only sync nearby objects)

---

### Network Costs

**Per-Player Bandwidth** (estimated):
- Ship movement: ~1-2 KB/s (NetworkTransform)
- Chat messages: ~0.5 KB/s average
- Combat events: ~1 KB/s during action
- **Total**: ~3-5 KB/s per player

**Server Requirements** (16 players):
- CPU: Low (Unity physics runs on server)
- RAM: ~200-500 MB per server instance
- Bandwidth: ~50-80 KB/s total (16 players × 5 KB/s)
- Latency: <50ms target (Edgegap edge computing)

---

## Security & Anti-Cheat

### Server Authority Protections

**Movement Validation**:
- Server checks ship speed limits
- Physics constraints enforced server-side
- Impossible movements rejected (teleporting, speed hacking)

**Action Validation**:
- Weapon fire rate limited server-side
- Damage calculations server-only
- Economy transactions server-authoritative

**Chat Validation**:
- Message size limits (prevent flooding)
- Rate limiting (anti-spam)
- Profanity filtering server-side
- Message validation (prevent exploits)

### Known Security Gaps
- ⚠️ No encryption on messages (Mirror default is unencrypted)
- ⚠️ No sophisticated anti-cheat (relying on server validation only)
- 📋 Phase 2: Add SSL/TLS transport layer
- 📋 Phase 3: Integrate dedicated anti-cheat solution

---

## Known Issues & Limitations

### Current Limitations

**No Encryption** ⚠️
- Mirror's default transport is unencrypted
- Player data visible to packet sniffers
- **Risk**: Low (no sensitive data transmitted)
- **Fix**: Phase 2 - Add SSL/TLS transport

**No Voice Chat** 📋
- Only text chat implemented
- Voice requires separate solution
- **Phase 3**: Evaluate Vivox or Agora integration

**Limited Interest Management** 📋
- All players sync all objects in scene
- Inefficient for large player counts (>32)
- **Phase 2**: Implement spatial interest management

**No Reconnection Handling** 📋
- Connection drops boot player to menu
- No automatic reconnection
- **Phase 2**: Add reconnection grace period

---

### Technical Debt

**Hardcoded Port** ⚠️
- Port 7777 is hardcoded in many places
- Should be centralized in ServerConfig
- Low priority (works fine for now)

**No Load Balancing** 📋
- Single server per match
- No multi-server scaling
- Fine for Phase 1 (16 player max)
- Phase 3: Consider multi-server architecture

---

## Testing

### Test Coverage
- ✅ Editor-to-Editor multiplayer (localhost testing)
- ✅ Client-server prediction (ship movement smoothness)
- ✅ Server authority validation (movement limits)
- ✅ Edgegap deployment (production environment)
- ✅ Multiple clients (2-4 players tested)
- ⭕ Large player counts (16+ players not tested)
- ⭕ High latency scenarios (>200ms not tested)
- ⭕ Packet loss recovery (not systematically tested)

### Known Bugs
- **None reported in Phase 1 scope**

---

## Future Enhancements

### Phase 2 Improvements
- [ ] Add SSL/TLS encryption for transport
- [ ] Implement spatial interest management
- [ ] Add reconnection grace period (60 seconds)
- [ ] Server-side performance monitoring
- [ ] Bandwidth usage analytics

### Phase 3 Improvements
- [ ] Dedicated anti-cheat integration
- [ ] Voice chat system (Vivox/Agora)
- [ ] Multi-server load balancing
- [ ] Advanced matchmaking with skill-based rating
- [ ] Server browser with filters

---

## Cross-References

### Related GDD Sections
- [[Chat-System]] - Uses network architecture for messaging
- [[Ship-Physics]] - Client prediction for ship movement
- [[Combat-Systems]] - Server-authoritative damage
- [[Authentication]] - Player login/validation

### Related Scripts
- [[ServerConfig]] - Server address configuration
- [[WOSEdgegapBootstrap]] - Startup validation
- [[NetworkedNavalController]] - Client prediction example
- [[ChatManager]] - Network messaging example

### External Documentation
- [Mirror Networking Docs](https://mirror-networking.gitbook.io/)
- [Edgegap Documentation](https://docs.edgegap.com/)
- Unity Networking Best Practices

---

## Developer Guidelines

### When to Use [Command] vs [ClientRpc]

**Use [Command] when**:
- Client wants to perform an action (shoot weapon, send chat)
- Server needs to validate input
- Action affects authoritative game state

**Use [ClientRpc] when**:
- Server wants to notify all clients (explosion VFX, announcements)
- Action is cosmetic/visual (doesn't affect game state)
- Broadcasting events to multiple players

### SyncVar Best Practices
- Use for critical state only (health, throttle, faction)
- Avoid for high-frequency data (use NetworkTransform instead)
- Use hooks for change callbacks: `[SyncVar(hook = nameof(OnHealthChanged))]`
- Remember: SyncVars only sync Server → Clients (not Client → Server)

### Client Prediction Guidelines
- Predict only local player actions (not remote players)
- Always send [Command] to server with predicted action
- Let NetworkTransform handle reconciliation
- Don't predict destructive actions (weapon damage, death)

---

## Changelog

- **2025-01-XX**: Mirror Networking integrated
- **2025-01-XX**: ServerConfig ScriptableObject implemented
- **2025-01-XX**: Edgegap deployment configured
- **2025-01-XX**: WOSEdgegapBootstrap validation added
- **2025-01-XX**: Client-side prediction implemented in NetworkedNavalController
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Core networking complete and production-ready
**Next Steps**: Phase 2 encryption and interest management
**Blockers**: None
