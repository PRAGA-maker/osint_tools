---
id: corrections-com-inmate-locaton-links
name: Corrections.com — Inmate Locator Links
description: Use when you have a `name` and want to find the right US state/federal inmate-locator to search — a curated directory of DOC lookup links that route to records returning custody status and `document-id`.
url: https://www.corrections.com/links/20
category: public-records
path:
- public-records
bestFor: Quickly finding the correct state Department of Corrections inmate-locator for a jurisdiction.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- dob
status: degraded
pricing: free
costNote: Free directory of links; the linked official DOC locators are themselves free.
opsec: passive
opsecNote: Following links and searching public DOC locators is passive; inmates/subjects are not notified. Nothing is tied to you beyond normal web requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Corrections.com is a long-standing corrections-industry portal; this is a link directory, so trust each destination DOC site (authoritative) rather than the aggregator.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- corrections.com inmate locator links
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- state-corrections-links
---

# Corrections.com — Inmate Locator Links

> A directory that points you to the right official inmate-locator — because the US has no single inmate database, only dozens of separate state/federal DOC systems.

## When to use
You have a `name` and believe (or want to check whether) the person is incarcerated in the US, but you don't know which jurisdiction's Department of Corrections locator to use. This page collects links to the various state and federal inmate-locator systems, saving you from hunting each DOC site individually. It was returning a server error at last check (`status: degraded`), so if it's down, go straight to the target state's DOC "inmate search" or the federal BOP locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.corrections.com/links/20 and locate the jurisdiction you need (state DOC or federal BOP).
2. Follow the link to that official locator.
3. Search the subject's `name` (and DOB if the locator asks) on the DOC site.
4. Read the result: custody status, facility, inmate/booking number (`document-id`), sometimes DOB and mugshot.
5. Pivot: an inmate/booking `document-id` and facility feed court-record lookups, visitation/mail context, and release-date tracking.

## Inputs → Outputs
- **In:** `name` (plus a jurisdiction guess)
- **Out:** routes to locators returning custody status, facility, `document-id` (inmate number), sometimes `dob`
- **Empty/negative result looks like:** dead directory links or no inmate match on the DOC site — check neighbouring states, county jails (not always covered), and the federal BOP separately.

## Gotchas & OpSec
- Fragmented data: no locator covers all US custody; county jails and immigration detention are often separate — a "not found" is not proof of liberty.
- Link directories rot; if a link is dead, search "[state] DOC inmate locator" directly.
- Records are official but can lag transfers/releases by days.

## Overlaps ("do both")
- Pairs with the Federal BOP inmate locator, VINELink, and county jail rosters — this directory helps you pick the state system, those cover federal/local gaps.

## Trust & verifiability
`trust: community` — the aggregator is a convenience layer; the authoritative data lives on the official DOC sites it links to, which you should treat as the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | corrections-com-inmate-locaton-links |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
