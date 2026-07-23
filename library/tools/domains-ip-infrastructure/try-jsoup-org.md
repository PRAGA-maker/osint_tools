---
id: try-jsoup-org
name: Try.jsoup.org
description: Use when you have a page's HTML or a `domain`/URL and want to extract specific elements — run CSS-selector queries in a browser sandbox to pull links, emails, and hidden text.
url: http://try.jsoup.org
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Testing CSS-selector/XPath extraction against a page's HTML to pull out links, emails, and structured fields without writing code.
selectorsIn:
- domain
selectorsOut:
- email
- domain
status: live
pricing: free
costNote: Free public demo of the open-source jsoup HTML parser, maintained by jsoup's author; no account.
opsec: passive
opsecNote: If you paste HTML you already have, nothing leaves toward the target. If you use the "fetch from URL" mode, jsoup.org's server retrieves the page — so the request comes from jsoup's IP, not yours, which incidentally shields you from the target's logs (but exposes your target of interest to jsoup.org).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Official interactive demo of jsoup by Jonathan Hedley (its author); a stable, long-running reference tool rather than a data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- try jsoup
- jsoup online parser
tags:
- Domain/IP/Links
- Searchers, scrapers, extractors, parsers
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Try.jsoup.org

> The official online jsoup sandbox — paste HTML (or fetch a URL) and test CSS-selector / XPath queries to carve out exactly the elements you want.

## When to use
You have a page's raw HTML — from view-source, a saved copy, or an archive — and want to **extract structured pieces**: every outbound link, mailto `email` addresses, hidden `<meta>`/comment content, phone numbers in a table, or elements a rendered view hides. Rather than eyeballing source, you write a CSS selector and see exactly what it matches. Handy for quickly pulling contact details and link graphs out of a profile or company page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://try.jsoup.org.
2. Either **paste the HTML** you already have, or enter a URL in "fetch" mode to have the sandbox retrieve it.
3. Enter a CSS query, e.g. `a[href]` (all links), `a[href^=mailto]` (email addresses), `meta`, `img[src]`, or a table-cell path.
4. Read the matched elements in the output pane; adjust the selector to narrow to the fields you need.
5. Pivot: harvested `email`/`domain`/link values feed email-OSINT, WHOIS, and profile-search tools.

## Inputs → Outputs
- **In:** HTML text, or a `domain`/URL to fetch
- **Out:** matched elements — `email` (mailto links), `domain`/links, meta tags, arbitrary text nodes
- **Empty/negative result looks like:** the output pane is empty — your selector matched nothing (wrong path) or the content is loaded by JavaScript and isn't in the static HTML jsoup sees.

## Gotchas & OpSec
- jsoup parses **static HTML only** — anything rendered client-side by JavaScript won't appear; capture the DOM from a real browser first for JS-heavy sites.
- "Fetch from URL" runs server-side on jsoup.org, so the target sees jsoup's IP, not yours — convenient for passive collection, but you're telling jsoup.org what you're looking at.
- It's a demo, not an API — for repeatable extraction, script jsoup (or another parser) locally.

## Overlaps ("do both")
- Complements headless-browser/scraper tooling: use a browser to capture rendered HTML from a JS-heavy page, then paste it here to nail down the exact selectors that isolate the data.

## Trust & verifiability
`trust: community` — the authoritative first-party demo of a mature open-source parser; it transforms HTML you supply and adds no external data, so results are deterministic and verifiable against the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | try-jsoup-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
