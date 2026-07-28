---
id: smart-ruler
name: Smart Ruler
description: Use when you have an on-screen `image`/web element and want to measure pixel distances, angles, and dimensions — a measurement aid for image analysis; no personal selectors out.
url: https://chromewebstore.google.com/detail/smart-ruler/npgpdlfoflcfcohplcdclmocfemgpdga
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: On-screen pixel/angle measurement for image analysis (shadow lengths, relative dimensions, alignment).
selectorsIn:
- image
selectorsOut: []
status: live
pricing: freemium
costNote: Free Chrome extension (~200k users); optional premium features. No account for basic measuring.
opsec: passive
opsecNote: The extension measures pixels rendered in your own browser — it makes no network request about the target and nothing is sent anywhere. Fully passive; the only footprint is your own visit to whatever page/image you open.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A general-purpose web design/measurement extension (not an OSINT-specific tool). It measures faithfully what's on screen; any investigative inference (e.g. shadow-based geolocation) is yours to make and verify.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- suncalc
- google-earth-pro
tags:
- Domain/IP/Links
- Website analyze
- image-analysis
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Smart Ruler

> A browser screen-ruler extension — for measuring pixel distances, angles, and proportions directly on an image or page, e.g. when doing shadow analysis or comparing dimensions during geolocation.

## When to use
You're analysing an `image` on screen and need measurements: the length/angle of a shadow (to reason about time/latitude with a sun-position tool), the relative height of two objects, sign/window proportions to match a candidate building, or pixel alignment. Smart Ruler overlays a measuring tool on whatever is rendered. It outputs measurements, not personal selectors.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension and open the image/page at a known, fixed zoom (record the zoom — measurements are pixel-relative).
2. Activate the ruler and drag to measure distances; use the angle mode for shadow/edge angles.
3. Record ratios rather than absolute pixels when comparing across images (ratios survive scaling; raw pixels don't).
4. Feed measurements into the actual analysis — e.g. shadow angle + date into a sun-position calculator, or proportions into a building match.
5. Pivot: shadow angle → `[[suncalc]]` for time/orientation; matched proportions → confirm the location in `[[google-earth-pro]]`.

## Inputs → Outputs
- **In:** an on-screen `image`/element
- **Out:** pixel distances, angles, and ratios (measurement data, no selectors)
- **Empty/negative result looks like:** n/a — it always measures what's shown; the risk is *meaningless* numbers if zoom/scale isn't controlled, not a null result.

## Gotchas & OpSec
- **Scale discipline:** on-screen pixels depend on zoom and image resolution. Fix the zoom, and prefer ratios/angles over absolute pixels when comparing images.
- It measures the rendered image, which may already be resized/cropped from the original — measure the highest-resolution source you have.
- Fully passive; it's a general design tool, so the OSINT value is entirely in how you apply the numbers.

## Overlaps ("do both")
- Feeds `[[suncalc]]` for shadow-based time/orientation and `[[google-earth-pro]]` for confirming a measured match against real geometry — Smart Ruler produces the numbers, those tools interpret them.

## Trust & verifiability
`trust: community` — a general-purpose measurement extension, reliable at what it does (measuring screen pixels). Every investigative conclusion drawn from a measurement must be independently checked against controlled references.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | smart-ruler |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | image → (measurements) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
