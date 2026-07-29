---
id: atlos
name: Atlos
description: Use when you run a large, multi-investigator open-source investigation and need a platform to organise, geolocate, and verify `image`/video evidence collaboratively — a case-management workspace, not a lookup.
url: https://www.atlos.org/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Collaborative case management and evidence verification for large-scale visual OSINT investigations.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free and open-source (self-hostable); the hosted platform is free for many investigations, with support/enterprise options.
opsec: passive
opsecNote: A workspace for organising evidence you have already collected — it does not query targets. But you are uploading sensitive case material to a shared platform: manage access carefully, and self-host if the material demands it. Preserve originals/hashes outside the platform too.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Purpose-built for human-rights/OSINT investigations (featured in Bellingcat's toolkit), open-source and used by established investigative teams.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- ATLOS
tags:
- bellingcat-toolkit
- data-organization-analysis
- evidence-management
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Atlos

> A purpose-built platform for collaborative, large-scale open-source investigations — organise incidents, catalogue and geolocate visual evidence, track verification status, and coordinate a team in one workspace.

## When to use
You are running an investigation with many pieces of visual evidence (photos/videos of incidents, locations, events) and/or several collaborators, and need structure: a place to log each item, record its geolocation and verification state, avoid duplicated work, and preserve provenance. For a missing-persons context, it can organise sighting imagery and location leads across a team.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://www.atlos.org/ (or self-host the open-source platform for sensitive cases).
2. Create a project/incident and add evidence items (`image`/video), with source URLs and timestamps.
3. Geolocate items, tag them, and set verification status; assign items to collaborators.
4. Use the map/incident views to see spatial and temporal patterns across the evidence.
5. Pivot: confirmed `geolocation`s feed mapping/geolocation tools; catalogued imagery feeds reverse-image and metadata analysis.

## Inputs → Outputs
- **In:** `image`/video evidence and candidate `geolocation`s
- **Out:** an organised, geolocated, verification-tracked case record (confirmed `geolocation`, provenance)
- **Empty/negative result looks like:** N/A as a query — its "output" is the structured case; value depends on what your team enters.

## Gotchas & OpSec
- Human-in-the-loop: account/login and team setup required (`account-login`).
- It manages evidence, it does not find it — pair with collection tools.
- OpSec: **passive**, but you centralise sensitive material — control access and self-host when warranted; keep hashed originals offline.

## Overlaps ("do both")
- Feeds and is fed by geolocation, reverse-image, and metadata tools; Atlos is the organising layer around them, not a replacement.

## Trust & verifiability
`trust: trusted` — open-source, investigation-purpose platform used by established teams and listed in Bellingcat's toolkit; provenance/verification tracking is a core feature, not an afterthought.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | atlos |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
