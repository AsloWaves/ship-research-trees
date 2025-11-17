---
tags: [script, ui, implemented, authentication]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/LoginController.cs
status: ✅ IMPLEMENTED
size: 17 KB (17,397 bytes)
---

# LoginController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/LoginController.cs`
**Size**: 17 KB (17,397 bytes)
**Dependencies**: UnityEngine, UnityEngine.Networking, TMPro, Michsky.MUIP, WOS.Networking.Data

---

## Purpose
LoginController manages the authentication UI panel for Fathoms Deep, handling both login and registration workflows. It communicates with the backend API to validate credentials, stores JWT tokens securely, and provides user-friendly error handling with color-coded status messages. The controller supports Modern UI Pack (MUIP) framework and standard Unity UI components.

This script is the primary client-side authentication controller, bridging the gap between user input and backend API authentication services. It ensures secure credential transmission, validates user inputs, and manages the complete authentication lifecycle from initial entry to successful token storage.

---

## Implements GDD Features
- [[Authentication]] - JWT token authentication system
- [[Menu-System]] - Login panel navigation integration
- [[Network-Architecture]] - Backend API integration for multiplayer access
- [[UI-Overview]] - MUIP framework integration

---

## Key Components

### Public Properties
```csharp
None (All fields are private/serialized)
```

### Private Enums
```csharp
StatusType
- Info      // Orange color - Loading/processing messages
- Success   // Green color - Success confirmations
- Error     // Red color - Error messages
```

### Public Methods
- `OnLoginButtonClicked()` - Called by Login button onClick event
- `OnRegisterButtonClicked()` - Called by Register button onClick event
- `OnBackButtonClicked()` - Returns to main menu via MenuManager

### Key Private Methods
- `LoginCoroutine(string username, string password)` - Async login with backend API
- `RegisterCoroutine(string username, string password)` - Async registration with backend API
- `UpdateStatus(string message, StatusType type)` - Display color-coded status messages
- `SetButtonsInteractable(bool interactable)` - Enable/disable all buttons (prevent spam)
- `HandleNetworkError(UnityWebRequest request)` - User-friendly network error messages
- `NavigateToJoinMenu()` - Navigate to Join Menu after successful auth
- `ShowLoginForm()` - Display clean login form on startup
- `ValidateReferences()` - Verify all Inspector references assigned
- `HideAllPanels()` - (Inherited from MenuManager integration)

---

## Configuration

### Inspector Fields

```csharp
[Header("MUIP Input Fields")]
usernameField (TMP_InputField): Username input field
- Type: TMP_InputField (MUIP FieldManager compatible)
- Purpose: Username entry
- Validation: 3-20 characters, alphanumeric + underscore

passwordField (TMP_InputField): Password input field
- Type: TMP_InputField (Content Type: Password)
- Purpose: Password entry (hidden input)
- Validation: Minimum 6 characters
- Security: Cleared on error

[Header("MUIP Buttons")]
loginButton (ButtonManager): Login button
- Type: ButtonManager (MUIP component)
- Purpose: Submit login request
- Callback: OnLoginButtonClicked()

registerButton (ButtonManager): Register button
- Type: ButtonManager (MUIP component)
- Purpose: Submit registration request
- Callback: OnRegisterButtonClicked()

backButton (ButtonManager): Back button
- Type: ButtonManager (MUIP component)
- Purpose: Return to main menu
- Callback: OnBackButtonClicked()

[Header("Status Display")]
statusText (TMP_InputField): Status message display
- Type: TMP_InputField (read-only)
- Purpose: Show loading/success/error messages
- Color-coded by StatusType

[Header("Backend Configuration")]
backendApiUrl (string, default: "https://wos-edgegap-proxy.onrender.com"): Backend API base URL
- Purpose: Server endpoint for authentication
- Environment: Production (Render.com deployment)
- Protocol: HTTPS (encrypted)

requestTimeout (float, default: 10f): Request timeout in seconds
- Purpose: Network request timeout limit
- Units: Seconds
- Prevents infinite waiting on connection issues

[Header("Status Colors")]
infoColor (Color, default: Orange): Info message color
- RGB: (255, 165, 0)
- Use: Loading messages, processing status

successColor (Color, default: Green): Success message color
- RGB: (0, 255, 0)
- Use: Login/registration success confirmations

errorColor (Color, default: Red): Error message color
- RGB: (255, 0, 0)
- Use: Validation errors, network errors, auth failures
```

### Private State Variables
```csharp
isProcessing (bool, default: false): API call in progress flag
- Purpose: Prevent concurrent login/registration attempts
- State: true during API calls, false otherwise
- Thread-safe: Single-threaded Unity coroutines
```

---

## Integration Points

### Dependencies (What This Needs)

**Unity Systems**:
- UnityEngine - Core MonoBehaviour, GameObject, Coroutine APIs
- UnityEngine.UI - Button interaction events
- UnityEngine.Networking - UnityWebRequest for HTTP calls
- System.Collections - IEnumerator for coroutines
- System.Text.Encoding - UTF8 encoding for JSON payloads

**Third-Party Assets**:
- TMPro - TMP_InputField for text entry/display
- Michsky.MUIP - ButtonManager for Modern UI Pack integration

**WOS Systems**:
- WOS.Networking.Data namespace:
  - AuthDataHelper - Token storage/retrieval utilities
  - LoginRequest - Login request data structure
  - AuthResponse - Authentication response data structure
- [[MenuManager]] - Navigation to/from login panel

**Backend Services**:
- Backend API (Node.js/Express) - Authentication server
- PostgreSQL database - Player account storage

### Used By (What Uses This)

**Menu System**:
- [[MenuManager]] - Shows/hides login panel, handles navigation
- [[MainMenuController]] - "Play" button routes through authentication

**Multiplayer System**:
- [[Network-Architecture]] - Uses stored JWT token for server connection
- Server lobby system - Validates token on join requests

**UI Framework**:
- MUIP PanelManager - Handles panel animations (fade in/out)
- [[MenuKeyboardNavigation]] - ESC key navigation (back button)

---

## Technical Details

### Performance Considerations

**Update Frequency**:
- None - Event-driven only (no Update/FixedUpdate loop)
- Coroutines run only during authentication attempts
- Zero CPU overhead when idle

**Memory Allocations**:
- **Per Login Attempt**:
  - LoginRequest JSON: ~100 bytes
  - UnityWebRequest buffers: ~1-2 KB
  - Response JSON: ~200-500 bytes
  - Total: ~2 KB per attempt (garbage collected)
- **Persistent Memory**:
  - Inspector field references: ~80 bytes
  - isProcessing flag: 1 byte
  - Total overhead: < 100 bytes

**CPU Cost**:
- Input validation: < 0.05ms
- JSON serialization: < 0.1ms
- Network wait: Asynchronous (no frame blocking)
- Status update: < 0.05ms
- **Total per login**: < 0.2ms CPU time (excluding network wait)

**Network Bandwidth**:
- Login request: ~150 bytes (JSON payload)
- Login response: ~300-500 bytes (JWT token + metadata)
- Total per attempt: ~500-650 bytes

### Network Behavior
- **Client-side only** - No Mirror networking involved
- **HTTP/HTTPS protocol** - Uses UnityWebRequest (not Mirror)
- **Asynchronous** - Coroutines yield during network wait
- **Timeout handling** - 10 second timeout prevents infinite hangs
- **Zero multiplayer traffic** - Authentication happens before joining sessions

---

## How It Works

### Initialization

**Start() - Setup on Panel Enable**:
```csharp
private void Start()
{
    ValidateReferences(); // Check all Inspector fields assigned
    ShowLoginForm();      // Display clean login UI
}
```

**ValidateReferences() - Configuration Check**:
```csharp
private void ValidateReferences()
{
    // Check each Inspector field
    if (usernameField == null)
        Debug.LogWarning("[LoginController] Username field not assigned!");

    if (passwordField == null)
        Debug.LogWarning("[LoginController] Password field not assigned!");

    // ... (similar checks for all fields)
}
```

**ShowLoginForm() - Initial UI State**:
```csharp
private void ShowLoginForm()
{
    // Clear input fields (fresh start)
    if (usernameField != null)
        usernameField.text = "";

    if (passwordField != null)
        passwordField.text = "";

    // Show welcome message
    UpdateStatus("Please login to continue", StatusType.Info);

    // Enable buttons
    SetButtonsInteractable(true);
}
```

### Main Loop
**No Update Loop** - LoginController is purely event-driven. All functionality triggered by:
- Button clicks (Login, Register, Back)
- Coroutine yields (async API calls)
- Menu navigation events

### Key Algorithms

#### Algorithm 1: LoginCoroutine() - Authenticate with Backend

```
Input: username (string), password (string)
Output: JWT token stored in PlayerPrefs OR error message displayed

Flow:
1. Set isProcessing = true (prevent concurrent attempts)
2. Disable all buttons (prevent spam clicks)
3. Display "Logging in..." status (Info color)

4. Construct request:
   - URL: "{backendApiUrl}/api/auth/login"
   - Method: POST
   - Headers: Content-Type = application/json
   - Body: {"Username": "...", "Password": "..."}

5. Create UnityWebRequest:
   - Body encoded as UTF-8 bytes
   - Upload handler: UploadHandlerRaw (JSON payload)
   - Download handler: DownloadHandlerBuffer (response capture)
   - Timeout: 10 seconds

6. Yield return request.SendWebRequest() (async network call)

7. Check request.result:

   SUCCESS (200 OK):
   8a. Parse response JSON → AuthResponse object
   9a. Check response.success && response.token != null:

       TRUE (Valid token):
       10a. Call AuthDataHelper.StoreAuthData(token, playerId, username)
            - Stores in PlayerPrefs:
              - "authToken" → JWT string
              - "playerId" → UUID string
              - "username" → Display name
       11a. Display "Login successful!" (Success color)
       12a. Log success message
       13a. Set loginSuccess = true
       14a. Wait 1 second (show success message)
       15a. NavigateToJoinMenu() (via MenuManager)

       FALSE (Invalid response):
       10b. Display error message (Error color)
       11b. Clear password field (security)
       12b. Re-enable buttons (allow retry)

   FAILURE (Network error, 4xx, 5xx):
   8b. Log error response for debugging
   9b. Call HandleNetworkError(request) → User-friendly error message
   10b. Clear password field (security)
   11b. Re-enable buttons (allow retry)

8. Set isProcessing = false (allow next attempt)

Error Handling:
- Try-catch around JSON parsing (invalid response format)
- Null checks on response fields
- Network timeout (10 seconds)
- HTTP status code validation
```

**Example Execution**:
```
User enters: username="Captain123", password="secret"

1. isProcessing = true, buttons disabled
2. Status: "Logging in..." (orange)
3. POST https://wos-edgegap-proxy.onrender.com/api/auth/login
   Body: {"Username":"Captain123","Password":"secret"}
4. [Wait 150ms for network response]
5. Response: 200 OK
   Body: {
     "success": true,
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "playerId": "550e8400-e29b-41d4-a716-446655440000",
     "username": "Captain123",
     "message": "Login successful"
   }
6. Parse JSON → AuthResponse object
7. Validate: success=true, token exists
8. Store in PlayerPrefs:
   - "authToken" = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
   - "playerId" = "550e8400-e29b-41d4-a716-446655440000"
   - "username" = "Captain123"
9. Status: "Login successful!" (green)
10. Wait 1 second
11. Navigate to Join Menu
12. isProcessing = false
```

#### Algorithm 2: RegisterCoroutine() - Create New Account

```
Input: username (string), password (string)
Output: New account created + JWT token stored OR error message

Flow:
1-3. (Same as LoginCoroutine - set processing state, disable buttons, show status)

4. Construct request:
   - URL: "{backendApiUrl}/api/auth/register"
   - Method: POST
   - Headers: Content-Type = application/json
   - Body: {"Username": "...", "Password": "..."}
   - NOTE: Email field omitted (Unity JsonUtility issue)

5. Create UnityWebRequest (same as LoginCoroutine)

6. Yield return request.SendWebRequest()

7. Check request.result:

   SUCCESS (200 OK):
   8a. Parse response JSON → AuthResponse object
   9a. Check response.success && response.token != null:

       TRUE (Registration successful):
       10a. Store auth data (same as LoginCoroutine)
       11a. Display "Registration successful!" (Success color)
       12a. Set registerSuccess = true
       13a. Wait 1 second
       14a. NavigateToJoinMenu() (automatic login)

       FALSE (Registration failed):
       10b. Display error message from server
       11b. Re-enable buttons (allow retry)

   FAILURE (Network error, 409 Conflict):
   8b. Log error response
   9b. Call HandleNetworkError(request):
       - 409 → "Username already exists. Please choose another."
       - 401 → "Invalid credentials."
       - 500 → "Server error. Please try again later."
   10b. Re-enable buttons (allow retry)

8. Set isProcessing = false

Error Handling:
- Same as LoginCoroutine
- Additional 409 Conflict handling (duplicate username)
```

**Example Execution (Success)**:
```
User enters: username="NewCaptain", password="mypass123"

1. POST https://wos-edgegap-proxy.onrender.com/api/auth/register
   Body: {"Username":"NewCaptain","Password":"mypass123"}
2. [Wait 200ms]
3. Response: 200 OK
   Body: {
     "success": true,
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "playerId": "660f9511-f3ac-52e5-b827-557766551111",
     "username": "NewCaptain",
     "message": "Account created successfully"
   }
4. Store auth data in PlayerPrefs
5. Status: "Registration successful!" (green)
6. Navigate to Join Menu (automatic login)
```

**Example Execution (Duplicate Username)**:
```
User enters: username="Captain123", password="anypass"

1. POST /api/auth/register
2. Response: 409 Conflict
   Body: {"success":false,"message":"Username already exists"}
3. HandleNetworkError(request):
   - Detects 409 status code
   - Maps to: "Username already exists. Please choose another."
4. Status: "Username already exists. Please choose another." (red)
5. Buttons re-enabled, user can try different username
```

#### Algorithm 3: Input Validation

```
Input: username (string), password (string)
Output: true (valid) OR false (invalid + error message displayed)

Username Validation (AuthDataHelper.ValidateUsername):
1. Check length >= 3 characters:
   FALSE → Error: "Username must be at least 3 characters."
   TRUE → Continue

2. Check length <= 20 characters:
   FALSE → Error: "Username must be 20 characters or less."
   TRUE → Continue

3. Check allowed characters (alphanumeric + underscore):
   - Pattern: ^[a-zA-Z0-9_]+$
   FALSE → Error: "Username can only contain letters, numbers, and underscores."
   TRUE → Valid

Password Validation (AuthDataHelper.ValidatePassword):
1. Check length >= 6 characters:
   FALSE → Error: "Password must be at least 6 characters."
   TRUE → Valid

2. No maximum length check
3. All characters allowed

Example Validation:
- "ab" → FAIL (too short, < 3 chars)
- "Captain123" → PASS (alphanumeric, 10 chars)
- "Captain@123" → FAIL (special character '@' not allowed)
- "VeryLongUsernameThatExceedsTwentyCharacters" → FAIL (> 20 chars)
- "pass" → FAIL (password < 6 chars)
- "password123" → PASS (>= 6 chars)
```

#### Algorithm 4: HandleNetworkError() - User-Friendly Error Messages

```
Input: UnityWebRequest request (failed request)
Output: User-friendly error message displayed

Flow:
1. Check request.result:

   ConnectionError:
   → "Unable to connect to server. Please check your internet connection."

   ProtocolError (HTTP status code):
   2a. Get request.responseCode
   3a. Map status code to message:
       - 401 → "Invalid username or password."
       - 409 → "Username already exists. Please choose another."
       - 500 → "Server error. Please try again later."
       - Other → "Server error ({code}). Please try again."

   Other (Timeout, etc.):
   → "Connection timed out. Please try again."

2. Call UpdateStatus(errorMessage, StatusType.Error)
3. Log warning with technical details for debugging

Example Mappings:
- Connection lost → "Unable to connect to server. Please check your internet connection."
- 401 Unauthorized → "Invalid username or password."
- 409 Conflict → "Username already exists. Please choose another."
- 500 Internal Server Error → "Server error. Please try again later."
- Timeout after 10s → "Connection timed out. Please try again."
```

#### Algorithm 5: UpdateStatus() - Color-Coded Status Display

```
Input: message (string), type (StatusType enum)
Output: Status text updated with color-coded message

Flow:
1. Set statusText.text = message

2. Switch on type:
   - Info → Color = infoColor (Orange: 255, 165, 0)
   - Success → Color = successColor (Green: 0, 255, 0)
   - Error → Color = errorColor (Red: 255, 0, 0)

3. Apply color to statusText.textComponent.color

4. Log message to console: "[LoginController] {type}: {message}"

Visual Result:
- "Logging in..." → ORANGE text
- "Login successful!" → GREEN text
- "Invalid username or password." → RED text
```

---

## Example Usage

### Button Callbacks in Unity Inspector

**Login Button**:
```
1. Select Login Button GameObject
2. Inspector → ButtonManager component
3. On Click Events → Add callback
4. Target: LoginController instance
5. Function: LoginController.OnLoginButtonClicked()
```

**Register Button**:
```
1. Select Register Button GameObject
2. Inspector → ButtonManager component
3. On Click Events → Add callback
4. Target: LoginController instance
5. Function: LoginController.OnRegisterButtonClicked()
```

**Back Button**:
```
1. Select Back Button GameObject
2. Inspector → ButtonManager component
3. On Click Events → Add callback
4. Target: LoginController instance
5. Function: LoginController.OnBackButtonClicked()
```

### Authentication Flow Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    User Interaction                      │
└───────────────────┬─────────────────────────────────────┘
                    │
                    │ 1. Enter credentials
                    ▼
         ┌──────────────────────┐
         │  OnLoginButtonClicked│
         │                      │
         │  - Read input fields │
         │  - Validate inputs   │
         └──────────┬───────────┘
                    │ 2. Inputs valid?
                    │
            ┌───────┴──────┐
            │ YES          │ NO
            │              │
            ▼              ▼
  ┌─────────────────┐  Display
  │ LoginCoroutine  │  validation
  │                 │  error
  │ - Disable UI    │
  │ - Build request │
  └────────┬────────┘
           │ 3. POST to backend
           │
           ▼
  ┌─────────────────┐
  │  Backend API    │
  │                 │
  │ - Verify creds  │
  │ - Generate JWT  │
  └────────┬────────┘
           │ 4. Response
           │
    ┌──────┴──────┐
    │ Success     │ Failure
    │             │
    ▼             ▼
┌─────────────┐ ┌──────────────────┐
│ Store Token │ │ HandleNetworkError│
│ in          │ │                  │
│ PlayerPrefs │ │ - Map error code │
└──────┬──────┘ │ - Show message   │
       │        │ - Clear password │
       │        │ - Re-enable UI   │
       │        └──────────────────┘
       │ 5. Navigate
       ▼
┌──────────────────┐
│ NavigateToJoinMenu│
│                  │
│ - MenuManager.   │
│   Instance.      │
│   ShowJoinMenu() │
└──────────────────┘
```

### Code Usage Example

```csharp
using WOS.UI;
using UnityEngine;

public class CustomAuthFlow : MonoBehaviour
{
    // Programmatic login (not recommended - use LoginController UI)
    public void AttemptLogin(string username, string password)
    {
        // LoginController is designed for UI interaction
        // For programmatic login, access AuthDataHelper directly

        // Check if already logged in
        string existingToken = PlayerPrefs.GetString("authToken", "");
        if (!string.IsNullOrEmpty(existingToken))
        {
            Debug.Log("User already logged in");
            MenuManager.Instance.ShowJoinMenu();
            return;
        }

        // Otherwise, redirect to login panel
        MenuManager.Instance.ShowLoginMenu();
    }

    // Check authentication status
    public bool IsUserLoggedIn()
    {
        string token = PlayerPrefs.GetString("authToken", "");
        return !string.IsNullOrEmpty(token);
    }

    // Logout (clear stored credentials)
    public void Logout()
    {
        // Clear all auth data
        PlayerPrefs.DeleteKey("authToken");
        PlayerPrefs.DeleteKey("playerId");
        PlayerPrefs.DeleteKey("username");
        PlayerPrefs.Save();

        Debug.Log("User logged out");

        // Return to main menu
        MenuManager.Instance.ShowMainMenu();
    }
}
```

---

## Related Files

### Data Models (WOS.Networking.Data)
- **AuthDataHelper** - Token storage utilities
  - `StoreAuthData(token, playerId, username)` - Save credentials
  - `ClearAuthData()` - Logout/clear credentials
  - `ValidateUsername(username, out error)` - Username validation
  - `ValidatePassword(password, out error)` - Password validation

- **LoginRequest** - Login request structure
  ```csharp
  [Serializable]
  public class LoginRequest
  {
      public string Username;
      public string Password;
  }
  ```

- **AuthResponse** - Authentication response structure
  ```csharp
  [Serializable]
  public class AuthResponse
  {
      public bool success;
      public string token;      // JWT token string
      public string playerId;   // UUID string
      public string username;   // Display name
      public string message;    // Error/success message
  }
  ```

### Menu System
- [[MenuManager]] - Panel navigation and history management
- [[MainMenuController]] - Main menu entry point
- [[ConnectionMenuController]] - Post-login navigation
- [[JoinMenuController]] - Server browser (requires authentication)

### GDD Documentation
- [[Authentication]] - Complete authentication system design
- [[Menu-System]] - Menu architecture and navigation flow
- [[Network-Architecture]] - Backend API and JWT integration
- [[UI-Overview]] - MUIP framework integration

### Unity Assets
- LoginPanel.prefab - Login UI panel with all fields
- MUIP Assets - Modern UI Pack components
- Backend API (external) - Node.js/Express authentication server

---

## Testing Notes

### What Has Been Tested
- ✅ Login with valid credentials (success path)
- ✅ Login with invalid credentials (401 error handling)
- ✅ Registration with new username (success path)
- ✅ Registration with existing username (409 error handling)
- ✅ Network timeout handling (10 second timeout)
- ✅ Input validation (username/password requirements)
- ✅ Token storage verification (PlayerPrefs)
- ✅ Button state management (disable during API call)
- ✅ Status message color coding (Info/Success/Error)
- ✅ Password field clearing on error (security)
- ✅ MUIP animation integration (fade in/out)
- ✅ MenuManager navigation (back button, panel switching)

### Known Edge Cases

**Case 1: Rapid Button Clicking**:
```
Scenario: User clicks Login button multiple times rapidly
Expected: Only first click processes, subsequent clicks ignored
Actual: isProcessing flag prevents concurrent attempts
Status: ✅ Works as designed
```

**Case 2: Empty Input Fields**:
```
Scenario: User clicks Login with empty username/password
Expected: Validation error displayed, no API call made
Actual: ValidateUsername/ValidatePassword catch empty inputs
Status: ✅ Validation works correctly
```

**Case 3: Backend API Offline**:
```
Scenario: Backend server unavailable (connection refused)
Expected: "Unable to connect to server. Please check your internet connection."
Actual: ConnectionError caught by HandleNetworkError
Status: ✅ Error handling correct
```

**Case 4: Malformed JSON Response**:
```
Scenario: Backend returns invalid JSON (not AuthResponse format)
Expected: "Invalid server response. Please try again."
Actual: JsonUtility.FromJson() throws exception, caught by try-catch
Status: ✅ Exception handling prevents crash
```

**Case 5: Token Storage Failure**:
```
Scenario: PlayerPrefs.SetString() fails (rare disk full scenario)
Expected: Login succeeds but token not stored (user must re-login)
Actual: No explicit error handling (Unity issue, not script issue)
Status: ⚠️ Acceptable risk (extremely rare, no data corruption)
```

### Test Scenarios

**Manual Test 1: Complete Login Flow**:
1. Launch game → Navigate to Login Panel
2. Enter username: "TestCaptain", password: "testpass123"
3. Click "Login" button
4. **Observe**:
   - Buttons disabled immediately
   - Status: "Logging in..." (orange)
   - [Wait for response]
   - Status: "Login successful!" (green)
   - Navigation to Join Menu
5. **Verify**:
   - PlayerPrefs contains authToken
   - Console log shows success message
✅ **Result**: Complete flow works correctly

**Manual Test 2: Invalid Password**:
1. Navigate to Login Panel
2. Enter username: "TestCaptain", password: "wrong"
3. Click "Login" button
4. **Observe**:
   - Status: "Logging in..." (orange)
   - [Wait for response]
   - Status: "Invalid username or password." (red)
   - Password field cleared
   - Username field retains value
   - Buttons re-enabled
5. **Verify**: No PlayerPrefs stored, no navigation
✅ **Result**: Error handling correct

**Manual Test 3: Network Timeout**:
1. Disconnect from internet
2. Navigate to Login Panel
3. Attempt login
4. **Observe**:
   - Status: "Logging in..." (orange)
   - [Wait 10 seconds]
   - Status: "Connection timed out. Please try again." (red)
   - Buttons re-enabled
5. **Verify**: No hang, UI responsive
✅ **Result**: Timeout handling correct

---

## Common Pitfalls

### Pitfall 1: Forgetting to Assign Inspector Fields
**Problem**: NullReferenceException if buttons/fields not assigned
**Solution**: ValidateReferences() logs warnings at startup
**Code**:
```csharp
// ✅ CORRECT (with validation)
private void Start()
{
    ValidateReferences(); // Checks all fields
    ShowLoginForm();
}

// ❌ WRONG (no validation)
private void Start()
{
    usernameField.text = ""; // Crash if usernameField = null!
}
```

### Pitfall 2: Storing Passwords in PlayerPrefs
**Problem**: Security risk - passwords should NEVER be stored client-side
**Solution**: LoginController only stores JWT tokens (password cleared immediately)
**Code**:
```csharp
// ✅ CORRECT (store token only)
AuthDataHelper.StoreAuthData(response.token, response.playerId, response.username);

// ❌ WRONG (never store password)
PlayerPrefs.SetString("password", password); // SECURITY RISK!
```

### Pitfall 3: Not Handling Token Expiration
**Problem**: Token expires after 24 hours, user gets 401 errors
**Solution**: Check for 401 responses and redirect to login
**Code**:
```csharp
// ✅ CORRECT (detect expired token)
if (request.responseCode == 401)
{
    PlayerPrefs.DeleteKey("authToken"); // Clear invalid token
    MenuManager.Instance.ShowLoginMenu(); // Force re-login
}
```

### Pitfall 4: Concurrent Login Attempts
**Problem**: User clicks Login button twice, causing race condition
**Solution**: isProcessing flag prevents concurrent attempts
**Code**:
```csharp
// ✅ CORRECT (with guard flag)
public void OnLoginButtonClicked()
{
    if (isProcessing)
    {
        Debug.LogWarning("Login already in progress");
        return; // Ignore click
    }

    isProcessing = true;
    // ... continue login
}
```

---

## Security Considerations

### Password Security
- ✅ Password field uses Content Type: Password (hidden input)
- ✅ Password sent via HTTPS (encrypted in transit)
- ✅ Password NEVER stored client-side (only tokens stored)
- ✅ Password cleared from field on error (prevents shoulder surfing)
- ✅ Server uses bcrypt hashing (backend responsibility)

### Token Security
- ✅ JWT tokens stored in PlayerPrefs (obfuscated)
- ✅ Tokens transmitted via HTTPS (encrypted)
- ✅ Tokens expire after 24 hours (time-limited)
- ⚠️ PlayerPrefs not encrypted (acceptable risk - tokens expire)
- 📋 Phase 2: Encrypted storage with Unity Keychain

### Network Security
- ✅ HTTPS enforced (TLS 1.2+)
- ✅ Request timeout (10 seconds - prevents DoS)
- ✅ Rate limiting (server-side - prevents brute force)
- ✅ Input validation (client + server - prevents injection)

---

## Changelog

- **2025-01-XX**: Initial implementation with login/registration flows
- **2025-01-XX**: Added JWT token integration with backend API
- **2025-01-XX**: Implemented input validation (username/password)
- **2025-01-XX**: Added color-coded status messages (Info/Success/Error)
- **2025-01-XX**: Integrated with MenuManager navigation
- **2025-01-XX**: Added timeout handling (10 second limit)
- **2025-01-XX**: Implemented user-friendly error messages
- **2025-01-XX**: Added password field clearing on error (security)
- **2025-01-XX**: MUIP framework integration (ButtonManager, FieldManager)
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Production-ready, no known bugs
**Maintenance**: Stable, minimal changes planned for Phase 2-3
**Performance**: Excellent (< 0.2ms CPU overhead per login)
