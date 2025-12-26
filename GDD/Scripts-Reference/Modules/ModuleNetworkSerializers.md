---
tags: [script, modules, networking, serialization, implemented]
script-type: Static Class
namespace: WOS.Modules.Data
file-path: Assets/Scripts/Modules/Data/ModuleNetworkSerializers.cs
status: IMPLEMENTED
size: ~261 lines
feature-group: modules
---

# ModuleNetworkSerializers.cs

## Quick Reference
**Type**: Static Extension Methods
**Namespace**: WOS.Modules.Data
**File**: `Assets/Scripts/Modules/Data/ModuleNetworkSerializers.cs`
**Size**: ~261 lines
**Dependencies**: Mirror, ModuleData

---

## Purpose
Custom Mirror serializers for module data types. Mirror cannot auto-generate serializers for complex types with Dictionaries or nested Lists. These extension methods provide explicit read/write implementations for network synchronization.

---

## Why Custom Serializers?

Mirror's weaver cannot automatically serialize:
- Classes with `Dictionary<K,V>` fields
- Classes with deeply nested Lists
- Complex object graphs with null references
- Enum fields in nested structures

This file provides manual serialization for all module data types.

---

## Serialized Types

### ModuleSlot

```csharp
public static void WriteModuleSlot(this NetworkWriter writer, ModuleSlot slot)
{
    if (slot == null)
    {
        writer.WriteBool(false);
        return;
    }

    writer.WriteBool(true);
    writer.WriteString(slot.slotId ?? string.Empty);
    writer.WriteString(slot.slotName ?? string.Empty);
    writer.WriteInt((int)slot.slotType);
    writer.WriteInt(slot.minTier);
    writer.WriteBool(slot.isUnlocked);
    writer.WriteString(slot.equippedModuleInstanceId ?? string.Empty);

    // Write allowed categories
    int categoryCount = slot.allowedCategories?.Count ?? 0;
    writer.WriteInt(categoryCount);
    foreach (var category in slot.allowedCategories)
    {
        writer.WriteInt((int)category);
    }
}

public static ModuleSlot ReadModuleSlot(this NetworkReader reader)
{
    bool hasValue = reader.ReadBool();
    if (!hasValue) return null;

    var slot = new ModuleSlot
    {
        slotId = reader.ReadString(),
        slotName = reader.ReadString(),
        slotType = (ModuleSlotType)reader.ReadInt(),
        minTier = reader.ReadInt(),
        isUnlocked = reader.ReadBool(),
        equippedModuleInstanceId = reader.ReadString()
    };

    // Handle empty string as null
    if (string.IsNullOrEmpty(slot.equippedModuleInstanceId))
    {
        slot.equippedModuleInstanceId = null;
    }

    // Read allowed categories
    int categoryCount = reader.ReadInt();
    slot.allowedCategories = new List<ModuleCategory>(categoryCount);
    for (int i = 0; i < categoryCount; i++)
    {
        slot.allowedCategories.Add((ModuleCategory)reader.ReadInt());
    }

    return slot;
}
```

### ModuleInstance

```csharp
public static void WriteModuleInstance(this NetworkWriter writer, ModuleInstance instance)
{
    if (instance == null)
    {
        writer.WriteBool(false);
        return;
    }

    writer.WriteBool(true);
    writer.WriteString(instance.instanceId ?? string.Empty);
    writer.WriteString(instance.moduleDefinitionId ?? string.Empty);
    writer.WriteInt((int)instance.quality);
    writer.WriteBool(instance.isEquipped);
    writer.WriteString(instance.equippedSlotId ?? string.Empty);
    writer.WriteFloat(instance.condition);
    writer.WriteInt(instance.upgradeLevel);

    // Write applied enhancements
    int enhancementCount = instance.appliedEnhancements?.Count ?? 0;
    writer.WriteInt(enhancementCount);
    foreach (var enhancement in instance.appliedEnhancements)
    {
        writer.WriteString(enhancement ?? string.Empty);
    }
}

public static ModuleInstance ReadModuleInstance(this NetworkReader reader)
{
    bool hasValue = reader.ReadBool();
    if (!hasValue) return null;

    var instance = new ModuleInstance
    {
        instanceId = reader.ReadString(),
        moduleDefinitionId = reader.ReadString(),
        quality = (ModuleQuality)reader.ReadInt(),
        isEquipped = reader.ReadBool(),
        equippedSlotId = reader.ReadString(),
        condition = reader.ReadFloat(),
        upgradeLevel = reader.ReadInt()
    };

    // Handle empty string as null
    if (string.IsNullOrEmpty(instance.equippedSlotId))
    {
        instance.equippedSlotId = null;
    }

    // Read applied enhancements
    int enhancementCount = reader.ReadInt();
    instance.appliedEnhancements = new List<string>(enhancementCount);
    for (int i = 0; i < enhancementCount; i++)
    {
        string enhancement = reader.ReadString();
        if (!string.IsNullOrEmpty(enhancement))
        {
            instance.appliedEnhancements.Add(enhancement);
        }
    }

    return instance;
}
```

### ShipModuleLoadout

```csharp
public static void WriteShipModuleLoadout(this NetworkWriter writer, ShipModuleLoadout loadout)
{
    if (loadout == null)
    {
        writer.WriteBool(false);
        return;
    }

    writer.WriteBool(true);

    // Write slots
    int slotCount = loadout.slots?.Count ?? 0;
    writer.WriteInt(slotCount);
    foreach (var slot in loadout.slots)
    {
        writer.WriteModuleSlot(slot);
    }

    // Write equipped modules
    int moduleCount = loadout.equippedModules?.Count ?? 0;
    writer.WriteInt(moduleCount);
    foreach (var module in loadout.equippedModules)
    {
        writer.WriteModuleInstance(module);
    }

    // Write cached bonuses list
    int bonusCount = loadout.cachedBonusList?.Count ?? 0;
    writer.WriteInt(bonusCount);
    foreach (var bonus in loadout.cachedBonusList)
    {
        writer.WriteInt((int)bonus.statType);
        writer.WriteFloat(bonus.value);
    }
}

public static ShipModuleLoadout ReadShipModuleLoadout(this NetworkReader reader)
{
    bool hasValue = reader.ReadBool();
    if (!hasValue) return null;

    var loadout = new ShipModuleLoadout();

    // Read slots
    int slotCount = reader.ReadInt();
    loadout.slots = new List<ModuleSlot>(slotCount);
    for (int i = 0; i < slotCount; i++)
    {
        var slot = reader.ReadModuleSlot();
        if (slot != null) loadout.slots.Add(slot);
    }

    // Read equipped modules
    int moduleCount = reader.ReadInt();
    loadout.equippedModules = new List<ModuleInstance>(moduleCount);
    for (int i = 0; i < moduleCount; i++)
    {
        var module = reader.ReadModuleInstance();
        if (module != null) loadout.equippedModules.Add(module);
    }

    // Read cached bonuses list
    int bonusCount = reader.ReadInt();
    loadout.cachedBonusList = new List<ModuleStatBonus>(bonusCount);
    for (int i = 0; i < bonusCount; i++)
    {
        var statType = (ModuleStatType)reader.ReadInt();
        var value = reader.ReadFloat();
        loadout.cachedBonusList.Add(new ModuleStatBonus(statType, value));
    }

    // Rebuild the local cache after network sync
    loadout.RebuildBonusCache();

    return loadout;
}
```

### ModuleStatBonus

```csharp
public static void WriteModuleStatBonus(this NetworkWriter writer, ModuleStatBonus bonus)
{
    writer.WriteInt((int)bonus.statType);
    writer.WriteFloat(bonus.value);
}

public static ModuleStatBonus ReadModuleStatBonus(this NetworkReader reader)
{
    var statType = (ModuleStatType)reader.ReadInt();
    var value = reader.ReadFloat();
    return new ModuleStatBonus(statType, value);
}
```

---

## Serialization Patterns

### Null Handling
- Write boolean flag first to indicate null/non-null
- Reader checks flag before deserializing
- Prevents null reference exceptions during sync

### Empty String Handling
- Null strings written as `string.Empty`
- On read, empty strings converted back to null
- Maintains semantic meaning across network

### List Serialization
- Write count first, then iterate items
- Reader pre-allocates with capacity
- Handles empty and null lists

### Enum Serialization
- Cast to int for writing
- Cast back to enum on read
- Works with all enum sizes

---

## Integration Points

### Dependencies
- Mirror (NetworkReader, NetworkWriter)
- [[ModuleData]] - Data types being serialized

### Used By
- Mirror SyncVar system
- [[ModuleController]] - Module loadout synchronization

---

## Related Files
- [[ModuleData]] - Data structures
- [[ModuleController]] - Module management

---

## Design Notes
- Extension methods on NetworkReader/NetworkWriter
- All types serializable with null safety
- Enum values cast to int for portability
- Lists pre-allocated with known capacity
- Cache rebuilt after deserialization
- Empty strings converted to null for consistency
- Hierarchical serialization (Loadout → Slots → Modules)

