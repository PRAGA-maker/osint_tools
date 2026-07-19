---
id: police-surveillance-in-chicago
name: Police Surveillance in Chicago
description: Use when you need to understand what surveillance technology Chicago police deploy (for counter-surveillance/context) — returns an educational, FOIA-based reference on tactics, not a searchable dataset.
url: https://redshiftzero.github.io/policesurveillance/
category: public-records
path:
- public-records
bestFor: Understanding the types of police surveillance tech used in Chicago, for counter-surveillance context.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free educational resource; no account. Note it's a static project last updated in 2021, so treat as historical context.
opsec: passive
opsecNote: Reading a static educational site is passive. Its value for an investigator is defensive — knowing that license-plate readers, cell-site simulators, gunshot detectors, biometric and social-media monitoring are in use informs your own counter-surveillance and OpSec when operating in that area. It contains no personal data on anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent FOIA-based research/education project; well-intentioned and sourced, but a 2021 snapshot — specifics may be outdated.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Chicago police surveillance
tags:
- public-records
- surveillance
- chicago
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Police Surveillance in Chicago

> A FOIA-based educational reference on the surveillance technologies Chicago police use — background for counter-surveillance and context, not a lookup tool.

## When to use
You want to understand the *surveillance landscape* in Chicago: which technologies (video cameras, automated license-plate readers, biometric databases, cell-site simulators/IMSI catchers, gunshot detection, social-media monitoring, predictive policing) are deployed and how. This is useful defensively — informing an investigator's own OpSec when working in the area — and as context for cases touching Chicago policing. It is not a database of camera locations or individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the project (https://redshiftzero.github.io/policesurveillance/ ; it redirects to redshiftzero.com/policesurveillance/).
2. Read through the seven documented surveillance tactics and their descriptions.
3. Use it to anticipate what data-collection you may encounter, and to shape counter-surveillance choices in the field.
4. Treat it as a 2021 snapshot — verify any specific capability against current FOIA releases or journalism before relying on it.
5. Pivot: not a data pivot — it's context that informs OpSec and framing, not a selector lookup.

## Inputs → Outputs
- **In:** none — it's an educational reference, not a query tool
- **Out:** none as a selector — descriptions of surveillance technologies/tactics
- **Empty/negative result looks like:** N/A; the content is fixed reference material, and being static/dated is its main limitation.

## Gotchas & OpSec
- Static and last updated 2021 — capabilities and vendors have likely changed; confirm current facts elsewhere. (Marked **degraded** for staleness.)
- Chicago-specific; don't generalize the specifics to other jurisdictions.
- OpSec: passive; its real use is *improving your own* counter-surveillance awareness, not collecting on a subject.

## Overlaps ("do both")
- Pairs with current investigative journalism and FOIA-document repositories on police tech, and with EFF's Atlas of Surveillance — those give up-to-date, location-level detail this static primer lacks.

## Trust & verifiability
`trust: community` — an independent, FOIA-sourced education project; credible but dated, so verify specific claims against current primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | police-surveillance-in-chicago |
| category | public-records |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
