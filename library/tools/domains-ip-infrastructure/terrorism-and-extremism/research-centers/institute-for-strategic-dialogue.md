---
id: institute-for-strategic-dialogue
name: Institute for Strategic Dialogue
description: Use when you're investigating extremism, hate, or disinformation and want authoritative research, actor/network analysis, and methodology from a leading think tank — a research/context source, not a per-target lookup.
url: https://www.isdglobal.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- terrorism-and-extremism
- research-centers
bestFor: Expert research and reports on extremism, hate movements, and online disinformation.
selectorsIn:
- name
selectorsOut:
- employer-org
- social-profile
status: live
pricing: free
costNote: Free public research and reports; no account required to read published work.
opsec: passive
opsecNote: Reading published research is passive and discloses nothing. If you follow ISD's methods to investigate live extremist spaces yourself, apply the usual OpSec (sock-puppet, isolated environment) at that stage — not here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-established, widely-cited think tank specialising in extremism and disinformation research; its reports are analytical and evidence-based.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ISD
- ISD Global
- isdglobal.org
tags:
- extremism-research
- disinformation
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Institute for Strategic Dialogue

> A leading think tank on extremism, hate, and disinformation — authoritative research, network analyses, and methods to inform (not replace) your own investigation.

## When to use
Context and methodology for extremism/disinformation cases, not person-finding. When you're investigating a movement, narrative, hate network, or influence operation, ISD's published reports provide expert analysis — how groups organise, which platforms/narratives they use, named organisations, and repeatable research methods. Use it to understand the landscape and to ground findings in credible research.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.isdglobal.org/.
2. Browse or search their research/reports by topic (extremism type, platform, region, disinformation campaign).
3. Read for analysis, named `employer-org`s/networks, platform/narrative patterns, and cited evidence.
4. Adopt their documented methodologies for your own investigation of the relevant spaces.
5. Pivot: named organisations/actors → corporate/social OSINT; platform/narrative leads → targeted SOCMINT collection.

## Inputs → Outputs
- **In:** a topic/movement/`name` to research
- **Out:** analytical reports naming `employer-org`s/networks and `social-profile`/platform patterns
- **Empty/negative result looks like:** no report on your specific target — ISD covers selected themes at a research level; it won't have a dossier on an individual, so use it for context, then investigate directly.

## Gotchas & OpSec
- **Research, not a database** — it provides analysis and named organisations/movements, not a searchable index of individuals.
- Reports are point-in-time; fast-moving spaces may have evolved since publication.
- Passive to read; any live investigation you launch from its methods needs its own OpSec.

## Overlaps ("do both")
- Complements primary-source SOCMINT collection and other extremism-research centres — ISD frames the landscape, your own collection and cross-org research fill in current specifics.

## Trust & verifiability
`trust: trusted` — a credible, widely-cited research institution; its analysis is authoritative as research, but corroborate any operational lead against primary sources before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | institute-for-strategic-dialogue |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name → employer-org, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
