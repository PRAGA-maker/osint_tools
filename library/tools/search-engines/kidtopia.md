---
id: kidtopia
name: Kidtopia
description: Use when you want a teacher-curated, safe-search view of the web on a topic — returns filtered educational results from a Google Custom Search restricted to vetted sites.
url: http://www.kidtopia.info
category: search-engines
path:
- search-engines
bestFor: A pre-filtered, safe subset of the web for topic research where you want only vetted educational sources.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free (donation-supported); it's a Google Custom Search front-end, no account needed.
opsec: passive
opsecNote: Queries go to Google via the custom-search engine, logged under your session/IP like any Google search; use a sock-puppet browser if you don't want the query tied to you. Nothing is exposed to a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A librarian/teacher-curated Google Custom Search index; niche and narrow by design — useful for vetted results, not for comprehensive OSINT coverage.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Kidtopia search
- kidtopia.info
tags:
- safe-search
- education
- custom-search
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Kidtopia

> A teacher/librarian-curated Google Custom Search engine for elementary students — the web filtered down to vetted educational sites.

## When to use
Kidtopia is a niche, safe-search engine, not a general OSINT tool. Reach for it when you specifically want results restricted to a curated, safe subset of the web — for example teaching an OSINT technique in a school/child-safe context, or when researching a topic and you want to skip the noise and see only vetted educational sources. As a general people/entity search it's far too narrow; use a mainstream engine for real coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.kidtopia.info.
2. Enter a topic or `name` in the search box (or browse the subject categories: science, social studies, biography, animals, etc.).
3. Results come from a Google Custom Search restricted to curated sites — open the `document-id`s (pages) returned.
4. Treat it as a filtered lens, not exhaustive: absence here says nothing about the wider web.

## Inputs → Outputs
- **In:** `name` / topic keyword
- **Out:** `document-id` (curated educational pages)
- **Empty/negative result looks like:** few or no hits — the topic isn't in the curated index; switch to a mainstream engine, this is a deliberately small pool.

## Gotchas & OpSec
- Deliberately narrow (safe, curated) — do not use it as a primary OSINT search; it will miss almost everything a normal engine finds.
- It's a Google Custom Search wrapper, so results ultimately come from Google under your session.
- OpSec: passive; standard search-privacy hygiene applies.

## Overlaps ("do both")
- Complements mainstream and specialist search engines: use a general engine for coverage and reserve Kidtopia for when a vetted, safe result set is the actual requirement.

## Trust & verifiability
`trust: community` — a curated Custom Search maintained by educators; results are hand-vetted (a plus for reliability) but the index is small and topic-limited, so it's a supplement, never the whole search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kidtopia |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
