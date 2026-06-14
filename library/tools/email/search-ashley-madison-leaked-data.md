---
id: search-ashley-madison-leaked-data
name: Search Ashley Madison Leaked Data
description: Use when you have an email and want to check whether it appeared in the 2015 Ashley Madison breach — returns a breach hit/miss signal.
url: http://checkashleymadison.com/
category: email
path:
- email
bestFor: Confirming whether a target email was registered in the 2015 Ashley Madison data dump.
selectorsIn:
- email
selectorsOut:
- email
- metadata-exif
status: unknown
pricing: freemium
costNote: Basic email check is free; some breach-lookup mirrors gate full record detail behind payment.
opsec: passive
opsecNote: You submit the target email to a third-party site that you do not control; assume the query is logged. Use a sock-puppet connection, not infrastructure tied to the case.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent breach-lookup mirror of the 2015 Ashley Madison dump, not an official source; multiple sites use the checkashleymadison name and data quality/freshness varies.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- breach
- email
source: osint4all
lastVerified: ''
enrichment: full
---

# Search Ashley Madison Leaked Data

> Email-to-breach lookup against the 2015 Ashley Madison dump — answers "was this address registered on that site?"

## When to use
You have an `email` for a missing or sought person and want to know whether it was tied to an Ashley Madison account. A hit can corroborate a secret relationship, a hidden online life, an alternate identity, or a motive/destination lead — all useful in adult missing-persons and runaway/voluntary-disappearance cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://checkashleymadison.com/ in a sock-puppet browser session.
2. Enter the target `email` in the lookup box.
3. Read the result: a positive match means the address was present in the leaked registration data; a negative means it was not found in this mirror's copy.
4. Pivot: a hit suggests the person maintained a hidden online identity — cross-check that email against `[[skymem]]`, breach aggregators, and username searches to expand the footprint.

## Inputs → Outputs
- **In:** `email`
- **Out:** breach hit/miss signal (plus any account `metadata-exif` the mirror exposes)
- **Empty/negative result looks like:** "not found"/no match — does not prove the person never used the site, only that this address is not in this mirror.

## Gotchas & OpSec
- Several unaffiliated sites use the "checkashleymadison" name; data may be partial, stale, or monetized. Treat any hit as a lead, not proof.
- OpSec: passive but you are handing a target email to an untrusted third party. Never query from infrastructure or accounts linked to the investigation.

## Overlaps ("do both")
- Pairs with broader breach search engines because a single mirror may miss records; corroborate across sources before acting on a hit.

## Trust & verifiability
`trust: community` — community-run breach mirror, not an official Ashley Madison/Avid Life source; freshness and completeness are unverifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-ashley-madison-leaked-data |
| category | email |
| selectorsIn → selectorsOut | email → email, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
