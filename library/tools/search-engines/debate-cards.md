---
id: debate-cards
name: Debate.Cards
description: Use when you have a `name` (an author or expert) and want to find where their work is quoted as competitive-debate evidence — returns citations, publications, and affiliations.
url: http://debate.cards/
category: search-engines
path:
- search-engines
bestFor: Full-text searching competitive-debate evidence to surface an author's quoted work and citation details.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free to search and read; the corpus is community-uploaded open-evidence debate files.
opsec: passive
opsecNote: Read-only full-text search of a public evidence archive; no account, no per-subject leak beyond a normal web query. Clean-browser hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run indexer of open debate evidence; cards are excerpts uploaded by debaters, so citation accuracy varies and passages are selectively highlighted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- debate.cards
- Debate Card Search Engine
tags:
- academic-search
- evidence-search
- citations
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Debate.Cards

> A full-text search engine over competitive-debate "cards" (cut evidence), useful for finding where a named author or expert has been quoted and what was said.

## When to use
You have a `name` — an academic, journalist, analyst, or expert — and want to see their work surfaced as debate evidence, complete with the author's credentials, publication, year, and often institutional affiliation. Because debate cards are cut from articles, books, and reports and tagged with full citations, a search can reveal an author's `employer-org`, their stance on a topic, and the exact passage debaters found quotable. A niche corroboration/attribution tool rather than a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://debate.cards/ and enter a search term — an author surname, an organisation, or a topic phrase.
2. Read the returned cards: each shows a tag (the claim), a full citation (author, credentials, publication, date), and the highlighted source text.
3. Note the author's stated affiliation/credentials and the original publication, which point back to a primary source.
4. Pivot: the author `name` + `employer-org` feed academic/people search; the cited publication feeds a direct read of the primary source; a distinctive quote can be web-searched to find the original article.

## Inputs → Outputs
- **In:** `name` (author/expert) or topic keyword
- **Out:** citation details — author `name`, credentials, and `employer-org`/affiliation — plus the source publication
- **Empty/negative result looks like:** no cards match the query — expected for anyone whose work has not been used as debate evidence, which is the vast majority of people. This is a specialised corpus, not a general index.

## Gotchas & OpSec
- Coverage is limited to material debaters have cut and uploaded; it is skewed toward argumentative, policy, and academic sources and is not a comprehensive citation database.
- Cards are selectively highlighted, so the excerpt reflects a debater's framing — always follow the citation back to the primary source before quoting.
- Citation accuracy varies with the uploader; treat author/affiliation as leads.

## Overlaps ("do both")
- Pairs with Google Scholar and general web search — this shows how an author's work is used argumentatively, those confirm the full publication record and the primary source.

## Trust & verifiability
`trust: community` — a community-maintained index of open debate evidence; the cards are real excerpts but user-uploaded and selectively cut, so verify any citation against the original publication.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | debate-cards |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
