---
id: keywordtool
name: Keyword Tool
description: Use when you have a `name`, `username`, or brand and want the search-autocomplete phrases the world associates with it — returns related query terms across Google/YouTube/Bing/etc.
url: http://keywordtool.io
category: search-engines
path:
- search-engines
bestFor: Harvesting search-engine autocomplete suggestions around a term to discover associated topics and phrasings.
selectorsIn:
- name
- username
selectorsOut: []
status: live
pricing: freemium
costNote: The free tier lists autocomplete keyword suggestions; search volume, CPC, and full export are paywalled behind a paid plan.
opsec: passive
opsecNote: Passive keyword lookups against a third-party SEO service; the subject is never contacted. Queries reach keywordtool.io — use a clean browser for sensitive terms.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial SEO keyword-research service that scrapes public autocomplete APIs; the suggestions are real, the analytics numbers are its own estimates.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-trends
- answerthepublic
aliases:
- KeywordTool
- keywordtool.io
tags:
- keywords-discovery-and-research
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Keyword Tool

> An SEO autocomplete harvester — feed it a name, handle, or brand and it returns the search phrases people actually type around it, useful for uncovering associated topics and spelling variants.

## When to use
You want the "long tail" of how a `name`, `username`, or brand appears in search: what terms search engines autocomplete alongside it, common misspellings, and associated topics/products. That can hint at a subject's associated businesses, aliases, or notable events worth searching directly. It is a lead-generator for search terms, not a data source about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://keywordtool.io.
2. Pick the source engine (Google, YouTube, Bing, Amazon, etc.) and enter the `name`/`username`/brand.
3. Read the free list of autocomplete suggestions — related phrases, question forms, and variants.
4. Take the interesting suggestions and search them directly on the real engine (the volume/CPC numbers here are paywalled and unnecessary for OSINT).
5. Pivot: promising phrases → targeted web/dork searches; discovered aliases/associated brands → people- and company-lookups.

## Inputs → Outputs
- **In:** `name`, `username`, or brand term
- **Out:** search-autocomplete suggestion phrases across chosen engines (no personal selector — leads to run elsewhere)
- **Empty/negative result looks like:** few or no suggestions — the term isn't commonly searched, so autocomplete has nothing; it says nothing about the person directly.

## Gotchas & OpSec
- Human-in-the-loop: the free tier gives the keyword list but paywalls volume/CPC/export — the free list is all you need for OSINT; don't pay for the metrics.
- Suggestions reflect aggregate search behaviour, not facts about your subject — treat them as search leads only.
- OpSec: passive; queries go to a third party.

## Overlaps ("do both")
- Pairs with `[[google-trends]]` and `[[answerthepublic]]` — Trends shows interest over time/geography and AnswerThePublic visualises question-phrasings; together they map how a term is searched.

## Trust & verifiability
`trust: community` — a legitimate commercial SEO tool; the autocomplete suggestions are scraped from real engine APIs (reliable as *search behaviour*), while its volume estimates are proprietary and unverifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | keywordtool |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
