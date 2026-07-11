---
id: os-death-records
name: OS Death Records
description: Use when you have a `name` and want to reach the right US state/county death-record and obituary databases — returns links yielding `dob`, death dates, and `associate` (surviving family).
url: http://publicrecords.onlinesearches.com/death-records.htm
category: public-records
path:
- public-records
bestFor: A directory that routes a US death-records inquiry to the correct state/county vital-records source.
selectorsIn:
- name
selectorsOut:
- dob
- associate
- name
status: live
pricing: free
costNote: The directory is free. It links to official state/county sources, some of which charge for certified copies; index/obituary lookups are typically free.
opsec: passive
opsecNote: Browsing the directory is passive. The onward official sources log queries per their own policies, but checking whether a person is deceased is a benign, low-risk lookup. Ordering a certified certificate may require identifying yourself and can be restricted to relatives.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: OnlineSearches is a reputable, long-running index of official public-records sources; it links to authoritative government databases rather than hosting data itself.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlineSearches Death Records
- publicrecords.onlinesearches.com death
tags:
- genealogy
- family
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# OS Death Records

> OnlineSearches' death-records portal — a curated directory that points you to the specific US state/county death indexes, vital-records offices, and obituary sources for a subject.

## When to use
You need to determine whether a US subject is deceased, or you're building out family context (surviving relatives, a date of birth, a death date) for a missing-persons or genealogy inquiry, and you have a `name` plus a likely state. Rather than a single database, this hands you the right official source per jurisdiction — the key first step because US death records are managed state-by-state.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the directory at http://publicrecords.onlinesearches.com/death-records.htm (redirects into the current `publicrecords.onlinesearches.com` structure).
2. Drill down to the subject's **state**, then county/city, to the death-records / vital-records entry.
3. Note the flag OnlineSearches shows for each link — free online search, paid service, or not-online.
4. Follow the link to the official index or obituary source and search the `name` there.
5. Read results: death date, birth date (`dob`), place, and — often in obituaries — surviving family members (`associate`). Pivot: relatives' names feed people-search; a confirmed death closes or redirects a trace.

## Inputs → Outputs
- **In:** `name` (+ US state for best routing)
- **Out:** links that yield death date, `dob`, and `associate` (family/next-of-kin, especially via obituaries)
- **Empty/negative result looks like:** a jurisdiction marked "not available online," or the target source returns no match — many older/certified records are offline or relative-restricted, so a null here does **not** confirm the person is alive.

## Gotchas & OpSec
- It's a router, not a database — the actual data quality depends entirely on the linked state/county source.
- Certified copies are frequently restricted to relatives; index/obituary lookups are the openly usable part.
- Coverage and record start-years vary wildly by state (some from the 1800s, some only recent).

## Overlaps ("do both")
- Pairs with `[[deathindexes-com]]` and obituary aggregators / `[[familysearch]]` — use both because OnlineSearches routes to official vital records while those cover indexed/genealogical and obituary angles the government sites omit.

## Trust & verifiability
`trust: community` — the directory itself is well-maintained and points to authoritative government sources; verify the actual record on the official destination it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | os-death-records |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
