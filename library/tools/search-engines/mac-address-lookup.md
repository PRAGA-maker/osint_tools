---
id: mac-address-lookup
name: MAC Address Lookup
description: Use when you have a `mac-address` (from a device, log, or capture) and want the hardware vendor/manufacturer behind it — returns the OUI-matched device maker.
url: https://maclookup.app/
category: search-engines
path:
- search-engines
bestFor: Resolving a MAC address prefix (OUI) to the device manufacturer.
selectorsIn:
- mac-address
selectorsOut:
- device-id
status: live
pricing: free
costNote: Free to search; free REST API and downloadable database (JSON/CSV/Cisco XML). Updated from the IEEE registry (last update noted July 2026).
opsec: passive
opsecNote: You look up a vendor prefix in a public IEEE-derived database; nothing touches the device owner. Fully passive. The MAC itself must come from a source you were authorised to access (a log, a capture, a device you control).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maps prefixes against the authoritative IEEE OUI registry; the vendor mapping is reliable, with the standard caveat that the OUI identifies the maker, not the specific device or owner.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- MAC Address Lookup
- maclookup.app
- OUI lookup
tags:
- mac-address
- oui
- device-identification
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# MAC Address Lookup

> Turn a MAC address into the hardware vendor behind it: the OUI (first half of the MAC) maps to the manufacturer registered with the IEEE.

## When to use
You have a `mac-address` — from a router's DHCP/ARP table, a Wi-Fi capture, a device you're examining, a leaked log, or router forensics — and you want to know what made the device. The first three octets (the OUI) identify the manufacturer (Apple, Samsung, Cisco, a specific IoT vendor), which helps you attribute a device on a network, distinguish a phone from a laptop from a camera, and corroborate what hardware a subject uses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://maclookup.app/ and paste the MAC address (e.g. `AC:DE:48:00:11:22`); only the OUI prefix is needed.
2. Read the manufacturer, the OUI block type (MA-L/MA-M/MA-S/CID/IAB), and registration details.
3. For bulk work, use the free REST API or download the database (JSON/CSV) and resolve OUIs offline.
4. Combine the vendor with context: an OUI plus a hostname/traffic pattern narrows the device type and role on a network.
5. Pivot: the device maker supports device attribution in an investigation; correlate with DHCP hostnames and other network artefacts.

## Inputs → Outputs
- **In:** `mac-address` (full address or just the OUI prefix)
- **Out:** `device-id` — the registered manufacturer, OUI block type, and registry detail
- **Empty/negative result looks like:** no vendor match, or a "locally administered/randomised" MAC — modern phones randomise Wi-Fi MACs for privacy, so the OUI may be meaningless; treat that as "randomised," not a real vendor.

## Gotchas & OpSec
- OUI ≠ owner: it identifies the manufacturer, never the person or the exact device model.
- Randomised MACs: iOS/Android randomise MACs per network, so a captured MAC often has a bogus/locally-administered OUI — don't over-attribute.
- Spoofing: MACs are trivially spoofable; a vendor match is a weak, corroborating signal only.
- OpSec: fully passive; ensure the MAC was obtained lawfully.

## Overlaps ("do both")
- Cross-check the OUI against the raw IEEE registry or another OUI database for confirmation, and combine with network-capture context (DHCP hostnames, traffic) — the vendor alone is a thin signal that gains meaning only alongside other device artefacts.

## Trust & verifiability
`trust: trusted` — the mapping derives from the authoritative IEEE OUI registry and is downloadable/auditable; reliable for vendor identification, with randomisation and spoofing the caveats to remember.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mac-address-lookup |
| category | search-engines |
| selectorsIn → selectorsOut | mac-address → device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
