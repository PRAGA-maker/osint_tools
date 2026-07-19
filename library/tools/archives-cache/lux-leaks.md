---
id: lux-leaks
name: LuxLeaks (ICIJ)
description: Use when you have an `employer-org` (a large company) and want to know if it appears in the Luxembourg Leaks tax-ruling investigation — returns which multinationals had secret Luxembourg tax deals, by industry.
url: https://projects.icij.org/luxembourg-leaks/viz/industries/index.html
category: archives-cache
path:
- archives-cache
bestFor: Checking whether a multinational appears in the 2014 ICIJ LuxLeaks tax-ruling investigation, browsable by industry.
selectorsIn:
- employer-org
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free ICIJ investigative project; no account required.
opsec: passive
opsecNote: You browse a published ICIJ investigation of already-public leaked documents; nothing is disclosed to any company. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the International Consortium of Investigative Journalists from the 2014 LuxLeaks disclosures; a vetted, widely-reported dataset — though it is a fixed historical investigation, not a live registry.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Luxembourg Leaks
- LuxLeaks
tags:
- icij
- leaks
- tax
- corporate
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- icij-offshore-leaks-database
---

# LuxLeaks (ICIJ)

> ICIJ's Luxembourg Leaks project — an interactive record of the 2014 investigation into secret Luxembourg tax rulings, showing which of 350+ multinationals had confidential tax deals, grouped by industry. A corporate-context and entity-link source.

## When to use
You are profiling an `employer-org` — a large multinational connected to your subject — and want to know whether it features in the LuxLeaks tax-avoidance investigation. It helps establish corporate context (aggressive tax structuring, Luxembourg subsidiaries) and can surface company-name links useful when mapping the corporate side of an investigation. It is company-focused, so its direct value for locating an individual is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.icij.org/luxembourg-leaks/viz/industries/index.html.
2. Browse the industry visualisation and locate the `employer-org` you're checking, or scan an industry for relevant companies.
3. Open a company entry to see its place in the investigation and links to the associated ICIJ reporting/documents.
4. Follow through to ICIJ's articles and, where relevant, the underlying leaked tax-ruling documents.
5. Pivot: a company's presence feeds corporate-registry and Offshore-Leaks-database searches; industry peers can widen an entity map.

## Inputs → Outputs
- **In:** `employer-org` (a multinational)
- **Out:** `document-id` (investigation entries/associated documents) and linked `employer-org` names by industry
- **Empty/negative result looks like:** the company isn't in the dataset — LuxLeaks covers a specific 2014 set of Luxembourg tax rulings, so absence just means it's not in that leak, not that it has no tax arrangements.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive** — a published investigation of leaked documents; no exposure.
- Fixed scope: this is the 2014 LuxLeaks investigation only. For broader offshore/company links, use ICIJ's Offshore Leaks Database and corporate registries; don't treat LuxLeaks as a general company-search tool.

## Overlaps ("do both")
- Pairs with the ICIJ Offshore Leaks Database and OpenCorporates — LuxLeaks is the narrow Luxembourg-tax-ruling slice; those give broader offshore-entity and corporate-registry coverage that connects a company to people and jurisdictions.

## Trust & verifiability
`trust: trusted` — an ICIJ investigation built from vetted leaked documents and extensively reported; entries are reliable for the covered investigation, with the caveat that it is a historical snapshot rather than a live or exhaustive registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lux-leaks |
| category | archives-cache |
| selectorsIn → selectorsOut | employer-org → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
