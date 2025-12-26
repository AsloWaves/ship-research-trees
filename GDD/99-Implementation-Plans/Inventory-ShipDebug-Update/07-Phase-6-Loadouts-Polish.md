# Phase 6: Loadout Presets & Polish

**Goal**: Implement loadout save/load system, share codes, undo/redo, and UI polish

---

## 6.1 Loadout Preset System Overview

From GDD `04-Ship-Customization/Ship-Fitting-UI.md`:

**Key Features**:
1. Save complete ship configurations as presets
2. Load presets with module ownership check
3. Share via alphanumeric codes and QR
4. Community preset library with ratings
5. Auto-crew assignment on load

---

## 6.2 Loadout Preset Data Structure

```csharp
// Assets/Scripts/Loadouts/LoadoutPreset.cs
namespace WOS.Loadouts
{
    using System;
    using System.Collections.Generic;
    using UnityEngine;
    using WOS.ScriptableObjects.Ships;

    [Serializable]
    public class LoadoutPreset
    {
        [Header("Preset Identity")]
        public string presetId;
        public string presetName;              // "Iowa Maximum Firepower"
        public string description;             // Markdown supported
        public string creatorPlayerId;
        public string creatorDisplayName;
        public DateTime createdAt;
        public DateTime lastModified;

        [Header("Target Ship")]
        public string targetShipId;            // Which ship class this is for
        public string targetShipName;          // Display name (e.g., "USS Iowa")
        public int targetTier;                 // T1-T10

        [Header("Module Configuration")]
        public List<SlotAssignment> slotAssignments;

        [Header("Armor Configuration")]
        public ArmorPresetData armorConfig;

        [Header("Cargo Layout (Optional)")]
        public List<CargoPresetItem> cargoLayout;

        [Header("Metadata")]
        public LoadoutVisibility visibility;
        public List<LoadoutTag> tags;
        public LoadoutRating rating;

        [Header("Sharing")]
        public string shareCode;               // "IOWA-AA-2F8K9X"
        public bool isPublished;
    }

    [Serializable]
    public class SlotAssignment
    {
        public string slotId;                  // Target slot
        public string moduleDefinitionId;      // Which module goes here
        public string assignedCrewId;          // Optional crew assignment
    }

    [Serializable]
    public class ArmorPresetData
    {
        public float beltThicknessInches;
        public float deckThicknessInches;
        public float bulkheadThicknessInches;
        public float turretFaceThicknessInches;
        public float turretRoofThicknessInches;
        public float turretSidesThicknessInches;
        public float barbetteThicknessInches;
        public float conningTowerThicknessInches;
        public float citadelThicknessInches;

        public ArmorMaterial beltMaterial;
        public ArmorMaterial deckMaterial;
        // ... etc for each zone
    }

    [Serializable]
    public class CargoPresetItem
    {
        public string itemDefinitionId;
        public Vector2Int gridPosition;
        public bool isRotated;
        public string partitionId;
    }

    public enum LoadoutVisibility
    {
        Private,        // Only creator can see
        FriendsOnly,    // Friends can view
        Public          // Listed in community library
    }

    [Serializable]
    public class LoadoutTag
    {
        public string tagName;
        public static readonly string[] STANDARD_TAGS = new[]
        {
            "AA Build", "Speed", "Armor", "Firepower",
            "Balanced", "Budget", "Premium", "PvP", "PvE",
            "T1-T3", "T4-T6", "T7-T10"
        };
    }

    [Serializable]
    public class LoadoutRating
    {
        public float averageStars;             // 1.0 - 5.0
        public int totalRatings;
        public int downloads;
        public int upvotes;
        public int downvotes;
    }
}
```

---

## 6.3 Loadout Preset Manager

```csharp
// Assets/Scripts/Loadouts/LoadoutPresetManager.cs
namespace WOS.Loadouts
{
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    using UnityEngine;
    using WOS.Networking.Managers;
    using WOS.ScriptableObjects;
    using WOS.ScriptableObjects.Ships;

    public class LoadoutPresetManager : MonoBehaviour
    {
        public static LoadoutPresetManager Instance { get; private set; }

        [Header("Local Cache")]
        [SerializeField] private int maxCachedPresets = 100;

        private List<LoadoutPreset> _localPresets = new();
        private Dictionary<string, LoadoutPreset> _presetCache = new();

        public event Action<LoadoutPreset> OnPresetSaved;
        public event Action<LoadoutPreset> OnPresetLoaded;
        public event Action<LoadoutPreset> OnPresetDeleted;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }
            Instance = this;
            DontDestroyOnLoad(gameObject);

            LoadLocalPresets();
        }

        #region Save Preset

        /// <summary>
        /// Create new preset from current ship configuration
        /// </summary>
        public async Task<LoadoutPreset> SavePreset(
            ShipConfigurationSO shipConfig,
            List<InstalledModule> installedModules,
            ArmorZoneConfiguration armorConfig,
            string presetName,
            string description,
            LoadoutVisibility visibility,
            List<LoadoutTag> tags)
        {
            var preset = new LoadoutPreset
            {
                presetId = Guid.NewGuid().ToString(),
                presetName = presetName,
                description = description,
                creatorPlayerId = PlayFabInventoryService.Instance?.GetPlayerId() ?? "local",
                creatorDisplayName = AuthenticationManager.Instance?.DisplayName ?? "Player",
                createdAt = DateTime.UtcNow,
                lastModified = DateTime.UtcNow,
                targetShipId = shipConfig.shipId,
                targetShipName = shipConfig.shipName,
                targetTier = shipConfig.tier,
                slotAssignments = new List<SlotAssignment>(),
                visibility = visibility,
                tags = tags,
                rating = new LoadoutRating()
            };

            // Capture slot assignments
            foreach (var module in installedModules)
            {
                preset.slotAssignments.Add(new SlotAssignment
                {
                    slotId = module.slotId,
                    moduleDefinitionId = module.moduleDefinition.moduleId,
                    assignedCrewId = module.assignedCrew?.crewId
                });
            }

            // Capture armor config
            preset.armorConfig = ConvertArmorConfig(armorConfig);

            // Generate share code
            preset.shareCode = GenerateShareCode(preset);

            // Save locally
            _localPresets.Add(preset);
            _presetCache[preset.presetId] = preset;
            SaveLocalPresets();

            // Upload if public
            if (visibility == LoadoutVisibility.Public)
            {
                await UploadPresetToCloud(preset);
            }

            OnPresetSaved?.Invoke(preset);
            return preset;
        }

        private ArmorPresetData ConvertArmorConfig(ArmorZoneConfiguration config)
        {
            return new ArmorPresetData
            {
                beltThicknessInches = config.belt.thicknessInches,
                deckThicknessInches = config.deck.thicknessInches,
                bulkheadThicknessInches = config.bulkhead.thicknessInches,
                turretFaceThicknessInches = config.turretFace.thicknessInches,
                turretRoofThicknessInches = config.turretRoof.thicknessInches,
                turretSidesThicknessInches = config.turretSides.thicknessInches,
                barbetteThicknessInches = config.barbette.thicknessInches,
                conningTowerThicknessInches = config.conningTower.thicknessInches,
                citadelThicknessInches = config.citadel.thicknessInches,
                beltMaterial = config.belt.material,
                deckMaterial = config.deck.material
            };
        }

        #endregion

        #region Load Preset

        /// <summary>
        /// Apply preset to current ship
        /// Returns list of missing modules that need purchase
        /// </summary>
        public async Task<PresetApplicationResult> ApplyPreset(
            LoadoutPreset preset,
            ShipConfigurationSO targetShip,
            ItemDatabaseSO itemDatabase)
        {
            var result = new PresetApplicationResult();

            // Validate ship compatibility
            if (preset.targetShipId != targetShip.shipId)
            {
                result.Success = false;
                result.ErrorMessage = "Preset is for different ship class";
                return result;
            }

            // Check module ownership
            var playerInventory = await PlayFabInventoryService.Instance.GetInventoryAsync();

            foreach (var assignment in preset.slotAssignments)
            {
                var moduleDef = itemDatabase.GetModuleById(assignment.moduleDefinitionId);
                if (moduleDef == null)
                {
                    result.MissingModules.Add(new MissingModuleInfo
                    {
                        ModuleId = assignment.moduleDefinitionId,
                        ModuleName = "Unknown Module",
                        Cost = 0
                    });
                    continue;
                }

                bool owned = playerInventory.HasItem(assignment.moduleDefinitionId);
                if (!owned)
                {
                    result.MissingModules.Add(new MissingModuleInfo
                    {
                        ModuleId = assignment.moduleDefinitionId,
                        ModuleName = moduleDef.moduleName,
                        Cost = moduleDef.purchaseCost
                    });
                }
            }

            result.TotalCost = 0;
            foreach (var missing in result.MissingModules)
            {
                result.TotalCost += missing.Cost;
            }

            result.Success = result.MissingModules.Count == 0;
            result.Preset = preset;

            return result;
        }

        /// <summary>
        /// Purchase missing modules and apply preset
        /// </summary>
        public async Task<bool> PurchaseAndApplyPreset(PresetApplicationResult applicationResult)
        {
            if (applicationResult.MissingModules.Count > 0)
            {
                // Purchase all missing modules
                foreach (var missing in applicationResult.MissingModules)
                {
                    bool purchased = await PlayFabInventoryService.Instance
                        .PurchaseItemAsync(missing.ModuleId, missing.Cost);

                    if (!purchased)
                    {
                        Debug.LogError($"Failed to purchase module: {missing.ModuleName}");
                        return false;
                    }
                }
            }

            // Now apply the configuration
            // This would interface with the ship fitting system
            OnPresetLoaded?.Invoke(applicationResult.Preset);

            return true;
        }

        #endregion

        #region Share Codes

        /// <summary>
        /// Generate alphanumeric share code
        /// Format: SHIPNAME-STYLE-XXXXXX
        /// </summary>
        private string GenerateShareCode(LoadoutPreset preset)
        {
            // Get ship abbreviation
            string shipAbbrev = GetShipAbbreviation(preset.targetShipName);

            // Get build style from tags
            string styleAbbrev = GetStyleAbbreviation(preset.tags);

            // Generate random 6-char code
            string randomPart = GenerateRandomCode(6);

            return $"{shipAbbrev}-{styleAbbrev}-{randomPart}";
        }

        private string GetShipAbbreviation(string shipName)
        {
            // Take first 4 chars, uppercase
            if (string.IsNullOrEmpty(shipName)) return "SHIP";
            return shipName.Replace("USS ", "").Replace(" ", "")
                .Substring(0, Mathf.Min(4, shipName.Length)).ToUpper();
        }

        private string GetStyleAbbreviation(List<LoadoutTag> tags)
        {
            if (tags == null || tags.Count == 0) return "STD";

            // Map first tag to abbreviation
            var firstTag = tags[0].tagName;
            return firstTag switch
            {
                "AA Build" => "AA",
                "Speed" => "SPD",
                "Armor" => "ARM",
                "Firepower" => "FP",
                "Balanced" => "BAL",
                "Budget" => "BUD",
                "Premium" => "PRE",
                _ => "STD"
            };
        }

        private string GenerateRandomCode(int length)
        {
            const string chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; // No 0,O,1,I
            var result = new char[length];
            for (int i = 0; i < length; i++)
            {
                result[i] = chars[UnityEngine.Random.Range(0, chars.Length)];
            }
            return new string(result);
        }

        /// <summary>
        /// Import preset from share code
        /// </summary>
        public async Task<LoadoutPreset> ImportFromShareCode(string shareCode)
        {
            // Lookup from cloud
            var preset = await FetchPresetByShareCode(shareCode);

            if (preset != null)
            {
                // Add to local cache
                if (!_presetCache.ContainsKey(preset.presetId))
                {
                    _localPresets.Add(preset);
                    _presetCache[preset.presetId] = preset;
                    SaveLocalPresets();
                }
            }

            return preset;
        }

        private async Task<LoadoutPreset> FetchPresetByShareCode(string shareCode)
        {
            // TODO: Implement PlayFab CloudScript call
            // For now, return null
            await Task.Yield();
            return null;
        }

        #endregion

        #region Community Library

        /// <summary>
        /// Browse community presets with filters
        /// </summary>
        public async Task<List<LoadoutPreset>> BrowseCommunityPresets(
            PresetSearchFilter filter)
        {
            // TODO: Implement PlayFab query
            await Task.Yield();
            return new List<LoadoutPreset>();
        }

        /// <summary>
        /// Rate a community preset
        /// </summary>
        public async Task RatePreset(string presetId, int stars)
        {
            stars = Mathf.Clamp(stars, 1, 5);

            // TODO: Implement PlayFab CloudScript call
            await Task.Yield();
        }

        private async Task UploadPresetToCloud(LoadoutPreset preset)
        {
            // TODO: Implement PlayFab CloudScript call
            await Task.Yield();
        }

        #endregion

        #region Local Storage

        private void LoadLocalPresets()
        {
            string json = PlayerPrefs.GetString("LoadoutPresets", "");
            if (!string.IsNullOrEmpty(json))
            {
                var data = JsonUtility.FromJson<LoadoutPresetCollection>(json);
                if (data != null)
                {
                    _localPresets = data.presets ?? new List<LoadoutPreset>();
                    foreach (var preset in _localPresets)
                    {
                        _presetCache[preset.presetId] = preset;
                    }
                }
            }
        }

        private void SaveLocalPresets()
        {
            var data = new LoadoutPresetCollection { presets = _localPresets };
            string json = JsonUtility.ToJson(data);
            PlayerPrefs.SetString("LoadoutPresets", json);
            PlayerPrefs.Save();
        }

        [Serializable]
        private class LoadoutPresetCollection
        {
            public List<LoadoutPreset> presets;
        }

        #endregion

        #region Queries

        public List<LoadoutPreset> GetLocalPresets()
        {
            return new List<LoadoutPreset>(_localPresets);
        }

        public List<LoadoutPreset> GetPresetsForShip(string shipId)
        {
            return _localPresets.FindAll(p => p.targetShipId == shipId);
        }

        public LoadoutPreset GetPresetById(string presetId)
        {
            return _presetCache.GetValueOrDefault(presetId);
        }

        public void DeletePreset(string presetId)
        {
            var preset = GetPresetById(presetId);
            if (preset != null)
            {
                _localPresets.Remove(preset);
                _presetCache.Remove(presetId);
                SaveLocalPresets();
                OnPresetDeleted?.Invoke(preset);
            }
        }

        #endregion
    }

    public class PresetApplicationResult
    {
        public bool Success;
        public LoadoutPreset Preset;
        public List<MissingModuleInfo> MissingModules = new();
        public int TotalCost;
        public string ErrorMessage;
    }

    public class MissingModuleInfo
    {
        public string ModuleId;
        public string ModuleName;
        public int Cost;
    }

    public class PresetSearchFilter
    {
        public string ShipClass;           // "Destroyer", "Battleship", etc.
        public int? MinTier;
        public int? MaxTier;
        public List<string> Tags;
        public float MinRating = 0f;
        public PresetSortOrder SortOrder = PresetSortOrder.MostPopular;
    }

    public enum PresetSortOrder
    {
        MostPopular,
        HighestRated,
        Newest,
        MostExpensive,
        Cheapest
    }
}
```

---

## 6.4 Loadout Presets UI Screen

```csharp
// Assets/Scripts/UI/Fitting/LoadoutPresetsScreen.cs
namespace WOS.UI.Fitting
{
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UI;
    using TMPro;
    using WOS.Loadouts;
    using WOS.ScriptableObjects.Ships;

    /// <summary>
    /// Screen 5: Loadout Presets
    /// Save, load, share complete ship configurations
    /// </summary>
    public class LoadoutPresetsScreen : MonoBehaviour
    {
        [Header("Tab Navigation")]
        [SerializeField] private Button myPresetsTab;
        [SerializeField] private Button communityTab;

        [Header("Preset List")]
        [SerializeField] private Transform presetListContainer;
        [SerializeField] private GameObject presetCardPrefab;
        [SerializeField] private ScrollRect presetScrollView;

        [Header("Preset Detail Panel")]
        [SerializeField] private GameObject detailPanel;
        [SerializeField] private TextMeshProUGUI detailNameText;
        [SerializeField] private TextMeshProUGUI detailDescriptionText;
        [SerializeField] private TextMeshProUGUI detailCreatorText;
        [SerializeField] private TextMeshProUGUI detailRatingText;
        [SerializeField] private Transform detailTagsContainer;
        [SerializeField] private Transform detailModuleList;

        [Header("Action Buttons")]
        [SerializeField] private Button applyButton;
        [SerializeField] private Button previewButton;
        [SerializeField] private Button shareButton;
        [SerializeField] private Button deleteButton;

        [Header("Save New Preset")]
        [SerializeField] private Button saveAsPresetButton;
        [SerializeField] private GameObject savePresetDialog;
        [SerializeField] private TMP_InputField presetNameInput;
        [SerializeField] private TMP_InputField descriptionInput;
        [SerializeField] private TMP_Dropdown visibilityDropdown;
        [SerializeField] private Transform tagTogglesContainer;

        [Header("Import/Export")]
        [SerializeField] private Button importCodeButton;
        [SerializeField] private TMP_InputField shareCodeInput;
        [SerializeField] private TextMeshProUGUI generatedCodeText;
        [SerializeField] private Button copyCodeButton;

        [Header("Community Filters")]
        [SerializeField] private GameObject communityFiltersPanel;
        [SerializeField] private TMP_Dropdown shipClassFilter;
        [SerializeField] private TMP_Dropdown tierFilter;
        [SerializeField] private TMP_Dropdown buildTypeFilter;
        [SerializeField] private TMP_Dropdown sortOrderDropdown;

        [Header("Current Ship Context")]
        [SerializeField] private ShipConfigurationSO currentShip;

        private LoadoutPresetManager _presetManager;
        private List<LoadoutPreset> _displayedPresets = new();
        private LoadoutPreset _selectedPreset;
        private bool _showingCommunity = false;

        private void Awake()
        {
            _presetManager = LoadoutPresetManager.Instance;

            // Tab buttons
            myPresetsTab.onClick.AddListener(ShowMyPresets);
            communityTab.onClick.AddListener(ShowCommunityPresets);

            // Action buttons
            applyButton.onClick.AddListener(OnApplyClicked);
            previewButton.onClick.AddListener(OnPreviewClicked);
            shareButton.onClick.AddListener(OnShareClicked);
            deleteButton.onClick.AddListener(OnDeleteClicked);
            saveAsPresetButton.onClick.AddListener(OpenSaveDialog);
            importCodeButton.onClick.AddListener(OnImportCode);
            copyCodeButton.onClick.AddListener(OnCopyCode);
        }

        private void OnEnable()
        {
            ShowMyPresets();
        }

        #region Tab Navigation

        private void ShowMyPresets()
        {
            _showingCommunity = false;
            communityFiltersPanel.SetActive(false);

            // Update tab visual state
            myPresetsTab.interactable = false;
            communityTab.interactable = true;

            // Load local presets for current ship
            var presets = _presetManager.GetPresetsForShip(currentShip.shipId);
            PopulatePresetList(presets);
        }

        private async void ShowCommunityPresets()
        {
            _showingCommunity = true;
            communityFiltersPanel.SetActive(true);

            // Update tab visual state
            myPresetsTab.interactable = true;
            communityTab.interactable = false;

            // Load community presets with current filters
            await RefreshCommunityPresets();
        }

        private async System.Threading.Tasks.Task RefreshCommunityPresets()
        {
            var filter = BuildSearchFilter();
            var presets = await _presetManager.BrowseCommunityPresets(filter);
            PopulatePresetList(presets);
        }

        private PresetSearchFilter BuildSearchFilter()
        {
            return new PresetSearchFilter
            {
                ShipClass = shipClassFilter.options[shipClassFilter.value].text,
                MinTier = GetTierFromFilter(tierFilter.value, true),
                MaxTier = GetTierFromFilter(tierFilter.value, false),
                SortOrder = (PresetSortOrder)sortOrderDropdown.value
            };
        }

        private int? GetTierFromFilter(int filterIndex, bool isMin)
        {
            return filterIndex switch
            {
                0 => null,        // "All Tiers"
                1 => isMin ? 1 : 3,   // "T1-T3"
                2 => isMin ? 4 : 6,   // "T4-T6"
                3 => isMin ? 7 : 10,  // "T7-T10"
                _ => null
            };
        }

        #endregion

        #region Preset List

        private void PopulatePresetList(List<LoadoutPreset> presets)
        {
            _displayedPresets = presets;

            // Clear existing cards
            foreach (Transform child in presetListContainer)
            {
                Destroy(child.gameObject);
            }

            // Create cards
            foreach (var preset in presets)
            {
                var cardObj = Instantiate(presetCardPrefab, presetListContainer);
                var card = cardObj.GetComponent<PresetCardUI>();
                if (card != null)
                {
                    card.Setup(preset, OnPresetSelected);
                }
            }

            // Clear selection if current not in list
            if (_selectedPreset != null && !presets.Contains(_selectedPreset))
            {
                ClearSelection();
            }
        }

        private void OnPresetSelected(LoadoutPreset preset)
        {
            _selectedPreset = preset;
            UpdateDetailPanel(preset);

            // Enable/disable buttons based on ownership
            bool isOwner = preset.creatorPlayerId ==
                (PlayFabInventoryService.Instance?.GetPlayerId() ?? "local");

            deleteButton.interactable = isOwner;
            shareButton.interactable = true;
            applyButton.interactable = true;
            previewButton.interactable = true;
        }

        private void ClearSelection()
        {
            _selectedPreset = null;
            detailPanel.SetActive(false);
        }

        #endregion

        #region Detail Panel

        private void UpdateDetailPanel(LoadoutPreset preset)
        {
            detailPanel.SetActive(true);

            detailNameText.text = preset.presetName;
            detailDescriptionText.text = preset.description ?? "";
            detailCreatorText.text = $"By: {preset.creatorDisplayName}";
            detailRatingText.text = $"⭐ {preset.rating.averageStars:F1} ({preset.rating.totalRatings} ratings)";

            // Show tags
            foreach (Transform child in detailTagsContainer)
            {
                Destroy(child.gameObject);
            }

            if (preset.tags != null)
            {
                foreach (var tag in preset.tags)
                {
                    // Create tag chip UI (simplified)
                    var tagObj = new GameObject("Tag");
                    tagObj.transform.SetParent(detailTagsContainer);
                    var text = tagObj.AddComponent<TextMeshProUGUI>();
                    text.text = $"[{tag.tagName}]";
                    text.fontSize = 12;
                }
            }

            // Update share code display
            generatedCodeText.text = preset.shareCode ?? "No code";
        }

        #endregion

        #region Actions

        private async void OnApplyClicked()
        {
            if (_selectedPreset == null) return;

            var result = await _presetManager.ApplyPreset(
                _selectedPreset,
                currentShip,
                ItemDatabaseSO.Instance);

            if (result.Success)
            {
                // Preset applied successfully
                await _presetManager.PurchaseAndApplyPreset(result);
                ShowApplySuccessMessage();
            }
            else if (result.MissingModules.Count > 0)
            {
                // Show purchase dialog
                ShowPurchaseDialog(result);
            }
            else
            {
                // Show error
                ShowErrorMessage(result.ErrorMessage);
            }
        }

        private void OnPreviewClicked()
        {
            if (_selectedPreset == null) return;

            // TODO: Open preview mode showing ship with preset applied
            Debug.Log($"Previewing preset: {_selectedPreset.presetName}");
        }

        private void OnShareClicked()
        {
            if (_selectedPreset == null) return;

            // Show share code prominently
            GUIUtility.systemCopyBuffer = _selectedPreset.shareCode;
            ShowMessage($"Share code copied: {_selectedPreset.shareCode}");
        }

        private void OnDeleteClicked()
        {
            if (_selectedPreset == null) return;

            // Confirm and delete
            ShowConfirmDialog(
                "Delete Preset",
                $"Are you sure you want to delete '{_selectedPreset.presetName}'?",
                () =>
                {
                    _presetManager.DeletePreset(_selectedPreset.presetId);
                    ShowMyPresets();
                });
        }

        private async void OnImportCode()
        {
            string code = shareCodeInput.text.Trim().ToUpper();
            if (string.IsNullOrEmpty(code))
            {
                ShowErrorMessage("Please enter a share code");
                return;
            }

            var preset = await _presetManager.ImportFromShareCode(code);
            if (preset != null)
            {
                ShowMessage($"Imported: {preset.presetName}");
                ShowMyPresets();
            }
            else
            {
                ShowErrorMessage("Share code not found");
            }
        }

        private void OnCopyCode()
        {
            if (_selectedPreset != null && !string.IsNullOrEmpty(_selectedPreset.shareCode))
            {
                GUIUtility.systemCopyBuffer = _selectedPreset.shareCode;
                ShowMessage("Code copied to clipboard");
            }
        }

        #endregion

        #region Save Dialog

        private void OpenSaveDialog()
        {
            savePresetDialog.SetActive(true);
            presetNameInput.text = "";
            descriptionInput.text = "";
            visibilityDropdown.value = 0; // Private by default
        }

        public async void OnSavePresetConfirm()
        {
            string name = presetNameInput.text.Trim();
            if (string.IsNullOrEmpty(name))
            {
                ShowErrorMessage("Please enter a preset name");
                return;
            }

            // Gather current configuration
            // (Would interface with ShipFittingManager)
            var installedModules = new List<InstalledModule>(); // TODO: Get from fitting manager
            var armorConfig = new ArmorZoneConfiguration();     // TODO: Get from fitting manager
            var visibility = (LoadoutVisibility)visibilityDropdown.value;
            var tags = GatherSelectedTags();

            var preset = await _presetManager.SavePreset(
                currentShip,
                installedModules,
                armorConfig,
                name,
                descriptionInput.text,
                visibility,
                tags);

            savePresetDialog.SetActive(false);
            ShowMessage($"Saved preset: {preset.presetName}");
            ShowMyPresets();
        }

        public void OnSavePresetCancel()
        {
            savePresetDialog.SetActive(false);
        }

        private List<LoadoutTag> GatherSelectedTags()
        {
            var tags = new List<LoadoutTag>();
            // TODO: Read from tag toggle UI
            return tags;
        }

        #endregion

        #region UI Helpers

        private void ShowMessage(string message)
        {
            Debug.Log(message);
            // TODO: Show toast notification
        }

        private void ShowErrorMessage(string message)
        {
            Debug.LogError(message);
            // TODO: Show error toast
        }

        private void ShowApplySuccessMessage()
        {
            ShowMessage("Preset applied successfully!");
        }

        private void ShowPurchaseDialog(PresetApplicationResult result)
        {
            // TODO: Show purchase confirmation dialog
            Debug.Log($"Missing {result.MissingModules.Count} modules, total cost: {result.TotalCost}");
        }

        private void ShowConfirmDialog(string title, string message, System.Action onConfirm)
        {
            // TODO: Show confirmation dialog
            onConfirm?.Invoke(); // For now, auto-confirm
        }

        #endregion
    }

    // Helper class to represent installed module
    public class InstalledModule
    {
        public string slotId;
        public ModuleDefinitionSO moduleDefinition;
        public WOS.Crew.CrewCard assignedCrew;
    }
}
```

---

## 6.5 Undo/Redo System

```csharp
// Assets/Scripts/UI/Fitting/UndoRedoManager.cs
namespace WOS.UI.Fitting
{
    using System;
    using System.Collections.Generic;
    using UnityEngine;

    /// <summary>
    /// Tracks all fitting changes for undo/redo
    /// Session-based, resets on save
    /// </summary>
    public class UndoRedoManager
    {
        private Stack<IFittingChange> _undoStack = new();
        private Stack<IFittingChange> _redoStack = new();

        public event Action OnHistoryChanged;

        public bool CanUndo => _undoStack.Count > 0;
        public bool CanRedo => _redoStack.Count > 0;

        public string LastActionDescription => CanUndo ? _undoStack.Peek().Description : "";
        public string NextRedoDescription => CanRedo ? _redoStack.Peek().Description : "";

        /// <summary>
        /// Record a new change (clears redo stack)
        /// </summary>
        public void RecordChange(IFittingChange change)
        {
            _undoStack.Push(change);
            _redoStack.Clear();
            OnHistoryChanged?.Invoke();
        }

        /// <summary>
        /// Undo last change
        /// </summary>
        public void Undo()
        {
            if (!CanUndo) return;

            var change = _undoStack.Pop();
            change.Undo();
            _redoStack.Push(change);
            OnHistoryChanged?.Invoke();
        }

        /// <summary>
        /// Redo last undone change
        /// </summary>
        public void Redo()
        {
            if (!CanRedo) return;

            var change = _redoStack.Pop();
            change.Redo();
            _undoStack.Push(change);
            OnHistoryChanged?.Invoke();
        }

        /// <summary>
        /// Clear all history (call on save)
        /// </summary>
        public void ClearHistory()
        {
            _undoStack.Clear();
            _redoStack.Clear();
            OnHistoryChanged?.Invoke();
        }

        public bool HasUnsavedChanges => _undoStack.Count > 0;
    }

    public interface IFittingChange
    {
        string Description { get; }
        void Undo();
        void Redo();
    }

    #region Change Types

    public class ModuleInstallChange : IFittingChange
    {
        private string _slotId;
        private ModuleDefinitionSO _newModule;
        private ModuleDefinitionSO _previousModule;
        private Action<string, ModuleDefinitionSO> _applyAction;

        public string Description => $"Installed {_newModule.moduleName}";

        public ModuleInstallChange(
            string slotId,
            ModuleDefinitionSO newModule,
            ModuleDefinitionSO previousModule,
            Action<string, ModuleDefinitionSO> applyAction)
        {
            _slotId = slotId;
            _newModule = newModule;
            _previousModule = previousModule;
            _applyAction = applyAction;
        }

        public void Undo() => _applyAction(_slotId, _previousModule);
        public void Redo() => _applyAction(_slotId, _newModule);
    }

    public class ModuleRemoveChange : IFittingChange
    {
        private string _slotId;
        private ModuleDefinitionSO _removedModule;
        private Action<string, ModuleDefinitionSO> _applyAction;

        public string Description => $"Removed {_removedModule.moduleName}";

        public ModuleRemoveChange(
            string slotId,
            ModuleDefinitionSO removedModule,
            Action<string, ModuleDefinitionSO> applyAction)
        {
            _slotId = slotId;
            _removedModule = removedModule;
            _applyAction = applyAction;
        }

        public void Undo() => _applyAction(_slotId, _removedModule);
        public void Redo() => _applyAction(_slotId, null);
    }

    public class ArmorChange : IFittingChange
    {
        private string _zoneName;
        private float _newThickness;
        private float _previousThickness;
        private Action<string, float> _applyAction;

        public string Description => $"Changed {_zoneName} armor to {_newThickness}\"";

        public ArmorChange(
            string zoneName,
            float newThickness,
            float previousThickness,
            Action<string, float> applyAction)
        {
            _zoneName = zoneName;
            _newThickness = newThickness;
            _previousThickness = previousThickness;
            _applyAction = applyAction;
        }

        public void Undo() => _applyAction(_zoneName, _previousThickness);
        public void Redo() => _applyAction(_zoneName, _newThickness);
    }

    public class CargoPlacementChange : IFittingChange
    {
        private string _itemId;
        private Vector2Int _newPosition;
        private Vector2Int _previousPosition;
        private bool _wasRotated;
        private bool _isRotated;
        private Action<string, Vector2Int, bool> _applyAction;

        public string Description => "Moved cargo item";

        public CargoPlacementChange(
            string itemId,
            Vector2Int newPosition,
            Vector2Int previousPosition,
            bool isRotated,
            bool wasRotated,
            Action<string, Vector2Int, bool> applyAction)
        {
            _itemId = itemId;
            _newPosition = newPosition;
            _previousPosition = previousPosition;
            _isRotated = isRotated;
            _wasRotated = wasRotated;
            _applyAction = applyAction;
        }

        public void Undo() => _applyAction(_itemId, _previousPosition, _wasRotated);
        public void Redo() => _applyAction(_itemId, _newPosition, _isRotated);
    }

    public class CrewAssignmentChange : IFittingChange
    {
        private string _slotId;
        private string _newCrewId;
        private string _previousCrewId;
        private Action<string, string> _applyAction;

        public string Description => $"Assigned crew to slot";

        public CrewAssignmentChange(
            string slotId,
            string newCrewId,
            string previousCrewId,
            Action<string, string> applyAction)
        {
            _slotId = slotId;
            _newCrewId = newCrewId;
            _previousCrewId = previousCrewId;
            _applyAction = applyAction;
        }

        public void Undo() => _applyAction(_slotId, _previousCrewId);
        public void Redo() => _applyAction(_slotId, _newCrewId);
    }

    #endregion
}
```

---

## 6.6 Keyboard Shortcuts Manager

```csharp
// Assets/Scripts/UI/Fitting/FittingKeyboardShortcuts.cs
namespace WOS.UI.Fitting
{
    using UnityEngine;
    using UnityEngine.InputSystem;

    /// <summary>
    /// GDD-defined keyboard shortcuts for fitting UI
    /// </summary>
    public class FittingKeyboardShortcuts : MonoBehaviour
    {
        [Header("References")]
        [SerializeField] private ShipFittingUIController fittingController;
        [SerializeField] private UndoRedoManager undoRedoManager;

        private InputAction _saveAction;
        private InputAction _undoAction;
        private InputAction _redoAction;
        private InputAction _tabAction;
        private InputAction _escapeAction;
        private InputAction _cycleForwardAction;
        private InputAction _cycleBackAction;
        private InputAction _deleteAction;
        private InputAction _crewAction;
        private InputAction _rotateAction;
        private InputAction _autoSortAction;
        private InputAction _screen1to5Actions;

        private void Awake()
        {
            SetupInputActions();
        }

        private void SetupInputActions()
        {
            // Global shortcuts
            _saveAction = new InputAction(binding: "<Keyboard>/s",
                modifiers: new[] { new InputBinding { path = "<Keyboard>/ctrl" } });
            _saveAction.performed += _ => OnSaveShortcut();

            _undoAction = new InputAction(binding: "<Keyboard>/z",
                modifiers: new[] { new InputBinding { path = "<Keyboard>/ctrl" } });
            _undoAction.performed += _ => OnUndoShortcut();

            _redoAction = new InputAction(binding: "<Keyboard>/y",
                modifiers: new[] { new InputBinding { path = "<Keyboard>/ctrl" } });
            _redoAction.performed += _ => OnRedoShortcut();

            _tabAction = new InputAction(binding: "<Keyboard>/tab");
            _tabAction.performed += _ => OnCycleScreen();

            _escapeAction = new InputAction(binding: "<Keyboard>/escape");
            _escapeAction.performed += _ => OnEscapeShortcut();

            // Screen navigation (1-5 keys)
            for (int i = 1; i <= 5; i++)
            {
                int screenIndex = i;
                var action = new InputAction(binding: $"<Keyboard>/{i}");
                action.performed += _ => OnScreenShortcut(screenIndex);
                action.Enable();
            }

            // Context shortcuts
            _cycleForwardAction = new InputAction(binding: "<Keyboard>/e");
            _cycleForwardAction.performed += _ => OnCycleSlotForward();

            _cycleBackAction = new InputAction(binding: "<Keyboard>/q");
            _cycleBackAction.performed += _ => OnCycleSlotBack();

            _deleteAction = new InputAction(binding: "<Keyboard>/delete");
            _deleteAction.performed += _ => OnDeleteSelected();

            _crewAction = new InputAction(binding: "<Keyboard>/c");
            _crewAction.performed += _ => OnOpenCrewAssignment();

            _rotateAction = new InputAction(binding: "<Keyboard>/r");
            _rotateAction.performed += _ => OnRotateItem();

            _autoSortAction = new InputAction(binding: "<Keyboard>/a",
                modifiers: new[] { new InputBinding { path = "<Keyboard>/ctrl" } });
            _autoSortAction.performed += _ => OnAutoSort();
        }

        private void OnEnable()
        {
            _saveAction?.Enable();
            _undoAction?.Enable();
            _redoAction?.Enable();
            _tabAction?.Enable();
            _escapeAction?.Enable();
            _cycleForwardAction?.Enable();
            _cycleBackAction?.Enable();
            _deleteAction?.Enable();
            _crewAction?.Enable();
            _rotateAction?.Enable();
            _autoSortAction?.Enable();
        }

        private void OnDisable()
        {
            _saveAction?.Disable();
            _undoAction?.Disable();
            _redoAction?.Disable();
            _tabAction?.Disable();
            _escapeAction?.Disable();
            _cycleForwardAction?.Disable();
            _cycleBackAction?.Disable();
            _deleteAction?.Disable();
            _crewAction?.Disable();
            _rotateAction?.Disable();
            _autoSortAction?.Disable();
        }

        #region Shortcut Handlers

        private void OnSaveShortcut()
        {
            fittingController?.SaveConfiguration();
        }

        private void OnUndoShortcut()
        {
            undoRedoManager?.Undo();
        }

        private void OnRedoShortcut()
        {
            undoRedoManager?.Redo();
        }

        private void OnCycleScreen()
        {
            // Tab cycles 1→2→3→4→5→1
            fittingController?.CycleToNextScreen();
        }

        private void OnScreenShortcut(int screenNumber)
        {
            // 1=Hardpoints, 2=Systems, 3=Armor, 4=Cargo, 5=Presets
            fittingController?.SwitchToScreen(screenNumber - 1);
        }

        private void OnEscapeShortcut()
        {
            if (undoRedoManager != null && undoRedoManager.HasUnsavedChanges)
            {
                fittingController?.ShowSaveConfirmDialog();
            }
            else
            {
                fittingController?.CloseFittingInterface();
            }
        }

        private void OnCycleSlotForward()
        {
            fittingController?.CycleSelectedSlot(1);
        }

        private void OnCycleSlotBack()
        {
            fittingController?.CycleSelectedSlot(-1);
        }

        private void OnDeleteSelected()
        {
            fittingController?.RemoveSelectedItem();
        }

        private void OnOpenCrewAssignment()
        {
            fittingController?.OpenCrewAssignmentPanel();
        }

        private void OnRotateItem()
        {
            fittingController?.RotateHeldItem();
        }

        private void OnAutoSort()
        {
            fittingController?.AutoSortCargo();
        }

        #endregion
    }
}
```

---

## 6.7 Accessibility - Colorblind Modes

```csharp
// Assets/Scripts/UI/Accessibility/ColorblindModeManager.cs
namespace WOS.UI.Accessibility
{
    using System;
    using UnityEngine;

    public class ColorblindModeManager : MonoBehaviour
    {
        public static ColorblindModeManager Instance { get; private set; }

        [SerializeField] private ColorblindMode currentMode = ColorblindMode.Standard;

        public ColorblindMode CurrentMode => currentMode;
        public event Action<ColorblindMode> OnModeChanged;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }
            Instance = this;
            DontDestroyOnLoad(gameObject);

            LoadSavedMode();
        }

        public void SetMode(ColorblindMode mode)
        {
            currentMode = mode;
            PlayerPrefs.SetInt("ColorblindMode", (int)mode);
            PlayerPrefs.Save();
            OnModeChanged?.Invoke(mode);
        }

        private void LoadSavedMode()
        {
            currentMode = (ColorblindMode)PlayerPrefs.GetInt("ColorblindMode", 0);
        }

        /// <summary>
        /// Get appropriate colors for current colorblind mode
        /// </summary>
        public ColorScheme GetColorScheme()
        {
            return currentMode switch
            {
                ColorblindMode.Standard => new ColorScheme
                {
                    Valid = new Color(0.2f, 0.8f, 0.2f),      // Green
                    Warning = new Color(0.8f, 0.8f, 0.2f),    // Yellow
                    Invalid = new Color(0.8f, 0.2f, 0.2f)     // Red
                },
                ColorblindMode.Deuteranopia => new ColorScheme
                {
                    Valid = new Color(0.2f, 0.4f, 0.8f),      // Blue
                    Warning = new Color(1.0f, 0.6f, 0.2f),    // Orange
                    Invalid = new Color(0.9f, 0.4f, 0.6f)     // Pink
                },
                ColorblindMode.Protanopia => new ColorScheme
                {
                    Valid = new Color(0.2f, 0.4f, 0.8f),      // Blue
                    Warning = new Color(0.8f, 0.8f, 0.2f),    // Yellow
                    Invalid = new Color(0.6f, 0.4f, 0.2f)     // Brown
                },
                ColorblindMode.Tritanopia => new ColorScheme
                {
                    Valid = new Color(0.2f, 0.8f, 0.2f),      // Green
                    Warning = new Color(0.6f, 0.3f, 0.8f),    // Purple
                    Invalid = new Color(0.8f, 0.2f, 0.2f)     // Red
                },
                _ => throw new ArgumentOutOfRangeException()
            };
        }
    }

    public enum ColorblindMode
    {
        Standard,       // Green/Yellow/Red
        Deuteranopia,   // Blue/Orange/Pink (Red-Green colorblindness)
        Protanopia,     // Blue/Yellow/Brown (Red-Blind)
        Tritanopia      // Green/Purple/Red (Blue-Yellow colorblindness)
    }

    public struct ColorScheme
    {
        public Color Valid;
        public Color Warning;
        public Color Invalid;
    }
}
```

---

## 6.8 Preset Card UI

```csharp
// Assets/Scripts/UI/Fitting/PresetCardUI.cs
namespace WOS.UI.Fitting
{
    using System;
    using UnityEngine;
    using UnityEngine.UI;
    using TMPro;
    using WOS.Loadouts;

    /// <summary>
    /// Visual representation of a loadout preset
    /// Matches GDD example card layout
    /// </summary>
    public class PresetCardUI : MonoBehaviour
    {
        [Header("Header")]
        [SerializeField] private TextMeshProUGUI presetNameText;
        [SerializeField] private TextMeshProUGUI creatorText;
        [SerializeField] private TextMeshProUGUI ratingText;
        [SerializeField] private Image shipThumbnail;

        [Header("Stats Summary")]
        [SerializeField] private TextMeshProUGUI turretSummary;
        [SerializeField] private TextMeshProUGUI engineSummary;
        [SerializeField] private TextMeshProUGUI armorSummary;
        [SerializeField] private TextMeshProUGUI supportSummary;

        [Header("Stat Bars")]
        [SerializeField] private Slider firepowerBar;
        [SerializeField] private Slider speedBar;
        [SerializeField] private Slider armorBar;
        [SerializeField] private Slider aaBar;

        [Header("Cost Info")]
        [SerializeField] private TextMeshProUGUI totalCostText;
        [SerializeField] private TextMeshProUGUI ownedModulesText;
        [SerializeField] private TextMeshProUGUI missingModulesText;

        [Header("Tags")]
        [SerializeField] private Transform tagsContainer;
        [SerializeField] private GameObject tagPrefab;

        [Header("Interaction")]
        [SerializeField] private Button cardButton;
        [SerializeField] private Image selectedHighlight;

        private LoadoutPreset _preset;
        private Action<LoadoutPreset> _onSelected;

        public void Setup(LoadoutPreset preset, Action<LoadoutPreset> onSelected)
        {
            _preset = preset;
            _onSelected = onSelected;

            // Header
            presetNameText.text = preset.presetName;
            creatorText.text = $"By: {preset.creatorDisplayName}";
            ratingText.text = FormatRating(preset.rating);

            // Stats (would calculate from slot assignments)
            // For now, show placeholder
            turretSummary.text = $"Turrets: {preset.slotAssignments?.Count ?? 0} modules";
            engineSummary.text = "Engines: Standard";
            armorSummary.text = $"Armor: {preset.armorConfig?.beltThicknessInches ?? 0}\" belt";
            supportSummary.text = "Support: Configured";

            // Tags
            ClearAndPopulateTags(preset.tags);

            // Interaction
            cardButton.onClick.RemoveAllListeners();
            cardButton.onClick.AddListener(OnCardClicked);

            selectedHighlight.enabled = false;
        }

        private string FormatRating(LoadoutRating rating)
        {
            if (rating == null || rating.totalRatings == 0)
                return "No ratings";

            string stars = "";
            int fullStars = Mathf.FloorToInt(rating.averageStars);
            for (int i = 0; i < fullStars; i++) stars += "⭐";
            return $"{stars} ({rating.totalRatings})";
        }

        private void ClearAndPopulateTags(System.Collections.Generic.List<LoadoutTag> tags)
        {
            foreach (Transform child in tagsContainer)
            {
                Destroy(child.gameObject);
            }

            if (tags == null) return;

            foreach (var tag in tags)
            {
                var tagObj = Instantiate(tagPrefab, tagsContainer);
                var text = tagObj.GetComponentInChildren<TextMeshProUGUI>();
                if (text != null)
                {
                    text.text = tag.tagName;
                }
            }
        }

        private void OnCardClicked()
        {
            _onSelected?.Invoke(_preset);
        }

        public void SetSelected(bool selected)
        {
            selectedHighlight.enabled = selected;
        }
    }
}
```

---

## 6.9 ShipDebugUIManager Overhaul

```csharp
// Assets/Scripts/UI/Fitting/ShipFittingUIController.cs
namespace WOS.UI.Fitting
{
    using System;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UI;
    using TMPro;
    using WOS.ScriptableObjects.Ships;
    using WOS.Loadouts;
    using WOS.Crew;

    /// <summary>
    /// Main controller for the Ship Fitting UI
    /// Replaces/upgrades ShipDebugUIManager
    /// Implements 5-screen GDD architecture
    /// </summary>
    public class ShipFittingUIController : MonoBehaviour
    {
        [Header("Screen References")]
        [SerializeField] private WeaponHardpointScreen weaponScreen;    // Screen 1
        [SerializeField] private ShipSystemsScreen systemsScreen;       // Screen 2
        [SerializeField] private ArmorConfigScreen armorScreen;         // Screen 3
        [SerializeField] private CargoGridScreen cargoScreen;           // Screen 4
        [SerializeField] private LoadoutPresetsScreen loadoutScreen;    // Screen 5

        [Header("Screen Navigation")]
        [SerializeField] private Button[] screenButtons;
        [SerializeField] private GameObject[] screens;
        [SerializeField] private int currentScreenIndex = 0;

        [Header("Common Bottom Panel")]
        [SerializeField] private CommonStatsPanel statsPanel;

        [Header("Action Bar")]
        [SerializeField] private Button undoButton;
        [SerializeField] private Button redoButton;
        [SerializeField] private Button saveButton;
        [SerializeField] private Button helpButton;
        [SerializeField] private TextMeshProUGUI lastActionText;

        [Header("Confirmation Dialogs")]
        [SerializeField] private GameObject saveConfirmDialog;
        [SerializeField] private GameObject discardConfirmDialog;

        [Header("Current Configuration")]
        [SerializeField] private ShipConfigurationSO currentShip;

        private UndoRedoManager _undoRedoManager;
        private LoadoutPresetManager _presetManager;
        private List<InstalledModule> _installedModules = new();

        public event Action OnConfigurationSaved;
        public event Action OnConfigurationClosed;

        private void Awake()
        {
            _undoRedoManager = new UndoRedoManager();
            _presetManager = LoadoutPresetManager.Instance;

            SetupScreenButtons();
            SetupActionBar();

            _undoRedoManager.OnHistoryChanged += UpdateUndoRedoButtons;
        }

        private void SetupScreenButtons()
        {
            for (int i = 0; i < screenButtons.Length; i++)
            {
                int index = i;
                screenButtons[i].onClick.AddListener(() => SwitchToScreen(index));
            }
        }

        private void SetupActionBar()
        {
            undoButton.onClick.AddListener(() => _undoRedoManager.Undo());
            redoButton.onClick.AddListener(() => _undoRedoManager.Redo());
            saveButton.onClick.AddListener(SaveConfiguration);

            UpdateUndoRedoButtons();
        }

        #region Screen Navigation

        public void SwitchToScreen(int screenIndex)
        {
            if (screenIndex < 0 || screenIndex >= screens.Length) return;

            // Hide all screens
            for (int i = 0; i < screens.Length; i++)
            {
                screens[i].SetActive(i == screenIndex);
                screenButtons[i].interactable = (i != screenIndex);
            }

            currentScreenIndex = screenIndex;
        }

        public void CycleToNextScreen()
        {
            int nextIndex = (currentScreenIndex + 1) % screens.Length;
            SwitchToScreen(nextIndex);
        }

        public void CycleSelectedSlot(int direction)
        {
            // Forward to active screen
            switch (currentScreenIndex)
            {
                case 0: weaponScreen?.CycleSlot(direction); break;
                case 1: systemsScreen?.CycleSlot(direction); break;
            }
        }

        #endregion

        #region Configuration Actions

        public void SaveConfiguration()
        {
            // Save to backend
            Debug.Log("Saving configuration...");

            _undoRedoManager.ClearHistory();
            OnConfigurationSaved?.Invoke();
        }

        public void CloseFittingInterface()
        {
            gameObject.SetActive(false);
            OnConfigurationClosed?.Invoke();
        }

        public void ShowSaveConfirmDialog()
        {
            saveConfirmDialog.SetActive(true);
        }

        public void OnSaveAndClose()
        {
            saveConfirmDialog.SetActive(false);
            SaveConfiguration();
            CloseFittingInterface();
        }

        public void OnDiscardChanges()
        {
            saveConfirmDialog.SetActive(false);
            _undoRedoManager.ClearHistory();
            CloseFittingInterface();
        }

        public void OnCancelClose()
        {
            saveConfirmDialog.SetActive(false);
        }

        #endregion

        #region Context Actions

        public void RemoveSelectedItem()
        {
            switch (currentScreenIndex)
            {
                case 0: weaponScreen?.RemoveSelectedModule(); break;
                case 1: systemsScreen?.RemoveSelectedModule(); break;
                case 3: cargoScreen?.RemoveSelectedItem(); break;
            }
        }

        public void OpenCrewAssignmentPanel()
        {
            switch (currentScreenIndex)
            {
                case 0: weaponScreen?.OpenCrewPanel(); break;
                case 1: systemsScreen?.OpenCrewPanel(); break;
            }
        }

        public void RotateHeldItem()
        {
            switch (currentScreenIndex)
            {
                case 3: cargoScreen?.RotateHeldItem(); break;
            }
        }

        public void AutoSortCargo()
        {
            cargoScreen?.AutoSort();
        }

        #endregion

        #region Undo/Redo

        private void UpdateUndoRedoButtons()
        {
            undoButton.interactable = _undoRedoManager.CanUndo;
            redoButton.interactable = _undoRedoManager.CanRedo;

            lastActionText.text = _undoRedoManager.LastActionDescription;
        }

        public void RecordChange(IFittingChange change)
        {
            _undoRedoManager.RecordChange(change);
        }

        #endregion

        #region Public API

        public void Open(ShipConfigurationSO shipConfig)
        {
            currentShip = shipConfig;
            gameObject.SetActive(true);

            // Initialize all screens with ship data
            weaponScreen?.Initialize(shipConfig);
            systemsScreen?.Initialize(shipConfig);
            armorScreen?.Initialize(shipConfig);
            cargoScreen?.Initialize(shipConfig);
            loadoutScreen?.Initialize(shipConfig);

            // Update stats panel
            statsPanel?.Refresh();

            // Start on screen 1
            SwitchToScreen(0);
        }

        public ShipConfigurationSO GetCurrentShip() => currentShip;

        #endregion
    }
}
```

---

## Phase 6 Validation Checklist

```
[ ] LoadoutPreset data structure with all GDD fields
[ ] Save preset captures slots, armor, cargo layout
[ ] Load preset checks module ownership
[ ] Missing modules purchase dialog functional
[ ] Share code generation: SHIP-STYLE-XXXXXX format
[ ] Import from share code works
[ ] Community preset browsing with filters
[ ] Rating system (1-5 stars, upvote/downvote)
[ ] Undo/Redo stack with change tracking
[ ] All change types tracked (module, armor, cargo, crew)
[ ] Keyboard shortcuts implemented per GDD
[ ] Ctrl+S saves, Ctrl+Z undoes, 1-5 switch screens
[ ] Q/E cycle slots, R rotates, Delete removes
[ ] Colorblind modes: Standard, Deuteranopia, Protanopia, Tritanopia
[ ] Icons supplement color (checkmark, warning, error)
[ ] 5-screen architecture functional
[ ] ShipFittingUIController replaces ShipDebugUIManager
[ ] Save confirmation dialog on close with changes
[ ] Help button context-sensitive
```

---

*Phase 6 Loadouts & Polish - Version 3.0*
