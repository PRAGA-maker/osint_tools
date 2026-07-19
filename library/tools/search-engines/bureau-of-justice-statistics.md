---
id: bureau-of-justice-statistics
name: Bureau of Justice Statistics
description: Use when you need official US crime/justice statistics (arrests, corrections, victimization) for context — an aggregate government data portal; returns datasets, not individual records.
url: https://bjs.ojp.gov/
category: search-engines
path:
- search-engines
bestFor: Authoritative aggregate US criminal-justice data (corrections, courts, victimization, law enforcement) for background/context, not person lookups.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free official US Department of Justice statistics portal; no account.
opsec: passive
opsecNote: Fully passive — you read published aggregate statistics from a government site; no personal query is involved and nothing reaches any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US DOJ Bureau of Justice Statistics; authoritative for national/state justice statistics, but it publishes aggregates, not individual case data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BJS
- bjs.ojp.gov
tags:
- toddington
- government-data
- statistics
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Bureau of Justice Statistics

> The US DOJ's statistics arm — authoritative aggregate crime/justice data for context, not a way to look up a specific person.

## When to use
You need reliable background numbers on US criminal justice — incarceration, arrests, victimization surveys, court processing, law-enforcement agencies — to frame a report or understand base rates around a case. It will not return records about an individual; it is aggregate statistics and datasets.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bjs.ojp.gov/ (the old bjs.gov redirects here).
2. Browse by topic (Corrections, Courts, Victims, Law Enforcement) or use the data tools/publications search.
3. Read the output: reports, tables, and downloadable datasets on the chosen topic.
4. Pivot: use the figures for context; for anything about a specific person, go to case-level public records instead.

## Inputs → Outputs
- **In:** a topic/statistics query (no personal selector)
- **Out:** aggregate datasets, tables, and publications
- **Empty/negative result looks like:** a niche query with no matching dataset — BJS covers broad national/state aggregates, not granular local or individual data.

## Gotchas & OpSec
- **Aggregate only** — no individual records; do not expect person-level output.
- Data can lag by a year or more, as is normal for official statistics.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Complements case-level public-records tools — BJS gives the statistical backdrop; those give the specific record.

## Trust & verifiability
`trust: trusted` — official government statistics with documented methodology; authoritative for aggregates, irrelevant for identifying an individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bureau-of-justice-statistics |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
