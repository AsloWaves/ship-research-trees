using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using TMPro;
using Mirror;
using WOS.Networking;
using WOS.Networking.Data;
using WOS.Networking.Messages;
using System;
using System.Collections;
using System.Collections.Generic;
using Michsky.MUIP;

namespace WOS.UI
{
    /// <summary>
    /// Handles Join panel - connects to remote server using IP address
    /// Includes server status checking, auto-refresh, and secure server browser integration.
    ///
    /// SECURITY: Uses ServerBrowserManager to fetch servers from YOUR backend API.
    /// Backend keeps Edgegap API token secure (never exposed to clients).
    /// </summary>
    public class JoinMenuController : MonoBehaviour
    {
        [Header("UI References")]
        [Tooltip("Status text showing server status and connection progress")]
        public TextMeshProUGUI serverStatusText;

        [Tooltip("MUIP Connect button to enable/disable based on server status")]
        public ButtonManager connectButton;

        [Tooltip("MUIP Back button to return to main menu")]
        public ButtonManager backButton;

        [Header("Server Browser (Secure)")]
        [Tooltip("ServerBrowserManager that fetches servers from YOUR backend (not Edgegap directly)")]
        public ServerBrowserManager serverBrowser;

        [Tooltip("Auto-select best server on start")]
        public bool autoSelectBestServer = true;

        [Header("Configuration")]
        [Tooltip("Server configuration (auto-populated from server browser or fallback)")]
        public ServerConfig serverConfig;

        [Tooltip("Scene to load after connecting (usually Main scene)")]
        public string gameSceneName = "Main";

        [Tooltip("How often to check server status (seconds)")]
        public float statusCheckInterval = 30f;

        [Tooltip("Timeout for server status check (seconds)")]
        public float statusCheckTimeout = 5f;

        [Tooltip("Port for HTTP health endpoint (must match server configuration)")]
        public int healthCheckPort = 30407;  // Edgegap external health port (maps to internal 8080)

        private NetworkManager networkManager;
        private NetworkAddressManager addressManager;
        private ServerStatus currentServerStatus = ServerStatus.Checking;
        private Coroutine statusCheckCoroutine;
        private bool isConnecting = false;
        private bool runtimeTextCreated = false;

        private void Start()
        {
            Debug.Log("[JoinMenu] ========== START INITIALIZING ==========");

            InitializeComponents();

            // Log current state before auto-detection
            Debug.Log($"[JoinMenu] serverStatusText before auto-detect: {(serverStatusText == null ? "NULL" : serverStatusText.gameObject.name)}");
            Debug.Log($"[JoinMenu] connectButton before auto-detect: {(connectButton == null ? "NULL" : connectButton.gameObject.name)}");
            Debug.Log($"[JoinMenu] backButton before auto-detect: {(backButton == null ? "NULL" : backButton.gameObject.name)}");

            // Auto-detect UI components if not assigned
            AutoDetectUIComponents();

            // Log current state after auto-detection
            Debug.Log($"[JoinMenu] serverStatusText after auto-detect: {(serverStatusText == null ? "NULL" : serverStatusText.gameObject.name)}");
            Debug.Log($"[JoinMenu] connectButton after auto-detect: {(connectButton == null ? "NULL" : connectButton.gameObject.name)}");
            Debug.Log($"[JoinMenu] backButton after auto-detect: {(backButton == null ? "NULL" : backButton.gameObject.name)}");

            // Validate UI references after auto-detection
            if (serverStatusText == null)
            {
                Debug.LogError("[JoinMenu] ⚠️ Server Status Text could not be found! Please assign manually.");

                // List all TextMeshProUGUI components found
                TextMeshProUGUI[] allTexts = GetComponentsInChildren<TextMeshProUGUI>(true);
                Debug.LogError($"[JoinMenu] Found {allTexts.Length} TextMeshProUGUI components in children:");
                foreach (var text in allTexts)
                {
                    Debug.LogError($"[JoinMenu]   - {text.gameObject.name} (active: {text.gameObject.activeInHierarchy})");
                }
            }
            if (connectButton == null)
            {
                Debug.LogError("[JoinMenu] ⚠️ Connect Button could not be found! Please assign manually.");

                // List all ButtonManager components found
                ButtonManager[] allButtons = GetComponentsInChildren<ButtonManager>(true);
                Debug.LogError($"[JoinMenu] Found {allButtons.Length} ButtonManager components in children:");
                foreach (var btn in allButtons)
                {
                    Debug.LogError($"[JoinMenu]   - {btn.gameObject.name} (active: {btn.gameObject.activeInHierarchy})");
                }
            }
            if (backButton == null)
            {
                Debug.LogWarning("[JoinMenu] ⚠️ Back Button could not be found! Please assign manually.");
            }

            // SECURE SERVER BROWSER INTEGRATION
            InitializeServerBrowser();

            // Start server status checking
            UpdateStatus("Checking server status...");
            StartStatusChecking();

            Debug.Log("[JoinMenu] ========== INITIALIZATION COMPLETE ==========");
        }

        // [Rest of the 1,000+ line JoinMenuController code truncated for space]
        // Full implementation available in GitHub repository
    }

    /// <summary>
    /// Server status states
    /// </summary>
    public enum ServerStatus
    {
        Checking,   // Currently checking server status
        Up,         // Server is online and accepting connections
        Down        // Server is offline or not responding
    }
}
