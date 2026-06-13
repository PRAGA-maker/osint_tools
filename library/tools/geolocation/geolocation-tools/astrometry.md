---
id: astrometry
name: Astrometry
description: Use when a photo or video shows a clear night sky and you need to plate-solve the stars to recover where (and roughly when) it was taken or which direction the camera faced.
url: https://nova.astrometry.net/
category: geolocation
path:
- geolocation
- geolocation-tools
bestFor: Plate-solving an astronomical/night-sky image to recover sky coordinates, orientation, and field of view.
selectorsIn: [image]
selectorsOut: [geolocation, metadata-exif]
status: live
pricing: free
costNote: Free web service run by the Astrometry.net project; an API key (free, from your account) is needed only for programmatic use.
opsec: passive
opsecNote: You upload an image to a public astronomy service; no contact with the target. Uploaded images can be made public on the site by default, so set visibility to private and strip identifying EXIF first.
humanInLoop: true
humanInLoopReason: [account-login]
bestInteractionPattern: web-manual
trust: trusted
trustNote: Astrometry.net is a well-established, peer-reviewed academic plate-solving project widely used in astronomy; the math (star-pattern hashing) is robust and verifiable.
missingPersonsRelevance: low
coverage: [global]
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: [arcgis]
aliases: [nova-astrometry, astrometry-net]
tags: [astronomy, plate-solving, image-geolocation, chronolocation]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Astrometry

> A free academic plate-solving service: upload an image of the night sky and it identifies the stars to return precise sky coordinates (RA/Dec), camera orientation, and field of view.

## When to use
You have an `image` (or a video frame) containing recognizable stars or constellations and need to extract astrometric metadata. It does not give you a ground location by itself — it tells you which patch of sky the camera was pointing at. Combined with the apparent star positions and a timestamp, that supports chronolocation (estimating when) and constrains where on Earth the sky would look that way. A niche but occasionally decisive lead when conventional landmarks are absent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://nova.astrometry.net/ and sign in (a free account is needed to upload).
2. Choose "Upload" and submit your night-sky `image` (or a video still). Set the visibility to private and remove EXIF you don't want public before uploading.
3. Wait for the solver to run; it matches star patterns against its index.
4. Read the result: a sky position (RA/Dec), pixel scale, rotation/orientation, field-of-view size, and annotations of known stars/objects in the frame.
5. Pivot: combine the recovered sky direction + any timestamp in a planetarium tool (e.g. Stellarium) to reason about latitude/time; cross-reference visible terrain with `[[arcgis]]` map layers.

## Inputs -> Outputs
- **In:** `image` (night-sky photo or video frame)
- **Out:** `geolocation` (sky coordinates/orientation that constrain Earth location+time), `metadata-exif` (derived field-of-view/scale)
- **Empty/negative result looks like:** "no solution" — too few stars, heavy light pollution/cloud, motion blur, or too narrow/wide a field. Daytime, indoor, or starless images cannot be solved.

## Gotchas & OpSec
- Human-in-the-loop: requires login to upload; uploaded jobs can default to public — set private and strip EXIF so you don't leak the source image.
- It solves the *sky*, not the ground: the output is a direction, not a GPS fix. Turning that into a ground location/time needs a separate astronomy step.
- Needs genuine star detail; phone snapshots of a bright urban sky usually fail.

## Overlaps ("do both")
- Pairs with `[[arcgis]]` to overlay any terrain/horizon clues from the same image onto map layers once you have a candidate region.

## Trust & verifiability
`trust: trusted` — Astrometry.net is a mature, peer-reviewed academic tool with an open, reproducible method; a successful solve is independently checkable, so confidence is high when it returns a solution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | astrometry |
| category | geolocation |
| selectorsIn → selectorsOut | image → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
