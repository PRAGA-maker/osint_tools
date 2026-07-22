---
id: web-search-navigator
name: Web Search Navigator
description: Use when you run high volumes of searches and want keyboard-driven navigation of results across Google, YouTube, GitHub and more — a productivity browser extension.
url: https://github.com/infokiller/web-search-navigator
category: search-engines
path:
- search-engines
bestFor: Speeding up manual search-heavy investigation by adding vim-style keyboard shortcuts to search-result pages.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (MIT).
opsec: passive
opsecNote: A local browser extension that only rebinds keys on result pages — it sends nothing extra to any server and does not change what your searches expose. OpSec is unchanged from browsing normally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source (MIT), actively maintained browser extension with ~950 GitHub stars; a productivity aid rather than a data source, so no data-quality concerns.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- web-search-navigator extension
- infokiller/web-search-navigator
tags:
- productivity
- browser-extension
- search
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Web Search Navigator

> A browser extension that adds configurable keyboard shortcuts to search-result pages — a workflow accelerator, not an intelligence source.

## When to use
Your investigation involves a lot of manual searching and result-triage, and reaching for the mouse constantly slows you down. Web Search Navigator adds vim-style keyboard navigation (j/k to move, numbers to open results, shortcuts to jump between tabs) to Google, YouTube, Startpage, Brave Search, Google Scholar, GitHub, GitLab and Amazon. It finds nothing itself — it just makes you faster at the searching you're already doing.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from your browser's add-on store (Chrome/Firefox/Edge; experimental Safari) or build from the repo.
2. On a supported search-results page, use the keyboard: `j`/`k` to move between results, `Enter`/number keys to open, and the configured keys to page or switch engines.
3. Open the extension options to remap any shortcut; settings sync across devices on the same browser profile.
4. Combine with dorking tools/queries — the extension just makes triaging long result lists quicker.

## Inputs → Outputs
- **In:** none (it enhances pages you're already on)
- **Out:** none (a UI/navigation aid, produces no data)
- **Empty/negative result looks like:** not applicable — it is a productivity tool, not a lookup.

## Gotchas & OpSec
- Purely a convenience layer; it will not find or reveal anything by itself.
- Only affects the supported sites' result pages.
- OpSec: neutral — no extra data leaves your browser.

## Overlaps ("do both")
- Complements search-dorking references and query builders — pair it with those so you can both craft strong queries and triage the results quickly.

## Trust & verifiability
`trust: community` — actively maintained MIT-licensed extension; as a keyboard-navigation aid it introduces no data-quality or sourcing risk.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-search-navigator |
