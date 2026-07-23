---
id: kidrex
name: KidRex
description: Use when you want a SafeSearch-locked, kid-safe web search for a `name`/topic — a filtered Google Custom Search returning family-safe results; little investigative edge over plain search.
url: http://www.kidrex.org
category: search-engines
path:
- search-engines
bestFor: A locked-SafeSearch, kid-oriented Google Custom Search front end.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free ad-supported search; no account required. The homepage now redirects to alarms.org/kidrex after acquisition.
opsec: passive
opsecNote: Passive web search. Queries go to a third party (and on to Google); use a clean browser for sensitive terms. No contact with any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A kid-safe search wrapping Google Programmable Search + SafeSearch, acquired by and now served under alarms.org; results are Google's, the filtering is KidRex's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- kidzsearch
aliases:
- kidrex.org
- KidRex Safe Search
tags:
- toddington
- curated-directory
- kid-friendly-educational-search-engines
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# KidRex

> A SafeSearch-locked, kid-safe Google front end (now hosted under alarms.org) — usable for family-safe results, but rarely the right tool for an actual investigation.

## When to use
Use KidRex only in narrow cases: you specifically want SafeSearch forced on — e.g. to see what a child would be shown for a `name` or term — or you want a simple filtered Google surface. For real OSINT you almost always want the *un*filtered engine, since KidRex blocks social media, adult, and edgy content, which is often exactly what a case needs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.kidrex.org (it now redirects to the alarms.org-hosted KidRex page).
2. Enter the `name` or topic; results are Google's, filtered through locked SafeSearch and KidRex's own blocklist.
3. Read the results — social platforms and mature content will be absent by design.
4. Pivot: for anything beyond family-safe browsing, re-run the query on a full/dork-capable search engine.

## Inputs → Outputs
- **In:** `name` / keyword
- **Out:** filtered, family-safe web results (no new selector — it's a search surface)
- **Empty/negative result looks like:** few or no results where a normal engine returns many — the content was filtered out, not absent.

## Gotchas & OpSec
- By design it removes social media and adult content — a poor fit for most people-search; know what it hides before trusting a blank result.
- It's a Google Custom Search wrapper, not an independent index; ownership moved to alarms.org, so branding/availability may shift.
- OpSec: passive; queries reach a third party then Google. Use a clean browser for sensitive terms.

## Overlaps ("do both")
- Essentially interchangeable with `[[kidzsearch]]` (another kid-safe Google wrapper); for real coverage, prefer an unfiltered engine over either.

## Trust & verifiability
`trust: community` — a legitimate kid-safe search portal (now under alarms.org); results are Google's and reliable, but the heavy filtering makes it unsuitable as a primary OSINT search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kidrex |
| category | search-engines |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
