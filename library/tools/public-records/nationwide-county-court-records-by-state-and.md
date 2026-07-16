---
id: nationwide-county-court-records-by-state-and
name: Black Book Online — Nationwide County Court Records
description: Use when you have a `name` and want the right free county/state court-records portal to search — returns links to official court, criminal, and record search sites indexed by state and county.
url: https://www.blackbookonline.info/usa-county-court-records.aspx
category: public-records
path:
- public-records
bestFor: A free directory that routes you to the correct county/state court-record search portal for a US locality.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free directory/aggregator of public-records portals. The destination court sites are mostly free, though some counties charge for document copies or full case detail.
opsec: passive
opsecNote: Browsing Black Book Online and running name searches on the county portals it links is passive — the subject is not notified. Some destination court systems log searches or require a clickwrap; use a clean session for sensitive work.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running free public-records directory maintained by PI Robert Scott; it aggregates links to official government portals. It explicitly disclaims data accuracy and is not an FCRA source.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- montana
- arrest-warrants
- black-book-online-criminal-search
- criminal-search-criminal-records-by-state-and
- free-aviation-records-black-book-online
- jail-records
- property-search-public-records-by-state
- sex-offender-search
aliases:
- Black Book Online
- blackbookonline.info
- BRB county court records
tags:
- court
- inmate
- public-records
- records-directory
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Black Book Online — Nationwide County Court Records

> A free, well-organized directory that points you to the correct official county/state court-record search portal — the fastest way to find *which* government site to search for a person in a given US locality.

## When to use
You have a `name` and a US locality (or need to sweep several) and want court/criminal/civil records, but every county runs its own system. Black Book Online indexes those official portals by state and county so you jump straight to the right search page instead of hunting for it. Court records surface case involvement, aliases, associates, DOBs and case `document-id`s — strong locators and identity corroboration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackbookonline.info/usa-county-court-records.aspx.
2. Select the state, then the county where the subject has ties.
3. Follow the link to that county/court's official record-search portal.
4. Search by name (add DOB/middle name to disambiguate) on the destination site and read the case records.
5. Pivot: case documents yield DOB, aliases, addresses, co-parties (`associate`); also use Black Book's other sections (criminal, death, inmate, reverse phone).

## Inputs → Outputs
- **In:** `name` (+ locality; optionally DOB)
- **Out:** links to official portals returning court/case records — `name`/aliases, `dob`, case `document-id`, parties
- **Empty/negative result looks like:** a county with no online portal (Black Book will say so), or a destination search returning no case. Black Book warns of false "no hits" and mislabeled data — a null is not proof of no record; try neighboring counties and statewide systems.

## Gotchas & OpSec
- It's a directory, not a database — it holds no records itself; quality/coverage belongs to each destination portal.
- Coverage is uneven: some counties are online, some aren't; through-dates vary and may be mislabeled.
- Not an FCRA-permissible source — do not use results for employment/housing/credit decisions.

## Overlaps ("do both")
- Pairs with statewide court portals, PACER (federal), and inmate locators like `[[montana]]` — Black Book routes you to local court records; use the federal/state-specific tools for their layers.

## Trust & verifiability
`trust: trusted` — a reputable, long-standing free directory to official government portals; the *links* are trustworthy, but verify every record at the destination and treat Black Book's accuracy disclaimer seriously.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nationwide-county-court-records-by-state-and |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
