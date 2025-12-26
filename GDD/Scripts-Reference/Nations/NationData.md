# NationData.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Nations/NationData.cs` |
| **Namespace** | `WOS.Nations` |
| **Lines** | ~40 |
| **Architecture** | Data structures for nation/faction system |

## Purpose
Defines data structures for the nation/faction system used for PvP rules, diplomacy, and faction-specific gameplay.

---

## NationData Struct

```csharp
[Serializable]
public struct NationData
{
    public NationID nationId;       // Nation identifier
    public string nationName;       // Display name
    public Color nationColor;       // UI color
    public string description;      // Nation description
    public Sprite nationFlag;       // Flag sprite

    public NationData(NationID id, string name, Color color);
}
```

---

## NationID Enum

```csharp
public enum NationID
{
    None = 0,       // No nation (neutral)
    Nation1 = 1,    // Placeholder: "Allies"
    Nation2 = 2,    // Placeholder: "Axis"
    Nation3 = 3,    // Placeholder: "Neutral"
    Pirate = 99     // Pirate faction
}
```

---

## Default Nations

| ID | Name | Color | Description |
|----|------|-------|-------------|
| Nation1 | Allies | Blue (0.2, 0.6, 1.0) | Allied forces |
| Nation2 | Axis | Red (1.0, 0.2, 0.2) | Axis powers |
| Nation3 | Neutral | Gray (0.8, 0.8, 0.8) | Neutral nations |
| Pirate | Pirates | - | Outlaw faction |

---

## Usage Example

```csharp
// Create nation data
NationData allies = new NationData(
    NationID.Nation1,
    "Allies",
    new Color(0.2f, 0.6f, 1f)
);

// Use in UI
nameLabel.text = allies.nationName;
nameLabel.color = allies.nationColor;

// Check nation
if (playerNationId == NationID.Pirate)
    Debug.Log("Yarr, ye be a pirate!");
```

---

## Integration Points

### Used By
- `NationManager` - Nation assignment and relations
- UI systems - Faction colors and icons

---

## Design Notes

### Placeholder System
- Phase 4 feature (disabled by default)
- Nation names/descriptions are placeholders
- Ready for historical/fantasy expansion

### Pirates
- Special faction (ID 99)
- Enemies with all nations
- Neutral among themselves
