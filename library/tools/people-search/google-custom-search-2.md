---
id: google-custom-search-2
name: Google Custom Search
description: Use when you have a `name`/`username`/`email` and want to search a curated slice of the web (a pre-built Custom Search Engine) rather than all of Google — returns social-profile, address, associate leads.
url: https://cse.google.com/cse?cx=017648920863780530960:lddgpbzqgoi
category: people-search
path:
- people-search
bestFor: Running a name/handle query against a pre-scoped Google Custom Search Engine for people-search.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- address
- associate
status: degraded
pricing: free
costNote: Free to use in the browser. It is a hosted Google Custom Search Engine (CSE); Google's programmatic CSE API has a free daily quota then charges, but the web widget here is free.
opsec: passive
opsecNote: Queries go to Google over the CSE, not to the subject — passive. Google logs the search against your IP/account like any Google query; use a sock-puppet browser and stay logged out for less attribution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The engine is Google's, but the *scope* (which sites it searches) is defined by an unknown third party via the `cx` config, and CSE configs silently rot as included sites change — so relevance and coverage are unverifiable and drift over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google CSE people search
tags:
- search-engine
- google-cse
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Google Custom Search

> A pre-built Google Custom Search Engine (CSE) that scopes Google to a curated set of people-search sources — a sharper first pass than a raw Google query when the config is still good.

## When to use
You have a `name`, `username`, or `email` and want to search only across a hand-picked set of people-search/records sites instead of the whole web. A CSE trades breadth for signal: fewer, more on-topic hits than a plain Google search — provided the underlying site list (the `cx` config) hasn't gone stale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (https://cse.google.com/cse?cx=017648920863780530960:lddgpbzqgoi) in a clean/sock-puppet browser.
2. Enter the selector — a full `name` in quotes, a `username`, or an `email` — and run it.
3. Read results as ordinary Google hits, but restricted to the sites baked into this CSE.
4. Refine with standard Google operators (quotes for exact name, `site:` if the CSE allows it, add a city to disambiguate).
5. Pivot: open promising `social-profile`/records hits directly, and re-run the same selector in a broad engine to catch what the narrow scope missed.

## Inputs → Outputs
- **In:** `name`, `username`, or `email`
- **Out:** `social-profile`, `address`, `associate` leads (whatever the scoped sites index)
- **Empty/negative result looks like:** zero results or clearly off-topic hits — often a sign the CSE's included sites have changed/died rather than a true negative; re-run in general Google before concluding.

## Gotchas & OpSec
- CSE configs decay: the `cx` owner may change or lose the included sites, so coverage is unverifiable and drifts — treat "no results" with suspicion.
- It only searches its configured scope; always back it up with a full-web search.
- OpSec: passive; still a Google query tied to your session — stay logged out.

## Overlaps ("do both")
- Pairs with a plain Google/Bing dork and with [[images-search-engine]] (its image-scoped sibling CSE) — run narrow and broad, then reconcile.

## Trust & verifiability
`trust: community` — Google runs the engine, but an unknown third party defines and maintains the scope; the results are only as trustworthy and current as that opaque `cx` config.
