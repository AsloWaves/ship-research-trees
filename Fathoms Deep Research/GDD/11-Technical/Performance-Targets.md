---
tags: [technical, performance, optimization]
status: 📋 PLANNED
last-updated: 2025-11-17
related: [[Tech-Stack]], [[Network-Architecture]], [[Development-Status]]
---

# 🎯 Performance Targets & Optimization Goals
## Technical Performance Requirements for 300+ Player MMO

**Document Purpose**: Defines all performance targets, optimization requirements, and scalability goals for Fathoms Deep. These metrics guide development decisions and validate system implementations.

---

## 🖥️ Client Performance Targets

### Frame Rate (FPS) Requirements

#### Minimum Requirements (Target: 60 FPS)
**Status**: ✅ ACHIEVED (Phase 1)

**Scenarios**:
- **Solo Navigation**: 60+ FPS sustained
- **Small Battles (5-10 ships)**: 60 FPS minimum
- **Medium Battles (20-50 ships)**: 60 FPS target, 45 FPS acceptable
- **Large Battles (100+ ships)**: 60 FPS target, 40 FPS acceptable
- **Massive Battles (200+ ships)**: 45 FPS minimum, 30 FPS degraded

**Current Phase 1 Performance**:
- ✅ Editor: 60+ FPS with single ship
- ✅ Build: 120+ FPS with single ship
- ⚠️ Multiplayer: Untested with 300+ players

**Optimization Strategies**:
- **LOD System**: Reduce detail on distant ships
- **Culling**: Network interest management and rendering culling
- **Object Pooling**: Reuse projectiles, effects, debris
- **Instanced Rendering**: Batch similar objects (waves, particles)
- **Dynamic Quality**: Auto-reduce settings under load

---

#### Recommended Specifications (Target: 90+ FPS)
**High-End Experience**

**Scenarios**:
- **All Combat Scenarios**: 90+ FPS sustained
- **Ultra Settings**: 60+ FPS with max visual quality
- **4K Resolution**: 60+ FPS at 3840x2160

**Hardware Profile**:
- RTX 3070 / RX 6700 XT or better
- 16 GB RAM
- i7-10700K / Ryzen 7 3700X
- SSD storage

---

### Memory Budget

#### RAM Allocation Targets
**Status**: 📋 PLANNED

**Normal Gameplay** (Target: < 6 GB):
- **Base Game**: 2.0 GB
- **Ship Assets**: 1.5 GB (streaming)
- **Ocean Environment**: 800 MB
- **UI and Menus**: 400 MB
- **Networking Buffers**: 300 MB
- **Audio**: 500 MB
- **Overhead**: 500 MB

**Intense Battles** (Target: < 8 GB):
- **Active Ships**: +1.0 GB (100+ ships visible)
- **Effects/Particles**: +500 MB (combat effects)
- **Audio Instances**: +200 MB (spatial audio)
- **Total Peak**: 7.5-8.0 GB

**Memory Optimization**:
- ✅ Addressable Assets for streaming
- 📋 Texture compression (Phase 2)
- 📋 Audio streaming (FMOD in Phase 3)
- 📋 Aggressive GC optimization

---

#### VRAM Allocation Targets
**GPU Memory Budget**

**Minimum (4 GB VRAM)**:
- **Textures**: 2.0 GB (compressed)
- **Render Targets**: 800 MB
- **UI Assets**: 400 MB
- **Shaders**: 200 MB
- **Buffers**: 600 MB

**Recommended (6+ GB VRAM)**:
- **Textures**: 3.5 GB (high quality)
- **Render Targets**: 1.2 GB (higher resolution)
- **UI Assets**: 600 MB
- **Effects**: 700 MB
- **Buffers**: 1.0 GB

**VRAM Optimization**:
- Texture atlasing
- Mipmap streaming
- Dynamic resolution scaling
- LOD texture quality

---

### Load Time Targets

#### Scene Transitions
**Status**: 📋 PLANNED

**Target Times**:
- **Ocean ↔ Port**: < 3 seconds (SSD), < 5 seconds (HDD)
- **Combat Zone Entry**: < 2 seconds
- **Ship Spawn**: < 500 ms
- **UI Panel Open**: < 100 ms instant feel

**Current Status**:
- ✅ Basic scene loading functional
- ⚠️ No loading screens implemented
- ⚠️ No progress indicators

**Optimization Strategies**:
- Addressable asset preloading
- Async scene loading
- Asset bundling by zone
- Predictive loading (load nearby zones)

---

#### Initial Game Launch
**Cold Start Performance**

**Targets**:
- **Splash to Menu**: < 15 seconds (SSD), < 20 seconds (HDD)
- **Menu to Gameplay**: < 10 seconds (first load)
- **Subsequent Loads**: < 5 seconds (cached)

**Loading Phases**:
1. **Engine Init**: 2-3 seconds
2. **Core Assets**: 3-5 seconds
3. **UI Load**: 2-3 seconds
4. **Auth/Network**: 2-4 seconds
5. **Scene Ready**: 1-2 seconds

---

## 🌐 Network Performance Targets

### Latency Requirements

#### Client-Server Latency
**Status**: 📋 PLANNED (Edgegap deployment)

**Optimal Performance** (< 50ms):
- ✅ Perfect responsiveness
- ✅ No visible lag
- ✅ Instant hit registration
- ✅ Smooth ship movement

**Good Performance** (50-100ms):
- ✅ Excellent responsiveness
- ✅ Minor lag compensation
- ✅ Accurate hit detection
- ⚠️ Slight prediction artifacts

**Acceptable Performance** (100-150ms):
- ⚠️ Noticeable lag
- ⚠️ Visible prediction correction
- ⚠️ Delayed hit feedback
- ✅ Playable with compensation

**Poor Performance** (> 150ms):
- ❌ Significant lag
- ❌ Frustrating combat experience
- ❌ Prediction errors frequent
- ❌ Consider region switching

**Edgegap Benefits**:
- Target: < 50ms for 80% of players
- Multi-region deployment
- Auto-scaling for demand
- Low-latency edge computing

---

### Bandwidth Requirements

#### Per-Client Bandwidth
**Status**: 📋 PLANNED

**Minimum Connection** (5 Mbps):
- Basic gameplay functional
- Reduced update rate (10 Hz)
- Visual degradation acceptable
- Combat playable but not optimal

**Recommended Connection** (25+ Mbps):
- Full update rate (20-30 Hz)
- All visual features enabled
- Smooth multiplayer experience
- No bandwidth-related issues

**Bandwidth Usage by Activity**:
- **Solo Navigation**: 50-100 KB/s
- **Small Battles**: 100-200 KB/s
- **Medium Battles**: 200-400 KB/s
- **Large Battles**: 400-800 KB/s
- **Massive Battles**: 800-1,500 KB/s (compressed)

**Bandwidth Optimization**:
- Delta compression
- Spatial interest management
- Priority-based updates
- Dynamic quality scaling

---

#### Total Server Bandwidth
**300 Player Capacity Planning**

**Upload Bandwidth** (per server):
- **Average**: 60-90 Mbps (300 players × 200-300 KB/s)
- **Peak Combat**: 150-200 Mbps (all players fighting)
- **Baseline**: 30 Mbps (distributed navigation)

**Download Bandwidth**:
- Much lower (client input only)
- ~10-20 Mbps for 300 players

**Edgegap Scaling**:
- Auto-provision servers as needed
- Regional load balancing
- Peak capacity handling

---

### Network Update Rates

#### Synchronization Frequency
**Status**: 📋 PLANNED

**Critical Systems** (30 Hz):
- Ship position/rotation
- Combat state
- Damage events
- Player input

**Important Systems** (15 Hz):
- Ship statistics
- Module states
- Crew status
- Inventory changes

**Low-Priority Systems** (5 Hz):
- Economy updates
- Chat messages
- UI state
- Cosmetic effects

**Adaptive Rate Scaling**:
- Reduce rates under high load
- Prioritize nearby/visible ships
- Graceful degradation

---

## 🖥️ Server Performance Targets

### Server Capacity

#### Player Capacity per Server
**Status**: 📋 PLANNED

**Target Capacity**: 300+ concurrent players

**Capacity Breakdown**:
- **Baseline**: 300 players scattered
- **Combat Clusters**: 150 players in battle
- **Economic Activity**: 100 players trading
- **Idle/Docked**: 50 players in ports

**Scaling Strategy**:
- Horizontal scaling (multiple servers)
- Regional distribution (Edgegap)
- Dynamic server provisioning
- Load balancing between servers

---

#### Server Resource Limits

**CPU Usage**:
- **Target**: < 70% average, < 90% peak
- **300 Players**: ~60-80% CPU (8-core server)
- **Physics**: 20-30% CPU
- **Networking**: 15-25% CPU
- **Game Logic**: 20-30% CPU
- **Overhead**: 10-15% CPU

**Server Memory**:
- **Target**: < 8 GB RAM for 300 players
- **Base Server**: 2 GB
- **Player Data**: 4-5 GB (300 × 15-20 MB each)
- **World State**: 1 GB
- **Buffers**: 500 MB
- **Overhead**: 500 MB

**Network Thread Performance**:
- **Target**: < 16ms per tick (60 Hz)
- **Packet Processing**: 5-8ms
- **State Updates**: 3-5ms
- **Validation**: 2-3ms
- **Margin**: 2-4ms

---

### Server Tick Rate

#### Simulation Update Frequency
**Status**: 📋 PLANNED

**Physics Simulation**: 60 Hz (16.67ms per tick)
- Ship physics updates
- Collision detection
- Projectile simulation
- Environmental effects

**Network Broadcast**: 20-30 Hz (33-50ms)
- Client state updates
- Synchronized to client needs
- Adaptive based on load

**Game Logic**: 30 Hz (33ms)
- AI decisions
- Economy updates
- Zone management
- Event processing

**Optimization**:
- Critical systems 60 Hz
- Non-critical systems lower rates
- Dynamic rate adjustment
- Load-based throttling

---

## 📊 Scalability Testing Targets

### Load Testing Requirements

#### Multiplayer Stress Tests
**Status**: ⚠️ NOT TESTED

**Test Scenarios**:

**Small Scale** (10-20 players):
- ✅ Phase 1: Functional
- 📋 Phase 2: Combat testing needed

**Medium Scale** (50-100 players):
- 📋 Phase 3 target
- Test server stability
- Measure performance degradation
- Identify bottlenecks

**Large Scale** (150-250 players):
- 📋 Phase 4 target
- Full server load testing
- Network optimization validation
- Database performance under load

**Full Scale** (300+ players):
- 📋 Phase 5 target (MMO readiness)
- Maximum capacity validation
- Failover and redundancy testing
- Peak load handling

**Test Methodology**:
- Bot simulation for player count
- Real player tests (alpha/beta)
- Automated performance monitoring
- Progressive load increases

---

### Performance Degradation Limits

#### Acceptable Quality Reduction
**Status**: 📋 PLANNED

**Client-Side Degradation**:
- **50-100 players visible**: Reduce particle quality
- **100-150 players**: Lower texture LOD
- **150-200 players**: Reduce update rates
- **200+ players**: Aggressive culling, simplified rendering

**Server-Side Degradation**:
- **200 players**: Normal performance
- **250 players**: Reduce non-critical updates
- **275 players**: Aggressive optimization mode
- **300 players**: Maximum capacity, degraded features
- **320+ players**: Queue or reject new connections

**Never Compromise**:
- ✅ Core combat mechanics
- ✅ Ship physics accuracy
- ✅ Damage calculations
- ✅ Economy integrity

---

## 🧪 Benchmarking & Profiling

### Performance Monitoring

#### Real-Time Metrics
**Status**: ✅ IMPLEMENTED (Debug UI - Phase 1)

**Current Metrics**:
- ✅ FPS counter
- ✅ Ship position/velocity
- ✅ Throttle state
- ✅ Camera mode

**Planned Metrics** (Phase 2+):
- 📋 Network latency (ping)
- 📋 Packet loss percentage
- 📋 CPU/GPU usage
- 📋 Memory allocation
- 📋 Draw calls
- 📋 Active network objects

---

#### Profiling Tools
**Status**: 📋 PLANNED

**Unity Profiler**:
- CPU usage breakdown
- Memory allocation tracking
- Rendering performance
- Physics simulation cost
- Networking overhead

**Custom Analytics**:
- Average FPS per session
- Network quality statistics
- Loading time tracking
- Performance regression detection

**Third-Party Tools** (Planned):
- Unity Cloud Diagnostics
- Custom telemetry dashboard
- Real-time alert system

---

## 🎯 Optimization Priorities

### Phase 2 Optimization Goals

**Combat Performance**:
- 📋 Projectile pooling system
- 📋 Damage calculation optimization
- 📋 Combat effect LOD
- 📋 Efficient collision detection

**Network Optimization**:
- 📋 Implement interest management
- 📋 State compression
- 📋 Delta updates
- 📋 Prediction and reconciliation

---

### Phase 3 Optimization Goals

**Large-Scale Battles**:
- 📋 Advanced LOD system
- 📋 Spatial partitioning
- 📋 Instanced rendering
- 📋 Culling improvements

**Memory Management**:
- 📋 Asset streaming
- 📋 Texture compression
- 📋 Audio streaming (FMOD)
- 📋 GC optimization

---

### Phase 4+ MMO Optimization

**300+ Player Support**:
- 📋 Distributed server architecture
- 📋 Database query optimization
- 📋 CDN integration
- 📋 Advanced caching strategies

---

## 🔧 Platform-Specific Targets

### Windows PC (Primary)

**Minimum Spec Performance**:
- 60 FPS @ 1920×1080 (Medium settings)
- 4 GB RAM usage
- 2 GB VRAM
- 5-10 second load times (HDD)

**Recommended Spec Performance**:
- 90+ FPS @ 1920×1080 (High settings)
- 6 GB RAM usage
- 4 GB VRAM
- 2-5 second load times (SSD)

---

### macOS (Planned)

**Metal Rendering**:
- 60 FPS target (Apple Silicon)
- 45-60 FPS (Intel Macs)
- Native Metal optimizations

---

### Linux (Planned)

**Vulkan Rendering**:
- 60 FPS target
- Performance parity with Windows
- Distribution compatibility testing

---

## 📊 Success Criteria

### Phase 1 Success Metrics
**Status**: ✅ ACHIEVED

- ✅ 60+ FPS in editor (single player)
- ✅ 120+ FPS in build (single player)
- ✅ Smooth camera following
- ✅ Responsive controls (< 16ms input lag)
- ✅ Stable scene transitions

---

### Phase 2 Success Criteria
**Status**: 📋 PENDING

- 📋 60 FPS with 10-20 players in combat
- 📋 < 100ms network latency (Edgegap)
- 📋 < 5% packet loss
- 📋 Projectiles pooled efficiently
- 📋 No frame drops during weapon fire

---

### Phase 3 Success Criteria (MMO Readiness)
**Status**: 📋 PLANNED

- 📋 60 FPS with 100+ players visible
- 📋 300 players per server stable
- 📋 < 50ms average latency
- 📋 < 8 GB RAM usage at peak
- 📋 < 15 second load times
- 📋 Graceful degradation under load

---

## 🔗 Related Documentation

### Technical Docs
- [[Tech-Stack]] - All implemented technologies
- [[Network-Architecture]] - Multiplayer implementation
- [[Development-Status]] - Current progress

### Phase Docs
- [[Phase-1-Complete]] - Phase 1 retrospective
- [[Phase-2-InProgress]] - Current optimization work
- [[Phase-3-Plan]] - MMO scaling roadmap

---

## 📝 Notes

### Performance Philosophy
1. **Measure First**: Profile before optimizing
2. **User Experience**: Responsiveness > raw FPS
3. **Graceful Degradation**: Reduce quality, maintain gameplay
4. **Network Priority**: Optimize for multiplayer from start
5. **Solo Developer Reality**: Balance perfection with progress

### Testing Strategy
- ✅ Phase 1: Manual testing, debug UI
- 📋 Phase 2: Bot testing (10-50 players)
- 📋 Phase 3: Alpha testing (100-200 real players)
- 📋 Phase 4: Beta testing (300+ players, stress tests)

---

**Last Updated**: 2025-11-17
**Phase**: Phase 1 Complete ✅
**Next Review**: Phase 2 Combat Implementation (Performance Validation Required)
