---
tags: [implemented, phase1, multiplayer, authentication, security]
status: ✅ IMPLEMENTED
phase: Phase 1
priority: HIGH
last-updated: 2025-11-17
---

# Authentication System

## Overview
Fathoms Deep implements JWT (JSON Web Token) based authentication for secure player accounts. The system provides login/registration flows with backend API integration, persistent token storage, and seamless integration with the multiplayer networking system. Authentication is required before joining multiplayer sessions.

## Implementation Status
**Status**: ✅ **IMPLEMENTED** (Core authentication complete)
**Phase**: Phase 1 Complete
**Scripts**: [[LoginController]], [[AuthDataHelper]], [[MenuManager]]
**Priority**: HIGH - Required for multiplayer access

---

## Design Specification

### Core Concept
The authentication system uses modern web standards (JWT tokens) to provide secure, stateless authentication. Players create accounts or login through a dedicated UI panel, receiving a JWT token that authorizes access to multiplayer features. The system is designed to be user-friendly while maintaining security best practices.

### Key Features
- **JWT Token Authentication**: Industry-standard JSON Web Tokens for stateless auth
- **Dual Workflows**: Separate login and registration flows with unified UI
- **Backend API Integration**: RESTful API communication via UnityWebRequest
- **Persistent Sessions**: Token storage using Unity PlayerPrefs
- **User-Friendly Error Handling**: Clear, actionable error messages for common issues
- **MUIP UI Integration**: Modern UI Pack framework for polished login screens
- **Validation**: Client-side and server-side input validation
- **Security-First Design**: Password field clearing, secure token storage, HTTPS support

### User Experience

#### Login Flow
1. Player launches game → Presented with Main Menu
2. Clicks "Play" → Navigates to Login Panel (via MenuManager)
3. Enters username and password
4. Clicks "Login" button
5. System validates inputs → Sends credentials to backend API
6. On success: Token stored → Navigates to Join Menu
7. On failure: Error message displayed → Password field cleared for retry

#### Registration Flow
1. New player clicks "Register" button (on Login Panel)
2. Enters desired username and password
3. System validates inputs (username length, password strength)
4. Sends registration request to backend API
5. On success: Account created + automatic login → Token stored → Join Menu
6. On failure: Error displayed (e.g., "Username already exists")

---

## Technical Implementation

### Current Implementation

The authentication system is fully implemented with the following components:

**LoginController.cs** (Primary Controller):
- Manages login/registration UI panel
- Handles user input validation
- Communicates with backend API via HTTPS
- Stores JWT tokens securely in PlayerPrefs
- Provides color-coded status messages (Info/Success/Error)

**Backend API** (Node.js/Express):
- URL: `https://wos-edgegap-proxy.onrender.com`
- Endpoints: `/api/auth/login` and `/api/auth/register`
- Returns JWT tokens on successful authentication
- Validates credentials against PostgreSQL database

**Data Models** (WOS.Networking.Data namespace):
- `LoginRequest`: Username + Password
- `AuthResponse`: Token + PlayerId + Username + Success flag
- `AuthDataHelper`: Token storage/retrieval utilities

### Key Components

#### JWT Token Structure
```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "playerId": "uuid-string",
    "username": "PlayerName",
    "iat": 1699564800,
    "exp": 1699651200
  },
  "signature": "encrypted-hash"
}
```

**Token Lifecycle**:
1. **Generation**: Server creates token on successful login
2. **Storage**: Client stores in PlayerPrefs (`authToken` key)
3. **Usage**: Included in HTTP headers for authenticated API calls
4. **Validation**: Server verifies signature on each request
5. **Expiration**: Token expires after 24 hours (configurable server-side)

#### Authentication Flow Diagram
```
┌──────────────┐
│   Player     │
│  (Client)    │
└──────┬───────┘
       │ 1. Enter credentials
       │
       ▼
┌──────────────────────┐
│  LoginController     │
│                      │
│  - Validate inputs   │
│  - Create JSON       │
└──────┬───────────────┘
       │ 2. POST /api/auth/login
       │    {username, password}
       │
       ▼
┌──────────────────────┐
│  Backend API         │
│  (Node.js/Express)   │
│                      │
│  - Verify credentials│
│  - Query PostgreSQL  │
│  - Generate JWT      │
└──────┬───────────────┘
       │ 3. Response {success, token, playerId}
       │
       ▼
┌──────────────────────┐
│  AuthDataHelper      │
│                      │
│  - Store token       │
│  - Save playerId     │
└──────┬───────────────┘
       │ 4. Token stored in PlayerPrefs
       │
       ▼
┌──────────────────────┐
│  MenuManager         │
│                      │
│  - Navigate to       │
│    JoinMenu          │
└──────────────────────┘
```

### Configuration

#### LoginController Inspector Settings
```
[Header("Backend Configuration")]
- backendApiUrl: "https://wos-edgegap-proxy.onrender.com"
- requestTimeout: 10 seconds

[Header("UI References")]
- usernameField: TMP_InputField (username entry)
- passwordField: TMP_InputField (password entry, Content Type: Password)
- loginButton: ButtonManager (MUIP login button)
- registerButton: ButtonManager (MUIP register button)
- backButton: ButtonManager (return to main menu)
- statusText: TMP_InputField (read-only status display)

[Header("Status Colors")]
- infoColor: Orange (RGB: 255, 165, 0) - Loading/processing messages
- successColor: Green (RGB: 0, 255, 0) - Success confirmations
- errorColor: Red (RGB: 255, 0, 0) - Error messages
```

#### Input Validation Rules
**Username**:
- Minimum length: 3 characters
- Maximum length: 20 characters
- Allowed characters: Alphanumeric + underscore
- Case-sensitive

**Password**:
- Minimum length: 6 characters
- No maximum length (within reason)
- All characters allowed
- Case-sensitive

---

## Integration Points

### Dependencies (What This Needs)

**Unity Systems**:
- UnityEngine.Networking - UnityWebRequest for HTTP calls
- TMPro - TMP_InputField for text entry
- UnityEngine.UI - Button interaction

**Third-Party Assets**:
- Michsky.MUIP - Modern UI Pack framework (ButtonManager, FieldManager)

**WOS Systems**:
- [[MenuManager]] - Navigation to/from login panel
- [[Network-Architecture]] - Uses auth token for multiplayer access
- WOS.Networking.Data - Auth data structures

**Backend Services**:
- Backend API (Render.com deployment)
- PostgreSQL database (player account storage)

### Used By (What Uses This)

**Menu System**:
- [[MainMenuController]] - "Play" button routes through login
- [[MenuManager]] - Shows/hides login panel

**Multiplayer System**:
- [[Network-Architecture]] - Requires valid token before connecting
- Server lobby system - Validates token on join requests

**Player Systems**:
- Player profile loading (uses stored playerId)
- Inventory synchronization (links to authenticated account)
- Progression tracking (XP, unlocks tied to account)

### Authentication API

**Stored Authentication Data** (PlayerPrefs):
```csharp
// Token storage keys
"authToken"      // JWT token string
"playerId"       // UUID string
"username"       // Player display name
```

**Usage Example**:
```csharp
// Check if player is authenticated
bool isLoggedIn = !string.IsNullOrEmpty(PlayerPrefs.GetString("authToken", ""));

// Retrieve stored credentials
string token = PlayerPrefs.GetString("authToken", "");
string playerId = PlayerPrefs.GetString("playerId", "");
string username = PlayerPrefs.GetString("username", "");

// Use token in API calls
request.SetRequestHeader("Authorization", $"Bearer {token}");
```

---

## Security Design

### Token Storage Security

**PlayerPrefs Storage**:
- **Location**: Platform-dependent (Registry on Windows, plist on macOS)
- **Security Level**: MEDIUM (obfuscated but not encrypted)
- **Risk**: Token visible to users inspecting PlayerPrefs
- **Mitigation**: Token expiration (24 hour lifetime)

**Future Enhancements** (Phase 2-3):
- Encrypted token storage using Unity Keychain
- Refresh tokens for extended sessions
- Hardware-based token storage on mobile platforms

### Password Handling

**Client-Side**:
1. Password entered in TMP_InputField (Content Type: Password)
2. Field displays dots/asterisks (hidden input)
3. Password sent to server via HTTPS (encrypted in transit)
4. Password cleared from field on error (security best practice)
5. **Password NEVER stored** on client (only username stored)

**Server-Side**:
1. Password hashed with bcrypt (industry standard)
2. Hash stored in PostgreSQL (never plaintext)
3. Login compares hashed values (secure comparison)
4. Password strength validation on registration

### Network Security

**Transport Layer**:
- **Protocol**: HTTPS (TLS 1.2+)
- **Encryption**: AES-256 for data in transit
- **Certificate**: Valid SSL certificate on backend
- **Result**: Credentials encrypted during transmission

**Request Validation**:
- Content-Type validation (must be `application/json`)
- Request size limits (prevents flooding attacks)
- Rate limiting (server-side, prevents brute force)
- CORS policy (restricts unauthorized domains)

### Common Attack Mitigations

**Brute Force Protection**:
- Server-side rate limiting (5 attempts per minute per IP)
- Account lockout after 10 failed attempts (30 minute cooldown)
- Progressive delays (increasing wait time after failures)

**SQL Injection Prevention**:
- Parameterized queries on backend (no raw SQL)
- Input sanitization (server-side validation)
- ORM usage (Sequelize library on Node.js)

**Token Theft Mitigation**:
- Token expiration (24 hour lifetime)
- HTTPS-only transmission (no plaintext tokens)
- Server-side token revocation (logout endpoint)

**Man-in-the-Middle Protection**:
- HTTPS enforced (TLS encryption)
- Certificate pinning (planned Phase 2)
- Secure token storage (no logging of tokens)

---

## Error Handling

### User-Friendly Error Messages

The system translates technical errors into actionable user guidance:

**Network Errors**:
```
ConnectionError → "Unable to connect to server. Please check your internet connection."
Timeout → "Connection timed out. Please try again."
```

**Authentication Errors**:
```
401 Unauthorized → "Invalid username or password."
409 Conflict → "Username already exists. Please choose another."
500 Server Error → "Server error. Please try again later."
```

**Validation Errors**:
```
Username too short → "Username must be at least 3 characters."
Password too short → "Password must be at least 6 characters."
Empty fields → "Please enter both username and password."
```

### Error Recovery Flow
```
1. User submits invalid credentials
2. Backend returns 401 error
3. LoginController displays: "Invalid username or password."
4. Password field automatically cleared (security)
5. Username field retains value (convenience)
6. User corrects password → Retry
```

---

## Known Issues & Limitations

### Current Limitations

**No Email Verification** 📋
- Registration requires only username + password
- No email confirmation step
- **Risk**: Spam accounts possible
- **Phase 2**: Add optional email verification

**No Password Recovery** 📋
- Forgotten password = lost account
- No "Forgot Password" flow implemented
- **Workaround**: Contact support
- **Phase 2**: Implement password reset via email

**Token Expiration Handling** ⚠️
- Token expires after 24 hours
- No automatic token refresh
- **Impact**: Player booted to login after expiration
- **Phase 2**: Implement refresh tokens

**No Two-Factor Authentication** 📋
- Single-factor authentication only (username + password)
- **Risk**: MEDIUM (accounts vulnerable to password guessing)
- **Phase 3**: Add 2FA support (TOTP/SMS)

**PlayerPrefs Security** ⚠️
- Tokens stored in PlayerPrefs (not encrypted)
- Advanced users can extract tokens
- **Risk**: LOW (tokens expire, server validates all actions)
- **Phase 2**: Encrypted storage with Unity Keychain

### Technical Debt

**Hardcoded Backend URL** ⚠️
- Backend URL hardcoded in LoginController
- Should be in ScriptableObject config
- **Priority**: LOW (works fine for now)

**No Logout Button** 📋
- Players cannot manually logout
- Token persists until expiration
- **Workaround**: Clear PlayerPrefs manually
- **Phase 2**: Add logout button to settings

**Registration Requires Immediate Login** ℹ️
- No separate registration confirmation screen
- New accounts automatically logged in
- **Impact**: No opportunity to review account details before login
- **Priority**: LOW (current flow is user-friendly)

---

## Future Enhancements

### Phase 2 Improvements
- [ ] Add email verification for new accounts
- [ ] Implement password recovery flow
- [ ] Add refresh tokens (extend session beyond 24 hours)
- [ ] Encrypted token storage (Unity Keychain)
- [ ] Logout button in settings menu
- [ ] Account settings panel (change password, email)
- [ ] Login session history (last 5 logins)

### Phase 3 Improvements
- [ ] Two-Factor Authentication (2FA) support
- [ ] Social login integration (Google, Discord, Steam)
- [ ] Account linking (multiple auth methods per account)
- [ ] Advanced security analytics (suspicious login detection)
- [ ] Guest accounts (play without registration)
- [ ] Account migration tools (transfer progress)

---

## Testing

### Test Coverage
- ✅ Login with valid credentials (success path)
- ✅ Login with invalid credentials (401 error handling)
- ✅ Registration with new username (success path)
- ✅ Registration with existing username (409 error handling)
- ✅ Network timeout handling (10 second timeout)
- ✅ Input validation (username/password requirements)
- ✅ Token storage verification (PlayerPrefs)
- ✅ UI state management (button disable during API call)
- ✅ Status message color coding (Info/Success/Error)
- ⭕ Token expiration handling (not systematically tested)
- ⭕ Concurrent login attempts (race conditions)
- ⭕ Backend API unavailability (graceful degradation)

### Test Scenarios

**Manual Test 1: Successful Login**:
1. Launch game → Navigate to Login Panel
2. Enter valid username and password
3. Click "Login" button
4. **Expected**: Status shows "Logging in..." (orange) → "Login successful!" (green) → Navigate to Join Menu
5. **Verify**: PlayerPrefs contains authToken, playerId, username
✅ **Result**: Login flow works correctly

**Manual Test 2: Invalid Credentials**:
1. Navigate to Login Panel
2. Enter invalid username or password
3. Click "Login" button
4. **Expected**: Status shows "Invalid username or password." (red) → Password field cleared
5. **Verify**: Username field retains value, password field empty
✅ **Result**: Error handling correct

**Manual Test 3: New Account Registration**:
1. Navigate to Login Panel
2. Enter new username and password (meeting validation rules)
3. Click "Register" button
4. **Expected**: Status shows "Creating account..." (orange) → "Registration successful!" (green) → Navigate to Join Menu
5. **Verify**: New account created in database, token stored
✅ **Result**: Registration flow works correctly

**Manual Test 4: Duplicate Username**:
1. Navigate to Login Panel
2. Enter existing username with any password
3. Click "Register" button
4. **Expected**: Status shows "Username already exists. Please choose another." (red)
5. **Verify**: Registration rejected, no navigation
✅ **Result**: Duplicate detection works

**Manual Test 5: Network Timeout**:
1. Disconnect from internet
2. Navigate to Login Panel
3. Attempt login
4. **Expected**: After 10 seconds, status shows "Connection timed out. Please try again." (red)
5. **Verify**: UI remains responsive, buttons re-enabled
✅ **Result**: Timeout handling correct

---

## Cross-References

### Related GDD Sections
- [[Network-Architecture]] - Uses JWT tokens for multiplayer authorization
- [[Menu-System]] - Navigation to/from login panel
- [[UI-Overview]] - MUIP framework integration
- [[Chat-System]] - Requires authentication for message sending

### Related Scripts
- [[LoginController]] - Primary authentication UI controller
- [[MenuManager]] - Panel navigation and history management
- [[ServerConfig]] - Backend API configuration
- AuthDataHelper - Token storage utilities (WOS.Networking.Data)

### External Documentation
- [JWT.io - JSON Web Tokens](https://jwt.io/)
- [Unity UnityWebRequest Documentation](https://docs.unity3d.com/ScriptReference/Networking.UnityWebRequest.html)
- [MUIP Documentation](https://michsky.com/muip/)

---

## Developer Guidelines

### Adding Authentication to New Features

**Step 1: Check if User is Authenticated**
```csharp
using WOS.Networking.Data;

bool isAuthenticated = !string.IsNullOrEmpty(PlayerPrefs.GetString("authToken", ""));

if (!isAuthenticated)
{
    Debug.LogWarning("Feature requires authentication");
    MenuManager.Instance.ShowLoginMenu(); // Redirect to login
    return;
}
```

**Step 2: Include Token in API Requests**
```csharp
string token = PlayerPrefs.GetString("authToken", "");
UnityWebRequest request = UnityWebRequest.Get("https://api.example.com/data");
request.SetRequestHeader("Authorization", $"Bearer {token}");

yield return request.SendWebRequest();

if (request.result == UnityWebRequest.Result.Success)
{
    // Process authenticated response
}
else if (request.responseCode == 401)
{
    // Token invalid or expired - redirect to login
    PlayerPrefs.DeleteKey("authToken"); // Clear invalid token
    MenuManager.Instance.ShowLoginMenu();
}
```

**Step 3: Handle Token Expiration**
```csharp
// Check for 401 Unauthorized (token expired)
if (request.responseCode == 401)
{
    Debug.LogWarning("Authentication token expired");

    // Clear stored credentials
    AuthDataHelper.ClearAuthData();

    // Notify user
    ShowMessage("Your session has expired. Please login again.");

    // Redirect to login
    MenuManager.Instance.ShowLoginMenu();
}
```

### Best Practices

**DO**:
- ✅ Always validate token existence before authenticated operations
- ✅ Handle 401 errors gracefully (redirect to login)
- ✅ Clear password fields after failed attempts (security)
- ✅ Use HTTPS for all authentication requests
- ✅ Log authentication events (login, logout, failures)

**DON'T**:
- ❌ Store passwords in PlayerPrefs (ONLY store tokens)
- ❌ Log tokens to console (security risk)
- ❌ Send tokens in URL query parameters (use headers)
- ❌ Implement custom JWT parsing (use backend validation)
- ❌ Cache authentication state in static variables (use PlayerPrefs)

---

## Changelog

- **2025-01-XX**: Initial authentication system implemented
- **2025-01-XX**: JWT token integration with backend API
- **2025-01-XX**: LoginController UI with MUIP framework
- **2025-01-XX**: Input validation and error handling
- **2025-01-XX**: Token storage using PlayerPrefs
- **2025-01-XX**: Integration with MenuManager navigation
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Core authentication complete and production-ready
**Next Steps**: Phase 2 - Password recovery and refresh tokens
**Blockers**: None
