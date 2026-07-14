---
id: sysoon-deceased-database
name: Sysoon Deceased Database
description: Use when you have a `name` and need to check whether the person is deceased — returns death record details (DOB/DOD, last known residence, burial/memorial) from a deceased-persons search engine.
url: http://www.sysoon.com
category: people-search
path:
- people-search
bestFor: Checking whether a subject has died and finding memorial/burial and last-residence details from a name.
selectorsIn:
- name
selectorsOut:
- dob
- address
- name
status: live
pricing: free
costNote: Free to search memorial/death records. No account required for basic lookups.
opsec: passive
opsecNote: Passive — you search a public memorial/death-records index, not the subject. Nothing is sent to any living associate and no alert is generated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A self-described "social network for death/funerals" aggregating obituary and memorial data; coverage is uneven and user-contributed, so entries are leads to confirm against official death records.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Sysoon
- sysoon.com
tags:
- toddington
- curated-directory
- people-search
- deceased
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Sysoon Deceased Database

> A deceased-persons search engine and online-memorial aggregator — used to check whether a subject has died and to find burial/last-residence details from a name.

## When to use
A key branch in missing-persons work is ruling a subject deceased. When you have a `name` (ideally full first + last, plus a city/state of death to narrow it), Sysoon lets you check obituary/memorial records for a death match and, if found, pull the date of birth/death, last known residence, and burial/memorial location. Use it to test the "are they deceased?" hypothesis before or alongside official death-record checks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.sysoon.com and use its people/death search.
2. Enter the subject `name` (first + last minimum); add city or state of death to refine.
3. Read the output: matching memorial/obituary entries with full name, `dob` and date of death, last known residence (`address`), and cemetery/memorial info.
4. Pivot: a death match with DOB/DOD feeds official death-record and obituary confirmation; a burial location and last residence corroborate identity and geography; surviving-family names (if listed) feed `associate` mapping.

## Inputs → Outputs
- **In:** `name` (+ optional place of death)
- **Out:** `dob` (and date of death), `address` (last known residence / burial place), `name` (aliases/full name)
- **Empty/negative result looks like:** no match — which is inconclusive (coverage is patchy and user-contributed), NOT proof the person is alive. Users report the search misses many individuals.

## Gotchas & OpSec
- Coverage is uneven and partly user-contributed; a null result does not rule out death, and a match should be confirmed against an official death index/obituary.
- Names collide — verify with DOB, place, or family details before concluding it's your subject.
- OpSec: fully passive; public memorial data.

## Overlaps ("do both")
- Pairs with obituary-search and official death-record tools — Sysoon is a broad first-pass net; confirm any death match against authoritative sources before acting on it.

## Trust & verifiability
`trust: unverified` — an aggregator of obituary/memorial data with variable, partly crowd-sourced coverage. Treat every hit as a lead to corroborate, never as a standalone death confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sysoon-deceased-database |
| category | people-search |
| selectorsIn → selectorsOut | name → dob, address, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
