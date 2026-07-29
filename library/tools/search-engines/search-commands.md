---
id: search-commands
name: Search Commands
description: Use when you want faster address-bar searching — a Chrome extension that adds command shortcuts (incognito/new tab/new window) to your browser search box.
url: https://chrome.google.com/webstore/detail/search-commands/ggjakfijchdkbmmhbfemjciidhnipgoe/related
category: search-engines
path:
- search-engines
bestFor: Speeding up repetitive searching from the address bar, e.g. firing a query straight into an incognito window during OSINT work.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension; no account. Requires a Chromium-based browser.
opsec: passive
opsecNote: The extension reads what you type in the address bar and your browsing/history to power its commands — a real permission footprint, so install it only in a compartmentalized investigation profile, not your personal one. Its "incognito" command is a convenience, NOT anonymity: incognito hides local history only, not your IP from the sites you visit — still use a VPN/sock-puppet for target-facing searches.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension (searchcommands.net) with a solid user base and rating; the developer states data isn't sold, but it's an unaudited extension with address-bar/history access — review permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Search Commands extension
tags:
- Tools for Google
- browser-extension
- productivity
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Search Commands

> A Chrome extension that turns the address bar into a quick-command tool — type a query, add a comma, and pick incognito / new tab / new window. A workflow accelerator, not a data source.

## When to use
A minor productivity helper for OSINT browsing. When you run many searches and repeatedly want each one in a fresh incognito window or new tab (to keep sessions clean), Search Commands lets you fire the query and choose the mode inline from the address bar instead of clicking around. Reach for it to shave friction off repetitive searching; it surfaces no subject data itself.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install it into a **compartmentalized** investigation browser profile (review its permissions first).
2. Type your query in the address bar, then a comma to open the command dropdown.
3. Choose Incognito, New Tab, or New Window to run the search that way.
4. Use "New Window/Incognito" to keep each search session isolated — but remember incognito ≠ anonymous (see OpSec).
5. Pair with a VPN/sock-puppet setup for any target-facing search.

## Inputs → Outputs
- **In:** a search query typed in the address bar (not a subject selector)
- **Out:** the search executed in your chosen browser mode — no derived data
- **Empty/negative result looks like:** N/A — it's a launcher; if the dropdown doesn't appear, check the extension is enabled and the comma trigger is configured.

## Gotchas & OpSec
- **Incognito is not anonymity** — it clears local history only; sites still see your IP. Use a VPN/sock-puppet for real separation.
- The extension has address-bar and history access — keep it in an investigation-only profile and audit permissions.
- Purely a convenience; it adds no search coverage, only speed.

## Overlaps ("do both")
- Complements dorking/search tools and OpSec browser-profile hygiene — it just speeds how you launch searches; it doesn't change what you can find.

## Trust & verifiability
`trust: unverified` — a popular but unaudited third-party extension with sensitive permissions; the developer's no-sale claim aside, treat it as a convenience tool to isolate in a dedicated profile, not a vetted security component.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-commands |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
