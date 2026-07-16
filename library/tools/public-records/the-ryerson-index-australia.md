---
id: the-ryerson-index-australia
name: The Ryerson Index (Australia)
description: Use when you have a `name` and want to confirm an Australian death or find the obituary/funeral trail — returns death-notice index entries pointing to the original newspaper source.
url: http://www.ryersonindex.org
category: public-records
path:
- public-records
bestFor: Confirming a death and locating Australian death/funeral/probate notices by name.
selectorsIn:
- name
selectorsOut:
- dob
- name
- associate
status: live
pricing: free
costNote: Free to search and always will be, per the operators; run by volunteers. No account required.
opsec: passive
opsecNote: Fully passive — you query a volunteer-run index, not a live government system, and nothing is attributed to the subject. Safe to use without a sock-puppet, though good browser hygiene never hurts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established, well-regarded volunteer genealogy index (10M+ entries from 500+ Australian sources); it is an index/finding aid, not a primary source, so confirm details in the original notice it points to.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- findagrave
- births-deaths-marriages-au
- ryersonindex-org
aliases:
- Ryerson Index
- Australian death notices index
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
- obituaries
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# The Ryerson Index (Australia)

> A free, volunteer-maintained index of death notices, funeral notices, probate notices and obituaries from Australian newspapers (1803–present) — the fastest way to confirm an Australian death and find the source notice.

## When to use
You have a `name` and a plausible Australian connection, and you need to know whether the person has died — and if so, to find the obituary/funeral trail that names relatives and dates. This is a core "is this person deceased?" check for Australian subjects, and a bridge into family networks (funeral notices list surviving relatives). Strongest for New South Wales but national in scope.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ryersonindex.org and go to the search.
2. Enter the surname (and given name); optionally narrow by date range or publication.
3. Read the index hits: name, death date (and sometimes age → approximate `dob`), notice type (death/funeral/probate/obituary), and the source newspaper + date.
4. The index points to the original — go to the named newspaper/funeral-director source for the full notice (which often lists relatives).
5. Pivot: a confirmed death date closes a missing-person thread or reframes it; funeral-notice relatives feed `associate` mapping; the source date feeds a `[[findagrave]]` / cemetery lookup.

## Inputs → Outputs
- **In:** `name` (surname essential; given name and date range help)
- **Out:** death/funeral notice index entry → death date, age/`dob`, source publication, and (via the original) `associate` (relatives)
- **Empty/negative result looks like:** no matching entry — which means no *indexed Australian death notice*, not proof the person is alive or never died (older, non-NSW, or unindexed notices may be missing).

## Gotchas & OpSec
- It's a finding aid, not the notice itself — you must retrieve the original source for full detail; don't quote the index as the primary record.
- Coverage skews to NSW and to indexed papers; gaps exist for other states and small/older publications.
- Same-name collisions happen — use dates and locations to disambiguate before concluding it's your subject.

## Overlaps ("do both")
- Pairs with `[[findagrave]]` (burial/memorial records, often with photos and family links) and the state `[[births-deaths-marriages-au]]` registries (authoritative certificates) — Ryerson finds the notice fast; those confirm and enrich it.

## Trust & verifiability
`trust: trusted` — a respected, decades-old volunteer index with transparent sourcing. Reliable as a pointer; always verify the specifics against the original notice it cites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-ryerson-index-australia |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
