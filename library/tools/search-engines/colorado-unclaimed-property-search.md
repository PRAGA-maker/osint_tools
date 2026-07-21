---
id: colorado-unclaimed-property-search
name: Colorado Unclaimed Property Search
description: Use when you have a `name` (person or business) and a Colorado connection and want to find unclaimed property/money the state holds for them — returns `address`, `associate`.
url: https://unclaimedproperty.colorado.gov/
category: search-engines
path:
- search-engines
bestFor: Searching Colorado's official unclaimed-property database by name to confirm a person/business had a Colorado footprint and surface last-known addresses.
selectorsIn:
- name
selectorsOut:
- address
- associate
status: live
pricing: free
costNote: Free official State of Colorado (Great Colorado Payback / Dept. of the Treasury) service; no account needed to search.
opsec: passive
opsecNote: A public government records search; you query the state's database, not the subject, so nothing is disclosed to the person. Still use a sock-puppet browser for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official State of Colorado Treasury site (unclaimedproperty.colorado.gov, the Great Colorado Payback); authoritative government record, not a third-party scraper.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- unclaimed-property-free-search-officially-endorsed-by-the-states-provinces-and-naupa
- colorado-licensed-professional-lookup
aliases:
- Great Colorado Payback
- Colorado unclaimed money search
tags:
- search-engines
- public-records
- unclaimed-property
- us-colorado
- toddington
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Colorado Unclaimed Property Search

> Colorado's official "unclaimed money" database — a free, authoritative name search that can confirm a subject's Colorado ties and last-reported address.

## When to use
You have a `name` (individual or business) and reason to think the subject lived, worked, or held accounts in Colorado. States hold "unclaimed property" — forgotten bank balances, uncashed checks, insurance payouts, utility deposits, safe-deposit contents — reported by the last holder with the owner's last-known name and address. A hit confirms the person existed at a Colorado address and can surface a mailing address and, sometimes, co-owners or related parties. Cheap, official corroboration for people-tracing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://unclaimedproperty.colorado.gov/ (the Great Colorado Payback).
2. Search by last name (add first name / city to narrow; broaden by omitting the first name to catch variants).
3. Review matches: each record shows the owner name, a reported address/city, the property type, and the reporting business (holder).
4. Note the reported address (a last-known location) and the holder — the holder (e.g. a specific bank or employer) is itself a lead tying the subject to an institution.
5. Pivot: repeat in other states via `[[unclaimed-property-free-search-officially-endorsed-by-the-states-provinces-and-naupa]]`, and feed the address into people-search / county-records tools.

## Inputs → Outputs
- **In:** `name` (individual or business), optionally + city
- **Out:** `address` (reported last-known address for the owner), `associate` (co-owners / reporting holder such as a bank or employer)
- **Empty/negative result looks like:** "no results found" — meaning no property is *reported* under that name in Colorado, which does not disprove a Colorado connection (much unclaimed property is never reported, or is filed under a variant name).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — an official public-records query; the subject is not notified.
- Name matches are not identity proof: common names collide, and the address is the *reported* one at the time of filing (often years old). Treat it as a lead to corroborate, and do not attempt to claim someone else's property.

## Overlaps ("do both")
- Pairs with `[[unclaimed-property-free-search-officially-endorsed-by-the-states-provinces-and-naupa]]` — that multi-state/NAUPA search covers other jurisdictions; run both so you don't miss a footprint in a neighboring state.

## Trust & verifiability
`trust: trusted` — it is the State of Colorado Treasury's own database, so a match is an authoritative government record (subject to the name-collision caveat above).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | colorado-unclaimed-property-search |
| category | search-engines |
| selectorsIn → selectorsOut | name → address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
