---
id: socmint
name: SOCMINT (start.me dashboard)
description: Use when you are starting social-media intelligence work and want a curated launchpad — a start.me dashboard linking dozens of SOCMINT tools by platform, yielding routes to `social-profile`s across networks.
url: https://start.me/p/Wp1kpe/socmint
category: social-networks
path:
- social-networks
bestFor: A one-page, categorized directory of social-media-intelligence tools to pick the right platform-specific tool fast.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public start.me page; no account required to view the linked tools (individual linked tools may have their own costs).
opsec: passive
opsecNote: Viewing the dashboard is passive. OpSec risk lives in the tools it links to — assess each linked tool's exposure before use, and route active lookups through a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated start.me board; quality depends on the maintainer and links rot over time — treat it as a signposting index, not a vetted toolset.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SOCMINT start.me
- social media intelligence dashboard
tags:
- tool-collection
- socmint
- social-media
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- cse-utopia
- geoint
- osint-assassin
- start-me
---

# SOCMINT (start.me dashboard)

> A curated start.me launchpad for social-media intelligence — a categorized wall of links to platform-specific search, scraping, and analysis tools.

## When to use
You are beginning SOCMINT on a subject and want to see, at a glance, which tools exist for a given platform (Facebook, Instagram, X/Twitter, TikTok, LinkedIn, Telegram, etc.) rather than recalling them from memory. It's an orientation/index resource: you have a `username`, `name`, or profile `image` and need to pick the right downstream tool to turn it into confirmed `social-profile`s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://start.me/p/Wp1kpe/socmint.
2. Scan the sections by platform/technique; pick the tool that matches your selector and goal.
3. Follow the link to the actual tool and run your lookup there.
4. Because start.me boards accumulate dead links, verify a tool still works before relying on it; fall back to this library's own entry for that tool.
5. Pivot: use the dashboard only to *reach* tools — record findings and pivots against the specific tools you end up using.

## Inputs → Outputs
- **In:** whatever selector your investigation holds (`username`, `name`, `image`) — the board routes you to a matching tool
- **Out:** not a lookup itself; it yields *routes* to tools that produce `social-profile`s and other data
- **Empty/negative result looks like:** links that 404 or tools that have shut down — expected on an aging curated board; move to a maintained index.

## Gotchas & OpSec
- It performs no lookups; it only links out — all data quality and OpSec risk sit with the linked tools.
- Link rot is significant on multi-year start.me boards; cross-check against this library.
- Curation reflects one maintainer's choices and may miss newer tools or include defunct ones.

## Overlaps ("do both")
- Pairs with `[[osint-techniques-tools]]` and other curated indexes — cross-referencing several directories catches tools any single board omits.

## Trust & verifiability
`trust: community` — a user-curated dashboard; useful as a signpost, but verify each destination tool independently before acting on its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socmint |
| category | social-networks |
| selectorsIn → selectorsOut | username, name, image → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
