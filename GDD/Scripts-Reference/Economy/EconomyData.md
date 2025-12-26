---
tags: [script, economy, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Economy.Data
file-path: Assets/Scripts/Economy/Data/EconomyData.cs
status: IMPLEMENTED
size: ~584 lines
feature-group: economy
---

# EconomyData.cs

## Quick Reference
**Type**: Data Classes & Enums
**Namespace**: WOS.Economy.Data
**File**: `Assets/Scripts/Economy/Data/EconomyData.cs`
**Size**: ~584 lines
**Dependencies**: None (standalone data)

---

## Purpose
Core economy system data structures. Includes wallet/currency, market/trading, contracts/missions, and auction house systems. Based on GDD Economy-System.md specifications.

---

## Wallet & Currency

### PlayerWallet

```csharp
[Serializable]
public class PlayerWallet
{
    public List<CurrencyBalance> currencies;
    public List<Transaction> recentTransactions;
    public int maxTransactionHistory = 100;
}
```

**Methods**:
- `GetBalance(string currencyId)` - Returns balance for currency
- `SetBalance(string currencyId, long amount)` - Sets balance
- `AddCurrency(string currencyId, long amount, string reason)` - Adds and records
- `RemoveCurrency(string currencyId, long amount, string reason)` - Removes if affordable
- `CanAfford(string currencyId, long amount)` - Checks affordability

### CurrencyBalance

```csharp
[Serializable]
public class CurrencyBalance
{
    public string currencyId;
    public long amount;
    public long lifetimeEarned;
    public long lifetimeSpent;
}
```

### Transaction

```csharp
[Serializable]
public class Transaction
{
    public string transactionId;
    public string currencyId;
    public long amount;
    public TransactionType transactionType;
    public string reason;
    public DateTime timestamp;
    public string relatedPlayerId;      // For trades
    public string relatedItemId;        // For purchases
}
```

### TransactionType (7 types)

```csharp
public enum TransactionType
{
    Earned,             // From gameplay (combat, missions)
    Spent,              // Purchased items
    Traded,             // Player-to-player trade
    Converted,          // Currency conversion
    Reward,             // Daily/event rewards
    AdminGrant,         // Admin-given currency
    Penalty             // Lost due to penalty
}
```

---

## Market & Trading

### MarketPrice

```csharp
[Serializable]
public class MarketPrice
{
    public string itemId;
    public string itemType;

    // Current Prices
    public long buyPrice;               // Price to buy from market
    public long sellPrice;              // Price to sell to market
    public string currencyId;

    // Price History
    public float priceVolatility;       // Daily change %
    public long basePrice;              // Reference price
    public float currentPriceMultiplier = 1f;

    // Supply & Demand
    public int supplyLevel;
    public int demandLevel;
    public float supplyDemandRatio;

    // Trading Limits
    public int maxBuyQuantity;          // Max per day
    public int maxSellQuantity;         // Max per day
}
```

**Methods**:
- `CalculateBuyPrice(int quantity)` - Buy price with demand modifier
- `CalculateSellPrice(int quantity)` - Sell price with supply modifier

### MarketListing

```csharp
[Serializable]
public class MarketListing
{
    public string listingId;
    public string sellerId;
    public string sellerName;

    // Item
    public string itemId;
    public string itemType;
    public int quantity;

    // Pricing
    public long askingPrice;            // Total price
    public string currencyId;

    // Listing Info
    public DateTime listingTime;
    public DateTime expirationTime;
    public ListingStatus status;

    // Fees
    public long listingFee;             // Fee paid to list
    public float transactionFeePercent; // Fee on sale
}
```

### ListingStatus (4 states)

```csharp
public enum ListingStatus
{
    Active,
    Sold,
    Expired,
    Cancelled
}
```

### TradeOffer

```csharp
[Serializable]
public class TradeOffer
{
    public string tradeId;
    public string initiatorId;
    public string recipientId;

    // Initiator Offer
    public List<TradeItem> initiatorItems;
    public List<CurrencyOffer> initiatorCurrency;

    // Recipient Offer
    public List<TradeItem> recipientItems;
    public List<CurrencyOffer> recipientCurrency;

    // State
    public TradeStatus status;
    public DateTime createdTime;
    public DateTime expirationTime;
    public bool initiatorConfirmed;
    public bool recipientConfirmed;
}
```

### TradeStatus (7 states)

```csharp
public enum TradeStatus
{
    Pending,            // Waiting for recipient
    Negotiating,        // Both parties adjusting
    Confirmed,          // Both confirmed, executing
    Completed,          // Trade completed
    Declined,           // Recipient declined
    Cancelled,          // Initiator cancelled
    Expired             // Timed out
}
```

---

## Contracts & Missions

### ContractData

```csharp
[Serializable]
public class ContractData
{
    public string contractId;
    public string contractName;
    public string description;

    // Classification
    public ContractType contractType;
    public ContractDifficulty difficulty;
    public int tierRequirement;         // Minimum ship tier

    // Requirements
    public List<ContractObjective> objectives;
    public float timeLimit;             // Seconds, 0 = no limit
    public string requiredZone;

    // Rewards
    public List<ContractReward> rewards;
    public float xpReward;
    public float reputationReward;

    // Availability
    public string factionId;
    public int minReputationRequired;
    public bool isRepeatable;
    public float repeatCooldown;        // Hours

    // Risk
    public float failurePenaltyPercent;
    public bool hasPermadeathRisk;
}
```

### ContractObjective

```csharp
[Serializable]
public class ContractObjective
{
    public string objectiveId;
    public string description;
    public ObjectiveType objectiveType;

    // Target
    public string targetId;
    public int requiredCount;
    public int currentCount;

    // State
    public bool isOptional;
    public bool isComplete => currentCount >= requiredCount;
    public float progress;

    // Bonus Rewards
    public List<ContractReward> bonusRewards;
}
```

### ObjectiveType (18 types)

| Category | Types |
|----------|-------|
| Combat | DestroyShips, DestroyShipType, DealDamage, AssistKills |
| Delivery | DeliverCargo, TransportPassengers, DeliverToLocation |
| Exploration | VisitLocation, DiscoverArea, SurveyLocation |
| Economy | TradeCargo, EarnCurrency, BuyFromMarket, SellToMarket |
| Survival | SurviveTime, EscapeZone, ProtectTarget |
| Special | CaptureShip, SalvageWreck, RescueCrew |

### ContractDifficulty (5 tiers)

| Difficulty | Risk Level |
|------------|------------|
| Routine | Easy, low risk |
| Standard | Normal difficulty |
| Hazardous | Increased risk |
| Dangerous | High risk, high reward |
| Extreme | Maximum risk, premium rewards |

### ContractType (9 types)

| Type | Description |
|------|-------------|
| Combat | PvE/PvP combat missions |
| Delivery | Cargo/passenger transport |
| Trade | Buy low, sell high |
| Exploration | Discover locations |
| Escort | Protect target ships |
| Salvage | Recover wrecks/cargo |
| Bounty | Hunt specific players/NPCs |
| Patrol | Zone presence missions |
| Event | Limited-time special missions |

### ContractReward

```csharp
[Serializable]
public class ContractReward
{
    public RewardType rewardType;
    public string rewardId;             // Currency ID, item ID, etc.
    public int quantity;
    public float chance = 1f;           // Probability
}
```

### RewardType (7 types)

- Currency, Item, Equipment
- CrewXP, Reputation
- ShipBlueprint, ModuleBlueprint

### ActiveContract

```csharp
[Serializable]
public class ActiveContract
{
    public string instanceId;
    public string contractId;
    public string playerId;

    // Progress
    public List<ContractObjective> objectives;
    public ContractState state;

    // Timing
    public DateTime acceptedTime;
    public DateTime expirationTime;
    public float timeRemaining;

    // Outcome
    public DateTime completedTime;
    public bool wasSuccessful;
    public List<ContractReward> earnedRewards;
}
```

### ContractState (6 states)

- Available, Active, Completed
- Failed, Expired, Abandoned

---

## Auction House

### AuctionListing

```csharp
[Serializable]
public class AuctionListing
{
    public string auctionId;
    public string sellerId;

    // Item
    public string itemId;
    public string itemType;
    public int quantity;

    // Pricing
    public long startingBid;
    public long buyoutPrice;            // Instant purchase (0 = no buyout)
    public long currentBid;
    public string currentBidderId;
    public string currencyId;

    // Timing
    public DateTime startTime;
    public DateTime endTime;
    public AuctionStatus status;

    // Bid History
    public List<AuctionBid> bidHistory;
}
```

### AuctionStatus (5 states)

- Active, Sold, BoughtOut, Unsold, Cancelled

---

## Integration Points

### Dependencies
- None (standalone data)

### Used By
- [[WalletManager]] - Currency operations
- [[MarketController]] - Market transactions
- [[ContractManager]] - Contract system
- UI economy panels

---

## Related Files
- [[WalletManager]] - Currency management
- [[MarketController]] - Market system
- [[ContractManager]] - Contract system

---

## Design Notes
- Long type for currency to support large values
- Transaction history capped at 100 entries
- Supply/demand affects market prices (0.5x-2x range)
- Listing fees are non-refundable
- Transaction fees taken from sale
- Contract objectives track progress
- Difficulty multiplies rewards
- Optional objectives give bonus rewards
- Permadeath risk flag for dangerous contracts
- Auctions support bidding and buyout

