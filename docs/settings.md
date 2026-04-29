# Regional Settings — USA / CSRA

To communicate with other nodes on the CSRA network, your device must be configured with matching settings. This page documents the standard settings used by the CSRA MeshCore community.

!!! success "These are the settings to use"
    Apply all settings on this page to join the primary CSRA network. Using different settings means your device won't be visible to — or able to hear — other local nodes.

---

## USA Frequency Band

The United States operates MeshCore on the **915 MHz ISM band** (902–928 MHz). This band is license-free for low-power devices under FCC Part 15 rules.

| Setting | Value |
|---|---|
| **Region** | United States |
| **Frequency band** | 915 MHz |
| **Regulatory** | FCC Part 15 (no license required) |

!!! warning "Do not use 868 MHz settings"
    868 MHz is the European band and is not legal for unlicensed use in the USA. Any device transmitting on 868 MHz in the US is operating outside FCC regulations.

---

## CSRA Primary Channel Settings

These are the community-agreed settings for the CSRA region's primary channel:

| Setting | Value |
|---|---|
| **Channel Name** | `CSRA-1` |
| **Modem Preset** | Long Range / Slow (`LONG_SLOW`) |
| **Frequency** | 906.875 MHz (default US slot 20) |
| **Bandwidth** | 250 kHz |
| **Spread Factor** | 11 |
| **Coding Rate** | 4/8 |
| **TX Power** | 27 dBm (500 mW) — legal US maximum for this band |

### Why Long Range / Slow?

The CSRA spans a large geographic area with a mix of urban and rural terrain. `LONG_SLOW` trades message throughput for maximum range and building penetration — the right tradeoff for a regional community network. High-density areas like downtown Augusta can sustain the lower throughput easily.

---

## Applying Settings in the App

=== "Android"

    1. Open MeshCore app → connect to your device
    2. Tap the **Device** tab → **Radio Settings**
    3. Set **Region** to `United States`
    4. Set **Modem Preset** to `Long Range / Slow`
    5. Under **Channels**, tap **+** to add a channel
    6. Enter channel name `CSRA-1`
    7. Tap **Save** — device will reboot to apply

=== "iOS"

    1. Open MeshCore app → connect to your device
    2. Tap **Settings** → **Radio**
    3. Set **Region** to `United States`
    4. Set **Preset** to `Long Range / Slow`
    5. Under **Channels**, add channel named `CSRA-1`
    6. Tap **Apply** — device will reboot to apply

---

## Channel Encryption

MeshCore channels use AES-256 encryption by default. The CSRA primary channel (`CSRA-1`) uses the **default public key** — this means any MeshCore user with the correct channel name and preset can join.

This is intentional: the public channel is for community coordination, not private conversation. For private messaging, use MeshCore's **Direct Message** feature, which uses device-to-device encrypted sessions.

---

## Transmit Power

| Setting | Value | Notes |
|---|---|---|
| **Maximum legal (USA)** | 30 dBm (1W) | FCC Part 15 limit |
| **CSRA recommended** | 27 dBm (500 mW) | Good balance of range and battery |
| **Portable/handheld** | 20–23 dBm | Extends battery life significantly |

!!! tip "More power ≠ more range"
    On a mesh network, adding relay nodes in strategic locations does far more for network coverage than cranking up transmit power. High power can actually cause interference and reduce network efficiency in dense areas.

---

## Hop Limit

| Setting | Recommended Value |
|---|---|
| **Hop Limit** | `3` |

A hop limit of 3 means a message can traverse up to 3 relay nodes. This is the CSRA community standard — it balances network reach with airtime efficiency. Setting this too high causes excessive rebroadcasting and degrades network performance for everyone.

---

## Advanced / Optional Settings

These are optional but recommended for fixed relay nodes:

| Setting | Recommended | Reason |
|---|---|---|
| **Node Role** | `Router` (fixed nodes) or `Client` (handheld) | Routers rebroadcast more aggressively |
| **Bluetooth** | Enabled on handhelds, optional on routers | Required for phone pairing |
| **MQTT** | Disabled | Not used on the CSRA network currently |
| **Position Broadcast** | Smart / On Movement | Share your location only when moving |

---

## Settings Summary (Quick Reference)

```
Region:        United States
Band:          915 MHz
Channel Name:  CSRA-1
Preset:        Long Range / Slow (LONG_SLOW)
TX Power:      27 dBm
Hop Limit:     3
Encryption:    AES-256 (default public key)
```

Print or save this — it's everything you need to get on the network.
