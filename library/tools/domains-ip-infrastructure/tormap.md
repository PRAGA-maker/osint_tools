---
id: tormap
name: TorMap
description: Use when you have an `ip-address` or `geolocation` and want to see whether it is a Tor relay and map/inspect the global Tor node network over time — returns relay metadata.
url: https://tormap.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Visualizing current and historical public Tor relays on a world map and checking whether a given IP is a known relay.
selectorsIn:
- ip-address
- geolocation
selectorsOut:
- ip-address
- geolocation
status: live
pricing: free
costNote: Free, open-source web app; no account required.
opsec: passive
opsecNote: You are querying a public dataset of Tor relay descriptors, not the subject or the Tor network itself. Nothing about your lookup reaches any target. Browse normally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (github.com/TorMap) built on official Tor Project relay archive descriptors; data provenance is the Tor Project, presentation is community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- tormap.org
- World City Map of Tor Nodes
tags:
- Maps, Geolocation and Transport
- Communications, Internet, Technologies
- tor
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# TorMap

> A time-travelling world map of public Tor relays, built from the Tor Project's own descriptor archive — use it to test "is this IP a Tor relay?" and to explore the network's geography.

## When to use
You have an `ip-address` that appeared in logs, a breach, or a subject's traffic and you need to know whether it is a public Tor relay (which changes how you interpret it — a relay/exit IP is shared infrastructure, not a subject's home connection). Or you have a `geolocation` and want to see the Tor relay footprint there, historically as well as now. TorMap plots current and past relays and lets you filter and search by relay attributes across time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tormap.org/.
2. Use the time slider to pick a date (relays as far back as October 2007 are available) — useful for checking whether an IP was a relay at the time of the event you're investigating.
3. Filter/search the relays (by flags such as Exit/Guard, family, country, etc.) or zoom to a region on the map.
4. Click a relay to inspect its details — IP, nickname, flags, bandwidth, first/last seen.
5. Pivot: if your IP matches a relay for the relevant date, treat it as Tor infrastructure (attribution stops there); if it does not appear as a relay, that IP was not a public relay at that time and other geo/hosting lookups apply.

## Inputs → Outputs
- **In:** `ip-address` to check, or a `geolocation` to explore
- **Out:** relay metadata — matching relay `ip-address`, `geolocation`, flags, bandwidth, first/last-seen dates
- **Empty/negative result looks like:** the IP does not correspond to any relay for the selected date. That is a meaningful negative — it was not a *public* relay then (bridges and private relays are not published and won't appear).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you query archived descriptors, never the live Tor network or the subject.
- Only *public* relays are covered. Tor bridges are deliberately unpublished, so an IP absent from TorMap can still be Tor bridge infrastructure. Always check the date: relay status changes constantly, so "is it a relay *now*" and "was it a relay *then*" are different questions.

## Overlaps ("do both")
- Pairs with IP-reputation and hosting-lookup tools — TorMap answers specifically "public Tor relay?" with historical precision, while general IP tools give ASN/geolocation/abuse context.

## Trust & verifiability
`trust: community` — the app itself is a community open-source project, but its underlying data is downloaded directly from the Tor Project's official relay descriptor archive, so relay facts trace back to an authoritative source and can be cross-checked against Tor Metrics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tormap |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, geolocation → ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
