---
id: australia-lookup
name: Australia Lookup
description: Use when you have an Australian `name` or `phone` and want a free residential address/phone match — returns address, phone and reverse-directory listings.
url: https://www.australialookup.com
category: people-search
path:
- people-search
bestFor: Free first-pass Australian people finder and reverse telephone directory from a name or number.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
status: live
pricing: free
costNote: Free directory built from public records, phone listings and opt-in data; no account required. Subjects can self-remove via a "Remove Listing" link, so coverage is partial.
opsec: passive
opsecNote: Passive against the target — it queries an aggregated public directory, not the subject's own accounts, so nothing is sent to them. The site logs your searches; use a clean browser. Because listings are opt-out, absence proves nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent Australian people/reverse-phone directory of unclear ownership and data freshness; treat hits as leads and corroborate against the White Pages or electoral/property records.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- zaba-search
aliases:
- AustraliaLookup.com
- Australian People Finder
tags:
- people-search
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Australia Lookup

> A free Australian people finder and reverse telephone directory — name or number in, residential address/phone out.

## When to use
Your subject has Australian ties and you have a `name` or a `phone` number to reverse. Australia Lookup is a quick, free first pass for a residential address or landline listing before moving to heavier sources (White Pages, electoral roll services, InfoTracer-style paid brokers). Useful early in an AU-focused trace to confirm a locality or seed an address pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.australialookup.com in a clean browser.
2. Choose people search (by name) or reverse telephone (by number) and submit.
3. Read the listing: matched `name`, residential `address`, and associated `phone`.
4. Pivot: an address feeds AU property/electoral and neighbour lookups; a confirmed suburb narrows further searches.

## Inputs → Outputs
- **In:** `name` or `phone`
- **Out:** `address`, `phone`, directory listing
- **Empty/negative result looks like:** no listing returned — likely unlisted, mobile-only, or self-removed via the opt-out link; not evidence the person doesn't exist.

## Gotchas & OpSec
- Opt-out directory: anyone can remove their listing, and mobiles are poorly covered, so misses are common.
- Data freshness is unverified — a listed address may be years old.
- OpSec: **passive**; no contact with the subject.

## Overlaps ("do both")
- Cross-check with Australia's official White Pages and, for cross-border subjects, a US broker like `[[zaba-search]]` — different directories index different people, and the overlap is where you gain confidence.

## Trust & verifiability
`trust: unverified` — an independent directory with opaque sourcing. Use it to generate leads, then confirm any address/phone against a primary Australian source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | australia-lookup |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → address, phone |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
