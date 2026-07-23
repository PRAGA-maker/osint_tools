---
id: forager
name: Foragear QuickSearch
description: Use when you're scanning many search results and want relevant sections auto-highlighted and jumped to — a Chrome extension that speeds reading Google results, not a data source.
url: https://chrome.google.com/webstore/detail/foragear-quicksearch-%20too/cldhjjcfiadipgdiiklpdhdkkakacdbm
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Speeding up manual triage of Google search results via inline keyword highlighting and autoscroll.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension (optional PayPal tip). Installed from the Chrome Web Store; a small independent project.
opsec: passive
opsecNote: A browser productivity add-on that highlights text in pages you already open — it doesn't query targets. As with any extension, it can read page content, so install only from the official Web Store and don't run it while handling highly sensitive material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A small third-party Chrome extension (low install count) that only enhances result reading; verify its Web Store listing and permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Forager
- Foragear Quick Search Tool
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- browser-extension
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Foragear QuickSearch

> Reading aid for search results: it highlights the relevant keywords on a clicked page and scrolls you straight to them — shaving time off manual result triage.

## When to use
You're working through long lists of Google results and each page is a slog to skim for the bit that matched. Foragear adds clickable icons beside results, opens pages in new tabs, highlights the search phrase (pink) and related keywords (yellow), and autoscrolls to the first hit. It's a small efficiency tool for the manual-search grind — it does not find or enrich data, it just makes reading what you already found faster.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Foragear QuickSearch Tool" from the Chrome Web Store (verify the listing/permissions first).
2. Run a normal Google search — the extension adds icons next to results.
3. Click a result's icon to open it in a new tab with keywords highlighted and the page auto-scrolled to the first match.
4. Use the extension popup to clear highlights when done.
5. Pivot: nothing to pivot — it accelerates review; the leads come from your search itself.

## Inputs → Outputs
- **In:** none (no selector — it acts on your existing Google searches)
- **Out:** faster manual triage — highlighted, auto-scrolled result pages
- **Empty/negative result looks like:** nothing highlighted — the keywords don't literally appear on the page (synonyms/paraphrase), or the extension didn't inject; it's a convenience layer, so "no highlight" just means read manually.

## Gotchas & OpSec
- It's a reading aid, not an OSINT lookup — it surfaces no new data.
- Small, low-install extension: review its permissions (it can read page content) and install only from the official Web Store.
- Highlighting is literal-string based, so paraphrased matches won't light up.
- OpSec: passive; be mindful that any content extension can read the pages you open.

## Overlaps ("do both")
- Complements search engines and dorking tools — those generate the result set; Foragear just helps you read through it faster.

## Trust & verifiability
`trust: unverified` — a minor third-party browser extension with few installs; it only enhances result reading, so the main due-diligence is checking its Web Store permissions before installing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forager |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
