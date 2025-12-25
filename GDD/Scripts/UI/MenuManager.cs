using UnityEngine;
using System.Collections.Generic;

namespace WOS.UI
{
    /// <summary>
    /// Manages menu panel transitions (MainMenu, ConnectionMenu, OptionsMenu)
    /// Simple panel switching system for MUIP layouts with keyboard navigation support
    /// </summary>
    public class MenuManager : MonoBehaviour
    {
        // Menu history stack for keyboard navigation "back" functionality
        private Stack<MenuPanel> menuHistory = new Stack<MenuPanel>();
        private MenuPanel currentPanel;
        [Header("Menu Panels")]
        [Tooltip("Main menu panel with Start, Options, Exit buttons")]
        public GameObject mainMenuPanel;

        [Tooltip("Login panel with username/password input")]
        public GameObject loginPanel;

        [Tooltip("Connection menu panel with Host, Join, Back buttons")]
        public GameObject connectionMenuPanel;

        [Tooltip("Host panel with hosting interface")]
        public GameObject hostPanel;

        [Tooltip("Join panel with IP input and Connect button")]
        public GameObject joinPanel;

        [Tooltip("Options menu panel (future implementation)")]
        public GameObject optionsMenuPanel;

        [Header("Main Menu UI")]
        [Tooltip("Main menu status text (MUIP Input Field set to read-only)")]
        public TMPro.TMP_InputField mainMenuStatusText;

        [Header("Configuration")]
        [Tooltip("Panel to show on startup")]
        public MenuPanel startingPanel = MenuPanel.MainMenu;

        // Singleton for easy access
        public static MenuManager Instance { get; private set; }

        private void Awake()
        {
            // Singleton pattern
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }
            Instance = this;

            ValidatePanels();

            // Force all panels to be hidden initially (in case they're active in scene)
            HideAllPanels();
        }

        private void Start()
        {
            // Clear menu history on fresh scene load
            menuHistory.Clear();
            currentPanel = default(MenuPanel);

            // Force hide all panels again (in case they activated themselves)
            HideAllPanels();

            // Show starting panel after all components have initialized
            ShowPanel(startingPanel);

            // Update main menu status text (MUIP Input Field)
            if (mainMenuStatusText != null)
            {
                mainMenuStatusText.text = "Fathoms Deep - Naval MMO";
                if (mainMenuStatusText.textComponent != null)
                {
                    mainMenuStatusText.textComponent.color = UnityEngine.Color.white;
                }
            }
        }

        /// <summary>
        /// Show specific menu panel, hide all others
        /// </summary>
        public void ShowPanel(MenuPanel panel)
        {
            // Add current panel to history stack (if not same panel)
            if (currentPanel != panel && currentPanel != default(MenuPanel))
            {
                menuHistory.Push(currentPanel);
            }

            currentPanel = panel;

            // Hide all panels first
            HideAllPanels();

            GameObject activatedPanel = null;

            // Show requested panel
            switch (panel)
            {
                case MenuPanel.MainMenu:
                    if (mainMenuPanel != null)
                    {
                        mainMenuPanel.SetActive(true);
                        activatedPanel = mainMenuPanel;
                    }
                    break;

                case MenuPanel.LoginPanel:
                    if (loginPanel != null)
                    {
                        loginPanel.SetActive(true);
                        activatedPanel = loginPanel;
                    }
                    break;

                case MenuPanel.ConnectionMenu:
                    if (connectionMenuPanel != null)
                    {
                        connectionMenuPanel.SetActive(true);
                        activatedPanel = connectionMenuPanel;
                    }
                    break;

                case MenuPanel.HostMenu:
                    if (hostPanel != null)
                    {
                        hostPanel.SetActive(true);
                        activatedPanel = hostPanel;
                    }
                    break;

                case MenuPanel.JoinMenu:
                    if (joinPanel != null)
                    {
                        joinPanel.SetActive(true);
                        activatedPanel = joinPanel;
                    }
                    break;

                case MenuPanel.OptionsMenu:
                    if (optionsMenuPanel != null)
                    {
                        optionsMenuPanel.SetActive(true);
                        activatedPanel = optionsMenuPanel;
                    }
                    break;
            }

            // Refresh keyboard navigation for newly activated panel
            if (activatedPanel != null)
            {
                MenuKeyboardNavigation keyboardNav = activatedPanel.GetComponent<MenuKeyboardNavigation>();
                if (keyboardNav != null)
                {
                    keyboardNav.RefreshNavigableElements();
                }
            }

            Debug.Log($"[MenuManager] Showing panel: {panel}");
        }

        /// <summary>
        /// Hide all menu panels
        /// </summary>
        private void HideAllPanels()
        {
            if (mainMenuPanel != null) mainMenuPanel.SetActive(false);
            if (loginPanel != null) loginPanel.SetActive(false);
            if (connectionMenuPanel != null) connectionMenuPanel.SetActive(false);
            if (hostPanel != null) hostPanel.SetActive(false);
            if (joinPanel != null) joinPanel.SetActive(false);
            if (optionsMenuPanel != null) optionsMenuPanel.SetActive(false);
        }

        /// <summary>
        /// Return to main menu from any panel
        /// </summary>
        public void ShowMainMenu()
        {
            ShowPanel(MenuPanel.MainMenu);
        }

        /// <summary>
        /// Show login panel
        /// </summary>
        public void ShowLoginMenu()
        {
            ShowPanel(MenuPanel.LoginPanel);
        }

        /// <summary>
        /// Show connection menu (Host/Join buttons)
        /// </summary>
        public void ShowConnectionMenu()
        {
            ShowPanel(MenuPanel.ConnectionMenu);
        }

        /// <summary>
        /// Show host panel
        /// </summary>
        public void ShowHostMenu()
        {
            ShowPanel(MenuPanel.HostMenu);
        }

        /// <summary>
        /// Show join panel
        /// </summary>
        public void ShowJoinMenu()
        {
            ShowPanel(MenuPanel.JoinMenu);
        }

        /// <summary>
        /// Show options menu
        /// </summary>
        public void ShowOptionsMenu()
        {
            ShowPanel(MenuPanel.OptionsMenu);
        }

        private void ValidatePanels()
        {
            if (mainMenuPanel == null)
                Debug.LogWarning("[MenuManager] Main Menu Panel not assigned!");

            if (loginPanel == null)
                Debug.LogWarning("[MenuManager] Login Panel not assigned!");

            if (connectionMenuPanel == null)
                Debug.LogWarning("[MenuManager] Connection Menu Panel not assigned!");

            if (hostPanel == null)
                Debug.LogWarning("[MenuManager] Host Panel not assigned!");

            if (joinPanel == null)
                Debug.LogWarning("[MenuManager] Join Panel not assigned!");

            if (optionsMenuPanel == null)
                Debug.LogWarning("[MenuManager] Options Menu Panel not assigned! (Optional for now)");
        }

        #region Public API for Button OnClick Events

        /// <summary>
        /// Called by Main Menu "Start" button
        /// Goes to Login menu first (Phase 3: Authentication)
        /// </summary>
        public void OnStartButtonClicked()
        {
            ShowLoginMenu();
        }

        /// <summary>
        /// Called by Main Menu "Options" button
        /// </summary>
        public void OnOptionsButtonClicked()
        {
            ShowOptionsMenu();
        }

        /// <summary>
        /// Called by Main Menu "Exit" button
        /// </summary>
        public void OnExitButtonClicked()
        {
            if (mainMenuStatusText != null)
            {
                mainMenuStatusText.text = "Exiting...";
            }
            QuitGame();
        }

        /// <summary>
        /// Called by any "Back" button or Escape key to return to previous menu
        /// Uses menu history stack for smart navigation
        /// </summary>
        public void OnBackButtonClicked()
        {
            // If we have history, go to previous panel
            if (menuHistory.Count > 0)
            {
                MenuPanel previousPanel = menuHistory.Pop();

                // Clear history to avoid adding current panel back
                MenuPanel temp = currentPanel;
                currentPanel = default(MenuPanel);

                ShowPanel(previousPanel);

                Debug.Log($"[MenuManager] Going back to: {previousPanel}");
            }
            else
            {
                // No history, go to main menu as fallback
                ShowMainMenu();
            }
        }

        #endregion

        #region Game Control

        /// <summary>
        /// Quit the application
        /// </summary>
        private void QuitGame()
        {
            Debug.Log("🚪 Quitting game...");

#if UNITY_EDITOR
            UnityEditor.EditorApplication.isPlaying = false;
#else
            Application.Quit();
#endif
        }

        #endregion
    }

    /// <summary>
    /// Available menu panels
    /// </summary>
    public enum MenuPanel
    {
        MainMenu,
        LoginPanel,
        ConnectionMenu,
        HostMenu,
        JoinMenu,
        OptionsMenu
    }
}
