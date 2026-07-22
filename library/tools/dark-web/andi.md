---
id: andi
name: Andi Search
description: Use when you have a `name` or topic and want an AI-summarised, ad-free web search — returns synthesised answers with cited source links to pivot from.
url: https://andisearch.com/
category: dark-web
path:
- dark-web
bestFor: Ad-free, privacy-oriented AI search that summarises results and cites sources for a name or topic.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to use; no account required for basic search. Privacy-focused (does not require login or profiling).
opsec: passive
opsecNote: Queries go to Andi's servers rather than a major ad-tracking engine, which is a mild privacy plus, but it is still a third party seeing your search — use a VPN/sock-puppet for sensitive queries. It reads the clearnet, not the dark web, despite this file's category.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent AI search product; answers are model-generated summaries that can be incomplete or wrong, so always follow the cited links.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Andi
- andisearch.com
tags:
- toddington
- curated-directory
- deep-web-search
- artificial-intelligence
- ai-search
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Andi Search

> A conversational, ad-free AI search engine — useful for a quick summarised sweep of a `name` or topic that surfaces cited links to chase down.

## When to use
You want a fast, ad-free overview of what the open web says about a `name`, `username`, organisation, or topic, with the results summarised and the sources cited so you can jump to primary pages. Andi is a convenience/orientation tool: its value is a clean, privacy-oriented first pass and the links it exposes, not the AI summary itself. (Despite this file's `dark-web` category from harvesting, Andi searches the clearnet.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://andisearch.com/ and enter a query — a quoted name/handle or a topic question.
2. Read the summarised answer, then — critically — open the cited source links; these are the OSINT-actionable part.
3. Use its follow-up/conversational prompts to narrow (e.g. add a location or employer).
4. Cross-check any factual claim against the underlying sources before trusting it.
5. Pivot: cited pages become `social-profile`/`employer-org` leads to enrich with dedicated tools.

## Inputs → Outputs
- **In:** `name` / `username` / topic
- **Out:** a summarised answer plus cited links pointing to `social-profile`s, `employer-org` pages, and articles
- **Empty/negative result looks like:** a thin summary with weak or no citations, or an "I couldn't find much" style answer — treat as "the open web is quiet on this term," and fall back to targeted engines and `site:` dorks.

## Gotchas & OpSec
- AI summaries can hallucinate or omit; never cite Andi's prose as fact — cite the source it links.
- Coverage is general-web; for deep/structured OSINT you still need specialised tools and operators.
- It is a third-party search service; use a VPN/sock-puppet for sensitive subjects.

## Overlaps ("do both")
- Pairs with mainstream and privacy search engines plus `site:` dorking — Andi gives a fast summarised orientation, the others give exhaustive, operator-controlled results.

## Trust & verifiability
`trust: community` — a legitimate independent AI search tool; because its answers are model-generated, reliability rests on the cited sources, which you must open and verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | andi |
| category | dark-web |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
