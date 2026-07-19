---
id: street-clip
name: StreetCLIP
description: Use when you have an `image` and want a zero-shot guess of which country/region it was taken in — returns a ranked geolocation likelihood.
url: https://www.plugger.ai/models/street-clip
category: image-video-face
path:
- image-video-face
bestFor: Zero-shot country/region geolocation of an outdoor photo when you have no metadata to work from.
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The plugger.ai hosting starts at $15/mo with a free demo; the underlying StreetCLIP model (geolocal/StreetCLIP) is free and open on Hugging Face and can be run locally at no cost.
opsec: passive
opsecNote: You upload the target image to a third-party inference server (plugger.ai or Hugging Face), which sees the photo. For sensitive images, run the open model locally instead so nothing leaves your machine. No footprint reaches the image's subject either way.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: StreetCLIP is a published, peer-reviewed open geolocation model; plugger.ai is one commercial host of it. Predictions are probabilistic estimates, not proof of location.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- StreetCLIP geolocation
- geolocal/StreetCLIP
tags:
- Image Search and Identification
- Image Analyze
- geolocation
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# StreetCLIP

> An open zero-shot image-geolocation model: feed it an outdoor photo and a candidate country list, and it ranks how likely each is the location — no training, no metadata needed.

## When to use
You have an `image` (a street scene, landscape, building, sign) and no EXIF geotag, and you want a machine estimate of the country or region it was shot in. StreetCLIP compares the photo against a candidate list of place names and scores each — best as a first-pass narrowing step before manual [[GeoGuessr]]-style visual analysis or reverse image search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Easiest: run the free open model — load `geolocal/StreetCLIP` from Hugging Face (or the plugger.ai demo) in a Python/Transformers CLIP zero-shot pipeline.
2. Provide the photo plus a candidate list of country/region names (⚠️ tailor the list per image — a bad candidate set produces confident-but-wrong answers).
3. Read the ranked probabilities; the top score is a hypothesis, not a fact.
4. Pivot: take the predicted country and confirm with visual cues (signage language, road markings, vegetation, architecture) and reverse image search before trusting it.

## Inputs → Outputs
- **In:** `image` + a candidate list of place names
- **Out:** ranked `geolocation` likelihoods (country/region/city depending on your candidate list)
- **Empty/negative result looks like:** a flat/low-confidence distribution across candidates, or a high score on an obviously wrong candidate — the model always returns *something*, so a top-1 with no visual corroboration means "unknown," not "found."

## Gotchas & OpSec
- The output is only as good as your candidate list; you must supply and refine it per image (hence human-in-the-loop).
- Indoor shots, close-ups, and images without geographic cues yield noise.
- OpSec: hosted inference uploads the image to a third party — for sensitive material, run the open model locally.

## Overlaps ("do both")
- Pairs with reverse-image and GeoGuessr-style visual tools — StreetCLIP narrows the country, those pinpoint the spot.

## Trust & verifiability
`trust: community` — a published open research model with real geolocation skill, but its outputs are probabilistic estimates; always corroborate with independent visual evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | street-clip |
| category | image-video-face |
| selectorsIn → selectorsOut | image → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
