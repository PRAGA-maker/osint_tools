---
id: whoishere-py
name: whoishere.py
description: Use when you have monitor-mode WiFi hardware on-site and want to detect a person's presence via their device's probe requests — returns mac-address, device-id and a mapped name.
url: https://github.com/hkm/whoishere.py
category: geolocation
path:
- geolocation
bestFor: On-site physical-presence detection — passively sniffing 802.11 probe requests to tell when a known device (person) is nearby.
selectorsIn:
- mac-address
- device-id
selectorsOut:
- mac-address
- device-id
- name
status: live
pricing: free
costNote: Free and open source (GitHub); the only cost is a WiFi adapter capable of monitor mode.
opsec: active
opsecNote: RF sniffing is receive-only so it emits nothing and doesn't touch the subject's device — but it requires YOU to be physically on-site with monitor-mode hardware, and passive interception of wireless traffic is legally restricted in many jurisdictions. Confirm you are authorized before deploying.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: A small but real open-source project (hkm/whoishere.py); it does what it claims but requires correct hardware/driver setup and manual device-to-person mapping.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- whoishere
- hkm/whoishere.py
tags:
- wifi
- probe-request
- device-tracking
- physical
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-19'
enrichment: full
---

# whoishere.py

> A Python WiFi sniffer that names devices from their 802.11 probe requests — an on-site tool for confirming that a specific person's device (and thus the person) is physically present.

## When to use
You are physically at or near a location and want to know whether a known device is there — a phone whose `mac-address` you've previously identified. Phones periodically broadcast probe requests looking for known networks; whoishere.py passively listens for these and can alert when a MAC you've labelled (`device-id` → `name`) appears in range. Situational but powerful for confirming presence at an address in an authorized surveillance/search context.

## How to use it (`bestInteractionPattern`: cli)
1. Get a WiFi adapter that supports **monitor mode**; set it into monitor mode (e.g. `airmon-ng`).
2. Clone and install: `git clone https://github.com/hkm/whoishere.py` and install its Python dependencies.
3. Populate the known-devices mapping (MAC → label/`name`) so alerts are meaningful.
4. Run the sniffer on the monitor interface; it logs/announces probe-request MACs, flagging known ones as they come into range.
5. Pivot: a confirmed presence corroborates an address/timeline; an unknown recurring MAC becomes a new `device-id` to attribute.

## Inputs → Outputs
- **In:** a target `mac-address`/`device-id` (labelled in the known-devices list), plus on-site monitor-mode hardware
- **Out:** detected `mac-address`es in range, mapped `name`/`device-id` for known ones, presence/timing
- **Empty/negative result looks like:** no probe requests from the target — modern phones use **MAC randomization** when not associated to a known network, so a device may never broadcast its real MAC; absence does NOT prove the person isn't there.

## Gotchas & OpSec
- MAC randomization (iOS/Android default) is the big limitation — real hardware MACs often only appear when the phone associates to a known SSID.
- Requires physical proximity and monitor-mode hardware/drivers; setup is fiddly.
- Human-in-the-loop: you must map MAC→person yourself, and interpret hits.
- OpSec/legal: **active deployment** — you are physically present, and wireless interception is legally constrained in many places; get authorization first.

## Overlaps ("do both")
- Complements other physical-presence and device-identification methods — pair with prior device attribution (a MAC captured when the phone was on a known network) so you have a non-randomized MAC to watch for.

## Trust & verifiability
`trust: community` — a genuine open-source tool that reliably reports the probe requests it hears; the weak link is attribution (MAC→person) and randomization, which you must account for, not the sniffing itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whoishere-py |
| category | geolocation |
| selectorsIn → selectorsOut | mac-address, device-id → mac-address, device-id, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (manual-review) |
