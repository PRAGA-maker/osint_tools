---
id: osint-search-engine
name: OSINT Search Engine (Google CSE)
description: Use when you have a `name`, `username` or `email` and want to search a curated set of people/OSINT sites at once — a prebuilt Google Custom Search Engine returning web hits scoped to sources the author configured.
url: https://cse.google.com/cse/publicurl?cx=006290531980334157382:qcaf4enph7i
category: people-search
path:
- people-search
bestFor: One-box searching across a curated bundle of people-search / OSINT sites via a prebuilt Google Custom Search Engine.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to use in the browser (it's a public Google CSE); no account needed. Its usefulness depends entirely on the site list its author configured, which you cannot see or edit.
opsec: passive
opsecNote: This runs as a normal Google search over a restricted site list; you query Google, not the subject, and no notification is sent. Search terms go to Google and the CSE owner's config — use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine; results are real Google results, but the value and coverage depend on an opaque, author-controlled site list that can go stale or be abandoned.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google CSE OSINT
- custom search engine people search
tags:
- people-search
- custom-search-engine
- technique
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# OSINT Search Engine (Google CSE)

> A prebuilt Google Custom Search Engine that restricts Google to a curated bundle of people-search/OSINT sites — one query, many sources, but the source list is opaque and author-controlled.

## When to use
You have a `name`, `username`, or `email` and want to sweep a hand-picked set of OSINT/people-search sites in a single search instead of visiting each. A Custom Search Engine (CSE) is just Google restricted to sites the CSE author configured, so it's a fast, low-effort first pass. Because you can't see the site list, treat it as a convenience layer over Google, not an authoritative or complete source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (https://cse.google.com/cse/publicurl?cx=006290531980334157382:qcaf4enph7i).
2. Enter the `name` (in quotes for exact match), `username`, or `email`; add a qualifier (city, employer) to disambiguate.
3. Review results — they are ordinary Google results limited to the CSE's configured sites; open promising hits directly.
4. Sanity-check coverage: run the same query in plain Google. If plain Google finds relevant sources the CSE misses, the CSE's site list is stale/narrow — fall back to Google with your own `site:`/X-ray operators.
5. Pivot: hits feed the specific people-search sites they land on; a confirmed handle/email feeds dedicated username/email tools.

## Inputs → Outputs
- **In:** `name` / `username` / `email` (+ optional qualifier)
- **Out:** web hits (`social-profile`, `name` mentions) scoped to the CSE's site list
- **Empty/negative result looks like:** no results, or obviously thin results — could mean the subject isn't on the configured sites OR the CSE is stale; confirm by re-running in plain Google.

## Gotchas & OpSec
- Opaque coverage: you can't see or edit which sites the CSE searches, and abandoned CSEs quietly rot — always cross-check against plain Google.
- Not authoritative: it's a search convenience, not a database; every hit still needs to be opened and verified at the source.
- OpSec: passive; a normal Google query over a restricted site list.

## Overlaps ("do both")
- Pairs with hand-built Google X-ray searches and dedicated people-search aggregators — the CSE is a quick first pass, but your own `site:` operators give coverage you control and can audit.

## Trust & verifiability
`trust: community` — results are genuine Google results, but the CSE's value rests on an opaque third-party site list that may be narrow or outdated, so verify every hit and don't treat empty results as conclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-search-engine |
| category | people-search |
| selectorsIn → selectorsOut | name, username, email → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
