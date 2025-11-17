using UnityEngine;
using TMPro;
using Michsky.MUIP;

namespace WOS.UI
{
    /// <summary>
    /// Manages the F1 controls help panel with configurable keybindings.
    /// Displays all game controls in a multi-line TMP text field.
    /// Supports both direct TMP assignment and MUIP CustomInputField components.
    /// </summary>
    public class ControlsHelpManager : MonoBehaviour
    {
        [Header("UI References")]
        [Tooltip("The panel GameObject containing the controls text")]
        public GameObject controlsPanel;

        [Header("Text Component (Choose ONE)")]
        [Tooltip("Option 1: Direct TextMeshProUGUI reference")]
        public TextMeshProUGUI controlsTextField;

        [Tooltip("Option 2: MUIP CustomInputField (auto-extracts TMP component)")]
        public CustomInputField muipInputField;

        [Tooltip("Option 3: TMP_InputField (auto-extracts text component)")]
        public TMP_InputField tmpInputField;

        // Internal reference to the actual TMP component being used
        private TMP_Text activeTextField;

        [Header("Toggle Settings")]
        [Tooltip("Key to toggle the controls panel")]
        public KeyCode toggleKey = KeyCode.F1;

        [Tooltip("Start with panel visible?")]
        public bool startVisible = false;

        [Header("Ship Movement Controls")]
        public ControlBinding steerLeft = new ControlBinding("A / Left Arrow", "Steer left (rudder port)");
        public ControlBinding steerRight = new ControlBinding("D / Right Arrow", "Steer right (rudder starboard)");
        public ControlBinding throttleUp = new ControlBinding("W", "Increase throttle");
        public ControlBinding throttleDown = new ControlBinding("S", "Decrease throttle");
        public ControlBinding emergencyStop = new ControlBinding("SPACE", "Emergency stop (full stop)");

        [Header("Navigation Controls")]
        public ControlBinding setWaypoint = new ControlBinding("Right Mouse Click", "Set navigation waypoint");
        public ControlBinding toggleAutopilot = new ControlBinding("Z", "Toggle autopilot");
        public ControlBinding clearWaypoints = new ControlBinding("X", "Clear all waypoints");
        public ControlBinding interact = new ControlBinding("E (hold)", "Interact with ports/objects");

        [Header("Camera Controls")]
        public ControlBinding zoomIn = new ControlBinding("Mouse Wheel Up", "Zoom in");
        public ControlBinding zoomOut = new ControlBinding("Mouse Wheel Down", "Zoom out");
        public ControlBinding panCamera = new ControlBinding("Middle Mouse + Drag", "Pan camera");

        [Header("UI Controls")]
        public ControlBinding openMenu = new ControlBinding("ESC", "Open/close menu");
        public ControlBinding openInventory = new ControlBinding("I", "Open inventory");
        public ControlBinding toggleHelp = new ControlBinding("F1", "Toggle this help panel");

        private bool isPanelVisible;

        // [Rest of ControlsHelpManager implementation - 250+ lines]
    }

    /// <summary>
    /// Serializable class representing a single control binding
    /// </summary>
    [System.Serializable]
    public class ControlBinding
    {
        [Tooltip("The key(s) to press")]
        public string key;

        [Tooltip("What this control does")]
        public string description;

        public ControlBinding(string key, string description)
        {
            this.key = key;
            this.description = description;
        }
    }
}
