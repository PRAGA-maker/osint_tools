---
id: non-typical-osint-guide
name: Non-typical OSINT Guide
description: Use when a standard approach has stalled and you want unconventional OSINT techniques, mindset training, or pointers to niche tools (crypto, geolocation, counter-OSINT) — returns methodology and curated resource links (reference reading, no selector output).
url: https://github.com/OffcierCia/non-typical-OSINT-guide
category: training-ctf
path:
- training-ctf
bestFor: Advanced/creative OSINT methodology, cognitive-bias and tradecraft training, and lesser-known tools for crypto, due-diligence and geolocation work.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open GitHub guide. No account.
opsec: passive
opsecNote: Passive — reading public documentation. Includes counter-OSINT sections useful for hardening your own operational security before working a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded community guide by OfficerCia (~1.5k stars, multi-language); a curated reference, not a data source — verify each linked tool independently.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OfficerCia OSINT guide
tags:
- guide
- techniques
- methodology
source: gh-topic-osint-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Non-typical OSINT Guide

> A popular, actively-maintained guide to the *unconventional* side of OSINT — mindset, cognitive-bias mitigation, crypto/on-chain investigation, geolocation, and counter-OSINT — for when the obvious approaches have run dry.

## When to use
Your standard playbook has stalled and you need fresh angles or niche tooling: on-chain cryptocurrency tracing, due-diligence workflows, geolocation via games/ARGs, psycholinguistic analysis, or defensive counter-OSINT. It's also strong for foundational skills — mind-mapping, critical thinking, bias mitigation — that improve *how* you investigate, not just which tool you open.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the guide on GitHub (translations exist: FR, DE, KO, ZH, IT, JA).
2. Jump to the relevant section — crypto investigations, geolocation, training/CTFs, counter-OSINT, or the reasoning/bias material.
3. Note the recommended techniques and the specific tools it links for your problem.
4. Apply the counter-OSINT/OPSEC advice to your own setup before engaging a target.
5. Pivot: from a technique here to the concrete tool in this library (crypto-wallet, geolocation, etc.).

## Inputs → Outputs
- **In:** an investigative problem or skill gap (not a selector)
- **Out:** methodology, mindset training, and curated links to niche tools (guidance, not data)
- **Empty/negative result looks like:** your exact problem isn't covered — it's a curated guide, not exhaustive; pair it with a broader OSINT framework list.

## Gotchas & OpSec
- It's a **reference/training** resource — it returns no data about a person.
- Emphasis on crypto/dark-web/creative techniques; some linked tools are advanced or niche — vet each before use.
- OpSec: passive; its counter-OSINT sections help protect your own operation.

## Overlaps ("do both")
- Pairs with `[[ohsint-gitbook]]` and general OSINT framework directories — read across methodology sources, then execute in the specific tools they cite.

## Trust & verifiability
`trust: community` — a widely-cited, actively-maintained individual guide; treat as informed guidance, confirm linked tools' current state, and rely on primary evidence for actual findings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | non-typical-osint-guide |
| category | training-ctf |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
