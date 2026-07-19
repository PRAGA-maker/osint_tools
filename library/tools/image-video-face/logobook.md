---
id: logobook
name: Logobook
description: Use when you have an `image` with an unknown logo/emblem and want to identify the company/brand by its visual form — returns candidate brands via a shape-organised logo gallery, aiding geolocation.
url: http://www.logobook.com/
category: image-video-face
path:
- image-video-face
bestFor: Identifying an unknown logo in a photo by browsing a large gallery organised by visual shape/object, to name the brand and narrow location.
selectorsIn:
- image
selectorsOut:
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Free to browse the logo galleries by category; no account required for the reference use.
opsec: passive
opsecNote: Fully passive — you browse a static logo reference and compare visually; nothing is uploaded to a target and no one is queried about your subject. No sock puppet needed.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: A curated logo-design reference gallery (design-inspiration oriented), not a reverse-image engine — matching is manual and its coverage skews to notable/branded logos, so it won't catch every small local mark.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Logobook.com
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
- logo-identification
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Logobook

> A large logo gallery organised by visual form (shapes, objects, nature, sectors) — browse by what a mystery logo *looks like* to identify the brand behind it and narrow a photo's location.

## When to use
You are geolocating or analysing an `image` that contains a logo, emblem, or symbol you can't identify — on a sign, vehicle, uniform, or building. Because Logobook is indexed by visual characteristics (circles, waves, animals, letters, sector), you can browse to logos resembling the one in your photo, identify the company/brand, and use that to narrow the country/region or confirm an organisation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.logobook.com/.
2. Describe the mystery logo to yourself by its dominant visual form (a shape, an object, an animal, letters/numbers, or a business sector) and browse that category.
3. Scan the gallery for a match; open candidates to read the associated company/brand.
4. This is a manual visual match, not a reverse-image upload — you compare by eye.
5. Pivot: an identified `employer-org` narrows `geolocation` (where that brand operates) and feeds corporate/branch OSINT to pin the exact site.

## Inputs → Outputs
- **In:** `image` containing an unidentified logo/emblem
- **Out:** candidate `employer-org`/brand identity, and `geolocation` narrowing from where that brand operates
- **Empty/negative result looks like:** no visual match — the logo may be a small/local business, a non-notable mark, or too stylised; the gallery favours well-known/design-notable logos. Fall back to reverse-image search and text-in-logo OCR.

## Gotchas & OpSec
- Manual matching only — there's no image-upload search, so success depends on the logo being distinctive and in the gallery.
- Coverage skews to notable brands; local/obscure logos are often absent.
- OpSec: fully passive reference browsing.

## Overlaps ("do both")
- Pairs with reverse-image search engines and OCR tools — those catch logos with readable text or exact matches, while Logobook helps when you only have an abstract *shape* to go on.

## Trust & verifiability
`trust: unverified` — a curated design gallery, reliable for the brands it lists but not exhaustive; always confirm an identification against the brand's official assets before treating it as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | logobook |
| category | image-video-face |
| selectorsIn → selectorsOut | image → employer-org, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
