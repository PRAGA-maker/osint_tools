---
id: mac-address-search-tool
name: Mac Address Search Tool
description: Use when you have a MAC address (or OUI prefix) and want the hardware vendor — returns the manufacturer/brand behind the address, and reverse (vendor → OUI ranges).
url: http://mac.lc
category: search-engines
path:
- search-engines
bestFor: Resolving a MAC address / OUI prefix to its device manufacturer, or a vendor to its OUI ranges.
selectorsIn:
- mac-address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free web lookup against the public IEEE OUI registry; no account.
opsec: passive
opsecNote: Passive — it queries a static registry of vendor prefixes, not any device or network. Looking up a MAC reveals nothing to the device's owner. The OpSec question is upstream: how you obtained the MAC (e.g. from a network capture) may itself be sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A thin front end over the public IEEE OUI/MA-L assignments; the vendor mapping is authoritative for the OUI portion, but note MACs can be randomised or spoofed, so a lookup identifies the assigned vendor, not necessarily the real device.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- mac.lc
- MAC vendor lookup
- OUI lookup
tags:
- Search engines
- mac-address
- oui
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Mac Address Search Tool

> A MAC-address ↔ vendor lookup: paste a full MAC or just its OUI prefix and learn which manufacturer registered it (or go the other way, vendor → prefixes).

## When to use
You have a `mac-address` — pulled from a device label, a router's client list, a network capture, EXIF/router logs, or an image of a device — and you want to identify the hardware maker. The first three bytes (OUI) are assigned by the IEEE to a manufacturer, so this tells you the brand of the network interface, a small but real pivot when attributing a device.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://mac.lc.
2. Search by full MAC (`AA:BB:CC:DD:EE:FF`), by OUI prefix (`AA:BB:CC`), or by vendor/brand name.
3. Read the result: the registered manufacturer for that prefix (the `employer-org`/vendor). A vendor-name search returns that maker's assigned OUI ranges.
4. Combine with context: e.g. an OUI resolving to "Hon Hai / Apple" alongside other clues supports a device-type hypothesis.
5. Pivot: knowing the device maker refines what other artefacts (default credentials, firmware behaviour, app ecosystem) to look for.

## Inputs → Outputs
- **In:** `mac-address` (full or OUI prefix), or a vendor name
- **Out:** the hardware manufacturer/brand (`employer-org`) for that OUI; or OUI ranges for a named vendor
- **Empty/negative result looks like:** "no vendor found" — the OUI is unassigned/private, or (very often now) the MAC is **randomised** by the OS for privacy. A randomised/locally-administered MAC (second-least-significant bit of the first byte set) has no real vendor and must not be attributed.

## Gotchas & OpSec
- Only the OUI (first 3 bytes) maps to a vendor — the rest is device-specific and not resolvable here.
- MAC randomisation (default on modern phones for Wi-Fi scanning) and spoofing make many MACs meaningless for attribution; check for locally-administered bit before trusting a result.
- A vendor tells you who made the NIC, not who owns or uses the device.
- OpSec: the lookup itself is passive and safe.

## Overlaps ("do both")
- Cross-check against another OUI database (Wireshark's manuf, macvendors.com) — they draw on the same IEEE registry, so agreement is expected and a mismatch flags a stale entry.

## Trust & verifiability
`trust: community` — a convenience front end over the authoritative IEEE OUI registry; the vendor mapping is reliable for real (non-randomised) OUIs, and the key caveat is randomisation/spoofing, not the data itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mac-address-search-tool |
