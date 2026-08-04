---
id: shipping-database
name: The Shipping Database
description: Use when you have a vessel `name` and want reference details about the ship — returns catalogued vessel/warship particulars (a static reference, not a live tracker).
url: https://theshippingdatabase.com/
category: transportation
path:
- transportation
bestFor: Looking up reference particulars for merchant ships and warships in a catalogued vessel database.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Free reference database; no account observed to be required for browsing entries.
opsec: passive
opsecNote: Read-only browsing of a public vessel-reference site — no interaction with any target and nothing tied to your subject beyond the site's own web-request logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community/hobbyist vessel-reference project (covering merchant and warship data); breadth and accuracy are uneven, so use it as a lead source and confirm particulars against an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- theshippingdatabase.com
tags:
- vessel-reference
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# The Shipping Database

> A catalogued reference of ships and warships — a static "look up the vessel's particulars" resource, distinct from the live AIS trackers.

## When to use
You have a vessel `name` and want background reference detail about the ship itself — type, class, particulars, and (for the warship coverage) service history — rather than its current position. Treat this as a starting reference to identify or disambiguate a vessel before moving to authoritative registries or a live tracker.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://theshippingdatabase.com/.
2. Browse or search for the vessel by `name`.
3. Read the catalogued entry: vessel type/class and available particulars.
4. Pivot: use the confirmed name/identifiers to query an AIS tracker like [[shippingexplorer]] for position, or an official ship registry for ownership and IMO details.

## Inputs → Outputs
- **In:** vessel `name`
- **Out:** reference particulars for the vessel (type/class/history) — keyed to the ship `name`, no position data
- **Empty/negative result looks like:** no catalogue entry for the name — the database is not exhaustive, so absence means "not catalogued here," not "vessel does not exist."

## Gotchas & OpSec
- This is a **static reference**, not a live tracker — it gives no current location.
- Coverage is uneven and community-maintained; verify anything load-bearing against an official registry (e.g. IMO/flag-state records).
- Direct access can be intermittent; if browsing is blocked, corroborate the vessel via a maritime registry instead.

## Overlaps ("do both")
- Pairs with live AIS trackers like [[shippingexplorer]] — this identifies and describes the vessel, the tracker locates it — and with official ship registries for authoritative ownership/IMO data.

## Trust & verifiability
`trust: community` — a hobbyist reference project; useful for identification leads but not authoritative, so confirm particulars against an official source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shipping-database |
| category | transportation |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
