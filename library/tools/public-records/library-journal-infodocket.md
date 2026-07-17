---
id: library-journal-infodocket
name: LJ INFOdocket
description: Use when you want to discover newly released databases, government reports, and research resources — a current-awareness feed for finding NEW OSINT sources (not a person lookup).
url: https://www.infodocket.com/
category: public-records
path:
- public-records
bestFor: Staying current on newly published databases, government/NGO reports, archives, and research tools that become new OSINT sources.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to read; published by Library Journal (edited by Gary Price). No account.
opsec: passive
opsecNote: Reading a public news/resource blog is passive and reveals nothing to any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running, professionally edited library-and-information-science news site (Library Journal / Gary Price); reliable curation of primary-source and database announcements.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- INFOdocket
- infodocket.com
- Gary Price INFOdocket
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# LJ INFOdocket

> A meticulously edited current-awareness feed for the information world — where new databases, government reports, archives, and research tools are announced, i.e. where you discover your next OSINT source.

## When to use
This is a source-discovery tool, not a subject lookup. Reach for it to keep abreast of newly launched or updated data resources: government and NGO reports, statistical databases, digitised archives, court/records portals, and research tools. When an investigation needs a data source you don't yet know exists, INFOdocket's archive and feed are a curated place to find it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.infodocket.com/ and browse recent posts, or search the site for a topic/agency/dataset.
2. Each post summarises and links a newly available resource (report, database, archive) — follow the link to the primary source.
3. Bookmark relevant new databases/tools into your own workflow.
4. Pivot: a newly announced records database or archive becomes a concrete lookup you run against your subject.

## Inputs → Outputs
- **In:** a topic/agency/dataset keyword (no subject selectors)
- **Out:** links to newly published data resources, reports, and tools — leads to new OSINT sources, not data about a person.
- **Empty/negative result looks like:** no relevant post for your topic — the resource you want may not have been covered; search the primary agency directly.

## Gotchas & OpSec
- It points to sources; it isn't itself a database — the value is discovery, then you use the linked resource.
- US/library-sector tilt, but it regularly covers globally useful government and research resources.
- OpSec: passive public reading.

## Overlaps ("do both")
- Complements curated OSINT tool directories — INFOdocket surfaces brand-new primary databases/reports before they hit the lists, so pair it with your standard directories to keep your source set fresh.

## Trust & verifiability
`trust: trusted` — a professionally edited Library Journal publication with a strong reputation for accurate, primary-source-linked curation; you verify each linked resource at its origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | library-journal-infodocket |
| category | public-records |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
