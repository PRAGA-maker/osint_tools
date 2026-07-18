---
id: osint-kit-buddhsen-tripathi
name: OSINT-Kit (Buddhsen Tripathi)
description: Use when you need to discover which tool fits an investigative task — a curated, categorised directory of OSINT tools returning pointers to other tools.
url: https://github.com/buddhsen-tripathi/OSINT-Kit
category: search-engines
path:
- search-engines
bestFor: A curated, categorised reference directory of OSINT tools to browse when picking the right tool for a task.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (MIT); browse the hosted site or the GitHub repo, no account needed.
opsec: passive
opsecNote: A static reference site/repo — reading it touches no target and reveals nothing. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained curated list (MIT, ~170 stars); a directory of links, not a data source itself — vet each linked tool independently.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OSINT-Kit
- buddhsen-tripathi/OSINT-Kit
tags:
- meta-resource
- tool-directory
- awesome-list
source: gh-topic-osint-resources
lastVerified: '2026-07-18'
enrichment: full
---

# OSINT-Kit (Buddhsen Tripathi)

> A tidy, categorised catalogue of OSINT tools — a meta-resource for finding *which* tool to reach for, not a data source itself.

## When to use
You are unsure which tool covers a given task (metadata analysis, image/video, breach search, geolocation, domain intel, SOCMINT) and want a curated shortlist rather than a raw awesome-list dump. OSINT-Kit groups tools by category with short descriptions on a clean hosted site, so it works as a quick jump-off when planning an investigation. It returns pointers to other tools — treat it as an index, then pivot into the actual tools in this library.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the hosted site (buddhsen-tripathi.github.io/OSINT-Kit) or the GitHub repo.
2. Browse to the category matching your task (e.g. "Image/Video Analysis", "Data Breaches", "Location").
3. Read the short entries and follow to the tool you need.
4. Cross-reference the tool against this library's authored skill (selectors, opsec, trust) before using it.
5. Pivot: it points you *to* tools — the actual selectors/outputs come from whichever tool you then use.

## Inputs → Outputs
- **In:** (none — it is a browsable directory, not a query tool)
- **Out:** pointers to other OSINT tools by category (no data selectors of its own)
- **Empty/negative result looks like:** the category you need isn't covered or links are stale — fall back to this library's own index and broader awesome-lists.

## Gotchas & OpSec
- It is a **directory of links**, not a tool — it produces no intelligence itself and links can rot; verify each destination independently.
- Curation reflects one maintainer's choices; it is not exhaustive.
- OpSec: passive reading; nothing is disclosed.

## Overlaps ("do both")
- Complements this library and larger awesome-OSINT lists — use OSINT-Kit for a quick categorised shortlist, then rely on the authored skills here for the operational detail (opsec, selectors, trust) it doesn't provide.

## Trust & verifiability
`trust: community` — a community-curated link list; useful for discovery, but every linked tool must be evaluated on its own merits before you trust its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-kit-buddhsen-tripathi |
| category | search-engines |
| selectorsIn → selectorsOut | (none) → (directory of tools) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
