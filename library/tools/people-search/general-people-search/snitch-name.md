---
id: snitch-name
name: Snitch.name
description: Use when you have a `name` and want candidate social-media profiles across many platforms in one pass — returns social-profile leads (site is degraded/expired-cert).
url: https://snitch.name/
category: people-search
path:
- people-search
- general-people-search
bestFor: One-shot name-to-social-profiles discovery across roughly 40 platforms — when it is up.
selectorsIn:
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free with no account. Reliability is the issue, not cost — the site has an expired SSL certificate and intermittent availability.
opsec: passive
opsecNote: The service queries platforms/search engines on its side, so the target is not directly contacted. Because the SSL cert is expired, your browser will warn and the connection may be unencrypted/tampered — avoid entering anything beyond the target name, use a sock-puppet browser/VPN, and don't trust the transport.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community name-search tool of uncertain upkeep (expired certificate, intermittent uptime); results are unverified leads.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- inteltechniques-people-search-tools
- social-searcher
aliases:
- Snitch
- snitch.name
tags:
- people-search
- social-media
- username-search
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Snitch.name

> A name-to-social-profiles discovery tool that fans a first+last name across ~40 platforms — handy when up, but currently degraded (expired certificate, patchy uptime).

## When to use
You have a person's `name` and want a fast, single-query sweep for candidate profiles across many social networks at once. Snitch.name is a lightweight alternative to running each platform by hand. Treat it as a bonus pass rather than a primary tool: its certificate is expired and availability is intermittent, so it may not load. When it does, it's a quick lead generator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://snitch.name/ (expect a browser TLS warning due to the expired certificate; proceed only in a sock-puppet browser and enter nothing sensitive).
2. Enter the target's first and last name.
3. Run the search; it returns candidate profile links across the platforms it covers.
4. Open each candidate natively to confirm it's the right person (name collisions are common).
5. Pivot: confirmed profiles yield usernames to spread further; corroborate breadth with [[inteltechniques-people-search-tools]] and content with [[social-searcher]].

## Inputs → Outputs
- **In:** `name` (first + last)
- **Out:** candidate `social-profile` links across ~40 platforms
- **Empty/negative result looks like:** the site fails to load (cert/uptime), or returns no candidates — given its degraded state, a blank is often a tool failure, not a real negative; fall back to other tools.

## Gotchas & OpSec
- **Degraded:** expired SSL certificate and intermittent availability — don't rely on it as a sole source; have a fallback ready.
- Name-only matching produces many false positives — always confirm on-platform before attributing.
- OpSec: passive, but the broken TLS means the transport isn't trustworthy; keep input minimal and use a burner browser/VPN.

## Overlaps ("do both")
- Pairs with [[inteltechniques-people-search-tools]] (broader, maintained multi-site launcher) and [[social-searcher]] (content search) — use those as the reliable core and Snitch.name only as a supplementary sweep.

## Trust & verifiability
`trust: unverified` — a community tool of uncertain maintenance (expired cert, flaky uptime). Its output is unverified leads to confirm directly on each platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snitch-name |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
