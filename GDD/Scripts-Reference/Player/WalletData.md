# WalletData.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/Data/WalletData.cs` |
| **Namespace** | `WOS.Player.Data` |
| **Inheritance** | None (Serializable data class) |
| **Lines of Code** | 121 |
| **Architecture** | Player currency storage with validation |

## Purpose

`WalletData` manages player currencies in the naval MMO economy. It stores both standard in-game credits (earned through gameplay) and premium currency (purchased with real money). The class provides transaction methods with built-in validation to prevent negative balances and invalid operations.

## Data Structure

### Player Identity

| Field | Type | Description |
|-------|------|-------------|
| `PlayerId` | `string` | Player ID this wallet belongs to |

### Currencies

| Field | Type | Description |
|-------|------|-------------|
| `Credits` | `long` | Standard in-game currency earned through gameplay |
| `PremiumCurrency` | `int` | Premium currency purchased with real money |

### Metadata

| Field | Type | Description |
|-------|------|-------------|
| `LastUpdated` | `string` | ISO 8601 timestamp of last wallet modification |

## Public API

### Constructors

```csharp
// Default constructor (0 credits, 0 premium)
public WalletData()
{
    PlayerId = "";
    Credits = 0;
    PremiumCurrency = 0;
    LastUpdated = DateTime.UtcNow.ToString("o");
}

// Parameterized constructor
public WalletData(string playerId, long credits, int premiumCurrency = 0)
{
    PlayerId = playerId;
    Credits = credits;
    PremiumCurrency = premiumCurrency;
    LastUpdated = DateTime.UtcNow.ToString("o");
}
```

### Credit Operations

```csharp
// Add credits (positive values only)
public void AddCredits(long amount)
{
    if (amount > 0)
    {
        Credits += amount;
        UpdateTimestamp();
    }
}

// Spend credits (validates sufficient balance)
public bool SpendCredits(long amount)
{
    if (amount <= 0) return false;
    if (Credits < amount) return false;

    Credits -= amount;
    UpdateTimestamp();
    return true;
}
```

**Design**: `AddCredits` silently ignores negative amounts, while `SpendCredits` returns `false` for invalid operations.

### Premium Currency Operations

```csharp
// Add premium currency
public void AddPremiumCurrency(int amount)
{
    if (amount > 0)
    {
        PremiumCurrency += amount;
        UpdateTimestamp();
    }
}

// Spend premium currency (validates sufficient balance)
public bool SpendPremiumCurrency(int amount)
{
    if (amount <= 0) return false;
    if (PremiumCurrency < amount) return false;

    PremiumCurrency -= amount;
    UpdateTimestamp();
    return true;
}
```

### Utility Methods

```csharp
// Update timestamp to current UTC time
public void UpdateTimestamp()
{
    LastUpdated = DateTime.UtcNow.ToString("o");
}

// Create deep copy of wallet
public WalletData Clone()
{
    return new WalletData
    {
        PlayerId = this.PlayerId,
        Credits = this.Credits,
        PremiumCurrency = this.PremiumCurrency,
        LastUpdated = this.LastUpdated
    };
}
```

## Usage Examples

### Creating a New Wallet

```csharp
// New player with starting credits
WalletData wallet = new WalletData(
    playerId: "player123",
    credits: 10000,
    premiumCurrency: 0
);
```

### Processing Transactions

```csharp
// Award match rewards
wallet.AddCredits(5000);
Debug.Log($"Credits: {wallet.Credits}");

// Purchase equipment
long equipmentCost = 150000;
if (wallet.SpendCredits(equipmentCost))
{
    Debug.Log("Purchase successful!");
}
else
{
    Debug.LogError("Insufficient credits!");
}
```

### Premium Currency Transactions

```csharp
// Player purchases premium currency
wallet.AddPremiumCurrency(1000);

// Use premium to skip research time
int skipCost = 50;
if (wallet.SpendPremiumCurrency(skipCost))
{
    Debug.Log("Research completed instantly!");
}
else
{
    Debug.LogError("Insufficient premium currency!");
}
```

### Transaction Validation Pattern

```csharp
// Safe transaction with validation
if (!wallet.SpendCredits(amount))
{
    // Handle insufficient funds
    ShowNotification($"Need {amount} credits, have {wallet.Credits}");
    return;
}

// Transaction succeeded, proceed with purchase
CompleteEquipmentPurchase(equipment);
```

## Integration Points

### Database Persistence
- **Storage**: PlayFab Player Data or local file storage
- **Sync**: Real-time synchronization for premium currency
- **Backup**: Periodic snapshots to prevent currency loss

### Related Systems

| System | Integration |
|--------|-------------|
| **Economy System** | Wallet is central currency storage |
| **Shop System** | Validates purchases against wallet balance |
| **Match Rewards** | Awards credits after combat |
| **Research System** | Deducts research costs |
| **Premium Store** | Handles premium currency transactions |
| **PlayFab** | Syncs wallet state to cloud |

## Design Notes

### Data Types

**Credits (`long`)**: Uses 64-bit integer to support large credit values (max: 9,223,372,036,854,775,807). This prevents overflow issues even for endgame players with millions of credits.

**Premium Currency (`int`)**: Uses 32-bit integer assuming premium currency amounts remain modest (max: 2,147,483,647).

### Timestamp Format

Uses **ISO 8601 format** (`"o"` format specifier) for timestamp:
- Example: `"2025-01-15T14:30:00.0000000Z"`
- Sortable, unambiguous, timezone-aware (UTC)
- Compatible with database timestamp columns

### Transaction Safety

All transaction methods have built-in validation:
1. **Positive amount check**: Prevents negative transactions
2. **Balance check**: Ensures sufficient funds before deduction
3. **Atomic update**: Balance and timestamp updated together
4. **Return value**: Indicates transaction success/failure

This prevents common bugs:
- Negative balance exploits
- Accidental credit duplication
- Inconsistent state (balance updated but timestamp not)

### Currency Separation

Separate methods for credits vs. premium currency enables:
1. **Different validation logic** (if needed in future)
2. **Separate transaction logs** for auditing
3. **Premium currency protection** (stricter security)
4. **Analytics tracking** (different metrics per currency type)

### Clone Method

Deep cloning supports:
- **UI previews** (show "what-if" scenarios without mutating real wallet)
- **Undo/redo systems** (restore previous wallet state)
- **Transaction rollback** (revert failed multi-step transactions)

### Defensive Programming

Methods ignore invalid inputs instead of throwing exceptions:
```csharp
if (amount > 0)  // Silently ignore negative amounts
{
    Credits += amount;
}
```

This prevents crashes from invalid data, but makes debugging harder. Consider adding logging for invalid operations in production.

### Thread Safety

**NOT thread-safe**. If wallet operations can occur from multiple threads, add locking:
```csharp
private readonly object _lock = new object();

public bool SpendCredits(long amount)
{
    lock (_lock)
    {
        // ... existing code
    }
}
```

### Future Enhancements

Potential additions:
1. **Transaction history**: List of all credits earned/spent
2. **Daily limits**: Cap certain transaction types
3. **Currency conversion**: Exchange credits for premium currency
4. **Soft cap**: Warn when credits exceed reasonable amounts
5. **Multi-currency**: Support additional currency types (event tokens, etc.)

### Economy Design Philosophy

The wallet represents a **pull system** where:
- Systems request to spend currency (pull)
- Wallet validates and approves (gatekeeper)
- Prevents systems from directly manipulating balance (security)

Alternative **push system** would allow systems to directly modify balance, but risks:
- Race conditions between systems
- Accidental duplicate charges
- Harder to audit transaction flow
