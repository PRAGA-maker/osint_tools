---
id: torry-io
name: Torry
description: Use when you have a keyword, `username`, or onion `domain` and want to search Tor/dark-web content from a normal browser — returns onion links viewable anonymously.
url: https://www.torry.io/
category: dark-web
path:
- dark-web
bestFor: Searching dark-web/onion content without running Tor Browser, then opening results through Tor anonymously.
selectorsIn:
- username
- email
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free web search plus free browser extensions/apps; no account required for basic searching.
opsec: passive
opsecNote: Torry proxies Tor access, so your clearnet IP isn't directly touching onion services, and it states searches are stripped of IP/metadata and not logged — but you are trusting a third party's claims. For serious work don't rely on it for anonymity; use a hardened Tor Browser in a VM. Never enter real credentials.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party service that brokers Tor access with strong no-log privacy claims that cannot be independently verified; convenient, but not an audited anonymity system.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- browseriling
- tor-browser
aliases:
- torry.io
- Torry search
tags:
- darkweb
- Dark Web Links
- onion-search
source: uk-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Torry

> A dark-web search engine and Tor gateway you can drive from a regular browser — search onion content, then open results through Tor's "anonymous view" without installing Tor Browser.

## When to use
You have a lead — a `username`, `email`, keyword, or a specific onion `domain` — that might surface on Tor hidden services (marketplaces, forums, leak sites) and you want to search that space quickly without standing up Tor Browser. Torry indexes/relays dark-web content and offers a per-result "anonymous view" that fetches the onion page through Tor for you. Use it for triage and discovery, not as your operational-security backbone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.torry.io/ (or install the Chrome extension / Android app).
2. Search a keyword, `username`, or paste an onion `domain`.
3. For a result, use the "Tor Anonymous View" button to load the onion page via Tor without your own Tor setup.
4. Screenshot/record anything relevant; do not log in or transact.
5. Pivot: handles, `social-profile` links, or contact addresses found on a hidden service feed the rest of your enrichment.

## Inputs → Outputs
- **In:** keyword / `username` / `email` / onion `domain`
- **Out:** onion links and previews (`domain`), handles/`social-profile` references on those pages
- **Empty/negative result looks like:** no onion results, or a result that won't load via the anonymous view — hidden services are volatile; a dead link doesn't mean the content never existed.

## Gotchas & OpSec
- **Trust boundary:** Torry mediates your Tor access and *claims* no logging — you cannot verify that. Do not treat it as anonymity; for that use `[[tor-browser]]` in a dedicated VM.
- Dark-web results can lead to illegal/hostile content — never open on your working machine, never authenticate.
- OpSec: nominally **passive**, but you are routing curiosity through a third party — assume they can see your queries.

## Overlaps ("do both")
- Pairs with `[[browseriling]]` and `[[tor-browser]]` — Torry is the *search/discovery* front end; Browserling's cloud Tor or a local Tor Browser is where you actually inspect a hidden service with more control.

## Trust & verifiability
`trust: unverified` — a real, working service, but its privacy guarantees are unaudited third-party claims; use it to find things, then verify and inspect them through tooling you control.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | torry-io |
| category | dark-web |
| selectorsIn → selectorsOut | username, email, domain → social-profile, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
