---
id: the-citizen-lab
name: The Citizen Lab
description: Use when you need authoritative research on spyware, surveillance, censorship and digital threats — a research group's report feed you can monitor and cite.
url: https://citizenlab.ca/feed/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Following and citing rigorous research on state spyware (Pegasus etc.), surveillance vendors, censorship and targeted digital threats.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free; reports and the RSS feed are open access, no account.
opsec: passive
opsecNote: Reading published research is passive and reveals nothing about your subject. Value is contextual/analytic — it names spyware, vendors and indicators you can use to interpret findings elsewhere.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: An interdisciplinary research lab at the University of Toronto's Munk School; peer-recognised, evidence-heavy reporting cited across journalism and policy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Citizen Lab
- citizenlab.ca
tags:
- osint-rss-feeds
- research
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# The Citizen Lab

> The University of Toronto research group behind much of the public reporting on mercenary spyware, surveillance vendors and censorship — a citable source and a feed worth monitoring.

## When to use
Your work touches surveillance or digital threats: you suspect spyware targeting, need to understand a surveillance vendor, or want authoritative context on censorship and network interference in a region. Citizen Lab publishes deep, well-sourced reports (e.g. Pegasus/NSO investigations) that provide indicators, vendor profiles and methodology you can cite and build on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Browse https://citizenlab.ca/ or subscribe to the RSS feed at https://citizenlab.ca/feed/ in a reader to monitor new reports.
2. Search their research by topic (spyware, app privacy, censorship) or region.
3. Read the report's evidence and appendices — indicators, domains, technical findings — and use them to interpret your own case data.
4. Cite the primary report (with date) rather than secondary coverage.
5. Pivot: technical indicators (domains, infrastructure) named in a report can seed your own domain/infrastructure OSINT.

## Inputs → Outputs
- **In:** n/a — a research/reading source, not a lookup taking a selector
- **Out:** authoritative reports and indicators on spyware, surveillance and censorship
- **Empty/negative result looks like:** not applicable; if a specific vendor/threat isn't covered, that just means no report exists — check adjacent research or other threat intel.

## Gotchas & OpSec
- It's an analysis/reporting source, not a queryable database — you read and cite, you don't look up a person.
- Reports are point-in-time; note publication dates as the threat landscape moves.
- OpSec: passive reading; no account, no target contact.

## Overlaps ("do both")
- Complements threat-intel platforms and RSS monitoring (`[[feedly]]`, `[[newsblur]]`) — those aggregate; Citizen Lab is a primary-research source you'd add to that monitoring for the surveillance/spyware beat.

## Trust & verifiability
`trust: trusted` — a rigorous academic research lab whose findings are evidence-heavy and widely corroborated; still cite the specific report and date for accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-citizen-lab |
