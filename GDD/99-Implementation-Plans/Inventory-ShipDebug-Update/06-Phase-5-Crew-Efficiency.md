# Phase 5: Crew Efficiency & Assignment

**Goal**: Implement GDD-compliant crew efficiency calculations and assignment system

---

## 5.1 Core Efficiency Formula

From GDD `03-Combat-Systems/Crew-Module-Mechanics.md`:

```
Module_Efficiency = Sailor_Factor × Stat_Factor

Where:
  Sailor_Factor = Current_Sailors / Max_Sailors
  Stat_Factor = 1.0 + ((Primary_Stat - 15) × 0.02)
```

### Critical Constraints

1. **Stat Cap**: Maximum stat value is **50** → Maximum Stat_Factor = **1.70** (+70%)
2. **Engine Floor**: Engine modules have **minimum 70% efficiency** regardless of crew status
3. **Neutral Crew Penalty**: Unclassified crews suffer **-20% efficiency** on all modules

---

## 5.2 Sailor Count Scaling Formula

```csharp
// Assets/Scripts/Crew/SailorScaling.cs
namespace WOS.Crew
{
    public static class SailorScaling
    {
        /// <summary>
        /// GDD Formula (Crew-Management.md):
        /// Levels 1-50:   10 + (Level - 1) × 5 sailors
        /// Levels 51-100: 255 + (Level - 50) × 4 sailors
        /// Levels 101-150: 455 + (Level - 100) × 3 sailors
        /// Levels 151-200: 605 + (Level - 150) × 2 sailors
        /// </summary>
        public static int GetMaxSailors(int level)
        {
            level = Mathf.Clamp(level, 1, 200);

            if (level <= 50)
                return 10 + (level - 1) * 5;       // 10 to 255 sailors
            else if (level <= 100)
                return 255 + (level - 50) * 4;    // 255 to 455 sailors
            else if (level <= 150)
                return 455 + (level - 100) * 3;   // 455 to 605 sailors
            else
                return 605 + (level - 150) * 2;   // 605 to 705 sailors
        }

        /// <summary>
        /// Quick reference for common levels
        /// </summary>
        public static readonly Dictionary<int, int> CommonLevelSailors = new()
        {
            { 1, 10 },
            { 25, 130 },
            { 50, 255 },
            { 75, 355 },
            { 100, 455 },
            { 150, 605 },
            { 200, 705 }
        };
    }
}
```

---

## 5.3 Crew Weight Formula

```csharp
// Assets/Scripts/Crew/CrewWeightCalculator.cs
namespace WOS.Crew
{
    public static class CrewWeightCalculator
    {
        private const float BASE_WEIGHT_PER_SAILOR = 0.1f;  // tons

        /// <summary>
        /// GDD Formula: Crew_Weight = Sailor_Count × 0.1 × (1.0 + Level/100)
        /// IMPORTANT: Uses MAX sailors, not current (represents equipment/quarters)
        /// </summary>
        public static float CalculateCrewWeight(int level, int maxSailors)
        {
            float levelModifier = 1.0f + (level / 100f);
            return maxSailors * BASE_WEIGHT_PER_SAILOR * levelModifier;
        }

        public static float CalculateCrewWeight(CrewCard crew)
        {
            int maxSailors = SailorScaling.GetMaxSailors(crew.level);
            return CalculateCrewWeight(crew.level, maxSailors);
        }

        /// <summary>
        /// Weight examples from GDD:
        /// Level 1 (10 sailors):   10 × 0.1 × 1.01 = 1.01 tons
        /// Level 50 (255 sailors): 255 × 0.1 × 1.50 = 38.3 tons
        /// Level 100 (455 sailors): 455 × 0.1 × 2.00 = 91 tons
        /// Level 200 (705 sailors): 705 × 0.1 × 3.00 = 211.5 tons
        /// </summary>
        public static readonly Dictionary<int, float> WeightExamples = new()
        {
            { 1, 1.01f },
            { 50, 38.3f },
            { 100, 91f },
            { 200, 211.5f }
        };
    }
}
```

---

## 5.4 Module Efficiency Calculator

```csharp
// Assets/Scripts/Crew/ModuleEfficiencyCalculator.cs
namespace WOS.Crew
{
    using UnityEngine;
    using WOS.ScriptableObjects.Ships;

    public class ModuleEfficiencyCalculator
    {
        // GDD Constants
        private const int STAT_BASELINE = 15;
        private const float STAT_SCALING_FACTOR = 0.02f;
        private const int STAT_CAP = 50;                    // Maximum stat value
        private const float MAX_STAT_FACTOR = 1.70f;        // At stat 50
        private const float NEUTRAL_CREW_PENALTY = 0.20f;   // -20% for neutral
        private const float ENGINE_EFFICIENCY_FLOOR = 0.70f; // Engine minimum

        /// <summary>
        /// Calculate sailor factor (casualty scaling)
        /// Sailor_Factor = Current_Sailors / Max_Sailors
        /// </summary>
        public float CalculateSailorFactor(int currentSailors, int maxSailors)
        {
            if (maxSailors <= 0) return 0f;
            return Mathf.Clamp01((float)currentSailors / maxSailors);
        }

        /// <summary>
        /// Calculate stat factor with STAT CAP enforcement
        /// Stat_Factor = 1.0 + ((Primary_Stat - 15) × 0.02)
        /// CAPPED at stat 50 → max factor 1.70
        /// </summary>
        public float CalculateStatFactor(int statValue)
        {
            // Enforce stat cap
            int cappedStat = Mathf.Min(statValue, STAT_CAP);
            float factor = 1.0f + ((cappedStat - STAT_BASELINE) * STAT_SCALING_FACTOR);

            // Clamp to valid range (0.84 at stat 7 to 1.70 at stat 50)
            return Mathf.Clamp(factor, 0.0f, MAX_STAT_FACTOR);
        }

        /// <summary>
        /// Calculate complete module efficiency
        /// Module_Efficiency = Sailor_Factor × Stat_Factor × (Modifiers)
        /// </summary>
        public ModuleEfficiencyResult CalculateEfficiency(
            CrewCard crew,
            ModuleDefinitionSO module,
            bool isNeutralCrew = false,
            bool isEngineModule = false)
        {
            if (crew == null || crew.currentSailors <= 0)
            {
                return new ModuleEfficiencyResult
                {
                    IsOperational = false,
                    TotalEfficiency = 0f,
                    SailorFactor = 0f,
                    StatFactor = 0f,
                    Status = ModuleOperationalStatus.NonFunctional
                };
            }

            int maxSailors = SailorScaling.GetMaxSailors(crew.level);
            float sailorFactor = CalculateSailorFactor(crew.currentSailors, maxSailors);

            // Get primary stat for this module type
            int primaryStat = GetPrimaryStat(crew, module.slotCategory);
            float statFactor = CalculateStatFactor(primaryStat);

            // Base efficiency calculation
            float baseEfficiency = sailorFactor * statFactor;

            // Apply neutral crew penalty
            if (isNeutralCrew)
            {
                baseEfficiency *= (1.0f - NEUTRAL_CREW_PENALTY);
            }

            // Apply engine floor if applicable
            float finalEfficiency = baseEfficiency;
            if (isEngineModule && finalEfficiency < ENGINE_EFFICIENCY_FLOOR)
            {
                finalEfficiency = ENGINE_EFFICIENCY_FLOOR;
            }

            return new ModuleEfficiencyResult
            {
                IsOperational = true,
                TotalEfficiency = finalEfficiency,
                SailorFactor = sailorFactor,
                StatFactor = statFactor,
                NeutralPenaltyApplied = isNeutralCrew,
                EngineFloorApplied = isEngineModule && baseEfficiency < ENGINE_EFFICIENCY_FLOOR,
                Status = GetOperationalStatus(sailorFactor)
            };
        }

        /// <summary>
        /// Get primary stat based on module category
        /// From GDD Stat-to-Module Effect Mapping
        /// </summary>
        private int GetPrimaryStat(CrewCard crew, EquipmentSlotCategory category)
        {
            return category switch
            {
                EquipmentSlotCategory.MainBattery => crew.stats.accuracy,
                EquipmentSlotCategory.SecondaryBattery => crew.stats.accuracy,
                EquipmentSlotCategory.TertiaryBattery => crew.stats.accuracy,
                EquipmentSlotCategory.AAHeavy => crew.stats.aaAccuracy,
                EquipmentSlotCategory.AALight => crew.stats.aaAccuracy,
                EquipmentSlotCategory.TorpedoTubes => crew.stats.torpedoAccuracy,
                EquipmentSlotCategory.EngineRoom => crew.stats.enginePower,
                EquipmentSlotCategory.DamageControl => crew.stats.fireFighting,
                EquipmentSlotCategory.Radar => crew.stats.detectionRange,
                EquipmentSlotCategory.Sonar => crew.stats.sonarRange,
                EquipmentSlotCategory.FireControl => crew.stats.radarAccuracy,
                _ => STAT_BASELINE  // Default baseline for misc modules
            };
        }

        private ModuleOperationalStatus GetOperationalStatus(float sailorFactor)
        {
            return sailorFactor switch
            {
                >= 0.80f => ModuleOperationalStatus.FullyOperational,
                >= 0.50f => ModuleOperationalStatus.Degraded,
                >= 0.25f => ModuleOperationalStatus.SeverelyDegraded,
                >= 0.01f => ModuleOperationalStatus.Critical,
                _ => ModuleOperationalStatus.NonFunctional
            };
        }
    }

    public struct ModuleEfficiencyResult
    {
        public bool IsOperational;
        public float TotalEfficiency;
        public float SailorFactor;
        public float StatFactor;
        public bool NeutralPenaltyApplied;
        public bool EngineFloorApplied;
        public ModuleOperationalStatus Status;
    }

    public enum ModuleOperationalStatus
    {
        FullyOperational,      // 80-100%
        Degraded,              // 50-79%
        SeverelyDegraded,      // 25-49%
        Critical,              // 1-24%
        NonFunctional          // 0%
    }
}
```

---

## 5.5 Stat-to-Module Effect Formulas

```csharp
// Assets/Scripts/Crew/ModuleEffectCalculator.cs
namespace WOS.Crew
{
    using UnityEngine;

    /// <summary>
    /// GDD-defined formulas for how stats affect module performance
    /// </summary>
    public static class ModuleEffectCalculator
    {
        #region Gunner Effects (Main/Secondary Batteries)

        /// <summary>
        /// Accuracy affects shell SPREAD (tightness of pattern)
        /// Final_Spread = Base_Spread × (2.0 - Efficiency)
        /// Higher efficiency = tighter spread
        /// </summary>
        public static float CalculateSpread(float baseSpread, float efficiency)
        {
            return baseSpread * (2.0f - efficiency);
        }

        /// <summary>
        /// Reload stat affects fire rate
        /// Final_Reload = Base_Reload / Efficiency
        /// Higher efficiency = faster reload
        /// </summary>
        public static float CalculateReloadTime(float baseReload, float efficiency)
        {
            if (efficiency <= 0) return float.MaxValue;
            return baseReload / efficiency;
        }

        /// <summary>
        /// Range stat affects maximum effective range
        /// Final_Range = Base_Range × Efficiency
        /// </summary>
        public static float CalculateEffectiveRange(float baseRange, float efficiency)
        {
            return baseRange * efficiency;
        }

        #endregion

        #region Engineer Effects (Propulsion)

        /// <summary>
        /// Engine power affects speed with 70% FLOOR
        /// Speed_Mod = 0.7 + (0.3 × Efficiency)
        /// Even badly damaged engines provide minimum 70% propulsion
        /// </summary>
        public static float CalculateSpeedModifier(float efficiency)
        {
            return 0.7f + (0.3f * efficiency);
        }

        /// <summary>
        /// Repair speed for engine self-repair
        /// Repair_Rate = Base_Rate × Efficiency
        /// </summary>
        public static float CalculateRepairRate(float baseRate, float efficiency)
        {
            return baseRate * efficiency;
        }

        /// <summary>
        /// Restore speed for disabled recovery
        /// Restore_Time = Base_Time / Efficiency
        /// </summary>
        public static float CalculateRestoreTime(float baseTime, float efficiency)
        {
            if (efficiency <= 0) return float.MaxValue;
            return baseTime / efficiency;
        }

        #endregion

        #region AA Specialist Effects

        /// <summary>
        /// AA Accuracy affects hit chance vs aircraft
        /// Hit_Chance = Base_Hit × Efficiency
        /// </summary>
        public static float CalculateAAHitChance(float baseHit, float efficiency)
        {
            return baseHit * efficiency;
        }

        #endregion

        #region Torpedo Specialist Effects

        /// <summary>
        /// Torpedo accuracy affects spread angle
        /// Final_Spread = Base_Spread / Efficiency
        /// Higher efficiency = tighter torpedo pattern
        /// </summary>
        public static float CalculateTorpedoSpread(float baseSpread, float efficiency)
        {
            if (efficiency <= 0) return baseSpread * 10f; // Very wide spread
            return baseSpread / efficiency;
        }

        #endregion

        #region Damage Control Effects

        /// <summary>
        /// Fire fighting speed
        /// Extinguish_Time = Base_Time / Efficiency
        /// </summary>
        public static float CalculateFireExtinguishTime(float baseTime, float efficiency)
        {
            if (efficiency <= 0) return float.MaxValue;
            return baseTime / efficiency;
        }

        /// <summary>
        /// Flood control pump rate
        /// Pump_Rate = Base_Rate × Efficiency
        /// </summary>
        public static float CalculatePumpRate(float baseRate, float efficiency)
        {
            return baseRate * efficiency;
        }

        #endregion

        #region Electronics/Radar Effects

        /// <summary>
        /// Detection range for radar/sensors
        /// Det_Range = Base_Range × Efficiency
        /// </summary>
        public static float CalculateDetectionRange(float baseRange, float efficiency)
        {
            return baseRange * efficiency;
        }

        /// <summary>
        /// Target lock speed
        /// Lock_Time = Base_Time / Efficiency
        /// </summary>
        public static float CalculateLockTime(float baseTime, float efficiency)
        {
            if (efficiency <= 0) return float.MaxValue;
            return baseTime / efficiency;
        }

        #endregion

        #region Command Officer Effects

        /// <summary>
        /// Command stat provides force multiplier to ALL other crew
        /// Command_Bonus = (Command - 15) × 0.025
        /// Effective_Crew_Stat = Base_Stat × (1 + Command_Bonus)
        /// </summary>
        public static float CalculateCommandBonus(int commandStat)
        {
            return (commandStat - 15) * 0.025f;
        }

        /// <summary>
        /// Apply command bonus to a crew stat
        /// </summary>
        public static int ApplyCommandBonus(int baseStat, float commandBonus)
        {
            return Mathf.RoundToInt(baseStat * (1.0f + commandBonus));
        }

        #endregion
    }
}
```

---

## 5.6 Crew Card Data Structure

```csharp
// Assets/Scripts/Crew/CrewCard.cs
namespace WOS.Crew
{
    using System;
    using UnityEngine;

    [Serializable]
    public class CrewCard
    {
        [Header("Identity")]
        public string crewId;
        public string crewName;
        public CrewClassification classification;
        public SpecializationTier specializationTier;

        [Header("Level & Experience")]
        public int level;
        public int currentXP;
        public int xpToNextLevel;

        [Header("Sailors")]
        public int currentSailors;      // After casualties
        public int maxSailors;          // Based on level

        [Header("Stats")]
        public CrewStats stats;

        [Header("Assignment")]
        public string assignedModuleSlotId;  // Which slot this crew is in
        public bool isAssigned => !string.IsNullOrEmpty(assignedModuleSlotId);

        /// <summary>
        /// Calculate weight using GDD formula
        /// </summary>
        public float GetWeight()
        {
            return CrewWeightCalculator.CalculateCrewWeight(level, maxSailors);
        }

        /// <summary>
        /// Check if this crew can be assigned to a module category
        /// </summary>
        public bool CanOperateModule(EquipmentSlotCategory category)
        {
            // Neutral crews can operate anything (with penalty)
            if (classification == CrewClassification.Neutral)
                return true;

            // Check classification → category mapping
            return ClassificationMatchesCategory(classification, category);
        }

        private bool ClassificationMatchesCategory(CrewClassification cls, EquipmentSlotCategory cat)
        {
            return cls switch
            {
                CrewClassification.Gunner => cat is EquipmentSlotCategory.MainBattery
                    or EquipmentSlotCategory.SecondaryBattery
                    or EquipmentSlotCategory.TertiaryBattery,

                CrewClassification.AASpecialist => cat is EquipmentSlotCategory.AAHeavy
                    or EquipmentSlotCategory.AALight,

                CrewClassification.TorpedoSpecialist => cat is EquipmentSlotCategory.TorpedoTubes
                    or EquipmentSlotCategory.TorpedoReload,

                CrewClassification.Engineer => cat is EquipmentSlotCategory.EngineRoom
                    or EquipmentSlotCategory.Boiler,

                CrewClassification.DamageControl => cat is EquipmentSlotCategory.DamageControl,

                CrewClassification.Electronics => cat is EquipmentSlotCategory.Radar
                    or EquipmentSlotCategory.FireControl
                    or EquipmentSlotCategory.Communication,

                CrewClassification.SonarOperator => cat is EquipmentSlotCategory.Sonar,

                _ => false
            };
        }
    }

    [Serializable]
    public struct CrewStats
    {
        // Gunner stats
        public int accuracy;
        public int reload;
        public int range;

        // AA stats
        public int aaAccuracy;
        public int aaReload;
        public int detection;

        // Torpedo stats
        public int torpedoAccuracy;
        public int tubeReload;
        public int spreadControl;

        // Engineer stats
        public int enginePower;
        public int repairSpeed;
        public int restoreSpeed;

        // Damage Control stats
        public int fireFighting;
        public int floodControl;

        // Electronics stats
        public int detectionRange;
        public int radarAccuracy;
        public int jamming;

        // Sonar stats
        public int sonarRange;
        public int contactAnalysis;
        public int noiseReduction;

        // Command stats
        public int command;
        public int tactics;
        public int leadership;
    }

    public enum CrewClassification
    {
        Neutral,            // Can operate any module with -20% penalty
        Gunner,             // Main/Secondary/Tertiary batteries
        AASpecialist,       // AA batteries
        TorpedoSpecialist,  // Torpedo tubes, depth charges
        Engineer,           // Engines, boilers
        DamageControl,      // DC stations
        Electronics,        // Radar, fire control, comms
        SonarOperator,      // Sonar systems
        CommandOfficer,     // Bridge
        SquadronLeader,     // Aircraft hangars
        FighterPilot,       // Fighter squadrons
        BomberPilot         // Bomber squadrons
    }

    public enum SpecializationTier
    {
        None,           // Level 1-24 (Neutral only)
        Basic,          // Level 25+ (first classification)
        Advanced,       // Level 50+ (specialization branch)
        Elite           // Level 100+ (mastery)
    }
}
```

---

## 5.7 Crew Casualty System

```csharp
// Assets/Scripts/Crew/CrewCasualtyManager.cs
namespace WOS.Crew
{
    using System;
    using System.Collections.Generic;
    using UnityEngine;

    public class CrewCasualtyManager
    {
        // Lethality factors from GDD
        private static readonly Dictionary<DamageType, float> LETHALITY_FACTORS = new()
        {
            { DamageType.HE, 0.15f },           // Fires, fragmentation
            { DamageType.APPenetrating, 0.25f }, // Internal damage
            { DamageType.APNonPen, 0.05f },     // Spalling only
            { DamageType.Torpedo, 0.10f },      // Flooding focused
            { DamageType.Bomb, 0.20f }          // Concussion, fire
        };

        public event Action<CrewCard, int> OnCrewCasualties;
        public event Action<CrewCard> OnCrewWipedOut;

        /// <summary>
        /// GDD Formula: Casualties = (Damage / Module_HP) × Sailor_Count × Lethality_Factor
        /// </summary>
        public int CalculateCasualties(
            float damageDealt,
            float moduleMaxHP,
            CrewCard crew,
            DamageType damageType)
        {
            if (crew == null || crew.currentSailors <= 0)
                return 0;

            float lethalityFactor = LETHALITY_FACTORS.GetValueOrDefault(damageType, 0.10f);
            float damageRatio = damageDealt / moduleMaxHP;

            int casualties = Mathf.FloorToInt(damageRatio * crew.currentSailors * lethalityFactor);

            return Mathf.Clamp(casualties, 0, crew.currentSailors);
        }

        /// <summary>
        /// Apply casualties to a crew card
        /// </summary>
        public void ApplyCasualties(CrewCard crew, int casualties)
        {
            if (crew == null || casualties <= 0)
                return;

            int previousSailors = crew.currentSailors;
            crew.currentSailors = Mathf.Max(0, crew.currentSailors - casualties);

            OnCrewCasualties?.Invoke(crew, casualties);

            if (crew.currentSailors == 0 && previousSailors > 0)
            {
                OnCrewWipedOut?.Invoke(crew);
            }
        }

        /// <summary>
        /// Fire/flooding causes distributed casualties across ALL crew
        /// Per_Tick = Intensity × Total_Sailors × Rate
        /// </summary>
        public void ApplyDistributedCasualties(
            List<CrewCard> allCrew,
            float intensity,
            float ratePerTick,
            bool isFloodingCompartment = false)
        {
            int totalSailors = 0;
            foreach (var crew in allCrew)
            {
                totalSailors += crew.currentSailors;
            }

            if (totalSailors <= 0) return;

            int totalCasualties = Mathf.FloorToInt(intensity * totalSailors * ratePerTick);

            // Distribute proportionally (or 3x for flooded compartments)
            foreach (var crew in allCrew)
            {
                float proportion = (float)crew.currentSailors / totalSailors;
                float multiplier = isFloodingCompartment ? 3f : 1f;
                int crewCasualties = Mathf.FloorToInt(totalCasualties * proportion * multiplier);

                if (crewCasualties > 0)
                {
                    ApplyCasualties(crew, crewCasualties);
                }
            }
        }

        /// <summary>
        /// Replenish sailors at port (costs credits)
        /// </summary>
        public int ReplenishCrew(CrewCard crew)
        {
            if (crew == null) return 0;

            int maxSailors = SailorScaling.GetMaxSailors(crew.level);
            int sailorsNeeded = maxSailors - crew.currentSailors;

            crew.currentSailors = maxSailors;
            crew.maxSailors = maxSailors;

            return sailorsNeeded;
        }
    }

    public enum DamageType
    {
        HE,
        APPenetrating,
        APNonPen,
        Torpedo,
        Bomb,
        Fire,
        Flooding
    }
}
```

---

## 5.8 Crew Assignment Panel UI

```csharp
// Assets/Scripts/UI/Fitting/CrewAssignmentPanel.cs
namespace WOS.UI.Fitting
{
    using System;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UI;
    using TMPro;
    using WOS.Crew;
    using WOS.ScriptableObjects.Ships;

    public class CrewAssignmentPanel : MonoBehaviour
    {
        [Header("References")]
        [SerializeField] private Transform crewListContainer;
        [SerializeField] private GameObject crewSlotPrefab;

        [Header("Selection Display")]
        [SerializeField] private TextMeshProUGUI selectedModuleLabel;
        [SerializeField] private TextMeshProUGUI mountCapacityText;
        [SerializeField] private TextMeshProUGUI moduleWeightText;
        [SerializeField] private TextMeshProUGUI availableForCrewText;

        [Header("Efficiency Preview")]
        [SerializeField] private TextMeshProUGUI projectedEfficiencyText;
        [SerializeField] private TextMeshProUGUI primaryStatEffectText;
        [SerializeField] private TextMeshProUGUI secondaryStatEffectText;
        [SerializeField] private Image fitCheckIndicator;
        [SerializeField] private TextMeshProUGUI fitCheckText;

        [Header("Color Coding")]
        [SerializeField] private Color colorFits = new Color(0.2f, 0.8f, 0.2f);
        [SerializeField] private Color colorTooHeavy = new Color(0.8f, 0.2f, 0.2f);
        [SerializeField] private Color colorWrongClass = new Color(0.8f, 0.6f, 0.2f);

        // Current context
        private EquipmentSlotDefinition _currentSlot;
        private ModuleDefinitionSO _currentModule;
        private List<CrewCard> _availableCrew = new();
        private CrewCard _selectedCrew;
        private ModuleEfficiencyCalculator _efficiencyCalculator;

        public event Action<CrewCard, EquipmentSlotDefinition> OnCrewAssigned;

        private void Awake()
        {
            _efficiencyCalculator = new ModuleEfficiencyCalculator();
        }

        /// <summary>
        /// Open panel for a specific module slot
        /// </summary>
        public void OpenForSlot(
            EquipmentSlotDefinition slot,
            ModuleDefinitionSO installedModule,
            List<CrewCard> unassignedCrew)
        {
            _currentSlot = slot;
            _currentModule = installedModule;
            _availableCrew = unassignedCrew;

            UpdateSlotInfo();
            PopulateCrewList();

            gameObject.SetActive(true);
        }

        private void UpdateSlotInfo()
        {
            selectedModuleLabel.text = _currentModule != null
                ? _currentModule.moduleName
                : "Empty Slot";

            float mountCapacity = _currentSlot.weightCapacityTons;
            float moduleWeight = _currentModule?.weightTons ?? 0f;
            float availableForCrew = mountCapacity - moduleWeight;

            mountCapacityText.text = $"Mount Capacity: {mountCapacity:F1} tons";
            moduleWeightText.text = $"Module Weight: {moduleWeight:F1} tons";
            availableForCrewText.text = $"Available for Crew: {availableForCrew:F1} tons";
        }

        private void PopulateCrewList()
        {
            // Clear existing
            foreach (Transform child in crewListContainer)
            {
                Destroy(child.gameObject);
            }

            // Create slots for each available crew
            foreach (var crew in _availableCrew)
            {
                var slotObj = Instantiate(crewSlotPrefab, crewListContainer);
                var slotUI = slotObj.GetComponent<CrewSelectionSlotUI>();

                if (slotUI != null)
                {
                    CrewFitStatus fitStatus = EvaluateCrewFit(crew);
                    slotUI.Setup(crew, fitStatus, OnCrewSelected);
                }
            }
        }

        private CrewFitStatus EvaluateCrewFit(CrewCard crew)
        {
            var status = new CrewFitStatus();

            // Check classification match
            if (_currentModule != null)
            {
                status.ClassificationMatches = crew.CanOperateModule(_currentModule.slotCategory);
                status.IsNeutralCrew = crew.classification == CrewClassification.Neutral;
            }
            else
            {
                status.ClassificationMatches = false;
            }

            // Check weight fit
            float mountCapacity = _currentSlot.weightCapacityTons;
            float moduleWeight = _currentModule?.weightTons ?? 0f;
            float availableWeight = mountCapacity - moduleWeight;
            float crewWeight = crew.GetWeight();

            status.CrewWeight = crewWeight;
            status.AvailableWeight = availableWeight;
            status.WeightFits = crewWeight <= availableWeight;

            // Overall fit determination
            status.CanAssign = status.ClassificationMatches && status.WeightFits;

            return status;
        }

        private void OnCrewSelected(CrewCard crew)
        {
            _selectedCrew = crew;
            UpdateEfficiencyPreview(crew);
        }

        private void UpdateEfficiencyPreview(CrewCard crew)
        {
            if (crew == null || _currentModule == null)
            {
                projectedEfficiencyText.text = "Efficiency: --";
                primaryStatEffectText.text = "";
                secondaryStatEffectText.text = "";
                return;
            }

            CrewFitStatus fitStatus = EvaluateCrewFit(crew);

            // Update fit check indicator
            if (!fitStatus.WeightFits)
            {
                fitCheckIndicator.color = colorTooHeavy;
                fitCheckText.text = $"TOO HEAVY ({fitStatus.CrewWeight:F1} > {fitStatus.AvailableWeight:F1} tons)";
            }
            else if (!fitStatus.ClassificationMatches)
            {
                fitCheckIndicator.color = colorWrongClass;
                fitCheckText.text = "CLASSIFICATION MISMATCH";
            }
            else
            {
                fitCheckIndicator.color = colorFits;
                fitCheckText.text = "FITS";
            }

            // Calculate projected efficiency
            bool isNeutral = crew.classification == CrewClassification.Neutral;
            bool isEngine = _currentModule.slotCategory == EquipmentSlotCategory.EngineRoom;

            var effResult = _efficiencyCalculator.CalculateEfficiency(
                crew, _currentModule, isNeutral, isEngine);

            projectedEfficiencyText.text = $"Projected Efficiency: {effResult.TotalEfficiency:P0}";

            // Show stat effects
            DisplayStatEffects(crew, effResult.TotalEfficiency);
        }

        private void DisplayStatEffects(CrewCard crew, float efficiency)
        {
            if (_currentModule == null) return;

            switch (_currentModule.slotCategory)
            {
                case EquipmentSlotCategory.MainBattery:
                case EquipmentSlotCategory.SecondaryBattery:
                    float spreadMod = (2.0f - efficiency);
                    float reloadMod = 1f / efficiency;
                    primaryStatEffectText.text = $"Spread: ×{spreadMod:F2}";
                    secondaryStatEffectText.text = $"Reload: ×{reloadMod:F2}";
                    break;

                case EquipmentSlotCategory.EngineRoom:
                    float speedMod = ModuleEffectCalculator.CalculateSpeedModifier(efficiency);
                    primaryStatEffectText.text = $"Speed: {speedMod:P0}";
                    secondaryStatEffectText.text = "(70% floor applied)";
                    break;

                default:
                    primaryStatEffectText.text = $"Effect: ×{efficiency:F2}";
                    secondaryStatEffectText.text = "";
                    break;
            }
        }

        public void OnConfirmAssignment()
        {
            if (_selectedCrew == null || _currentSlot == null)
                return;

            CrewFitStatus fitStatus = EvaluateCrewFit(_selectedCrew);
            if (!fitStatus.CanAssign)
                return;

            // Assign crew to slot
            _selectedCrew.assignedModuleSlotId = _currentSlot.slotId;

            OnCrewAssigned?.Invoke(_selectedCrew, _currentSlot);

            Close();
        }

        public void Close()
        {
            _selectedCrew = null;
            gameObject.SetActive(false);
        }
    }

    public struct CrewFitStatus
    {
        public bool ClassificationMatches;
        public bool IsNeutralCrew;
        public bool WeightFits;
        public float CrewWeight;
        public float AvailableWeight;
        public bool CanAssign;
    }
}
```

---

## 5.9 Crew Selection Slot UI

```csharp
// Assets/Scripts/UI/Fitting/CrewSelectionSlotUI.cs
namespace WOS.UI.Fitting
{
    using System;
    using UnityEngine;
    using UnityEngine.UI;
    using TMPro;
    using WOS.Crew;

    public class CrewSelectionSlotUI : MonoBehaviour
    {
        [Header("Display Elements")]
        [SerializeField] private TextMeshProUGUI crewNameText;
        [SerializeField] private TextMeshProUGUI classificationText;
        [SerializeField] private TextMeshProUGUI levelText;
        [SerializeField] private TextMeshProUGUI sailorCountText;
        [SerializeField] private TextMeshProUGUI weightText;
        [SerializeField] private Image classificationIcon;
        [SerializeField] private Image statusIndicator;
        [SerializeField] private Button selectButton;

        [Header("Status Colors")]
        [SerializeField] private Color colorCanFit = new Color(0.2f, 0.8f, 0.2f);
        [SerializeField] private Color colorTooHeavy = new Color(0.8f, 0.2f, 0.2f);
        [SerializeField] private Color colorWrongClass = new Color(0.8f, 0.6f, 0.2f);
        [SerializeField] private Color colorNeutral = new Color(0.6f, 0.6f, 0.8f);

        private CrewCard _crew;
        private Action<CrewCard> _onSelected;

        public void Setup(CrewCard crew, CrewFitStatus fitStatus, Action<CrewCard> onSelected)
        {
            _crew = crew;
            _onSelected = onSelected;

            // Basic info
            crewNameText.text = crew.crewName;
            classificationText.text = crew.classification.ToString();
            levelText.text = $"Lv.{crew.level}";
            sailorCountText.text = $"{crew.currentSailors}/{crew.maxSailors} sailors";
            weightText.text = $"{crew.GetWeight():F1} tons";

            // Status indicator
            if (!fitStatus.WeightFits)
            {
                statusIndicator.color = colorTooHeavy;
                selectButton.interactable = false;
            }
            else if (!fitStatus.ClassificationMatches)
            {
                statusIndicator.color = colorWrongClass;
                selectButton.interactable = false;
            }
            else if (fitStatus.IsNeutralCrew)
            {
                statusIndicator.color = colorNeutral;
                selectButton.interactable = true;
            }
            else
            {
                statusIndicator.color = colorCanFit;
                selectButton.interactable = true;
            }

            selectButton.onClick.AddListener(OnClick);
        }

        private void OnClick()
        {
            _onSelected?.Invoke(_crew);
        }

        private void OnDestroy()
        {
            selectButton.onClick.RemoveListener(OnClick);
        }
    }
}
```

---

## 5.10 Module Status Display

```csharp
// Assets/Scripts/UI/HUD/ModuleStatusDisplay.cs
namespace WOS.UI.HUD
{
    using UnityEngine;
    using UnityEngine.UI;
    using TMPro;
    using WOS.Crew;

    /// <summary>
    /// Real-time module status display during combat
    /// Updates: sailor count, efficiency, operational status
    /// </summary>
    public class ModuleStatusDisplay : MonoBehaviour
    {
        [Header("Display Elements")]
        [SerializeField] private TextMeshProUGUI moduleNameText;
        [SerializeField] private TextMeshProUGUI crewNameText;
        [SerializeField] private TextMeshProUGUI sailorCountText;
        [SerializeField] private Slider sailorSlider;
        [SerializeField] private TextMeshProUGUI efficiencyText;
        [SerializeField] private Image statusIndicator;
        [SerializeField] private TextMeshProUGUI statusText;

        [Header("Stat Effect Display")]
        [SerializeField] private TextMeshProUGUI primaryStatEffectText;
        [SerializeField] private TextMeshProUGUI secondaryStatEffectText;

        [Header("Color Coding (GDD Spec)")]
        [SerializeField] private Color colorGreen = new Color(0.2f, 0.8f, 0.2f);   // 80-100%
        [SerializeField] private Color colorYellow = new Color(0.8f, 0.8f, 0.2f);  // 50-79%
        [SerializeField] private Color colorOrange = new Color(0.8f, 0.5f, 0.2f);  // 25-49%
        [SerializeField] private Color colorRed = new Color(0.8f, 0.2f, 0.2f);     // 1-24%
        [SerializeField] private Color colorGray = new Color(0.5f, 0.5f, 0.5f);    // 0%

        private ModuleEfficiencyCalculator _calculator = new();

        public void UpdateDisplay(
            string moduleName,
            CrewCard crew,
            ModuleDefinitionSO module)
        {
            moduleNameText.text = moduleName;

            if (crew == null)
            {
                crewNameText.text = "UNMANNED";
                sailorCountText.text = "0/0";
                sailorSlider.value = 0f;
                efficiencyText.text = "0%";
                statusIndicator.color = colorGray;
                statusText.text = "NON-FUNCTIONAL";
                primaryStatEffectText.text = "";
                secondaryStatEffectText.text = "";
                return;
            }

            if (crew.currentSailors == 0)
            {
                crewNameText.text = crew.crewName;
                sailorCountText.text = $"0/{crew.maxSailors}";
                sailorSlider.value = 0f;
                efficiencyText.text = "0%";
                statusIndicator.color = colorGray;
                statusText.text = "CREW WIPED OUT";
                primaryStatEffectText.text = "";
                secondaryStatEffectText.text = "";
                return;
            }

            // Active crew display
            crewNameText.text = crew.crewName;
            sailorCountText.text = $"{crew.currentSailors}/{crew.maxSailors}";
            sailorSlider.value = (float)crew.currentSailors / crew.maxSailors;

            // Calculate efficiency
            bool isNeutral = crew.classification == CrewClassification.Neutral;
            bool isEngine = module.slotCategory == EquipmentSlotCategory.EngineRoom;

            var result = _calculator.CalculateEfficiency(crew, module, isNeutral, isEngine);

            efficiencyText.text = $"{result.TotalEfficiency:P0}";

            // Status color and text
            UpdateStatusDisplay(result);
        }

        private void UpdateStatusDisplay(ModuleEfficiencyResult result)
        {
            switch (result.Status)
            {
                case ModuleOperationalStatus.FullyOperational:
                    statusIndicator.color = colorGreen;
                    statusText.text = "OPERATIONAL";
                    break;
                case ModuleOperationalStatus.Degraded:
                    statusIndicator.color = colorYellow;
                    statusText.text = "DEGRADED";
                    break;
                case ModuleOperationalStatus.SeverelyDegraded:
                    statusIndicator.color = colorOrange;
                    statusText.text = "SEVERE";
                    break;
                case ModuleOperationalStatus.Critical:
                    statusIndicator.color = colorRed;
                    statusText.text = "CRITICAL";
                    break;
                case ModuleOperationalStatus.NonFunctional:
                    statusIndicator.color = colorGray;
                    statusText.text = "NON-FUNCTIONAL";
                    break;
            }
        }
    }
}
```

---

## Phase 5 Validation Checklist

```
[ ] ModuleEfficiencyCalculator with stat cap (50) enforcement
[ ] Stat_Factor correctly capped at 1.70
[ ] Engine efficiency floor at 70% implemented
[ ] Neutral crew -20% penalty applied
[ ] Sailor count scaling formula matches GDD breakpoints
[ ] Crew weight formula: Sailor_Count × 0.1 × (1.0 + Level/100)
[ ] Casualty formula: (Damage/ModuleHP) × Sailors × Lethality
[ ] All lethality factors match GDD (HE 0.15, AP 0.25, etc.)
[ ] Crew assignment panel shows weight fit check
[ ] Classification → Module type mapping complete
[ ] Real-time module status display with color coding
[ ] Command officer bonus calculation implemented
[ ] Fire/flooding distributed casualties work correctly
[ ] Replenishment system restores to max sailors
[ ] All stat-to-module effect formulas implemented
```

---

*Phase 5 Crew Efficiency - Version 3.0*
