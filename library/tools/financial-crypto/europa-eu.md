---
id: europa-eu
name: Europol Spotlight — Cryptocurrencies (Tracing criminal finances)
description: Use when you are tracing a `crypto-wallet` in a criminal-finance context and want an authoritative methodology reference — returns Europol's tradecraft on how illicit crypto flows are followed, not target data.
url: https://www.europol.europa.eu/cms/sites/default/files/documents/Europol%20Spotlight%20-%20Cryptocurrencies%20-%20Tracing%20the%20evolution%20of%20criminal%20finances.pdf
category: financial-crypto
path:
- financial-crypto
bestFor: Grounding a crypto-tracing investigation in Europol's published methodology for following illicit cryptocurrency finances.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free public PDF published by Europol; no account or payment required.
opsec: passive
opsecNote: Downloading a public Europol PDF discloses nothing about your subject. It is reference reading — the opsec footprint is entirely on whichever tracing tools you subsequently use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Europol (EU law-enforcement agency); an authoritative methodology document, not an interactive lookup service.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Europol Spotlight Cryptocurrencies
- Tracing the evolution of criminal finances
tags:
- cryptosites
- CryptoCurrency Related Sites
- methodology
- europol
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- e-justice-europa-eu
- eu-consolidated-corporate-registers
- eu-sanctions-tool
- europa-press-releases
- european-commission-home-affairs
- european-union-open-data-portal
- eurostat
- frontex-migratory-map
- inspire-geoportal
- vat-number-validation
---

# Europol Spotlight — Cryptocurrencies (Tracing criminal finances)

> An authoritative Europol reference report on how illicit cryptocurrency flows are traced — methodology and tradecraft, not a lookup tool.

## When to use
You are working a `crypto-wallet` in a criminal-finance context (fraud, laundering, extortion) and want to ground your approach in how professional law-enforcement tracing actually works — mixers, chain-hopping, exchange cash-out points, and the investigative sequence. Read this to sharpen method and vocabulary before (and while) you use the actual explorers and chain-analysis tools. It informs technique; it holds no target data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open/download the PDF from the Europol URL.
2. Read the sections on how criminal crypto finances evolve and are followed (obfuscation techniques, cash-out chokepoints).
3. Map the described method onto your case: identify where your subject's flow could be pierced (exchange KYC, mixer patterns).
4. Execute the actual tracing in a blockchain explorer / chain-analysis tool, guided by this framing.
5. Pivot: methodology → concrete steps in explorer tools; identified cash-out exchanges → KYC/legal-process leads.

## Inputs → Outputs
- **In:** a `crypto-wallet` / tracing problem you want methodology for
- **Out:** investigative method and tradecraft to apply elsewhere (no direct `crypto-wallet` data)
- **Empty/negative result looks like:** not applicable — it's a static reference document; "no result" only means the report doesn't cover your specific technique, so supplement with current chain-analysis guides.

## Gotchas & OpSec
- It is a reading resource, NOT a tracer — it returns no on-chain data; you still run explorers/analysis tools.
- Dated (2021): the tradecraft is durable but the tooling landscape has moved; treat specifics as a foundation, not the latest state.
- OpSec: passive; footprint lives entirely in the tools you use after reading.

## Overlaps ("do both")
- Pairs with blockchain explorers, chain-analysis tools, and EU corporate/sanctions resources (e.g. [[eu-sanctions-tool]]) — this gives the method; those do the actual tracing and entity resolution.

## Trust & verifiability
`trust: trusted` — an official Europol publication, authoritative as methodology; verify current tooling and typologies against up-to-date sources given the 2021 date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | europa-eu |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
