# Hardware Guide

MeshCore runs on a variety of affordable LoRa-based devices. This page covers the most popular options available in 2026, with notes on what works best for different use cases in the CSRA.

!!! warning "USA Band Requirement"
    You **must** purchase a device with the **915 MHz** LoRa band for legal US operation. Double-check product listings — many otherwise identical devices are sold in 868 MHz (EU) variants that cannot be used in the USA.

---

## Recommended Devices

### Heltec WiFi LoRa 32 V3

**Best for: Beginners, portable use**

The Heltec V3 is one of the most popular MeshCore devices due to its built-in display, USB-C charging, and low cost. It's a great first device.

| Spec | Value |
|---|---|
| Chip | ESP32-S3 |
| LoRa | SX1262, 915 MHz |
| Display | 0.96" OLED |
| Battery | 18650 via JST connector |
| Approximate Price | $25–35 |

**Pros:** Cheap, widely available, integrated display, easy to flash  
**Cons:** Smaller battery connector, no GPS, basic casing

---

### LILYGO T-Beam

**Best for: GPS tracking, mobile use**

The T-Beam includes an onboard GPS module, making it ideal for location sharing and tracking. Available in multiple antenna configurations.

| Spec | Value |
|---|---|
| Chip | ESP32 |
| LoRa | SX1276 or SX1262, 915 MHz |
| GPS | u-blox NEO-M8N |
| Display | Optional OLED add-on |
| Approximate Price | $35–55 |

**Pros:** GPS built-in, 18650 battery holder included, robust community support  
**Cons:** Larger form factor, older SX1276 on some versions (confirm SX1262 for best performance)

---

### LILYGO T-Echo

**Best for: Everyday carry, e-ink display**

The T-Echo is a compact, finished-looking device with an e-ink display that's readable in direct sunlight — great for outdoor use.

| Spec | Value |
|---|---|
| Chip | nRF52840 |
| LoRa | SX1262, 915 MHz |
| Display | 1.54" e-ink |
| GPS | Optional |
| Approximate Price | $45–65 |

**Pros:** Excellent battery life (nRF52840 is very low power), sunlight readable, compact  
**Cons:** nRF52840 flash process is slightly different — use the [nRF-specific flasher instructions](https://meshcore.io/docs)

---

### RAK WisBlock Starter Kit

**Best for: Fixed nodes, custom builds**

RAK's modular WisBlock system lets you mix and match radio, base board, sensor, and enclosure modules. Popular for building permanent relay nodes.

| Spec | Value |
|---|---|
| Chip | nRF52840 |
| LoRa | RAK4631 (SX1262), 915 MHz |
| Modular | Yes — add GPS, sensors, displays |
| Approximate Price | $50–80 (starter kit) |

**Pros:** Modular and expandable, low power, great for outdoor fixed installations  
**Cons:** Requires some assembly, higher upfront cost for full kit

---

## Antennas

The stock antenna that comes with most devices is adequate for getting started, but upgrading your antenna can dramatically improve range.

| Antenna Type | Use Case | Gain |
|---|---|---|
| Stock stub antenna | Handheld / portable | 0–2 dBi |
| Fiberglass whip (12–18") | Fixed node, elevated | 3–5 dBi |
| Yagi directional | Point-to-point links | 8–12 dBi |

!!! tip "Height beats power"
    A $15 antenna on a rooftop will outperform a $100 antenna at ground level. For fixed relay nodes in the CSRA, elevation is the most valuable upgrade.

---

## Enclosures for Fixed Nodes

If you're deploying a permanent relay node outdoors, weatherproofing is essential in the humid Augusta climate.

- **Hammond 1554 series** (IP67) — watertight, easy to modify, widely available
- **BUD Industries NBF series** — good balance of size and price
- **3D printed + conformal coat** — flexible but requires proper sealing around connectors

Use **N-type** or **SMA** weatherproof connectors for antenna feed-throughs. Don't leave coax connectors exposed to rain.

---

## Power Options for Fixed Nodes

| Option | Notes |
|---|---|
| USB wall adapter | Simplest, requires AC power at site |
| USB power bank | Good for short-term / portable deployments |
| 18650 + solar panel | Popular for off-grid relay nodes |
| LiFePO4 battery + MPPT | Best long-term solution for outdoor solar nodes |

A 5W solar panel with a 3000 mAh LiFePO4 battery is sufficient to power most devices indefinitely in the CSRA's sun exposure.

---

## Where to Buy

- **Amazon** — fastest shipping, verify seller ratings and confirm 915 MHz
- **AliExpress** — lowest prices, 2–4 week shipping from China, check band carefully
- **Rokland** (rokland.com) — US-based, LoRa specialty retailer, good antenna selection
- **Mouser / Digi-Key** — for RAK WisBlock modules and professional components

---

## What NOT to Buy

- **433 MHz devices** — wrong frequency band for the USA, illegal on unlicensed frequencies
- **868 MHz devices** — EU band, will not interoperate with the CSRA network
- **No-name "LoRa" modules without SX1276/SX1262** — clone chips often have poor range and reliability
