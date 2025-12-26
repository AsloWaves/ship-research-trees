---
tags: [script, economy, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Economy.Controllers
file-path: Assets/Scripts/Economy/Controllers/WalletManager.cs
status: IMPLEMENTED
size: ~347 lines
feature-group: economy
---

# WalletManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton)
**Namespace**: WOS.Economy.Controllers
**File**: `Assets/Scripts/Economy/Controllers/WalletManager.cs`
**Size**: ~347 lines
**Dependencies**: EconomyData, Mirror, WOS.Debugging

---

## Purpose
Server-authoritative player wallet and currency management. Handles currency transactions, validation, rate limiting, combat rewards, and persistence. Based on GDD Economy-System.md specifications.

---

## Singleton Access

```csharp
private static WalletManager _instance;
public static WalletManager Instance => _instance;
```

---

## Configuration

```csharp
[Header("Currency Configuration")]
[SerializeField] private string defaultCurrencyId = "credits";
[SerializeField] private long startingCredits = 10000;

[Header("Transaction Limits")]
[SerializeField] private long maxTransactionAmount = 999999999;
[SerializeField] private int maxTransactionsPerMinute = 60;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Synced State

```csharp
[SyncVar(hook = nameof(OnWalletChanged))]
private PlayerWallet playerWallet;
```

---

## Events

```csharp
public event Action<string, long, long> OnCurrencyChanged;  // currencyId, oldAmount, newAmount
public event Action<Transaction> OnTransactionComplete;
public event Action<string, string> OnTransactionFailed;    // currencyId, reason
```

---

## Initialization

```csharp
[Server]
private void InitializeWallet()
{
    playerWallet = new PlayerWallet();

    // Add starting credits
    playerWallet.currencies.Add(new CurrencyBalance
    {
        currencyId = defaultCurrencyId,
        amount = startingCredits
    });
}

[Server]
public void LoadWallet(string playerId, PlayerWallet savedWallet)
{
    playerWallet = savedWallet ?? new PlayerWallet();
}
```

---

## Currency Operations

### Query Methods

```csharp
public long GetBalance(string currencyId = null)
{
    currencyId ??= defaultCurrencyId;
    return playerWallet?.GetBalance(currencyId) ?? 0;
}

public bool CanAfford(long amount, string currencyId = null)
{
    currencyId ??= defaultCurrencyId;
    return GetBalance(currencyId) >= amount;
}
```

### Add Currency (Server)

```csharp
[Server]
public bool AddCurrency(long amount, string currencyId = null, string reason = "")
{
    if (amount <= 0 || amount > maxTransactionAmount) return false;

    currencyId ??= defaultCurrencyId;

    long oldBalance = GetBalance(currencyId);
    bool success = playerWallet.AddCurrency(currencyId, amount, reason);

    if (success)
    {
        long newBalance = GetBalance(currencyId);
        OnCurrencyChanged?.Invoke(currencyId, oldBalance, newBalance);
        RpcNotifyCurrencyChanged(currencyId, oldBalance, newBalance);
    }

    return success;
}
```

### Remove Currency (Server)

```csharp
[Server]
public bool RemoveCurrency(long amount, string currencyId = null, string reason = "")
{
    if (amount <= 0 || amount > maxTransactionAmount) return false;

    currencyId ??= defaultCurrencyId;

    if (!CanAfford(amount, currencyId))
    {
        OnTransactionFailed?.Invoke(currencyId, "Insufficient funds");
        return false;
    }

    long oldBalance = GetBalance(currencyId);
    bool success = playerWallet.RemoveCurrency(currencyId, amount, reason);

    if (success)
    {
        long newBalance = GetBalance(currencyId);
        OnCurrencyChanged?.Invoke(currencyId, oldBalance, newBalance);
        RpcNotifyCurrencyChanged(currencyId, oldBalance, newBalance);
    }

    return success;
}
```

### Transfer Currency (Command)

```csharp
[Command]
public void CmdTransferCurrency(string targetPlayerId, long amount, string currencyId)
{
    // Rate limiting check
    if (!CheckTransactionLimit(connectionId))
    {
        OnTransactionFailed?.Invoke(currencyId, "Transaction limit exceeded");
        return;
    }

    // TODO: Validate target player, process transfer
}
```

---

## Rate Limiting

```csharp
[Server]
private bool CheckTransactionLimit(string playerId)
{
    if (!transactionCounts.TryGetValue(playerId, out int count))
    {
        transactionCounts[playerId] = 0;
    }

    if (count >= maxTransactionsPerMinute)
    {
        return false;
    }

    transactionCounts[playerId] = count + 1;
    return true;
}
```

Transaction counts reset every 60 seconds.

---

## Combat Rewards

```csharp
[Server]
public void AwardCombatReward(float damage, bool isKill, int targetTier)
{
    long reward = CalculateCombatReward(damage, isKill, targetTier);
    AddCurrency(reward, defaultCurrencyId, isKill ? "Enemy destroyed" : "Combat damage");
}

private long CalculateCombatReward(float damage, bool isKill, int targetTier)
{
    float baseReward = damage * 0.5f;  // 0.5 credits per damage point

    // Kill bonus (2x)
    if (isKill) baseReward *= 2f;

    // Tier multiplier (1.0 + tier * 0.2)
    float tierMultiplier = 1f + (targetTier * 0.2f);
    baseReward *= tierMultiplier;

    return (long)Mathf.Max(1, baseReward);
}
```

### Combat Reward Formula

| Factor | Value |
|--------|-------|
| Base | damage * 0.5 credits |
| Kill Bonus | 2x multiplier |
| Tier Bonus | +20% per tier |
| Minimum | 1 credit |

**Example**: 1000 damage kill on Tier 3 target = `1000 * 0.5 * 2 * 1.6 = 1,600 credits`

---

## Transaction Limits

| Limit | Value |
|-------|-------|
| Max Transaction | 999,999,999 |
| Max per Minute | 60 |
| Starting Credits | 10,000 |

---

## Public API

```csharp
public PlayerWallet GetWallet();
public string GetDefaultCurrencyId();
public List<Transaction> GetRecentTransactions();
```

---

## Client RPCs

```csharp
[ClientRpc]
private void RpcNotifyCurrencyChanged(string currencyId, long oldAmount, long newAmount);
```

---

## Network Callbacks

```csharp
private void OnWalletChanged(PlayerWallet oldWallet, PlayerWallet newWallet)
{
    // Client-side wallet update notification
}
```

---

## Integration Points

### Dependencies
- [[EconomyData]] - PlayerWallet, Transaction
- Mirror networking
- WOS.Debugging

### Used By
- [[MarketController]] - Purchase transactions
- [[ContractManager]] - Currency rewards
- Combat system - Damage rewards
- UI wallet display

---

## Related Files
- [[EconomyData]] - Data structures
- [[MarketController]] - Market transactions
- [[ContractManager]] - Contract rewards

---

## Design Notes
- Server-authoritative with Singleton pattern
- SyncVar for wallet synchronization
- Default currency is "credits"
- Players start with 10,000 credits
- Rate limiting: 60 transactions per minute
- Max single transaction: ~1 billion
- Combat rewards: 0.5 credits per damage
- Kill bonus doubles reward
- Tier bonus adds 20% per tier
- Null currencyId defaults to "credits"
- Transaction history in PlayerWallet
- Insufficient funds triggers failure event

