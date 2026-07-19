---
id: context-menu-search
name: Context Menu Search
description: Use when you want to right-click any selected `name`/`username` and search it in a chosen engine — a Chrome extension that adds multi-engine search to the context menu.
url: https://chromewebstore.google.com/detail/context-menu-search/ocpcmghnefmdhljkoiapafejjohldoga
category: search-engines
path:
- search-engines
bestFor: Right-click searching selected text across many configurable engines from the context menu.
selectorsIn:
- name
- username
selectorsOut: []
status: live
pricing: freemium
costNote: Free core (add up to ~40 engines); an optional paid tier adds AI prompts, sub-menus and multi-launch. No account for the free features.
opsec: passive
opsecNote: The extension only builds context-menu links to search engines locally; the searches themselves run on whichever engine you pick and are logged there against your IP/fingerprint. Run it in a dedicated sock-puppet browser profile when investigating a live subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular third-party extension (~90k users, 4.5★, no violation history); workflow glue that adds no data of its own.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- search-all
aliases:
- Context Menu Search extension
tags:
- search
- add-ons-apps-extensions
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Context Menu Search

> A right-click accelerator: highlight a selector on any page and search it in your chosen engine (or several) straight from the context menu.

## When to use
You're reading a page and hit a `name`, `username`, address or handle you want to pursue — Context Menu Search lets you select it and launch a search in any engine you've configured without copy-pasting into a new tab. It's fan-out workflow glue for the investigation, not a data source.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Context Menu Search" from the Chrome Web Store into your OSINT browser profile.
2. In options, add the engines you want (web search, image search, a username-lookup site, a records site — up to ~40, including custom URL templates).
3. On any page, highlight the text, right-click, and pick the engine to search it in (open in a focused or background tab).
4. Reorder engines by drag-and-drop so your most-used ones are on top.
5. Pivot: launch a selected `username` straight into a username tool like [[whatsmyname]], or a `name` into people-search — the extension just removes the copy-paste step.

## Inputs → Outputs
- **In:** any selected text — typically `name` or `username`
- **Out:** none as a selector; it opens your query in the chosen engine(s)
- **Empty/negative result looks like:** the extension always launches the search; an empty result is the target engine returning nothing, read per-engine.

## Gotchas & OpSec
- Convenience layer only — verify anything it surfaces in the underlying engine.
- The free tier covers core multi-engine search; AI/sub-menu extras are paywalled but not needed for OSINT.
- OpSec: passive locally, but each engine logs the search against your fingerprint — use a sock-puppet profile.

## Overlaps ("do both")
- Pairs with [[search-all]] — both fan a selection across engines; Context Menu Search works from the right-click menu, Search All from a toolbar box. Pick whichever fits your flow; you don't need both.

## Trust & verifiability
`trust: community` — a widely-used third-party extension that only routes queries and adds no data; trust rests on the engines you point it at.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | context-menu-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
