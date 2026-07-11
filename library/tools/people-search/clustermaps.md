---
id: clustermaps
name: ClustrMaps
description: Use when you have a `name` or `address` and want US resident/address intelligence — returns current and past residents, relatives/neighbors, phones and property/household detail.
url: https://clustrmaps.com/
category: people-search
path:
- people-search
bestFor: Reverse-address and name lookups that reveal who lives (or lived) at a US address plus their relatives, neighbors and phones.
selectorsIn:
- name
- address
selectorsOut:
- address
- phone
- associate
status: live
pricing: freemium
costNote: Free to browse a lot of address/resident data; deeper "background report" detail is upsold via paid third-party partners. No account needed for basic lookups.
opsec: passive
opsecNote: A data-broker aggregation of public/commercial records — searching does not notify the subject. It is broker data, so treat outputs as leads to corroborate, and mind privacy law when handling third-party PII. Use a sock-puppet browser. (If YOU are the subject, ClustrMaps offers an opt-out.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ClustrMaps is a widely-used address/people aggregator compiling public and commercial records. Data is often stale or conflated (old residents shown as current); reliable as a lead source, not as proof.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- clustrmaps.com
- Clustermaps
tags:
- people-investigations
- people-search
- reverse-address
- data-broker
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ClustrMaps

> A free-to-browse US address/people aggregator — enter an address to see who lives or lived there, or a name to find their addresses, relatives, neighbors and phones.

## When to use
You have a US `address` and want its residents (current and historical), or a `name` and want their address history plus relatives and associated phones. Strong for reverse-address work — building the household and neighbor graph around a location — and for enriching a name into contact leads before spending on paid people-search. A go-to free complement to TruePeopleSearch/FastPeopleSearch.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://clustrmaps.com/ in a sock-puppet browser.
2. Search by `address` (reverse) or by `name` (+ state/city to disambiguate).
3. Read the record: current/past residents, listed relatives and neighbors (`associate`), phone numbers, and household/property detail.
4. Note the "lived here" dates to distinguish current from former occupants.
5. Pivot: relatives/neighbors feed further people-search; phones feed reverse-phone tools; the address history corroborates or extends a subject's timeline.

## Inputs → Outputs
- **In:** `address` (reverse) or `name`
- **Out:** current/former residents, relatives & neighbors (`associate`), `phone`, address history (`address`)
- **Empty/negative result looks like:** thin or no record, or clearly outdated residents — the address is new/commercial, the person opted out, or the data simply hasn't been refreshed. Cross-check a second aggregator before trusting a "current" resident.

## Gotchas & OpSec
- Broker data is frequently STALE — it commonly lists former residents as current; always corroborate with a fresher source.
- US-only; sparse or absent for recent movers and opt-outs.
- "Background report" buttons route to paid partners; the free listing is usually enough for leads.

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch-com]]`, `[[fastpeoplesearch-com]]` and `[[melissadata]]` — each aggregator holds a slightly different slice/vintage of the same records, so run several and reconcile before concluding who currently lives at an address.

## Trust & verifiability
`trust: community` — a mainstream but broker-sourced aggregator; useful and broad, but accuracy/recency vary, so treat every result as a lead to confirm elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | clustermaps |
| category | people-search |
| selectorsIn → selectorsOut | name, address → address, phone, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
