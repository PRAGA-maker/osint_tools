---
id: onion-engine
name: Onion Engine
description: Use when you have a `username`, `domain`, `crypto-wallet` or keyword and want to find it on Tor hidden services from the clearnet — returns `.onion` `social-profile`/`domain` leads.
url: https://onionengine.com/
category: dark-web
path:
- dark-web
bestFor: Searching indexed .onion hidden services from a normal browser for a name, handle, keyword or identifier.
selectorsIn:
- username
- domain
- crypto-wallet
selectorsOut:
- domain
- social-profile
status: live
pricing: freemium
costNote: Free anonymous web search ("forever free, no credit card"); an enterprise threat-intelligence API with higher limits and monitoring is paid.
opsec: passive
opsecNote: Searching from the clearnet means you query OnionEngine's index rather than crawling Tor yourself — you don't touch any hidden service, so it is passive and keeps you off the darknet. The site claims no IP logging and ephemeral queries; still treat it as third-party and use a sock-puppet browser/VPN.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent darkweb search index active since 2017; coverage and freshness of .onion indexing are unverifiable from outside, so treat hits as leads to confirm on Tor.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- onionengine.com
- OnionEngine
tags:
- dark-web
- tor
- onion-search
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Onion Engine

> A clearnet search engine over Tor hidden services — look for a name, handle, keyword, domain or wallet across indexed `.onion` sites without opening Tor yourself.

## When to use
You want to know whether a selector — a `username`, a `domain`, a `crypto-wallet` address, an email, or a keyword — appears on the dark web, and you'd rather search a clearnet index than crawl Tor manually. OnionEngine indexes millions of `.onion` pages and lets you query them from a normal browser. Useful for checking if a subject's identifier surfaces on marketplaces, forums, or leak sites, and for finding hidden-service `domain`s to investigate further on Tor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onionengine.com/ in a sock-puppet browser (VPN recommended).
2. Enter your selector — `username`, `domain`, `crypto-wallet`, email, or keyword.
3. Review the results: matching `.onion` URLs with snippets/titles.
4. Assess relevance from the snippet before deciding to visit — note the hidden-service `domain`s worth confirming.
5. Pivot: open promising `.onion` addresses in the Tor Browser (never from the clearnet) to verify; take confirmed handles/wallets into cross-platform and blockchain tools.

## Inputs → Outputs
- **In:** `username`, `domain`, `crypto-wallet`, email, or keyword
- **Out:** `.onion` `domain`s and `social-profile`/mention leads from indexed hidden services
- **Empty/negative result looks like:** no matches — which is weak evidence, since no darkweb crawler indexes everything and many services are unlinked, gated, or short-lived. Absence here is not proof the selector is absent from the dark web.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; visiting results requires Tor and judgement.
- OpSec: **passive** to search from the clearnet — you hit OnionEngine's index, not the hidden services. But **only ever open .onion results in the Tor Browser**, never by clicking through on the clearnet, and use a sock-puppet identity throughout.
- Index quality is opaque: coverage, freshness, and completeness can't be verified externally, and darkweb content is volatile. Treat every hit as a lead to confirm live.

## Overlaps ("do both")
- Pairs with other darkweb search indexes (Ahmia, etc.) and with clearnet username/wallet tools — run the same selector across multiple onion indexes (coverage differs widely), and cross-reference darkweb hits with clearnet identity to attribute.

## Trust & verifiability
`trust: community` — an independent index with claims (no-logging, millions of pages) that can't be externally verified. Its value is as a lead generator; confirm anything material by visiting the source over Tor.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onion-engine |
| category | dark-web |
| selectorsIn → selectorsOut | username, domain, crypto-wallet → domain, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
