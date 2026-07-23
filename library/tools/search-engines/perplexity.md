---
id: perplexity
name: Perplexity
description: Use when you have a natural-language research question about a `name`/entity and want a cited synthesis across the web — returns a summarised answer with source links to chase.
url: https://www.perplexity.ai
category: search-engines
path:
- search-engines
bestFor: Asking a plain-English question and getting a source-cited synthesis to jump-start research.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier covers standard searches; a paid Pro tier adds more advanced-model queries and features. No account strictly required for basic use, but signing in unlocks more.
opsec: active
opsecNote: Your question is sent to Perplexity (and, indirectly, its search and model providers) and may be retained/used per their policy, so don't paste truly sensitive target details. Perplexity itself fetches the web pages, not you — so the *sources* aren't directly touched by your IP, but your query leaves a trail with Perplexity. Use a research account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A reputable AI-search product, but it is an LLM that summarises and can hallucinate or misattribute; the cited source links are the ground truth, not the generated prose.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- birdsql
aliases:
- Perplexity AI
- perplexity.ai
tags:
- general-search
- ai
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Perplexity

> An AI answer engine: ask a research question in plain English and get a synthesised, source-cited answer — a fast way to orient on an entity, provided you always click through to the citations.

## When to use
You have a broad or fuzzy research question — "what companies is <name> associated with", "summarise the public record on <entity>", "what is <domain> known for" — and want a quick synthesised starting point with links, rather than paging through raw search results. Reach for Perplexity to orient and to gather candidate sources fast. Treat its prose as a lead generator: the *value* is the cited links, which you must verify, because the summary can be wrong or conflate people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.perplexity.ai and ask your question in natural language; add context ("the <name> who works in <field>") to disambiguate.
2. Read the synthesised answer, then — critically — open every cited source link.
3. Verify each claim against its source; discard anything the sources don't actually support.
4. Use follow-up questions to drill into a specific thread, or the Pro/API tiers for heavier work.
5. Pivot: confirmed source pages (a `social-profile`, a filing, an article) feed the rest of your workflow; the AI summary itself is never a citable finding.

## Inputs → Outputs
- **In:** a natural-language question, ideally scoped to a `name`/entity
- **Out:** a synthesised answer plus source citations (links to pages, profiles, articles)
- **Empty/negative result looks like:** a hedged or generic answer with weak/irrelevant citations — the web has little, or your query was too vague; tighten it and re-ask.

## Gotchas & OpSec
- It's an LLM: it can hallucinate, misattribute, or merge two different people with the same name. Never trust the prose without checking the cited source.
- OpSec: **active** in the sense that your query is sent to and retained by a third-party service — keep sensitive target specifics out of it and use a research account.
- Coverage and recency depend on what its search layer indexed; corroborate with direct searches.

## Overlaps ("do both")
- Complements traditional search engines and specialised people/entity tools — use Perplexity to *orient and gather leads*, then verify each lead with primary sources and dedicated OSINT tools. Cross-check its citations against a manual search.

## Trust & verifiability
`trust: community` — a capable AI-search product whose generated text is not authoritative; verifiability comes entirely from clicking through to and confirming the cited sources, treating the summary as a hypothesis.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | perplexity |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
