---
id: word-tracker
name: Wordtracker
description: Use when you have a topic, brand, or `username`/handle keyword and want to see the real search phrases and related terms people use around it — returns keyword lists and search-volume signals (no subject PII).
url: https://www.wordtracker.com
category: search-engines
path:
- search-engines
bestFor: Discovering the alternate terms, spellings, and phrasings people search for around a name, brand, or topic.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free keyword tool gives a limited number of results/searches; deeper volume data and unlimited queries require a paid plan.
opsec: passive
opsecNote: You query Wordtracker's own database with a keyword, not the target's infrastructure — the subject sees nothing. Your search terms are logged by Wordtracker; use a sock-puppet account if the keyword itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established commercial SEO keyword-research vendor; the data is aggregated search-behaviour, not verified facts about any person.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
aliases:
- wordtracker.com
tags:
- keywords-discovery-and-research
- search-terms
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Wordtracker

> A commercial keyword-research engine used sideways in OSINT: it surfaces the exact phrasings, misspellings, and related terms real people type, so you can widen a search around a name, handle, or topic.

## When to use
Your first queries for a subject's name, brand, or online handle are returning little, and you suspect people refer to them with different words, spellings, or phrasings. Wordtracker takes a seed keyword and returns the associated search phrases and their relative popularity — a way to generate better query variants for Google, social search, and username tools rather than a source of subject data itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.wordtracker.com and open the free keyword tool (a free registration unlocks more results).
2. Enter a seed term — a name, brand, nickname, or topic tied to the subject.
3. Read the output: a ranked list of related search phrases with volume/competition signals. Note alternate spellings, co-occurring terms, and long-tail variants.
4. Pivot: feed the strongest variants back into general search, [[google-dorking]]-style queries, or a username hunt to catch results your first phrasing missed.

## Inputs → Outputs
- **In:** a seed keyword (name / brand / nickname / topic) — no subject PII
- **Out:** related search phrases and search-volume/competition signals
- **Empty/negative result looks like:** few or no related terms for an obscure or unique seed — normal for rare names; broaden the seed or use it only as a spelling-variant check.

## Gotchas & OpSec
- Human-in-the-loop: none for the query itself, though the free tier caps results and a paid plan is needed for full volume data.
- OpSec: passive — you touch Wordtracker, never the subject. It is a research aid, not an identity source; it will not return a person's details.
- Treat volumes as directional SEO estimates, not precise counts.

## Overlaps ("do both")
- Pairs with [[google-dorking]] — Wordtracker generates the term variants, dorking applies them as precise queries; together they recover results a single phrasing misses.

## Trust & verifiability
`trust: community` — a reputable SEO vendor, but the value to an investigation is the term-discovery, not any verifiable fact. Confirm anything actionable in the downstream search results, not here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | word-tracker |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
