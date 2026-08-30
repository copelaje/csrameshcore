# Getting Started with MeshCore

Welcome to the CSRA MeshCore network. This guide will take you from zero to connected - no prior radio or networking experience needed.

---

## Overview: What You'll Need

Getting on the MeshCore network requires three things:

1. **A LoRa node** - a small radio device (handheld or fixed)
2. **The MeshCore app** - free on Android and iOS
3. **The correct regional settings** - so you can talk to other CSRA nodes

The whole process typically takes under an hour.

---

## Step 1: Choose Your Hardware

Not sure what to buy? The **Buying Guide** matches your situation - just getting on the network, adding a repeater, or building your own - to a specific recommendation. For a full comparison of every supported device, antennas, and accessories, see the **Hardware Guide**.

If you just want a quick starting point, here are the most common picks. Each links to full specs, pricing, and buy links:

<div class="grid cards" markdown>

-   ![Seeed SenseCAP T1000-E](assets/hardware/t1000-e.jpg){ .product-image }

    **Seeed SenseCAP T1000-E**

    Most portable, everyday carry. ~$40

    [Details](hardware.md#seeed-sensecap-card-tracker-t1000-e)

-   ![Seeed Wio Tracker L1 Pro](assets/hardware/wio-tracker-l1-pro.jpg){ .product-image }

    **Seeed Wio Tracker L1 Pro**

    Better range and battery life. ~$47

    [Details](hardware.md#seeed-wio-tracker-l1-pro)

-   ![Seeed SenseCAP Solar Node P1-Pro](assets/hardware/solar-node-p1-pro.webp){ .product-image }

    **Seeed SenseCAP Solar Node P1-Pro**

    A fixed rooftop repeater. ~$90

    [Details](hardware.md#seeed-sensecap-solar-node-p1-pro)

</div>

[Start with the Buying Guide](buying-guide.md){ .md-button .md-button--primary } &nbsp; [Full Hardware Guide](hardware.md){ .md-button }

--8<-- "band-warning.md"

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

Need USB drivers, manual `esptool` flashing, over-the-air updates, or help getting a device into flash mode? See the [Firmware Reference](#firmware-reference) below.

---

## Step 3: Install the MeshCore App

=== "Android"

    1. Open the **Google Play Store**
    2. Search for **MeshCore**
    3. Install the official app by Liam Cottle
    4. Open the app - you'll be guided through initial setup

=== "iOS"

    1. Open the **App Store**
    2. Search for **MeshCore**
    3. Install the official app
    4. Open the app - you'll be guided through initial setup

---

## Step 4: Pair Your Device

1. Power on your LoRa node.
2. Enable Bluetooth on your phone.
3. Open the MeshCore app and tap **Add Device**.
4. Select your device from the Bluetooth scan list.
5. Pair when prompted - no PIN required on most devices, others default to 123456.

---

## Step 5: Apply CSRA Regional Settings

In the app's Radio Settings, select the **USA/Canada (Recommended)** preset. That's it - the default **Public** channel requires no additional configuration.

!!! success "You're on the network!"
    Once your settings match, your device will automatically begin discovering and communicating with nearby CSRA nodes.

!!! warning "Be patient!"
    To save power nodes advertise infrequently. It may take a day or two for things to show, but you can still communicate without "seeing" the node adverts as follows...

---

## Step 6: Test and Say Hello

Join the **`#test`** channel and send a message - bots will auto-reply to confirm your device is on the network and relaying. Then hop over to the **Public** channel and introduce yourself! Include your general location (e.g., "Augusta south side" or "North Augusta") so others can get a sense of coverage in your area.

---

## Firmware Reference

The web flasher in Step 2 covers most devices. These sections are for less common hardware, manual flashing, and over-the-air updates.

??? info "USB drivers (Windows / macOS)"
    Some devices use USB-to-serial chips that require drivers on Windows and macOS.

    | Chip | Used By | Driver |
    |---|---|---|
    | CP2102 | Heltec V3, some T-Beams | [Silicon Labs CP210x](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) |
    | CH340 | Many budget ESP32 boards | [WCH CH340 Driver](https://www.wch-ic.com/downloads/CH341SER_EXE.html) |
    | FTDI | Some older boards | [FTDI VCP Drivers](https://ftdichip.com/drivers/vcp-drivers/) |

    Linux typically detects these automatically. macOS may require manual installation for CH340.

??? info "Putting a device into flash mode"
    If the web flasher can't communicate with your device, it may need to be put into flash/bootloader mode manually:

    - **Heltec V3** - hold **PRG** button, plug in USB, release after 2 seconds
    - **LILYGO T-Beam** - hold **IO0/BOOT** button, plug in USB, release after 2 seconds
    - **T-Echo (nRF52840)** - double-tap the **RESET** button quickly; the device mounts as a USB drive, then drag the `.uf2` firmware file onto the drive

??? info "Updating firmware over-the-air (OTA)"
    For hard-to-reach devices it can be convenient to update firmware over-the-air (OTA) via Bluetooth without a USB cable. Most devices support this, but may need to be flashed with an OTA-capable bootloader before installing MeshCore itself.

    [This page](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md#73-q-is-there-a-way-to-lower-the-chance-of-a-failed-ota-device-firmware-update-dfu) links to the latest bootloader and install instructions.

    !!! warning "Keep the app open during OTA updates"
        Closing the app or losing Bluetooth connection mid-update can corrupt firmware. Stay close to the device.

??? info "Manual flash with esptool (advanced)"
    For ESP32 devices, you can flash manually using `esptool.py`:

    ```bash
    # Install esptool
    pip install esptool

    # Download firmware .bin from https://meshcore.io/downloads

    # Flash (replace /dev/ttyUSB0 with your port, COM3 etc. on Windows)
    esptool.py --chip esp32s3 --port /dev/ttyUSB0 \
      --baud 921600 write_flash -z 0x0 meshcore-heltec-v3-latest.bin
    ```

    Check the [MeshCore documentation](https://docs.meshcore.io) for the correct flash address and chip type for your specific device.

??? info "Verifying the installation"
    After flashing:

    1. The device display (if equipped) should show the MeshCore logo or startup screen
    2. Open the MeshCore app, tap **Add Device**, and your device should appear in the Bluetooth scan
    3. After pairing, open **Device Info** and confirm the firmware version shows `MeshCore vX.X.X`

    If the device doesn't appear in Bluetooth scans, try powering it off and back on after flashing.

---

## Troubleshooting

??? question "My device paired but I don't see any other nodes"
    - Confirm you selected the **USA/Canada (Recommended)** preset in Radio Settings
    - Check that your antenna is fully connected - never transmit without an antenna
    - Move to a higher location if possible - LoRa is line-of-sight sensitive
    - Check the [CSRA Network](https://corescope.csramesh.org/#/map) page to see if there are known nodes near you

??? question "The web flasher doesn't detect my device"
    - Try a different USB cable - many cables are charge-only with no data pins
    - Try a different USB port on your computer
    - Put the device into flash mode and install USB drivers if prompted - see the [Firmware Reference](#firmware-reference) above

??? question "My device gets hot or the battery drains fast"
    - Ensure transmit power is not set above the legal US limit (30 dBm / 1W)
    - Enable sleep mode between transmissions in device settings
    - Check that you have a proper antenna - a mismatch causes reflected power and heat

??? question "I still have questions, what do I do?"
    - Many hang out on [CSRAMesh discord](https://discord.com/invite/mgzj2PmhKf) and are happy to help in the `#meshcore` room.
    - [Facebook](https://www.google.com/url?q=https%3A%2F%2Fwww.facebook.com%2Fshare%2Fg%2F15wMGLcU8Q%2F&sa=D&sntz=1&usg=AOvVaw1g3jS0FPGZQ2DREpKuDqR-) is less active, but you can reach out there as well.

---

## Next Steps

- Explore the [Hardware Guide](hardware.md) for accessory and antenna recommendations
- Visit [Resources](resources.md) for links to the official docs, firmware releases, and community forums
