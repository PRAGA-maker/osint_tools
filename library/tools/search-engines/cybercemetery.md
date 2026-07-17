---
id: cybercemetery
name: CyberCemetery
description: Use when you need content from a defunct US federal agency/commission website or its final reports — returns archived pages and documents (`document-id`) from shut-down government bodies.
url: https://govinfo.library.unt.edu/
category: search-engines
path:
- search-engines
bestFor: Recovering websites and final reports of US government agencies and commissions that have ceased operation.
selectorsIn:
- employer-org
- name
selectorsOut:
- document-id
- name
status: live
pricing: free
costNote: Free public archive; no account. A partnership of the University of North Texas Libraries and the U.S. Government Publishing Office under the Federal Depository Library Program.
opsec: passive
opsecNote: You read an academic government-document archive; nothing here touches a living subject. Fully passive and unremarkable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by UNT Libraries with the GPO as part of the FDLP; a mandated preservation archive, so its captures of defunct .gov sites are authoritative primary sources.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- archive-org
- archive-today
aliases:
- CyberCemetery
- UNT CyberCemetery
- govinfo.library.unt.edu
tags:
- toddington
- government-archive
- web-archive
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# CyberCemetery

> A preservation archive of shut-down US government websites and their final reports, run by UNT Libraries and the GPO — the place to find a .gov site or commission record that no longer exists live.

## When to use
Your investigation touches a US federal agency, commission, or task force that has since been dissolved — and you need its old website, membership, publications, or final report. Because the CyberCemetery preserves entire snapshots of defunct government bodies (often the only surviving copy of a commission's site), it can yield an agency's staff/`name` listings, contract and hearing documents, and authoritative final reports that provide names, roles, and dates you can't get from a dead link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://govinfo.library.unt.edu/ and browse the alphabetical/agency listing or search for the defunct body by name.
2. Open the archived site and navigate it as it existed — reports, personnel pages, press releases, and datasets are preserved.
3. Download final reports and documents as primary-source evidence; note the agency, dates, and named officials.
4. If a specific old .gov URL is what you need, also check the Wayback Machine, which may hold additional captures.
5. Pivot: named officials feed people/official-record search; a final report's findings and dates feed your timeline.

## Inputs → Outputs
- **In:** `employer-org` (a defunct US government body) or a `name` associated with one
- **Out:** archived pages and `document-id` (final reports, publications), plus official `name`/role listings from the preserved site
- **Empty/negative result looks like:** the body isn't in the collection — it's still active (use its live site), never had a preserved site, or falls outside the FDLP scope; try the Wayback Machine instead.

## Gotchas & OpSec
- Scope: US federal (and some related) bodies that have *ceased operation* — not active agencies, not general web pages.
- Frozen snapshots: content is preserved as of closure; interactive features and outbound links may be dead.
- US-only, government-only: don't expect non-US or private-sector material.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[archive-org]]` and `[[archive-today]]` — the CyberCemetery is the curated, authoritative home for defunct federal sites, while the general web archives may hold extra captures or intermediate versions; check both for full coverage.

## Trust & verifiability
`trust: trusted` — an FDLP preservation archive maintained by UNT Libraries and the GPO; its captures are authoritative primary sources you can cite as the record of a now-defunct government body.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cybercemetery |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, name → document-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
