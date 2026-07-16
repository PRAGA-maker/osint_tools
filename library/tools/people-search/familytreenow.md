---
id: familytreenow
name: FamilyTreeNow
description: Use when you have a US `name` and want a free deep people-search — returns `address` history, approximate `dob`/age, relatives and `associate` links, and past phone numbers.
url: https://familytreenow.com
category: people-search
path:
- people-search
bestFor: Free US people search with unusually rich relatives/associates and address history — no paywall for the core data.
selectorsIn:
- name
- address
selectorsOut:
- address
- associate
- dob
status: live
pricing: free
costNote: Genuinely free (ad-supported); most people-search sites tease then paywall, but FamilyTreeNow shows addresses, relatives, and associates without paying. No account required.
opsec: passive
opsecNote: Querying is passive and does not notify the subject. Note the ethical flip side — FamilyTreeNow is itself a doxxing concern, so if you are the subject consider its opt-out; as an investigator, browse from a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates US public records and marketing data; broad and free but can be stale or conflate namesakes — a strong lead source, not proof.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- family-tree-now
- voter-records
- thatsthem-phone-search
- familytree
aliases:
- Family Tree Now
- familytreenow.com
tags:
- people-investigations
- relatives
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# FamilyTreeNow

> One of the most useful free US people-search sites — address history, ages, and (crucially) a dense web of relatives and associates, all without a paywall.

## When to use
You have a US subject's `name` and want to build out their identity and network cheaply: current and prior `address`es, approximate `dob`/age, past phone numbers, and — its standout feature — lists of likely relatives and associates. That relatives/associates graph is invaluable for missing-persons work, giving you people to contact and alternate leads when the subject themselves is off-grid.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://familytreenow.com and search the subject `name` (add a state/city or approximate age to disambiguate).
2. Open the matching person record.
3. Read the fields: address history, age/`dob`, associated phone numbers, and the **Possible Relatives** / **Possible Associates** lists.
4. Follow relative/associate names into their own records to expand the network.
5. Pivot: addresses feed reverse-address lookups; relatives feed contact attempts and `[[voter-records]]`; phones feed `[[thatsthem-phone-search]]`.

## Inputs → Outputs
- **In:** `name` (+ location/age), or an `address` to see who's linked to it
- **Out:** `address` history, approximate `dob`/age, past phones, and `associate`/relative links
- **Empty/negative result looks like:** no record or an ambiguous cluster of namesakes — narrow with location/age; a common name will over-match, so corroborate before trusting a specific record.

## Gotchas & OpSec
- Data blends public records with marketing data — it can be outdated and can merge different people with the same name; verify against a second source.
- "Possible relatives/associates" are algorithmic and include false links (former co-residents, coincidental ties) — treat as leads.
- Ethical note: this is also a doxxing vector; respect its opt-out if handling your own or a protected subject's data.
- OpSec: passive; no notification to the subject. Use a sock puppet.

## Overlaps ("do both")
- Overlaps heavily with `[[family-tree-now]]` (same service/family) and complements `[[voter-records]]` and `[[thatsthem-phone-search]]` — cross-check addresses and relatives across all of them.

## Trust & verifiability
`trust: community` — a broad, free aggregator that is excellent for leads but not authoritative. Confirm any specific address/relationship against corroborating records before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familytreenow |
| category | people-search |
| selectorsIn → selectorsOut | name, address → address, associate, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
