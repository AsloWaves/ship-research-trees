# SOGeneratorWindow.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Editor/SOGeneratorWindow.cs` |
| **Namespace** | `WOS.Editor` |
| **Inheritance** | `EditorWindow` |
| **Lines** | 1928 |
| **Architecture** | Editor tool, bulk asset generator |

---

## Purpose

Bulk ScriptableObject generator for creating game content assets. Provides tabbed interface for generating modules, turrets, crew templates, cargo items, ships, and batch imports from CSV/JSON.

**Key Features**:
- Multi-tab generation workflow (Modules, Turrets, Crew, Cargo, Ships, Batch Import)
- Tier-based generation with quality variance (70-130% per GDD)
- CSV/JSON import/export capabilities
- Auto-generation of complete equipment sets
- Folder organization and asset management

---

## Generation Capabilities

### Module Generation

**Quality Variance System**: All modules support 70-130% quality variance per GDD specifications.

| Module Type | Base Effect (T1) | Effect/Tier | Base Price | Weight (T1) |
|-------------|------------------|-------------|------------|-------------|
| FireControl | 5.0 | +4.0/tier | 1000 * tier² | 5 + tier*2 |
| DamageControl | 10.0 | +8.0/tier | 800 * tier² | 5 + tier*2 |
| Radar | 8.0 | +6.4/tier | 1500 * tier² | 5 + tier*2 |
| Sonar | 6.0 | +4.8/tier | 1200 * tier² | 5 + tier*2 |
| Communications | 4.0 | +3.2/tier | 600 * tier² | 5 + tier*2 |

**Generation Options**:
- Individual type generation (T1-T7 range selection)
- Bulk "Generate ALL Module Types" button (creates 5 types × 7 tiers = 35 modules)
- Quality variance: 0.7-1.3x multiplier on base stats

### Turret Generation

| Turret Type | Base Caliber | Caliber/Tier | Barrel Count | Rate of Fire |
|-------------|--------------|--------------|--------------|--------------|
| Main | 5.0" | +2.0"/tier | 1 + tier/3 (max 4) | 15 - tier*2 rpm |
| Secondary | 3.0" | +1.0"/tier | 2 (max) | 20 - tier rpm |
| AA | 0.5" | +0.5"/tier | 1 + tier/2 (max 4) | 60 - tier*5 rpm |

**Damage Calculation**: `20 + tier * 40` kJ per shell
**Accuracy**: `60 + tier * 5` base accuracy
**Weight**: `10 + tier * 8` tons
**Price**: `2000 * tier²` credits

**Generation Options**:
- Single type, tier range selection
- "Generate ALL Turret Types (T1-T7)" creates 3 types × 7 tiers = 21 turrets

### Crew Template Generation

**GDD Stat System**:
- **Base Stats**: Random 7-15 at recruitment
- **Primary Growth**: +0.19/level
- **Secondary Growth**: +0.10/level
- **Classification Bonus**: +5 at Level 25
- **Max Stat Cap**: 50

| Rarity | Starting Level | Recruitment Cost | Special Ability | Requires Unlock |
|--------|----------------|------------------|-----------------|-----------------|
| Common | 1 | 500 | No | No |
| Uncommon | 15 | 2,500 | No | No |
| Rare | 40 | 10,000 | No | No |
| Epic | 70 | 30,000 | Yes | No |
| Legendary | 120 | 100,000 | Yes | Yes |

**18 Classifications**: Gunner, TorpedoSpecialist, AASpecialist, DamageControl, Engineer, Navigator, RadarOperator, SonarOperator, RadioOperator, Spotter, LoadingSpecialist, DeckOfficer, FireControl, Command, SubmarineCommander, CarrierCommander, Intelligence, Electronics

**Bulk Generation**:
- "Generate ALL 18 Classifications (Common)": Creates 18 crew templates
- "Generate ALL Classifications × ALL Rarities": Creates 18 × 5 = 90 crew templates

### Cargo Item Generation

| Category | Grid Size | Max Stack | Weight/Unit | Base Price |
|----------|-----------|-----------|-------------|------------|
| RawMaterial | 2×2 | 100 | 2.0 tons | 10 * (index+1) |
| RefinedMaterial | 2×3 | 50 | 1.5 tons | 50 * (index+1) |
| Food | 1×2 | 200 | 0.5 tons | 15 * (index+1) |
| Luxury | 1×1 | 20 | 0.2 tons | 200 * (index+1) |
| Equipment | 2×2 | 10 | 3.0 tons | 100 * (index+1) |
| Military | 1×3 | 50 | 4.0 tons | 300 * (index+1) |
| Medical | 1×1 | 100 | 0.3 tons | 80 * (index+1) |
| Container | 4×2 | 1 | 5.0 tons | 500 * (index+1) |

**8 Predefined Items Per Category** (examples: Iron Ore, Steel Plates, Grain, Wine, etc.)

### Ship Generation

**Comprehensive Ship Creation** with:
- Equipment slots (turrets, engines, modules)
- Cargo grid dimensions and weight capacity
- Crew positions and officer slots
- Tier-based stats and economics

**Ship Stats by Class**:

| Ship Class | Base HP (T1) | Max Speed (T1) | Turn Rate | Cargo Grid (T1) |
|------------|--------------|----------------|-----------|-----------------|
| Destroyer | 500 | 35 kts | 15°/s | 3×3 |
| Light Cruiser | 800 | 32 kts | 12°/s | 4×4 |
| Heavy Cruiser | 1200 | 28 kts | 8°/s | 5×4 |
| Battleship | 2500 | 22 kts | 4°/s | 6×5 |
| Dreadnought | 3500 | 18 kts | 3°/s | 6×5 |
| Fleet Carrier | 1500 | 28 kts | 6°/s | 6×5 |
| Coastal Submarine | 300 | 12 kts | 8°/s | 3×3 |
| Transport | 400 | 15 kts | 8°/s | 8×6 |

**Armor System**: Automatically applies appropriate armor scheme (Unarmored, Lightweight, Balanced, HeavyProtection, AllOrNothing) based on ship class with nation-specific armor types (KruppCemented, TerniSteel, DucolSteel, STS, RHA).

**Turret Slot Generation** (consolidated weapon system):
- Main Battery (forward/aft positions)
- Secondary Batteries (port/starboard broadside)
- Anti-Aircraft Mounts (360° rotation, multiple positions)
- Torpedo Tubes (fixed/limited rotation)
- Depth Charges (destroyers/ASW vessels)

**Module Slot Generation** (Bridge/Engine/Support):
- Bridge (Command): Required, 1 per ship
- Engine: Required, 1-2 depending on size
- Fire Control: Combat ships only
- Radar: Large ships, T5+
- Sonar: Submarines, destroyers
- Damage Control: All ships
- Medical: Large ships, T4+
- Concealment: Destroyers, submarines

**Quick Generation Buttons**:
- "Generate Starter Fleet": Creates Destroyer/LightCruiser/Transport (T1-T3)
- "Generate ALL Ship Classes (T1-T5)": Creates 11 common classes × 5 tiers

---

## Batch Import/Export

### CSV Import

**Format** (14 columns minimum):
```csv
Name,Type,Tier,BaseEffect
Module_FireControl_T1,FireControl,1,5.0
```

**Supported Import Types**:
- Modules: Name, Type, Tier, BaseEffect
- Turrets: Name, Type, Tier, Caliber, Barrels
- Crew: Name, Classification, Rarity
- Cargo: Name, Category, GridW, GridH, Weight, Price
- Ships: Name, Class, Tier, Nation

### CSV Export

**Exports All Existing ScriptableObjects** to structured CSV with separate sections:
- Modules section
- Turrets section
- Crew section
- Ships section

**Auto-categorizes** based on type and includes relevant fields for each category.

---

## Key Code Sections

### Module Generation Logic

```csharp
// Lines 165-193: Single module generation with quality variance
for (int tier = moduleTierStart; tier <= moduleTierEnd; tier++)
{
    var module = CreateInstance<ModuleDefinitionSO>();
    module.equipmentId = $"Module_T{tier}_{selectedModuleType}";
    module.tier = tier;
    module.moduleType = selectedModuleType;
    module.baseEffectValue = moduleBaseEffect + (tier - 1) * moduleEffectPerTier;
    module.enableQualityVariance = true;  // GDD requirement
    module.minQuality = 0.7f;             // 70% minimum
    module.maxQuality = 1.3f;             // 130% maximum
    module.weightTons = 5f + tier * 2f;
    module.purchasePrice = 500 * tier * tier;

    AssetDatabase.CreateAsset(module, path);
}
```

### Turret Stat Calculations

```csharp
// Lines 362-393: Caliber, barrel count, damage, ROF by type
private float GetCaliberForType(TurretType type, int tier)
{
    return type switch
    {
        TurretType.Main => 5f + tier * 2f,      // 5" to 19"
        TurretType.Secondary => 3f + tier * 1f, // 3" to 10"
        TurretType.AA => 0.5f + tier * 0.5f,    // 0.5" to 4"
        _ => 5f + tier * 2f
    };
}

private int GetBarrelCount(TurretType type, int tier)
{
    if (type == TurretType.AA) return Mathf.Min(4, 1 + tier / 2);
    return Mathf.Min(4, 1 + tier / 3);
}

private int GetDamagePerShell(int tier)
{
    return 20 + tier * 40;  // T1: 60, T7: 300
}
```

### Ship Armor Configuration

```csharp
// Lines 966-1031: Armor scheme application with tier scaling
private void ApplyArmorSchemeForClass(ShipDefinitionSO ship, ShipClass shipClass, ShipTier tier)
{
    // Select armor scheme based on class
    ArmorScheme scheme = shipClass switch
    {
        ShipClass.Destroyer => ArmorScheme.Lightweight,
        ShipClass.Battleship => ArmorScheme.HeavyProtection,
        ShipClass.Dreadnought => ArmorScheme.AllOrNothing,
        // ... other classes
    };

    ship.armorConfiguration.ApplyScheme(scheme, shipClass);

    // Select armor type based on nation
    ArmorType armorType = ship.nation switch
    {
        ShipNation.KM => ArmorType.KruppCemented,
        ShipNation.RM => ArmorType.TerniSteel,
        ShipNation.RN => ArmorType.DucolSteel,
        ShipNation.USN => ArmorType.STS,
        _ => ArmorType.RHA
    };
    ship.armorConfiguration.SetUniformArmorType(armorType);

    // Tier scaling: T1 = 0.85x, T7 = 1.15x (clamped to max limits)
    float tierMultiplier = 0.8f + tierValue * 0.05f;
}
```

### Turret Slot Generation (Consolidated Weapons)

```csharp
// Lines 1149-1258: Unified turret slot generation for all weapon types
private List<TurretSlotConfig> GenerateTurretSlots(ShipClass shipClass, ShipTier tier)
{
    var slots = new List<TurretSlotConfig>();

    // Main Battery (centerline mounts)
    int mainBatteryCount = GetMainBatteryCount(shipClass, tierValue);
    for (int i = 0; i < mainBatteryCount; i++)
    {
        slots.Add(new TurretSlotConfig
        {
            slotId = $"main_{i + 1}",
            slotName = GetMainBatteryName(i, mainBatteryCount), // "A Turret", "B Turret", etc.
            position = new Vector3(0, 0, (i - mainBatteryCount / 2f) * 3f),
            mountType = TurretMountType.MainBattery,
            // ... rotation limits, crew requirements
        });
    }

    // Secondary (port/starboard broadside)
    // Torpedoes (fixed/limited rotation)
    // AA (360° rotation)
    // Depth Charges (ASW)
}
```

---

## Public API / Menu Items

### Menu Access

```csharp
[MenuItem("Tools/WOS/SO Generator", priority = 100)]
public static void ShowWindow()
```

**Menu Path**: `Tools > WOS > SO Generator`

### Window Configuration

```csharp
// Lines 74-79: Window setup
var window = GetWindow<SOGeneratorWindow>("SO Generator");
window.minSize = new Vector2(500, 600);
```

**Minimum Size**: 500×600px
**Features**: Scrollable, tabbed interface

---

## Usage Examples

### Generate All Modules (T1-T7)

1. Open: `Tools > WOS > SO Generator`
2. Select "Modules" tab
3. Click "Generate ALL Module Types (T1-T7)"
4. Output: 35 modules (5 types × 7 tiers) in `Assets/ScriptableObjects/Generated/Modules/`

### Create Custom Turret Range

1. Select "Turrets" tab
2. Choose turret type (Main, Secondary, AA)
3. Set tier range (e.g., T3-T5)
4. Adjust base caliber and caliber/tier increment
5. Click "Generate [N] Turret(s)"
6. Output: `Assets/ScriptableObjects/Generated/Turrets/`

### Crew Rarity Set

1. Select "Crew" tab
2. Choose classification (e.g., Gunner)
3. Select rarity (e.g., Epic)
4. Set count (e.g., 5 for variation)
5. Click "Generate [N] Crew Template(s)"
6. Output: `Assets/ScriptableObjects/Generated/Crew/Epic/`

### Import from CSV

1. Select "Batch Import" tab
2. Choose import type (Module, Turret, Crew, Cargo, Ship)
3. Select CSV file
4. Click "Import from CSV"
5. Assets created with auto-naming

### Export Existing Assets

1. Select "Batch Import" tab
2. Click "Export Existing SOs to CSV"
3. Select save location
4. CSV generated with categorized sections

---

## Integration Points

### Asset Creation

**Uses Unity AssetDatabase**:
```csharp
AssetDatabase.CreateAsset(module, path);
AssetDatabase.SaveAssets();
AssetDatabase.Refresh();
```

### Folder Management

**Auto-creates nested folders**:
```csharp
// Lines 1898-1915: Recursive folder creation
private void EnsureOutputFolderExists(string path)
{
    var parts = path.Split('/');
    string current = parts[0];

    for (int i = 1; i < parts.Length; i++)
    {
        string next = $"{current}/{parts[i]}";
        if (!AssetDatabase.IsValidFolder(next))
        {
            AssetDatabase.CreateFolder(current, parts[i]);
        }
        current = next;
    }
}
```

### ScriptableObject Types

**Creates**:
- `ModuleDefinitionSO`
- `TurretDefinitionSO`
- `CrewTemplateSO`
- `CargoItemDefinitionSO`
- `ShipDefinitionSO`

**Imports**:
- `WOS.ScriptableObjects.Items`
- `WOS.ScriptableObjects.Crew`
- `WOS.ScriptableObjects.Core`
- `WOS.Player.Data`
- `WOS.Ships.Data`
- `WOS.Ships.ScriptableObjects`

---

## Design Notes

### Quality Variance System

**Per GDD Requirements**: All modules support 70-130% quality variance on base stats. This creates variety in loot drops and trading economy.

**Implementation**:
- `enableQualityVariance = true` on all generated modules
- `minQuality = 0.7f` (70% of base stats)
- `maxQuality = 1.3f` (130% of base stats)

### Tier Progression Formulas

**Linear Growth**:
- Module effect: `baseValue + (tier - 1) * increment`
- Turret caliber: `baseCaliber + (tier - 1) * caliberPerTier`

**Quadratic Pricing**:
- Modules: `basePrice * tier²`
- Turrets: `2000 * tier²`
- Ships: `baseClassPrice * tier²`

**Why Quadratic**: Prevents tier inflation, maintains tier value at high levels.

### CSV Format Choices

**Double-quote wrapped values**: Handles commas in descriptions
**Semicolon-separated prerequisites**: Allows multiple dependencies
**Comment support**: Lines starting with `#` are ignored
**Header row required**: First row defines column mapping

### Ship Generation Complexity

**Automatic Slot Generation** based on:
- **Ship Class**: Determines base slot counts and types
- **Tier**: Modifies slot counts and stat ranges
- **Nation**: Affects armor types and naming conventions

**Position Calculation**: Slots positioned in 3D space relative to ship center (Vector3: x=port/starboard, y=fore/aft, z=height). Bow is +Y, stern is -Y, port is -X, starboard is +X.

### Armor Thickness Limits

**ShipClassArmorLimits** enforces historical constraints:
- Destroyers: Light armor, minimal protection
- Cruisers: Balanced armor schemes
- Battleships: Heavy belt/deck armor
- Carriers: Light armor, relies on aircraft

**Tier scaling clamped** to prevent unrealistic armor values at high tiers.

### Crew Classification System

**18 Distinct Classifications** mapped to specific equipment:
- **Gunner**: Main/Secondary turrets
- **TorpedoSpecialist**: Torpedo tubes
- **AASpecialist**: AA mounts
- **SonarOperator**: Sonar modules
- **RadarOperator**: Radar modules
- **Engineer**: Engines, DamageControl modules
- **Command**: Bridge modules

**Stat Mapping**: Each classification has primary/secondary stat preferences (defined in `ClassificationStatMapping.GetAllMappings()`).

---

## Performance Considerations

**Batch Creation**: Generates multiple assets in single operation, then saves once:
```csharp
for (int tier = 1; tier <= 7; tier++)
{
    var module = CreateInstance<ModuleDefinitionSO>();
    // ... configure module
    AssetDatabase.CreateAsset(module, path);
}
// Single save/refresh after all created
AssetDatabase.SaveAssets();
AssetDatabase.Refresh();
```

**Folder Validation**: Checks `AssetDatabase.IsValidFolder()` before creation to avoid redundant operations.

**Import Optimization**: Uses `LINQ` for filtering/grouping, but processes sequentially to maintain stable asset references.
