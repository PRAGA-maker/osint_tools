---
id: webcam-cse
name: WEBCAM CSE
description: Use when you have a place/`geolocation` and want a live street webcam there — returns webcam feeds from 10 online webcam catalogs via one Google Custom Search.
url: https://cipher387.github.io/webcamcse/
category: image-video-face
path:
- image-video-face
bestFor: One search box across 10 street-webcam directories to find a live public camera near a location of interest.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free; a static GitHub Pages page wrapping a Google Custom Search Engine. No account.
opsec: passive
opsecNote: You're searching public webcam directories via Google, not accessing anyone's private camera. Viewing the resulting public webcams is passive and legal; do not attempt to reach cameras that aren't intentionally public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built Google CSE by cipher387 (well-known OSINT curator); it only searches existing public webcam catalogs, so quality tracks those sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- webcamcse
tags:
- Maps, Geolocation and Transport
- Worldwide street webcams
- webcam
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# WEBCAM CSE

> A single Google Custom Search Engine that queries 10 public street-webcam catalogs at once — the fast way to find a live public camera near a place you're investigating.

## When to use
Your case has a `geolocation` — a last-known location, a place seen in a photo/video, a route — and you want current or recent visuals of that area from public street webcams (for weather/light corroboration, live monitoring of a public place, or verifying a scene). WEBCAM CSE saves you from checking each webcam directory separately.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/webcamcse/.
2. Search by place name, city, landmark, or keyword (e.g. "Times Square", a beach, a highway junction).
3. Browse the aggregated results, which link into public webcam catalogs (EarthCam, Windy webcams, etc.).
4. Open a promising camera to view its public live/recent feed; note its exact location and view direction.
5. Cross-reference the webcam view against a photo/video you're geolocating — matching signage, buildings, or angles confirms a location.
6. Pivot: a confirmed camera location → mapping/Street View for ground truth; live feed → monitoring a public place over time.

## Inputs → Outputs
- **In:** a `geolocation` / place keyword (or an `image` scene you're trying to match)
- **Out:** links to public street webcams near that place, with their live/recent `image` feeds and `geolocation`
- **Empty/negative result looks like:** no cameras indexed for that area — public webcams are dense in tourist/urban spots and sparse in rural/residential areas. Absence means no public camera is catalogued there, not that the place doesn't exist.

## Gotchas & OpSec
- Only finds intentionally-public webcams from mainstream catalogs; it is not a tool for reaching private or misconfigured cameras — don't try to, legally or ethically.
- Coverage is uneven and skews to landmarks; a residential street rarely has a public cam.
- As a Google CSE, result quality depends on Google's index and the underlying catalogs.
- OpSec: fully passive.

## Overlaps ("do both")
- Complements mapping/Street View geolocation — webcams give live/current conditions where Street View gives a fixed past capture; use both to place and time-check a scene.

## Trust & verifiability
`trust: community` — a curator-built search wrapper over public catalogs; the webcams themselves are the evidence, so verify a camera's stated location against the map before relying on its view.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webcam-cse |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, image → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
