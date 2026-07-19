---
id: the-pegasus-project-occrp
name: The Pegasus Project | OCCRP
description: Use when you have a `name` and want to know if they appear among Pegasus spyware targets — returns the "Who's on the List" investigative findings for that person.
url: https://www.occrp.org/interactives/project-p/
category: public-records
path:
- public-records
bestFor: Checking whether a person is among the journalists, activists, and officials identified in the Pegasus Project investigation into NSO spyware targeting.
selectorsIn:
- name
selectorsOut:
- name
- associate
status: live
pricing: free
costNote: Free published investigative resource from the OCCRP / Forbidden Stories consortium.
opsec: passive
opsecNote: You read a published investigation, not a live database of the target — nothing is signalled. The subject matter (surveillance targets) is sensitive; handle any match discreetly and corroborate before repeating claims.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by OCCRP within the Forbidden Stories–led Pegasus Project consortium with Amnesty's Security Lab; a rigorously-reported, widely-corroborated investigation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Pegasus Project
- Who's on the List
- Forbidden Stories Pegasus
tags:
- surveillance
- pegasus
- investigative-journalism
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- data-occrp-org
- occrp-aleph
- occrp-org
- organized-crime-and-corruption-reporting-project
- visual-investigative-scenarios
- investigative-dashboard
---

# The Pegasus Project | OCCRP

> OCCRP's interactive from the Pegasus Project — "Who's on the List": the reported people selected as potential targets of NSO Group's Pegasus spyware.

## When to use
You have a `name` — typically a journalist, activist, lawyer, executive, or official — and want to know whether they surfaced in the Pegasus Project, the consortium investigation into a leaked list of ~50,000 phone numbers selected for potential Pegasus targeting. A match is a strong lead that the person was of interest to a state client of NSO, and often surfaces the reporting that names *who* may have targeted them. It's a fixed published dataset, not a live lookup, so treat it as a reference to consult, not a monitoring tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.occrp.org/interactives/project-p/ (the "Who's on the List" interactive).
2. Browse/search the profiled individuals for your `name`.
3. Read the entry: who they are, the country/client context, and links to the underlying reporting.
4. Corroborate against the broader Pegasus Project coverage (Forbidden Stories, The Guardian, Washington Post, Amnesty's technical reports) before relying on it.
5. Pivot: the named suspected operator/country and associated people (`associate`) are leads; the person's inclusion frames their risk profile.

## Inputs → Outputs
- **In:** `name`
- **Out:** whether/how the person featured in the investigation, plus context and `associate`/actor links
- **Empty/negative result looks like:** name not present — the individual wasn't among those the consortium chose to profile; the leaked selection list was partial and not everyone was named publicly, so absence is not proof they were never targeted.

## Gotchas & OpSec
- It is a **snapshot investigation** (2021), not a maintained database — it won't reflect targeting before/after the leak or people the consortium didn't publish.
- "On the list" meant *selected as a potential target*; forensic confirmation of actual infection was established only for a subset — don't overstate a match.
- OpSec: passive; the topic is sensitive — corroborate and attribute carefully.

## Overlaps ("do both")
- Pairs with Amnesty International's Security Lab technical reporting and Forbidden Stories' Pegasus coverage — those provide the forensic/methodological backing behind a name in this interactive.

## Trust & verifiability
`trust: trusted` — a rigorously-reported consortium investigation (OCCRP/Forbidden Stories/Amnesty). Findings are well-corroborated, but read each entry precisely: selection ≠ confirmed infection, and the published list is a partial subset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-pegasus-project-occrp |
