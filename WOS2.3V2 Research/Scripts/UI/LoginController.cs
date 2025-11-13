using System;
using System.Collections;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using TMPro;
using Michsky.MUIP;
using WOS.Networking.Data;

namespace WOS.UI
{
    /// <summary>
    /// Login screen controller for WOS2.3
    /// Handles authentication with backend API and JWT token storage.
    /// Supports MUIP (Modern UI Pack) components and standard Unity UI.
    /// </summary>
    public class LoginController : MonoBehaviour
    {
        #region Serialized Fields

        [Header("MUIP Input Fields")]
        [Tooltip("Username input field (MUIP FieldManager or TMP_InputField)")]
        [SerializeField] private TMP_InputField usernameField;

        [Tooltip("Password input field (MUIP FieldManager or TMP_InputField - set Content Type to Password)")]
        [SerializeField] private TMP_InputField passwordField;

        [Header("MUIP Buttons")]
        [Tooltip("Login button (MUIP ButtonManager)")]
        [SerializeField] private ButtonManager loginButton;

        [Tooltip("Register button (MUIP ButtonManager)")]
        [SerializeField] private ButtonManager registerButton;

        [Tooltip("Back to main menu button (MUIP ButtonManager)")]
        [SerializeField] private ButtonManager backButton;

        [Header("Status Display")]
        [Tooltip("Status text for messages and errors (MUIP Input Field set to read-only)")]
        [SerializeField] private TMP_InputField statusText;

        [Header("Backend Configuration")]
        [Tooltip("Backend API base URL")]
        [SerializeField] private string backendApiUrl = "https://wos-edgegap-proxy.onrender.com";

        [Tooltip("Request timeout in seconds")]
        [SerializeField] private float requestTimeout = 10f;

        [Header("Status Colors")]
        [SerializeField] private Color infoColor = new Color(1f, 0.65f, 0f); // Orange
        [SerializeField] private Color successColor = Color.green;
        [SerializeField] private Color errorColor = Color.red;

        #endregion

        #region Private Fields

        private bool isProcessing = false;

        #endregion

        #region Unity Lifecycle

        private void Start()
        {
            ValidateReferences();

            // Always show fresh login form (no returning user detection)
            ShowLoginForm();
        }

        #endregion

        #region Public Methods (UI Callbacks)

        /// <summary>
        /// Called by Login button onClick event.
        /// </summary>
        public void OnLoginButtonClicked()
        {
            if (isProcessing)
            {
                Debug.LogWarning("[LoginController] Login already in progress");
                return;
            }

            string username = usernameField?.text ?? "";
            string password = passwordField?.text ?? "";

            // Validate inputs
            if (!AuthDataHelper.ValidateUsername(username, out string usernameError))
            {
                UpdateStatus(usernameError, StatusType.Error);
                return;
            }

            if (!AuthDataHelper.ValidatePassword(password, out string passwordError))
            {
                UpdateStatus(passwordError, StatusType.Error);
                return;
            }

            // Start login process
            StartCoroutine(LoginCoroutine(username, password));
        }

        /// <summary>
        /// Called by Register button onClick event.
        /// </summary>
        public void OnRegisterButtonClicked()
        {
            if (isProcessing)
            {
                Debug.LogWarning("[LoginController] Registration already in progress");
                return;
            }

            string username = usernameField?.text ?? "";
            string password = passwordField?.text ?? "";

            // Validate inputs
            if (!AuthDataHelper.ValidateUsername(username, out string usernameError))
            {
                UpdateStatus(usernameError, StatusType.Error);
                return;
            }

            if (!AuthDataHelper.ValidatePassword(password, out string passwordError))
            {
                UpdateStatus(passwordError, StatusType.Error);
                return;
            }

            // Start registration process
            StartCoroutine(RegisterCoroutine(username, password));
        }

        /// <summary>
        /// Called by Back button onClick event.
        /// Returns to main menu.
        /// </summary>
        public void OnBackButtonClicked()
        {
            if (MenuManager.Instance != null)
            {
                MenuManager.Instance.ShowMainMenu();
            }
            else
            {
                Debug.LogError("[LoginController] MenuManager not found!");
            }
        }

        #endregion

        #region Private Methods - API Calls

        /// <summary>
        /// Login coroutine - authenticates with backend API.
        /// </summary>
        private IEnumerator LoginCoroutine(string username, string password)
        {
            isProcessing = true;
            SetButtonsInteractable(false);
            UpdateStatus("Logging in...", StatusType.Info);

            string url = $"{backendApiUrl}/api/auth/login";
            LoginRequest requestData = new LoginRequest
            {
                Username = username,
                Password = password
            };

            string jsonData = JsonUtility.ToJson(requestData);
            Debug.Log($"[LoginController] 🔍 LOGIN REQUEST JSON: {jsonData}");
            bool loginSuccess = false;

            using (UnityWebRequest request = new UnityWebRequest(url, "POST"))
            {
                byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonData);
                request.uploadHandler = new UploadHandlerRaw(bodyRaw);
                request.downloadHandler = new DownloadHandlerBuffer();
                request.SetRequestHeader("Content-Type", "application/json");
                request.timeout = (int)requestTimeout;

                yield return request.SendWebRequest();

                isProcessing = false;

                if (request.result == UnityWebRequest.Result.Success)
                {
                    try
                    {
                        AuthResponse response = JsonUtility.FromJson<AuthResponse>(request.downloadHandler.text);

                        if (response.success && !string.IsNullOrEmpty(response.token))
                        {
                            // Store authentication data
                            AuthDataHelper.StoreAuthData(response.token, response.playerId, response.username);

                            UpdateStatus("Login successful!", StatusType.Success);
                            Debug.Log($"[LoginController] Login successful for: {response.username}");

                            loginSuccess = true;
                        }
                        else
                        {
                            string errorMsg = string.IsNullOrEmpty(response.message)
                                ? "Login failed. Please try again."
                                : response.message;
                            UpdateStatus(errorMsg, StatusType.Error);
                            SetButtonsInteractable(true);

                            // Clear password field for security
                            if (passwordField != null)
                            {
                                passwordField.text = "";
                            }
                        }
                    }
                    catch (Exception e)
                    {
                        Debug.LogError($"[LoginController] Failed to parse login response: {e.Message}");
                        UpdateStatus("Invalid server response. Please try again.", StatusType.Error);
                        SetButtonsInteractable(true);
                    }
                }
                else
                {
                    // Log the actual error response from backend
                    string errorResponse = request.downloadHandler?.text ?? "No response";
                    Debug.LogError($"[LoginController] 🔍 LOGIN ERROR RESPONSE: {errorResponse}");

                    HandleNetworkError(request);
                    SetButtonsInteractable(true);

                    // Clear password field for security
                    if (passwordField != null)
                    {
                        passwordField.text = "";
                    }
                }
            }

            // Handle navigation after try-catch (outside the using block)
            if (loginSuccess)
            {
                // Brief pause to show success message
                yield return new WaitForSeconds(1f);
                NavigateToJoinMenu();
            }
        }

        /// <summary>
        /// Register coroutine - creates new account with backend API.
        /// </summary>
        private IEnumerator RegisterCoroutine(string username, string password)
        {
            isProcessing = true;
            SetButtonsInteractable(false);
            UpdateStatus("Creating account...", StatusType.Info);

            string url = $"{backendApiUrl}/api/auth/register";

            // Manually construct JSON to omit Email field when empty
            // Unity's JsonUtility converts null to "" which fails backend validation
            string jsonData = $"{{\"Username\":\"{username}\",\"Password\":\"{password}\"}}";
            Debug.Log($"[LoginController] 🔍 REGISTER REQUEST JSON: {jsonData}");
            bool registerSuccess = false;

            using (UnityWebRequest request = new UnityWebRequest(url, "POST"))
            {
                byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonData);
                request.uploadHandler = new UploadHandlerRaw(bodyRaw);
                request.downloadHandler = new DownloadHandlerBuffer();
                request.SetRequestHeader("Content-Type", "application/json");
                request.timeout = (int)requestTimeout;

                yield return request.SendWebRequest();

                isProcessing = false;

                if (request.result == UnityWebRequest.Result.Success)
                {
                    try
                    {
                        string responseText = request.downloadHandler.text;
                        Debug.Log($"[LoginController] 🔍 REGISTER SUCCESS RESPONSE: {responseText}");

                        AuthResponse response = JsonUtility.FromJson<AuthResponse>(responseText);

                        if (response.success && !string.IsNullOrEmpty(response.token))
                        {
                            // Store authentication data
                            AuthDataHelper.StoreAuthData(response.token, response.playerId, response.username);

                            UpdateStatus("Registration successful!", StatusType.Success);
                            Debug.Log($"[LoginController] Registration successful for: {response.username}");

                            registerSuccess = true;
                        }
                        else
                        {
                            string errorMsg = string.IsNullOrEmpty(response.message)
                                ? "Registration failed. Please try again."
                                : response.message;
                            UpdateStatus(errorMsg, StatusType.Error);
                            SetButtonsInteractable(true);
                        }
                    }
                    catch (Exception e)
                    {
                        Debug.LogError($"[LoginController] Failed to parse registration response: {e.Message}");
                        UpdateStatus("Invalid server response. Please try again.", StatusType.Error);
                        SetButtonsInteractable(true);
                    }
                }
                else
                {
                    // Log the actual error response from backend
                    string errorResponse = request.downloadHandler?.text ?? "No response";
                    Debug.LogError($"[LoginController] 🔍 REGISTER ERROR RESPONSE: {errorResponse}");

                    HandleNetworkError(request);
                    SetButtonsInteractable(true);
                }
            }

            // Handle navigation after try-catch (outside the using block)
            if (registerSuccess)
            {
                // Brief pause to show success message
                yield return new WaitForSeconds(1f);
                NavigateToJoinMenu();
            }
        }

        #endregion

        #region Private Methods - UI Management

        /// <summary>
        /// Update status text with message and color coding.
        /// </summary>
        private void UpdateStatus(string message, StatusType type)
        {
            if (statusText != null)
            {
                statusText.text = message;

                // Set color on the text component (TMP_InputField uses textComponent for visual styling)
                if (statusText.textComponent != null)
                {
                    statusText.textComponent.color = type switch
                    {
                        StatusType.Info => infoColor,
                        StatusType.Success => successColor,
                        StatusType.Error => errorColor,
                        _ => Color.white
                    };
                }
            }

            Debug.Log($"[LoginController] {type}: {message}");
        }

        /// <summary>
        /// Set all buttons interactable state (for preventing spam during API calls).
        /// </summary>
        private void SetButtonsInteractable(bool interactable)
        {
            if (loginButton != null)
                loginButton.isInteractable = interactable;

            if (registerButton != null)
                registerButton.isInteractable = interactable;

            if (backButton != null)
                backButton.isInteractable = interactable;
        }

        /// <summary>
        /// Handle network errors with user-friendly messages.
        /// </summary>
        private void HandleNetworkError(UnityWebRequest request)
        {
            string errorMessage;

            if (request.result == UnityWebRequest.Result.ConnectionError)
            {
                errorMessage = "Unable to connect to server. Please check your internet connection.";
            }
            else if (request.result == UnityWebRequest.Result.ProtocolError)
            {
                long statusCode = request.responseCode;

                errorMessage = statusCode switch
                {
                    401 => "Invalid username or password.",
                    409 => "Username already exists. Please choose another.",
                    500 => "Server error. Please try again later.",
                    _ => $"Server error ({statusCode}). Please try again."
                };
            }
            else
            {
                errorMessage = "Connection timed out. Please try again.";
            }

            UpdateStatus(errorMessage, StatusType.Error);
            Debug.LogWarning($"[LoginController] Network error: {request.error} (Code: {request.responseCode})");
        }

        /// <summary>
        /// Navigate to Join Menu after successful authentication.
        /// </summary>
        private void NavigateToJoinMenu()
        {
            if (MenuManager.Instance != null)
            {
                MenuManager.Instance.ShowJoinMenu();
            }
            else
            {
                Debug.LogError("[LoginController] MenuManager not found!");
            }
        }

        /// <summary>
        /// Show fresh login form (always starts clean).
        /// </summary>
        private void ShowLoginForm()
        {
            // Clear input fields
            if (usernameField != null)
            {
                usernameField.text = "";
            }

            if (passwordField != null)
            {
                passwordField.text = "";
            }

            UpdateStatus("Please login to continue", StatusType.Info);
            SetButtonsInteractable(true);
        }

        /// <summary>
        /// Validate component references.
        /// </summary>
        private void ValidateReferences()
        {
            if (usernameField == null)
                Debug.LogWarning("[LoginController] Username field not assigned!");

            if (passwordField == null)
                Debug.LogWarning("[LoginController] Password field not assigned!");

            if (loginButton == null)
                Debug.LogWarning("[LoginController] Login button not assigned!");

            if (registerButton == null)
                Debug.LogWarning("[LoginController] Register button not assigned!");

            if (statusText == null)
                Debug.LogWarning("[LoginController] Status text field not assigned! (Use MUIP Input Field set to read-only)");
        }

        #endregion

        #region Enums

        private enum StatusType
        {
            Info,
            Success,
            Error
        }

        #endregion
    }
}
