---
id: state-corrections-links
name: State Corrections Links
description: Use when you have a `name` and want to find the right state DOC inmate locator to check incarceration status — returns a directory pointing to name, dob, and inmate document-id data.
url: https://www.corrections.com/links/30
category: public-records
path:
- public-records
bestFor: A directory of links to US state Department of Corrections inmate-locator and offender-search systems.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: degraded
pricing: free
costNote: Free links directory; the state DOC locators it points to are also free to search.
opsec: passive
opsecNote: Browsing a links directory and searching an official state inmate locator are both passive — the incarcerated subject is not notified, and you reveal only your IP to the state system. No login needed; use a sock-puppet browser for sensitive casework.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: corrections.com is a long-running corrections-industry portal; its links page is a community-curated index that points to authoritative official DOC locators (verify the target link is current, as directory entries can rot).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- michigan-state-records
- vinelink
- corrections-com-inmate-locaton-links
aliases:
- corrections.com links
- DOC inmate locator directory
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# State Corrections Links

> A directory on the corrections-industry portal corrections.com that indexes US state Department of Corrections inmate-locator systems — the jump-off to check whether a person is (or was) incarcerated.

## When to use
You have a `name` and reason to think the subject may be incarcerated in a US state prison, and you need the correct state's official offender-search/inmate-locator quickly. Each state runs its own system with its own interface; this directory saves you hunting for the right URL. High value in missing-persons and skip-trace work, where confirming incarceration explains a person's disappearance from other records and yields a facility `address` and inmate ID.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.corrections.com/links/30 and locate the state(s) where the subject may be held.
2. Follow the link to that state's official DOC inmate locator / offender search.
3. Search by name (and any known identifiers) on the official system.
4. Read the official result: current custody status, facility, inmate `document-id`/number, often `dob` and physical description.
5. Pivot: for federal custody use the BOP locator; to set victim/release notifications use [[vinelink]]; if unsure of the state, cross-check aggregators.

## Inputs → Outputs
- **In:** `name` (plus the likely state)
- **Out:** a link to the correct state DOC locator, which yields custody status, facility `address`, inmate `document-id`, `dob`, and physical description
- **Empty/negative result looks like:** a dead directory link, or the official locator returns no match — many states exclude released, juvenile, or county-jail inmates, so a negative doesn't rule out past/other-jurisdiction incarceration (also try the federal BOP locator and county jails).

## Gotchas & OpSec
- It's a *directory* — the authoritative data lives on each state's DOC site; verify there, and watch for stale/broken links (hence `status: degraded`).
- Coverage differs by state: some show only currently-incarcerated people, exclude juveniles, or omit county jails; absence is not proof.
- OpSec: passive — checking an official locator does not alert the subject.

## Overlaps ("do both")
- Pairs with [[vinelink]] (nationwide custody search + release/victim notifications) and aggregators like [[michigan-state-records]] — use this to reach the official state source, VINELink for cross-state coverage and alerts.

## Trust & verifiability
`trust: community` — the directory itself is a community-curated index on corrections.com, but it points to authoritative first-party state DOC systems. Trust the official locator's result; treat the directory only as routing, and confirm links are current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-corrections-links |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
