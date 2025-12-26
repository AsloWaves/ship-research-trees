---
tags: [script, networking, inventory, data, implemented]
script-type: Data Class
namespace: WOS.Networking.Data
file-path: Assets/Scripts/Networking/Data/ItemData.cs
status: IMPLEMENTED
size: ~8 KB (288 lines)
feature-group: inventory
---

# ItemData.cs

## Quick Reference
**Type**: Serializable Data Class
**Namespace**: WOS.Networking.Data
**File**: `Assets/Scripts/Networking/Data/ItemData.cs`
**Size**: ~8 KB (288 lines)
**Dependencies**: CargoGrid, GridSize, Position

---

## Purpose
Represents a single item instance in the inventory system. Supports multiple item types including cargo, equipment (turrets, engines, modules), containers (wallets), and crew cards. Includes Tetris-style grid placement data (position, rotation, size).

---

## Item Types

| Type | Description | Stacks | Size | Notes |
|------|-------------|--------|------|-------|
| `Cargo` | Basic trade goods | Yes | Variable | Standard inventory items |
| `Turret` | Weapon equipment | No | Variable | EquipmentWeight, Tier |
| `Engine` | Propulsion equipment | No | Variable | EquipmentWeight, Tier |
| `Module` | Ship modules | No | Variable | QualityPercent support |
| `Wallet` | Container item | No | 1x1 | Has ContainerGrid |
| `Container` | Generic container | No | Variable | Has ContainerGrid |
| `CrewCard` | Crew member | No | 1x1 | Non-stackable |

---

## Core Properties

### Basic Properties
```csharp
public string ItemId;                    // Unique instance ID
public string ItemType;                  // Type category
public int Quantity;                     // Stack quantity
public Position Position;                // Grid placement X,Y
public int Rotation;                     // 0, 90, 180, 270 degrees
public GridSize Size;                    // Width × Height cells
public string ItemDefinitionId;          // Reference to definition SO
```

### Equipment Properties
```csharp
public string EquipmentDefinitionId;     // References EquipmentDefinitionSO
public int EquipmentTier;                // Tier 1-7, 0 if not equipment
public float EquipmentWeight;            // Weight in tons
public string EquipmentSubType;          // "Main", "Secondary", "AA", etc.
```

### Quality Properties
```csharp
public float QualityPercent;             // 0.7-1.3 multiplier (1.0 = standard)
public string QualityTierName;           // "Poor" to "Exceptional"
```

Quality tiers:
- Poor (0.7-0.8)
- BelowAverage (0.8-0.9)
- Average (0.9-1.1)
- AboveAverage (1.1-1.2)
- Excellent (1.2-1.3)
- Exceptional (1.3+)

### Extended Data
```csharp
[TextArea(1, 5)]
public string ExtendedDataJson;          // JSON for complex instance data
```

### Container Properties
```csharp
[NonSerialized]
public CargoGrid ContainerGrid;          // Nested grid (not serialized)
public int ContainerWidth;               // Internal grid width
public int ContainerHeight;              // Internal grid height
```

---

## Constructors

```csharp
public ItemData()
public ItemData(string itemId, string itemType, int quantity = 1)
```

---

## Type Checking Methods

```csharp
public bool IsEquipment()    // Turret, Engine, or Module
public bool IsContainer()    // Wallet, Container, or has ContainerGrid
public bool IsCrewCard()     // CrewCard type
public bool IsCargo()        // Not equipment, container, or crew
public bool HasQualityVariance()  // QualityPercent != 1.0
public bool HasExtendedData()     // ExtendedDataJson not empty
```

---

## Stacking

### CanStackWith
Checks if two items can stack.
```csharp
public bool CanStackWith(ItemData other, int maxStack)
```

**Rules**:
- Same ItemId and ItemType
- Current quantity < maxStack
- Neither item is equipment (equipment never stacks)

---

## Weight Calculation

```csharp
public float GetTotalWeight(Func<string, float> getItemWeight = null)
```

**Weight Logic**:
- **Equipment**: Returns EquipmentWeight (quantity always 1)
- **Container**: Own weight + contents weight (recursive)
- **Cargo**: Unit weight × Quantity

---

## Extended Data API

Generic JSON storage for complex instance data:

```csharp
public T GetExtendedData<T>() where T : class
public void SetExtendedData<T>(T data)
```

**Use Cases**:
- Crew stats and abilities
- Module instance variations
- Custom item properties

---

## Container Support

### InitializeAsContainer
Initializes item as a container.
```csharp
public void InitializeAsContainer(int internalWidth, int internalHeight)
```

**Example**: Wallet with 10×25 internal grid
```csharp
walletItem.InitializeAsContainer(10, 25);
```

**Note**: ContainerGrid is `[NonSerialized]` to prevent circular reference issues. Container dimensions are stored in ContainerWidth/Height for reconstruction.

---

## Serialization

```csharp
public string ToJson()
public static ItemData FromJson(string json)
public ItemData Clone()  // Deep copy including nested ContainerGrid
```

---

## Position Class

```csharp
[Serializable]
public class Position
{
    public int X;
    public int Y;

    public Position()
    public Position(int x, int y)
    public override bool Equals(object obj)
    public override int GetHashCode()
    public override string ToString()  // "(X, Y)"
}
```

---

## Clone Method

Creates deep copy including:
- All basic properties
- Equipment properties
- Quality properties
- Extended data JSON
- Container dimensions
- Nested ContainerGrid (via ContainerGrid.Clone())

---

## Integration Points

### Used By
- [[CargoGrid]] - Contains ItemData instances
- [[PlayFabInventoryService]] - Serialization
- [[InventoryPanel]] - UI display
- [[EquipmentPanel]] - Equipment display

### References
- [[ItemDefinitionSO]] - Item type definitions
- [[EquipmentDefinitionSO]] - Equipment stats
- [[TurretDefinitionSO]] - Turret specifics

---

## Network Considerations

- Uses Unity's JsonUtility for serialization
- Mirror-compatible (List-based, not Dictionary)
- ContainerGrid marked NonSerialized to prevent depth issues
- Position uses value-based equality for comparison

---

## Related Files
- [[CargoGrid]] - Grid container for items
- [[GridSize]] - Width/Height data structure
- [[ItemDefinitionSO]] - Item type definitions
- [[EquipmentDefinitionSO]] - Equipment definitions

---

## Testing Notes
- Equipment quantity always 1
- QualityPercent default 0 (not 1.0)
- ContainerGrid reconstructed from Width/Height
- Extended data stored as raw JSON string
- Position equality is value-based

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added equipment properties
- **2025-01**: Added quality variance support
- **2025-01**: Added container support
- **2025-01**: Added extended data JSON storage
- **2025-01**: Added Clone() method

