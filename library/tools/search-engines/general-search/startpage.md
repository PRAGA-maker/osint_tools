---
id: startpage
name: Startpage
description: Use when you have a `name`/`username`/keyword and want Google-quality results without a personal search footprint — returns web results anonymously, with an "Anonymous View" proxy for opening pages.
url: https://www.startpage.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: Running Google-sourced searches privately, and opening result pages through an anonymizing proxy.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free; supported by privacy-respecting ads, no account required.
opsec: passive
opsecNote: Startpage proxies your query to Google and strips trackers, so Google sees Startpage's servers rather than your IP, and results carry no personalized-profile bias. "Anonymous View" opens a result page through Startpage's proxy so the destination site sees Startpage, not you. Still combine with Tor/VPN for high-sensitivity work — Startpage the operator receives your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established Netherlands-based private search engine (EU privacy jurisdiction) that resells Google results; long-standing reputation, though it relies on Google's index.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- searx
aliases:
- StartPage
- startpage.com
- Ixquick
tags:
- search-engines
- general-search
- privacy
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Startpage

> Google's results without Google watching you: Startpage proxies your queries to Google, strips the tracking, and can open any result page through an anonymizing "Anonymous View" proxy.

## When to use
You want the coverage of Google's index for a `name`, `username`, address fragment, or phrase, but without your own IP, cookies, or a logged-in Google profile shaping (or logging) the search. It's the go-to when you need un-personalized, un-attributed Google results, and when you want to peek at a result page without your real browser touching the target's server.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.startpage.com/ and run your query; Google operators (`site:`, `"exact phrase"`, `-exclude`, `filetype:`) are forwarded, so power-search as you would on Google.
2. Read the aggregated results — because they aren't personalized, ranking reflects the query, not your history.
3. To visit a hit without exposing yourself, click **Anonymous View** next to a result to load it through Startpage's proxy.
4. Pivot: promising `domain`s and `social-profile` links feed selector-specific tools; re-run the same query on a second engine to catch what Google buries.

## Inputs → Outputs
- **In:** `name`, `username`, or keywords (with Google operators)
- **Out:** anonymized web result links — candidate `social-profile`s, `domain`s, documents
- **Empty/negative result looks like:** few/no results or a rate-limit prompt — Startpage occasionally throttles heavy querying; wait or vary the query rather than assuming the web has nothing.

## Gotchas & OpSec
- Human-in-the-loop: none normally; sustained rapid queries can trigger an anti-abuse challenge.
- OpSec: passive and shielded from the destination (especially via Anonymous View), but the Startpage operator still sees your queries — layer Tor/VPN for sensitive subjects.
- It mirrors Google's index, so it inherits Google's blind spots; it is not a second independent index.

## Overlaps ("do both")
- Pairs with `[[searx]]` — Startpage anonymizes Google specifically, while SearX aggregates many engines at once; run both so a Google-only blind spot doesn't hide a result.

## Trust & verifiability
`trust: trusted` — Startpage is a long-established EU-based private search engine with a solid privacy record; results are genuine Google results served anonymously, so trust the coverage while remembering it's Google's index underneath.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | startpage |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
