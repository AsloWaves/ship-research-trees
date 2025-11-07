# German Navy Battleship Research Tree (1890-1945)

## Era Overview

| Era | Years | Key Innovation | Classes | Ships |
|-----|-------|----------------|---------|-------|
| **Pre-Dreadnoughts (Kaiserliche Marine)** | 1890-1908 | Modern steel battleships | 5 classes | 24 ships |
| **Dreadnoughts (Kaiserliche Marine)** | 1908-1916 | All-big-gun battleships | 4 classes | 17 ships |
| **Super-Dreadnoughts (Kaiserliche Marine)** | 1915-1918 | 15-inch gun battleships | 1 class | 2 ships (4 planned) |
| **Battlecruisers (Kaiserliche Marine)** | 1909-1918 | Speed and firepower | 5 classes | 9 ships (13 planned) |
| **Interwar Gap (Treaty of Versailles)** | 1919-1931 | No battleships allowed | 0 classes | 0 ships |
| **Pocket Battleships (Kriegsmarine)** | 1931-1936 | Treaty circumvention | 1 class | 3 ships |
| **Battlecruisers (Kriegsmarine)** | 1936-1939 | Fast battleships | 1 class | 2 ships |
| **Battleships (Kriegsmarine)** | 1939-1941 | 15-inch gun battleships | 1 class | 2 ships |
| **Planned (Never Built)** | 1939-1945 | H-class super-battleships | 5+ designs | 0 ships |

**Total:** ~20+ major classes, ~57+ battleships and battlecruisers built (79+ planned)

## Production Summary

| Type | Classes | Total Ships | Peak Era |
|------|---------|-------------|----------|
| Pre-Dreadnoughts (Kaiserliche Marine) | 5 | 24 ships | 1890-1908 |
| Dreadnoughts (Kaiserliche Marine) | 4 | 17 ships | 1908-1916 |
| Super-Dreadnoughts (Kaiserliche Marine) | 1 | 2 ships (4 planned) | 1915-1918 |
| Battlecruisers (Kaiserliche Marine) | 5 | 9 ships (13 planned) | 1909-1918 |
| Pocket Battleships (Kriegsmarine) | 1 | 3 ships | 1931-1936 |
| Battlecruisers (Kriegsmarine) | 1 | 2 ships | 1936-1939 |
| Battleships (Kriegsmarine) | 1 | 2 ships | 1939-1941 |
| Planned H-class (Never Built) | 6+ | 0 ships | 1939-1945 |
| **Grand Total (Built)** | **18** | **~59** | **55 years** |
| **Grand Total (Planned)** | **24+** | **~79+** | **55 years** |

## Research Tree Diagram

```mermaid
graph TD
    PRE[Pre-Dreadnoughts 1890-1908<br/>24 ships] --> NASS[Nassau 1908<br/>First dreadnoughts<br/>4 ships]

    NASS --> HELG[Helgoland 1909<br/>12" guns<br/>4 ships]
    HELG --> KAIS[Kaiser 1911<br/>Superfiring<br/>5 ships]
    KAIS --> KOEN[König 1913<br/>4 ships]
    KOEN --> BAY[Bayern 1915<br/>15" guns<br/>2 ships]

    NASS -.-> VDT[Von der Tann 1909<br/>First battlecruiser]
    VDT --> MOLT[Moltke 1910<br/>2 ships]
    MOLT --> SEYD[Seydlitz 1912<br/>1 ship]
    SEYD --> DERF[Derfflinger 1913<br/>3 ships]
    DERF --> MACK[Mackensen 1917<br/>INCOMPLETE<br/>4 planned]

    BAY --> TREATY[Treaty of Versailles 1919<br/>12-YEAR GAP]
    MACK --> TREATY

    TREATY --> DEUT[Deutschland 1931<br/>Pocket battleships<br/>3 ships]
    DEUT --> SCHAR[Scharnhorst 1936<br/>Fast battleships<br/>2 ships]
    SCHAR --> BISM[Bismarck 1939<br/>15" guns<br/>2 ships]
    BISM --> H39[H-class 1939<br/>PLANNED ONLY<br/>16" guns+]

    style NASS fill:#f00,color:#fff
    style BAY fill:#0f0,color:#000
    style DERF fill:#ff0,color:#000
    style TREATY fill:#999,color:#fff
    style BISM fill:#00f,color:#fff
    style H39 fill:#f0f,color:#fff
```

## Major Milestones

### Technological Firsts

| Achievement | Class/Ship | Year |
|-------------|------------|------|
| **First modern battleships** | Brandenburg | 1891 |
| **First dreadnoughts** | Nassau | 1908 |
| **First battlecruiser** | Von der Tann | 1909 |
| **First superfiring layout** | Kaiser | 1911 |
| **First 15-inch guns** | Bayern | 1915 |
| **Treaty circumvention (pocket battleships)** | Deutschland | 1931 |
| **Diesel propulsion battleship** | Deutschland | 1931 |
| **Last battleships completed** | Bismarck | 1940 |

### Historical Context

**Kaiserliche Marine (Imperial German Navy) 1871-1918:**
- Built to challenge British naval supremacy
- Tirpitz's naval laws (1898, 1900, 1906, 1908, 1912)
- Anglo-German naval arms race 1906-1914
- Battle of Jutland (1916) - largest battleship engagement
- Scuttled High Seas Fleet at Scapa Flow (1919)

**Versailles Treaty Gap (1919-1933):**
- Germany forbidden battleships >10,000 tons
- Limited to 6 pre-dreadnought coast defense ships
- Secret rearmament and planning began 1920s
- Pocket battleships exploited treaty loopholes

**Kriegsmarine (Nazi German Navy) 1935-1945:**
- Treaty repudiation and rapid rearmament (1935+)
- Plan Z (1939) - massive fleet expansion (never realized)
- WWII surface operations (1939-1945)
- Bismarck sunk 1941, Tirpitz destroyed 1944
- H-class designs increasingly fantastical (up to 141,500 tons planned)

## Timeline

```mermaid
graph LR
    A[1908<br/>Nassau<br/>First dreadnought] --> B[1909<br/>Von der Tann<br/>First battlecruiser]
    B --> C[1911<br/>Kaiser<br/>Superfiring]
    C --> D[1915<br/>Bayern<br/>15" guns]
    D --> E[1919<br/>Treaty of Versailles<br/>12-year gap]
    E --> F[1931<br/>Deutschland<br/>Pocket battleship]
    F --> G[1936<br/>Scharnhorst<br/>Fast battleship]
    G --> H[1940<br/>Bismarck<br/>Last completed]

    style A fill:#f00,stroke:#333,stroke-width:4px,color:#fff
    style D fill:#0f0,stroke:#333,stroke-width:4px
    style E fill:#999,stroke:#333,stroke-width:4px,color:#fff
    style H fill:#00f,stroke:#fff,stroke-width:4px,color:#fff
```

## Class Listing by Era

### Kaiserliche Marine Pre-Dreadnought Battleships (1890-1908)

1. [[Brandenburg-Class]] (1891-1894) - 4 ships, first modern German battleships
   - Brandenburg, Wörth, Weißenburg, Kurfürst Friedrich Wilhelm
   - 6× 11-inch guns, 15.5 knots, 10,500 tons
   - First ocean-going German battleships

2. [[Kaiser-Friedrich-III-Class]] (1896-1902) - 5 ships
   - Kaiser Friedrich III, Kaiser Wilhelm II, Kaiser Wilhelm der Große, Kaiser Barbarossa, Kaiser Karl der Große
   - 4× 9.4-inch guns, 18 knots, 11,600 tons
   - Improved armor and armament

3. [[Wittelsbach-Class]] (1900-1904) - 5 ships
   - Wittelsbach, Wettin, Zähringen, Schwaben, Mecklenburg
   - 4× 9.4-inch guns, 18 knots, 12,800 tons
   - Enhanced secondary battery

4. [[Braunschweig-Class]] (1902-1906) - 5 ships
   - Braunschweig, Elsass, Hessen, Preußen, Lothringen
   - 4× 11-inch guns, 18 knots, 14,200 tons
   - Return to larger caliber guns

5. [[Deutschland-Class-Pre-Dreadnought]] (1904-1908) - 5 ships, last pre-dreadnoughts
   - Deutschland, Hannover, Pommern, Schlesien, Schleswig-Holstein
   - 4× 11-inch guns, 18 knots, 14,200 tons
   - SMS Pommern only battleship sunk at Jutland

### Kaiserliche Marine Dreadnought Battleships (1908-1916)

6. [[Nassau-Class]] (1908-1910) - **4 ships, first German dreadnoughts**
   - Nassau, Westfalen, Rheinland, Posen
   - 12× 11-inch guns (hexagonal turret arrangement), 20 knots, 19,000 tons
   - Revolutionary all-big-gun design

7. [[Helgoland-Class]] (1909-1912) - 4 ships
   - Helgoland, Ostfriesland, Thüringen, Oldenburg
   - 12× 12-inch guns (hexagonal arrangement), 21 knots, 23,000 tons
   - Improved armor and firepower

8. [[Kaiser-Class]] (1911-1913) - **5 ships, first superfiring**
   - Kaiser, Friedrich der Große, Kaiserin, König Albert, Prinzregent Luitpold
   - 10× 12-inch guns (superfiring layout), 21 knots, 25,000 tons
   - First German ships with superfiring turrets

9. [[König-Class]] (1913-1916) - 4 ships
   - König, Großer Kurfürst, Markgraf, Kronprinz
   - 10× 12-inch guns, 21 knots, 26,000 tons
   - Improved Kaiser design

### Kaiserliche Marine Super-Dreadnought Battleships (1915-1918)

10. [[Bayern-Class]] (1915-1917) - **2 ships completed (4 planned), 15-inch guns**
    - Bayern, Baden (completed)
    - Sachsen, Württemberg (cancelled incomplete)
    - 8× 15-inch guns, 22 knots, 32,000 tons
    - Most powerful German WWI battleships

### Kaiserliche Marine Battlecruisers (1909-1918)

11. [[SMS-Von-der-Tann]] (1909) - **1 ship, first German battlecruiser**
    - 8× 11-inch guns, 27.5 knots, 21,000 tons
    - Jutland veteran, superior to British Invincible-class

12. [[Moltke-Class]] (1910-1911) - 2 ships
    - Moltke, Goeben
    - 10× 11-inch guns, 28 knots, 23,000 tons
    - Goeben escaped to Turkey 1914, became Yavuz

13. [[SMS-Seydlitz]] (1912) - 1 ship
    - 10× 11-inch guns, 28.5 knots, 25,000 tons
    - Survived 21 hits at Jutland (legendary durability)

14. [[Derfflinger-Class]] (1913-1917) - **3 ships, best WWI battlecruisers**
    - Derfflinger, Lützow, Hindenburg
    - 8× 12-inch guns, 27 knots, 31,000 tons
    - Superior to British battlecruisers (better armor)

15. [[Mackensen-Class]] (1917) - **4 planned, NONE COMPLETED**
    - Mackensen, Graf Spee, Prinz Eitel Friedrich, Fürst Bismarck
    - 8× 13.8-inch guns, 28 knots, 35,000 tons (planned)
    - All broken up on slips 1919-1923

### Interwar Period (1919-1931)

**Treaty of Versailles Restrictions:**
- Germany limited to 6 pre-dreadnought coast defense ships (<10,000 tons)
- No new construction allowed initially
- Existing battleships to be scrapped
- High Seas Fleet scuttled at Scapa Flow (21 June 1919)

**Retained Ships (1920s):**
- 8 pre-dreadnoughts kept as coast defense ships
- Schlesien and Schleswig-Holstein (Deutschland-class) served until WWII

### Kriegsmarine Pocket Battleships (1931-1936)

16. [[Deutschland-Class-Pocket-Battleship]] (1931-1936) - **3 ships, treaty circumvention**
    - Deutschland (renamed Lützow 1940), Admiral Scheer, Admiral Graf Spee
    - 6× 11-inch guns, 28 knots (diesel), 16,000 tons (officially 10,000 tons)
    - Designed to outrun battleships, outgun cruisers
    - Graf Spee scuttled after Battle of River Plate (1939)

### Kriegsmarine Battlecruisers / Fast Battleships (1936-1939)

17. [[Scharnhorst-Class]] (1936-1939) - **2 ships, fast battleships**
    - Scharnhorst, Gneisenau
    - 9× 11-inch guns (planned upgrade to 6× 15-inch never completed), 32 knots, 38,900 tons
    - Scharnhorst sunk by HMS Duke of York (1943)
    - Gneisenau bombed and decommissioned (1942)

### Kriegsmarine Battleships (1939-1941)

18. [[Bismarck-Class]] (1939-1941) - **2 ships, 15-inch guns**
    - Bismarck, Tirpitz
    - 8× 15-inch guns, 30 knots, 50,300 tons
    - Bismarck sunk May 1941 (after sinking HMS Hood)
    - Tirpitz sunk by RAF November 1944 (Tallboy bombs)

### Planned But Never Built (1939-1945)

19. [[H39-Class]] - **6 ships planned (H, J, K, L, M, N), NONE LAID DOWN**
    - 8× 16-inch guns, 30 knots, 56,200 tons
    - Cancelled 1939 (WWII outbreak)

20. [[H41-Class]] - **Planned, NEVER BEGUN**
    - 8× 16.5-inch guns, 30 knots, 68,000 tons
    - Design study only

21. [[H42-Class]] - **Planned, NEVER BEGUN**
    - 8× 18-inch guns, 30 knots, 90,000 tons
    - Increasingly unrealistic design

22. [[H43-Class]] - **Planned, NEVER BEGUN**
    - 8× 20-inch guns, 30 knots, 111,000 tons
    - Fantasy design

23. [[H44-Class]] - **Planned, NEVER BEGUN**
    - 8× 20-inch guns, 30 knots, 141,500 tons
    - Largest battleship ever designed (never serious proposal)

24. [[O-Class-Battlecruiser]] - **3 ships planned, NONE BUILT**
    - 6× 15-inch guns, 35 knots, 35,000 tons
    - Improved Scharnhorst design, cancelled 1939

## Key Technologies

### Main Battery Evolution
- **1890-1906:** 4× 9.4-11-inch guns (pre-dreadnoughts)
- **1908-1909:** 12× 11-inch guns (Nassau, Helgoland - hexagonal layout)
- **1911-1916:** 10× 12-inch guns (Kaiser, König - superfiring)
- **1915-1918:** 8× 15-inch guns (Bayern - most powerful WWI)
- **1931-1939:** 6× 11-inch guns (Deutschland, Scharnhorst - smaller caliber, higher rate of fire)
- **1939-1941:** 8× 15-inch guns (Bismarck - return to 15-inch)
- **1939-1945 (planned):** 8× 16-20-inch guns (H-class - never built)

### Armor Evolution
- **1890-1906:** Harvey/Krupp armor, 6-12 inches
- **1908-1916:** Krupp cemented armor, improved protection
- **1915-1918:** Enhanced armor schemes (Bayern)
- **1931-1936:** Diesel engines allowed better armor distribution (Deutschland)
- **1936-1941:** Advanced armor (Bismarck class)

### Propulsion Evolution
- **1890-1915:** Coal-fired boilers, reciprocating engines/turbines
- **1908-1945:** Steam turbines standard (most ships)
- **1931-1936:** Diesel engines (Deutschland-class - unique)
- **1936-1945:** High-pressure steam turbines

### Speed Evolution
- **1890-1906:** 16-18 knots (pre-dreadnoughts)
- **1908-1916:** 20-22 knots (dreadnoughts)
- **1909-1918:** 27-28 knots (battlecruisers)
- **1931-1936:** 28 knots (pocket battleships - diesel)
- **1936-1939:** 32 knots (Scharnhorst - fastest battleships)
- **1939-1941:** 30 knots (Bismarck)

## Size Growth

| Class | Year | Displacement | Length | Main Guns | Speed |
|-------|------|--------------|--------|-----------|-------|
| Brandenburg | 1891 | 10,500 tons | 377 ft | 6× 11" | 15.5 kn |
| Nassau | 1908 | 19,000 tons | 479 ft | 12× 11" | 20 kn |
| Kaiser | 1911 | 25,000 tons | 564 ft | 10× 12" | 21 kn |
| Bayern | 1915 | 32,000 tons | 590 ft | 8× 15" | 22 kn |
| Derfflinger | 1913 | 31,000 tons | 689 ft | 8× 12" | 27 kn |
| Deutschland | 1931 | 16,000 tons | 610 ft | 6× 11" | 28 kn |
| Scharnhorst | 1936 | 38,900 tons | 771 ft | 9× 11" | 32 kn |
| Bismarck | 1939 | 50,300 tons | 823 ft | 8× 15" | 30 kn |
| H39 (planned) | 1939 | 56,200 tons | 870 ft | 8× 16" | 30 kn |

## Notable Service

### Pre-WWI
- **Naval Race:** Tirpitz's naval laws sparked arms race with Britain
- **Dreadnought Gap:** Germany initially behind Britain (1906-1910)
- **High Seas Fleet:** Concentrated in North Sea to challenge Royal Navy

### World War I (1914-1918)
- **Battle of Jutland (31 May 1916):** Largest battleship engagement
  - 16 German dreadnoughts vs 28 British dreadnoughts
  - SMS Pommern (pre-dreadnought) sunk - only German battleship lost
  - German tactical victory (more British losses), British strategic victory (High Seas Fleet never challenged again)
  - German battlecruisers superior armor saved them (vs British losses)
- **Scapa Flow Scuttling (21 June 1919):** 52 ships scuttled by crews
  - 15 battleships and battlecruisers scuttled
  - Prevented British from seizing German fleet
  - Largest deliberate sinking of ships in history

### Interwar Period (1919-1933)
- **Treaty of Versailles:** Severe restrictions on German navy
- **Secret Rearmament:** Planning began 1920s for future expansion
- **Pocket Battleships:** Exploited treaty loopholes (1931+)

### World War II (1939-1945)
- **Battle of River Plate (1939):** Admiral Graf Spee scuttled after damage
- **Sinking of Hood (1941):** Bismarck sank pride of Royal Navy (3 minutes)
- **Sinking of Bismarck (1941):** Royal Navy hunted down and sank Bismarck
- **Channel Dash (1942):** Scharnhorst and Gneisenau escaped through English Channel
- **Battle of North Cape (1943):** Scharnhorst sunk by HMS Duke of York
- **Sinking of Tirpitz (1944):** RAF sank with Tallboy bombs (Norway)

### Famous Ships

- **SMS Bayern:** Most powerful WWI battleship, surrendered 1918, scuttled Scapa Flow
- **SMS Seydlitz:** Survived 21 hits at Jutland, legendary durability
- **SMS Derfflinger:** Best WWI battlecruiser, scuttled Scapa Flow
- **Admiral Graf Spee:** Scuttled after River Plate (1939)
- **Bismarck:** Sank HMS Hood, hunted down and sunk May 1941
- **Tirpitz:** "Lone Queen of the North" - tied down Royal Navy 1942-1944
- **Scharnhorst:** Sunk Battle of North Cape December 1943

## Cancelled Battleship Programs

### Mackensen-Class Battlecruisers (1917) - INCOMPLETE
- **Ordered:** 4 ships under 1914 program
- **Specifications:** 35,000 tons, 8× 13.8-inch guns, 28 knots
- **Progress:** All laid down 1915-1917, construction stopped 1917
- **Cancellation:** WWI material shortages, U-boat priority
- **Fate:** Broken up on slips 1919-1923

### Ersatz Yorck-Class Battlecruisers (1916) - CANCELLED
- **Ordered:** 3 ships planned
- **Specifications:** 38,000 tons, 8× 15-inch guns, 28 knots
- **Cancellation:** Never laid down (WWI priorities)

### H39-Class Battleships (1939) - CANCELLED
- **Ordered:** 6 ships planned (H, J, K, L, M, N)
- **Specifications:** 56,200 tons, 8× 16-inch guns, 30 knots
- **Progress:** None laid down
- **Cancellation:** September 1939 (WWII outbreak, resources diverted to U-boats)

### H41, H42, H43, H44 Designs - FANTASY PROJECTS
- **H41:** 68,000 tons, 8× 16.5-inch guns
- **H42:** 90,000 tons, 8× 18-inch guns
- **H43:** 111,000 tons, 8× 20-inch guns
- **H44:** 141,500 tons, 8× 20-inch guns (largest battleship ever designed)
- **Status:** Design studies only, increasingly unrealistic
- **Purpose:** Hitler's megalomania, never serious proposals

### O-Class Battlecruisers (1939) - CANCELLED
- **Ordered:** 3 ships planned
- **Specifications:** 35,000 tons, 6× 15-inch guns, 35 knots
- **Progress:** None laid down
- **Cancellation:** September 1939 (WWII outbreak)

---

**Tree:** Master Research Tree | **Classes:** ~24 | **Ships Built:** ~59 | **Ships Planned:** ~79+

#battleship #kaiserliche-marine #kriegsmarine #german-navy #dreadnought #bismarck #tirpitz #scharnhorst #jutland #scapa-flow #plan-z #h-class

## Comparison to Royal Navy

| Feature | Germany | Britain | Advantage |
|---------|---------|---------|-----------|
| **Pre-Dreadnoughts** | 24 ships | 52 ships | Britain (quantity) |
| **Dreadnoughts** | 17 ships | 22 ships | Britain (quantity) |
| **Battlecruiser Armor** | Superior (better protection) | Inferior (speed priority) | Germany (quality) |
| **Jutland Losses** | 1 battleship (Pommern) | 3 battlecruisers | Germany (survivability) |
| **15-inch Guns** | 4 ships (Bayern, Bismarck classes) | 13 ships (QE, Revenge, Nelson) | Britain (quantity) |
| **WWII Readiness** | 2 modern battleships | 5 modern battleships | Britain (quantity) |
| **Diesel Propulsion** | Deutschland-class (innovative) | None | Germany (innovation) |

**Strategic Assessment:**
- Germany: Quality over quantity, superior armor and survivability
- Britain: Quantity over quality, global naval supremacy
- Result: British numerical superiority decisive in both World Wars
