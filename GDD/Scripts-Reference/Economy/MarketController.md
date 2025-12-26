---
tags: [script, economy, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Economy.Controllers
file-path: Assets/Scripts/Economy/Controllers/MarketController.cs
status: IMPLEMENTED
size: ~439 lines
feature-group: economy
---

# MarketController.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton)
**Namespace**: WOS.Economy.Controllers
**File**: `Assets/Scripts/Economy/Controllers/MarketController.cs`
**Size**: ~439 lines
**Dependencies**: EconomyData, Mirror, WOS.Debugging

---

## Purpose
Server-authoritative market and trading system. Handles NPC market prices, player listings, supply/demand dynamics, and transactions. Based on GDD Economy-System.md specifications.

---

## Singleton Access

```csharp
private static MarketController _instance;
public static MarketController Instance => _instance;
```

---

## Configuration

```csharp
[Header("Market Configuration")]
[SerializeField] private float priceUpdateInterval = 300f;  // 5 minutes
[SerializeField] private float transactionFeePercent = 5f;
[SerializeField] private float listingFeePercent = 2f;
[SerializeField] private float listingDurationHours = 48f;

[Header("Limits")]
[SerializeField] private int maxActiveListingsPerPlayer = 20;
[SerializeField] private int maxPriceHistoryDays = 30;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Events

```csharp
public event Action<MarketPrice> OnPriceUpdated;
public event Action<MarketListing> OnListingCreated;
public event Action<MarketListing> OnListingSold;
public event Action<string> OnListingCancelled;
public event Action<string, string, long> OnTransactionComplete;  // buyerId, itemId, amount
```

---

## Price System

### Price Updates

```csharp
[Server]
private void UpdateMarketPrices()
{
    foreach (var price in marketPrices.Values)
    {
        // Calculate supply/demand influence
        float supplyDemandModifier = 1f;
        if (price.demandLevel > 0 && price.supplyLevel > 0)
        {
            supplyDemandModifier = (float)price.demandLevel / price.supplyLevel;
            supplyDemandModifier = Mathf.Clamp(supplyDemandModifier, 0.5f, 2f);
        }

        // Add random volatility
        float volatility = UnityEngine.Random.Range(
            -price.priceVolatility / 100f,
            price.priceVolatility / 100f
        );

        price.currentPriceMultiplier = supplyDemandModifier * (1f + volatility);
        price.currentPriceMultiplier = Mathf.Clamp(price.currentPriceMultiplier, 0.25f, 4f);

        OnPriceUpdated?.Invoke(price);
    }
}
```

### Price Queries

```csharp
public MarketPrice GetPrice(string itemId);
public long GetBuyPrice(string itemId, int quantity);
public long GetSellPrice(string itemId, int quantity);
```

---

## NPC Market Transactions

### Buy from Market

```csharp
[Command(requiresAuthority = false)]
public void CmdBuyFromMarket(string itemId, int quantity, NetworkConnectionToClient sender = null)
{
    long totalPrice = GetBuyPrice(itemId, quantity);

    // Update supply
    var price = GetPrice(itemId);
    if (price != null)
    {
        price.supplyLevel -= quantity;
    }

    // TODO: Validate currency, give items, deduct currency
    RpcNotifyTransaction(connectionId, itemId, quantity, totalPrice, isBuy: true);
}
```

### Sell to Market

```csharp
[Command(requiresAuthority = false)]
public void CmdSellToMarket(string itemId, int quantity, NetworkConnectionToClient sender = null)
{
    long totalPrice = GetSellPrice(itemId, quantity);

    // Update supply
    var price = GetPrice(itemId);
    if (price != null)
    {
        price.supplyLevel += quantity;
    }

    // TODO: Validate items, remove items, add currency
    RpcNotifyTransaction(connectionId, itemId, quantity, totalPrice, isBuy: false);
}
```

---

## Player Listings

### Create Listing

```csharp
[Command(requiresAuthority = false)]
public void CmdCreateListing(string itemId, int quantity, long askingPrice, string currencyId,
    NetworkConnectionToClient sender = null)
{
    // Check listing limit
    if (playerListings >= maxActiveListingsPerPlayer) return;

    // Calculate listing fee (2%)
    long listingFee = (long)(askingPrice * (listingFeePercent / 100f));

    var newListing = new MarketListing
    {
        listingId = Guid.NewGuid().ToString(),
        sellerId = playerId,
        itemId = itemId,
        quantity = quantity,
        askingPrice = askingPrice,
        currencyId = currencyId,
        listingTime = DateTime.UtcNow,
        expirationTime = DateTime.UtcNow.AddHours(listingDurationHours),
        status = ListingStatus.Active,
        listingFee = listingFee,
        transactionFeePercent = transactionFeePercent
    };

    activeListings.Add(newListing);
    OnListingCreated?.Invoke(newListing);
}
```

### Purchase Listing

```csharp
[Command(requiresAuthority = false)]
public void CmdPurchaseListing(string listingId, NetworkConnectionToClient sender = null)
{
    var listing = activeListings.Find(l => l.listingId == listingId);
    if (listing == null || listing.status != ListingStatus.Active) return;

    // Can't buy own listing
    if (listing.sellerId == buyerId) return;

    // Calculate fees (5% transaction fee)
    long transactionFee = (long)(listing.askingPrice * (transactionFeePercent / 100f));
    long sellerReceives = listing.askingPrice - transactionFee;

    // TODO: Deduct from buyer, give to seller, transfer items

    listing.status = ListingStatus.Sold;
    OnListingSold?.Invoke(listing);
    OnTransactionComplete?.Invoke(buyerId, listing.itemId, listing.askingPrice);
}
```

### Cancel Listing

```csharp
[Command(requiresAuthority = false)]
public void CmdCancelListing(string listingId, NetworkConnectionToClient sender = null)
{
    var listing = activeListings.Find(l => l.listingId == listingId);
    if (listing == null || listing.sellerId != playerId) return;
    if (listing.status != ListingStatus.Active) return;

    listing.status = ListingStatus.Cancelled;
    // Return items to seller (listing fee NOT refunded)

    OnListingCancelled?.Invoke(listingId);
}
```

---

## Fee Structure

| Fee Type | Percentage | Notes |
|----------|------------|-------|
| Listing Fee | 2% | Paid upfront, non-refundable |
| Transaction Fee | 5% | Deducted from sale price |

---

## Price Modifiers

| Factor | Range | Effect |
|--------|-------|--------|
| Supply/Demand | 0.5x - 2.0x | Demand > Supply raises prices |
| Volatility | ± volatility% | Random daily fluctuation |
| Final Multiplier | 0.25x - 4.0x | Total price range |

---

## Public API

```csharp
public List<MarketListing> GetAllActiveListings();
public List<MarketListing> GetListingsForItem(string itemId);
public List<MarketListing> GetPlayerListings(string playerId);
public float GetTransactionFeePercent();
public float GetListingFeePercent();
```

---

## Client RPCs

```csharp
[ClientRpc] private void RpcNotifyTransaction(int connectionId, string itemId, int quantity, long price, bool isBuy);
[ClientRpc] private void RpcNotifyListingCreated(string listingId, string sellerId);
[ClientRpc] private void RpcNotifyListingSold(string listingId, string buyerId, string sellerId);
[ClientRpc] private void RpcNotifyListingCancelled(string listingId, string sellerId);
```

---

## Integration Points

### Dependencies
- [[EconomyData]] - Data structures
- Mirror networking
- WOS.Debugging

### Used By
- Market UI panels
- [[WalletManager]] - Currency transactions
- Inventory system

---

## Related Files
- [[EconomyData]] - Data structures
- [[WalletManager]] - Currency management
- [[ContractManager]] - Contract rewards

---

## Design Notes
- Server-authoritative with Singleton pattern
- Prices update every 5 minutes
- Supply/demand dynamically affects prices
- Maximum 20 active listings per player
- Listings expire after 48 hours
- Listing fee is 2%, transaction fee is 5%
- Listing fee is non-refundable on cancel
- Self-purchase is blocked
- Supply increases on sell, decreases on buy
- Price multiplier capped at 0.25x-4x range

