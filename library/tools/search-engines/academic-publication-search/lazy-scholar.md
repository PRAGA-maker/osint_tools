---
id: lazy-scholar
name: Lazy Scholar
description: Use when you have a paper's DOI/URL and want its free full text — a browser extension that finds legal open-access copies of paywalled academic articles.
url: https://lazyscholar.org/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Getting free legal full-text of a paywalled paper via a browser extension.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free browser extension; no subscription needed (optional free account syncs your library across devices).
opsec: passive
opsecNote: The extension queries open-access indexes in the background for the paper you're viewing; it doesn't broadcast your identity to the publisher. Still, install it in a research/sock-puppet browser profile rather than a personal one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Community-built academic-access extension similar to Unpaywall; it links to legal open-access copies from public indexes, so reliability depends on those sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- LazyScholar
- lazyscholar.org
tags:
- academic
- open-access
- browser-extension
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Lazy Scholar

> A browser extension that hunts down free, legal full-text copies of paywalled academic papers — one click from a journal page to an open-access PDF.

## When to use
Your research has led you to a specific academic paper (a `document-id`: DOI or article URL) that corroborates a subject's work, claims, or a technical detail, but it sits behind a paywall. Lazy Scholar checks open-access indexes and repositories for a free, legal copy so you can read the source rather than just the abstract. It's a document-access utility that supports academic/expert investigations — it doesn't identify people itself.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Lazy Scholar extension in a research browser profile from https://lazyscholar.org/.
2. Navigate to the paywalled article's page (or a DOI/Google Scholar result); the extension automatically checks for free full text in the background.
3. Click its indicator to open the free PDF/full text where one exists; it also surfaces citation counts and related metadata.
4. Pivot: the full text yields author affiliations, co-authors (`associate`), funding and methods — feed those into academic-index and people/org research.

## Inputs → Outputs
- **In:** `document-id` (a DOI or article URL you're viewing)
- **Out:** `document-id` — a link to a free legal full-text copy where an open-access version exists
- **Empty/negative result looks like:** no free copy found — the paper has no open-access version indexed; that's common for recent/closed journals, so try the author's own page or an interlibrary route.

## Gotchas & OpSec
- Human-in-the-loop: one-time extension install; requires a Chromium/Firefox browser.
- OpSec: passive — it queries open indexes, not the publisher on your behalf; still keep it in a non-personal profile.
- It only finds *legal* open-access copies, so paywalled-only papers simply won't resolve; it's an access aid, not a piracy tool.

## Overlaps ("do both")
- Pairs with academic indexes like `[[scinapse-io]]` and `[[research-rabbit]]` — those find which papers exist and who wrote them, while Lazy Scholar gets you the readable full text of a specific one.

## Trust & verifiability
`trust: community` — a community extension that relays open-access sources (Unpaywall-style); the papers it links are authoritative from their repositories, so verify a copy is the final published version when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lazy-scholar |
| category | search-engines |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
