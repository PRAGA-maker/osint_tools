---
id: open-source-munitions-portal
name: Open Source Munitions Portal
description: Use when you have an `image` of a weapon/munition from a conflict scene and want to identify it — search a verified reference library to match model, category and calibre.
url: https://osmp.ngo/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying munitions in conflict imagery by visual comparison against a verified, expert-reviewed reference archive.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free public research tool run by non-profits (Airwars + ARES); no payment. Some browsing may be behind bot protection but access is free.
opsec: passive
opsecNote: You compare your own image against a reference archive — you are not querying anyone about the subject, so it is passive. Handle the underlying conflict imagery responsibly (graphic content, source protection) rather than as an OpSec-against-target concern.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Airwars (civilian-harm watchdog) and Armament Research Services (ARES); images are expert-verified through multiple review rounds, though identifications are explicitly tentative, not definitive.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OSMP
- osmp.ngo
tags:
- maps-geospatial-data
- conflict
- munitions
- verification
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Open Source Munitions Portal

> A verified, expert-reviewed reference library of munitions imagery — the go-to for putting a name to a weapon or remnant seen in conflict footage.

## When to use
You have an `image` from a conflict zone — a strike remnant, unexploded ordnance, a weapon in a video frame — and need to identify what it is. OSMP holds 1000+ verified images of munitions, each tagged by taxonomies (model, category, use, colour, condition, calibre), so you can visually compare your source against confirmed examples. It's a core tool for conflict researchers and journalists documenting the bombing of civilians and attributing weapon types.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osmp.ngo/.
2. Browse or filter the library by the taxonomies that match your image — munition category, calibre, colour, condition, use.
3. Visually compare your source image against the verified reference photos to find the closest match.
4. Read the entry's identification and metadata, treating it as a **tentative** ID — OSMP is explicit that identifications are indicative, not exact.
5. Pivot: pair a candidate ID with the surrounding open-source evidence (geolocation, chronolocation of the footage) to build an incident record; corroborate with a munitions expert for anything you'll publish.

## Inputs → Outputs
- **In:** `image` (a munition/weapon to identify)
- **Out:** a reference `image` match with model/category/calibre taxonomy (a tentative identification)
- **Empty/negative result looks like:** no close visual match in the archive — the munition may be outside the collection's current scope, obscured, or a variant. Absence is not identification; escalate to expert review.

## Gotchas & OpSec
- Human-in-the-loop: yes — matching and confirming an ID is manual visual work, and identifications are deliberately tentative.
- OpSec: **passive** toward any subject. The real duty of care is around the imagery itself — graphic conflict content and protecting the sources who shared it.
- It is a *reference* archive (compare-against), not an automated reverse-image classifier; you do the matching.

## Overlaps ("do both")
- Pairs with geolocation/chronolocation workflows and reverse-image tools — OSMP answers "what is this weapon," while those establish where and when the footage was taken to complete an incident report.

## Trust & verifiability
`trust: trusted` — produced by Airwars and ARES with multi-round expert verification of every image. Note the project's own caveat: matches are tentative aids to identification, so confirm critical IDs with a specialist before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-source-munitions-portal |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
