---
id: bellingcat-s-online-investigation-toolkit-2
name: Bellingcat's Online Investigation Toolkit
description: Use when you need a vetted, current directory of OSINT tools by category (geolocation, social media, maps, verification) — returns pointers to specific tools, not person data itself.
url: https://bellingcat.gitbook.io/toolkit
category: search-engines
path:
- search-engines
bestFor: A continuously maintained, category-organised meta-directory of investigation tools curated by Bellingcat — the place to discover the right tool for a task.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public GitBook; no account. Some tools it links to are themselves paid, but the directory is free.
opsec: passive
opsecNote: Reading the toolkit is inert and reveals nothing about a target. OpSec depends entirely on which linked tool you then use — assess each tool on its own page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Bellingcat, a leading open-source investigation organisation; the toolkit is community-vetted and kept current, making it one of the most reliable meta-directories.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bellingcat Toolkit
- Bellingcat's Online Investigation Toolkit
tags:
- tool-collection
- geolocation
- social-networks
- verification
source: ultimate-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Bellingcat's Online Investigation Toolkit

> Bellingcat's living, category-organised catalogue of investigation tools — where you go to find the *right* tool, not to search for a person directly.

## When to use
You know the task (geolocate a photo, verify a video, enumerate a username, map a flight) but not the best current tool for it. Bellingcat maintains this toolkit as a vetted, frequently updated index across geolocation, maps, imagery/verification, social media, transport, and archiving. Reach for it when your usual tool has died or you need coverage for a category you don't have a go-to for — especially valuable because dead OSINT tools are the norm and Bellingcat prunes/updates entries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bellingcat.gitbook.io/toolkit.
2. Browse or search by category (e.g. "Maps, Satellite & Aerial Imagery," "Social Media," "Verification," "Transportation").
3. Pick a tool entry; read its short description and caveats, then open the tool's own site.
4. Because it's a directory, the actual investigative work happens in the tool you select — assess that tool's cost/OpSec/trust separately.
5. Pivot: use it as the jumping-off point at the start of a task, or when a specific step (say, reverse-image or flight-tracking) has no obvious tool.

## Inputs → Outputs
- **In:** none (it's a directory; you bring a task/category, not a selector)
- **Out:** curated pointers to specific OSINT tools by category
- **Empty/negative result looks like:** a category with few entries, or a listed tool that has since died — cross-check against other meta-lists (OSINT Framework, awesome-osint) if the toolkit is thin for your need.

## Gotchas & OpSec
- It's a **meta-directory, not a search engine** — it won't return facts about a person; it returns tools.
- Even a well-maintained list lags reality; some linked tools may be down. Verify the tool works before relying on it.
- OpSec: reading is passive; the risk lives in whichever tool you then run.

## Overlaps ("do both")
- Complements other meta-collections (OSINT Framework, awesome-osint, IntelTechniques) — consult more than one, since each curates differently.

## Trust & verifiability
`trust: trusted` — maintained by Bellingcat, a highly credible investigation org; entries are vetted. Still confirm each linked tool's current status yourself, as any directory can go stale between updates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat-s-online-investigation-toolkit-2 |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
