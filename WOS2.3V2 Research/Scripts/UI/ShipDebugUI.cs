using UnityEngine;
using UnityEngine.UI;
using TMPro;
using Unity.Mathematics;
using WOS.Player;
using WOS.Debugging;
using WOS.Environment;
using WOS.ScriptableObjects;
using Mirror;

namespace WOS.UI
{
    /// <summary>
    /// Real-time debug UI panel for displaying ship information and telemetry.
    /// Designed for use with MUIP (Multi-line UI Panel) components.
    /// </summary>
    public class ShipDebugUI : MonoBehaviour
    {
        [Header("UI Components")]
        [Tooltip("TextMeshPro component for displaying ship information (Primary - MUIP compatible)")]
        [SerializeField] private TextMeshProUGUI shipInfoText;

        [Tooltip("Alternative UI Text component if not using TextMeshPro")]
        [SerializeField] private Text legacyInfoText;

        [Tooltip("MUIP InputField component for multi-line display (if using MUIP package)")]
        [SerializeField] private TMP_InputField muipInputField;

        [Header("Update Settings")]
        [Tooltip("How often to update the display (times per second)")]
        [SerializeField] private float updateRate = 10f;

        [Tooltip("Number of decimal places for speed values")]
        [SerializeField] private int speedPrecision = 1;

        [Tooltip("Number of decimal places for angle values")]
        [SerializeField] private int anglePrecision = 1;

        [Header("MUIP Settings")]
        [Tooltip("Use MUIP InputField instead of regular text component")]
        [SerializeField] private bool useMuipInputField = false;

        [Tooltip("Make MUIP field read-only (recommended for display)")]
        [SerializeField] private bool muipReadOnly = true;

        [Tooltip("MUIP line spacing for better readability")]
        [SerializeField] private float muipLineSpacing = 1.2f;

        [Header("Input Controls")]
        [Tooltip("Enable F3 key to toggle debug panel visibility")]
        [SerializeField] private bool enableToggleKey = true;

        [Header("Ship Reference")]
        [Tooltip("Reference to the ship controller (auto-found if not assigned)")]
        [SerializeField] private MonoBehaviour shipController; // Can be SimpleNavalController or NetworkedNavalController

        [Header("Ocean Biome Reference")]
        [Tooltip("Reference to ocean chunk manager for depth info (auto-found if not assigned)")]
        [SerializeField] private OceanChunkManager oceanManager;

        // Update timing
        private float lastUpdateTime;
        private float updateInterval;

        // Cached values for rate calculations
        private float lastBearing;
        private float lastUpdateTimeForRates;
        private float rateOfTurn; // degrees per second

        // UI Text reference (either TMPro or legacy)
        private Component activeTextComponent;

        // Initialization state
        private bool isInitialized = false;
        private float initializationStartTime;
        private const float INITIALIZATION_TIMEOUT = 30f; // Wait up to 30 seconds for player to spawn

        // [Rest of ShipDebugUI implementation - 700+ lines]
    }
}
