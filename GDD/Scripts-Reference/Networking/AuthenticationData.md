# AuthenticationData.cs

## Quick Reference

| **File** | AuthenticationData.cs |
|----------|---------------------|
| **Namespace** | WOS.Networking.Data |
| **Type** | Data Models + Helper Class |
| **Lines** | 225 |
| **Architecture** | JSON serialization models, PlayerPrefs storage |

---

## Purpose

Authentication data models for login/register operations with backend API and PlayFab. Provides JSON serialization models and PlayerPrefs storage helpers.

**Note**: Field names must match backend API exactly (case-sensitive).

---

## Request Models

### `LoginRequest`

Login request payload sent to backend API.

**Endpoint**: `POST /api/auth/login`

```csharp
[Serializable]
public class LoginRequest
{
    public string Username;  // PascalCase (backend requirement)
    public string Password;  // PascalCase (backend requirement)
}
```

### `RegisterRequest`

Registration request payload sent to backend API.

**Endpoint**: `POST /api/auth/register`

```csharp
[Serializable]
public class RegisterRequest
{
    public string Username;  // PascalCase (backend requirement)
    public string Password;  // PascalCase (backend requirement)
    public string Email;     // Optional field
}
```

---

## Response Models

### `AuthResponse`

Authentication response from backend API (used for both login and registration).

**Backend Response**: `{ success, playerId, username, token }`

```csharp
[Serializable]
public class AuthResponse
{
    public bool success;      // Backend returns lowercase
    public string token;      // PlayFab SessionTicket (was JWT token)
    public string playerId;   // PlayFab ID (camelCase)
    public string username;   // Display name (lowercase)
    public string message;    // Success message or error description
}
```

---

## AuthDataHelper Class

Static helper class for authentication data management using PlayerPrefs.

### Storage Keys

| PlayerPrefs Key | Stores | Type |
|----------------|--------|------|
| `WOS_JWT_Token` | PlayFab SessionTicket (legacy name) | string |
| `WOS_PlayerId` | PlayFab player ID | string |
| `WOS_Username` | Display username | string |
| `WOS_LoginTimestamp` | Login timestamp (ISO 8601) | string |

### Public Methods

#### `StoreAuthData(string token, string playerId, string username)`
Stores authentication data in PlayerPrefs after successful login.

**Parameters**:
- `token` - PlayFab SessionTicket (stored in `WOS_JWT_Token` key)
- `playerId` - PlayFab player ID
- `username` - Display username

**Example**:
```csharp
AuthDataHelper.StoreAuthData(authResponse.token, authResponse.playerId, authResponse.username);
```

#### `ClearAuthData()`
Clears all authentication data from PlayerPrefs (logout).

**Example**:
```csharp
AuthDataHelper.ClearAuthData();
```

#### `HasStoredToken()`
Checks if user has stored authentication token.

**Returns**: `bool`

**Example**:
```csharp
if (AuthDataHelper.HasStoredToken())
{
    string token = AuthDataHelper.GetToken();
    // Auto-login with stored token
}
```

#### `GetToken()`
Gets stored authentication token (PlayFab SessionTicket).

**Returns**: `string` (empty if not stored)

#### `GetPlayerId()`
Gets stored player ID.

**Returns**: `string` (empty if not stored)

#### `GetUsername()`
Gets stored username.

**Returns**: `string` (empty if not stored)

#### `GetLoginTimestamp()`
Gets login timestamp.

**Returns**: `DateTime` (`DateTime.MinValue` if not stored)

### Validation Methods

#### `ValidateUsername(string username, out string errorMessage)`
Validates username input.

**Rules**:
- Not empty/whitespace
- 3-20 characters
- Letters, numbers, underscores only

**Returns**: `bool` (true if valid)

**Example**:
```csharp
if (!AuthDataHelper.ValidateUsername(username, out string error))
{
    Debug.LogError(error);
    // Display error to user
}
```

#### `ValidatePassword(string password, out string errorMessage)`
Validates password input.

**Rules**:
- Not empty/whitespace
- 8-64 characters
- Must match backend validation

**Returns**: `bool` (true if valid)

**Example**:
```csharp
if (!AuthDataHelper.ValidatePassword(password, out string error))
{
    Debug.LogError(error);
    // Display error to user
}
```

---

## Usage Example

### Complete Login Flow

```csharp
using WOS.Networking.Data;

public class LoginManager : MonoBehaviour
{
    public void Login(string username, string password)
    {
        // Validate input
        if (!AuthDataHelper.ValidateUsername(username, out string usernameError))
        {
            ShowError(usernameError);
            return;
        }

        if (!AuthDataHelper.ValidatePassword(password, out string passwordError))
        {
            ShowError(passwordError);
            return;
        }

        // Create request
        var request = new LoginRequest
        {
            Username = username,
            Password = password
        };

        // Send to backend (PlayFab authentication)
        AuthenticationManager.Instance.Login(username, password, (response, success) =>
        {
            if (success)
            {
                // Store credentials
                AuthDataHelper.StoreAuthData(response.token, response.playerId, response.username);

                Debug.Log($"Logged in as {response.username} (ID: {response.playerId})");
            }
            else
            {
                ShowError(response.message);
            }
        });
    }

    public void Logout()
    {
        // Clear stored credentials
        AuthDataHelper.ClearAuthData();
        Debug.Log("Logged out");
    }
}
```

### Auto-Login

```csharp
void Start()
{
    // Check for stored credentials
    if (AuthDataHelper.HasStoredToken())
    {
        string token = AuthDataHelper.GetToken();
        string playerId = AuthDataHelper.GetPlayerId();
        string username = AuthDataHelper.GetUsername();

        Debug.Log($"Auto-login: {username} (last login: {AuthDataHelper.GetLoginTimestamp()})");

        // Attempt auto-login with stored SessionTicket
        AuthenticationManager.Instance.AutoLogin(token, playerId);
    }
    else
    {
        // Show login screen
        ShowLoginUI();
    }
}
```

---

## Integration Points

### AuthenticationManager

AuthDataHelper is used by AuthenticationManager to persist login state:

```csharp
// AuthenticationManager.cs
private void HandleLoginSuccess(AuthResponse response)
{
    // Store credentials for auto-login
    AuthDataHelper.StoreAuthData(response.token, response.playerId, response.username);

    // Continue with game connection
    ConnectToGameServer();
}
```

### UI Forms

Validation methods integrate with login/register UI:

```csharp
// LoginController.cs
private bool ValidateForm()
{
    if (!AuthDataHelper.ValidateUsername(usernameInput.text, out string usernameError))
    {
        usernameErrorText.text = usernameError;
        return false;
    }

    if (!AuthDataHelper.ValidatePassword(passwordInput.text, out string passwordError))
    {
        passwordErrorText.text = passwordError;
        return false;
    }

    return true;
}
```

---

## Design Notes

### Field Name Case Sensitivity

**Important**: JSON field names must match backend API exactly.

**Request Models** (sent to backend):
```csharp
public string Username;  // PascalCase (backend uses C# models)
public string Password;  // PascalCase
```

**Response Models** (received from backend):
```csharp
public bool success;     // lowercase (backend uses C# → JSON serialization)
public string token;     // lowercase
public string playerId;  // camelCase
```

### PlayFab SessionTicket Storage

**Legacy Key Name**: `WOS_JWT_Token`
- Originally stored JWT token from custom backend
- Now stores PlayFab SessionTicket
- Key name kept for backwards compatibility

**SessionTicket Usage**:
- Returned by PlayFab after successful login
- Used to authenticate subsequent PlayFab API calls
- Expires after period of inactivity
- Stored in PlayerPrefs for auto-login

---

## Key Takeaways

1. **Case-Sensitive**: Field names must match backend API exactly
2. **PlayerPrefs Storage**: Uses PlayerPrefs for persistent login state
3. **Validation**: Client-side validation matches backend requirements
4. **PlayFab Integration**: Stores PlayFab SessionTicket for auto-login
5. **Security**: Password validation enforces minimum requirements (8-64 chars)
