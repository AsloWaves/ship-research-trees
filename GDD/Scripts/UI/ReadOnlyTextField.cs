using UnityEngine;
using TMPro;

namespace WOS.UI
{
    /// <summary>
    /// Makes TMP_InputField or TextMeshProUGUI components read-only (non-editable).
    /// Useful for status text, labels, or display-only fields.
    /// </summary>
    public class ReadOnlyTextField : MonoBehaviour
    {
        [Header("Read-Only Settings")]
        [Tooltip("Make the field read-only on Awake")]
        [SerializeField] private bool readOnlyOnAwake = true;

        [Tooltip("Disable raycast target to prevent interaction (recommended)")]
        [SerializeField] private bool disableRaycastTarget = true;

        private TMP_InputField inputField;
        private TextMeshProUGUI textComponent;

        private void Awake()
        {
            // Check for TMP_InputField first
            inputField = GetComponent<TMP_InputField>();

            // If no InputField, check for TextMeshProUGUI
            if (inputField == null)
            {
                textComponent = GetComponent<TextMeshProUGUI>();
            }

            // Validate that we found at least one component
            if (inputField == null && textComponent == null)
            {
                Debug.LogWarning($"[ReadOnlyTextField] No TMP_InputField or TextMeshProUGUI found on {gameObject.name}");
                return;
            }

            if (readOnlyOnAwake)
            {
                SetReadOnly(true);
            }
        }

        /// <summary>
        /// Set the component to read-only or editable
        /// </summary>
        public void SetReadOnly(bool readOnly)
        {
            // Handle TMP_InputField
            if (inputField != null)
            {
                inputField.interactable = !readOnly;

                if (readOnly)
                {
                    inputField.DeactivateInputField();
                }

                if (disableRaycastTarget)
                {
                    // Disable raycast on the input field's text component
                    if (inputField.textComponent != null)
                    {
                        inputField.textComponent.raycastTarget = !readOnly;
                    }
                }
            }

            // Handle TextMeshProUGUI
            if (textComponent != null)
            {
                // TextMeshProUGUI is already non-editable, just disable interaction
                if (disableRaycastTarget)
                {
                    textComponent.raycastTarget = !readOnly;
                }
            }
        }

        /// <summary>
        /// Set the text content
        /// </summary>
        public void SetText(string text)
        {
            if (inputField != null)
            {
                inputField.text = text;
            }
            else if (textComponent != null)
            {
                textComponent.text = text;
            }
        }

        /// <summary>
        /// Get the text content
        /// </summary>
        public string GetText()
        {
            if (inputField != null)
            {
                return inputField.text;
            }
            else if (textComponent != null)
            {
                return textComponent.text;
            }

            return string.Empty;
        }
    }
}
