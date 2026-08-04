---
id: newspaper-archive
name: Newspaper Archive
description: Use when you have a `name`, place or event and want historical Turkish/Ottoman press coverage — returns OCR-searchable newspaper pages and clippings by keyword or date.
url: https://www.gastearsivi.com/en/
category: search-engines
path:
- search-engines
bestFor: Full-text (OCR) searching millions of historical Turkish and Ottoman newspaper pages by keyword or date.
selectorsIn:
- name
status: live
pricing: freemium
costNote: Large parts of the archive (e.g. Cumhuriyet 1929–present) are free to search and read as PDF; some features/collections have moved behind pricing — the core keyword search and many titles remain free.
opsec: passive
opsecNote: Passive archive search — you query a media database, not the subject. No login needed for free content; use a clean browser if you don't want searches tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Gaste Arşivi is an independent digitization project widely regarded as Turkey's most comprehensive free newspaper archive; the scanned pages are authentic primary press, though OCR accuracy varies with scan quality.
missingPersonsRelevance: medium
coverage:
- tr
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Gaste Arşivi
- gastearsivi
- Turkish newspaper archive
tags:
- newspaper-archive
- turkey
- historical-press
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Newspaper Archive

> Gaste Arşivi: an OCR-searchable archive of millions of Turkish and Ottoman newspaper pages — the way to find historical press mentions of a person, place, or event in Turkey.

## When to use
You need historical Turkish media coverage — a person's name in an old news story, a report of an event, an obituary, a court or business notice — from Turkish and Ottoman-era newspapers. Gaste Arşivi digitizes decades of major titles (e.g. Cumhuriyet from 1929) and lets you full-text search across them, which is invaluable for background, timelines, or locating a subject's earlier public record in Turkey.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gastearsivi.com/en/ (English interface available).
2. Enter a keyword — a `name`, place, organisation, or event — in the OCR search, or browse by newspaper title/year/date.
3. Open matching pages; the hit is highlighted on the scanned page. Refine by date range or specific title to narrow.
4. Download the page or clipping as PDF for the case file.
5. Pivot: a dated news mention anchors a timeline; names/places in the article feed further person and location searches.

## Inputs → Outputs
- **In:** a `name`, place, organisation, or event term (Turkish spelling works best)
- **Out:** OCR-matched newspaper pages/clippings with dates and titles
- **Empty/negative result looks like:** no hits — the term may be transliterated differently, the OCR may have misread the scan, or the coverage predates/postdates the archived issues; try Turkish spelling variants and date browsing.

## Gotchas & OpSec
- Turkey-focused and Turkish-language; use Turkish spellings/transliterations for best recall, and expect OCR misses on poor scans.
- Freemium: most core search and major titles are free, but some collections/features are now priced — note which before assuming a gap is "not in the archive."
- Passive: a media-archive query, invisible to any subject.

## Overlaps ("do both")
- Complements global newspaper archives (e.g. large English-language archive sites) — Gaste Arşivi's Turkish/Ottoman depth covers what those miss, so run both when a subject has a Turkish connection.

## Trust & verifiability
`trust: community` — an independent but highly regarded digitization project; the scanned pages are authentic primary sources (verify by reading the original scan), while OCR-matched text should be confirmed against the image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | newspaper-archive |
| category | search-engines |
| selectorsIn → selectorsOut | name → (media coverage) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
