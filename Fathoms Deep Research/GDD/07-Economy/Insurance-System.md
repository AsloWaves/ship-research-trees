---
title: Insurance System
category: economy
description: Crew and ship insurance mechanics - providers, costs, claims, and recovery
version: 1.0
last_updated: 2025-12-11
tags: [insurance, economy, permadeath, recovery, crew]
status: CONFIRMED
---

# Insurance System

> Insurance is the only path to recovering permadead crew. It's not a safety net - it's a calculated investment against catastrophic loss.

## Design Philosophy

The insurance system creates meaningful economic gameplay through:

1. **Risk Mitigation** - Reduce but never eliminate permadeath impact
2. **Economic Tradeoff** - Insurance costs vs. replacement costs
3. **Player Services** - Player-run insurance creates economic gameplay
4. **Time Investment** - Processing delays prevent instant recovery

---

## Core Mechanics

### What Can Be Insured

| Asset Type | Insurable | Notes |
|------------|-----------|-------|
| Crew Cards | YES | Primary insurance target |
| Ships | YES | Hull and structure |
| Modules | YES | Installed equipment |
| Cargo/Loot | NO | Never insurable - creates extraction tension |

**CONFIRMED**: Cargo cannot be insured. Losing cargo is always permanent.

---

## Insurance Providers

### Dual Provider System

**CONFIRMED**: Both NPC and Player-run insurance available.

#### NPC Insurance Companies

Fixed-rate insurance always available at ports:
- Standard rates (baseline pricing)
- Guaranteed payout
- No negotiation
- Always available

**Example NPC Providers**:
- Lloyd's of the Seven Seas (general coverage)
- Pacific Maritime Assurance (regional specialty)
- Imperial Naval Insurance (nation-specific bonuses)

#### Player-Run Insurance

Player organizations can offer insurance services:
- Competitive rates (undercut or premium)
- Custom coverage terms
- Risk of fraud/default
- Economic gameplay opportunity

**Player Insurance Features**:
- Insurance guilds can form
- Set custom premiums
- Build claim reserves
- Risk underwriting as gameplay
- Potential for scams (buyer beware)

---

## Premium Costs

### Cost Calculation

**CONFIRMED**: Insurance costs scale with crew level.

```
Premium_Cost = Base_Rate × Level_Multiplier × Coverage_Type_Modifier

Level_Multiplier = 1.0 + (Crew_Level × 0.02)
```

### Premium Examples by Crew Level

| Crew Level | Level Multiplier | Approximate Monthly Premium |
|------------|------------------|----------------------------|
| 1-25 | 1.0-1.5× | 1,000 - 3,000 credits |
| 26-50 | 1.5-2.0× | 3,000 - 8,000 credits |
| 51-100 | 2.0-3.0× | 8,000 - 25,000 credits |
| 101-150 | 3.0-4.0× | 25,000 - 75,000 credits |
| 151-200 | 4.0-5.0× | 75,000 - 200,000 credits |

**Note**: These are representative ranges. Actual costs depend on provider, coverage type, and market conditions.

### Coverage Types

| Coverage | Cost Modifier | What It Covers |
|----------|---------------|----------------|
| Crew Only | 1.0× | Crew card recovery |
| Ship + Crew | 1.5× | Both ship and crew |
| Full Fleet | 2.0× | All ships and crew in fleet |
| Module Rider | +0.2× | Adds module coverage |

---

## Claims Process

### Claim Trigger

Insurance claim activates when:
1. Ship is destroyed (permadeath roll fails)
2. Crew card permadeaths (individual card roll fails)
3. Module is destroyed (if module coverage purchased)

### Processing Time

**CONFIRMED**: Claims take real-world days to process.

```
Processing_Time = Base_Days + Queue_Modifier

Base_Days: 1-3 days (standard)
Queue_Modifier: 0-2 additional days during high-volume periods
```

| Provider Type | Processing Time |
|---------------|-----------------|
| NPC Standard | 2-3 days |
| NPC Premium | 1-2 days |
| Player Guild | Variable (1-5 days based on guild) |

**Design Rationale**: Processing time prevents instant respawn of veteran crews. It creates meaningful downtime after major losses.

### Claim Result

**CONFIRMED**: Insurance returns same stats and level, but different identity.

When a crew card is claimed:
```yaml
Original_Crew:
  name: "Captain Tanaka"
  level: 175
  stats: {accuracy: 45, reload: 42, repair: 38, endurance: 40}
  classification: Main_Battery_Specialist
  service_history: [battles, kills, achievements]

Recovered_Crew:
  name: "NEW RANDOM NAME"  # Different identity
  level: 175              # Same level preserved
  stats: {accuracy: 45, reload: 42, repair: 38, endurance: 40}  # Same stats
  classification: Main_Battery_Specialist  # Same classification
  service_history: []     # Reset - new person
```

**What Changes**:
- Name (new random generation)
- Portrait (new appearance)
- Service history (reset to empty)
- Achievements (lost)

**What Stays**:
- Level
- All stats
- Classification and specializations
- Trained skills

### Claim Limits

**CONFIRMED**: Unlimited coverage - players can insure as many crews as they want.

- No per-crew claim limit
- No cooldown between claims
- Multiple simultaneous claims allowed
- Each claim processes independently

---

## Ship Insurance

### Ship Recovery

When a ship is insured and destroyed:
- Hull type returned (same class)
- Quality rating: Random within standard range (not guaranteed same quality)
- Modules: NOT included unless module rider purchased
- Processing: Same timeline as crew

### Module Coverage

Optional module rider covers installed equipment:
- Each module rolled for recovery (70% chance)
- Recovered modules: Same type, random quality
- Lost modules: Must be reacquired

---

## Economic Implications

### When to Insure

**High Value (Always Insure)**:
- Level 100+ crew cards
- Rare/legendary crew
- Expensive ship classes
- Before high-tier expeditions (T6+)

**Moderate Value (Consider)**:
- Level 50-100 crew
- Standard ship classes
- Medium-tier expeditions (T4-5)

**Low Value (Skip)**:
- Level 1-50 crew (cheap to replace)
- Expendable ships
- Training missions

### Cost-Benefit Analysis

```
Insurance_Value = Replacement_Cost × Permadeath_Chance - Premium_Cost

If Insurance_Value > 0: Insurance is economically justified
```

**Example**:
- Level 150 crew replacement cost: ~500,000 credits (time + training)
- T8 permadeath chance: 50%
- Expected loss: 250,000 credits
- Premium cost: 75,000 credits
- Insurance value: 175,000 credits → WORTH IT

### Market Dynamics

Player-run insurance creates economic gameplay:
- Competitive premium pricing
- Risk pool management
- Reinsurance between guilds
- Fraud investigation gameplay
- Actuarial analysis for pricing

---

## Insurance Fraud Prevention

### NPC Safeguards

- Premium must be paid before expedition
- Cannot insure mid-combat
- Cooldown after policy purchase (24 hours before active)
- Claim verification (automatic)

### Player Guild Safeguards

- Escrow systems for claim reserves
- Reputation systems for guilds
- Public claim history
- Guild rating systems

---

## Integration with Permadeath

### Permadeath Percentages (Reference)

| Ship Tier | Permadeath Chance | Insurance Recommendation |
|-----------|-------------------|--------------------------|
| T1-T5 | 0% | Not needed (no permadeath) |
| T6 | 10% | Optional for valuable crews |
| T7 | 25% | Recommended for invested crews |
| T8 | 50% | Strongly recommended |
| T9 | 75% | Essential |
| T10 | 100% | Mandatory if you want anything back |

### Per-Card Rolling

**CONFIRMED**: Permadeath rolls are per-card, not ship-wide.

- Each crew card rolls independently
- Some cards may permadeath while others survive
- Insurance claim filed for each permadead card separately
- Processing runs in parallel

---

## User Interface

### Insurance Management Screen

```
╔═══════════════════════════════════════════════════════════╗
║                    INSURANCE MANAGEMENT                     ║
╠═══════════════════════════════════════════════════════════╣
║  ACTIVE POLICIES                                            ║
║  ┌─────────────────────────────────────────────────────┐   ║
║  │ Crew: Capt. Yamamoto (Lv.175) │ Premium: 180k/mo    │   ║
║  │ Status: ACTIVE               │ Provider: Lloyd's    │   ║
║  └─────────────────────────────────────────────────────┘   ║
║                                                             ║
║  PENDING CLAIMS                                             ║
║  ┌─────────────────────────────────────────────────────┐   ║
║  │ Crew: Lt. Tanaka (Lv.142)    │ Est. Delivery: 2d 4h │   ║
║  │ Claim Filed: 2025-12-11      │ Status: PROCESSING   │   ║
║  └─────────────────────────────────────────────────────┘   ║
║                                                             ║
║  [New Policy]  [View Claims]  [Provider Directory]          ║
╚═══════════════════════════════════════════════════════════╝
```

### Claim Delivery

When claim completes:
- Notification sent to player
- Recovered asset delivered to mailbox
- Player must collect from port

---

## Cross-References

- [[Permadeath-System]] - Complete permadeath mechanics
- [[Crew-System]] - Crew card progression and value
- [[Economy-System]] - Overall economic framework
- [[Guild-System]] - Player organization features
- [[Extraction-Mechanics]] - Why cargo isn't insurable

---

## Changelog

- **2025-12-11**: Initial document creation from Q&A session
  - Confirmed: NPC + Player-run dual provider system
  - Confirmed: Level-based premium scaling
  - Confirmed: Same stats/level returned, different identity
  - Confirmed: Processing takes days (real-time)
  - Confirmed: No cargo insurance
  - Confirmed: Unlimited coverage (no claim limits)
