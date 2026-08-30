# Observer from a Spare Companion + Computer

Already have a spare MeshCore node and any always-on computer? You can turn that pair into a mesh observer in a few minutes - no soldering, no dedicated hardware. The node stays in Companion mode and does the listening; the computer runs [meshcore-packet-capture](https://github.com/agessaman/meshcore-packet-capture), which reads every packet the node hears and publishes it to an MQTT broker.

This is the fastest path to feeding observer networks like the [LetsMesh Analyzer](https://analyzer.letsmesh.net/packets?region=AGS) and [Corescope](https://corescope.csramesh.org) with live CSRA traffic. If you'd rather build a purpose-made, deploy-and-forget unit, see the [Raspberry Pi + SX1262 observer](diy-rpi-observer.md) instead.

---

## What You Need

- **A spare MeshCore node running Companion firmware.** This is a normal companion node - the same kind you pair with the phone app. It stays plugged in and listening.
- **Any always-on computer** on the same location as the node - a Raspberry Pi, an old laptop, a mini PC, or a home server. Needs Python 3.11 or later.
- **A connection between the two**, either a USB cable or, for a WiFi-capable node, a network path (see below).

!!! warning "Companion radios only"
    meshcore-packet-capture works with nodes running **Companion** firmware only - not Repeaters or Room Servers. A repeater doesn't expose the packet stream the tool needs. If your spare node is currently a repeater, reflash or reconfigure it as a companion first.

---

## Connect the Node to the Computer

meshcore-packet-capture can reach the companion three ways. Pick whichever matches your setup - USB and TCP are the two most common for an always-on observer.

=== "USB (serial)"

    Plug the node into the computer with a USB cable. On Linux it usually appears as `/dev/ttyUSB0` or `/dev/ttyACM0`:

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM*
    ```

    This is the simplest and most reliable option when the node and computer sit next to each other.

=== "TCP (WiFi companion)"

    A node running a WiFi-capable companion build exposes a companion interface over TCP - by default on port `5000`. Point the tool at the node's IP address and no cable is required, so the node can sit anywhere on the same network as the computer.

    Confirm you can reach it first:

    ```bash
    nc -vz <node-ip> 5000
    ```

---

## Install meshcore-packet-capture

Pick whichever fits how you like to run things. The managed service script is the fewest steps; Docker is a natural fit if you already run containers.

=== "Managed service"

    A single command sets up a systemd (Linux) or launchd (macOS) service so the capture restarts on boot and after crashes:

    ```bash
    sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/agessaman/meshcore-packet-capture/main/install.sh)"
    ```

=== "Docker"

    Good if you already run containers and want the capture isolated with reproducible config. Clone the repo, then bring it up with compose:

    ```bash
    git clone https://github.com/agessaman/meshcore-packet-capture.git
    cd meshcore-packet-capture
    docker compose up -d
    ```

    Configure it with a volume-mounted `/etc/meshcore-packet-capture/config.toml` or `PACKETCAPTURE_*` environment variables (see the next section).

    !!! note "USB needs device passthrough"
        For a **USB** node the container needs access to the serial device - pass `--device=/dev/ttyUSB0` (and `--privileged` if your host requires it), or add the equivalent `devices:` entry to `docker-compose.yml`. A **TCP** node needs no passthrough, so Docker is cleanest there.

=== "pipx (CLI)"

    Best for testing interactively before committing to a service:

    ```bash
    pipx install meshcore-packet-capture
    meshcore-packet-capture --help
    ```

---

## Configure

Configuration lives in a TOML file under `/etc/meshcore-packet-capture/` (or set `PACKETCAPTURE_*` environment variables). The two things to get right are the **connection** to your node and the **MQTT broker** you're publishing to.

```toml
[connection]
# USB:  type = "serial"  with serial_ports set to your device
# TCP:  type = "tcp"     with host/port pointing at the node
type = "serial"
serial_ports = "/dev/ttyUSB0"
# For a WiFi companion instead, comment the two lines above and use:
# type = "tcp"
# host = "192.168.1.50"
# port = 5000

[[broker]]
name = "csra"
enabled = true
server = "mqtt.example.org"
port = 1883
username = "your-user"
password = "your-pass"
use_tls = false

[topics]
packets = "meshcore/{IATA}/{PUBLIC_KEY}/packets"
status  = "meshcore/{IATA}/{PUBLIC_KEY}/status"

[stats]
enabled = true
refresh_interval = 300
```

!!! tip "Use the AGS region code"
    The Augusta / CSRA region uses the IATA code **AGS**. The `{IATA}` variable in the topic templates should resolve to `AGS` so your packets land alongside the rest of the local traffic on the [LetsMesh Analyzer](https://analyzer.letsmesh.net/packets?region=AGS). Depending on your build you may set this as `PACKETCAPTURE_IATA=AGS` or in the config file.

!!! note "Broker credentials"
    Publishing to a shared observer network needs that network's broker address and credentials. Ask in the CSRA community for the current MQTT endpoint and login, or stand up your own broker (e.g. Mosquitto) if you just want to collect your own data.

The tool captures every packet locally but only uploads the packet types you choose. To narrow what's published to MQTT:

```toml
# In config, or PACKETCAPTURE_UPLOAD_PACKET_TYPES=0,1,2,4
upload_packet_types = "0,1,2,4"
```

---

## Run and Verify

If you used the service installer, start and check it:

```bash
sudo systemctl enable --now meshcore-packet-capture
sudo systemctl status meshcore-packet-capture
journalctl -u meshcore-packet-capture -f
```

To test interactively before committing to a service, run it in the foreground:

```bash
meshcore-packet-capture --verbose
```

You should see packets scrolling as the node hears mesh traffic. Confirm they're landing on the broker by subscribing from another machine:

```bash
mosquitto_sub -h mqtt.example.org -t 'meshcore/AGS/#' -v
```

Within a few minutes your node should also show up on the [LetsMesh Analyzer](https://analyzer.letsmesh.net/packets?region=AGS).

---

!!! note "This is one example setup"
    Connection types, broker details, and service management will vary with your hardware and network. Treat the values above as a starting point and adjust for your node, computer, and the observer network you're feeding. See the [meshcore-packet-capture README](https://github.com/agessaman/meshcore-packet-capture) for the full list of options.
