---
id: xgs
name: XGS
description: Use when you have a search term/dork and want to run it against Google (and legacy .onion gateways) from a Python CLI — returns domain/link results.
url: https://github.com/XAMFRA/XGS
category: search-engines
path:
- search-engines
bestFor: Scripting Google Hacking Database (dork) searches, plus a legacy .onion dork mode.
selectorsIn: []
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free/open-source Python script; no account or key.
opsec: passive
opsecNote: Passive toward any subject, but automated Google querying from your own IP is quickly flagged — Google will serve CAPTCHAs or block the IP after a few requests. Use a research IP and low volume.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: unverified
trustNote: Small single-author GitHub script; its .onion dork feature relies on Tor2web gateways (onion.cab/onion.city) that are largely defunct, so only the Google-dork path is reliably useful.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- XAMFRA/XGS
tags:
- Tools for Google
- google-dork
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# XGS

> A small Python CLI for running Google Hacking Database dork searches, with an (aging) mode for dorking .onion sites via web gateways.

## When to use
You want to run canned Google dork queries from the command line rather than the browser — for example to sweep for exposed documents, indexes, or a subject's footprint across indexed sites — and you like having a menu of Google Hacking Database patterns to hand. The tool also advertises a `.onion` dork mode, but that path depends on Tor2web gateways (onion.cab, onion.city) that have mostly shut down, so treat the onion feature as broken and lean on the Google-dork side.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and run `python XGS.py` (Python 3).
2. Pick a mode from the menu: Google Hacking Database dorks or the (legacy) .onion dork search.
3. Enter your keyword/dork and page through results; the tool assembles the dork query and returns the matching links.
4. Because it drives Google directly, expect a CAPTCHA/soft-block after a handful of automated queries — solve it in a browser or slow down.
5. Pivot: indexed `domain`/links that surface feed further manual review; treat any onion-gateway result as unverified.

## Inputs → Outputs
- **In:** a keyword or dork (no structured OSINT selector required)
- **Out:** `domain` / link results from the Google index
- **Empty/negative result looks like:** a CAPTCHA page or zero results — with Google scraping this usually means you were rate-limited, not that nothing exists. The .onion mode typically returns nothing now because the gateways it queries are dead.

## Gotchas & OpSec
- Human-in-the-loop: automated Google queries trigger CAPTCHAs/blocks (`captcha`); manual dorking in a browser is often more reliable.
- OpSec: passive, but your IP is doing the searching — throttle and use a research IP.
- Status is **degraded**: the onion-gateway feature is effectively obsolete; only the Google-dork functionality is dependable.

## Overlaps ("do both")
- For the same dorks without the scraping fragility, run the queries manually in Google, or use a maintained dork/search resource in this category; XGS is a convenience wrapper, not a unique data source.

## Trust & verifiability
`trust: unverified` — a single-author script with a partly-defunct feature set; verify anything it returns directly in a browser, and don't rely on its .onion mode.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xgs |
| category | search-engines |
| selectorsIn → selectorsOut | — → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (captcha) |
