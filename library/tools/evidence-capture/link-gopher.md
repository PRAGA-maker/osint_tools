---
id: link-gopher
name: Link Gopher
description: Use when you have a page open and want every link and unique domain on it extracted at once — returns a de-duplicated list of URLs and domains.
url: https://sites.google.com/site/linkgopher/
category: evidence-capture
path:
- evidence-capture
bestFor: One-click extraction of all links (and all unique domains) from the current web page.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free browser extension on Firefox Add-ons and the Chrome Web Store; no account, no payment.
opsec: passive
opsecNote: Link Gopher only reads links already present in the page your browser has loaded — it makes no new requests, so it adds no footprint beyond your normal visit. (Loading the page in the first place is the visit the target may log; the extraction itself is inert.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Simple, long-standing, single-purpose extension. It only parses the loaded DOM, so risk is minimal; output completeness depends on the page being fully rendered/scrolled first.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- LinkGopher
tags:
- link-extraction
- evidence-capture
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Link Gopher

> A one-click browser extension that pulls every link (and every unique domain) out of the page you're viewing, de-duplicates them, and dumps the list in a new tab to copy.

## When to use
You're on a page dense with links — a directory, a profile's link section, a forum thread, search results, a sitemap — and you want all of them, or just the unique domains, without hand-copying. Fast for harvesting outbound links to feed into further enumeration, or for extracting the set of domains a page references.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Link Gopher from Firefox Add-ons or the Chrome Web Store.
2. Load the target page and fully render it — scroll to trigger lazy-loaded content, expand sections — since it only sees what's in the DOM.
3. Click the Link Gopher icon → "Extract All Links" (every URL, embedded ones included) or "Extract All Domains" (unique domains only). Results open in a new tab, sorted and de-duplicated.
4. Copy the list into your notes or a script for the next step.
5. Pivot: extracted domains feed WHOIS/subdomain tooling; extracted URLs feed archiving (`[[single-file]]`) or a scraper.

## Inputs → Outputs
- **In:** the currently loaded page (its links / `domain`s)
- **Out:** a de-duplicated, sorted list of all URLs, or all unique `domain`s
- **Empty/negative result looks like:** few or no links returned — usually because the page renders links via JavaScript that hasn't run/loaded yet; re-render/scroll and re-extract.

## Gotchas & OpSec
- It only captures links present in the DOM at extraction time — infinite-scroll or click-to-load content must be loaded first, or you'll miss links.
- No crawling: it does the current page only, not linked pages.
- OpSec: **passive** — no new network requests; the only exposure is your having loaded the page normally.

## Overlaps ("do both")
- Pairs with `[[single-file]]` — Link Gopher lists what a page points to; SingleFile preserves the page itself. Extract links, then archive the ones that matter.

## Trust & verifiability
`trust: community` — a simple, well-established utility that just parses the loaded page. Reliable for what's actually in the DOM; completeness is on you (render fully before extracting).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | link-gopher |
| category | evidence-capture |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
