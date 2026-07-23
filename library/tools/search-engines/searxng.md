---
id: searxng
name: SearXNG
description: Use when you have a `name`, `username` or `email` and want to sweep many search engines at once without being profiled — returns aggregated links, `social-profile`s and `domain`s from a privacy-preserving metasearch.
url: https://searxng.org/
category: search-engines
path:
- search-engines
bestFor: Privacy-preserving metasearch that aggregates ~200 engines into one query without logging or profiling you.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free and open source (AGPL). Use a hosted public instance (list at searx.space) or self-host via Docker at no cost.
opsec: passive
opsecNote: A strong OpSec choice — no cookies/profiling, results can be proxied, and it works over Tor, so your search terms aren't tied to a personal Google/Bing profile. On a public instance the operator can still see your queries; self-host or pick a trusted instance for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Mature, widely-used open-source project (AGPL); self-hostable and auditable. Result quality depends on which upstream engines a given instance enables.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SearX-NG
- searxng.org
tags:
- meta-search
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# SearXNG

> A privacy-first metasearch engine that queries ~200 search services at once and returns merged results with no tracking — the OpSec-friendly way to Google someone.

## When to use
You have a `name`, `username`, `email` or other string and want broad web coverage in one shot, without your searches being logged against a personal account or shaping (and being shaped by) a filter bubble. Aggregating many engines surfaces hits that any single engine buries or omits, and doing it privately keeps the investigation off your own Google history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Pick a public instance from https://searx.space (or run your own via Docker for full privacy).
2. Enter the `name`/`username`/`email`/quoted phrase; use quotes and engine bang-syntax (`!gh`, `!ddg`) to target specific sources.
3. Read the merged result list — each hit shows which upstream engine returned it.
4. Optionally view results through the instance's proxy so the destination site sees the instance, not you.
5. Pivot: profile links feed username enumeration; a distinctive domain feeds infra tooling; a leaked-email hit feeds breach/account tooling.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or any query string
- **Out:** aggregated result links → `social-profile`s, `domain`s, documents mentioning the subject
- **Empty/negative result looks like:** few or no results — often an instance with several engines rate-limited/disabled rather than a truly empty web. Retry on a different instance before concluding nothing exists.

## Gotchas & OpSec
- Instances vary: some have engines disabled, throttled, or returning CAPTCHAs upstream, so coverage differs instance to instance. Try two or three.
- On a public instance the operator sees your queries — self-host or use a reputable instance for sensitive targets.
- OpSec: passive and privacy-preserving — no personal profiling, Tor-capable, proxied result viewing available.

## Overlaps ("do both")
- Pairs with direct engine use and dedicated username/people tools — SearXNG gives broad, private coverage in one pass, then you drill into the specific hits with a focused tool.

## Trust & verifiability
`trust: community` — a well-established open-source (AGPL) project you can self-host and audit; the engine itself is trustworthy, though each public instance's result quality depends on its operator's configuration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searxng |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
