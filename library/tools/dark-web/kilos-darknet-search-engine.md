---
id: kilos-darknet-search-engine
name: Kilos Darknet Search Engine
description: Use when you have a darknet vendor `username`, `crypto-wallet`, or product term and want marketplace listings and vendor profiles — returns market vendors, listings, and linked wallets/PGP.
url: http://dnmugu4755642434.onion.pet/captcha
category: dark-web
path:
- dark-web
bestFor: Searching darknet-market vendors, listings, reviews, and Bitcoin addresses across multiple markets at once.
selectorsIn:
- username
- crypto-wallet
selectorsOut:
- username
- crypto-wallet
status: degraded
pricing: free
costNote: Free to search; no payment. Frequently offline and requires Tor plus a CAPTCHA to reach.
opsec: active
opsecNote: This indexes live darknet-market content. Access ONLY over Tor from an isolated/VM environment on a non-attributable connection — never via a clearnet Tor2web proxy (the .onion.pet address in the URL field is a defunct proxy; find the current Kilos .onion via Ahmia). Searching is passive toward vendors, but you are on darknet infrastructure and may surface illegal content — collect intelligence only, never transact.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: A well-documented darknet market search engine (successor to Grams), but anonymously run, frequently down, and reachable only over Tor — treat results as leads, not verified facts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ahmia
- onionsearch
- torch
- deepsearch
- raklet
- ransomware-group-sites
aliases:
- KILOS
- Kilos search
tags:
- Search engines
- Darknet/deepweb search tools
- darknet-market
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Kilos Darknet Search Engine

> The most extensive darknet-market search engine (Grams' successor) — search vendors, listings, reviews, and Bitcoin addresses across markets, when it's actually online.

## When to use
You are investigating darknet-market activity and have a vendor `username`, a `crypto-wallet` (Bitcoin address), a PGP fingerprint, or a product term. Kilos indexes multiple marketplaces at once — vendor profiles, listings, review histories, and (notably) a Bitcoin-address lookup — making it the go-to when you need marketplace-level visibility that clearnet-safe Tor search engines deliberately exclude.

## How to use it (`bestInteractionPattern`: web-manual)
1. Reach Kilos over **Tor Browser** (the clearnet `.onion.pet` proxy in the URL field is defunct). Find its current `.onion` via `[[ahmia]]` or a trusted darknet index — verify the address before trusting it.
2. Solve the CAPTCHA (Kilos gates access to deter scraping/abuse).
3. Search a vendor `username`, product term, or Bitcoin address; browse results by market.
4. Read vendor profiles, listing details, review histories, and any linked wallets/PGP keys.
5. Pivot: a `crypto-wallet` → blockchain-analysis tools; a vendor handle/PGP → cross-market correlation and username-search. Collect only — never place an order.

## Inputs → Outputs
- **In:** vendor `username`, `crypto-wallet` (BTC address), product term, or PGP fingerprint
- **Out:** market vendor profiles, listings, reviews, linked `crypto-wallet`s and PGP keys (`username` correlations)
- **Empty/negative result looks like:** no results, a failed CAPTCHA, or the site simply unreachable — Kilos is often down; retry later or fall back to broader onion search.

## Gotchas & OpSec
- Frequently offline and anonymously operated — treat availability and results as unreliable; corroborate everything.
- **Darknet infrastructure:** access only over Tor from an isolated VM on a non-attributable connection. Verify the current onion address (phishing clones exist). Gather intelligence only; transacting is illegal.
- Human-in-the-loop: CAPTCHA on entry.

## Overlaps ("do both")
- Pairs with `[[ahmia]]` (safer clearnet-accessible onion search, and to find Kilos's current address), `[[onionsearch]]` (multi-engine breadth), and `[[torch]]` — Kilos is uniquely market-focused; the others index the wider darknet.

## Trust & verifiability
`trust: unverified` — a real, well-known darknet search engine, but anonymously run, unstable, and Tor-only; its index is a lead source, not authoritative, and phishing clones make address verification essential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kilos-darknet-search-engine |
| category | dark-web |
| selectorsIn → selectorsOut | username, crypto-wallet → username, crypto-wallet |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
