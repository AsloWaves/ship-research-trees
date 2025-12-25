using UnityEngine;
using UnityEngine.SceneManagement;
using Mirror;
using Michsky.MUIP;

namespace WOS.UI
{
    /// <summary>
    /// In-game pause/ESC menu controller for WOS Naval MMO
    /// Handles menu toggling, network disconnect, and game exit
    /// Note: Does NOT pause game time in multiplayer (other players continue playing)
    /// </summary>
    public class InGameMenuController : MonoBehaviour
    {
        [Header("Menu Panels")]
        [Tooltip("The main in-game menu panel (should be hidden by default)")]
        public GameObject menuPanel;

        [Tooltip("The settings panel (optional, should be hidden by default)")]
        public GameObject settingsPanel;

        [Tooltip("The quit confirmation panel (should be hidden by default)")]
        public GameObject quitConfirmationPanel;

        [Header("MUIP Buttons")]
        [Tooltip("Resume button - closes menu and returns to gameplay")]
        public ButtonManager resumeButton;

        [Tooltip("Settings button - opens settings menu (optional)")]
        public ButtonManager settingsButton;

        [Tooltip("Exit to Main Menu button - disconnects and loads MainMenu scene")]
        public ButtonManager exitToMenuButton;

        [Tooltip("Quit Game button - closes application")]
        public ButtonManager quitButton;

        [Header("Settings Panel Buttons")]
        [Tooltip("Back button on settings panel - returns to main menu")]
        public ButtonManager settingsBackButton;

        [Header("Quit Confirmation Buttons")]
        [Tooltip("Yes button on quit confirmation panel - confirms quit")]
        public ButtonManager quitYesButton;

        [Tooltip("No button on quit confirmation panel - cancels quit")]
        public ButtonManager quitNoButton;

        [Header("Configuration")]
        [Tooltip("Scene to load when exiting to main menu")]
        public string mainMenuSceneName = "MainMenu";

        [Tooltip("Lock cursor during gameplay")]
        public bool lockCursorInGame = true;

        [Tooltip("Show cursor when menu is open")]
        public bool showCursorInMenu = true;

        private bool isMenuOpen = false;
        private NetworkManager networkManager;

        // [Rest of InGameMenuController implementation - 400+ lines]
    }
}
