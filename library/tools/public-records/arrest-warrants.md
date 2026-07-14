---
id: arrest-warrants
name: BlackBookOnline — Arrest Warrants
description: Use when you have a `name` and want to find an outstanding US arrest warrant — a directory routing you to free state/county warrant searches, returning name, dob, and document-id (warrant/case) leads.
url: https://www.blackbookonline.info/usa-arrest-warrants.aspx
category: public-records
path:
- public-records
bestFor: Finding the right free official arrest-warrant search for a US jurisdiction, as a gateway to checking whether a person has an active warrant.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free public-records directory; the destination county/state warrant searches it links to are also free.
opsec: passive
opsecNote: Browsing the directory is passive. The linked jurisdiction searches are official public-records sites; querying them does not notify the subject, but use normal sock-puppet browsing hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: BlackBookOnline is a long-running, reputable public-records portal (run by PI Robert Scott / The Open Data People); it curates links but the underlying data quality belongs to each jurisdiction.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- blackbookonline
- vinelink
aliases:
- Black Book Online arrest warrants
- USA arrest warrant search directory
tags:
- court
- inmate
- warrants
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# BlackBookOnline — Arrest Warrants

> A curated directory of free, official US arrest-warrant searches, organized by state — the fastest way to reach the right jurisdiction's warrant lookup.

## When to use
You have a `name` and want to know whether the person has an outstanding arrest warrant in the US — a possible explanation for a disappearance, or a lead on where they've had contact with the justice system. Warrant data is fragmented across thousands of county and state systems; this page is the index that routes you to the correct free official search for a jurisdiction instead of guessing URLs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackbookonline.info/usa-arrest-warrants.aspx.
2. Pick the state (and it will point you to county/agency warrant searches where available).
3. Follow the link to the official jurisdiction search and query by `name`.
4. Read results on the destination site: outstanding warrants with the subject's name, often DOB and a warrant/case number (`document-id`).
5. Empty result → no warrant in that jurisdiction's indexed system; repeat for other relevant counties/states.

## Inputs → Outputs
- **In:** `name` (plus the jurisdiction you're checking)
- **Out:** `name`, `dob`, `document-id` (warrant/case number), issuing agency — on the destination sites
- **Empty/negative result looks like:** "no records" on the linked search, or a jurisdiction with no online warrant search — absence is not proof; many agencies don't publish warrants online, and false "no hits" occur.

## Gotchas & OpSec
- This page is a **directory**, not a search box — the actual query happens on each jurisdiction's site.
- Coverage is uneven: many counties have no public warrant search, so a clean result only covers what's online.
- Data accuracy is the jurisdiction's, not BlackBookOnline's — verify before relying on it.

## Overlaps ("do both")
- Pairs with the broader `[[blackbookonline]]` record portal (other record types for the same person) and `[[vinelink]]` (custody/booking status) — a warrant plus a custody hit together explain where someone is.

## Trust & verifiability
`trust: community` — a well-regarded public-records aggregator that curates links; the authoritative data lives on the official jurisdiction sites it points to, so cite those, not this index.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arrest-warrants |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
