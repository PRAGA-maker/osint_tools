---
id: start-consortium-for-the-study-of-terrorism-and-responses-to-terrorism
name: START Consortium for the Study of Terrorism and Responses to Terrorism
description: Use when you need vetted academic research or incident data on terrorism and extremism — returns University of Maryland studies, datasets, and the Global Terrorism Database.
url: https://www.start.umd.edu/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- terrorism-and-extremism
- academic-research
bestFor: Peer-reviewed terrorism research and structured incident datasets (home of the Global Terrorism Database).
selectorsIn: []
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public access to research, reports, and most datasets; some datasets require a short registration/request form for download.
opsec: passive
opsecNote: Reading a public university research center; no target is queried. A dataset download may ask you to register — use a research/sock-puppet identity if you'd rather not tie the request to your real name.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: START is a University of Maryland-based research center (a former DHS Center of Excellence) producing peer-reviewed, methodologically documented research and the widely cited Global Terrorism Database.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- global-terrorism-database
- street-drug-slang
aliases:
- START UMD
- National Consortium for the Study of Terrorism and Responses to Terrorism
tags:
- terrorism
- academic-research
- dataset
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# START Consortium for the Study of Terrorism and Responses to Terrorism

> A University of Maryland research center and the home of the Global Terrorism Database — authoritative academic research and incident data on terrorism and extremism.

## When to use
You need credible, sourced background on a terrorist organization, an extremist movement, radicalization patterns, or historical incidents — for context, corroboration, or to find structured incident records tied to a case. START is a reference/data layer: it explains and quantifies the threat landscape and provides datasets to query events, not the identities of living individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.start.umd.edu/.
2. Browse Research & Publications for peer-reviewed reports on a group, region, or phenomenon.
3. For incident-level data, go to Data & Tools — notably the [[global-terrorism-database]] — and search events by date, location, perpetrator, and tactic (some downloads require a registration form).
4. Read methodology/codebooks before interpreting dataset fields.
5. Pivot: a named organization (`employer-org`) or incident → sanctions/court-record searches; a GTD event's location/date → local news and primary records.

## Inputs → Outputs
- **In:** none — you browse publications or query datasets by attributes (place, date, group), not by a personal selector
- **Out:** peer-reviewed research, reports, and incident datasets; named groups (`employer-org`) and events to pivot on
- **Empty/negative result looks like:** a topic START hasn't studied, or a GTD query with no matching events — absence reflects research/coverage scope (and GTD's cut-off years), not proof nothing occurred.

## Gotchas & OpSec
- Human-in-the-loop: none to read; some dataset downloads need a registration form.
- Coverage windows: datasets like GTD cover specific year ranges and definitions — check the codebook so you don't over-read gaps or boundaries.
- OpSec: passive; no subject is touched (mind only the optional registration for downloads).

## Overlaps ("do both")
- Pairs with [[global-terrorism-database]] (its flagship dataset) and think-tank analysis like the CSIS terrorism program — START gives academic rigor and structured incident data; think tanks give current strategic framing.

## Trust & verifiability
`trust: trusted` — a university research consortium with peer-reviewed output and documented dataset methodology; among the most authoritative open sources on terrorism, though (as with any research) confirm specific incident facts against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | start-consortium-for-the-study-of-terrorism-and-responses-to-terrorism |
