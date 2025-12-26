# PlayFabConnectionTest

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Testing/PlayFabConnectionTest.cs` |
| **Namespace** | `WOS.Testing` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 112 |
| **Architecture** | Testing utility for PlayFab SDK integration |

## Purpose

Simple test component to verify PlayFab SDK configuration and authentication. Tests basic authentication with email/password and automatically attempts registration if login fails.

## Configuration

### Inspector Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `runOnStart` | `bool` | `true` | Automatically run test on component Start |
| `testEmail` | `string` | `"test@wosnavalmmo.com"` | Test account email |
| `testPassword` | `string` | `"TestPassword123!"` | Test account password |

## Key Features

### Automated Testing Flow

```csharp
// Test sequence:
// 1. Verify Title ID configured
// 2. Attempt login with test credentials
// 3. If login fails (AccountNotFound) → Attempt registration
// 4. Log all results with network context
```

### Test Validation

```csharp
// Title ID check
if (string.IsNullOrEmpty(PlayFabSettings.TitleId))
{
    DebugManager.LogError(DebugCategory.Networking,
        "[PlayFabTest] Title ID not configured!", this);
    return;
}
```

## Public API

### Context Menu Methods

#### `TestConnection()`
```csharp
[ContextMenu("Test PlayFab Connection")]
public void TestConnection()
```

Manually trigger PlayFab connection test. Can be called from Inspector or code.

**Test Steps**:
1. Validates `PlayFabSettings.TitleId` is configured
2. Attempts login with test credentials
3. On `AccountNotFound` error, attempts registration
4. Logs all results with session ticket preview

## Usage Examples

### Basic Setup

```csharp
// Attach to GameObject in test scene
// Configure test credentials in Inspector
// Enable runOnStart for automatic testing
```

### Manual Invocation

```csharp
// From another script
var tester = FindObjectOfType<PlayFabConnectionTest>();
if (tester != null)
{
    tester.TestConnection();
}
```

### Expected Output

```
[PlayFabTest] Testing PlayFab connection...
[PlayFabTest] Title ID configured: ABCD1234
[PlayFabTest] Successfully connected to PlayFab!
[PlayFabTest] PlayFab ID: 1234567890ABCDEF
[PlayFabTest] Session Ticket: A1B2C3D4E5F6G7H8I9...
[PlayFabTest] Player Display Name: TestPlayer
```

## Integration Points

### Dependencies

- **PlayFab SDK**: `PlayFab.ClientModels`, `PlayFabClientAPI`
- **DebugManager**: Category-based logging with network context

### Network Context

All logs include network role:
- `[OFFLINE]` - No network connection
- `[CLIENT]` - Client-only mode
- `[SERVER]` - Server-only mode
- `[HOST]` - Combined server + client

## Error Handling

### Expected Errors

| Error | Reason | Auto-Recovery |
|-------|--------|---------------|
| Title ID not configured | Missing PlayFab setup | No - requires manual configuration |
| AccountNotFound | First run, no account exists | Yes - attempts registration |
| Unexpected error | Network/API issue | No - logs error report |

### Registration Flow

```csharp
// Auto-triggered on AccountNotFound
var request = new RegisterPlayFabUserRequest
{
    Email = testEmail,
    Password = testPassword,
    Username = "TestPlayer",
    RequireBothUsernameAndEmail = false
};
```

## Testing Workflow

### Pre-Test Checklist

1. ✅ PlayFab Title ID configured (`PlayFab → Make PlayFab Shared Settings`)
2. ✅ DebugManager present in scene
3. ✅ Network category logging enabled
4. ✅ Test credentials configured

### Test Scenarios

#### Scenario 1: First Run (No Account)
```
1. Login fails → AccountNotFound
2. Auto-registers new account
3. Success → PlayFab ID logged
```

#### Scenario 2: Subsequent Runs (Account Exists)
```
1. Login succeeds immediately
2. Session ticket received
3. Player profile loaded
```

#### Scenario 3: Configuration Error
```
1. Title ID check fails
2. Error logged with configuration instructions
3. Test aborted
```

## Design Notes

### Callback Architecture

Uses PlayFab async callback pattern:
- `OnLoginSuccess` / `OnLoginFailure`
- `OnRegisterSuccess` / `OnRegisterFailure`

### Session Data

Retrieves combined player info:
```csharp
InfoRequestParameters = new GetPlayerCombinedInfoRequestParams
{
    GetPlayerProfile = true,
    GetUserAccountInfo = true
}
```

### Security Considerations

**⚠️ WARNING**: Test credentials are visible in Inspector.
- **For development/testing only**
- **Never use in production builds**
- **Change default password before deployment**

## Related Scripts

- **AuthenticationManager**: Production authentication system
- **DebugManager**: Centralized logging
- **PlayFabServerManager**: Server-side PlayFab integration
