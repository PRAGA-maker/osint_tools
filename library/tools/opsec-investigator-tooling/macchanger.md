---
id: macchanger
name: macchanger
description: Use when you want to spoof or randomize the `mac-address` of your own network interface for investigator OpSec — returns/sets a new hardware MAC.
url: https://github.com/alobbs/macchanger
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Randomizing the investigator's hardware MAC before joining a network so the real adapter address isn't logged.
selectorsIn:
- mac-address
selectorsOut:
- mac-address
status: live
pricing: free
costNote: Free and open source (GPL-3.0); packaged in Debian/Ubuntu/Kali as `macchanger`.
opsec: passive
opsecNote: Purely defensive — it changes YOUR adapter's MAC, not a target's. Nothing leaves your machine. Change the MAC before associating with a network; a MAC set after you're already connected may still have leaked the original. Some networks flag randomized/locally-administered MACs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Long-standing GNU/open-source utility (alobbs/macchanger), shipped in mainstream distro repos and installed in the Trace Labs OSINT VM.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- GNU MAC Changer
- macchanger
tags:
- opsec
- network
- mac-address
source: tracelabs-repos
lastVerified: '2026-07-23'
enrichment: full
---

# macchanger

> A GNU command-line utility for viewing and spoofing the MAC address of a network interface — pure investigator OpSec.

## When to use
You are about to connect an investigation machine to a network (public Wi-Fi, a burner hotspot, a lab segment) and don't want your adapter's real, hardware-burned `mac-address` recorded by the access point or DHCP logs. Run macchanger first to present a randomized or chosen MAC. This is a hygiene step, not an investigative lookup.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `sudo apt install macchanger` (Debian/Ubuntu/Kali) — it is preinstalled in the Trace Labs VM.
2. Bring the interface down: `sudo ip link set dev wlan0 down`.
3. View the current/permanent MAC: `macchanger -s wlan0`.
4. Set a random MAC: `sudo macchanger -r wlan0` (or `-a` for a same-vendor random MAC, or `-m XX:XX:XX:XX:XX:XX` for a specific one).
5. Bring it back up: `sudo ip link set dev wlan0 up`, then connect.
6. Restore the hardware MAC afterward with `sudo macchanger -p wlan0`.

## Inputs → Outputs
- **In:** your interface name plus (optionally) a desired `mac-address`
- **Out:** the interface's new/spoofed `mac-address`
- **Empty/negative result looks like:** "ERROR: Can't change MAC" — usually the interface is still up or the driver forbids it; bring the link down first, or the hardware doesn't support it.

## Gotchas & OpSec
- Change the MAC **before** associating — doing it mid-session may have already leaked the real address.
- Randomization is reset on reboot unless scripted; re-run per session.
- Locally-administered/randomized MACs can themselves be a fingerprint on networks that expect vendor OUIs.

## Overlaps ("do both")
- Complements full-VM OpSec setups (e.g. the Trace Labs image) — MAC spoofing covers the link layer while a VPN/Tor covers the network layer; do both for a clean footprint.

## Trust & verifiability
`trust: trusted` — a mature, widely-audited GNU tool distributed through official distro repositories; the code is open and its behavior is well understood.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | macchanger |
