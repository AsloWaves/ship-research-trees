using System;
using System.Collections.Generic;
using System.Linq;
using Mirror;
using UnityEngine;

namespace WOS.Networking
{
    /// <summary>
    /// Edgegap bootstrap script for WOS2.3 Naval MMO
    /// Validates server configuration and port mappings for Edgegap deployment
    ///
    /// IMPORTANT: This is a standalone validation script that does NOT require
    /// the Edgegap plugin classes. It works in both Editor and Runtime.
    ///
    /// This script is OPTIONAL - the server will work without it.
    /// It's provided for configuration validation and debugging.
    ///
    /// Requirements:
    /// 1. Attach to GameObject in first scene (MainMenu)
    /// 2. Edgegap port mapping: 7777 TCP (Telepathy default)
    /// 3. NetworkManager must have networkAddress = "localhost" or "0.0.0.0"
    ///
    /// Validation:
    /// - Checks Mirror transport configuration
    /// - Verifies NetworkManager address is set correctly
    /// - Logs warnings if configuration issues detected
    /// </summary>
    public class WOSEdgegapBootstrap : MonoBehaviour
    {
        [Header("WOS2.3 Configuration")]
        [Tooltip("Expected server port (should match Edgegap port mapping)")]
        public ushort expectedPort = 7777;

        [Tooltip("Expected transport protocol (UDP for KCP, TCP for Telepathy)")]
        public string expectedProtocol = "UDP";

        [Header("Debug")]
        [Tooltip("Enable verbose logging for debugging")]
        public bool verboseLogging = true;

        private void Awake()
        {
            Log("🌊 WOSEdgegapBootstrap initialized");
            ValidateServerConfiguration();
        }

        // [Rest of implementation - see GitHub repository for full 250+ line file]
    }
}
