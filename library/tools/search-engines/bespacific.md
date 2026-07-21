---
id: bespacific
name: beSpacific
description: Use when you have a topic, agency, or `name` tied to law/tech/government and want a curated, searchable feed of primary-source reporting on it — returns links to authoritative documents and articles (a research pivot, no direct selector output).
url: http://www.bespacific.com/
category: search-engines
path:
- search-engines
bestFor: Topic-driven research on law, privacy, surveillance, government and technology via a long-running curated blog with a searchable 20+ year archive.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free to read and search; no account. Some linked primary sources may sit behind their own paywalls.
opsec: passive
opsecNote: Passive — reading and searching a public research blog. Requests come from your IP and reveal nothing to any subject. If you follow links to logging destinations, standard web-hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored since 2002 by law librarian Sabrina I. Pacifici; a widely respected, single-author professional resource that links to primary sources rather than publishing rumor.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- beSpacific.com
tags:
- toddington
- curated-directory
- specialty-search
- legal-research
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# beSpacific

> A curated, searchable 20+-year archive of "accurate, focused research on law, technology and knowledge discovery" by law librarian Sabrina Pacifici — a way in to authoritative primary sources, not a people-finder.

## When to use
You need background or primary-source material on a **topic, agency, statute, or public matter** connected to your subject — privacy law, surveillance programs, government data practices, cybersecurity, a named agency or program — rather than a lookup on a private individual. It is strongest for framing the legal/technical context around a case and for finding the authoritative document behind a news story.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.bespacific.com/ and use the site search (or a `site:bespacific.com <terms>` dork) for your topic, agency, or public figure's `name`.
2. Browse by category (Legal Research, privacy, government documents, cybersecurity, etc.) for a curated reading list.
3. Follow each post through to the **primary source** it links (the point of the site — it surfaces the underlying report/dataset/ruling).
4. Pivot: use the primary documents to establish context, timelines, and named institutions/officials relevant to your investigation.

## Inputs → Outputs
- **In:** a topic / agency / public `name`
- **Out:** curated links to authoritative articles, reports and primary documents (context and leads, not a structured selector)
- **Empty/negative result looks like:** no posts on a niche or non-US-centric topic — the archive skews toward US law/tech/government, so broaden terms or use a general search.

## Gotchas & OpSec
- It is a **research blog/database**, not a person-search engine — use it for context around a subject, not to locate one.
- Coverage leans US law, government and technology; other jurisdictions are thinner.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with general web search and government-records tools — beSpacific points you at the authoritative primary source, which you then pull and search directly.

## Trust & verifiability
`trust: trusted` — a single, well-regarded law-librarian author (Sabrina Pacifici) with a two-decade track record who links to primary sources; still verify by reading the original document she cites, not just the blog summary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bespacific |
| category | search-engines |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
