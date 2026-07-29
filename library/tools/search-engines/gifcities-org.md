---
id: gifcities-org
name: GifCities
description: Use when you have a keyword and want to find animated GIFs salvaged from 1990s GeoCities pages — returns period GIFs each linked back to its original archived page.
url: https://gifcities.org/
category: search-engines
path:
- search-engines
bestFor: Searching the Internet Archive's GeoCities GIF collection and pivoting from a GIF to its original archived host page.
selectorsIn:
- username
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public project of the Internet Archive; no account. Aggressive querying triggers a temporary rate-limit page.
opsec: passive
opsecNote: You query the Internet Archive's index, not any live target — fully passive. The GIFs come from a dead, archived platform (GeoCities, closed 2009), so there's no live owner to alert.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive; a curated, authoritative archive of GeoCities content, not a third-party scraper.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wayback-machine
- archive-org
aliases:
- gifcities
- GeoCities GIF search
tags:
- Search engines
- archive
- retro-web
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# GifCities

> The Internet Archive's search engine over ~4.5 million animated GIFs rescued from GeoCities — a niche way back into late-1990s personal homepages.

## When to use
This is a **niche archival** tool. Its investigative value is narrow: someone with a GeoCities-era web presence (a decades-old personal homepage, fan site, or handle) may have used a distinctive GIF that GifCities has indexed, and each result links back to the *original archived GeoCities page* — which can surface an old `username`, neighbourhood/city sub-URL, or contact details long since deleted from the live web. Reach for it only when you're chasing a very old online footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gifcities.org/.
2. Search a keyword — a name, hobby, city, or handle the subject might have used on a GeoCities page.
3. For any matching GIF, follow the link to its source: the archived GeoCities URL (often `geocities.com/<Neighborhood>/<number>` or a named page) in the `[[wayback-machine]]`.
4. Read that archived page for period-accurate `username`, `domain`/subpath, guestbook names, and contact info.

## Inputs → Outputs
- **In:** keyword / `username` / topic
- **Out:** matching GIFs, each with its original archived GeoCities `domain`/URL to pivot into
- **Empty/negative result looks like:** no matching GIFs, or a rate-limit page ("you've reached the limit… in a short period") — wait a minute and retry; it does not mean the archive is down.

## Gotchas & OpSec
- **Very narrow scope:** GeoCities only (shut down 2009), GIFs only — irrelevant to anyone without a 1990s–2000s web presence.
- Rate-limited; space out queries.
- OpSec: **passive** — you touch only the Internet Archive; no live target is contacted.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` / `[[archive-org]]` — GifCities is the *entry point* to a lost GeoCities page; the Wayback Machine is where you read the full archived site around that page.

## Trust & verifiability
`trust: trusted` — a first-party Internet Archive project drawing on their curated GeoCities capture; the provenance of each GIF (its original URL) is preserved and verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gifcities-org |
| category | search-engines |
| selectorsIn → selectorsOut | username → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no (rate-limit) |
