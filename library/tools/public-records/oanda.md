---
id: oanda
name: Oanda
description: Use when you have a money amount and a date and want the exchange rate then — returns historical and live currency conversion at a chosen date, useful for making sense of financial figures in a case.
url: https://www.oanda.com/currency-converter/
category: public-records
path:
- public-records
bestFor: Converting a transaction/asset amount between currencies at the exact historical date it occurred.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: The web currency converter (including historical rates) is free. High-volume, API, and long-range corporate rate data are paid; single manual conversions fit the free tier.
opsec: passive
opsecNote: You look up a public exchange rate — nothing about your subject is entered or disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: OANDA is a long-established, regulated FX company; its historical rate data is widely cited as a reference source in finance.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- OANDA Currency Converter
- oanda.com
tags:
- toddington
- curated-directory
- reference-sites
- currency
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Oanda

> A trusted currency converter with historical rates — turn a foreign-currency amount and a date into its value in your reference currency.

## When to use
A financial figure appears in a case in a foreign currency — a wire transfer, a purchase, an asset value, a ransom or scam amount — and you need to understand its real size, either today or on the specific date it occurred. Because exchange rates move, converting a 2019 transfer at today's rate misleads; OANDA lets you set the actual date so the figure is meaningful in context and comparable across records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.oanda.com/currency-converter/.
2. Enter the amount, pick the source and target currencies.
3. Set the **date** to when the transaction/observation happened (the converter supports historical dates, not just live rates).
4. Read the converted value; note whether it's an interbank/mid rate vs a card/retail rate if precision matters.
5. Pivot: the normalized amount feeds a financial timeline, sanity-checks a claimed sum, or compares figures stated in different currencies across documents.

## Inputs → Outputs
- **In:** a currency amount + currencies + a date (you supply these; not a person selector)
- **Out:** the converted value at that date (historical) or now (live)
- **Empty/negative result looks like:** very old dates or thinly-traded/legacy currencies may lack a rate or return only a mid-market approximation — treat gaps as "rate unavailable," and note pre-redenomination currencies need special handling.

## Gotchas & OpSec
- Human-in-the-loop: none for a single conversion; bulk/programmatic historical data is the paid API.
- The rate shown is typically an interbank/mid rate — actual bank/card conversions include spreads, so a converted figure is an estimate of economic value, not the exact amount a party received.
- Watch currency redenominations and code changes over long time spans.

## Overlaps ("do both")
- Pairs with any transaction-record or crypto-tracing tool — those give you the raw amount and currency; OANDA normalizes it to a comparable value at the right date.

## Trust & verifiability
`trust: trusted` — OANDA is a regulated FX firm whose historical rate data is a standard finance reference; cite the rate type (mid vs retail) and date for reproducibility.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oanda |
| category | public-records |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
