---
id: newseum-today-front-pages
name: Newseum - Today Front Pages
description: Use when you have a place and a date and want that day's local newspaper front page — returns scanned front pages from 500+ papers worldwide, mapped by location.
url: https://frontpages.freedomforum.org/
category: search-engines
path:
- search-engines
bestFor: Viewing today's (or an archived) newspaper front pages from hundreds of cities worldwide on a map.
selectorsIn:
- geolocation
status: live
pricing: free
costNote: Free public gallery hosted by the Freedom Forum (which took over the Newseum's Today's Front Pages after the museum closed in 2019). No account.
opsec: passive
opsecNote: Passive — you browse a public gallery of published newspaper front pages; nothing about any subject is queried and no login is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Freedom Forum, the nonprofit that ran the Newseum; front pages are the actual published editions submitted by the newspapers themselves.
missingPersonsRelevance: low
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Today's Front Pages
- Newseum front pages
- Freedom Forum front pages
tags:
- newspapers
- front-pages
- verification
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Newseum - Today Front Pages

> The Newseum's "Today's Front Pages" (now hosted by the Freedom Forum): a map-browsable gallery of that day's actual newspaper front pages from 500+ cities worldwide.

## When to use
You want to know what the local press in a specific place was leading with on a given day — to corroborate that a reported event happened, to see how a local story was covered, or as a geolocation/verification aid (a front page in a photo can be matched to the paper and date here). It's a place-and-date media browser, not a person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://frontpages.freedomforum.org/ (the URL moved here after the Newseum closed in 2019).
2. Browse the map or list and pick a city/region (`geolocation`); the newspaper's front page for that day loads as a scanned image.
3. Click a front page to enlarge and read the lead stories, or open the paper's site for the full edition.
4. Use the date/archive controls where available to compare coverage across days.
5. Pivot: the newspaper name + date feeds a newspaper-archive search (`[[newspaper-archive]]`) for the full article; the lead story feeds event verification.

## Inputs → Outputs
- **In:** a `geolocation` (city/region) and a date
- **Out:** the scanned front page(s) of local newspaper(s) for that place/day
- **Empty/negative result looks like:** a city with no participating paper that day — coverage is limited to newspapers that submit front pages; absence isn't proof no local paper exists.

## Gotchas & OpSec
- Coverage is only newspapers that voluntarily submit — strong in the US, patchier elsewhere, and mostly *current* front pages (deep back-archives require dedicated archive tools).
- Front pages are images; for full article text, follow to the paper or a newspaper archive.
- Passive: a public media gallery.

## Overlaps ("do both")
- Pairs with `[[newspaper-archive]]` and other newspaper archives — Today's Front Pages shows *what led where, now*; the archives retrieve the *full historical article text*.

## Trust & verifiability
`trust: trusted` — run by the Freedom Forum (successor to the Newseum); the front pages are the genuine published editions supplied by the newspapers, making them reliable primary artifacts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | newseum-today-front-pages |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → (front pages) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
