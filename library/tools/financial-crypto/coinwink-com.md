---
id: coinwink-com
name: Coinwink
description: Use when you're tracking a crypto asset relevant to a case and want to be alerted on price moves without watching charts — returns email/Telegram/SMS alerts when a coin hits a threshold.
url: https://coinwink.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Free crypto price-alert monitoring (email/Telegram/SMS) for coins/tokens tied to an investigation — a monitoring utility, not a blockchain-analysis tool.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier allows ~5 active email and ~5 active Telegram alerts plus a watchlist; paid plans ($8–$12/mo) lift limits and add SMS. Free tier suffices for light monitoring.
opsec: passive
opsecNote: You monitor public market prices, not any target — nothing about a subject is disclosed. To receive alerts you register an email/phone with Coinwink, so use a research contact, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Straightforward commercial price-alert service; reliable for what it is, but it only relays market data and has no investigative/on-chain capability.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- coinmarketcap
- blockchain-explorer
aliases:
- coinwink.com
- Coinwink price alerts
tags:
- crypto
- price-alerts
- monitoring
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Coinwink

> A free crypto price-alert service (email/Telegram/SMS) — useful for passively watching a coin relevant to a case, but strictly a market-monitoring utility, not a blockchain investigator's tool.

## When to use
An investigation touches a specific cryptocurrency or token (a coin a subject trades, a ransom asset, a token tied to a scheme) and you want to be pinged when its price crosses a level or moves sharply, instead of sitting on charts. Coinwink handles that alerting for free. Be clear on its limits: it monitors *market prices*, not wallets, transactions, or addresses — for on-chain investigation you need a blockchain explorer/analytics tool, not this.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://coinwink.com/ and register with a research email (add Telegram for free push alerts).
2. Add a coin/token and set an alert condition — above/below a target price, or a percentage move.
3. Optionally build a watchlist to track several assets at once; alerts arrive by email/Telegram (SMS on paid plans).
4. Use triggers as timing cues (e.g. a sharp move around an event of interest), then investigate the *why* elsewhere.
5. Pivot: correlate price events with on-chain activity via a `[[blockchain-explorer]]`, and use `[[coinmarketcap]]` for market context/history.

## Inputs → Outputs
- **In:** none in the OSINT-selector sense — you configure coins/tokens and thresholds.
- **Out:** none per-subject — price-threshold notifications and a watchlist (a monitoring stream, no entity data).
- **Empty/negative result looks like:** no alert fires because the threshold wasn't hit — that's expected, not a failure. An unlisted obscure token means Coinwink doesn't track it.

## Gotchas & OpSec
- Human-in-the-loop: requires an account to receive alerts.
- OpSec: **passive** — public market data only; nothing about any subject is exposed. Register with a throwaway research contact so your monitoring targets aren't tied to your identity.
- Zero investigative depth: no address tracking, clustering, or transaction analysis. Do not mistake it for an on-chain tool.

## Overlaps ("do both")
- Pairs with `[[blockchain-explorer]]` — the explorer does the actual investigative work (addresses, transactions, flows); Coinwink just tells you when the market moved. Use Coinwink for timing, the explorer for substance.
- Overlaps with `[[coinmarketcap]]` alerts as an interchangeable price-watch source.

## Trust & verifiability
`trust: community` — a simple, dependable price-alert relay. It adds no data of its own beyond market feeds, so there's little to verify; just don't expect any investigative signal from it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coinwink-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
