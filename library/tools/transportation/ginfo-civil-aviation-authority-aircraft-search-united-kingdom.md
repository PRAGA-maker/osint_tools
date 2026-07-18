---
id: ginfo-civil-aviation-authority-aircraft-search-united-kingdom
name: GINFO Civil Aviation Authority Aircraft Search (United Kingdom)
description: Use when you have a UK aircraft registration (`vehicle-plate`, a G- mark) and want its registered owner — returns owner `name` and `address`, aircraft type and status from the official CAA register.
url: https://siteapps.caa.co.uk/g-info/
category: transportation
path:
- transportation
bestFor: Turning a UK aircraft G-registration into the legally-recorded owner's name and address plus aircraft details.
selectorsIn:
- vehicle-plate
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free read-only web search of the official UK register; no account needed for the online lookup.
opsec: passive
opsecNote: An official statutory register, searched via the CAA's own site — the owner is not notified of a lookup. The CAA logs requests against your IP; use a clean session for arm's-length work. The register exists by law to be publicly inspectable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the UK Civil Aviation Authority; by law the register must list the names and addresses of aircraft owners and be publicly inspectable, so the data is authoritative for UK-registered aircraft.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- G-INFO
- CAA aircraft register
- UK aircraft registration search
tags:
- toddington
- curated-directory
- specialty-search
- aviation
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# GINFO Civil Aviation Authority Aircraft Search (United Kingdom)

> The UK CAA's public aircraft register — a G-registration in, the legally-recorded owner's name and address (plus aircraft type and status) out.

## When to use
You have a UK aircraft registration mark (the "G-" tail number, e.g. `G-ABCD`) — spotted on a photo, a flight-tracker, or tied to a subject — and want to know who owns it. Uniquely among vehicle registers, UK aviation law requires G-INFO to publish the **owner's name and address** and to be openly inspectable, so this is a rare public route from a registration straight to an identity and location. Also works in reverse for context: confirm an aircraft's type, base and registration status.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://siteapps.caa.co.uk/g-info/.
2. Enter the registration mark (`vehicle-plate`, e.g. `G-ABCD`) — you can also search by aircraft type or owner name.
3. Read the record: **registered owner name and address**, aircraft manufacturer/type, serial number, registration and de-registration dates, and status.
4. Pivot: the owner name + address feeds people-search and property records; the aircraft type/base feeds flight-tracking (ADS-B) tools to map movements.

## Inputs → Outputs
- **In:** UK registration mark (`vehicle-plate`)
- **Out:** owner `name` and `address`, aircraft type/serial, registration dates and status
- **Empty/negative result looks like:** "no match" — the mark isn't a current UK registration (it may be foreign-registered, de-registered, reserved-but-unused, or mistyped). Foreign aircraft need that country's register instead.

## Gotchas & OpSec
- Human-in-the-loop: none for the web search.
- OpSec: **passive** — the owner isn't alerted; only the CAA logs the query.
- The registered owner may be a **company, trust, or leasing entity** rather than the operator/individual actually flying it — treat a corporate owner as a lead to unwind, not the end.
- UK-only. For other countries use their civil aviation register (e.g. FAA registry for US N-numbers).
- Owner details reflect the current registration; recent sales may not yet be updated (register is refreshed each working day).

## Overlaps ("do both")
- Do both with ADS-B flight-tracking tools — G-INFO gives the owner identity, flight trackers give the aircraft's movements and base; together they connect a person to places and travel.

## Trust & verifiability
`trust: trusted` — first-party UK CAA statutory register; owner name/address are authoritative by law, with the only caveats being corporate-owner indirection and normal update lag.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ginfo-civil-aviation-authority-aircraft-search-united-kingdom |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
