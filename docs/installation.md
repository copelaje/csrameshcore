# Installation & Firmware

This page covers firmware flashing in more detail for users who want to go beyond the basic web flasher, or who are working with less common hardware.

---

## Web Flasher (Recommended)

The MeshCore web flasher at **[flasher.meshcore.io](https://flasher.meshcore.io)** handles most ESP32-based devices automatically.

**Requirements:**
- Google Chrome or Microsoft Edge (WebSerial API required)
- USB data cable (not a charge-only cable)
- Device drivers installed (see below)

**Steps:**
1. Connect device via USB
2. Open [flasher.meshcore.io](https://flasher.meshcore.io) in Chrome/Edge
3. Click **Connect** and select your device's serial port
4. Choose your device model
5. Click **Flash** — do not disconnect during flashing
6. Device reboots automatically when complete

---

## USB Drivers

Some devices use USB-to-serial chips that require drivers on Windows and macOS.

| Chip | Used By | Driver |
|---|---|---|
| CP2102 | Heltec V3, some T-Beams | [Silicon Labs CP210x](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) |
| CH340 | Many budget ESP32 boards | [WCH CH340 Driver](https://www.wch-ic.com/downloads/CH341SER_EXE.html) |
| FTDI | Some older boards | [FTDI VCP Drivers](https://ftdichip.com/drivers/vcp-drivers/) |

Linux typically detects these automatically. macOS may require manual installation for CH340.

---

## Putting Devices into Flash Mode

If the web flasher can't communicate with your device, it may need to be put into flash/bootloader mode manually:

=== "Heltec V3"
    Hold **PRG** button → plug in USB → release after 2 seconds

=== "LILYGO T-Beam"
    Hold **IO0/BOOT** button → plug in USB → release after 2 seconds

=== "T-Echo (nRF52840)"
    Double-tap the **RESET** button quickly — the device mounts as a USB drive. Drag the `.uf2` firmware file onto the drive.

---

## Updating Firmware (OTA)

Once MeshCore is installed, you can update over-the-air (OTA) via the app without a USB cable:

1. Open the MeshCore app and connect to your device
2. Go to **Device Settings → Firmware**
3. If an update is available, tap **Update**
4. Wait for the device to download, flash, and reboot (~3–5 minutes)

!!! warning "Keep the app open during OTA updates"
    Closing the app or losing Bluetooth connection mid-update can corrupt firmware. Stay close to the device.

---

## Manual Flash with esptool (Advanced)

For ESP32 devices, you can flash manually using `esptool.py`:

```bash
# Install esptool
pip install esptool

# Download firmware .bin from https://meshcore.io/downloads

# Flash (replace /dev/ttyUSB0 with your port, COM3 etc. on Windows)
esptool.py --chip esp32s3 --port /dev/ttyUSB0 \
  --baud 921600 write_flash -z 0x0 meshcore-heltec-v3-latest.bin
```

Check the [MeshCore documentation](https://meshcore.io/docs) for the correct flash address and chip type for your specific device.

---

## Verifying Installation

After flashing:

1. The device display (if equipped) should show the MeshCore logo or startup screen
2. Open the MeshCore app → **Add Device** → your device should appear in the Bluetooth scan
3. After pairing, navigate to **Device Info** — confirm firmware version shows `MeshCore vX.X.X`

If the device doesn't appear in Bluetooth scans, try powering it off and back on after flashing.
