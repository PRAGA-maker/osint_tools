---
id: euvsdisinfo
name: EUvsDisinfo
description: Use when you have a claim, narrative, outlet, or `name` and want to check it against the EU's searchable database of catalogued pro-Kremlin disinformation cases — returns source/associate and document-id leads.
url: https://euvsdisinfo.eu/category/blog/feed/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Searching a curated database of catalogued pro-Kremlin disinformation narratives and the outlets that spread them.
selectorsIn:
- name
selectorsOut:
- associate
- document-id
status: live
pricing: free
costNote: Free public database and RSS feed run by the EU's East StratCom Task Force (EEAS). No account required.
opsec: passive
opsecNote: Fully passive — reading/searching a public database and its RSS feed. Nothing you do reaches any target. Note it catalogues narratives and outlets, not private individuals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official EU (EEAS East StratCom Task Force) project; each case is documented with sources, though it reflects an explicit EU counter-disinformation mandate — read it as sourced analysis, not neutral wire copy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- EUvsDisinfo
- euvsdisinfo.eu
- EU East StratCom
tags:
- osint-rss-feeds
- disinformation
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# EUvsDisinfo

> The EU's flagship disinformation database (East StratCom Task Force) — thousands of catalogued pro-Kremlin disinformation cases, each with the claim, a debunk, and the outlets that published it.

## When to use
You encounter a suspicious claim, a recurring narrative, or a media outlet/`name` and want to know whether it has been catalogued as disinformation: when it appeared, which outlets pushed it, and the sourced debunk. Useful for assessing a source's credibility, tracing which outlets repeat a narrative (a network-mapping signal), and grounding information-operations analysis. Subscribe to the RSS feed to monitor new cases as they're added.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://euvsdisinfo.eu (or subscribe to the RSS feed at `/category/blog/feed/`).
2. Use the **Disinformation cases** database search — filter by keyword, country/language, outlet, or date.
3. Open a case: the disinformation claim, the debunk with sources, and the list of outlets/publications that carried it.
4. Read the linked outlets as a network — the same narrative across many sites maps a coordinated ecosystem.
5. Pivot: an outlet name → domain/infrastructure tooling and cross-reference other cases citing it; a narrative → search social/news for its current spread.

## Inputs → Outputs
- **In:** a claim/narrative keyword, outlet `name`, country/language, or date
- **Out:** catalogued disinformation cases with debunks, the outlets that published each (`associate`/source network), case references (`document-id`)
- **Empty/negative result looks like:** no case for your query — the narrative isn't in the database (it focuses on pro-Kremlin disinformation), which is not proof a claim is true or false; verify independently.

## Gotchas & OpSec
- Scope is pro-Kremlin disinformation specifically — it won't cover other information operations.
- It carries an EU counter-disinformation mandate; use the sourced debunks, not the framing, as your evidence.
- OpSec: fully passive public database/feed.

## Overlaps ("do both")
- Complements fact-check aggregators and media-bias tools — EUvsDisinfo gives the case-level debunk + outlet network; general fact-checkers cover a broader claim set.

## Trust & verifiability
`trust: trusted` — official EU EEAS project with sourced case documentation; treat it as sourced analysis with a stated mandate, not neutral reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | euvsdisinfo |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name → associate, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
