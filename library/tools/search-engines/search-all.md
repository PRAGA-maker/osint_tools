---
id: search-all
name: Search All
description: Use when you have a `name`/`username` selector and want to fire it across many search engines fast — returns the same query re-run on Google, Bing, DuckDuckGo and custom engines from one toolbar.
url: https://chromewebstore.google.com/detail/search-all/kpdkbemdpepjjppbfgeapjienologapa
category: search-engines
path:
- search-engines
bestFor: Rapidly re-running one selector across multiple search engines without retyping.
selectorsIn:
- name
- username
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension; no account or payment.
opsec: passive
opsecNote: The extension only rewrites your search URL locally and collects no data per the developer. But every engine you fan the query out to still logs the search against your IP/browser fingerprint, so run it from a sock-puppet browser profile when querying a live subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Third-party extension (offered by "Screen Recorder"), ~20k users and 4.4★; useful workflow glue, not an authoritative data source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Search All Chrome extension
tags:
- toddington
- curated-directory
- search-engines
- add-ons-apps-extensions
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Search All

> A Chrome toolbar that takes whatever you've highlighted or typed and re-runs it across a stack of search engines with one click.

## When to use
You have a single strong selector — a full `name`, a `username`, a rare handle — and you want to see how it surfaces across Google, Bing, DuckDuckGo, Yandex and any custom engines you've added, without retyping it into each. It's workflow glue for the fan-out phase of a search, not a data source in its own right.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Search All" from the Chrome Web Store (link above) in a dedicated OSINT browser profile.
2. Add the engines you care about in the extension options (it ships with the majors and supports custom search-URL templates — add Yandex images, a username-lookup site, etc.).
3. Highlight text on any page, or type into the extension box, then pick a target engine (or use the right-click context menu) to launch that query.
4. Read the results in each engine's own tab; the extension only routes the query, it doesn't merge or dedupe results.
5. Pivot: promising hits feed a dedicated username tool like [[whatsmyname]] or an image search — Search All just gets you there faster.

## Inputs → Outputs
- **In:** any search string — typically `name` or `username`
- **Out:** none as a selector; it just opens the same query in multiple engines
- **Empty/negative result looks like:** the extension always "works" (it opens tabs); an empty result is each engine returning nothing, which you read per-engine.

## Gotchas & OpSec
- Human-in-the-loop: none for the extension, but each downstream engine may throw its own CAPTCHA/rate limit.
- OpSec: passive locally, but fanning one query across many engines multiplies your footprint — every engine logs it. Use a clean browser profile and, ideally, a sock-puppet IP when the subject could be monitoring.
- It's a convenience layer only; verify anything it surfaces in the primary engine.

## Overlaps ("do both")
- Pairs with dedicated multi-engine metasearch pages — a browser extension re-runs *your* engine list interactively, whereas a metasearch site aggregates results server-side. Use the extension for control, a metasearch for a single merged view.

## Trust & verifiability
`trust: community` — a popular but third-party extension; it moves your query around and adds no data of its own, so trust rests entirely on the engines you point it at.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-all |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
