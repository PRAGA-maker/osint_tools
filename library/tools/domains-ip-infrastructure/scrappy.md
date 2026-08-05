---
id: scrappy
name: Scrappy
description: Use when you have a web page/domain and want to point-and-click scrape structured data (links, text, tables) from it into a usable format fast — returns extracted page data to pivot from.
url: https://chrome.google.com/webstore/detail/scrappy/bcphfcbaecjifhiojhejdiogpanlmadm/related
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast, easy point-and-click web scraping of a page's structured content from the browser.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Chrome extension; no account required.
opsec: passive
opsecNote: Scraping runs in your browser against pages you load, so the only server-visible action is your normal page view — passive. For sensitive targets, load pages through a sock-puppet browser; rapid multi-page scraping can still trip rate limits/anti-bot and stand out, so pace it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A third-party scraping extension; it introduces no external data source (it reads the page you're on), but vet its permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Scrappy scraper
tags:
- web-scraping
- Domain/IP/Links
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Scrappy

> A beginner-friendly, fast point-and-click web scraper as a browser extension — grab structured data off a page without writing code.

## When to use
When a page holds data you want in bulk — a directory listing, a table of members, search results, a profile's link list — and hand-copying is impractical. Scrappy lets you select the elements you want and extracts them into structured output, so you can quickly turn a `domain`/page into a dataset of `domain`s, names, or links to pivot on.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Scrappy into a sock-puppet browser profile.
2. Load the target page (fully — scroll/paginate so all content renders).
3. Use its point-and-click selector to mark the fields you want (links, text, table cells).
4. Extract and export the structured data.
5. Pivot: extracted domains → infrastructure OSINT; names/usernames → people/username tools; links → reverse-image or further scraping.

## Inputs → Outputs
- **In:** a loaded web page (its `domain`/content)
- **Out:** structured extracted data (links/`domain`s, text, tables)
- **Empty/negative result looks like:** nothing captured — usually content loaded dynamically after your selection, or the elements weren't selected consistently; re-render and reselect.

## Gotchas & OpSec
- Reads the current DOM only — trigger dynamic/lazy content to load before scraping.
- Fast multi-page scraping can hit rate limits or anti-bot defences and looks conspicuous; pace requests and respect ToS.
- Third-party extension: check permissions and keep it in a disposable profile.

## Overlaps ("do both")
- Overlaps `[[copy-all-links-and-image-links-to-csv-or-json]]` (link/image dumps) but adds selective field extraction; for whole-site or scheduled scraping, step up to a dedicated crawler.

## Trust & verifiability
`trust: community` — it restructures data already on the page you loaded, so there's no external accuracy risk; verify the extension's publisher/permissions before installing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scrappy |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
