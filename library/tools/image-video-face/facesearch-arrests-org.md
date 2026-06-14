---
id: facesearch-arrests-org
name: facesearch.arrests.org
description: Use when you have a face photo and want to check it against US arrest/booking (mugshot) records aggregated by Arrests.org.
url: https://facesearch.arrests.org/
category: image-video-face
path:
- image-video-face
bestFor: Reverse face search against a US mugshot / arrest-record corpus.
selectorsIn:
- image
- face
selectorsOut:
- name
- dob
- address
- document-id
status: unknown
pricing: freemium
costNote: Arrests.org surfaces free record previews but typically funnels to paid background-report partners for full details.
opsec: active
opsecNote: Uploading a face to a commercial records broker is active collection and may be logged; the operator may retain the query image. Use a sock puppet.
humanInLoop: true
humanInLoopReason:
- captcha
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Arrests.org is a known US mugshot/arrest-record aggregator; the face-search subdomain's matching quality and current status are not independently verified. Records can be stale or misattributed.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Arrests.org Face Search
tags:
- reverseimagesearching
- mugshot
- arrest-records
source: uk-osint
lastVerified: ''
enrichment: full
---

# facesearch.arrests.org

> Face-search front end over Arrests.org's US mugshot/arrest-record aggregation.

## When to use
You have an `image`/`face` of a missing person (or unidentified individual) who may have a US arrest history, and you want to match it to a booking photo to recover a `name`, `dob`, charges, or jurisdiction. Useful when someone has gone off-grid and may have been arrested or jailed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://facesearch.arrests.org/.
2. Upload a clear, front-facing `face` crop.
3. Review ranked mugshot candidates; click through to the underlying arrest record for `name`/`dob`/jurisdiction.
4. Full details often route to a paid background-report partner.
5. Pivot: take the recovered `name`/`dob` into people-search and corrections/inmate-locator tools to confirm current status and location.

## Inputs → Outputs
- **In:** `image` / `face`
- **Out:** `name`, `dob`, `address` (record jurisdiction), `document-id` (booking/case identifiers).
- **Empty/negative result looks like:** no candidate mugshots, or low-similarity matches with inconsistent identities — means no arrest record indexed, not that the person is "clear".

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA likely; full records behind a paywall partner.
- OpSec: **active** — you are querying a commercial broker; the upload and query may be retained. Mugshot data is often outdated, misspelled, or expunged-but-still-listed; verify against an authoritative source.

## Overlaps ("do both")
- Pairs with general face engines (`[[facecheck-facial-recognition-search]]`, `[[pimeyes]]`) which index the open web rather than booking photos; run both to cover criminal-record and social-media surfaces.

## Trust & verifiability
`trust: unverified` — Arrests.org is a recognized US arrest-record aggregator, but its face-matching accuracy and data freshness are uncontrolled; treat any hit as a lead requiring corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facesearch-arrests-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → name, dob, address, document-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
