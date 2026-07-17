---
id: open-benches
name: OpenBenches
description: Use when you have a `name` from a memorial-bench inscription and want its location — returns the bench `geolocation`, photo and full inscription text.
url: https://openbenches.org/
category: geolocation
path:
- geolocation
bestFor: Searching a worldwide crowdsourced map of memorial-bench inscriptions to place a name at a physical location.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to search and browse; open data (photos CC-licensed). No account needed to search.
opsec: passive
opsecNote: A public crowdsourced memorial database; searching contacts no one. Records commemorate (often deceased) individuals — handle with sensitivity, especially in bereavement/missing-persons contexts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Volunteer-contributed inscriptions and photos; content is user-submitted, so accuracy and completeness vary.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Open Benches
- openbenches.org
tags:
- Maps, Geolocation and Transport
- memorials
- crowdsourced
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# OpenBenches

> A crowdsourced world map of memorial benches — search the inscriptions and a `name` can resolve to a specific bench, its photo, and its exact coordinates.

## When to use
You have a `name` that may appear on a memorial/dedication bench (a deceased relative, a commemorated person, or a lead from a photo of a bench) and want to place it geographically. Each entry carries the full inscription, a photo, and precise `geolocation`. This is a niche but real pivot: it can confirm a death and its commemoration, tie a family to a locality (benches are usually near where the person lived or spent time), and provide a datable, located artifact. Also works in reverse — browse a map area to read who is memorialised there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://openbenches.org/ and use "Search inscriptions."
2. Enter the `name` (or a distinctive phrase from a known inscription).
3. Open a matching bench: read the full inscription, view the photo, and note its `geolocation` on the map.
4. For area-based work, pan/zoom the map to list benches near a place of interest.
5. Pivot: use the location to narrow a family's locality; combine inscription dates (birth/death) with obituary and cemetery searches to confirm identity.

## Inputs → Outputs
- **In:** `name` (or inscription phrase)
- **Out:** bench `geolocation` (coordinates + map), photo, full inscription text (often with dates)
- **Empty/negative result looks like:** no match — the person isn't commemorated on a bench that anyone has submitted. Coverage is crowdsourced and patchy, so absence means very little.

## Gotchas & OpSec
- OpSec: **passive** — public memorial data; nothing reaches anyone.
- Coverage is volunteer-driven and heavily skewed to the UK and English-speaking areas; most benches worldwide aren't logged.
- Sensitive context: entries commemorate the dead — treat findings with care in bereavement/missing-persons work.

## Overlaps ("do both")
- Pairs with cemetery/memorial databases (Find a Grave, BillionGraves) and obituary search — OpenBenches adds a precisely-located physical artifact; those give the fuller death/burial record.

## Trust & verifiability
`trust: community` — crowdsourced inscriptions and photos; a photo of the bench is decent evidence of the inscription, but verify the person's identity/dates against an authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-benches |
| category | geolocation |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
