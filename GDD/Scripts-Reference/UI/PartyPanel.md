---
tags: [script, ui, party, implemented, phase2]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/PartyPanel.cs
status: ✅ IMPLEMENTED
size: 8.5 KB
---

# PartyPanel.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/UI/PartyPanel.cs` |
| **Namespace** | `WOS.UI` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~253 |
| **Architecture** | UI Controller with network party integration |

---

## Purpose

PartyPanel manages the UI display and interaction for the party system. Shows party members, leader indicators, member count, and provides controls for leaving, disbanding, inviting, and kicking members. Integrates with PartyManager (WOS.Party namespace) for server-authoritative party operations.

**Phase 2 Feature**: Party system UI for cooperative multiplayer gameplay.

---

## Configuration

### Inspector Fields

```csharp
[Header("UI References")]
panelContainer (GameObject): Panel container (shown when in party)
partyNameText (TextMeshProUGUI): Party name display
memberCountText (TextMeshProUGUI): Member count (e.g., "3/8 Members")
memberListScrollRect (ScrollRect): Scroll container for member list
memberListContainer (Transform): Container for member UI elements
memberPrefab (GameObject): Prefab for individual member display

[Header("Party Controls")]
leaveButton (ButtonManager): Leave party button
disbandButton (ButtonManager): Disband party (leader only)
inviteButton (ButtonManager): Invite player button

[Header("Invite UI")]
invitePlayerNameInput (TMP_InputField): Player name input for invites

[Header("References")]
partyManager (PartyManager): Reference to PartyManager component
```

### Private State

```csharp
currentPartyId (string): Current party ID
isLeader (bool): Is local player the party leader?
memberUIElements (List<GameObject>): Instantiated member UI elements
```

---

## Public API

### Display Methods

```csharp
void ShowParty(PartyData party, bool isPlayerLeader)
```
**Purpose**: Display party panel with party data
**Parameters**:
- `party`: Party data (members, name, max size)
- `isPlayerLeader`: Whether local player is leader
**Behavior**:
- Activates panel container
- Updates party name and member count
- Populates member list with leader indicators
- Shows/hides disband button based on leadership

```csharp
void HideParty()
```
**Purpose**: Hide party panel and clear state
**Behavior**:
- Deactivates panel container
- Clears current party ID and leadership flag

---

## Integration Points

### Dependencies (What This Needs)

**Unity Systems**:
- UnityEngine - GameObject, MonoBehaviour, Transform
- UnityEngine.UI - Button, Toggle, ScrollRect
- TMPro - TextMeshProUGUI for text display
- Michsky.MUIP - ButtonManager for MUIP integration

**WOS Systems**:
- `WOS.Party.PartyManager` - Network party operations (Cmd methods)
- `WOS.Party.PartyData` - Party data structure (members, leader, name)
- `WOS.Debugging.DebugManager` - Logging and diagnostics
- Mirror - NetworkClient for network connectivity checks

### Used By (What Uses This)

**Party System**:
- `PartyManager` - Calls ShowParty() when joining party
- `PartyManager` - Calls HideParty() when leaving party
- Player HUD - Panel visibility controlled by party membership

---

## How It Works

### Initialization

**Awake()**: Find PartyManager reference and hide panel initially

```csharp
private void Awake()
{
    if (partyManager == null)
        partyManager = FindFirstObjectByType<PartyManager>();

    if (panelContainer != null)
        panelContainer.SetActive(false);
}
```

**Start()**: Initialize button listeners

```csharp
private void Start()
{
    InitializeButtons();
}
```

### Member List Display

**Algorithm: UpdateMemberList(PartyData party)**

```
Input: PartyData with member IDs and leader ID

1. Destroy all existing member UI elements
2. Clear memberUIElements list

3. For each member ID in party.memberIds:
   a. Instantiate memberPrefab in memberListContainer
   b. Find TextMeshProUGUI component for name display
   c. Check if member is leader (party.IsLeader(memberId))
   d. Format name with leader icon: "⚓ Player{id}" or "Player{id}"
   e. Set name text

   f. Find ButtonManager for kick button
   g. Determine if kick allowed: isLeader && !party.IsLeader(memberId)
      - Leader can kick members (but not themselves)
      - Non-leaders cannot kick anyone
   h. Show/hide kick button based on permission
   i. Add onClick listener with lambda: () => OnKickMemberClicked(targetId)

   j. Add instantiated element to memberUIElements list

Output: Populated member list with leader icons and kick buttons
```

**Example Output**:
```
Party: "Alpha Squadron" (3/8 Members)
⚓ Player1234      [no button - leader can't kick self]
  Player5678      [Kick] - only visible if local player is leader
  Player9012      [Kick] - only visible if local player is leader
```

### Button Callbacks

**OnLeavePartyClicked()**:
```csharp
if (NetworkClient.active)
{
    partyManager.CmdLeaveParty(); // Server RPC
}
```

**OnDisbandPartyClicked()** (leader only):
```csharp
if (NetworkClient.active && isLeader)
{
    partyManager.CmdDisbandParty(); // Server RPC
}
```

**OnInvitePlayerClicked()**:
```csharp
string playerName = invitePlayerNameInput.text.Trim();
if (!string.IsNullOrWhiteSpace(playerName) && NetworkClient.active)
{
    partyManager.CmdInviteToParty(playerName); // Server RPC
    invitePlayerNameInput.text = ""; // Clear input
}
```

**OnKickMemberClicked(uint targetConnectionId)** (leader only):
```csharp
if (NetworkClient.active && isLeader)
{
    partyManager.CmdKickFromParty(targetConnectionId); // Server RPC
}
```

---

## Network Behavior

**Client-side Only**: UI controller with no network synchronization

**Server Communication**: Calls PartyManager ServerRpc methods:
- `CmdLeaveParty()` - Request to leave current party
- `CmdDisbandParty()` - Request to disband party (leader only)
- `CmdInviteToParty(string playerName)` - Request to invite player by name
- `CmdKickFromParty(uint connectionId)` - Request to kick member (leader only)

**Network Requirements**:
- `NetworkClient.active` must be true to send commands
- PartyManager validates all requests server-side

---

## Performance Considerations

- **Update Frequency**: None - event-driven only (no Update loop)
- **Memory**: Minimal overhead
  - Panel references: ~100 bytes
  - Member UI list: ~8 bytes per member (max 64 bytes for 8-member party)
- **CPU Cost**:
  - UpdateMemberList(): O(n) where n = member count
  - Instantiation: ~0.1-0.5ms per member (8 members max)
- **Optimization**: Reuses memberPrefab via Instantiate (pooling could be added)

---

## Example Usage

### Show Party When Joining

```csharp
// Called by PartyManager when player joins party
PartyData myParty = new PartyData
{
    partyId = "party-abc123",
    partyName = "Alpha Squadron",
    memberIds = new List<uint> { 1001, 1002, 1003 },
    leaderId = 1001,
    maxMembers = 8
};

bool amILeader = (localPlayerId == myParty.leaderId);
partyPanel.ShowParty(myParty, amILeader);
```

### Hide Party When Leaving

```csharp
// Called by PartyManager when player leaves/kicked
partyPanel.HideParty();
```

### Invite Flow

```
1. User types "PlayerName" in invitePlayerNameInput
2. User clicks inviteButton
3. OnInvitePlayerClicked() validates input
4. Sends CmdInviteToParty("PlayerName") to server
5. Server validates and sends invite notification to target player
6. Input field cleared for next invite
```

### Kick Flow

```
1. Leader clicks [Kick] button next to member
2. OnKickMemberClicked(targetId) called with member's connection ID
3. Sends CmdKickFromParty(targetId) to server
4. Server removes member from party
5. PartyManager updates all clients
6. Kicked player's UI shows HideParty()
7. Remaining members see updated member list
```

---

## Design Notes

### Leader Indicators

**Visual Design**:
- Leader marked with "⚓ " (anchor emoji) prefix
- Leader name displayed first in member list
- Leader has disband button (members don't)
- Leader can kick members (but not themselves)

### Network Authority

**Server-Authoritative**:
- All party operations validated server-side
- UI only sends requests via Cmd methods
- Server determines actual party state
- Prevents exploits (e.g., non-leaders kicking)

### Future Enhancements (Phase 3+)

- Party chat channel
- Party voice chat indicator
- Ready check system
- Party invite notifications panel
- Party finder/browser
- Role assignments (tank/healer/DPS)

---

## Related Files

### Core Party System
- `WOS.Party.PartyManager` - Network party manager (Cmd/Rpc methods)
- `WOS.Party.PartyData` - Party data structure
- `WOS.Party.PartyInvite` - Invite system

### UI Components
- `ChatPanel` - Party chat channel integration (Phase 2+)
- `VoiceSettingsPanel` - Party voice settings (Phase 2+)

---

## Testing Notes

### What Has Been Tested
- ✅ Show/hide panel functionality
- ✅ Member list display with leader icons
- ✅ Leave button (all members)
- ✅ Disband button (leader only visibility)
- ✅ Kick buttons (leader only visibility)
- ✅ Invite input field and validation
- ✅ Network connectivity checks before Cmd calls

### Known Edge Cases

**Case 1: Leader Leaves Party**:
```
Scenario: Party leader clicks "Leave"
Expected: Server promotes new leader, updates all clients
Status: ⚠️ Depends on PartyManager implementation
```

**Case 2: Last Member Leaves**:
```
Scenario: Solo player in party leaves
Expected: Party disbanded automatically
Status: ⚠️ Depends on PartyManager implementation
```

**Case 3: Network Disconnect During Kick**:
```
Scenario: Leader disconnects while kick request in flight
Expected: Request lost, no kick occurs (safe failure)
Status: ✅ Server handles gracefully
```

---

## Changelog

- **Phase 2**: Initial party panel implementation
- **Phase 2**: Added leader indicators and kick functionality
- **Phase 2**: Integrated with PartyManager network system
- **2025-12-20**: Documentation created

---

**Status**: ✅ Implemented (Phase 2)
**Maintenance**: Active development
**Performance**: Excellent (event-driven, minimal overhead)
