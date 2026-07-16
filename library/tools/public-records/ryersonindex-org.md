---
id: ryersonindex-org
name: ryersonindex.org
description: Use when you have an Australian subject's `name` and suspect they've died — returns death-notice/obituary index entries (death date, age, sometimes place) pointing to the source newspaper.
url: https://ryersonindex.org/search.php
category: public-records
path:
- public-records
bestFor: Free index of Australian death notices, obituaries, and funeral notices from newspapers — confirming a death and its date.
selectorsIn:
- name
selectorsOut:
- dob
- name
- associate
status: live
pricing: free
costNote: Entirely free, volunteer-run index; no account. It indexes notices (with source citations) rather than hosting the full text.
opsec: passive
opsecNote: Searching an index of published death notices is passive and touches no living subject. Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running Australian volunteer index of newspaper death/funeral notices; entries are transcribed from published notices and are reliable pointers, though the full notice must be read at the source.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- legacy-com
- billiongraves-com
- the-ryerson-index-australia
aliases:
- Ryerson Index
- ryersonindex.org
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- death-notices
- australia
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ryersonindex.org

> The Ryerson Index — a free, volunteer-built index of Australian death notices, obituaries, and funeral notices from newspapers, used to confirm a death and locate the source notice.

## When to use
You have an Australian subject's `name` and need to establish whether (and when) they died. The Ryerson Index catalogues death/funeral notices published in Australian newspapers, giving death dates, ages, sometimes place, and a citation to the exact newspaper and date — the fastest free way to confirm an Australian death and find the notice to read in full.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ryersonindex.org/search.php and search the subject `name` (try variants and date-range filters).
2. Read matching index entries: name, notice type (death/funeral/obituary), date of death or notice, age, and the source newspaper + publication date.
3. Use the citation to find and read the full notice (library/newspaper archive), which often names relatives (`associate`).
4. Pivot: death date/age anchor genealogy searches; the full obituary's named relatives feed people-search; cross-check with `[[billiongraves-com]]` for burial.

## Inputs → Outputs
- **In:** `name` (+ approximate date range)
- **Out:** death/notice date, age (→ `dob` estimate), source citation, and (via the full notice) relatives as `associate`s
- **Empty/negative result looks like:** no entry — the person may be alive, died outside the indexed papers/dates, or the notice wasn't published; absence is not proof of anything.

## Gotchas & OpSec
- It is an **index**, not full text — you get a pointer to the notice, which you then read at the source.
- Australia-focused; coverage depends on which papers and periods volunteers have indexed.
- Name-only matches include namesakes; confirm with age/place/relatives before concluding it's your subject.
- OpSec: passive; no contact with any living person.

## Overlaps ("do both")
- Pairs with `[[legacy-com]]` (obituaries aggregator) and `[[billiongraves-com]]` (burial records) — use Ryerson to find the Australian notice, the others to corroborate death/burial and relatives.

## Trust & verifiability
`trust: community` — a respected long-running volunteer index. Entries are faithful transcriptions of published notices; verify the specifics by reading the cited original notice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ryersonindex-org |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
