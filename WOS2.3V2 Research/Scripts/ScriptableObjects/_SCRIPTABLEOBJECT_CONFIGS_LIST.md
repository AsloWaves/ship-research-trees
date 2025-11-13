# ScriptableObject Configurations

The ScriptableObjects/Configs folder contains 7 configuration ScriptableObjects for game systems.

## Ocean & Environment Configs

- **OceanBiomeConfigurationSO.cs** (16KB) - Configures ocean depth zones, tile types, biome colors, and procedural depth maps

## Port System Configs

- **PortConfigurationSO.cs** (14KB) - Core port properties (name, location, nation, tier, faction)
- **PortIntegrationConfigurationSO.cs** (23KB) - Port integration with economy, reputation, missions
- **PortServicesConfigurationSO.cs** (19KB) - Port services (repair, refuel, resupply, crew, outfitting)
- **PortUIConfigurationSO.cs** (19KB) - Port UI layout and visual configuration
- **PortVisualConfigurationSO.cs** (20KB) - Port visual effects (buildings, docks, ambient particles)
- **DockingConfigurationSO.cs** (18KB) - Docking mechanics and collision detection

## Key Systems

### Ocean Biome System
OceanBiomeConfigurationSO defines:
- 5 depth zones (Coastal 0-50m, Shallow 50-200m, Medium 200-1000m, Deep 1000-4000m, Abyssal 4000m+)
- Tile types with color gradients for each depth range
- Procedural depth calculation using Perlin noise
- Optional custom depth maps (Texture2D) for specific regions
- Feature spawning (reefs, wrecks, seamounts) based on depth

### Port System
The port configs use a modular architecture:
1. **PortConfigurationSO** - Core identity and location
2. **PortServicesConfigurationSO** - What services are available
3. **PortVisualConfigurationSO** - Visual presentation (buildings, effects)
4. **PortUIConfigurationSO** - UI layout and styling
5. **PortIntegrationConfigurationSO** - Economy/mission/reputation links
6. **DockingConfigurationSO** - Docking zones and mechanics

This separation allows:
- Reusing service configs across multiple ports
- Easy port variants (different visuals, same services)
- Modular testing and debugging
- Designer-friendly editing without code changes
