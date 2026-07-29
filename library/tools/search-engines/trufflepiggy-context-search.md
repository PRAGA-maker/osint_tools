---
id: trufflepiggy-context-search
name: Trufflepiggy (Context Search)
description: Use when you have selected `image` or text on a page and want to fan a lookup out across many search engines/OSINT sites at once — returns `social-profile`, `image` matches, and site hits from a right-click menu.
url: https://chromewebstore.google.com/detail/trufflepiggy-context-sear/chffnhocnckigoapjdienmaphjnljpmo
category: search-engines
path:
- search-engines
bestFor: Right-click multi-engine and reverse-image searches on selected text or images without retyping into each site.
selectorsIn:
- image
- name
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free Chrome/Chromium extension; no account or payment required.
opsec: active
opsecNote: Each launched search sends the selected text/image to whatever third-party engines you configured, from your browser session. Run it in a sock-puppet browser profile so queries about a target are not tied to your real accounts or cookies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Independent extension (~1k users, 4.5-star/22 ratings) migrated to Manifest V3 and updated May 2025; it only automates opening searches, it stores no target data itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Context Search
- Trufflepiggy
tags:
- Universal search tools
- reverse-image-search
- browser-extension
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Trufflepiggy (Context Search)

> A configurable browser context-menu that blasts selected text or an image to a whole panel of search engines and OSINT sites in one click.

## When to use
You are reading a page and hit a selector worth pivoting on — a `name`, `username`, phrase, or an `image`. Instead of copy-pasting it into ten sites one at a time, you highlight/right-click and Context Search opens the query across every engine you have configured (general search, social sites, reverse-image services). It is a speed multiplier for the manual pivot stage of an investigation.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store into a Chromium browser (Chrome, Brave, Edge) — ideally a dedicated investigation profile.
2. Open the extension options and add the search targets you care about: Google/Bing, social platforms, username-checkers, and reverse-image engines. Group them so you can fire a whole group at once.
3. On any page, select text (a `name` or `username`) — or right-click an `image` — then choose Context Search → your engine/group from the menu.
4. Read the results: each configured engine opens in its own tab. Reverse-image lookups return visually similar `image`s and pages; text lookups return `social-profile`s and site hits.
5. Pivot: promising profiles/images feed dedicated tools for confirmation.

## Inputs → Outputs
- **In:** selected `image`, `name`, or `username` on a web page
- **Out:** parallel tabs of `social-profile` hits and reverse-`image` matches from your configured engines
- **Empty/negative result looks like:** the tabs open but each engine returns no relevant hits — the selector is either too common or absent from those indexes; it is not evidence of anything.

## Gotchas & OpSec
- Human-in-the-loop: none for launching, but you still read and judge each engine's results manually.
- OpSec: this is **active** — every launched query leaves your browser toward third parties carrying whatever you selected. Use a sock-puppet profile with no logged-in personal accounts.
- The tool only *routes* queries; result quality is entirely down to the engines you configure. Curate your engine list for the case type.
- Browser-only: there is no CLI or API, so it does not fit automated pipelines.

## Overlaps ("do both")
- Complements dedicated reverse-image and username tools rather than replacing them: use Context Search to fan out quickly, then take the strongest hit into a purpose-built verifier. It is the launcher, not the analyzer.

## Trust & verifiability
`trust: community` — a small but maintained third-party extension that merely opens searches; it neither stores nor brokers target data, so the trust question is really about the downstream engines you point it at.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trufflepiggy-context-search |
| category | search-engines |
| selectorsIn → selectorsOut | image, name, username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
