---
module_id: COM-008
name: Radio UHF (Tactical Secure)
category: support
subcategory: communications
era: 1960+
nation: USA/NATO
slot_type: support
weight: 120
crew_required: 1

# Performance
range: 30                      # km
data_rate: instant
reliability: 98                # percentage
security: medium

# Capabilities
voice_capable: true
text_capable: false
data_capable: false            # automated sharing
vision_sharing: true           # shares fog of war

# Requirements
line_of_sight: true
weather_affected: false
crew_required: 1

tags: [communications, voice, radio, uhf, secure, modern]
---

# Radio UHF (Tactical Secure)

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-008 |
| **Era** | 1960+ |
| **Range** | 30 km |
| **Type** | Voice Radio (UHF Secure) |

## Description

Ultra High Frequency (UHF) tactical radio systems operate at 300 MHz to 3 GHz, providing short-range secure voice communication. UHF's higher frequencies allow more channels, better frequency hopping capability, and built-in encryption systems. Modern tactical UHF radios feature frequency-agile transmission, anti-jam modes, and secure voice encryption as standard features.

UHF tactical radios are designed for close-range coordination with high security. Frequency hopping makes interception difficult, and modern encryption prevents enemy comprehension even if signals are intercepted. The shorter range (30 km vs 50 km for VHF) is deliberate - it reduces detection probability and focuses on close tactical coordination.

## Effect on Multiplayer

**This module enables:**
- Secure real-time voice communication with allied players
- Vision sharing: **Yes** - Allied radar contacts appear on your displays
- Voice chat: **Yes** - Crystal-clear, secure voice communication
- Text messages: No (voice only)
- Encrypted channels (enemy cannot understand)
- Frequency hopping (harder to jam)
- Quick tactical commands via voice macros
- Coordinated targeting and maneuvers
- Anti-jam modes

**Secure Coordination:**

UHF improves on VHF with:
- Built-in encryption (enemy cannot understand even if intercepted)
- Frequency hopping (harder to jam or intercept)
- Better anti-jam capability
- More channels available
- Higher security classification

**Security Features:**
- Voice encryption standard (not optional)
- Frequency hopping spread spectrum
- Anti-jam modes activate automatically
- Interception alert (warns if enemy attempts jamming)
- Secure key distribution

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (30 km) |
| Rain/Fog | Slight reduction (heavy rain may affect) |
| Night | No effect (radio works 24/7) |
| Enemy jamming | Anti-jam mode engages, reduced but functional |
| Beyond horizon | No signal (line of sight required) |
| Antenna height | +5-10 km (taller masts = longer range) |

## Communication Range

| Configuration | Range | Notes |
|---------------|-------|-------|
| Standard UHF | 30 km | Line of sight, secure mode |
| Clear mode | 40 km | Non-secure, longer range |
| Anti-jam mode | 20 km | Reduced range, increased security |
| Aircraft relay | 150+ km | Aircraft extends secure range |

## Security Features

**Encryption:**
- Voice encryption: KY-57/58 or equivalent
- 256-bit or higher encryption
- Key changes: Daily or per-mission
- Secure key distribution via COMSEC procedures

**Frequency Hopping:**
- 100+ frequency changes per second
- Synchronized hopping pattern
- Requires cryptographic key to follow
- Makes jamming extremely difficult

**Anti-Jam Modes:**
- Spread spectrum modulation
- Power management (increases power to overcome jamming)
- Frequency selection (avoids jammed frequencies)
- Notification if jamming detected

## Tactical Use

1. **Close Tactical Coordination**: Secure small unit operations
2. **Special Operations**: Covert coordination
3. **Anti-Surface Warfare**: Coordinated strikes
4. **Close Air Support**: Secure air-ground coordination
5. **Amphibious Assault**: Shore party coordination
6. **Intelligence Operations**: Secure communication of sensitive intel
7. **Task Unit Coordination**: Destroyers, frigates coordinating

## Advantages

**Over VHF:**
- Built-in encryption (VHF requires separate encryption)
- Frequency hopping (harder to jam)
- More channels available (less congestion)
- Better anti-jam capability
- More secure against interception
- Modern solid-state reliability

**Over Earlier Systems:**
- Cannot be understood by enemy (encryption)
- Extremely difficult to jam (frequency hopping)
- Clearer audio quality
- More reliable (modern electronics)
- Smaller, lighter equipment
- Lower power consumption

## Limitations

- Shorter range than VHF (30 km vs 50 km)
- Line of sight only
- Heavy rain may affect (UHF more susceptible)
- Requires crypto keys (COMSEC procedures)
- Key distribution security critical
- More complex operation
- Cannot communicate with non-secure radios

## Historical Notes

UHF tactical radios emerged in the 1960s as the need for secure tactical communication became paramount. The Vietnam War demonstrated that unsecure VHF could be intercepted by enemy forces, compromising operations. UHF with encryption provided tactical security.

The Have Quick (1970s-80s) and SINCGARS (1980s-90s) programs developed frequency-hopping UHF radios that were extremely difficult to jam or intercept. These systems became standard on US and NATO ships, aircraft, and ground forces. The synchronized frequency hopping meant only allied forces with the correct crypto keys could communicate.

Gulf War (1991) demonstrated the effectiveness of secure UHF. Coalition forces coordinated complex multi-service operations without Iraqi forces able to jam or intercept communications. The ability to rapidly distribute crypto keys and change communication plans gave coalition forces a decisive advantage.

Modern tactical UHF is integrated with digital systems, supporting both voice and data transmission. Link 16 often uses UHF frequencies for automated tactical data exchange, while voice nets use separate secure UHF channels.

## Comparison to Other Systems

**vs VHF Radio:**
- Shorter range (30 km vs 50 km)
- Better security (built-in encryption)
- Better anti-jam capability
- More channels available
- More modern technology

**vs WWII/Early Radio:**
- Completely secure (vs easily intercepted)
- Cannot be jammed effectively (vs vulnerable)
- Much more reliable
- Clearer audio
- More sophisticated features

**vs Data Link:**
- Voice only (data link automated)
- More intuitive for simple messages
- Cannot share complex tactical pictures
- Better for immediate coordination

**vs Satellite Communications:**
- Shorter range (30 km vs global)
- No satellite dependency
- Lower latency (instant vs slight delay)
- More secure (harder to intercept UHF tactical vs SATCOM uplinks)
- Better for close tactical coordination

## Upgrade Path

- [[Radio-SATCOM]] - Add beyond line-of-sight capability (1970+)
- [[DataLink-Link16]] - Add automated tactical data exchange (1980+)
- [[Encrypted-Comms]] - Advanced encryption systems (1990+)

## Compatible With

- CIC Bridge (full integration with combat information center)
- Modern Bridge (full integration)
- Aegis Combat System (integrated)
- All modern radar systems (contact sharing)
- Fire Control Directors (targeting coordination)
- Data Link systems (voice + data integration)
- IFF Transponders (identification integration)

## COMSEC Procedures

**Crypto Key Management:**

Operating secure UHF requires proper COMSEC:
- Daily key changes (or mission-specific)
- Secure key distribution (encrypted channels or physical transfer)
- Key zeroization (destroy keys if capture imminent)
- Authentication procedures (verify identity)

**Operational Security:**
- Even encrypted, transmission reveals presence
- Use radio silence when appropriate
- Minimize transmission time
- Use pre-arranged code words for added security

**Multi-Level Security:**
- Different key sets for different classification levels
- Secret vs Top Secret nets
- Allied vs national nets
- Compartmented vs general access

## Game Balance Notes

UHF represents modern secure tactical communication. The built-in encryption means enemy players cannot intercept messages even if they have equivalent equipment. This provides significant tactical advantage - coordinate freely without enemy intelligence.

The shorter range (30 km vs 50 km for VHF) balances the security advantage. UHF is for close tactical coordination, not long-range fleet operations. Ships must stay relatively close to communicate, encouraging formation play.

The frequency-hopping and anti-jam capabilities make UHF resistant to electronic warfare. Enemy jamming is less effective, requiring dedicated ECM systems to degrade UHF communications. This creates counter-counter-measures gameplay.

**Gameplay Mechanics:**

Without UHF:
- VHF communications can be intercepted (enemy hears)
- Easier to jam
- Tactical plans exposed

With UHF:
- Secure voice (enemy cannot understand)
- Difficult to jam (anti-jam modes)
- Tactical surprise maintained
- Coordination without intelligence leak

The crypto key mechanic could be simplified in gameplay:
- Blue team auto-shares crypto keys
- Keys change periodically (daily)
- Captured ships lose keys after delay (crew destroys)
- Inter-allied coordination requires compatible keys

The 30 km range keeps UHF tactical. A destroyer division can coordinate securely, but fleet-wide coordination requires VHF or SATCOM. This creates interesting communication architecture: UHF for local secure, VHF for fleet-wide, SATCOM for strategic.
