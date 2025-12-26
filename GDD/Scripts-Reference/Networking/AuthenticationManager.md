---
tags: [script, networking, playfab, authentication, implemented]
script-type: MonoBehaviour (Singleton)
namespace: WOS.Networking.Managers
file-path: Assets/Scripts/Networking/Managers/AuthenticationManager.cs
status: IMPLEMENTED
size: ~12 KB (420 lines)
feature-group: networking
---

# AuthenticationManager.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Networking.Managers
**File**: `Assets/Scripts/Networking/Managers/AuthenticationManager.cs`
**Size**: ~12 KB (420 lines)
**Dependencies**: PlayFab, Mirror

---

## Purpose
Client-side PlayFab authentication manager. Handles login, registration, session management, and server-side ticket validation.

This component manages:
- Email/password login flow
- New player registration
- Session ticket management
- Guest authentication (development)
- Server-side session validation
- Logout and session cleanup

---

## Key Components

### Singleton Access
```csharp
public static AuthenticationManager Instance { get; }
```

### Properties
```csharp
public string PlayFabId { get; }           // Current user's PlayFab ID
public string SessionTicket { get; }       // Session ticket for server auth
public string DisplayName { get; }         // Player display name
public bool IsAuthenticated { get; }       // Authentication state
```

### Public Methods
- `Login(string email, string password, Action<bool, string> callback)`
- `Register(string email, string password, string displayName, Action<bool, string> callback)`
- `LoginAsGuest(Action<bool, string> callback)`
- `Logout()`
- `ValidateSessionTicket(string ticket, Action<bool> callback)` [Server]

### Events
```csharp
event Action OnLoginSuccess;
event Action<string> OnLoginFailed;
event Action OnLogout;
```

---

## Authentication Flow

### Login
```csharp
public void Login(string email, string password, Action<bool, string> callback)
{
    var request = new LoginWithEmailAddressRequest
    {
        Email = email,
        Password = password,
        InfoRequestParameters = new GetPlayerCombinedInfoRequestParams
        {
            GetPlayerProfile = true
        }
    };

    PlayFabClientAPI.LoginWithEmailAddress(request,
        result =>
        {
            PlayFabId = result.PlayFabId;
            SessionTicket = result.SessionTicket;
            DisplayName = result.InfoResultPayload?.PlayerProfile?.DisplayName;
            IsAuthenticated = true;

            OnLoginSuccess?.Invoke();
            callback?.Invoke(true, null);
        },
        error =>
        {
            OnLoginFailed?.Invoke(error.ErrorMessage);
            callback?.Invoke(false, error.ErrorMessage);
        });
}
```

### Registration
```csharp
public void Register(string email, string password, string displayName,
    Action<bool, string> callback)
{
    var request = new RegisterPlayFabUserRequest
    {
        Email = email,
        Password = password,
        DisplayName = displayName,
        RequireBothUsernameAndEmail = false
    };

    PlayFabClientAPI.RegisterPlayFabUser(request,
        result =>
        {
            // Auto-login after registration
            Login(email, password, callback);
        },
        error =>
        {
            callback?.Invoke(false, error.ErrorMessage);
        });
}
```

### Guest Login (Development)
```csharp
public void LoginAsGuest(Action<bool, string> callback)
{
    var request = new LoginWithCustomIDRequest
    {
        CustomId = SystemInfo.deviceUniqueIdentifier,
        CreateAccount = true,
        InfoRequestParameters = new GetPlayerCombinedInfoRequestParams
        {
            GetPlayerProfile = true
        }
    };

    PlayFabClientAPI.LoginWithCustomID(request,
        result =>
        {
            PlayFabId = result.PlayFabId;
            SessionTicket = result.SessionTicket;
            IsAuthenticated = true;

            callback?.Invoke(true, null);
        },
        error =>
        {
            callback?.Invoke(false, error.ErrorMessage);
        });
}
```

---

## Server-Side Validation

### ValidateSessionTicket
Called by server to validate client session:

```csharp
[Server]
public void ValidateSessionTicket(string ticket, Action<bool> callback)
{
    var request = new AuthenticateSessionTicketRequest
    {
        SessionTicket = ticket
    };

    PlayFabServerAPI.AuthenticateSessionTicket(request,
        result =>
        {
            bool isValid = result.IsSessionTicketExpired == false;
            callback?.Invoke(isValid);
        },
        error =>
        {
            DebugManager.LogError(DebugCategory.Networking,
                $"Session validation failed: {error.ErrorMessage}");
            callback?.Invoke(false);
        });
}
```

---

## Session Management

### Logout
```csharp
public void Logout()
{
    // Clear session data
    PlayFabId = null;
    SessionTicket = null;
    DisplayName = null;
    IsAuthenticated = false;

    // Notify listeners
    OnLogout?.Invoke();

    // Disconnect from server if connected
    if (NetworkClient.isConnected)
    {
        NetworkManager.singleton.StopClient();
    }
}
```

### Session Persistence
Session tokens stored in PlayerPrefs for remember-me:

```csharp
private void SaveSession()
{
    PlayerPrefs.SetString("PlayFabId", PlayFabId);
    PlayerPrefs.SetString("SessionTicket", SessionTicket);
    PlayerPrefs.Save();
}

private bool TryRestoreSession()
{
    string savedId = PlayerPrefs.GetString("PlayFabId", null);
    string savedTicket = PlayerPrefs.GetString("SessionTicket", null);

    if (string.IsNullOrEmpty(savedId) || string.IsNullOrEmpty(savedTicket))
        return false;

    // Validate saved session
    ValidateSessionTicket(savedTicket, isValid =>
    {
        if (isValid)
        {
            PlayFabId = savedId;
            SessionTicket = savedTicket;
            IsAuthenticated = true;
        }
    });

    return true;
}
```

---

## Integration with Mirror

### Connection Authentication
```csharp
// In WOSNetworkManager.OnClientConnect:
var authRequest = new AuthRequestMessage
{
    PlayFabId = AuthenticationManager.Instance.PlayFabId,
    SessionTicket = AuthenticationManager.Instance.SessionTicket
};
NetworkClient.Send(authRequest);
```

---

## Integration Points

### Dependencies
- **PlayFab Client SDK** - Login/Register APIs
- **PlayFab Server SDK** - Session validation
- **Mirror** - Network connection

### Used By
- [[LoginController]] - UI integration
- [[RegisterController]] - Registration UI
- [[WOSNetworkManager]] - Connection auth

---

## Error Handling

Common PlayFab errors:
- `InvalidEmailOrPassword` - Wrong credentials
- `AccountNotFound` - Email not registered
- `EmailAddressNotAvailable` - Already registered
- `InvalidParams` - Invalid input format
- `SessionTicketExpired` - Session timeout

---

## Related Files
- [[LoginController]] - Login UI
- [[WOSNetworkManager]] - Uses session ticket
- [[PlayFabServerManager]] - Server-side auth

---

## Testing Notes
- Guest login uses device ID
- Session tickets expire (default 24h)
- Server validation requires Server SDK
- DontDestroyOnLoad for persistence

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added session persistence
- **2025-01**: Added server-side validation

