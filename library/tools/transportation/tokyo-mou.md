---
id: tokyo-mou
name: Tokyo MOU PSC Database
description: Use when you have a ship `name` or IMO `document-id` and want its Asia-Pacific port-state-control inspection and detention history — returns operator org and inspection ports.
url: http://www.tokyo-mou.org/
category: transportation
path:
- transportation
bestFor: Pulling a vessel's inspection, deficiency and detention record across Asia-Pacific ports.
selectorsIn:
- name
- document-id
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Public PSC inspection search is free; no account required. A separate members' site exists for member authorities only.
opsec: passive
opsecNote: Passive lookup against a regional maritime authority's public database; you disclose only your own query, nothing to the vessel or its operator. Standard VPN hygiene is enough on sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Tokyo MOU, the official Asia-Pacific port state control organisation (22 member maritime authorities); inspection records are first-party regulatory data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Tokyo Memorandum of Understanding
- Asia-Pacific PSC database
tags:
- maritime
- transport
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Tokyo MOU PSC Database

> The Asia-Pacific port state control regime's inspection database — where and when a ship was inspected, what deficiencies were found, and whether it was detained.

## When to use
You have a vessel `name` or its IMO `document-id` and want its regulatory footprint in Asia-Pacific waters: which ports inspected it, what deficiencies were logged, and any detentions. In an investigation this places a specific ship at specific ports on specific dates and links it to its flag, operator and recognised organisation — useful for tracing cargo, ownership, or a person known to work a vessel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.tokyo-mou.org/ and follow the "PSC Database" / inspection search quick link.
2. Search by ship `name` or IMO number (`document-id`); flag/date filters narrow results.
3. Open an inspection record to read the port and date, deficiencies, action taken, and detention status.
4. Read the output: the inspection port is a `geolocation`+date fix; the company/operator field is an `employer-org` pivot.
5. Pivot: cross-reference the same IMO in the sibling Paris MoU / other regional PSC databases and in AIS trackers like `[[marinetraffic]]` to build a movement timeline.

## Inputs → Outputs
- **In:** ship `name` or IMO `document-id`
- **Out:** `geolocation` (inspection ports + dates), `employer-org` (company/operator, flag, recognised organisation), deficiency & detention history
- **Empty/negative result looks like:** no inspection on file — the vessel may simply never have been inspected in a Tokyo MOU port, or trades outside the Asia-Pacific region; check Paris MoU and other regional regimes.

## Gotchas & OpSec
- OpSec: passive; the vessel/operator learns nothing.
- Regional scope: only inspections at Tokyo MOU member ports (Asia-Pacific). A clean record here does not mean a clean record globally — check other MoUs.
- Ships are keyed by IMO number, which is permanent; the ship's *name* and flag change often, so prefer the IMO where possible.

## Overlaps ("do both")
- Pairs with `[[marinetraffic]]` — Tokyo MOU gives the regulatory inspection history and operator, MarineTraffic gives live/historical position tracks; together they place a vessel in time and space.

## Trust & verifiability
`trust: trusted` — first-party regulatory data from the official Asia-Pacific port state control organisation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tokyo-mou |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
