---
id: birmingham-public-library-databases
name: Birmingham Public Library Databases
description: Use when you have a `name` linked to Alabama/Birmingham and want niche local-history records (coal-mine fatalities, obituaries, church registers, inventors) — returns `dob`/death, `associate`, `employer-org`, `address` from historical indexes.
url: http://www.bplonline.org/virtual/databases/default.aspx?p=2&q=11#db
category: public-records
path:
- public-records
bestFor: Specialty local-history and genealogy indexes for the Birmingham/Alabama area (mine fatalities, obituaries, church and civil records).
selectorsIn:
- name
selectorsOut:
- name
- address
- associate
- employer-org
status: live
pricing: free
costNote: The library's own local-history index databases are free to search; some linked commercial genealogy databases may require a library card / in-library access.
opsec: passive
opsecNote: A library records index — you query historical databases, nothing reaches any subject. Some databases may want a free library-card login; use a research account where needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Birmingham Public Library (Alabama); its curated local-history indexes are drawn from primary records, though transcription errors are possible.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
aliases:
- BPL databases
- Birmingham Alabama Public Library databases
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Birmingham Public Library Databases

> The Birmingham (Alabama) Public Library's specialty local-history indexes — coal-mine fatalities 1898–1938, obituaries, Episcopal church registers, inventors, and more.

## When to use
You have a `name` with a plausible tie to Birmingham/Alabama (especially historical), and you need niche local records that broad genealogy sites miss: Alabama coal-mine fatality records, local obituary indexes, church registers, and civil records. Ideal for deep-background or historical family research anchored in that region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the BPL databases page (http://www.bplonline.org/virtual/databases/ and browse the local-history/specialty collections).
2. Pick the relevant database (e.g. coal-mine fatalities, obituary index, church registers).
3. Search by `name` (and date/place where offered).
4. Read the record for death/`dob` dates, `employer-org` (e.g. mine/company), `address`, and named relatives (`associate`).
5. Pivot: relatives → people-search; employer/mine → occupational records; obituary → `[[legacy]]`/`[[hmcpl-obituary-index]]` for corroboration.

## Inputs → Outputs
- **In:** `name` (+ optional date/place)
- **Out:** `name`, death/`dob` dates, `employer-org` (e.g. mining company), `address`, `associate` (relatives)
- **Empty/negative result looks like:** no index entry — the person likely isn't in that specific Alabama collection (wrong region/era, or not yet indexed). Absence is local, not global.

## Gotchas & OpSec
- Geographically/thematically narrow — Birmingham/Alabama local history; useless outside that scope.
- Some linked commercial databases need a library card or in-library access; the library's own indexes are free online.
- Transcriptions can contain errors; verify against originals.

## Overlaps ("do both")
- Pairs with `[[hmcpl-obituary-index]]` (another Alabama library index), `[[legacy]]`, and `[[familysearch-s-united-states-record-collections]]` — each covers different local/national records; combine for Alabama-linked subjects.

## Trust & verifiability
`trust: trusted` — an official public-library resource over primary local records; corroborate individual entries with source documents.
