---
id: obituaries-australia
name: Obituaries Australia
description: Use when you have the `name` of a deceased person with an Australian connection and want their published obituary — returns death details, biography and named relatives/associates.
url: http://oa.anu.edu.au/
category: people-search
path:
- people-search
bestFor: Finding published Australian obituaries by name to confirm a death and harvest biographical detail and family relationships.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: free
costNote: Free academic resource hosted by the Australian National University; no account required.
opsec: passive
opsecNote: Searching a published obituary archive is passive and notifies no one. The subject is deceased; the sensitivity is the living relatives named in obituaries — handle their details responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the National Centre of Biography at the Australian National University; a reputable, sourced academic repository of obituaries transcribed from real publications.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- oa.anu.edu.au
- Obituaries Australia ANU
tags:
- toddington
- curated-directory
- people-search
- obituaries
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Obituaries Australia

> An ANU-run archive of obituaries transcribed from Australian newspapers and journals — confirm a death and lift the family tree straight out of the published notice.

## When to use
You have the `name` of a deceased person connected to Australia and want their obituary: the death (and often birth) dates, a biographical sketch, and — most valuable for OSINT — the survivors and relatives named in the notice. Reach for it to confirm a death, place a person in a time and community, and generate `associate`/relative leads when tracing family for a missing-persons or genealogical case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://oa.anu.edu.au/.
2. Search the deceased's `name` (browse by name/date if needed).
3. Read the transcribed obituary: death/birth dates, life summary, occupation, and named family members.
4. Note the publication/date cited (the archive sources each entry) to corroborate.
5. Pivot: named survivors (`associate`) become new subjects; dates/`dob` and places seed `[[familysearch-org]]` and grave/records searches; the community named points to local records.

## Inputs → Outputs
- **In:** `name` (of the deceased)
- **Out:** obituary text → death/birth `dob` dates, biography, and named relatives/`associate`s
- **Empty/negative result looks like:** no obituary — the person had no published notice, isn't in the (curated, non-exhaustive) archive, or has an Australian link too tenuous to appear; absence is not proof of anything.

## Gotchas & OpSec
- Curated, not complete: this is a transcribed academic collection, not every Australian death — a miss reflects coverage, not non-existence.
- Living relatives: obituaries name survivors — treat those living people's details with care.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with `[[familysearch-org]]` and `[[github-io]]` grave search — obituaries name the survivors, vital/grave records confirm the dates and burial.
- Pairs with Trove/newspaper archives for the original published notice and surrounding context.

## Trust & verifiability
`trust: trusted` — a reputable ANU academic repository that cites the source publication for each entry, so obituary content is verifiable, bounded only by its curated coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | obituaries-australia |
