---
id: csis-warfare-irregular-threats-and-terrorism-program
name: CSIS Warfare, Irregular Threats, and Terrorism Program
description: Use when you need authoritative analysis or datasets on terrorism, extremist networks, and irregular warfare — returns reports, podcasts, and a US terrorism-incidents dataset.
url: https://www.csis.org/programs/warfare-irregular-threats-and-terrorism-program
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- terrorism-and-extremism
- research-centers
bestFor: Vetted think-tank research and structured datasets on terrorism, extremist groups, and state/non-state irregular threats.
selectorsIn: []
selectorsOut:
- employer-org
status: live
pricing: free
costNote: All program articles, reports, podcasts, and datasets are published free on csis.org; no account required.
opsec: passive
opsecNote: Reading a public think-tank site; no target is queried and nothing is submitted. Only your own browsing (IP/referrer) is visible to CSIS — standard web hygiene applies, nothing about a subject is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Center for Strategic and International Studies is an established, non-partisan Washington DC research institution; the WITT program is led by named academics (Dr. Daniel Byman) and publishes sourced, editorially reviewed analysis and datasets.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- CSIS WITT Program
- Warfare, Irregular Threats, and Terrorism Program
tags:
- terrorism
- research-center
- threat-analysis
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# CSIS Warfare, Irregular Threats, and Terrorism Program

> A major think-tank research program publishing vetted analysis and structured datasets on terrorism, extremist networks, and irregular/hybrid warfare — background and context, not a live selector lookup.

## When to use
You need authoritative context on a terrorist or extremist organization, a state actor's irregular-warfare tactics (covert action, disinformation, cyber), or trends in political violence, and want sourced analysis rather than raw social chatter. It is a reference/background layer: use it to understand the groups, actors, and datasets behind a case, not to resolve a person's identity or location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the program page at https://www.csis.org/programs/warfare-irregular-threats-and-terrorism-program.
2. Browse the output — 100+ articles, 80+ reports, 80+ podcast episodes — filterable by topic (specific groups, regions, or threat types).
3. For structured data, open the program's specialized datasets (e.g. the U.S. Terrorism Incidents Dataset) for incident-level records.
4. Pivot: a named organization (`employer-org`) or incident from a report feeds targeted news/court-record searches; a dataset record gives dates/locations to corroborate elsewhere.

## Inputs → Outputs
- **In:** none — you browse/search a research library, not query a selector
- **Out:** analytical reports, podcasts, and incident datasets; named organizations (`employer-org`) and events to pivot on
- **Empty/negative result looks like:** a topic simply not covered by the program's publications — absence here says nothing about the subject, only that CSIS has not written on it.

## Gotchas & OpSec
- Human-in-the-loop: none; read and download freely.
- Scope: strategic/analytical, US-and-adversary-state focused; it explains threat landscapes, it does not do people-search — treat findings as context, not identifiers.
- OpSec: fully passive; no subject is touched.

## Overlaps ("do both")
- Pairs with primary-source terror/sanctions databases and court records — CSIS gives the vetted narrative and datasets; those give the authoritative individual records to confirm names and events.

## Trust & verifiability
`trust: trusted` — an established non-partisan research institution with named authors and editorial review; its analysis and datasets are citable, though (as with any think tank) read them as expert interpretation, and confirm specific facts against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | csis-warfare-irregular-threats-and-terrorism-program |
