---
id: disconnect-search
name: Disconnect Search
description: Use when you want a search that isn't tied to your profile or logged with your identity — returns results from your chosen engine (e.g. DuckDuckGo) without personalization skew.
url: https://search.disconnect.me/
category: search-engines
path:
- search-engines
bestFor: Running un-personalized, privacy-preserving searches so results aren't shaped by your history or identity.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free privacy search front end; no account required.
opsec: passive
opsecNote: It reduces the personalization/tracking tied to your searches, giving results closer to a neutral "logged-out" view — but it is not anonymity. Your IP still reaches the provider; for real separation search from Tor or a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A privacy-search front end (by Disconnect) that passes queries to mainstream providers like DuckDuckGo; the results are the provider's, with reduced personalization.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- disconnect
aliases:
- search.disconnect.me
tags:
- privacy-focused-search-engines
- private-search
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Disconnect Search

> A privacy-preserving search front end: it runs your query through a mainstream engine (DuckDuckGo and others) without binding it to your profile, so results come back closer to a neutral, un-personalized view.

## When to use
When you need search results that are *not* shaped by your account history or aggressively logged to your identity — checking how a subject's `name`/`username` appears to a neutral searcher, or simply keeping your investigative queries from feeding your own profile. It returns the underlying engine's results, minus the personalization layer; the intelligence is in those results.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.disconnect.me/ (no login).
2. Choose a provider (e.g. DuckDuckGo) and set language/country if offered; it uses non-identifying first-party cookies to remember these preferences.
3. Search your term and read the results as a less-personalized view.
4. Pivot: profiles, mentions, and documents you find feed people-search, username hunting, and document analysis.

## Inputs → Outputs
- **In:** a `name`/`username`/topic query
- **Out:** the chosen engine's results with reduced personalization (leading to `social-profile`s, mentions)
- **Empty/negative result looks like:** the same sparse results the underlying engine would give — a null here reflects the provider, not a filter; try another provider or a general search.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — reduces personalization/tracking of your search, but **not anonymity**: your IP still reaches the provider. For genuine separation, search over [[tor-browser]] or a sock-puppet browser.
- It relies on third-party providers, so its coverage and freshness are theirs, not Disconnect's.

## Overlaps ("do both")
- Pairs with [[overload-search]] and Tor Browser — Disconnect strips personalization by default, Overload Search adds precise operators and country/language control, Tor adds anonymity; combine by how sensitive the query is.

## Trust & verifiability
`trust: community` — a reputable privacy front end over mainstream engines. Trust the underlying provider's results and verify findings at their source, as with any search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disconnect-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
