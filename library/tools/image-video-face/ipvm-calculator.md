---
id: ipvm-calculator
name: IPVM Calculator
description: Use when you have a `geolocation`/`address` of a surveillance camera and want to model its field of view and blind spots over satellite/street imagery — returns coverage `geolocation` analysis.
url: https://calculator.ipvm.com/
category: image-video-face
path:
- image-video-face
bestFor: Modeling a CCTV camera's field of view, range, and blind spots over Google Maps for geolocation and coverage verification.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free for non-members for small designs (up to ~4 cameras); the full feature set and larger projects require a paid IPVM membership.
opsec: passive
opsecNote: You model camera geometry over Google Maps/Street View — queries hit Google and IPVM, never the target site or camera, so it's passive. Creating an IPVM account to save designs ties activity to you; use a research account if you sign in.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: IPVM is the leading independent surveillance-industry research group; the calculator is their first-party tool with an authoritative database of real camera models and lens specs.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- IPVM Camera Calculator
- IPVM Design Calculator
tags:
- bellingcat-toolkit
- misc
- geolocation
- cctv
- camera
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# IPVM Calculator

> IPVM's first-party CCTV design tool: drop real camera models onto Google Maps and see exactly what field of view, range, and blind spots they'd produce.

## When to use
You're doing geolocation or chronolocation work involving surveillance cameras and want to reason about what a given camera could actually see. Given a camera's `geolocation`/`address` (or a candidate mounting point), you can model its cone of coverage over satellite and Street View imagery — to test whether a specific camera plausibly captured an event, to estimate a subject's position from footage, or to identify blind spots and likely camera placements around a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://calculator.ipvm.com/ — the basic calculator loads over Google Maps without a login.
2. Navigate the map to the location of interest and place a camera icon at the suspected mounting point.
3. Pick a camera model (thousands are in the database) or set focal length / sensor / resolution manually; the tool draws the field-of-view cone, range, and per-distance pixel density (image quality).
4. Rotate and reposition the camera; where Street View exists, the preview updates so you can compare modeled coverage against ground reality.
5. Read the coverage/blind-spot output and use it to confirm or reject a `geolocation` hypothesis for what a camera saw.
6. Pivot: combine with imagery from [[mapswitcher]]-style multi-provider views to verify the scene from other angles/dates.

## Inputs → Outputs
- **In:** `geolocation` / `address` of a camera position (plus a camera model or lens spec)
- **Out:** modeled field-of-view cone, range, pixel-density, and blind-spot `geolocation` analysis
- **Empty/negative result looks like:** a coverage cone that clearly does not reach the event location, or requires an implausible lens — evidence the hypothesized camera did not capture it.

## Gotchas & OpSec
- Human-in-the-loop: **partial paywall** — non-members are limited to small designs (about 4 cameras); bigger projects and some features need a paid IPVM membership.
- It models *geometry*, not the actual footage — a modeled sightline doesn't prove a camera exists or was recording.
- OpSec: passive; all queries go to Google/IPVM, nothing to the target. Sign in with a research account only if you need to save work.

## Overlaps ("do both")
- Pairs with multi-provider map tools like [[mapswitcher]] — the calculator reasons about camera geometry while those give you the surrounding imagery and angles to validate the scene.

## Trust & verifiability
`trust: trusted` — IPVM is the recognized independent authority on surveillance technology and the camera-spec database is first-party and authoritative; the coverage output is only as good as the position and model you input.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipvm-calculator |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
