---
id: inteltechniques-tools-search-engines-suite
name: IntelTechniques Tools (search engines suite)
description: Use when you have almost any selector (name, email, username, phone, image, domain, location) and want pre-built query interfaces that fan it across dozens of sources — returns links/results to social-profile, address, email and more.
url: https://inteltechniques.com/tools/index.html
category: search-engines
path:
- search-engines
bestFor: A canonical, free one-stop set of search interfaces covering nearly every selector — the standard starting point for person-finding.
selectorsIn:
- name
- email
- username
- phone
- image
- geolocation
- domain
- address
selectorsOut:
- social-profile
- address
- email
status: degraded
pricing: free
costNote: Free hosted tools by Michael Bazzell. No account. Some individual modules break over time as target platforms change their query formats.
opsec: passive
opsecNote: The pages build query URLs against third-party sites and open them in your browser — the actual searches hit those destinations, so your browser/IP is what reaches them, not IntelTechniques. Use a sock-puppet browser. Nothing is submitted to Bazzell's server beyond loading the tool page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michael Bazzell (IntelTechniques), a foundational and widely-cited figure in OSINT. The tooling is authoritative and regularly referenced in training.
missingPersonsRelevance: high
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- sherlock
- account-live-com
aliases:
- inteltechniques.com/tools
- Bazzell tools
tags:
- search
- bazzell
- suite
- pivot-hub
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# IntelTechniques Tools (search engines suite)

> Michael Bazzell's free suite of pre-built search interfaces — feed it a selector and it constructs the right queries across dozens of sites. The classic OSINT jumping-off point.

## When to use
You have a selector and want to blast it across many sources quickly without hand-writing each query. The suite has dedicated tabs for `name`, `email`, `username`, `phone`, `image` (reverse search), `domain`, `geolocation`/maps, business, and more — each generating ready-made searches against the relevant platforms. It's the efficient first sweep before you narrow to specialist tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inteltechniques.com/tools/index.html in a sock-puppet browser.
2. Pick the tab matching your selector (e.g. **Email**, **Username**, **Telephone**, **Images**).
3. Enter the value and either run individual searches or the "submit all" style options; results open against the destination sites.
4. Triage the hits, then pivot to specialists — e.g. `[[sherlock]]` for exhaustive username enumeration, `[[account-live-com]]` for email-existence checks.

## Inputs → Outputs
- **In:** `name` / `email` / `username` / `phone` / `image` / `domain` / `geolocation` / `address`
- **Out:** `social-profile`, `address`, `email` and other links surfaced from the many queried sources
- **Empty/negative result looks like:** a specific module returns nothing or errors — often because the target site changed its URL/query scheme and that tab is temporarily broken; try another module or the site directly.

## Gotchas & OpSec
- Human-in-the-loop: none, but some modules are stale — Bazzell updates them, yet platform changes routinely break individual tabs.
- OpSec: **passive** — searches go from *your* browser to the destination sites; sock-puppet it. IntelTechniques itself only serves the tool page.
- **Degraded** only in the sense that not every module works at any given time; the suite as a whole is very much alive.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` (deeper username coverage) and `[[account-live-com]]` (email existence) — the suite gives breadth-first fan-out, those give depth on a single selector.

## Trust & verifiability
`trust: trusted` — authored and maintained by Michael Bazzell, a canonical OSINT authority. The tool only assembles queries; the trustworthiness of each *result* still depends on the destination source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inteltechniques-tools-search-engines-suite |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, username, phone, image, geolocation, domain, address → social-profile, address, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
