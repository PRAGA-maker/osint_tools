---
id: wildme-and-wildbook
name: WildMe & WildBook
description: Use when you have a photo of an individual animal (whale fluke, shark, zebra, jaguar) and want to match it against a collaborative catalog to identify the specific animal and its prior sightings — returns image-match identity and geolocation history.
url: https://wildme.org/#/platforms/bass
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Re-identifying a specific wild animal from its markings across a shared sighting database.
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open-source (Wild Me is a nonprofit; Wildbook platforms are open to researchers/citizen scientists).
opsec: passive
opsecNote: You upload an animal photo to a conservation platform — not a person-tracking service. Standard sock-puppet/account hygiene applies if you register. Photos you upload may carry EXIF (including GPS) — strip metadata first if you don't intend to share the capture location.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Wild Me is an established conservation-tech nonprofit; Wildbook is its widely-used open-source platform relied on by wildlife researchers worldwide.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Wild Me
- Wildbook
tags:
- bellingcat-toolkit
- environment-wildlife
source: bellingcat-toolkit
lastVerified: '2026-08-05'
enrichment: full
---

# WildMe & WildBook

> Open-source computer-vision pattern recognition that identifies *individual* wild animals from their natural markings across a crowdsourced sighting catalog — a niche geospatial/environmental OSINT tool.

## When to use
Environmental and wildlife-crime investigations, not people-hunting. You have an `image` of a specific animal — a whale's fluke, a shark's markings, a zebra's stripes, a jaguar's rosettes — and want to know *which individual* it is and where/when it has been seen before. Wildbook matches the photo against its shared database and returns the animal's identity and sighting history, which builds a `geolocation` timeline useful for tracking trafficked or poached wildlife.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://wildme.org and pick the relevant Wildbook platform for your species.
2. Register/log in (an account is required to submit and view matches).
3. Upload your animal photo; the pattern-recognition engine proposes candidate matches from the catalog.
4. Confirm the individual and read its sighting records — locations, dates, contributing researchers.
5. Pivot: the sighting `geolocation`/date history feeds a movement timeline; contributing-observer metadata can corroborate where/when a photo was taken.

## Inputs → Outputs
- **In:** `image` of an individual animal
- **Out:** matched individual identity + `geolocation`/date sighting history
- **Empty/negative result looks like:** no confident match — either a new/uncatalogued individual, an unsupported species, or a photo too poor for the markings to be read.

## Gotchas & OpSec
- Species-specific: each Wildbook covers particular animals; use the right platform or you'll get nothing.
- Match quality depends heavily on photo angle/clarity of the identifying markings.
- Requires an account (human-in-the-loop login). Strip EXIF from photos you upload unless you intend to contribute the capture location.

## Overlaps ("do both")
- Complements general reverse-image search and mapping tools: Wildbook does the specialist animal-ID that generic engines can't, while mapping tools plot the resulting sighting timeline.

## Trust & verifiability
`trust: trusted` — Wild Me is an established conservation nonprofit and Wildbook is a peer-used, open-source research platform, so identity matches come with reviewable evidence and contributor provenance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wildme-and-wildbook |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
