---
tags: [script, inventory, scriptableobject, item, implemented]
script-type: ScriptableObject
namespace: WOS.Inventory.Items
file-path: Assets/Scripts/Inventory/Items/ItemDefinitionSO.cs
status: IMPLEMENTED
size: ~5 KB (206 lines)
feature-group: inventory
---

# ItemDefinitionSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Inventory.Items
**File**: `Assets/Scripts/Inventory/Items/ItemDefinitionSO.cs`
**Size**: ~5 KB (206 lines)
**Create**: `Create > WOS > Inventory > Item Definition`

---

## Purpose
ScriptableObject defining item properties. Referenced by `ItemData.ItemDefinitionId` for runtime lookup via `ItemDatabase`. Contains visual, economic, and gameplay properties.

---

## Enums

### ItemCategory
```csharp
public enum ItemCategory
{
    Cargo,       // Trade goods, resources
    Equipment,   // Turrets, engines, modules
    Container,   // Wallets, chests
    Ammunition,  // Ship ammunition
    Consumable,  // Single-use items
    CrewCard,    // Crew member cards
    Currency     // Money, tokens
}
```

### ItemRarity
```csharp
public enum ItemRarity
{
    Common,      // White - 60% drop
    Uncommon,    // Green - 25% drop
    Rare,        // Blue - 10% drop
    Epic,        // Purple - 4% drop
    Legendary    // Gold - 1% drop
}
```

### AmmoType
```csharp
public enum AmmoType
{
    None,          // Not ammunition
    Standard,      // Default damage
    ArmorPiercing, // +25% vs armored
    HighExplosive, // +50% splash
    Incendiary     // Fire damage over time
}
```

---

## Configuration

### Identification
```csharp
[Header("Identification")]
public string ItemId;         // Unique ID matching ItemData.ItemDefinitionId
public string DisplayName;    // UI display name
public string Description;    // Tooltip text
```

### Classification
```csharp
[Header("Classification")]
public ItemCategory Category = ItemCategory.Cargo;
public ItemRarity Rarity = ItemRarity.Common;
public AmmoType AmmunitionType = AmmoType.None;
```

### Grid Properties
```csharp
[Header("Grid Properties")]
[Range(1, 10)] public int Width = 1;
[Range(1, 10)] public int Height = 1;
```

### Stacking & Weight
```csharp
[Header("Stacking & Weight")]
[Range(1, 999)] public int MaxStack = 1;
[Min(0f)] public float WeightPerUnit = 0.1f;
```

### Container Properties
```csharp
[Header("Container Properties")]
[Range(1, 25)] public int ContainerInternalWidth = 10;
[Range(1, 50)] public int ContainerInternalHeight = 25;
```

### Economy
```csharp
[Header("Economy")]
[Min(0)] public int BaseBuyPrice = 100;
[Min(0)] public int BaseSellPrice = 50;
```

### Visual
```csharp
[Header("Visual")]
public Sprite Icon;
public Color RarityColor = Color.white;
```

### Restrictions
```csharp
[Header("Restrictions")]
[Range(0, 10)] public int MinShipTier = 0;
public bool IsTradeable = true;
public bool IsDroppable = true;
```

---

## Properties & Methods

```csharp
public GridSize GetGridSize()           // Returns (Width, Height)
public Color GetRarityColor()           // Auto-color by rarity if not set
public bool IsContainer                 // Category == Container
public bool IsStackable                 // MaxStack > 1
public bool IsAmmunition                // AmmunitionType != None
public float GetTotalWeight(int quantity)  // WeightPerUnit * quantity
```

---

## Rarity Colors

| Rarity | Color | RGB |
|--------|-------|-----|
| Common | White | (1, 1, 1) |
| Uncommon | Green | (0.2, 0.8, 0.2) |
| Rare | Blue | (0.2, 0.4, 1) |
| Epic | Purple | (0.6, 0.2, 0.8) |
| Legendary | Gold | (1, 0.8, 0.2) |

---

## Editor Validation (OnValidate)

- Auto-generates ItemId from asset name if empty
- Ensures sell price <= buy price (caps at 70%)
- Containers cannot stack (MaxStack = 1)
- CrewCards always 1x1, non-stackable

---

## Example Assets

| Item | Category | Size | Stack | Weight |
|------|----------|------|-------|--------|
| Iron Ore | Cargo | 2x2 | 100 | 1.0 |
| Gold Bar | Cargo | 1x1 | 50 | 2.5 |
| Basic Wallet | Container | 2x2 | 1 | 0.1 |
| 5" Shell | Ammunition | 2x1 | 999 | 0.05 |
| Health Kit | Consumable | 1x1 | 10 | 0.1 |

---

## Integration Points

### Dependencies
- None (base ScriptableObject)

### Used By
- [[ItemDatabase]] - Runtime lookup
- [[ItemDatabaseSO]] - Asset collection
- [[InventoryPanel]] - UI display
- [[TradingPanel]] - Prices

---

## Related Files
- [[ItemDatabase]] - Runtime accessor
- [[ItemDatabaseSO]] - Database collection
- [[ItemData]] - Instance data

---

## Testing Notes
- ItemId auto-generated from asset name
- RarityColor auto-assigned if left white
- Container items enforce MaxStack = 1
- CrewCard items enforce 1x1 size

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added ammunition types
- **2025-01**: Added container properties
- **2025-01**: Added rarity system

