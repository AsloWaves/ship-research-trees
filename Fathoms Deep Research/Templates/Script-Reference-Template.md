---
tags: [script, SYSTEM-TAG, implemented]
script-type: [MonoBehaviour | ScriptableObject | NetworkBehaviour]
namespace: WOS.NAMESPACE
file-path: WOS2.3V2 Research/Scripts/PATH/TO/SCRIPT.cs
status: ✅ IMPLEMENTED
size: XX KB
---

# ScriptName.cs

## Quick Reference
**Type**: [MonoBehaviour/ScriptableObject/etc]
**Namespace**: WOS.NAMESPACE
**File**: `Scripts/PATH/TO/SCRIPT.cs`
**Size**: XX KB
**Dependencies**: List key dependencies

---

## Purpose
Single-sentence description of what this script does.

Detailed explanation of the script's role in the game and why it exists.

---

## Implements GDD Features
- [[GDD-Section-1]] - Specific feature implemented
- [[GDD-Section-2]] - Specific feature implemented

---

## Key Components

### Public Properties
```
propertyName (type): Description of what this property does
anotherProperty (type): Description
```

### Public Methods
- `MethodName(params)` - What this method does
- `AnotherMethod(params)` - What this method does

### Key Private Methods
- `PrivateMethod()` - Important internal logic explanation

---

## Configuration

### Inspector Fields
List of serialized fields visible in Unity Inspector:
```
[Header("Category Name")]
fieldName (type, default): Description
anotherField (type, default): Description
```

### ScriptableObject Dependencies
If this script uses ScriptableObjects, list them:
- ConfigSO - What configuration it provides

---

## Integration Points

### Dependencies (What This Needs)
- Unity Package/System - Why it's needed
- Other Scripts - How they're used

### Used By (What Uses This)
- [[Other-Script-1]] - How it uses this script
- [[Other-Script-2]] - How it uses this script

---

## Technical Details

### Performance Considerations
- Update frequency (Update, FixedUpdate, LateUpdate?)
- Memory allocations per frame
- Optimization notes

### Network Behavior (if applicable)
- Client-side only / Server-side only / Both
- Network messages sent/received
- Sync variables

---

## How It Works

### Initialization
Explain what happens in Awake/Start.

### Main Loop
Explain what happens in Update/FixedUpdate.

### Key Algorithms
Explain any important calculations or logic.

---

## Example Usage
```csharp
// How to use this script from other code
ScriptName instance = GetComponent<ScriptName>();
instance.PublicMethod(parameters);
```

---

## Related Files
- [[Related-Script-1]] - How they relate
- [[Related-Script-2]] - How they relate
- [[GDD-Design-Doc]] - Design specification
- AssetName.asset - Related ScriptableObject assets

---

## Testing Notes
- What has been tested
- Known edge cases
- Test scenarios

---

## Changelog
- **YYYY-MM-DD**: Initial implementation
- **YYYY-MM-DD**: Added feature X
- **YYYY-MM-DD**: Fixed bug Y
