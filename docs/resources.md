# Resources & Links

A curated collection of links for CSRA MeshCore users — from official documentation to community forums and hardware suppliers.

---

## CSRA Local Resources

| Resource | Purpose |
|---|---|
| [csramesh.org](https://www.csramesh.org) | CSRA community mesh home page |
| [Corescope Map](https://corescope.csramsh.org/#/map) | Live map of active CSRA nodes |
| [AGS MeshMapper](https://ags.meshmapper.net) | War drive coverage map for the Augusta area |
| [CSRA Mesh Discord](https://discord.com/invite/mgzj2PmhKf) | Primary community chat — `#meshcore` channel for help and discussion |
| [CSRA Mesh Facebook Group](https://www.facebook.com/share/g/15wMGLcU8Q/) | Less active, but another way to connect with local members |
| [Augusta Ham](https://www.augustaham.net/) | Local amateur radio community — many CSRA MeshCore users are licensed hams |

---

## Official MeshCore

| Resource | Link | Notes |
|---|---|---|
| **MeshCore Website** | [meshcore.io](https://meshcore.io) | Main project site |
| **Documentation** | [docs.meshcore.io](https://docs.meshcore.io) | Official user and developer docs |
| **Web Flasher** | [flasher.meshcore.io](https://flasher.meshcore.io) | Flash firmware via browser |
| **Firmware Releases** | [GitHub Releases](https://github.com/meshcore-dev/MeshCore/releases) | Latest firmware downloads |
| **GitHub** | [github.com/meshcore-dev](https://github.com/meshcore-dev) | Source code and issue tracker |

---

## Apps

=== "Android"
    Search **"MeshCore"** on the Google Play Store, or download the APK directly from the [GitHub releases page](https://github.com/meshcore-dev/MeshCore/releases).

=== "iOS"
    Search **"MeshCore"** on the Apple App Store.

=== "Desktop (Python CLI)"
    A Python-based CLI client is available for Linux/macOS/Windows via:
    ```bash
    pip install meshcore-cli
    meshcore-cli --help
    ```

---

## Community

| Community | Platform | Purpose |
|---|---|---|
| **MeshCore Discord** | [discord.gg/meshcore](https://discord.gg/meshcore) | Main community hub, help & discussion |
| **MeshCore Subreddit** | [r/meshcore](https://reddit.com/r/meshcore) | Longer-form posts and project showcases |
| **CSRA Ham Radio** | Contact via this site | Local amateur radio community coordination |

!!! tip "Best place for help"
    The MeshCore Discord `#troubleshooting` channel is the fastest way to get answers from experienced users and developers.

---

## Learning Resources

### MeshCore & LoRa Basics

- **What is LoRa?** — [The Things Network LoRa overview](https://www.thethingsnetwork.org/docs/lorawan/what-is-lorawan/) — explains the underlying radio technology in accessible terms
- **Spread Spectrum explained** — good background on why LoRa achieves such long range at low power

### Radio & Antenna Fundamentals

Understanding a few basic antenna concepts will help you get the most out of your node placement:

- **dBi and gain** — higher gain antennas focus energy in a particular direction
- **Line of sight** — LoRa is primarily line-of-sight; elevation is your best friend
- **Fresnel zones** — why trees and buildings at distance matter more than you might expect

### FCC Part 15 Rules

The 915 MHz ISM band is governed by FCC Part 15, which allows unlicensed operation within power limits. Key points for MeshCore users:

- Maximum conducted power: **+30 dBm (1 Watt)**
- Maximum EIRP (with antenna gain): **+36 dBm (4 Watts)**
- No license required for operation within these limits
- Must accept interference from other Part 15 devices and cannot cause harmful interference

---

## Amateur Radio in the CSRA

MeshCore is popular in the ham radio community and complements traditional voice repeater networks. You don't need a license to use MeshCore (it operates under Part 15), but many CSRA MeshCore users are licensed amateurs.

Local ham resources:

- **CSRA Amateur Radio Community** — search for local clubs in Augusta and Aiken
- **ARRL** — [arrl.org](https://arrl.org) — national amateur radio organization, license info and study materials
- **HamStudy** — [hamstudy.org](https://hamstudy.org) — free Technician license exam prep

A **Technician license** opens up additional VHF/UHF digital modes that pair well with MeshCore for wider-area coordination.

---

## Hardware Suppliers

| Supplier | Notes |
|---|---|
| [Rokland](https://rokland.com) | US-based LoRa hardware and antenna specialist |
| [Amazon](https://amazon.com) | Convenient, verify 915 MHz band carefully |
| [AliExpress](https://aliexpress.com) | Lowest prices, 2–4 week shipping, check band |
| [Mouser Electronics](https://mouser.com) | RAK WisBlock modules and professional components |
| [Digi-Key](https://digikey.com) | Wide component selection for DIY builds |

---

## Tools & Utilities

| Tool | Purpose |
|---|---|
| [RF Line of Sight Calculator](https://www.scadacore.com/tools/rf-path/rf-line-of-sight/) | Estimate coverage between two points |
| [HeyWhatsThat](https://heywhatsthat.com) | Viewshed analysis — see what's visible from a hilltop |
| [FCC ID Search](https://fccid.io) | Verify a device's FCC certification and frequency |
| [esptool.py](https://github.com/espressif/esptool) | Manual firmware flashing for ESP32 devices |

---

## This Site

This documentation site is maintained by the CSRA MeshCore community. If you find an error, have updated settings to share, or want to contribute content:

- Reach out on the Public channel
- Open an issue or pull request on the site's GitHub repository

The site is built with [MkDocs](https://www.mkdocs.org) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, deployed to [meshcore.csramsh.org](https://meshcore.csramsh.org).
