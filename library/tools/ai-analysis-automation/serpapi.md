---
id: serpapi
name: SerpApi
description: Use when you need to run search-engine queries at scale and get structured results in code — returns JSON of Google/Bing/etc. results (organic, maps, knowledge graph, images).
url: https://serpapi.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Programmatic, structured scraping of Google and other search engines (handles proxies/CAPTCHAs).
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- domain
status: live
pricing: freemium
costNote: Free plan gives ~250 searches/month; paid plans ($25–$275+/mo) for higher volume. Requires an API key.
opsec: passive
opsecNote: SerpApi runs the search from its own infrastructure/proxies, so the query does not originate from your IP — good separation. But your search terms (which may name the target) are sent to a third party; assume they're logged.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: trusted
trustNote: Established commercial SERP-scraping vendor with documented, stable JSON schemas; results mirror the live search engine.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- SerpApi.com
tags:
- ai-analysis-automation
- search
- api
- automation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# SerpApi

> A search-engine scraping API — send a query, get clean JSON of the results, with proxy rotation and CAPTCHA handling done for you.

## When to use
You want to automate search across a subject's `name`, `username`, or `email` — dorking at scale, monitoring for new mentions, or feeding results into a pipeline — without building and maintaining your own scraper. SerpApi returns structured organic results plus Maps/Local, Knowledge Graph, images, news, and shopping, from Google and many other engines.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://serpapi.com/ and get an API key (free tier ≈ 250 searches/month).
2. Call the API with your query and parameters (engine, location, language, result type) — via HTTP or one of the client libraries.
3. Parse the JSON: organic result links/titles/snippets, plus structured blocks (knowledge graph, local pack, images).
4. Pivot: result URLs surface `social-profile`s and `domain`s to enumerate; loop dork queries (e.g. `"name" site:linkedin.com`) to build a footprint.

## Inputs → Outputs
- **In:** a search query built from `name`/`username`/`email` (+ engine/location params)
- **Out:** structured JSON — result links (`domain`, `social-profile`), snippets, knowledge-graph facts
- **Empty/negative result looks like:** an empty results array — the query genuinely returns nothing on that engine/locale, or you've exhausted your free quota.

## Gotchas & OpSec
- Requires an account/API key and has quota limits; heavy dorking needs a paid plan.
- Your queries (possibly containing the target's name) go to SerpApi — acceptable for OSINT, but not zero-leak.
- Results reflect the engine's personalisation/locale settings you pass — set location deliberately.

## Overlaps ("do both")
- Complements manual dorking and `[[advanced-search-operators-list]]` — write the operators there, then run them at scale here; cross-check against the live engine for anything critical.

## Trust & verifiability
`trust: trusted` — a mature commercial API that faithfully mirrors search-engine output; the data is the engine's, so verify individual results against the live page when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | serpapi |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, email → social-profile, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
