---
id: osintbookmarks
name: OSINTBookmarks
description: Use when you want a ready-made, categorised set of OSINT tool links loaded straight into your browser — returns an importable bookmarks tree, not lookup data.
url: https://github.com/5nacks/OSINTBookmarks
category: search-engines
path:
- search-engines
bestFor: Bootstrapping an investigation browser with a curated, categorised bookmarks file of OSINT resources.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; just download the HTML file from GitHub.
opsec: passive
opsecNote: Passive — it's a static bookmarks file, no queries run on import. Import it into your sock-puppet browser profile rather than your personal one to keep investigation tooling compartmented.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated bookmarks (built on SPMedia, the Bellingcat toolkit and Trace Labs contributions); links inevitably rot over time, so treat it as a starting map, not a guaranteed-live index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OSINT Bookmarks
tags:
- Tools collections/toolkits
- bookmarks
source: uk-osint
lastVerified: '2026-08-05'
enrichment: full
---

# OSINTBookmarks

> A curated OSINT bookmarks file you import once — instantly stocking your investigation browser with categorised links to search, social, geo, image and people tools.

## When to use
You're setting up (or refreshing) a dedicated OSINT browser profile and want a broad, organised toolkit at your fingertips instead of hunting for links per task. It's a launcher/index, not a resolver — it points you to tools, it doesn't return data itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Download the bookmarks HTML from https://github.com/5nacks/OSINTBookmarks.
2. In your sock-puppet browser: Firefox — `Ctrl+Shift+B` → Import and Backup → Import Bookmarks from HTML; Chrome/Edge/Safari have equivalent "Import bookmarks from HTML file" options.
3. Browse the imported folder tree (by discipline: search, social, geo, image, people, etc.) and open tools as needed.
4. Prune dead links as you go, and keep your own additions in the same tree.

## Inputs → Outputs
- **In:** none — it's a resource collection, not a lookup
- **Out:** none as a selector — an organised set of tool links
- **Empty/negative result looks like:** N/A; the only failure mode is stale links, which you remove as you encounter them.

## Gotchas & OpSec
- Human-in-the-loop: none to import; ongoing curation is on you as links rot.
- Vet each linked tool before use — a bookmark is not an endorsement of a tool's current safety or OpSec.
- Import into a compartmented profile, not your personal browser.

## Overlaps ("do both")
- Complements framework directories like the OSINT Framework and awesome-osint lists: same idea (a map of tools), delivered as a browser-native bookmarks file.

## Trust & verifiability
`trust: community` — a community bookmarks collection; its value is curation and breadth, but every link needs its own verification and freshness check before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintbookmarks |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
