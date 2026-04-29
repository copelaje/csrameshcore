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
| Lowest cost entry | Seeed XIAO nRF52840 + Wio-SX1262 Kit | ~$13 |
| Getting started / portable | Heltec V3 or LILYGO T-Beam | ~$35–55 |
| Everyday carry / GPS | Seeed SenseCAP T1000-E or Wio Tracker L1 Pro | ~$40–47 |
| Fixed node / relay | RAK WisBlock or Seeed SenseCAP Solar Node P1-Pro | ~$25–90 |

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

If you prefer to flash manually using `esptool` or PlatformIO, refer to the [official MeshCore documentation](https://docs.meshcore.io) for device-specific instructions.

---

## Step 3: Install the MeshCore App

=== "Android"

    1. Open the **Google Play Store**
    2. Search for **MeshCore**
    3. Install the official app by Liam Cottle
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
5. Pair when prompted — no PIN required on most devices, others default to 123456.

---

## Step 5: Apply CSRA Regional Settings

In the app's Radio Settings, select the **USA/Canada (Recommended)** preset. That's it — the default **Public** channel requires no additional configuration.

!!! success "You're on the network!"
    Once your settings match, your device will automatically begin discovering and communicating with nearby CSRA nodes.

!!! warning "Be patient!"
    To save power nodes advertise infrequently. It may take a day or two for things to show, but you can still communicate without "seeing" the node adverts as follows...

---

## Step 6: Test and Say Hello

Join the **`#test`** channel and send a message — bots will auto-reply to confirm your device is on the network and relaying. Then hop over to the **Public** channel and introduce yourself! Include your general location (e.g., "Augusta south side" or "North Augusta") so others can get a sense of coverage in your area.

---

## Troubleshooting

??? question "My device paired but I don't see any other nodes"
    - Confirm you selected the **USA/Canada (Recommended)** preset in Radio Settings
    - Check that your antenna is fully connected — never transmit without an antenna
    - Move to a higher location if possible — LoRa is line-of-sight sensitive
    - Check the [CSRA Network](https://corescope.csramsh.org/#/map) page to see if there are known nodes near you

??? question "The web flasher doesn't detect my device"
    - Try a different USB cable — many cables are charge-only with no data pins
    - Hold the BOOT button on your device while plugging in (puts it in flash mode)
    - Try a different USB port on your computer
    - Install the CP210x or CH340 USB driver for your OS if prompted

??? question "My device gets hot or the battery drains fast"
    - Ensure transmit power is not set above the legal US limit (30 dBm / 1W)
    - Enable sleep mode between transmissions in device settings
    - Check that you have a proper antenna — a mismatch causes reflected power and heat

??? question "I still have questions, what do I do?"
    - Many hang out on [CSRAMesh discord](https://discord.com/invite/mgzj2PmhKf) and are happy to help in the `#meshcore` room.
    - [Facebook](https://www.google.com/url?q=https%3A%2F%2Fwww.facebook.com%2Fshare%2Fg%2F15wMGLcU8Q%2F&sa=D&sntz=1&usg=AOvVaw1g3jS0FPGZQ2DREpKuDqR-) is less active, but you can reach out there as well.

---

## Next Steps

- Explore the [Hardware Guide](hardware.md) for accessory and antenna recommendations
- Visit [Resources](resources.md) for links to the official docs, firmware releases, and community forums
