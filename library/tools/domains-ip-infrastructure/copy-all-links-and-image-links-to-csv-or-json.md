---
id: copy-all-links-and-image-links-to-csv-or-json
name: Copy All Links and Image Links to CSV or JSON
description: Use when you have a web page and want to extract every hyperlink and image URL on it as structured CSV/JSON in one click — returns domains and image links to pivot from.
url: https://chrome.google.com/webstore/detail/copy-all-links-and-image/ccddopnnikeeoogpfbnfommfoeliaidg/related
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-click export of all links and image URLs on a page to CSV/JSON for analysis.
selectorsIn:
- domain
selectorsOut:
- domain
- image
status: live
pricing: free
costNote: Free Chrome extension; no account required.
opsec: passive
opsecNote: Extraction runs locally in your browser against the page already loaded — it sends nothing to the page's server beyond your normal page view. Loading the page itself is the only server-visible action, so use a sock-puppet browser for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A third-party productivity extension that parses the current page's DOM; vet its permissions before installing, but it introduces no external data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Copy All Links extension
tags:
- Domain/IP/Links
- Source Code Analyzes
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Copy All Links and Image Links to CSV or JSON

> A right-click browser extension that dumps every link and image URL on the current page into structured CSV/JSON — turning a page into a link/asset inventory.

## When to use
You're analysing a website/profile page and want a machine-readable list of everything it links to and every image it embeds — outbound domains, linked social profiles, CDN/image hosts, document URLs. Instead of hand-scraping, this extension exports the lot to CSV/JSON so you can pivot on the `domain`s and pull the `image` URLs for reverse search.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension into a sock-puppet browser profile.
2. Navigate to the target page (a bio, a company page, a forum profile).
3. Trigger the extension to export all hyperlinks and image links to CSV or JSON.
4. Sort/filter the export: outbound domains → infrastructure/ownership pivots; image URLs → reverse-image search.
5. Pivot: linked social profiles feed username tooling; linked domains feed WHOIS/DNS OSINT; images feed face/photo search.

## Inputs → Outputs
- **In:** a loaded web page (its `domain`/content)
- **Out:** structured list of all link `domain`s and `image` URLs on the page
- **Empty/negative result looks like:** few/no links on a heavily-scripted SPA where content loads dynamically — scroll/interact to load content first, or use a full crawler.

## Gotchas & OpSec
- It reads only what's currently in the page DOM — dynamically-loaded content must be triggered to appear first.
- Third-party extension: check permissions and prefer a disposable profile.
- No crawling depth: it captures one page at a time, not a whole site.

## Overlaps ("do both")
- Pairs with a proper crawler/spider for whole-site coverage, and with reverse-image search for the image URLs it extracts.

## Trust & verifiability
`trust: community` — it only restructures data already on the page you loaded, so there's no external accuracy risk; just confirm the extension's publisher/permissions before installing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | copy-all-links-and-image-links-to-csv-or-json |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
