# PermadeathData.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Permadeath/Data/PermadeathData.cs` |
| **Namespace** | `WOS.Permadeath.Data` |
| **Lines** | ~497 |
| **Architecture** | Pure data classes and enums for permadeath/extraction systems |

## Purpose
Defines all data structures, enumerations, and serializable classes for the permadeath, extraction, insurance, and salvage systems. Provides the complete type foundation for risk-reward gameplay mechanics.

---

## Enumerations

### Death Types
```csharp
public enum DeathType
{
    Combat,         // Destroyed by enemy
    Environmental,  // Storm, collision, grounding
    Scuttled,       // Self-destruct
    Disconnected,   // Left in danger zone
    Extraction      // Died during extraction
}
```

### Extraction States
```csharp
public enum ExtractionState
{
    Inactive,       // Not available
    Available,      // Can be used
    Contested,      // Enemy presence
    InProgress,     // Player extracting
    Completed,      // Recently used
    Destroyed       // Temporarily unavailable
}
```

### Extraction Results
```csharp
public enum ExtractionResult
{
    Success,        // Full extraction
    Partial,        // Some cargo lost
    Interrupted,    // Extraction cancelled
    Failed,         // Ship destroyed
    Timeout         // Time ran out
}
```

### Insurance Tiers
| Tier | Hull Coverage |
|------|---------------|
| None | 0% |
| Basic | 25% |
| Standard | 50% |
| Premium | 75% |
| Full | 100% (expensive) |

### Salvage Quality
| Quality | Value Multiplier |
|---------|------------------|
| Debris | 0.1x (minimal) |
| Damaged | 0.5x (reduced) |
| Recovered | 1.0x (standard) |
| Pristine | 1.5x (full) |

### Risk Zones
| Zone | Death Penalty |
|------|---------------|
| Safe | None (practice) |
| Low | 10% |
| Medium | 25% |
| High | 50% |
| Extreme | 75% |
| Hardcore | 100% (true permadeath) |

---

## Death Penalty Classes

### DeathPenalty
Complete death penalty calculation result.

```csharp
[Serializable]
public class DeathPenalty
{
    // Identifiers
    public string playerId;
    public string shipId;
    public DeathType deathType;
    public RiskZone riskZone;

    // Ship Loss
    public bool shipDestroyed;
    public float shipValueLost;
    public float insurancePayout;

    // Cargo Loss
    public List<LostCargoItem> lostCargo;
    public float cargoValueLost;

    // Crew Loss
    public List<string> lostCrewIds;
    public int crewCasualties;

    // Currency/Reputation
    public float currencyLost;
    public float reputationLost;

    // Recovery
    public bool canSalvage;
    public string salvageLocationId;
    public float salvageWindowEndTime;
}
```

### TierDeathPenalty
Configurable death penalty settings per ship tier.

```csharp
[Serializable]
public class TierDeathPenalty
{
    public int shipTier;

    [Range(0f, 1f)] public float shipLossChance = 1f;
    [Range(0f, 1f)] public float cargoLossPercent = 0.5f;
    [Range(0f, 1f)] public float crewLossChance = 0.25f;
    [Range(0f, 1f)] public float currencyPenaltyPercent = 0.1f;

    public float baseRepairCost;
    public float respawnCooldown;
    public bool allowsSalvage;
    public float salvageWindowDuration = 300f;  // 5 minutes
}
```

### LostCargoItem
Individual lost cargo item tracking.

```csharp
[Serializable]
public class LostCargoItem
{
    public string itemId;
    public string itemName;
    public int quantity;
    public float unitValue;
    public bool recoverable;
    public SalvageQuality salvageQuality;
}
```

---

## Extraction Classes

### ExtractionPoint
Extraction point definition and configuration.

```csharp
[Serializable]
public class ExtractionPoint
{
    public string extractionId;
    public string zoneId;
    public string displayName;

    // Location
    public Vector3 position;
    public float interactionRadius = 50f;
    public float safeZoneRadius = 100f;

    // State
    public ExtractionState state;
    public float stateChangeTime;
    public string occupyingPlayerId;

    // Requirements
    public int minTier;
    public int maxTier;
    public float extractionDuration = 30f;
    public bool requiresClearArea;

    // Availability
    public float activeStartTime;
    public float activeEndTime;
    public float cooldownDuration = 300f;
    public int maxUsesPerCycle = 3;
    public int currentUses;
}
```

### ExtractionAttempt
Active extraction attempt tracking.

```csharp
[Serializable]
public class ExtractionAttempt
{
    public string attemptId;
    public string playerId;
    public string shipId;
    public string extractionPointId;

    // Timing
    public float startTime;
    public float requiredDuration;
    public float currentProgress;

    // Cargo
    public List<ExtractionCargoItem> cargoToExtract;
    public float totalCargoValue;

    // Status
    public bool isInterrupted;
    public string interruptReason;
    public int threatCount;
}
```

### ExtractionResultData
Extraction completion data with rewards.

```csharp
[Serializable]
public class ExtractionResultData
{
    public string attemptId;
    public string playerId;
    public ExtractionResult result;

    // Extracted Items
    public List<ExtractedItem> extractedItems;
    public float totalValueExtracted;
    public float bonusMultiplier;

    // Rewards
    public float currencyReward;
    public float reputationReward;
    public float experienceReward;

    // Statistics
    public float extractionTime;
    public int threatsEvaded;
    public bool wasContested;
}
```

---

## Insurance Classes

### InsurancePolicy
Active insurance policy for a ship.

```csharp
[Serializable]
public class InsurancePolicy
{
    public string policyId;
    public string playerId;
    public string shipId;

    // Coverage
    public InsuranceTier tier;
    [Range(0f, 1f)] public float coveragePercent;
    public float maxPayout;
    public float deductible;

    // Terms
    public float premiumCost;
    public float purchaseTime;
    public float expirationTime;
    public int claimsRemaining;
    public int maxClaims = 1;

    // Restrictions
    public List<DeathType> excludedDeathTypes;
    public List<string> excludedZoneIds;
    public bool coversCargoLoss;
    public bool coversCrewLoss;
}
```

### InsuranceClaim
Insurance claim processing data.

```csharp
[Serializable]
public class InsuranceClaim
{
    public string claimId;
    public string policyId;
    public string playerId;

    // Loss Details
    public DeathType deathType;
    public string zoneId;
    public float shipValue;
    public float cargoValue;

    // Payout
    public float claimAmount;
    public float approvedAmount;
    public float deductibleApplied;
    public bool isApproved;
    public string denialReason;

    // Processing
    public float claimTime;
    public float processedTime;
    public bool isPaid;
}
```

### InsuranceTierConfig
Insurance tier configuration.

```csharp
[Serializable]
public class InsuranceTierConfig
{
    public InsuranceTier tier;
    public string displayName;

    // Coverage
    [Range(0f, 1f)] public float hullCoverage;
    [Range(0f, 1f)] public float cargoCoverage;
    [Range(0f, 1f)] public float crewCoverage;

    // Cost
    public float premiumMultiplier;    // × ship value
    public float deductiblePercent;
    public int claimsPerPolicy;

    // Availability
    public int minPlayerLevel;
    public int minShipTier;
    public float cooldownAfterClaim = 3600f;  // 1 hour
}
```

---

## Salvage Classes

### SalvageableWreck
Salvageable wreck from destroyed ship.

```csharp
[Serializable]
public class SalvageableWreck
{
    public string wreckId;
    public string originalShipId;
    public string originalPlayerId;

    // Location
    public string zoneId;
    public Vector3 position;
    public float heading;

    // State
    public float creationTime;
    public float expirationTime;
    public bool isBeingSalvaged;
    public string salvagingPlayerId;

    // Contents
    public List<SalvageItem> salvageItems;
    public float totalSalvageValue;
    public float salvageProgress;

    // Difficulty
    public float salvageDifficulty;
    public bool requiresSpecialEquipment;
    public float depthMeters;
}
```

### SalvageItem
Individual salvage item data.

```csharp
[Serializable]
public class SalvageItem
{
    public string itemId;
    public string itemName;
    public int quantity;
    public SalvageQuality quality;
    public float baseValue;
    public float salvageChance;
    public bool isRecovered;
}
```

### SalvageResult
Salvage operation result.

```csharp
[Serializable]
public class SalvageResult
{
    public string wreckId;
    public string salvagerId;

    public List<SalvageItem> recoveredItems;
    public float totalValueRecovered;

    public float operationDuration;
    public float successRate;
    public bool wasInterrupted;
}
```

---

## Risk/Reward Configuration

### RiskZoneConfig
Risk zone configuration with penalties and rewards.

```csharp
[Serializable]
public class RiskZoneConfig
{
    public RiskZone riskLevel;
    public string displayName;
    public Color zoneColor;

    // Penalties
    [Range(0f, 1f)] public float deathPenaltyMultiplier;
    [Range(0f, 1f)] public float cargoLossMultiplier;
    [Range(0f, 1f)] public float currencyLossMultiplier;

    // Rewards
    public float lootMultiplier = 1f;
    public float experienceMultiplier = 1f;
    public float reputationMultiplier = 1f;

    // Features
    public bool allowsInsurance;
    public bool allowsSalvage;
    public bool allowsRespawnInZone;
    public float respawnCooldownMultiplier = 1f;
}
```

### PlayerDeathStats
Cumulative player death statistics.

```csharp
[Serializable]
public class PlayerDeathStats
{
    public string playerId;

    // Deaths by type
    public int totalDeaths;
    public int combatDeaths;
    public int environmentalDeaths;
    public int extractionDeaths;

    // Losses
    public int shipsLost;
    public int crewLost;
    public float totalValueLost;
    public float totalCargoLost;

    // Recovery
    public int successfulSalvages;
    public int insuranceClaimsPaid;
    public float totalInsuranceReceived;

    // Extraction
    public int extractionAttempts;
    public int successfulExtractions;
    public float totalValueExtracted;
}
```

---

## Integration Points

### Used By
- `PermadeathManager.cs` - Death processing and insurance
- `ExtractionController.cs` - Extraction point management
- UI systems for death/insurance/salvage displays

### Design References
- Based on GDD Risk-Reward.md specifications

---

## Design Notes

### Risk-Reward Balance
- Higher risk zones = higher penalties but better loot/XP multipliers
- Insurance provides safety net at cost
- Extraction allows safe cargo recovery

### Salvage Economy
- Quality affects value multiplier (0.1x to 1.5x)
- Time-limited recovery window
- Competition for valuable wrecks

### Insurance Tiers
- Scaling coverage from 25% to 100%
- Premium cost based on ship value
- Death type exclusions possible

### Hardcore Mode
- 100% loss (true permadeath)
- No insurance allowed
- Maximum reward multipliers
