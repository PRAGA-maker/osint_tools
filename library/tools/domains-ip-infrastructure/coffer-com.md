---
id: coffer-com
name: coffer.com (MAC_Find)
description: Use when you have a `mac-address` and want the hardware vendor behind it — returns the manufacturer/OUI owner, and the reverse (a vendor's MAC ranges).
url: http://www.coffer.com/mac_find/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Resolving a MAC address prefix (OUI) to its hardware manufacturer, or listing a vendor's MAC ranges.
selectorsIn:
- mac-address
selectorsOut:
- device-id
- employer-org
status: degraded
pricing: free
costNote: Free web lookup, no account. Caveat — the underlying OUI database was last refreshed around 2013, so newer allocations may be missing.
opsec: passive
opsecNote: A purely local lookup of a MAC prefix against a static vendor table; you contact no target and reveal nothing about a subject. Standard passive web use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: "The self-described “Internet’s oldest online MAC address database”; the OUI mapping is accurate for its era but stale (≈2013), so confirm modern prefixes against a current source."
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- MAC_Find
- coffer MAC lookup
- OUI lookup
tags:
- domainsandips
- Domains & IPs
- mac-address
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# coffer.com (MAC_Find)

> A long-standing MAC-address-to-vendor lookup: paste an OUI prefix and learn which manufacturer made the device — handy for attributing hardware seen in logs, EXIF, or captures.

## When to use
You have a `mac-address` (full address or just the first 6 hex digits / OUI) — from router logs, a network capture, device metadata, or an image's embedded data — and want to know the hardware manufacturer. It also works in reverse: give a vendor name and get the MAC ranges assigned to it. This attributes a device to a maker, which can corroborate what equipment a subject used.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.coffer.com/mac_find/ .
2. Enter a `mac-address` in any common format (`00:13:A9`, `00-80-C7`, or a full `08:00:69:02:01:FC`) to get the vendor; or enter a vendor name to list its MAC ranges.
3. Read the result: the manufacturer/OUI owner (`employer-org`) tied to that prefix (a `device-id`-level attribution).
4. Pivot: the vendor narrows the device type (e.g. an Apple vs. Cisco prefix), which corroborates other device/EXIF evidence.

## Inputs → Outputs
- **In:** `mac-address` (or a vendor name for the reverse lookup)
- **Out:** hardware manufacturer / OUI owner (`employer-org`), device attribution (`device-id`)
- **Empty/negative result looks like:** no match for the prefix — likely a **newer OUI** the 2013-era database never captured, or a locally-administered/randomised MAC (common on modern phones), not proof the prefix is invalid.

## Gotchas & OpSec
- The database is **stale (~2013)** — for anything allocated since, cross-check a current OUI source (IEEE registry, maclookup); treat a "no match" as "check elsewhere."
- Modern devices randomise MACs for privacy, so a captured MAC may be ephemeral and not vendor-attributable at all.
- Only the OUI (first 3 bytes) identifies the vendor; the remaining bytes are device-specific and not resolvable to an owner here.
- OpSec: fully passive — a static table lookup.

## Overlaps ("do both")
- Pair with a current IEEE OUI lookup — coffer is quick and covers historic prefixes, while an up-to-date registry catches allocations made after 2013.

## Trust & verifiability
`trust: community` — a venerable, accurate-for-its-time database; reliable for older OUIs but explicitly outdated, so verify recent prefixes against a maintained source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coffer-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | mac-address → device-id, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
