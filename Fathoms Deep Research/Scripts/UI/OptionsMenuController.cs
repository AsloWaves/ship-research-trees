using UnityEngine;
using UnityEngine.UI;
using TMPro;

namespace WOS.UI
{
    /// <summary>
    /// Options menu controller (placeholder for future implementation)
    /// Will handle audio, graphics, key bindings, etc.
    /// </summary>
    public class OptionsMenuController : MonoBehaviour
    {
        [Header("Audio Settings (Future)")]
        [Tooltip("Master volume slider")]
        public Slider masterVolumeSlider;

        [Tooltip("Music volume slider")]
        public Slider musicVolumeSlider;

        [Tooltip("SFX volume slider")]
        public Slider sfxVolumeSlider;

        [Header("Graphics Settings (Future)")]
        [Tooltip("Quality dropdown")]
        public TMP_Dropdown qualityDropdown;

        [Tooltip("Fullscreen toggle")]
        public Toggle fullscreenToggle;

        [Header("Status")]
        [Tooltip("Status text for options")]
        public TextMeshProUGUI statusText;

        private void Start()
        {
            LoadSettings();
            UpdateStatus("Options menu - Coming soon!");
        }

        /// <summary>
        /// Load saved settings from PlayerPrefs
        /// </summary>
        private void LoadSettings()
        {
            // TODO: Implement settings loading
            Debug.Log("[OptionsMenu] Settings loaded (placeholder)");
        }

        /// <summary>
        /// Save settings to PlayerPrefs
        /// </summary>
        public void SaveSettings()
        {
            // TODO: Implement settings saving
            UpdateStatus("Settings saved!");
            Debug.Log("[OptionsMenu] Settings saved (placeholder)");
        }

        #region Button Events

        /// <summary>
        /// Return to main menu
        /// Called by "Back" button
        /// </summary>
        public void OnBackButtonClicked()
        {
            if (MenuManager.Instance != null)
            {
                MenuManager.Instance.ShowMainMenu();
            }
            else
            {
                Debug.LogWarning("[OptionsMenu] MenuManager not found!");
            }
        }

        #endregion

        #region Helper Methods

        private void UpdateStatus(string message)
        {
            if (statusText != null)
            {
                statusText.text = message;
            }

            Debug.Log($"[OptionsMenu] {message}");
        }

        #endregion
    }
}
