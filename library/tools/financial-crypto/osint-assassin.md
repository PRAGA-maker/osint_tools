---
id: osint-assassin
name: OSINT-Assassin
description: Use when you want a curated start.me link-collection of OSINT resources (crypto/blockchain-leaning) — returns a directory of tools to pivot into, not a lookup itself.
url: https://start.me/u/l61Bqy
category: financial-crypto
path:
- financial-crypto
bestFor: Browsing a community-curated start.me dashboard of OSINT resources (with a cryptocurrency/blockchain slant) as a jumping-off point to other tools.
selectorsIn:
- crypto-wallet
- name
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free to view; start.me pages are publicly readable without an account.
opsec: passive
opsecNote: Reading a start.me link dashboard is passive — you're just browsing a curated list of links. OpSec matters at the tools you click through to, not here. Nothing on this page queries a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A personal, user-curated start.me page (author handle l61Bqy); it is a link collection whose quality and freshness depend entirely on one uploader — treat linked tools on their own merits.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- start-me
aliases:
- OSINT Assassin start.me
tags:
- cryptosites
- CryptoCurrency Related Sites
- link-directory
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# OSINT-Assassin

> A community-curated start.me dashboard of OSINT links with a cryptocurrency/blockchain slant — a directory to pivot *from*, not a tool that returns data on a subject.

## When to use
You want a ready-made, human-curated set of OSINT resources — particularly crypto/blockchain-oriented ones — gathered on a single start.me page, so you can scan categories and click through to the actual lookup tools. Use it early as an orientation/menu, not as something that itself takes a `crypto-wallet` or `name` and returns findings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://start.me/u/l61Bqy in a browser (start.me may block automated fetchers, so view it interactively).
2. Scan the categorised link tiles; note the crypto/blockchain section and any tools relevant to your case.
3. Click through to individual tools — that is where the real querying happens.
4. Sanity-check each linked tool before relying on it (start.me lists are personal and can contain dead or low-quality links).
5. Pivot: the linked blockchain-analysis and explorer tools are where you actually investigate a `crypto-wallet`.

## Inputs → Outputs
- **In:** none directly — you bring your case; the page offers a menu (nominally crypto/`name`-related resources)
- **Out:** links to other tools (which in turn may return `crypto-wallet` intelligence); this page returns no data on a subject itself
- **Empty/negative result looks like:** the page is a static link list — "empty" means the links are stale/dead or none fit your need. It never returns a per-subject result.

## Gotchas & OpSec
- It is a directory, not an analytical tool — don't expect it to look anything up.
- Personal curation means variable quality and link rot; verify each destination tool independently.
- OpSec is a property of the tools you click into, not of browsing the list.

## Overlaps ("do both")
- Pairs with `[[start-me]]` and other curated OSINT dashboards — cross-reference several link collections, since each curator includes tools the others miss.

## Trust & verifiability
`trust: unverified` — a single user's start.me page; the collection may be useful but is unvetted, so judge every linked tool on its own merits rather than trusting inclusion here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-assassin |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, name → crypto-wallet |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
