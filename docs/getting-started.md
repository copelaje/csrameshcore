# Getting Started with MeshCore

Welcome to the CSRA MeshCore network. This guide will take you from zero to connected — no prior radio or networking experience needed.

---

## Overview: What You'll Need

Getting on the MeshCore network requires three things:

1. **A LoRa node** — a small radio device (handheld or fixed)
2. **The MeshCore app** — free on Android and iOS
3. **The correct regional settings** — so you can talk to other CSRA nodes

The whole process typically takes under an hour.

---

## Step 1: Choose Your Hardware

See the full [Hardware Guide](hardware.md) for detailed comparisons, but here's the short version:

| Use Case | Recommended Device | Price |
|---|---|---|
| Getting started / portable | Heltec V3 or LILYGO T-Beam | ~$35–55 |
| Everyday carry / rugged | RAK Wireless WisBlock | ~$50–80 |
| Fixed node / relay | LILYGO T-Echo or any USB-powered device | ~$40–60 |

!!! note "USA Frequency Band"
    All devices must support the **915 MHz** LoRa band for use in the United States. Confirm before purchasing — some budget devices are 868 MHz (EU) only.

---

## Step 2: Flash MeshCore Firmware

Most LoRa devices ship with other firmware (Meshtastic, LoRa32, etc.) and need to be flashed with MeshCore before use.

### Using the MeshCore Web Flasher (Easiest)

1. Connect your device to your computer via USB.
2. Open the MeshCore web flasher at **[flasher.meshcore.io](https://flasher.meshcore.io)** in Chrome or Edge (other browsers may not support WebSerial).
3. Select your device model from the dropdown.
4. Click **Flash** and wait for the process to complete (~2 minutes).
5. The device will reboot automatically when done.

!!! warning "Use Chrome or Edge"
    The web flasher requires WebSerial API support, which Firefox and Safari do not currently support.

### Manual Flash (Advanced)

If you prefer to flash manually using `esptool` or PlatformIO, refer to the [official MeshCore documentation](https://meshcore.io/docs) for device-specific instructions.

---

## Step 3: Install the MeshCore App

=== "Android"

    1. Open the **Google Play Store**
    2. Search for **MeshCore**
    3. Install the official app by the MeshCore team
    4. Open the app — you'll be guided through initial setup

=== "iOS"

    1. Open the **App Store**
    2. Search for **MeshCore**
    3. Install the official app
    4. Open the app — you'll be guided through initial setup

---

## Step 4: Pair Your Device

1. Power on your LoRa node.
2. Enable Bluetooth on your phone.
3. Open the MeshCore app and tap **Add Device**.
4. Select your device from the Bluetooth scan list.
5. Pair when prompted — no PIN required on most devices.

---

## Step 5: Apply CSRA Regional Settings

This is the most important step for connecting to the local network. Your device must be on the same channel and frequency settings as other CSRA nodes.

See the full [Regional Settings](settings.md) page, but the quick version:

- **Region:** United States
- **Frequency slot:** Default USA (915 MHz band)
- **Channel name:** `CSRA-1` *(primary local channel)*
- **Modem preset:** Long Range / Slow (recommended for range)

!!! success "You're on the network!"
    Once your settings match, your device will automatically begin discovering and communicating with nearby CSRA nodes.

---

## Step 6: Say Hello

Open the **Public Channel** in the app and introduce yourself! The CSRA MeshCore community is friendly and happy to help newcomers.

Include your general location (e.g., "Augusta south side" or "North Augusta") so others can get a sense of coverage in your area.

---

## Troubleshooting

??? question "My device paired but I don't see any other nodes"
    - Confirm your regional settings match exactly (see [Settings](settings.md))
    - Check that your antenna is fully connected — never transmit without an antenna
    - Move to a higher location if possible — LoRa is line-of-sight sensitive
    - Check the [CSRA Network](network.md) page to see if there are known nodes near you

??? question "The web flasher doesn't detect my device"
    - Try a different USB cable — many cables are charge-only with no data pins
    - Hold the BOOT button on your device while plugging in (puts it in flash mode)
    - Try a different USB port on your computer
    - Install the CP210x or CH340 USB driver for your OS if prompted

??? question "My device gets hot or the battery drains fast"
    - Ensure transmit power is not set above the legal US limit (30 dBm / 1W)
    - Enable sleep mode between transmissions in device settings
    - Check that you have a proper antenna — a mismatch causes reflected power and heat

---

## Next Steps

- Explore the [Hardware Guide](hardware.md) for accessory and antenna recommendations
- Read about [CSRA Network topology](network.md) and where to place a fixed node for best coverage
- Visit [Resources](resources.md) for links to the official docs, firmware releases, and community forums
