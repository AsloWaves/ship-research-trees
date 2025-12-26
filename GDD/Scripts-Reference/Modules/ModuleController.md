---
tags: [script, modules, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Modules.Controllers
file-path: Assets/Scripts/Modules/Controllers/ModuleController.cs
status: IMPLEMENTED
size: ~542 lines
feature-group: modules
---

# ModuleController.cs

## Quick Reference
**Type**: NetworkBehaviour (per-ship, Singleton)
**Namespace**: WOS.Modules.Controllers
**File**: `Assets/Scripts/Modules/Controllers/ModuleController.cs`
**Size**: ~542 lines
**Dependencies**: ModuleData, ModuleDefinitionSO, Mirror, WOS.Debugging

---

## Purpose
Server-authoritative module management for ships. Handles module equipping/unequipping, stat calculations, active/conditional effects, and module upgrades. Based on GDD Module-System.md specifications.

---

## Singleton Access

```csharp
private static ModuleController _instance;
public static ModuleController Instance => _instance;
```

---

## Configuration

```csharp
[Header("Configuration")]
[SerializeField] private int maxModuleSlots = 6;
[SerializeField] private int maxUpgradeLevel = 5;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Synced State

```csharp
[SyncVar(hook = nameof(OnLoadoutChanged))]
private ShipModuleLoadout moduleLoadout;
```

---

## Events

```csharp
public event Action<ShipModuleLoadout> OnModuleLoadoutChanged;
public event Action<string, string> OnModuleEquipped;       // slotId, moduleId
public event Action<string, string> OnModuleUnequipped;     // slotId, moduleId
public event Action<ModuleStatType, float> OnStatBonusChanged;
public event Action<string> OnActiveEffectActivated;
public event Action<string> OnConditionalEffectTriggered;
```

---

## Initialization

```csharp
[Server]
private void InitializeLoadout()
{
    moduleLoadout = new ShipModuleLoadout();

    // Create default slots
    for (int i = 0; i < maxModuleSlots; i++)
    {
        var slot = new ModuleSlot
        {
            slotId = $"slot_{i}",
            slotName = $"Slot {i + 1}",
            slotType = i < 2 ? ModuleSlotType.Defensive :
                      i < 4 ? ModuleSlotType.Offensive :
                      ModuleSlotType.Utility,
            isUnlocked = true
        };
        moduleLoadout.slots.Add(slot);
    }
}

private void LoadModuleDefinitions()
{
    var definitions = Resources.LoadAll<ModuleDefinitionSO>("ModuleDefinitions");
    foreach (var def in definitions)
    {
        moduleDefinitions[def.equipmentId] = def;
    }
}
```

---

## Module Equipment

### Equip Module

```csharp
[Command]
public void CmdEquipModule(string slotId, string moduleInstanceId)
{
    var slot = moduleLoadout.GetSlot(slotId);
    var module = moduleLoadout.GetModule(moduleInstanceId);
    var definition = moduleDefinitions[module.moduleDefinitionId];

    // Check slot compatibility
    if (!slot.CanEquip(definition.category)) return;

    // Unequip existing module in slot
    if (!string.IsNullOrEmpty(slot.equippedModuleInstanceId))
    {
        UnequipModuleInternal(slotId);
    }

    // Equip the module
    slot.equippedModuleInstanceId = moduleInstanceId;
    module.isEquipped = true;
    module.equippedSlotId = slotId;

    RecalculateStatBonuses();
    RegisterModuleEffects(module, definition);

    OnModuleEquipped?.Invoke(slotId, moduleInstanceId);
    RpcNotifyModuleEquipped(slotId, moduleInstanceId);
}
```

### Unequip Module

```csharp
[Server]
private void UnequipModuleInternal(string slotId)
{
    var slot = moduleLoadout.GetSlot(slotId);
    var module = moduleLoadout.GetModule(slot.equippedModuleInstanceId);

    module.isEquipped = false;
    module.equippedSlotId = null;
    UnregisterModuleEffects(module);

    slot.equippedModuleInstanceId = null;
    RecalculateStatBonuses();

    OnModuleUnequipped?.Invoke(slotId, unequippedId);
    RpcNotifyModuleUnequipped(slotId, unequippedId);
}
```

---

## Stat Calculations

```csharp
[Server]
private void RecalculateStatBonuses()
{
    calculatedBonuses.Clear();

    foreach (var slot in moduleLoadout.slots)
    {
        if (string.IsNullOrEmpty(slot.equippedModuleInstanceId)) continue;

        var module = moduleLoadout.GetModule(slot.equippedModuleInstanceId);
        var definition = moduleDefinitions[module.moduleDefinitionId];
        float effectiveness = module.GetEffectiveness();

        foreach (var modifier in definition.statModifiers)
        {
            float bonus = (modifier.flatBonus + modifier.percentageModifier) * effectiveness;
            if (modifier.isPenalty) bonus = -Mathf.Abs(bonus);

            if (calculatedBonuses.ContainsKey(modifier.statType))
            {
                calculatedBonuses[modifier.statType] += bonus;
            }
            else
            {
                calculatedBonuses[modifier.statType] = bonus;
            }

            OnStatBonusChanged?.Invoke(modifier.statType, calculatedBonuses[modifier.statType]);
        }
    }

    // Update cached bonuses (List for Mirror serialization)
    moduleLoadout.SetCachedBonuses(calculatedBonuses);
}
```

### Stat Query Methods

```csharp
public float GetStatBonus(ModuleStatType statType)
{
    if (calculatedBonuses.TryGetValue(statType, out float bonus))
    {
        return bonus;
    }
    return 0f;
}

public float ApplyBonus(float baseValue, ModuleStatType statType)
{
    float bonus = GetStatBonus(statType);
    return baseValue * (1f + bonus);
}
```

---

## Active Effects

### Activate Effect

```csharp
[Command]
public void CmdActivateEffect(string effectId)
{
    var effect = activeEffects.Find(e => e.effectId == effectId);
    if (effect == null) return;

    if (effect.currentCooldown > 0 || effect.isActive) return;

    effect.isActive = true;
    effect.activeTimeRemaining = effect.duration;
    effect.currentCooldown = effect.cooldown;

    // TODO: Apply temporary stat modifiers

    OnActiveEffectActivated?.Invoke(effectId);
    RpcNotifyEffectActivated(effectId);
}
```

### Update Effects

```csharp
[Server]
private void UpdateActiveEffects(float deltaTime)
{
    for (int i = activeEffects.Count - 1; i >= 0; i--)
    {
        var effect = activeEffects[i];

        // Update cooldown
        if (effect.currentCooldown > 0)
        {
            effect.currentCooldown -= deltaTime;
        }

        // Update active duration
        if (effect.isActive)
        {
            effect.activeTimeRemaining -= deltaTime;
            if (effect.activeTimeRemaining <= 0)
            {
                effect.isActive = false;
                // Remove temporary stat modifiers
            }
        }
    }
}
```

### Trigger Conditional Effects

```csharp
[Server]
public void TriggerConditionalEffects(ModuleTriggerType triggerType)
{
    foreach (var effect in conditionalEffects)
    {
        if (effect.triggerType != triggerType) continue;

        // Check cooldown
        if (Time.time - effect.lastTriggerTime < effect.triggerCooldown) continue;

        // Check probability
        if (UnityEngine.Random.value > effect.triggerChance) continue;

        // Trigger effect
        effect.lastTriggerTime = Time.time;
        // Apply effect modifiers

        OnConditionalEffectTriggered?.Invoke(effect.effectId);
    }
}
```

---

## Module Upgrades

```csharp
[Command]
public void CmdUpgradeModule(string moduleInstanceId)
{
    var module = moduleLoadout.GetModule(moduleInstanceId);
    if (module == null) return;

    if (module.upgradeLevel >= maxUpgradeLevel) return;

    // TODO: Check upgrade requirements (cost, materials)

    module.upgradeLevel++;

    if (module.isEquipped)
    {
        RecalculateStatBonuses();
    }

    RpcNotifyModuleUpgraded(moduleInstanceId, module.upgradeLevel);
}
```

---

## Network Callbacks

```csharp
private void OnLoadoutChanged(ShipModuleLoadout oldLoadout, ShipModuleLoadout newLoadout)
{
    // Rebuild local bonus cache after network sync
    if (newLoadout != null)
    {
        newLoadout.RebuildBonusCache();
    }
    OnModuleLoadoutChanged?.Invoke(newLoadout);
}

[ClientRpc] private void RpcNotifyModuleEquipped(string slotId, string moduleId);
[ClientRpc] private void RpcNotifyModuleUnequipped(string slotId, string moduleId);
[ClientRpc] private void RpcNotifyEffectActivated(string effectId);
[ClientRpc] private void RpcNotifyModuleUpgraded(string moduleId, int newLevel);
```

---

## Public API

```csharp
public ShipModuleLoadout GetLoadout();
public int GetMaxSlots();
public int GetMaxUpgradeLevel();
public ModuleDefinitionSO GetModuleDefinition(string definitionId);
public List<ModuleActiveEffect> GetActiveEffects();
```

---

## Default Slot Layout

| Slot Index | Type |
|------------|------|
| 0-1 | Defensive |
| 2-3 | Offensive |
| 4-5 | Utility |

---

## Integration Points

### Dependencies
- [[ModuleData]] - Data structures
- [[ModuleDefinitionSO]] - Module definitions
- Mirror networking
- WOS.Debugging

### Used By
- UI module panel
- Combat systems (stat bonuses)
- Ship configuration

---

## Related Files
- [[ModuleData]] - Data structures
- [[ModuleNetworkSerializers]] - Network serialization
- [[ModuleDefinitionSO]] - Module definitions
- [[GenericEquipmentMount]] - Visual mounting

---

## Design Notes
- Server-authoritative with SyncVar synchronization
- Singleton pattern for global access
- 6 default module slots (2 defensive, 2 offensive, 2 utility)
- Definitions loaded from Resources/ModuleDefinitions
- Stats recalculated on every equip/unequip
- Effectiveness = condition * quality * upgrade multipliers
- Active effects have cooldown and duration
- Conditional effects trigger on game events
- Upgrade levels 0-5 maximum
- Cache rebuilt on client after network sync

