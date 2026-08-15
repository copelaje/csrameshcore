# A Technical Case for MeshCore over Meshtastic for EmComm

I ran Meshtastic in the CSRA before I ran MeshCore, and Meshtastic is how a lot of us found LoRa mesh in the first place. This page is not a knock on that project or the people running it. It is an explanation of the specific technical reasons I believe MeshCore is superior for emergency communications, written so it can be linked into a conversation instead of retyped every time the question comes up.

The short version: Meshtastic optimizes for a casual, self-configuring network of chatty devices. That is a legitimate goal, and it produces impressive-looking maps. But several of the design choices that make it work at that scale actively undermine the thing EmComm actually needs, which is getting a specific message to a specific person several hops away and knowing that it arrived.

!!! note "Scope and timing"
    My hands-on Meshtastic testing was current as of **late 2025**. Meshtastic is actively developed and this is a moving target. As my Meshtastic friends let me know of changes I'll attempt to keep this comparison current. Any updates that make our EmComm options more reliable are much appreciated!

---

## The Bar for EmComm Is Different

Most mesh demos measure the wrong thing. "I can see 200 nodes" and "the public channel is busy" are both compatible with a network that cannot reliably deliver a direct message to the person you need.

For emergency use, the network has to do three things:

1. Deliver a message to a **specific recipient**, not just to whoever happens to be listening.
2. Deliver it across **however many hops separate you**, not just to your immediate neighbors.
3. Tell you **whether it actually arrived**, so you know whether to retry or find another way.

Every point below is a place where Meshtastic's architecture makes one of those three harder, and where MeshCore's makes it easier.

---

## 1. Seeing a Node Is Not the Same as Talking to It

This is a common misunderstanding, and it is the reason people are surprised when a network that looks healthy performs badly.

Your node's list of surrounding nodes is **cumulative**. A distant node needs exactly **one** nodeinfo to reach your receiver in order to display on your map. Once it is there, it stays. Nothing about that entry tells you how many of its transmissions you missed to get it.

Now consider a node you receive at a 20% success rate. Over an afternoon of it beaconing, one such packet gets through, and it lands on your map looking exactly like a node you receive at 95%. But 20% is extremely unreliable (basically unusable) for messaging.

Showing up and getting through are not the same job:

| | What it takes |
|---|---|
| **Showing up on your map** | One nodeinfo packet, at any point in history |
| **Delivering a message** | Every hop, in sequence, right now |
| **Delivering a message and knowing it arrived** | Every hop, in sequence, in **both directions**, right now |

Your map is reporting the best moment ever recorded. **Messaging** depends on something much closer to the product of the per-hop success rates at the instant you press send. Even generous-looking numbers compound badly: three hops at 70% per hop is only 34% chance of success one way, and just 12% for a round trip. At the same time you can have both a map full of neighbors and a channel you cannot depend on! This defies most folks' expectations and can make them overconfident of Meshtastic's EmComm capabilities.

!!! note "Public maps have a second, separate problem"
    Online Meshtastic maps are inflated further by MQTT. Nodes get injected into the map over the internet without any RF path to your area at all. That is worth knowing, but it is a distinct issue. The effect described above happens on a clean, RF-only setup with no MQTT anywhere near it.

**The honest test** is not how many nodes you can see. It is picking a node several hops out and measuring how often a direct message to it gets a confirmed reply. If you don't have a friend to test with, run an in app [traceroute](https://meshtastic.org/docs/software/android/user/discovery/#traceroute) against that same node and see what the success rate looks like.

---

## 2. The Hop Ceiling Is Low, and the Default Is Lower

Meshtastic carries its [hop limit](https://meshtastic.org/docs/configuration/radio/lora/#max-hops) in a **3-bit field**. Seven hops is not a tuning recommendation or a practical guideline, it is the hard ceiling of the protocol[^zerocost]. The shipped default is **3**, and reliability degrades well before you approach the ceiling anyway, for the compounding reason described above.

In practice on our mesh, MeshCore reliably handles **5+ hop direct messages**, and the constraint is the size/spread of the current local mesh rather than anything in the protocol. I've seen considerably more than that when traveling in larger, more established meshes. When atmospheric ducting opens up and links us into wider meshes, paths in the range of **15 hops** work. I've had bi-directional chats to Ohio from CSRA! As we keep building out we'll become constantly connected to the wider mesh.

The comparison worth making is ceiling to ceiling and real-world to real-world. Meshtastic's ceiling is 7 and its real-world useful range is a small number of hops. MeshCore's real-world useful range already exceeds Meshtastic's protocol ceiling.

---

## 3. You Cannot Tell "Delivered" from "Lost"

This one matters more than anything else on this page for emergency use.

**Meshtastic gives you no dependable way to know that your message reached the person you sent it to.** Nothing comes back from the recipient's own device that you can count on, so there is no signal that separates a delivered message from a lost one.

That claim surprises people, because the app does put a check-mark on direct messages. The check-mark is real, but it does not mean what most users assume. Meshtastic leans on **implicit acknowledgments**: when your node hears a neighbor one hop away rebroadcast your packet, it treats that as the message making progress and marks it. What you are being told is "a nearby node passed this along." The person you were writing to may be four hops beyond that neighbor and may never have seen it.

The check-mark answers a question you did not ask. It tells you your packet left the neighborhood, not that it arrived. When you send a message, without manual response from the end user you cannot distinguish:

- It reached them and they have not replied yet
- It reached them and their reply was lost
- It never got there at all

Those three situations call for completely different responses, and the network will not tell you which one you are in. Retrying becomes guesswork, and in an actual emergency you burn time and airtime resending things that already arrived while giving up on things that never did.

MeshCore gives you an **end-to-end acknowledgment generated by the recipient's device**. A confirmed message is confirmed by the endpoint, not inferred from a relay. That single property changes the character of the network: silence becomes information, and retry becomes a decision instead of a guess.

---

## 4. Managed Flood Can Silently Truncate Paths

Meshtastic uses "managed flood routing". When a node hears a neighbor rebroadcast a packet it was about to rebroadcast itself, it suppresses its own transmission[^roles].

The assumption baked into that behavior is that the neighbor's coverage substantially overlaps your own. When it does, this is a genuinely clever airtime optimization. When it does not, and in real terrain with real antenna heights it frequently does not, the flood **truncates**. Your node was the only path into some branch of the network, it stayed quiet because a neighbor spoke, and that neighbor cannot reach the nodes you can.

The failure mode is what makes this hard:

- It is **silent**. No error, no indication that a branch was pruned.
- It is **intermittent**. Whether suppression happens depends on timing and which node wins the rebroadcast race for that particular packet.
- It is **path-dependent**. Some destinations become unreachable while others in the same direction stay fine, which makes it look like a hardware problem at the far end.

Combine this with the acknowledgment gap in the previous section and you get the characteristic Meshtastic EmComm experience: messages that mostly work, sometimes do not, and never tell you which.

MeshCore takes a different approach. Full flooding is used for **discovery**, to find a path to a contact. After that, traffic follows the **known path** to that contact. Rather than every message being a fresh flood that has to be suppressed to stay affordable, the expensive operation happens once and the routine operation is cheap and deterministic.

---

## 5. Underneath All of It: Airtime Economics

The four points above are connected, and the connection is how each network spends its airtime budget.

Meshtastic clients are chatty by default. Position, telemetry, and node info go out automatically from every device on the network. Those intervals are configurable, and a carefully tuned node can be much quieter, but defaults are what the majority of a network actually runs, and you do not control anyone else's settings. Every one of those packets is flooded, and every flood is multiplied by the number of nodes that rebroadcast it. On a healthy, growing network, that traffic scales badly, and it competes directly with the messages people are actually trying to send.

The flood management in section 4 is largely a **response** to that pressure. It exists to buy back airtime that automatic housekeeping traffic consumes. So the reliability cost is not really the price of good routing, it is the price of paying for chatter.

MeshCore starts from the other end:

- **Clients are quiet.** A companion node is not broadcasting telemetry into the mesh as a matter of course.
- **Relaying is an explicit role.** Repeaters are deployed deliberately, with placement and antennas chosen for the job, instead of every handheld in a parking lot participating in routing.
- **Discovery is separated from delivery.** Flooding happens when you need to find someone, not on every packet.

The result is that the airtime budget goes toward messages, which is why the hop counts in section 2 are achievable without the suppression tricks that cause section 4.

---

## Where Meshtastic Is Still the Right Choice

To be fair about it, this is not a case that MeshCore wins everywhere:

- **You already have an established local Meshtastic network.** Coverage is the product of participation, and switching costs are real. A network you are actually on beats a better protocol nobody near you runs.
- **Your use case is group activity tracking.** Automatic position reporting for a hiking or event group is a real feature, and it is the exact behavior MeshCore deliberately suppresses. It is not impossible with MeshCore, but you'll definitely find more friction.
- **You want the largest install base and app ecosystem.** Meshtastic has a substantial head start on both.
- **Casual broadcast chat is the goal.** If nobody is depending on delivery confirmation, most of this page does not apply to you.

That first point deserves an honest caveat, because taken to its conclusion it argues against ever adopting anything. Every mesh in every region started with one person running something nobody else had yet, Meshtastic very much included. Switching cost is a one-time price, while protocol ceilings are permanent. The question is not whether moving is free, it is whether where you end up is better enough to be worth the move.

It also does not have to be a clean break. Much of the popular hardware flashes either firmware, so you can stand up a MeshCore node alongside the Meshtastic one you already run and measure the difference on your own terrain rather than taking my word for any of this.

The argument here is specifically about **emergency communications**, where a specific recipient, a real hop count, and confirmed delivery are requirements rather than nice-to-haves. EmComm is by far my primary motivation for getting into mesh so it weighs heavily for me, but you must consider your own objectives and make choices that make sense.

---

## Bottom Line

Meshtastic answers "who is out there?" very well. MeshCore answers "did my message get to that person?" very well. For EmComm, the second question is the one that matters, and it is the one I struggled with on Meshtastic.

If you want to see the local network for yourself before deciding, CSRA mesh is open and the barrier to entry is a $40 device.

[Getting Started](getting-started.md){ .md-button .md-button--primary } &nbsp; [Network Coverage](network.md){ .md-button }

---

[^zerocost]: Meshtastic has introduced some [zero-cost configs](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/) that can be used to stretch this out a little more in specific scenarios.

[^roles]: To be fair, Meshtastic does have a number of ["device roles"](https://meshtastic.org/docs/configuration/radio/device/#roles) that can be configured to modify this behavior, but from a whole net perspective you are beholden to others setting things appropriately, and if they set wrong it can make things even worse. Also what is "right" can change in time as the net changes, which can make things confusing, even for those who are quite experienced.
