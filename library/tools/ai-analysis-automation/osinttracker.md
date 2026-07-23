---
id: osinttracker
name: Osintracker
description: Use when you have multiple entry points (`email`, `domain`, `crypto-wallet`, phone, accounts) and want to map and document an investigation as a linked graph — returns a visual, sourced entity/relationship board.
url: https://app.osintracker.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Visualising and documenting an OSINT investigation as a local entity-relationship graph.
selectorsIn:
- email
- crypto-wallet
selectorsOut:
- associate
- crypto-wallet
status: live
pricing: free
costNote: Free web app; all investigation data is stored locally in your browser (IndexedDB) — no account required, and nothing is uploaded.
opsec: passive
opsecNote: Data never leaves your machine (browser-local storage), which is strong OpSec for casework. It doesn't perform lookups against targets itself — you import findings from other tools — so it adds no target-facing footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Free tool by OSINT analyst Matthieu Amiot; well-regarded in the OSINT community. It's a documentation/visualisation aid — it holds your data, it doesn't source or verify it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINTTracker
- app.osintracker.com
tags:
- Tools collections/toolkits
- visualization
- case-management
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Osintracker

> Investigation whiteboard: model people, emails, domains, wallets and their links as an interactive graph — entirely in your browser, nothing uploaded.

## When to use
You're running an investigation with several entry points — an `email`, a `domain`, a `crypto-wallet`, phone numbers, social accounts — and need to keep track of entities and how they connect. Osintracker turns your findings into a node-link graph you can annotate, date, source and rate, so relationships (`associate` links) become visible and the case is documented as you go. It's the analysis/record layer, not a data-collection tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.osintracker.com/ (no signup; data lives in your browser).
2. Add entities — people, emails, phones, accounts, domains, IPs, wallets — organised by family/type.
3. Draw connections between them: each link can carry a direction, date, source, rating and colour.
4. Enrich by importing JSON exported from Epieos or OSINT Industries (no API key needed).
5. Export the board to HTML/Markdown/CSV/JSON or a PNG of the graph for your report. Pivot: use the graph to spot gaps and shared nodes to chase next.

## Inputs → Outputs
- **In:** investigation entry points (`email`, `domain`, `crypto-wallet`, phones, accounts) and findings from other tools
- **Out:** a visual, sourced entity/relationship graph exposing `associate` links and shared `crypto-wallet`/identifiers; exportable report
- **Empty/negative result looks like:** an empty/sparse graph — you haven't fed it findings yet; Osintracker doesn't discover data on its own, so it only reflects what you add.

## Gotchas & OpSec
- It doesn't perform lookups — pair it with tools that actually source data, then record results here.
- Data is browser-local: strong for privacy, but clearing browser storage or switching machines loses the board — export regularly to back up.
- OpSec: passive and low-footprint; keeping the case local avoids uploading sensitive investigation data to a third party.

## Overlaps ("do both")
- Pairs with enrichment tools (Epieos, OSINT Industries) — those collect the data on an email/phone, and Osintracker imports and visualises it into the case graph.

## Trust & verifiability
`trust: community` — a respected free community tool; it's a documentation and visualisation aid, so trust rests on the sourced data you put in, not on any lookup it performs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osinttracker |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, crypto-wallet → associate, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
