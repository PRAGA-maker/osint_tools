---
id: pureref
name: PureRef
description: Use when you have a set of `image`s to compare — a lightweight desktop canvas for pinning, arranging, and zooming reference photos side by side during visual analysis and geolocation.
url: https://www.pureref.com/index.php
category: image-video-face
path:
- image-video-face
bestFor: Building a visual comparison board — arrange a target image next to candidate landmarks/faces/evidence shots on an infinite always-on-top canvas.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Pay-what-you-want desktop app (you can download it for free by entering 0); one-time optional payment, no subscription.
opsec: passive
opsecNote: Runs entirely offline on your machine — images you load never leave your computer, so it's safe for sensitive case imagery. The only risk is local: secure the saved .pur board like any evidence file.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Established, widely used tool (popular with digital artists, recommended in Bellingcat's toolkit for image work); it organises images you supply and makes no claims about them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- PureRef
tags:
- bellingcat-toolkit
- image-comparison
- misc
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# PureRef

> An infinite, always-on-top image canvas — drag in reference shots and arrange them so you can eyeball-compare a target image against candidates during geolocation or identity work.

## When to use
You have multiple `image`s to hold in view at once and compare detail-for-detail: a target photo beside candidate buildings/landmarks while geolocating, several avatars you suspect are the same person, or evidence frames you're sequencing. PureRef gives you a distraction-free board that floats over your other windows so you can flip between a map/search and your reference set without losing your arrangement. It's a *workspace*, not an analyzer — it finds nothing itself.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download PureRef from https://www.pureref.com (enter 0 to get it free) and install for Windows/macOS/Linux.
2. Drag in the images: the target shot plus every candidate/reference you're weighing.
3. Arrange and zoom — line up the target next to each candidate, crop to the diagnostic detail (a roofline, a sign, a scar), and annotate mentally as you rule options in/out.
4. Keep it **always-on-top** while you work another tool (Google Maps, reverse-image search) so comparisons stay in view.
5. Save the board as a `.pur` file with the case; export a flattened image for the report.

## Inputs → Outputs
- **In:** one or more `image`s
- **Out:** none as selectors — a saved visual comparison board (an analysis aid, not new data)
- **Empty/negative result looks like:** N/A; it's a canvas. The "result" is your own conclusion from the comparison, which must be justified with the visible evidence, not the tool.

## Gotchas & OpSec
- It **organises, it doesn't verify** — a side-by-side that "looks like a match" is a hypothesis; support any identification with concrete, described features.
- Fully offline, so safe for sensitive imagery; protect the saved board as evidence.
- Not a measurement tool — for precise pixel/shadow/measurement analysis use dedicated forensic/geolocation tooling.

## Overlaps ("do both")
- Complements reverse-image search and geolocation tools: those *find* candidate images/locations, PureRef is where you lay them beside the original to decide which holds up.

## Trust & verifiability
`trust: community` — a mature, widely trusted utility (in Bellingcat's toolkit); it makes no analytic claims of its own, so verifiability rests entirely on the images you bring and the reasoning you apply.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pureref |
| category | image-video-face |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
