---
tags: [technical, infrastructure, tools]
status: ✅ IMPLEMENTED
last-updated: 2025-11-17
related: [[Performance-Targets]], [[Network-Architecture]], [[Development-Status]]
---

# 🛠️ Technology Stack
## Implemented Technologies & Development Tools

**Document Purpose**: Comprehensive reference of all technologies, frameworks, and tools currently implemented in Fathoms Deep. This reflects the actual production stack as of Phase 1 completion.

---

## 🎮 Core Engine

### Unity 6000.0.55f1
**Status**: ✅ IMPLEMENTED (Primary Engine)

**Configuration**:
- **Rendering**: Universal Render Pipeline (URP) 2D
- **Platform**: PC (Windows Primary, macOS/Linux Planned)
- **Architecture**: 64-bit builds
- **API Compatibility**: .NET Standard 2.1

**Why Unity 6**:
- Latest LTS features and performance improvements
- Enhanced URP 2D rendering for large-scale naval environments
- Improved multiplayer networking support
- Better memory management for 300+ player servers

**Key Features in Use**:
- ✅ 2D Feature Set (optimized physics and sprite rendering)
- ✅ URP 2D Renderer (custom render features for water/weather)
- ✅ Modern Input System (rebindable controls)
- ✅ Addressable Assets System (dynamic content loading)
- ✅ Timeline System (cutscenes and scripted events)
- ✅ Unity.Mathematics (high-performance calculations)
- ✅ Burst Compiler (optimized physics and ballistics)
- ✅ Job System (multi-threaded naval calculations)

---

## 🌐 Networking Stack

### Mirror Networking Framework
**Status**: ✅ IMPLEMENTED
**Version**: Latest Stable (2024)
**Purpose**: Authoritative multiplayer networking for 300+ player servers

**Architecture**:
- **Transport**: KCP (reliable UDP) for real-time combat
- **Model**: Client-Server (authoritative server)
- **Prediction**: Client-side prediction with server reconciliation
- **Interest Management**: Spatial partitioning for performance

**Implemented Features**:
- ✅ **NetworkedNavalController**: Multiplayer ship control with client prediction
- ✅ **Server Authority**: All critical calculations server-side
- ✅ **Lag Compensation**: Smooth gameplay under network latency
- ✅ **Spatial Culling**: Network visibility optimization
- ✅ **State Synchronization**: Ship position, rotation, and state

**Why Mirror**:
- Open-source with active community
- Proven scalability (supports 300+ CCU target)
- Excellent documentation and examples
- Compatible with Edgegap deployment

**Related Scripts**:
- [[NetworkedNavalController]] - Multiplayer ship control
- [[ServerConfig]] - Server configuration management

---

### Edgegap Cloud Deployment
**Status**: ✅ IMPLEMENTED
**Purpose**: Distributed edge computing for low-latency multiplayer

**Configuration**:
- **Deployment**: Containerized Unity server builds
- **Regions**: Multi-region deployment for global coverage
- **Auto-Scaling**: Dynamic server provisioning based on demand
- **Dev/Prod**: Automatic environment switching

**Implementation**:
- ✅ [[ServerConfig]] script handles dev/production URLs
- ✅ Automatic server selection based on build configuration
- ✅ JWT authentication integrated with backend

**Benefits**:
- Sub-50ms latency for most players
- Automatic scaling during peak hours
- Cost-effective pay-per-use model
- Simplified DevOps for solo developer

---

## 🖥️ Backend Services

### JWT Authentication Server
**Status**: ✅ IMPLEMENTED
**Technology**: Node.js + Express + PostgreSQL (assumed)
**Purpose**: User authentication and session management

**Implemented Features**:
- ✅ JWT token-based authentication
- ✅ Secure token storage (PlayerPrefs encrypted)
- ✅ Login/Register endpoints
- ✅ Token validation and refresh

**API Endpoints**:
```
POST /api/auth/register - Create new account
POST /api/auth/login - Authenticate user
POST /api/auth/validate - Verify token
POST /api/auth/refresh - Refresh expired token
```

**Security**:
- HTTPS-only communication
- Encrypted token storage client-side
- Server-side validation of all requests
- Rate limiting for brute-force protection

**Related Scripts**:
- [[LoginController]] - Client-side authentication
- [[Authentication]] - Token management

---

## 🎨 UI & Visual Systems

### Modern UI Pack (MUIP)
**Status**: ✅ IMPLEMENTED
**Purpose**: Professional UI components with modern aesthetics

**Components in Use**:
- Animated buttons with hover/click feedback
- Custom input fields with validation states
- Modal dialogs and panels
- Progress bars and loading indicators
- Toggle switches and checkboxes

**Customization**:
- Themed for naval/military aesthetic
- Custom color schemes per UI context
- Accessibility-compliant contrast ratios

---

### TextMeshPro (TMP)
**Status**: ✅ IMPLEMENTED
**Purpose**: High-quality text rendering

**Implementation**:
- All UI text uses TMP components
- Custom fonts for naval theme
- Dynamic text sizing for accessibility
- Rich text markup for chat system

**Performance**:
- GPU-based text rendering
- Efficient memory usage
- Sharp text at all zoom levels

---

### Unity Input System
**Status**: ✅ IMPLEMENTED
**Purpose**: Modern, rebindable input handling

**Features**:
- **Action Maps**: Ship controls, camera, UI navigation
- **Multi-Device**: Keyboard, mouse, gamepad, joystick
- **Rebinding**: User-customizable control schemes
- **Conflict Resolution**: Prevents duplicate bindings

**Implemented Actions**:
- Ship throttle control (8 speeds)
- Camera zoom, pan, toggle modes
- Waypoint system controls
- Chat and menu navigation
- Debug UI toggle

**Accessibility**:
- Alternative input methods
- Hold-to-activate options
- Customizable sensitivity
- One-handed gameplay support

---

## 📊 Data & Persistence

### SQLite Database (Local)
**Status**: 🚧 PARTIAL (Planned for Phase 3)
**Purpose**: Local player data and preferences

**Planned Use**:
- Player settings and preferences
- Cached ship configurations
- Offline progression data
- Achievement tracking

---

### Cloud Save Integration
**Status**: 📋 PLANNED (Phase 3)
**Platforms**: Steam Cloud, Epic Games Cloud Save

**Planned Features**:
- Automatic save synchronization
- Cross-device progression
- Save conflict resolution
- Backup and restore

---

## 🎵 Audio Systems

### Unity Audio System
**Status**: ✅ IMPLEMENTED (Basic)
**Status**: 📋 PLANNED (FMOD Integration - Phase 3)

**Current Implementation**:
- Unity's built-in audio system
- 2D spatial audio for UI
- Basic sound effects

**Planned FMOD Integration (Phase 3)**:
- **3D Spatial Audio**: Positional sound for tactical advantage
- **Dynamic Music**: Adaptive orchestral score
- **Audio Streaming**: High-quality naval combat audio
- **VoIP Integration**: Fleet coordination voice chat

---

## 🧪 Development Tools

### Version Control
**Status**: ✅ IMPLEMENTED
**System**: Git + GitHub

**Configuration**:
- **.gitignore**: Excludes Unity temp files, builds
- **LFS**: Large file storage for assets
- **Branching**: Main, dev, feature branches

---

### AI Development Assistant
**Status**: ✅ ACTIVE
**Tool**: Claude Code (Anthropic)

**Usage**:
- Code generation and refactoring
- Documentation writing
- Architecture planning
- Bug investigation
- Design document creation

**CLAUDE.md Integration**:
- Project-specific guidance document
- Coding standards and conventions
- Architecture patterns
- Common tasks and workflows

---

### Unity Editor Extensions
**Status**: ✅ IMPLEMENTED

**Tools in Use**:
- **Unity Cloud Build**: Automated builds (planned)
- **Addressables**: Content management
- **Debug UI**: Custom in-game debugging tools
- **Scene Management**: Multi-scene workflows

---

## 📦 Package Dependencies

### Unity Packages (via Package Manager)
```json
{
  "com.unity.render-pipelines.universal": "17.0.3",
  "com.unity.inputsystem": "1.8.2",
  "com.unity.textmeshpro": "3.2.0",
  "com.unity.mathematics": "1.3.2",
  "com.unity.addressables": "2.3.1",
  "com.unity.timeline": "1.8.6",
  "com.unity.burst": "1.8.13",
  "com.unity.collections": "2.5.1",
  "com.unity.jobs": "0.70.0"
}
```

### Third-Party Assets
- **Mirror Networking**: Latest stable from Asset Store
- **Modern UI Pack**: MUIP from Asset Store
- **KCP Transport**: Mirror transport layer

---

## 🔒 Security & Anti-Cheat

### Server Authority
**Status**: ✅ IMPLEMENTED

**Approach**:
- All critical calculations server-side
- Client input validation
- State verification
- Movement validation

### Planned Security (Phase 3)
**Status**: 📋 PLANNED

- **Code Obfuscation**: Protect against reverse engineering
- **Integrity Checking**: Validate game files at runtime
- **Memory Protection**: Prevent memory editing
- **Statistical Monitoring**: Detect impossible performance

---

## 🧰 Build Pipeline

### Current Build Process
**Status**: ✅ IMPLEMENTED

**Platforms**:
- Windows 64-bit (Primary)
- Dedicated Server (Linux)

**Configuration**:
- Development builds for testing
- Release builds with optimizations
- Server builds without graphics

### Planned CI/CD (Phase 3)
**Status**: 📋 PLANNED

- **Unity Cloud Build**: Automated multi-platform builds
- **Automated Testing**: Unit and integration tests
- **Quality Gates**: Performance validation before deployment
- **Version Management**: Semantic versioning

---

## 📊 Analytics & Monitoring

### Unity Analytics
**Status**: 📋 PLANNED (Phase 3)

**Planned Tracking**:
- Player behavior patterns
- Popular ships and loadouts
- Tactical performance metrics
- Session duration and retention

**Privacy**:
- GDPR-compliant data collection
- User consent required
- Anonymous analytics only
- Opt-out available

---

## 🎯 Performance Optimization Stack

### Unity.Mathematics
**Status**: ✅ IMPLEMENTED
**Purpose**: High-performance mathematical calculations

**Usage**:
- Ship physics calculations
- Ballistics and trajectory
- Vector/quaternion operations
- SIMD optimizations

---

### Burst Compiler
**Status**: ✅ IMPLEMENTED
**Purpose**: Native code compilation for performance-critical systems

**Optimized Systems**:
- Ship physics updates
- Ocean chunk generation
- Collision detection
- Future: Ballistics calculations

---

### Job System
**Status**: ✅ IMPLEMENTED
**Purpose**: Multi-threaded game logic

**Parallelized Systems**:
- Ocean chunk updates
- Ship physics calculations
- Future: AI pathfinding
- Future: Damage calculations

---

## 🔧 Development Environment

### Recommended IDE
- **Primary**: Visual Studio 2022
- **Alternative**: JetBrains Rider
- **Lightweight**: Visual Studio Code

### System Requirements (Development)
- **OS**: Windows 10/11 64-bit
- **CPU**: 6+ core processor
- **RAM**: 16+ GB
- **GPU**: GTX 1060 or better
- **Storage**: 100+ GB SSD

---

## 📈 Technology Roadmap

### Phase 2 Additions (Combat & Economy)
- ✅ Current stack sufficient for Phase 2
- No new major technologies required

### Phase 3 Additions (Advanced Features)
- 📋 FMOD Audio Integration
- 📋 Unity Analytics
- 📋 Cloud Save System
- 📋 Steam SDK Integration
- 📋 VoIP (Vivox or Discord SDK)

### Phase 4+ (MMO Scale)
- 📋 Distributed Server Architecture
- 📋 Database Scaling (PostgreSQL → Cluster)
- 📋 CDN for Asset Delivery
- 📋 Advanced Anti-Cheat

---

## 🔗 Related Documentation

### Technical Docs
- [[Performance-Targets]] - FPS, network, and memory goals
- [[Network-Architecture]] - Mirror implementation details
- [[Authentication]] - JWT login system

### Development Docs
- [[Development-Status]] - Current implementation status
- [[Phase-1-Complete]] - Completed Phase 1 systems
- [[CLAUDE.md]] - AI assistant project guidance

---

## 📝 Notes

### Technology Selection Philosophy
1. **Proven Reliability**: Choose battle-tested technologies
2. **Active Community**: Ensure ongoing support and updates
3. **Solo-Friendly**: Prioritize tools suitable for solo development
4. **Scalability**: Plan for 300+ player capacity from start
5. **Cost-Effective**: Minimize operational costs during development

### Version Pinning Strategy
- **Unity**: Pin to specific LTS version for stability
- **Packages**: Update cautiously, test thoroughly
- **Mirror**: Stay on stable branch, avoid bleeding edge
- **Third-Party**: Document exact versions in CLAUDE.md

---

**Last Updated**: 2025-11-17
**Phase**: Phase 1 Complete ✅
**Next Review**: Phase 2 Kickoff (Combat Systems Implementation)
