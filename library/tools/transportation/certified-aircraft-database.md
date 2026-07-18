---
id: certified-aircraft-database
name: Aircraft Registration Prefix Reference
description: Use when you have an aircraft tail number (`vehicle-plate`) and want to decode its country of registration — returns the `geolocation` (nation) a registration prefix maps to.
url: http://www.pilotfriend.com/aircraft%20performance/reg.htm
category: transportation
path:
- transportation
bestFor: Looking up which country an aircraft registration prefix (tail-number mark) belongs to.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free static reference page, no account.
opsec: passive
opsecNote: A static lookup table — you read a page, you query no one. Nothing about your subject is transmitted. Only your own IP hitting pilotfriend.com is exposed; use a VPN if the collection is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A hobbyist aviation reference (PilotFriend). The prefix-to-country mapping is stable ICAO-derived data, but the page is old and not actively maintained; verify current prefixes against ICAO for edge cases and recent changes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- PilotFriend aircraft registration prefixes
- aircraft nationality marks
tags:
- toddington
- aviation
- registration-prefix
- reference
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Aircraft Registration Prefix Reference

> A static table decoding aircraft registration prefixes (nationality marks) into the country that issued them — the first step in reading a tail number.

## When to use
You have an aircraft tail number or registration mark (from a photo, a spotting report, an ADS-B track) and need to know which country registered it. The leading prefix is a nationality code (e.g. `N` = United States, `G-` = United Kingdom), so this table turns raw markings into a `geolocation` before you go to a national registry for the specific airframe/owner. Purely a decode step, not an owner lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page and read the two-column Country / Marks table.
2. Match the leading letters of the tail number to a prefix row to get the registering country.
3. Note the country, then go to that nation's civil-aviation registry (or an ADS-B/registration database) to resolve the specific aircraft, operator, and history.
4. Watch for historical notes (e.g. prefixes reassigned over time) that can affect older sightings.
5. Pivot: the country + full registration feeds national aircraft registries and flight-tracking tools for owner/operator detail.

## Inputs → Outputs
- **In:** `vehicle-plate` (aircraft tail number / registration mark)
- **Out:** `geolocation` (country of registration) derived from the prefix
- **Empty/negative result looks like:** the prefix isn't in the table (very new/reassigned code, or a mis-read mark) — fall back to the current ICAO nationality-mark list rather than assuming the aircraft is unregistered.

## Gotchas & OpSec
- Reference only: it gives the country, never the owner — that requires the relevant national registry.
- The page is dated; a few prefixes have changed since (it even notes a 2002 reassignment). Verify unusual or recent marks against ICAO.
- Fully passive; no target interaction of any kind.

## Overlaps ("do both")
- A pre-step to the aircraft-registry and flight-tracking tools in the [[transportation]] set — decode the country here, then those tools resolve the individual airframe and operator.

## Trust & verifiability
`trust: community` — a hobbyist reference reflecting stable ICAO prefix conventions. Good enough for the country-decode step; confirm current/edge-case prefixes against the authoritative ICAO list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | certified-aircraft-database |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
