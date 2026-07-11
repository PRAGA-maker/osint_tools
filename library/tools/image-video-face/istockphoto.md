---
id: istockphoto
name: iStock (by Getty Images)
description: Use when you suspect a profile `image` is a stock/model photo and want to check it against a major royalty-free catalog — returns matching stock images (evidence the photo is not a real person's).
url: http://www.istockphoto.com
category: image-video-face
path:
- image-video-face
bestFor: Confirming that a suspected fake-profile or catfish photo is a licensed stock image by finding it in the iStock/Getty catalog.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: freemium
costNote: Browsing and searching the (watermarked-preview) catalog is free; actually licensing/downloading an image requires payment. For OSINT you only need the free search/preview to confirm a match.
opsec: passive
opsecNote: Browsing the catalog is passive and reveals nothing to any subject. iStock has no native reverse-image upload, so you typically arrive here from a reverse-image engine — keep that upstream search on a clean/sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: iStock is Getty Images' royalty-free stock marketplace — a first-party, reputable catalog; the limitation is coverage (it only helps for images that are actually Getty/iStock stock), not authenticity.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- iStock
- istockphoto.com
- iStock by Getty Images
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- stock-photo
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# iStock (by Getty Images)

> Getty's royalty-free stock-image marketplace — in OSINT, a catalog to check when you suspect a profile picture is a paid stock/model photo rather than a real person.

## When to use
You have a profile `image` from a suspected fake account, romance-scam persona, or catfish, and you want to prove the photo is generic stock rather than the account holder. iStock is one of the largest stock catalogs (Getty), so a suspect photo that turns out to be iStock stock is strong evidence the profile is fabricated. This is a corroboration step, not a person-finder — its direct missing-persons value is limited to unmasking fake imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. First run the suspect `image` through a reverse-image engine (Google Images, TinEye, Yandex). If a result points to istockphoto.com, follow it.
2. On iStock, confirm the match by comparing the licensed image to your suspect photo (same model, pose, background).
3. Alternatively, search by keywords describing the photo (e.g. "smiling businessman headshot") to see whether near-identical stock exists — a sign the persona used a stock look.
4. Note the image title/ID; the watermarked free preview is enough to document the match.
5. Pivot: a confirmed stock photo lets you discount the profile's imagery and refocus on other selectors (username, phone, writing style).

## Inputs → Outputs
- **In:** `image` (a suspected stock/profile photo)
- **Out:** matching stock `image`(s) in the iStock/Getty catalog (confirming the photo is not a candid of a real subject)
- **Empty/negative result looks like:** no match — the image is not iStock stock; it may be a genuine photo, or stock from a different library (Shutterstock, Adobe Stock, Unsplash), so check those too before concluding it's authentic.

## Gotchas & OpSec
- No native reverse search: iStock cannot take an uploaded photo — you must arrive via an external reverse-image engine or keyword-match manually.
- Scope: only catches Getty/iStock stock; a fake using another library will not appear here.
- OpSec: passive; do the reverse-image step from a clean session.

## Overlaps ("do both")
- Pairs with `[[tineye]]` and `[[yandex-images]]` — those do the actual reverse-image matching; iStock confirms and identifies the specific stock listing.
- Pairs with `[[pimeyes]]` — PimEyes tells you if the face appears on real people's accounts; iStock tells you if it's a manufactured stock face.

## Trust & verifiability
`trust: trusted` — a first-party Getty catalog, so a match is authoritative proof the image is licensed stock; the limitation is coverage (Getty only), not reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | istockphoto |
