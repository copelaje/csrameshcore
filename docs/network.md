# CSRA MeshCore Network

The Central Savannah River Area (CSRA) MeshCore network covers Augusta, GA; North Augusta, SC; Aiken, SC; and surrounding communities across two states.

---

## Coverage Area

The CSRA network is designed to serve the following communities:

- **Augusta, GA** — city core and surrounding neighborhoods
- **North Augusta, SC** — across the Savannah River
- **Aiken, SC** — western Aiken County
- **Evans, GA / Columbia County** — fastest-growing part of the region
- **Grovetown & Harlem, GA** — Fort Eisenhower corridor
- **Martinez & Augusta South** — Richmond County south

Coverage is a community effort — the more nodes deployed, the better it gets for everyone.

---

## Network Topology

The CSRA network uses a combination of:

- **Portable/handheld nodes** — carried by individuals, form the bulk of the network during events or emergencies
- **Fixed relay nodes** — permanently deployed at elevated locations, provide backbone coverage 24/7
- **Home base nodes** — connected to home power, always on, relay for neighbors

```
                 CSRA MeshCore Network

    [Fixed Relay]      [Fixed Relay]      [Fixed Relay]
  Downtown Augusta     North Augusta      Evans / CSRA
          |                  |                  |
    ------+------------------+------------------+------
          |                  |                  |
    [Home Nodes]        [Handhelds]       [Home Nodes]
    (always on)        (when active)      (always on)
```

---

## Deploying a Fixed Relay Node

Fixed relay nodes are the backbone of the network. If you can deploy one, you make the network better for everyone in your area.

### Ideal Locations

- **Rooftops** — 1–2 story height gain dramatically increases range
- **Attic installations** — protected from weather, still elevated
- **On existing structures** — fence posts, flag poles, deck railings at height
- **High ground** — the CSRA is relatively flat; any natural elevation helps

### What You Need

- Any MeshCore-compatible device (see [Hardware](hardware.md))
- Power source — USB wall adapter, power bank, or solar setup
- Weatherproof enclosure if outdoors
- Configured with **Router** role and CSRA settings

### Node Role Configuration

Set your fixed node to **Router** role in the app settings. Router-role devices:

- Aggressively rebroadcast messages (help messages travel farther)
- Can be configured to skip the phone app entirely (headless mode)
- Should have Position set to **Fixed** with your GPS coordinates entered manually

---

## Community Guidelines

The CSRA MeshCore network is a shared resource. Please follow these guidelines to keep it working well for everyone:

1. **Use the correct channel settings** — off-spec nodes cause confusion and don't help the network
2. **Keep hop limit at 3** — higher values cause network flooding
3. **Set your node role appropriately** — handhelds should be `Client`, permanent nodes `Router`
4. **Share your location** — position broadcasting helps others see network coverage
5. **Be neighborly** — the public channel is for coordination, not spam
6. **Announce your node** — let the community know you've deployed a fixed relay so we can track coverage

---

## Getting Involved

The CSRA MeshCore community is volunteer-run and welcoming to newcomers at all technical levels. Ways to participate:

### On the Network
- Deploy a home base or fixed relay node to extend coverage
- Be active on the public channel, especially during events or severe weather

### In the Community
- **Introduce yourself** on the CSRA-1 public channel with your location and node type
- **Report coverage gaps** — tell us where you have trouble reaching the network
- **Help new users** — if someone is struggling with settings, assist if you can

### Technical Contributions
- Help maintain this documentation site
- Assist with node placement planning
- Participate in net events to test coverage

---

## Planned Coverage Expansion

The following areas are priorities for coverage improvement. If you live or work in these areas, deploying even a simple home node makes a real difference:

| Area | Current Status | Notes |
|---|---|---|
| Fort Eisenhower / Grovetown | Partial | Need relay at elevation |
| Aiken, SC core | Limited | Distance from Augusta nodes |
| Augusta south (Windsor Spring) | Sparse | Residential expansion needed |
| Savannah River corridor | Good | Natural radio path along river |
| North Augusta hilltop areas | Good | Elevation helps significantly |

---

## Severe Weather & Emergency Use

The CSRA experiences significant severe weather seasons — late winter ice storms, summer thunderstorms, and occasional hurricane remnants. The MeshCore network is a valuable tool during these events when cell towers become overloaded or lose power.

**During severe weather:**
- Keep your handheld node charged
- Monitor the CSRA-1 public channel for community updates
- If you have a solar-powered fixed node, it will likely remain operational through outages
- Share road conditions, power status, and safety information on the public channel

!!! note "MeshCore is not a substitute for 911"
    In a life-threatening emergency, always try 911 first. MeshCore is a community communication tool, not an emergency dispatch system.
