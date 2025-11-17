using UnityEngine;
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
    /// Manages 6 separate debug panels displaying ship information across the bottom of the screen.
    /// Replaces monolithic ShipDebugUI with individual TextMeshProUGUI fields for better layout control.
    /// Always visible (no toggle), updates at 10Hz, local player only in multiplayer.
    /// </summary>
    public class ShipDebugUIManager : MonoBehaviour
    {
        #region Panel References

        [Header("Panel 1 - VESSEL & SPECS")]
        [Tooltip("Ship name (e.g., 'USS Constitution')")]
        public TextMeshProUGUI vesselName;

        [Tooltip("Ship class (e.g., 'Frigate')")]
        public TextMeshProUGUI vesselClass;

        [Tooltip("Ship length in meters")]
        public TextMeshProUGUI vesselLength;

        [Tooltip("Ship displacement in tons")]
        public TextMeshProUGUI vesselDisplacement;

        [Tooltip("Maximum rudder angle (±degrees)")]
        public TextMeshProUGUI vesselMaxRudder;

        [Header("Panel 2 - PROPULSION & OCEAN")]
        [Tooltip("Current speed in knots")]
        public TextMeshProUGUI propCurrentSpeed;

        [Tooltip("Target speed in knots")]
        public TextMeshProUGUI propTargetSpeed;

        [Tooltip("Throttle setting (e.g., 'FULL AHEAD')")]
        public TextMeshProUGUI propThrottle;

        [Tooltip("Maximum speed in knots")]
        public TextMeshProUGUI propMaxSpeed;

        [Tooltip("Ocean depth in meters")]
        public TextMeshProUGUI oceanDepth;

        [Tooltip("Ocean tile type")]
        public TextMeshProUGUI oceanTileType;

        [Tooltip("Ocean zone name")]
        public TextMeshProUGUI oceanZone;

        [Header("Panel 3 - NAVIGATION")]
        [Tooltip("Current bearing in degrees")]
        public TextMeshProUGUI navBearing;

        [Tooltip("Rate of turn in degrees per second")]
        public TextMeshProUGUI navRateOfTurn;

        [Tooltip("Current rudder angle in degrees")]
        public TextMeshProUGUI navRudderAngle;

        [Tooltip("Navigation mode (AUTO/MANUAL)")]
        public TextMeshProUGUI navMode;

        [Header("Panel 4 - NEAREST PORT")]
        [Tooltip("Name of nearest port")]
        public TextMeshProUGUI portName;

        [Tooltip("Bearing to port in degrees")]
        public TextMeshProUGUI portBearing;

        [Tooltip("Distance to port in nautical miles")]
        public TextMeshProUGUI portDistance;

        [Header("Panel 5 - NETWORK")]
        [Tooltip("Connection status (Connected/Disconnected)")]
        public TextMeshProUGUI netStatus;

        [Tooltip("Network mode (Host/Client/Server)")]
        public TextMeshProUGUI netMode;

        [Tooltip("Ping in milliseconds")]
        public TextMeshProUGUI netPing;

        [Tooltip("Round-trip time in milliseconds")]
        public TextMeshProUGUI netRTT;

        [Tooltip("Network quality indicator")]
        public TextMeshProUGUI netQuality;

        [Header("Panel 6 - RESERVED")]
        // Empty for now - user will add fields later

        #endregion

        #region Configuration

        [Header("Update Settings")]
        [Tooltip("How often to update the display (times per second)")]
        [SerializeField] private float updateRate = 10f;

        [Tooltip("Number of decimal places for speed values")]
        [SerializeField] private int speedPrecision = 1;

        [Tooltip("Number of decimal places for angle values")]
        [SerializeField] private int anglePrecision = 1;

        [Header("Ship Reference")]
        [Tooltip("Reference to the ship controller (auto-found if not assigned)")]
        [SerializeField] private MonoBehaviour shipController; // Can be SimpleNavalController or NetworkedNavalController

        [Header("Ocean Biome Reference")]
        [Tooltip("Reference to ocean chunk manager for depth info (auto-found if not assigned)")]
        [SerializeField] private OceanChunkManager oceanManager;

        #endregion

        // [Rest of ShipDebugUIManager implementation - 650+ lines]
    }
}
