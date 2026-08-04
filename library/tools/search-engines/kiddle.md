---
id: kiddle
name: Kiddle
description: Use when you want to see the child-safe, filtered web view of a topic or name — a kid-oriented Google Custom Search that shows what young users would find.
url: https://www.kiddle.co
category: search-engines
path:
- search-engines
bestFor: Viewing the filtered, kid-safe search results a young user would see for a term.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free, no account; a Google-powered Custom Search with additional kid-safe filtering.
opsec: passive
opsecNote: A normal passive search — you query Kiddle/Google, not any subject. No login, no notification.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party kid-safe search front-end over Google Custom Search; not affiliated with Google, and its filtering is its own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- kiddle.co
tags:
- kid-friendly-educational-search-engines
- safe-search
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Kiddle

> A kid-safe visual search engine built on Google Custom Search — useful for seeing the filtered, child-appropriate web view of a name or topic.

## When to use
Niche, but real in child-focused work: you want to know what a young user searching a `name`, term or place would actually be shown, or you want a lightly-filtered result set that strips explicit content. It's not an investigative lookup so much as a lens on the kid-safe web — occasionally handy when the subject or context involves minors and what content is reachable by them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.kiddle.co (Spanish version also exists).
2. Enter your `name`/keyword and choose a search type (Web, Facts, Images).
3. Read the filtered results — Kiddle blocks/keyword-filters explicit sites and orders kid-appropriate sources first.
4. Compare against a normal Google search to see what's filtered out or ranked differently.
5. Pivot: for actual investigative breadth, use a standard search engine; use Kiddle only for the specific "what would a child see" question.

## Inputs → Outputs
- **In:** `name` / keyword
- **Out:** filtered, kid-safe search results (a curated web view, not selectors)
- **Empty/negative result looks like:** blocked or sparse results for a term Kiddle deems non-kid-safe — reflecting its filter, not the true breadth of the web.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a standard search; nothing reaches any subject.
- Its results are deliberately filtered and re-ranked, so it is *not* a substitute for full-web search in an investigation — only for the safe-search perspective.

## Overlaps ("do both")
- Contrast with a normal Google/Bing search — the difference between the two shows exactly what the kid-safe filter removes, which is the whole point of using Kiddle.

## Trust & verifiability
`trust: community` — an independent kid-safe front-end over Google Custom Search; reliable for its filtered view, but unaffiliated with Google and not comprehensive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kiddle |
| category | search-engines |
| selectorsIn → selectorsOut | name →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
