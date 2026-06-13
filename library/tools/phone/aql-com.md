---
id: aql-com
name: aql.com
description: Use when you have a UK phone number and need its network operator (and ported status) from Ofcom data, to confirm carrier before further phone OSINT.
url: http://www.aql.com/telecoms/network-lookup/
category: phone
path:
- phone
bestFor: UK mobile/landline network (carrier) lookup based on Ofcom allocation and number portability.
selectorsIn:
- phone
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Basic allocation-based network lookup is free; a genuine "live" HLR lookup, foreign numbers, or the API require logging into the aql portal and each live lookup costs one SMS credit.
opsec: passive
opsecNote: Allocation-based lookup reads Ofcom range data and does not contact the handset. A genuine/live HLR lookup does query the network (active) — avoid unless needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: aql is an established UK telecoms/messaging carrier; network data is derived from official Ofcom number allocations.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
aliases:
- aql
- aql Network Lookup
tags:
- mobilephone
- Mobile & Phone Related
- carrier
- uk
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# aql.com Network Lookup

> UK telecoms carrier's free number-network lookup — tells you which operator a UK mobile/landline number belongs to (including ported numbers) using Ofcom data.

## When to use
You have a UK `phone` number and need to know the network operator and line type before deeper phone OSINT — e.g. to pick the right carrier-specific approach, sanity-check a number, or detect that a number has been ported away from its original range. This is metadata/enrichment, not subscriber identification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the network lookup at aql (web form: `portal.aql.com/telecoms/network_lookup.php`).
2. Enter the UK `phone` number (e.g. 0161... or 07...).
3. Read the result: current network operator and active/non-active state based on Ofcom allocation. For a genuine *live* (HLR) lookup or non-UK numbers, log into the aql portal — each live lookup spends one SMS credit.
4. Pivot: knowing the carrier and that the number is valid/ported feeds into subscriber-finding tools and helps avoid wasting effort on dead ranges.

## Inputs → Outputs
- **In:** `phone` (UK)
- **Out:** `metadata-exif` (carrier/network, line state, ported status — number metadata)
- **Empty/negative result looks like:** unallocated/invalid range or no operator returned, indicating a non-genuine or non-UK number.

## Gotchas & OpSec
- The free lookup is *allocation-based*: for a ported number it returns the correct current operator from range data, but for absolute certainty on live status you need the credit-based genuine lookup.
- UK numbers only on the free path; foreign numbers require login + credits.
- OpSec: the allocation lookup is passive; a *genuine/live* HLR lookup pings the network (active) — don't use it if you must stay passive.

## Overlaps ("do both")
- Pairs with `[[carrier-lookup]]` (US-focused) — use aql for UK carrier identification, carrierlookup for US; both establish line type before subscriber search.

## Trust & verifiability
`trust: trusted` — aql is a licensed UK telecoms/SMS carrier and the data comes from official Ofcom number allocations; carrier results are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aql-com |
| category | phone |
| selectorsIn → selectorsOut | phone → metadata-exif (carrier/network) |
| pricing / cost | freemium (live lookup costs SMS credit) |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
