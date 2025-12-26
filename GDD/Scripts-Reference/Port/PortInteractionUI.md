---
tags: [script, port, ui, implemented]
script-type: MonoBehaviour
namespace: WOS.Port
file-path: Assets/Scripts/Port/UI/PortInteractionUI.cs
status: IMPLEMENTED
size: ~131 lines
feature-group: port
---

# PortInteractionUI.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Port
**File**: `Assets/Scripts/Port/UI/PortInteractionUI.cs`
**Size**: ~131 lines
**Dependencies**: TextMeshProUGUI

---

## Purpose
UI controller for port interaction prompts. Shows context-sensitive prompts like "Press E to Enter Port", "Press E to Dock", and "Press E to Leave Harbor".

---

## Configuration

```csharp
[SerializeField] private GameObject promptPanel;
[SerializeField] private TextMeshProUGUI promptText;
[SerializeField] private string enterPortPrompt = "Press E to Enter {0}";
[SerializeField] private string dockPrompt = "Press E to Dock";
[SerializeField] private string exitHarborPrompt = "Press E to Leave Harbor";
```

---

## Public Methods

```csharp
public void ShowEnterPortPrompt(string portName);
public void HideEnterPortPrompt();
public void ShowDockPrompt();
public void HideDockPrompt();
public void ShowExitHarborPrompt();
public void HideAllPrompts();
```

---

## Prompt Summary

| State | Prompt |
|-------|--------|
| Ocean_InAoI | "Press E to Enter {PortName}" |
| Harbor_InDockZone | "Press E to Dock" |
| Harbor_AtExitZone | "Press E to Leave Harbor" |

---

## Integration Points

### Used By
- [[PortZoneManager]], [[HarborSceneManager]]

