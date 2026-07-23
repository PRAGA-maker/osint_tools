---
id: osintcombine-tools
name: Osintcombine Tools
description: Use when you want a free, browser-based hub of OSINT pivots and utilities — returns a launcher of search/social/domain/crypto/username tools plus a client-side link-graph visualiser.
url: https://osintcombine.tools/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A one-stop free launcher of common OSINT lookups and a client-side data-visualisation tool.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
status: live
pricing: free
costNote: The web tools here are free and run client-side; OSINT Combine also sells separate professional products, but this tools hub is free to use.
opsec: passive
opsecNote: The hub itself just launches queries/visualises your local data — nothing is processed on OSINT Combine's servers (data stays client-side). Each launched search runs on the destination platform, so your OpSec is really that of the underlying tool (Google, Yandex, a platform search); use a sock puppet/VPN as appropriate for the searches you fire.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by OSINT Combine, a reputable OSINT training/tooling company; the hub is a convenience launcher, so trust in any result rests on the underlying platform it sends you to.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT Combine Tools
- osintcombine.tools
tags:
- Tools collections/toolkits
- launcher
- data-visualisation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Osintcombine Tools

> A free, browser-based hub of OSINT pivots — pre-built search links across engines, social platforms, domains/IP, crypto, and usernames — plus a client-side tool to turn a CSV into a link graph.

## When to use
You want a fast launcher for common lookups without maintaining a bookmark folder, or a lightweight way to visualise relationships in data you already have. Reach for the OSINT Combine tools hub to fire the same `name`/`username`/`domain` query across many platforms (Google/Yandex, Facebook/Twitter/LinkedIn/TikTok/Telegram/Instagram, Reddit/4chan/Pastebin, reverse-IP/WHOIS/geolocation, BTC address/tx, WhatsMyName username search), and use its DataVis tool to draw a network diagram from a local CSV — all client-side.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osintcombine.tools/ and pick a category (search, social, domain/IP, crypto, username, documents).
2. Enter your selector; the hub builds and launches the appropriate query on the destination platform.
3. Work each platform's results as you normally would (the hub just gets you there faster).
4. For relationship mapping, use the DataVis tool: load a local CSV and it renders a network graph in-browser (nothing uploaded).
5. Pivot: promising hits feed dedicated tools; the graph helps you see which entities connect.

## Inputs → Outputs
- **In:** `name`, `username`, `domain` (or a local CSV for DataVis)
- **Out:** launched platform searches surfacing `social-profile`s and mentions; a client-side relationship graph
- **Empty/negative result looks like:** a launched search returns nothing on that platform — that's the platform's answer, not the hub's; and DataVis only reflects the CSV you feed it.

## Gotchas & OpSec
- It's a *launcher/visualiser*, not a data source — results and their reliability belong to the underlying platform each link opens.
- OpSec is per-search: firing a Facebook/LinkedIn search still exposes you to that platform — use sock puppets/VPN for the sensitive ones.
- DataVis is client-side (private), but the launched searches are ordinary web queries.

## Overlaps ("do both")
- Overlaps every tool it links to — its value is speed and breadth of pivots, not depth. Pair its username launcher with a full WhatsMyName run, and its DataVis with a heavier graph tool like `[[linkscope-client]]` for serious link analysis.

## Trust & verifiability
`trust: trusted` — from a reputable OSINT vendor, but as a launcher its trustworthiness is really that of the destination platforms; verify each finding on the source it takes you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintcombine-tools |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, domain → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
