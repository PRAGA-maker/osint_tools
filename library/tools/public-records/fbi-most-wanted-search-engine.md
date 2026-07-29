---
id: fbi-most-wanted-search-engine
name: FBI Most Wanted Search Engine
description: Use when you have a `name` or case detail and want to check US federal wanted/missing/kidnapping listings — returns matching FBI and law-enforcement bulletin pages.
url: https://cse.google.com/cse?cx=1ee952e6584aa91f9
category: public-records
path:
- public-records
bestFor: Searching across FBI Most Wanted, missing-persons, and kidnapping bulletins in one query.
selectorsIn:
- name
- physical-description
selectorsOut:
- name
- image
- physical-description
status: live
pricing: free
costNote: Free Google Custom Search Engine over official law-enforcement wanted/missing pages; no account needed.
opsec: passive
opsecNote: This is a Google search over public bulletin pages — you query Google, not any subject, and nothing is disclosed to the person searched for. Standard search-engine logging applies; use a clean session if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Google Custom Search Engine (CSE), not an official FBI portal. It scopes Google to law-enforcement wanted/missing sites; the underlying bulletin pages are authoritative, but the CSE config is community-maintained and its coverage/scope can drift.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- fbi-gov
- namus
- charley-project
aliases:
- FBI Most Wanted CSE
tags:
- wanted
- missing-persons
- law-enforcement
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# FBI Most Wanted Search Engine

> A Google Custom Search Engine scoped to FBI Most Wanted, missing-persons, and kidnapping bulletins — one query across official law-enforcement listings.

## When to use
You have a `name`, alias, or `physical-description` and want to check whether the person appears in US federal wanted, missing, or kidnapping bulletins. Relevant to missing-persons work (the FBI publishes missing-person and kidnapping notices alongside wanted fugitives), and to vetting whether a subject is the target of a federal notice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=1ee952e6584aa91f9.
2. Search a `name`/alias, or descriptive terms (location, offense, distinctive features).
3. Review results — they link to official bulletin pages with photos, aliases, physical details, and case/field-office contacts.
4. Open the official page (fbi.gov or partner site) to read the authoritative notice; do not rely on the CSE snippet alone.
5. Pivot: a confirmed notice gives `image`, `physical-description`, aliases, and jurisdiction to feed people-search and missing-persons databases.

## Inputs → Outputs
- **In:** `name` / alias / `physical-description`
- **Out:** matching bulletin pages → `name`, `image`, `physical-description`, case/jurisdiction details
- **Empty/negative result looks like:** no results — the person isn't in the indexed federal bulletins (they may be in a state/local or dedicated missing-persons registry instead); check NamUs and the Charley Project.

## Gotchas & OpSec
- It is a **third-party CSE**, not the FBI's own search — always click through to the official page to confirm, and treat scope as best-effort (a CSE's site list can be incomplete or stale).
- US-federal focus; state/local missing-persons cases often live in dedicated registries this won't surface.
- Bulletins update frequently; a person may be added/removed between checks.

## Overlaps ("do both")
- Pairs with `[[fbi-gov]]` (the authoritative first-party site) and dedicated missing-persons resources `[[namus]]` / `[[charley-project]]`. Do both: use this CSE for a fast cross-source sweep, then confirm and expand on the authoritative registries.

## Trust & verifiability
`trust: community` — the CSE wrapper is community-maintained, but it points to authoritative law-enforcement pages. Verify every hit on the official site; do not treat a search snippet as confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fbi-most-wanted-search-engine |
