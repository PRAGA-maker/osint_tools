---
id: yandex-wordstat
name: Yandex Wordstat
description: Use when you need search-demand and regional interest data for a keyword/name/brand on Yandex — returns query volumes and geographic breakdown, a soft signal of where a term matters.
url: https://wordstat.yandex.com
category: search-engines
path:
- search-engines
bestFor: Gauging Yandex search demand for a keyword/term and its regional distribution (strong for Russia/CIS).
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: You query Yandex's aggregated search-statistics tool, not any individual — no person is identified or alerted. It requires a Yandex account to use; log in with a sock-puppet Yandex account, not a personal one, since Yandex logs the session.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Yandex product; the data authentically reflects Yandex search demand (Russia/CIS-weighted), though it's aggregate keyword statistics, not per-person data.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- yandex
- yandex-image-search
- yandex-maps
- yandex-browser
- yandex-images
- yandex-mail
- yandex-russia
- yandex-translate
- yandex-video-search
- yandexmaps
aliases:
- Yandex Wordstat
- wordstat.yandex.com
tags:
- keyword-research
- search-demand
- keywords-discovery-and-research
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Yandex Wordstat

> Yandex's keyword-statistics tool — how often people search a term on Yandex, broken down by region and over time; a demand/interest signal, strongest for Russia and the CIS.

## When to use
A supporting, low-signal tool. When investigating a name, brand, product, or phrase with a Russia/CIS dimension, Wordstat shows how much it's searched on Yandex and *where* (regional breakdown) and *when* (trend over time). Useful for gauging whether a term/alias is locally significant, spotting related queries people pair it with, and getting a rough geographic weighting of interest. It profiles search behavior in aggregate, not individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wordstat.yandex.com and log in with a (sock-puppet) Yandex account.
2. Enter the keyword/term — a `name`, alias, brand, or phrase.
3. Read the results: total monthly query counts, associated/related queries, the "by region" tab for geographic distribution, and the history/seasonality view.
4. Pivot: related queries suggest search terms and context; the regional breakdown adds a soft geographic lead to combine with stronger evidence.

## Inputs → Outputs
- **In:** `name` / keyword / phrase
- **Out:** aggregate Yandex query volumes, related queries, regional distribution, and time trend (no per-person selectors)
- **Empty/negative result looks like:** near-zero volume — the term isn't searched much on Yandex (common for non-Russian-language or niche terms); it doesn't mean the subject is insignificant, just low Yandex demand.

## Gotchas & OpSec
- Human-in-the-loop: a Yandex account/login is required (`account-login`) — use a puppet account.
- OpSec: passive — aggregate statistics, no individual is queried or alerted.
- Yandex-centric and Russia/CIS-weighted; it reflects Yandex users, not global search, so read regional/volume figures in that context.

## Overlaps ("do both")
- Pairs with Google Trends / Keyword Planner (Western search demand) and the broader [[yandex]] toolset — use Wordstat for the Yandex/CIS view and Google's tools for the rest, since their user bases and coverage differ sharply.

## Trust & verifiability
`trust: trusted` — a first-party Yandex product, so the search-demand figures are authentic. Just remember they're aggregate keyword statistics weighted to Yandex's audience, useful as a soft interest/geographic signal rather than evidence about any individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yandex-wordstat |
| category | search-engines |
| selectorsIn → selectorsOut | name → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
