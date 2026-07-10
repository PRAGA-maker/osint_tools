---
id: shutterstock
name: Shutterstock
description: Use when you have a profile `image` and want to check if it's actually a stock photo (catfish signal) — returns whether the picture is a licensed stock/model image.
url: https://www.shutterstock.com/
category: image-video-face
path:
- image-video-face
bestFor: Detecting that a profile/dating photo is a stock or model image (catfish/fake-account signal) and searching stock catalogs by keyword.
selectorsIn:
- image
- name
selectorsOut:
- metadata-exif
- image
status: live
pricing: freemium
costNote: Searching and previewing (watermarked) is free; licensing/downloading images is paid — but for OSINT you only need the free search to check whether a photo is stock.
opsec: passive
opsecNote: Searching Shutterstock (or reverse-searching an image against it) is passive and doesn't touch the subject. Use a clean session; you never need to buy anything to get the catfish signal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Shutterstock is a legitimate major stock-media marketplace; a match confirms an image is commercial stock (strong "not a real personal photo" signal), which is exactly its OSINT value.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-reverse-image-search
aliases:
- shutterstock.com
tags:
- toddington
- curated-directory
- stock-photo
- catfish-detection
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Shutterstock

> A major stock-photo marketplace — in OSINT its value is *catfish detection*: confirming that a suspiciously polished profile photo is actually a licensed stock/model image, not a real person's picture.

## When to use
You have a profile, dating, or social-media `image` that looks too professional, and you suspect the account is fake. If the picture is Shutterstock (or other) stock, the account is almost certainly a catfish/scam persona and the "person" in the photo is an uninvolved model. You can also search the catalog by `name`/keyword to see if a claimed "personal" photo is a themed stock shoot. This complements — it does not replace — a general reverse-image search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Run the suspect `image` through reverse-image engines first (`[[google-reverse-image-search]]`, Yandex, TinEye) — stock hits usually surface Shutterstock/iStock/Adobe Stock links directly.
2. To check Shutterstock specifically, use its on-site image search or search keywords describing the photo at https://www.shutterstock.com/.
3. If the photo appears as a watermarked stock asset with a contributor/model-release, treat the profile as fake.
4. Note the contributor and any series — scammers often reuse multiple shots of the same model.
5. Pivot: a confirmed stock photo redirects effort away from the fake persona toward the account's other selectors (username, phone, writing style).

## Inputs → Outputs
- **In:** `image` (or descriptive `name`/keywords)
- **Out:** `metadata-exif`-style verdict — "this image is licensed stock" (contributor/series info), and related stock `image`s
- **Empty/negative result looks like:** no stock match — the photo may be a genuine personal image (or stock from another library); a miss doesn't clear it, so check other stock sources too.

## Gotchas & OpSec
- It is **not** a face-recognition or people-search tool — it only tells you if an image is commercial stock.
- Reverse-image engines usually reveal a stock origin faster than browsing Shutterstock directly; use those first.
- OpSec: passive; no purchase needed for the catfish signal.

## Overlaps ("do both")
- Runs downstream of `[[google-reverse-image-search]]` — reverse-search flags a stock origin; Shutterstock confirms the source and contributor. Do both when vetting a suspected fake profile.

## Trust & verifiability
`trust: community` — a legitimate marketplace; a stock match is a high-confidence "fake photo" signal, but a non-match doesn't prove authenticity — corroborate across stock libraries and reverse-image tools.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shutterstock |
| category | image-video-face |
| selectorsIn → selectorsOut | image, name → metadata-exif, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
