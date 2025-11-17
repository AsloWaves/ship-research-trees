# Asset Production Pipeline

**Document Status**: ⭕ NOT STARTED
**Tags**: [planned, phase3, art-audio, production]
**Priority**: LOW-MEDIUM (Phase 3 polish)
**Related Documents**: [Visual-Design.md](./Visual-Design.md), [Audio-Design.md](./Audio-Design.md), [Historical-Research.md](./Historical-Research.md)

---

## Overview

This document defines the complete asset production pipeline for Fathoms Deep, covering art asset creation, audio production, version control, quality assurance, and outsourcing workflows. The pipeline ensures consistent quality, historical accuracy, and efficient production across all visual and audio assets.

---

## 1. Pipeline Philosophy

### 1.1 Core Production Principles

**Quality Over Quantity**
- Every asset undergoes rigorous quality control
- Historical accuracy verified before final approval
- Performance benchmarking required for all assets
- Iteration encouraged until quality standards met

**Consistency Across Assets**
- Unified art style maintained across all ships, effects, and UI
- Audio design language consistent for all sound categories
- Technical specifications standardized (file formats, naming conventions)
- Documentation templates ensure complete asset information

**Collaboration and Communication**
- Clear handoff procedures between departments
- Regular cross-department reviews (art + audio + design + engineering)
- Feedback loops integrated into production workflow
- Knowledge sharing through documentation and asset libraries

**Scalability and Efficiency**
- Reusable components and modular design
- Template systems for rapid asset creation
- Automation tools for repetitive tasks
- Batch processing workflows for efficiency

---

## 2. Visual Asset Production Pipeline

### 2.1 Ship Asset Creation Workflow

**Phase 1: Historical Research and Reference Gathering**
- **Duration**: 2-4 days per ship class
- **Deliverables**: Reference package with photos, technical drawings, specifications
- **Process**:
  1. Identify ship class and historical period
  2. Gather museum photographs, historical photos, technical drawings
  3. Reference existing databases (see [Historical-Research.md](./Historical-Research.md))
  4. Compile dimension specifications, weapon placements, camouflage patterns
  5. Document unique visual characteristics and notable features
  6. Create reference board (digital or physical) for artist review

**Phase 2: Concept Art and Style Approval**
- **Duration**: 1-2 days per ship class
- **Deliverables**: Approved concept art with annotations
- **Process**:
  1. Sketch initial concept (top-down view, appropriate scale)
  2. Apply color palette based on nation and period
  3. Mark weapon placements, equipment, and key features
  4. Review with art director and historical consultant
  5. Iterate based on feedback (accuracy, style consistency)
  6. Final approval from art director before moving to production

**Phase 3: Asset Creation**
- **Duration**: 3-7 days per ship class (depending on tier/complexity)
- **Deliverables**: High-resolution ship sprite with layers
- **Process**:
  1. Create base ship silhouette at target resolution (see [Visual-Design.md](./Visual-Design.md))
  2. Add structural details (deck features, superstructure, weapons)
  3. Apply shading and lighting (consistent with lighting standard)
  4. Add nation-specific details (markings, flags, camouflage)
  5. Create damage state variants (0%, 25%, 50%, 75%, 100% damage)
  6. Generate texture maps if needed (normal maps, emission maps)
  7. Export final assets in correct format (PNG, RGBA, specified resolution)

**Phase 4: Technical Implementation**
- **Duration**: 1-2 days per ship class
- **Deliverables**: Unity-ready ship prefab with all components
- **Process**:
  1. Import sprite into Unity and configure texture settings
  2. Create ship prefab with sprite renderer and colliders
  3. Set up LOD system with distance-based switching
  4. Integrate damage state system (progressive damage visuals)
  5. Add particle effects (wake, smoke, fires, spray)
  6. Configure lighting response (if using dynamic lighting)
  7. Test rotation and movement (ensure smooth transform rotation)
  8. Verify scale relationships with other ships

**Phase 5: Performance Optimization and LOD Generation**
- **Duration**: 1 day per ship class
- **Deliverables**: Optimized asset with LOD variants
- **Process**:
  1. Generate LOD variants (simplified sprites for distant viewing)
  2. Test performance across target hardware (60 FPS minimum)
  3. Optimize texture compression (balance quality and file size)
  4. Verify draw call efficiency (sprite batching)
  5. Profile memory usage (stay within budget per ship)
  6. Create texture atlases if needed (group similar ships)
  7. Document performance characteristics (poly count, texture memory, draw calls)

**Phase 6: QA Testing and Historical Validation**
- **Duration**: 1-2 days per ship class
- **Deliverables**: QA report with approval or revision notes
- **Process**:
  1. Visual quality check (consistent with art style, no visual artifacts)
  2. Historical accuracy review by consultant (compare to reference materials)
  3. Performance testing (FPS, memory, draw calls on target hardware)
  4. In-game visibility testing (readable at all zoom levels)
  5. Damage state progression testing (smooth transitions)
  6. Integration testing (works correctly in all game modes)
  7. Final approval sign-off (art director + historical consultant)

**Total Timeline**: 9-18 days per ship class (1.5 - 3 weeks)

### 2.2 Environmental Asset Creation

**Ocean and Water Assets**
- **Water Shaders**: Unity shader graph or custom shader development
- **Wave Textures**: Tileable normal maps for wave effects
- **Foam Textures**: Sprite sheets for wake effects and splash
- **Color Ramps**: Gradient textures for water depth visualization
- **Performance**: Real-time wave simulation optimized for target hardware

**Weather Effect Assets**
- **Particle Systems**: Rain, snow, fog particle effects
- **Skybox Textures**: Dynamic skyboxes for different weather conditions
- **Post-Processing Profiles**: Weather-specific color grading and effects
- **Optimization**: LOD for particle effects (reduce density at distance)

**Port and Harbor Assets**
- **Building Modular Kit**: Reusable building components for port construction
- **Dockyard Props**: Cranes, warehouses, dry docks, fuel depots
- **Animated Props**: NPC ships, dockworkers, vehicles
- **Optimization**: Occlusion culling for complex port environments

**Combat Effect Assets**
- **Explosion Sprites**: Sprite sheets for explosions (various sizes)
- **Muzzle Flash Sprites**: Weapon-specific muzzle flash effects
- **Tracer Sprites**: Bullet tracers, shell trajectories
- **Smoke Particle Systems**: Fire smoke, gun smoke, screening smoke
- **Performance**: Particle pooling for efficient reuse

### 2.3 UI Asset Creation

**MUIP-Based UI Elements**
- **Buttons**: Various button styles (primary, secondary, danger, disabled)
- **Panels**: Background panels, dialog boxes, info cards
- **Icons**: Ship class icons, weapon icons, status indicators
- **Sliders**: Volume sliders, settings adjustments
- **Typography**: Font selection and sizing standards

**Custom UI Assets**
- **Ship Status Displays**: Hull integrity bars, speed indicators
- **Tactical Overlays**: Radar display, sonar screen, fire control
- **Mini-Map Elements**: Map backgrounds, territory colors, contact icons
- **Instrument Panels**: Analog gauge textures, period-correct UI elements

**UI Animation Assets**
- **Transitions**: Screen transitions, panel slide-ins
- **Button States**: Hover, pressed, disabled animations
- **Notifications**: Alert animations, message pop-ins
- **Loading Indicators**: Progress bars, spinners

### 2.4 Asset Naming Conventions

**Ship Sprites**
```
NATION_CLASS_VARIANT_STATE_RES.png

Examples:
USA_Iowa_1944_Intact_2048.png
UK_KingGeorgeV_1941_Damage50_2048.png
GER_Bismarck_1941_Critical_2048.png
JPN_Yamato_1945_Intact_2048.png
```

**Effects**
```
VFX_TYPE_DESCRIPTION_SIZE.png

Examples:
VFX_Explosion_Magazine_Large_512.png
VFX_MuzzleFlash_16inch_256.png
VFX_Splash_8inch_512.png
VFX_Smoke_Fire_Black_512.png
```

**UI Assets**
```
UI_CATEGORY_ELEMENT_STATE.png

Examples:
UI_Button_Primary_Normal.png
UI_Button_Primary_Hover.png
UI_Panel_Background_Dark.png
UI_Icon_Battleship_64.png
```

### 2.5 File Format Standards

**Sprite Assets**
- **Format**: PNG (lossless, alpha channel support)
- **Color Depth**: 32-bit RGBA
- **Compression**: Unity texture compression applied on import
- **Resolution**: Power-of-two dimensions preferred (512, 1024, 2048, 4096)

**Texture Assets**
- **Diffuse Maps**: PNG or TGA (32-bit RGBA)
- **Normal Maps**: PNG (RGB channels for normal data)
- **Emission Maps**: PNG (RGB for glow effects)
- **Masks**: PNG (grayscale or RGB for multiple masks)

**Source Files**
- **Photoshop**: PSD with organized layers and groups
- **Clip Studio Paint**: CLIP format with layers
- **Other Tools**: Native format + flattened PSD export for compatibility

---

## 3. Audio Asset Production Pipeline

### 3.1 Audio Asset Creation Workflow

**Phase 1: Historical Research and Audio Reference**
- **Duration**: 1-3 days per audio category
- **Deliverables**: Audio reference library with historical recordings
- **Process**:
  1. Identify audio requirement (weapon sound, engine sound, etc.)
  2. Gather historical recordings (archival audio, documentaries)
  3. Research technical specifications (gun caliber, engine type)
  4. Reference similar sounds for creative direction
  5. Document audio characteristics (tone, pitch, duration, intensity)
  6. Compile reference audio library for sound designer

**Phase 2: Sound Design and Creation**
- **Duration**: 2-5 days per audio category
- **Deliverables**: Raw audio assets (WAV format, high quality)
- **Process**:
  1. **Recording**: Capture original sounds (foley, field recordings)
  2. **Synthesis**: Generate sounds using audio synthesis tools
  3. **Layering**: Combine multiple sounds for complexity
  4. **Processing**: EQ, compression, reverb, effects
  5. **Variation**: Create multiple variants to prevent audio fatigue
  6. **Iteration**: Review and refine based on feedback
  7. **Final Export**: Export as high-quality WAV (48kHz, 24-bit)

**Phase 3: Audio Middleware Implementation**
- **Duration**: 2-3 days per audio system
- **Deliverables**: FMOD/Wwise project with integrated audio
- **Process**:
  1. Import audio assets into middleware (FMOD Studio or Wwise)
  2. Create audio events (fire weapon, engine start, explosion, etc.)
  3. Set up parameter controls (intensity, distance, pitch variation)
  4. Configure randomization (prevent repetition)
  5. Set up adaptive music layers (exploration, combat, tension)
  6. Create audio buses and mixing hierarchy
  7. Export middleware project for Unity integration

**Phase 4: Unity Integration**
- **Duration**: 1-2 days per audio system
- **Deliverables**: Unity-integrated audio with scripting
- **Process**:
  1. Import FMOD/Wwise Unity integration plugin
  2. Create audio event triggers in Unity scripts
  3. Configure 3D spatial audio (Audio Source settings)
  4. Set up audio occlusion and attenuation curves
  5. Implement dynamic music system (parameter passing)
  6. Test audio synchronization with visuals (gunfire, explosions)
  7. Verify audio playback across different scenarios

**Phase 5: Performance Optimization**
- **Duration**: 1-2 days per audio system
- **Deliverables**: Optimized audio with LOD and streaming
- **Process**:
  1. Compress audio assets (Vorbis OGG for music/ambient, WAV for short SFX)
  2. Implement audio LOD (reduce quality at distance)
  3. Set up audio streaming (stream long audio, preload short audio)
  4. Configure voice limiting (maximum simultaneous sounds)
  5. Profile audio CPU usage (must stay under 10%)
  6. Profile audio memory usage (stay within platform limits)
  7. Test performance with 300+ players (worst-case scenario)

**Phase 6: QA Testing and Audio Balance**
- **Duration**: 2-3 days per audio system
- **Deliverables**: QA report and final audio mix
- **Process**:
  1. Audio authenticity review (compare to historical recordings)
  2. Audio clarity testing (critical sounds always audible)
  3. Mixing and balance (proper volume relationships)
  4. Cross-platform testing (PC speakers, headphones, surround, console)
  5. Accessibility testing (subtitles, visual cues working correctly)
  6. Performance testing (no audio dropouts, glitches, or clipping)
  7. Final approval sign-off (audio director + historical consultant)

**Total Timeline**: 9-16 days per audio system (1.5 - 2.5 weeks)

### 3.2 Audio Asset Categories

**Weapon Sounds**
- **Light AA Guns (20mm-40mm)**: Rapid-fire sounds, brass ejection
- **Medium Guns (3"-6")**: Sharp cracks, mechanical reloading
- **Heavy Guns (8"-16")**: Thunderous booms, extended echoes
- **Torpedoes**: Launch, running, detonation
- **Depth Charges**: Splash, underwater explosion

**Engine Sounds**
- **Steam Turbines**: Turbine whine, steam hiss
- **Diesel Engines**: Rumble, mechanical clatter
- **Gas Turbines**: High-pitch whine
- **Nuclear Reactors**: Low hum, coolant pumps

**Environmental Sounds**
- **Ocean**: Wave patterns, splashes, underwater
- **Weather**: Rain, thunder, wind, snow
- **Port Ambience**: Dockyard activity, urban sounds
- **Combat Ambience**: Battle noise, explosions, fires

**Voice and Communication**
- **Crew Voices**: Bridge communications, damage reports
- **Radio Communications**: Formal naval protocols, static
- **Enemy Communications**: Intercepted enemy chatter
- **Historical Broadcasts**: News, political speeches

**Music**
- **Exploration**: Ambient, contemplative orchestral
- **Combat**: Intense, driving orchestral
- **Harbor**: Peaceful maritime themes
- **Victory/Defeat**: Triumphant fanfares or somber themes

**UI Sounds**
- **Button Clicks**: Mechanical switch sounds
- **Notifications**: Alert tones, warnings
- **Navigation**: Map interactions, waypoint setting
- **Combat Interface**: Target locks, weapon selections

### 3.3 Audio Naming Conventions

**Sound Effects**
```
SFX_CATEGORY_DESCRIPTION_VARIANT.wav

Examples:
SFX_Weapon_16inchGun_Fire_01.wav
SFX_Engine_SteamTurbine_Idle_Loop.wav
SFX_Explosion_Magazine_Large_01.wav
SFX_Ocean_Waves_Moderate_Loop.wav
```

**Music Tracks**
```
MUS_TYPE_INTENSITY_LAYER.ogg

Examples:
MUS_Exploration_Calm_Base.ogg
MUS_Combat_High_Percussion.ogg
MUS_Harbor_Peaceful_USA.ogg
MUS_Victory_Triumphant.ogg
```

**Voice Lines**
```
VO_NATION_ROLE_LINE_VARIANT.wav

Examples:
VO_USA_Captain_OrderFullSpeed_01.wav
VO_UK_Engineer_DamageReport_03.wav
VO_GER_Gunnery_TargetAcquired_02.wav
VO_JPN_Radio_EnemyContact_01.wav
```

### 3.4 Audio File Format Standards

**Short Sound Effects** (< 5 seconds)
- **Format**: WAV (uncompressed)
- **Sample Rate**: 48kHz
- **Bit Depth**: 24-bit
- **Channels**: Mono (positional sounds) or Stereo (UI sounds)
- **Rationale**: Minimal latency for immediate playback

**Long Sound Effects** (> 5 seconds)
- **Format**: Vorbis OGG (compressed)
- **Quality**: Q7-Q8 (~192-224 kbps VBR)
- **Sample Rate**: 48kHz
- **Channels**: Mono or Stereo
- **Rationale**: Memory efficiency for ambient loops

**Music**
- **Format**: Vorbis OGG (compressed)
- **Quality**: Q8-Q9 (~224-256 kbps VBR)
- **Sample Rate**: 48kHz
- **Channels**: Stereo
- **Rationale**: High quality with reasonable file size

**Voice/Dialog**
- **Format**: Vorbis OGG (compressed)
- **Quality**: Q6-Q7 (~160-192 kbps VBR)
- **Sample Rate**: 44.1kHz or 48kHz
- **Channels**: Mono
- **Rationale**: Speech-optimized compression

---

## 4. Version Control and Asset Management

### 4.1 Version Control System

**Git LFS for Large Assets**
- All binary assets (PSD, PNG, WAV, OGG) stored in Git LFS
- Source files and exported assets both versioned
- Commit messages follow convention: `[Asset Type] Description`
- Example: `[Ship] Add USS Iowa 1944 variant with damage states`

**Repository Structure**
```
/Assets
  /Art
    /Ships
      /USA
        /Iowa-Class
          Iowa_1944_Source.psd
          Iowa_1944_Intact_2048.png
          Iowa_1944_Damage50_2048.png
          Iowa_1944_Metadata.json
      /UK
      /Germany
      /Japan
    /Effects
      /Explosions
      /MuzzleFlashes
      /Smoke
    /UI
      /Buttons
      /Panels
      /Icons
  /Audio
    /SFX
      /Weapons
      /Engines
      /Environment
    /Music
      /Exploration
      /Combat
      /Harbor
    /Voice
      /USA
      /UK
      /Germany
      /Japan
  /Middleware
    /FMOD
      /FMOD_Project.fspro
      /Build
    /Wwise (alternative)
```

**Asset Metadata**
- JSON sidecar files with asset information
- Tracks: Author, creation date, historical sources, technical specs
- Example metadata file: `Iowa_1944_Metadata.json`
```json
{
  "assetName": "USS Iowa BB-61 1944 Configuration",
  "nation": "USA",
  "shipClass": "Iowa-Class",
  "year": 1944,
  "tier": 10,
  "artist": "John Doe",
  "creationDate": "2025-11-17",
  "resolution": "2048x2048",
  "fileFormat": "PNG RGBA",
  "damageStates": ["Intact", "Damage25", "Damage50", "Damage75", "Critical"],
  "historicalSources": [
    "Naval History and Heritage Command Photo Archive",
    "Iowa-Class Technical Manual 1944",
    "Museum Ship USS Iowa Reference Photos"
  ],
  "technicalSpecs": {
    "texturMemory": "16MB",
    "drawCalls": 1,
    "triangles": 0 (sprite-based)
  },
  "approvals": {
    "artDirector": "Jane Smith - 2025-11-18",
    "historicalConsultant": "Dr. Naval Historian - 2025-11-19"
  }
}
```

### 4.2 Asset Library and Organization

**Centralized Asset Library**
- Internal wiki or documentation system with asset browser
- Searchable by nation, ship class, time period, asset type
- Preview thumbnails for quick identification
- Links to source files and metadata

**Asset Reuse Strategy**
- Component library for modular construction (turrets, radar, equipment)
- Texture library for shared materials (camouflage patterns, metal surfaces)
- Effect templates for consistent visual style
- Audio variations for preventing repetition

**Asset Status Tracking**
- **Concept**: Initial concept stage, not approved
- **In Progress**: Currently being created
- **Review**: Submitted for QA and approval
- **Revision**: Requires changes based on feedback
- **Approved**: Passed QA, ready for integration
- **Integrated**: Implemented in Unity, available for use
- **Deprecated**: Old asset, replaced by newer version

### 4.3 Backup and Disaster Recovery

**Backup Strategy**
- **Real-time**: Git commits and pushes to remote repository
- **Daily**: Automated backups of entire repository to NAS
- **Weekly**: Full backup to cloud storage (Google Drive, Dropbox, AWS S3)
- **Monthly**: Archive backup to external hard drive (off-site storage)

**Disaster Recovery Plan**
1. Primary: Restore from Git repository (remote origin)
2. Secondary: Restore from daily NAS backup (24-hour loss maximum)
3. Tertiary: Restore from weekly cloud backup (1-week loss maximum)
4. Last Resort: Restore from monthly external drive (1-month loss maximum)

---

## 5. Quality Assurance and Testing

### 5.1 Visual Asset QA Checklist

**Technical Quality**
- [ ] Resolution meets specifications (correct power-of-two dimensions)
- [ ] File format correct (PNG RGBA for sprites)
- [ ] No visual artifacts (aliasing, compression, color banding)
- [ ] Alpha channel clean (no fringing, proper transparency)
- [ ] Layers organized in source file (easy to modify)
- [ ] Proper color space (sRGB for Unity)

**Historical Accuracy**
- [ ] Ship silhouette matches historical photographs
- [ ] Weapon placements historically accurate
- [ ] Camouflage pattern authentic to time period
- [ ] National markings correct (flags, hull numbers, insignia)
- [ ] Equipment and details period-appropriate
- [ ] Historical consultant sign-off obtained

**Art Style Consistency**
- [ ] Matches established art style guide
- [ ] Lighting consistent with other assets
- [ ] Color palette appropriate to nation and period
- [ ] Detail level appropriate to ship tier
- [ ] Damage states consistent with other ships
- [ ] Visual clarity at all zoom levels

**Performance**
- [ ] Frame rate impact acceptable (60 FPS maintained)
- [ ] Texture memory within budget
- [ ] Draw calls minimized (sprite batching working)
- [ ] LOD system functioning correctly
- [ ] No performance spikes during damage state changes
- [ ] Works correctly on minimum spec hardware

**In-Game Testing**
- [ ] Ship rotates smoothly (Unity transform rotation)
- [ ] Damage progression displays correctly
- [ ] Visual effects properly attached (wake, smoke, fires)
- [ ] Scale relationship correct with other ships
- [ ] Lighting response correct (if using dynamic lighting)
- [ ] UI elements display correctly (ship name, health bar)

### 5.2 Audio Asset QA Checklist

**Technical Quality**
- [ ] Audio file format correct (WAV for short SFX, OGG for long/music)
- [ ] Sample rate correct (48kHz for SFX, 48kHz/44.1kHz for voice)
- [ ] Bit depth correct (24-bit for source, compressed for final)
- [ ] No audio artifacts (clipping, distortion, noise, clicks, pops)
- [ ] Proper loudness normalization (consistent perceived volume)
- [ ] Channels correct (mono for positional, stereo for UI/music)

**Historical Accuracy**
- [ ] Sound matches historical recordings (when available)
- [ ] Appropriate to time period (technology limitations)
- [ ] Communication protocols historically accurate
- [ ] National accents authentic (native speakers or quality VO)
- [ ] Historical consultant sign-off obtained

**Audio Design Quality**
- [ ] Fits audio design language (consistent with other sounds)
- [ ] Clarity and impact appropriate to sound type
- [ ] Variation sufficient (multiple variants to prevent fatigue)
- [ ] Mixing and balance correct (proper levels relative to other sounds)
- [ ] Effects processing appropriate (reverb, EQ, compression)

**Performance**
- [ ] CPU usage acceptable (audio stays under 10% CPU)
- [ ] Memory usage within budget (platform-specific limits)
- [ ] Streaming works correctly (no loading stutters)
- [ ] LOD system functioning (audio simplifies at distance)
- [ ] No audio dropouts during high load (300+ players)
- [ ] Works correctly on all target platforms (PC, console, mobile)

**In-Game Testing**
- [ ] 3D positional audio works correctly (directional, distance attenuation)
- [ ] Audio synchronizes with visuals (gunfire matches muzzle flash)
- [ ] Ducking and mixing works correctly (important sounds prioritized)
- [ ] Music transitions smoothly between states
- [ ] Voice communications clear and intelligible
- [ ] Accessibility features working (subtitles, visual cues)

### 5.3 Integration Testing

**Cross-Department Testing**
- Art + Audio: Visual effects paired correctly with audio effects
- Art + Engineering: Assets load and display correctly in Unity
- Audio + Engineering: Audio events trigger correctly from scripts
- Design + Art + Audio: Gameplay feel appropriate (feedback, clarity, impact)

**Multiplayer Testing**
- Network synchronization: Visual/audio states sync correctly across clients
- Performance under load: 300+ player testing (FPS, audio quality)
- Bandwidth usage: Asset streaming and updates optimized
- Latency compensation: Visual/audio interpolation smooth despite lag

**Platform Testing**
- PC: Test on minimum, recommended, and enthusiast hardware
- Console: Test on target consoles (PlayStation, Xbox)
- Mobile: Test on mobile devices (if applicable)
- VR: Test VR compatibility (if VR support planned)

---

## 6. Outsourcing and External Production

### 6.1 Outsourcing Strategy

**When to Outsource**
- Large volume of similar assets needed (all ships for a nation)
- Specialized skills required (3D modeling, voice acting, orchestral recording)
- Tight deadlines requiring additional workforce
- Cost-effective compared to hiring full-time staff

**What to Outsource**
- **High Volume Assets**: Ship sprites for multiple classes, weapon sound effects
- **Specialized Assets**: Orchestral music recording, professional voice acting
- **Technical Assets**: 3D models for conversion to sprites, animation work
- **Localization**: Translation, cultural consultation, accent coaching

**What to Keep In-House**
- **Creative Direction**: Art direction, audio design, style consistency
- **Quality Control**: All QA and approval processes
- **Integration**: Unity implementation, scripting, technical integration
- **Core Assets**: Iconic ships, hero assets, unique gameplay elements

### 6.2 Outsourcing Workflow

**Phase 1: Specification and Documentation**
- Create detailed asset specification document
- Include reference materials, style guides, technical requirements
- Provide examples of approved assets (quality benchmark)
- Define deliverables, milestones, and timeline
- Establish communication protocols and feedback loops

**Phase 2: Vendor Selection**
- Research potential vendors (portfolio review, references)
- Request quotes and timelines from multiple vendors
- Evaluate quality, cost, communication, and reliability
- Contract negotiation (deliverables, payment terms, IP ownership)
- NDA and contract signing

**Phase 3: Production**
- Kick-off meeting (introduce project, answer questions, clarify expectations)
- Regular progress reviews (weekly or bi-weekly check-ins)
- Feedback and iteration (provide clear, actionable feedback)
- Milestone reviews (approve milestones before proceeding)
- Maintain open communication (respond quickly to vendor questions)

**Phase 4: Delivery and Integration**
- Receive final assets from vendor
- Run through internal QA checklist (same standards as in-house)
- Provide final feedback and request revisions if needed
- Final approval and payment upon acceptance
- Integrate assets into project (Unity implementation)
- Credit vendor in game credits

### 6.3 Outsourcing Quality Control

**Clear Quality Standards**
- Provide detailed style guides and technical specifications
- Share examples of approved assets (quality benchmark)
- Define acceptance criteria upfront (no surprises)
- Regular reviews prevent major revisions at the end

**Feedback Best Practices**
- Provide specific, actionable feedback (not vague "make it better")
- Use visual annotations (mark up screenshots, draw on images)
- Prioritize feedback (critical issues vs nice-to-haves)
- Be respectful and professional (maintain good relationship)

**Revision Budget**
- Contract includes X rounds of revisions (typically 2-3)
- Additional revisions cost extra (incentive to provide clear feedback early)
- Major scope changes may require contract renegotiation

---

## 7. Asset Optimization and Performance

### 7.1 Visual Asset Optimization

**Texture Compression**
- Unity automatically applies texture compression on import
- PC: DXT5 for RGBA textures (4:1 compression)
- Mobile: ASTC or ETC2 for cross-platform compatibility
- Balance quality and file size (test compressed quality)

**Texture Atlasing**
- Combine multiple small textures into single large atlas
- Reduces draw calls (entire atlas loaded once)
- Unity Sprite Atlas for UI and effects
- Manual atlasing for ship component libraries

**Sprite Batching**
- Unity automatically batches sprites using same texture
- Ensure ships use consistent shaders (enable batching)
- Profile draw calls and optimize batching efficiency
- Reduce state changes (material swaps) for better performance

**LOD System**
- Generate simplified sprites for distant viewing
- Automatic LOD switching based on camera distance
- LOD0: Full detail (0-500m), LOD1: Reduced (500-2000m), LOD2: Simplified (2000m+)
- Test visual quality at LOD switching distances

**Culling Optimization**
- Frustum culling: Don't render objects outside camera view
- Occlusion culling: Don't render objects behind islands/obstacles
- Distance culling: Hide or simplify very distant objects
- Dynamic adjustment based on current FPS

### 7.2 Audio Asset Optimization

**Audio Compression**
- Short SFX: Uncompressed WAV for minimal latency
- Long SFX/Ambient: Vorbis OGG compression (~192 kbps)
- Music: Vorbis OGG compression (~224-256 kbps)
- Voice: Vorbis OGG compression (~160 kbps, speech-optimized)

**Audio Streaming**
- Stream long audio files (music, ambient loops) from disk
- Preload short audio files (gunshots, impacts) into memory
- Asynchronous loading prevents frame drops
- Memory budget management (stay within platform limits)

**Audio LOD**
- Reduce audio quality at distance (lower sample rate, simpler processing)
- Distant sounds simplified (fewer layers, less processing)
- Voice limiting: Maximum simultaneous sounds (prioritize important sounds)
- Dynamic quality adjustment during high CPU load

**Audio Pooling**
- Reuse audio sources instead of creating/destroying
- Audio source pool (pre-allocated, recycled)
- Efficient for frequently played sounds (gunfire, explosions)
- Reduces garbage collection overhead

### 7.3 Performance Budgets

**Visual Asset Budgets (Per Ship)**
- **Tier 1-3**: Max 1MB texture memory, 1 draw call
- **Tier 4-6**: Max 4MB texture memory, 1-2 draw calls
- **Tier 7-9**: Max 8MB texture memory, 1-2 draw calls
- **Tier 10**: Max 16MB texture memory, 1-3 draw calls

**Audio Asset Budgets (Total)**
- **PC**: 1GB audio memory, 128 simultaneous audio sources
- **Console**: 512MB audio memory, 64 simultaneous audio sources
- **Mobile**: 256MB audio memory, 32 simultaneous audio sources
- **Audio CPU**: Maximum 10% CPU usage for audio processing

**Performance Targets**
- **Frame Rate**: 60 FPS minimum on recommended hardware
- **Frame Time**: 16.67ms per frame (60 FPS), 1% lows above 30 FPS
- **Memory**: Stay within platform memory limits (PC: 8GB, Console: varies)
- **Load Times**: Asset loading < 5 seconds per scene transition

---

## 8. Documentation and Knowledge Sharing

### 8.1 Asset Documentation

**Style Guides**
- Visual style guide: Art direction, color palettes, lighting standards
- Audio style guide: Sound design language, mixing standards
- Technical specifications: File formats, naming conventions, performance budgets
- Historical guidelines: Accuracy standards, acceptable deviations

**Production Templates**
- Asset creation checklists (ensure nothing is missed)
- Metadata templates (consistent asset information)
- QA testing templates (standardized testing procedures)
- Outsourcing specification templates (clear vendor communication)

**Asset Library Documentation**
- Searchable asset database with previews and metadata
- Usage examples (how to use assets in Unity)
- Integration tutorials (step-by-step implementation guides)
- Best practices and optimization tips

### 8.2 Training and Onboarding

**New Artist Onboarding**
- Style guide review and discussion
- Review approved assets (quality benchmark)
- Practice asset creation (junior artist creates test asset)
- Feedback and mentoring (senior artist reviews, provides guidance)
- First production asset under supervision

**New Audio Designer Onboarding**
- Audio design language review
- FMOD/Wwise training (middleware proficiency)
- Practice sound creation (test sounds reviewed)
- Feedback and mentoring (audio director reviews)
- First production sound under supervision

**Cross-Training**
- Artists learn basic audio principles (audiovisual integration)
- Audio designers learn visual production (understand artist workflow)
- Engineers learn asset pipeline (understand production constraints)
- Designers learn technical limitations (design within feasibility)

### 8.3 Knowledge Base

**Internal Wiki**
- Production workflows documented step-by-step
- Tool tutorials (Photoshop, Unity, FMOD/Wwise)
- Troubleshooting guides (common issues and solutions)
- Historical research resources (links to references)

**Lessons Learned**
- Post-mortem after major asset production pushes
- Document what went well, what could improve
- Share knowledge across team (avoid repeating mistakes)
- Update workflows based on lessons learned

**Asset Creation Tips and Tricks**
- Efficient techniques discovered by team members
- Optimization strategies that work well
- Creative solutions to production challenges
- Tool scripts and automation (share helpful tools)

---

## 9. Tools and Software

### 9.1 Visual Production Tools

**Primary Art Tools**
- **Photoshop**: Industry-standard for 2D sprite creation
- **Clip Studio Paint**: Alternative 2D art tool (popular with artists)
- **GIMP**: Free alternative for budget-conscious production
- **Aseprite**: Pixel art and sprite animation tool

**Supporting Art Tools**
- **Blender**: 3D modeling for reference or pre-visualization
- **Substance Painter**: PBR texture creation if needed
- **Inkscape**: Vector graphics for UI elements
- **Krita**: Free digital painting tool

**Unity Tools**
- **Sprite Editor**: Built-in Unity sprite slicing and editing
- **Sprite Atlas**: Automatic texture atlasing
- **Particle System**: Built-in particle effects creation
- **Shader Graph**: Visual shader creation (URP)

### 9.2 Audio Production Tools

**Primary Audio Tools**
- **Reaper**: Affordable DAW for audio editing and production
- **Audacity**: Free audio editor for basic tasks
- **Adobe Audition**: Professional audio editor (if budget allows)
- **Logic Pro / Pro Tools**: Professional DAW (Mac / Industry standard)

**Audio Middleware**
- **FMOD Studio**: Recommended audio middleware (free for indie)
- **Wwise**: Alternative audio middleware (free for indie)
- **Unity Audio Mixer**: Built-in Unity audio system (basic needs)

**Sound Design Tools**
- **Serum / Vital**: Synthesizer for sound generation
- **Kontakt**: Sample library player for orchestral sounds
- **FabFilter**: Professional audio processing plugins
- **iZotope RX**: Audio repair and restoration

**Recording Equipment**
- **Microphones**: Condenser mic for foley, dynamic mic for voice
- **Audio Interface**: Quality preamps for recording
- **Portable Recorder**: Field recording for environmental sounds
- **Acoustic Treatment**: Studio foam or blankets for clean recording

### 9.3 Version Control and Collaboration

**Version Control**
- **Git**: Version control system
- **Git LFS**: Large file storage extension for binary assets
- **GitHub / GitLab / Bitbucket**: Remote repository hosting

**Collaboration Tools**
- **Slack / Discord**: Team communication
- **Trello / Jira**: Project management and task tracking
- **Google Drive / Dropbox**: Cloud storage for large files
- **Figma / Miro**: Collaborative design and brainstorming

**Documentation Tools**
- **Notion / Confluence**: Internal wiki and documentation
- **Markdown**: Documentation format (human-readable)
- **Obsidian**: Knowledge base with linking (used for research notes)

---

## 10. Future Pipeline Improvements

### 10.1 Automation and Tooling

**Automated Asset Processing**
- Batch processing scripts (convert, resize, optimize multiple assets)
- Automated LOD generation (AI-based downscaling)
- Automatic texture atlas generation (optimize sprite batching)
- Automated asset validation (check for issues before submission)

**AI-Assisted Production**
- AI texture upscaling (enhance low-resolution references)
- AI-based colorization (colorize historical black-and-white photos)
- Procedural asset generation (generate variations automatically)
- Machine learning QA (detect visual artifacts automatically)

**Pipeline Dashboard**
- Real-time asset status tracking (see production progress)
- Performance metrics visualization (texture memory, draw calls)
- Asset library browser with search and filtering
- Integration with project management (Trello/Jira)

### 10.2 Advanced Production Techniques

**Procedural Generation**
- Procedural camouflage pattern generation (infinite variations)
- Procedural damage state generation (physics-based deformation)
- Procedural weathering (age ships dynamically)
- Reduces manual asset creation workload

**Real-Time Asset Updates**
- Hot-reload system (update assets without restarting game)
- Live preview in Unity (see changes immediately)
- Faster iteration (reduced testing time)
- Improved artist/designer workflow

**Photogrammetry**
- 3D scanning of museum ships (ultra-accurate reference models)
- Convert 3D scans to 2D sprites (authentic top-down views)
- Texture capture for realistic materials
- High upfront cost, exceptional accuracy

---

## Related Documents

- **[Visual-Design.md](./Visual-Design.md)**: Visual asset specifications and style guide
- **[Audio-Design.md](./Audio-Design.md)**: Audio asset specifications and sound design
- **[Historical-Research.md](./Historical-Research.md)**: Historical references for authentic assets
- **[Project-Setup.md](../00-Project-Setup/)**: Unity project configuration and settings
- **[Technical-Architecture.md](../11-Technical/)**: Technical requirements for asset integration

---

**Document Version**: 1.0
**Last Updated**: 2025-11-17
**Next Review**: Phase 3 Planning (TBD)
