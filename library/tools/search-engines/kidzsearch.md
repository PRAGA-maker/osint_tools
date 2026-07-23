---
id: kidzsearch
name: KidzSearch
description: Use when you want a SafeSearch-locked, ad-light web search for a `name`/topic — a filtered Google front end returning family-safe results; minimal investigative edge over plain search.
url: https://www.kidzsearch.com
category: search-engines
path:
- search-engines
bestFor: A locked-SafeSearch, kid-oriented web search front end over Google results.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free ad-supported search; no account required.
opsec: passive
opsecNote: Passive web search. Queries go to a third party (and on to Google); use a clean browser for sensitive terms. No contact with any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial kid-safe search portal wrapping Google Programmable Search + SafeSearch; results are Google's, the filtering and framing are KidzSearch's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- boolify-boolean-search-teaching-tool-for-kids
- kidrex
aliases:
- kidzsearch.com
tags:
- toddington
- curated-directory
- kid-friendly-educational-search-engines
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# KidzSearch

> A SafeSearch-locked, kid-oriented front end over Google — occasionally handy for family-safe results, but rarely worth choosing over an unfiltered search for real investigative work.

## When to use
Reach for KidzSearch only in narrow cases: you specifically want SafeSearch forced on (e.g. checking what a child would see for a `name` or term), or you want a lightweight, tracker-reduced Google front end. For genuine OSINT you almost always want the *un*filtered engine — KidzSearch deliberately blocks social media and adult/edgy content, which is exactly the material an investigation often needs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.kidzsearch.com.
2. Enter the `name` or topic in the search box; results are Google's, filtered through locked SafeSearch and KidzSearch's blocklist.
3. Read the results — expect social platforms and mature content to be missing.
4. Pivot: for anything beyond family-safe browsing, re-run the same query on a full search engine or a dork-capable tool.

## Inputs → Outputs
- **In:** `name` / keyword
- **Out:** filtered, family-safe web results (no new selector — it's a search surface)
- **Empty/negative result looks like:** few or no results where a normal engine returns many — the content was filtered out, not absent.

## Gotchas & OpSec
- Filtering removes social media and adult content by design — a poor fit for most people-search; use it knowing what it hides.
- Results still originate from Google; this is a wrapper, not an independent index.
- OpSec: passive; queries reach a third party then Google. Use a clean browser for sensitive terms.

## Overlaps ("do both")
- Sits alongside `[[kidrex]]` (another kid-safe Google wrapper) and `[[boolify-boolean-search-teaching-tool-for-kids]]`; for real coverage, prefer an unfiltered engine over any of these.

## Trust & verifiability
`trust: community` — a legitimate commercial kid-safe portal; the results are Google's (reliable), but the aggressive filtering makes it unsuitable as a primary OSINT search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kidzsearch |
| category | search-engines |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
