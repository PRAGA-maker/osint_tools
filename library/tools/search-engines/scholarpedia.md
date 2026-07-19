---
id: scholarpedia
name: Scholarpedia
description: Use when you encounter a technical/scientific concept in a case and want an expert-written, peer-reviewed explainer — returns authoritative articles (with named expert authors) on science and scholarship topics.
url: http://www.scholarpedia.org
category: search-engines
path:
- search-engines
bestFor: Getting a peer-reviewed, expert-authored explanation of a scientific concept or the researchers associated with a field.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to read. Unlike Wikipedia, articles are commissioned from and signed by named experts and peer-reviewed; no account needed to read.
opsec: passive
opsecNote: You read a public encyclopedia; nothing about your subject is disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A peer-reviewed scholarly wiki with named expert authors and curators; more authoritative than open wikis, though narrow in topic coverage.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- scholarpedia.org
tags:
- toddington
- curated-directory
- specialty-search
- academic
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Scholarpedia

> A peer-reviewed, expert-authored encyclopedia — authoritative explainers for scientific concepts, with named experts behind each article.

## When to use
A case surfaces a technical or scientific concept you need to understand accurately — a method, a phenomenon, a specialized term in a document or a subject's field — and you want a reliable, expert-written explanation rather than an open-wiki entry you'd have to second-guess. Scholarpedia's articles are commissioned from and signed by named authorities and peer-reviewed, so they're a trustworthy grounding read. It's a background/reference resource, not a people-finding tool — its missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.scholarpedia.org and search the concept or term.
2. Read the article; note the named author(s) and curator listed — these are real domain experts.
3. Follow the references and the author's identity as a lead into the wider academic literature (and, if the person themselves matters, into arXiv/Google Scholar).
4. Use it to sanity-check a technical claim before you rely on it in analysis.
5. Pivot: an author's name → academic search (`[[arxiv-org]]`, Google Scholar) to map that expert's work.

## Inputs → Outputs
- **In:** none (a concept/term you look up)
- **Out:** peer-reviewed, expert-authored explanatory articles with references and named authors
- **Empty/negative result looks like:** narrow coverage — Scholarpedia only has articles in the fields it commissions (computational neuroscience, dynamical systems, physics, etc.); no result means the topic isn't covered here, so fall back to a broader encyclopedia or the primary literature.

## Gotchas & OpSec
- Human-in-the-loop: none.
- **Coverage is narrow and uneven:** it's deep in a handful of scientific areas and absent elsewhere — don't expect broad topical coverage.
- It's a reference for *understanding*, not for finding people; use it to interpret, then pivot to investigative tools.

## Overlaps ("do both")
- Pairs with Wikipedia (broad but open) and `[[arxiv-org]]`/Google Scholar (primary research) — Scholarpedia gives an authoritative expert explainer where it exists; the others give breadth and the underlying papers.

## Trust & verifiability
`trust: trusted` — articles are peer-reviewed and signed by named experts, making it a high-credibility reference within its narrow subject range; verify a topic is actually covered rather than assuming breadth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scholarpedia |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
