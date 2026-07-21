---
id: national-criminal-justice-service
name: NCJRS Virtual Library (via OJP)
description: Use when you need US criminal-justice research, statistics, and publications for background/context — returns reports and document-id references, not records about individuals.
url: https://www.ncjrs.gov/
category: search-engines
path:
- search-engines
bestFor: Finding authoritative US criminal-justice research, statistics, and reports for case context.
selectorsIn:
- name
selectorsOut:
- document-id
- employer-org
status: degraded
pricing: free
costNote: Free government publications; no account. The standalone NCJRS service was wound down and now redirects into the Office of Justice Programs (OJP) site.
opsec: passive
opsecNote: Reading government research publications discloses nothing about a subject; this is background literature, not a targeted query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: US Office of Justice Programs content (formerly the National Criminal Justice Reference Service); authoritative government research, though the legacy NCJRS portal itself now redirects.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NCJRS
- National Criminal Justice Reference Service
- ncjrs.gov
tags:
- toddington
- curated-directory
- specialty-search
- government-research
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# NCJRS Virtual Library (via OJP)

> The US government's criminal-justice research library — reports, statistics, and evaluations — now served through the Office of Justice Programs after the standalone NCJRS site was retired.

## When to use
A **background/literature** resource, not a person locator. When a case needs authoritative US criminal-justice context — the research behind a method, official statistics, program evaluations, or an agency publication — this is a trusted government library. It answers "what does the evidence/policy say," not "where is this person"; expect documents and data, never individual records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ncjrs.gov/ — it now 301-redirects into the OJP site's legacy NCJRS library area.
2. Use the OJP/NCJRS library search for a topic, agency, or author `name`.
3. Open matching publications (many free PDFs) for research findings, statistics, and citations.
4. Note issuing `employer-org` agencies (NIJ, BJS, OJJDP) and follow their current portals for the latest data.
5. Pivot: statistics/agency leads feed BJS/NIJ data tools; a report's citations point to primary sources.

## Inputs → Outputs
- **In:** a topic, agency, or author `name`
- **Out:** research/publication `document-id`s (reports, PDFs) and issuing `employer-org` agencies
- **Empty/negative result looks like:** dead or redirected links to old NCJRS URLs — the standalone service is retired, so some legacy links won't resolve; search the OJP library instead.

## Gotchas & OpSec
- **Degraded:** ncjrs.gov no longer stands alone; it redirects into OJP, and some old deep links are broken. Prefer the OJP library search.
- Literature only — no individual criminal records here.
- OpSec: fully passive government-document research.

## Overlaps ("do both")
- Pairs with the Bureau of Justice Statistics and National Institute of Justice sites — those host the current datasets, while this preserves the broader publication archive.

## Trust & verifiability
`trust: trusted` — content originates from the US Office of Justice Programs and its bureaus, so the research is authoritative; only the legacy portal's availability is degraded.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-criminal-justice-service |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
