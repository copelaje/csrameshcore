# Buying Guide for Beginners

!!! info "Affiliate links"
    Amazon links on this page use our affiliate tag. **You pay the same price** — commissions go directly toward hardware for CSRA community relay nodes. If you're buying anyway, many thanks for using our links!

So you've heard about off-grid mesh messaging and want in. This page skips the theory and matches your situation to the fastest path to getting started.

---

## Where do you want to start?

<div class="grid cards" markdown>

- **[Just get on the network](#just-get-on-the-network)**

    I want to try messaging with the least friction and spend.

- **[Add a repeater node](#add-a-repeater-node)**

    I want to strengthen coverage or extend the network from a fixed location.

</div>

!!! tip "Want to build your own?"
    If you're interested in DIY builds — custom handheld nodes, Harbor Breeze tree node conversions, or magnetic mount repeaters — head to the [DIY Builds](diy-builds.md) section.

---

## Just Get on the Network

This is the "I want to see if this is for me" path. The trick: **buy two devices**. Having a second lets you test messaging back and forth between two phones right away — you'll get a feel for range, message relay, and network behavior in an afternoon rather than piecing it together gradually as you connect with others on the network.

Buying two of the same device keeps things simple — identical firmware, identical settings. But starting with two different devices is also worth considering: you'll naturally learn more about how form factor, antenna, and battery trade-offs play out in real use. Both approaches work. Pick what makes sense for you:

### Seeed SenseCAP T1000-E — Compact and Pocketable

Credit-card sized and only 6.5mm thick, the T1000-E is the most portable option. IP65 waterproof with built-in GPS, it slips into a pocket and goes anywhere with you.

![Seeed SenseCAP Card Tracker T1000-E](assets/hardware/t1000-e.jpg){ .product-image }

**~$50 each (~$100 for two)**

[Amazon](https://www.amazon.com/SenseCAP-Card-Tracker-T1000-Meshtastic/dp/B0DJ6KGXKB?tag=csrameshcore-20){ .md-button .md-button--primary } &nbsp; [Seeed Studio](https://www.seeedstudio.com/SenseCAP-Card-Tracker-T1000-E-for-Meshtastic-p-5913.html){ .md-button }

### Seeed Wio Tracker L1 Pro — Better Range and Battery Life

The L1 Pro steps up with a larger battery and an external antenna connector — a meaningful range improvement over the T1000-E's internal antenna. The trade-off is a bulkier form factor. If range matters more than pocket size, this is the pick.

![Seeed Wio Tracker L1 Pro](assets/hardware/wio-tracker-l1-pro.jpg){ .product-image }

**~$60 each (~$120 for two)**

[Amazon](https://www.amazon.com/seeed-studio-L1-Pro-Tracker/dp/B0FNCS5ST1?tag=csrameshcore-20){ .md-button .md-button--primary } &nbsp; [Seeed Studio](https://www.seeedstudio.com/Wio-Tracker-L1-Pro-for-Meshcore-p-6717.html){ .md-button }

!!! tip "Once you have your devices"
    Follow the [Getting Started guide](getting-started.md) — it walks through flashing firmware, installing the app, and connecting to the CSRA network step by step.

---

## Add a Repeater Node

Repeater nodes sit in a fixed location and re-broadcast messages, extending the reach of the network for everyone nearby. A good location — elevated, with clear line of sight — matters more than the hardware you pick.

---

### Buy a Pre-Built Repeater

#### Tree Node

**Best for:** Rural areas, wooded terrain, backyards — hang it high in a tree for above-canopy coverage.

**PeakMesh Altitude** — a solar-powered, weatherproof node designed specifically for tree-hanging deployment. Ships pre-assembled and MeshCore-ready. No flashing, no wiring — hang it and you're done.

![PeakMesh Altitude](assets/hardware/peakmesh-altitude.jpg){ .product-image }

**~$140**

[Etsy](https://www.etsy.com/listing/4331277320/peakmesh-altitude-tree-hanging-solar){ .md-button .md-button--primary }

---

#### Building / Rooftop Node

**Best for:** Urban and suburban coverage — mounted on a roofline, chimney, or exterior wall for broad neighborhood reach.

**Seeed SenseCAP Solar Node P1-Pro** — purpose-built for permanent outdoor deployment. Ships with MeshCore repeater firmware pre-installed, solar-powered, and includes GPS and an OLED display. The simplest path to a rooftop node.

![Seeed SenseCAP Solar Node P1-Pro](assets/hardware/solar-node-p1-pro.webp){ .product-image }

**~$90**

[Amazon](https://www.amazon.com/SenseCAP-Solar-Node-P1-Pro-Communication/dp/B0FMDHBWX8?tag=csrameshcore-20){ .md-button .md-button--primary } &nbsp; [Seeed Studio](https://www.seeedstudio.com/SenseCAP-Solar-Node-P1-Pro-for-Meshcore-p-6741.html){ .md-button }

---

#### Magnetic Mount Node

**Best for:** Vehicles, metal rooftops, or any situation where you want quick placement and easy repositioning.

!!! info "No tested commercial option yet"
    We don't have firsthand experience with a pre-built magnetic mount node. If you've found one that works well on MeshCore, let us know in the [Discord `#meshcore` channel](https://discord.com/invite/mgzj2PmhKf).

---

!!! info "What's next"
    - Follow the [Getting Started guide](getting-started.md) to flash firmware, install the app, and connect
    - The [Hardware Guide](hardware.md) covers antennas and enclosures in more detail
    - Interested in building your own repeater? See the [DIY Builds](diy-builds.md) section
