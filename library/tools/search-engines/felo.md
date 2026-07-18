---
id: felo
name: Felo
description: Use when you have a `name`, topic, or question and want an AI answer engine that searches the live web multilingually — returns a cited synthesis with source links to pivot from.
url: https://felo.ai/search
category: search-engines
path:
- search-engines
bestFor: Multilingual AI web search that summarizes findings on a person/topic with citations — good for cross-language coverage and quick lead-gathering.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to use with generous limits; a paid Pro tier adds higher usage and advanced models. Basic searches need no account.
opsec: passive
opsecNote: Your query is sent to Felo's servers and to the search/LLM providers behind it — treat the query text as disclosed to a third party. It does not touch the target directly. Avoid putting sensitive operational identifiers in the prompt; use a research session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial AI answer engine; results are LLM-synthesized from web sources and can hallucinate or misattribute. Value is the aggregated, cited leads — always click through to the primary source before trusting a claim.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Felo AI
- felo.ai
tags:
- toddington
- curated-directory
- search-engines
- deep-web-search
- artificial-intelligence
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Felo

> A free multilingual AI answer engine — ask about a person or topic and it searches the web across languages, then returns a synthesized, citation-backed summary you can pivot from.

## When to use
You want a fast, broad first pass on a `name`, `username`, org, or question — especially when the subject spans languages (Felo's strength is multilingual retrieval, e.g. surfacing Japanese/Chinese/European sources an English query misses). It's a lead-generation and orientation step: get a cited overview, spot which sources and profiles exist, then dig into the primaries. Not a database lookup — an aggregating search assistant.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://felo.ai/search (no login needed for basic use).
2. Ask a specific question or enter the subject — a `name` plus a disambiguator (employer, city, handle) works best.
3. Read the synthesized answer and, crucially, the **cited sources** listed alongside it.
4. Try the query in the subject's likely native language too — Felo will pull sources an English-only search misses.
5. Click through every citation you intend to rely on — confirm the claim at the source.
6. Pivot: cited pages → `social-profile`s, articles, and records; corroborated facts → your other tools; contradictions → flags to resolve.

## Inputs → Outputs
- **In:** `name` / `username` / topic / natural-language question
- **Out:** an AI summary plus cited source links (often surfacing `social-profile`s, articles, and `name` associations)
- **Empty/negative result looks like:** a vague, generic answer with weak or off-topic citations — a signal the web has little on the subject (or your query was ambiguous), not a confirmed negative.

## Gotchas & OpSec
- **LLM output can hallucinate or misattribute** — never treat the summary as fact without opening the cited source; if a claim has no citation, distrust it.
- Coverage/quality vary by language and topic; rerun in other languages for non-English subjects.
- Your query goes to Felo and its upstream providers — don't include sensitive operational identifiers.

## Overlaps ("do both")
- Complements traditional search engines and other AI answer engines (Perplexity-style tools) — run more than one, since each retrieves and summarizes different sources; use classic search to verify what the AI surfaces.

## Trust & verifiability
`trust: unverified` — a commercial AI aggregator with no editorial guarantee; its value is the cited leads, and verifiability comes entirely from following those citations to primary sources yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | felo |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
