---
id: fastscanner-app-mobile-android
name: Fastscanner App (Mobile – Android)
description: Use when you need to digitise a physical document or photo into a clean PDF/image in the field — turns a phone camera into a scanner producing a file you can then OCR or store as evidence (no subject selectors).
url: https://play.google.com/store/apps/details?id=com.coolmobilesolution.fastscannerfree
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Capturing a physical document, notice, or photo as a de-skewed, cropped PDF/image for the case file when you only have a phone.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free version scans to PDF with ads and basic features; a Pro upgrade removes ads and adds batch/OCR extras.
opsec: passive
opsecNote: Scanning happens locally on the device, but the app can upload/share scans to cloud services — keep sensitive evidence local and disable auto-sync. As with any consumer scanner app, review its permissions before using it on case material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: unverified
trustNote: A common third-party consumer scanner app; fine for digitisation, but it is not evidence-grade software — document provenance yourself.
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
- Fast Scanner
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- evidence-capture
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Fastscanner App (Mobile – Android)

> A phone-camera document scanner — capture a physical page or photo, auto-crop and de-skew it, and export a clean PDF for the case file when you're away from a desk.

## When to use
Investigator tooling, not a lookup: it yields no selectors, it *captures* them. Use it in the field to digitise something physical — a notice on a door, a document handed to you, a photo, a whiteboard — into a legible PDF/image you can then run OCR on, extract text/metadata from, or attach to the file. It's the "get the paper into the case" step.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Fast Scanner from Google Play on the device.
2. Photograph the document; let the app detect edges, crop, de-skew, and enhance contrast.
3. Add multiple pages if needed and export as a single PDF (or image).
4. Save/transfer the file **locally** to your case store; note what it is, when and where you captured it.
5. Downstream: run OCR to make it searchable, or a metadata/EXIF tool on the exported image.

## Inputs → Outputs
- **In:** none (a capture utility — you point the camera at a physical item)
- **Out:** none as selectors — produces a PDF/image artifact
- **Empty/negative result looks like:** N/A; the failure mode is a blurry/cropped-wrong scan — re-shoot with better light and framing before relying on OCR.

## Gotchas & OpSec
- Scanning is local, but the app offers cloud upload/share — **keep sensitive scans off third-party clouds** and check app permissions.
- Consumer scanner output is not tamper-proof evidence; record provenance (source, time, who scanned) alongside it.
- Interchangeable with any reputable scanner app; pick one that matches your data-handling policy.

## Overlaps ("do both")
- Feeds OCR and document-metadata tooling: Fast Scanner produces the clean image, those tools pull the text and embedded metadata out of it.

## Trust & verifiability
`trust: unverified` — a generic third-party consumer app; adequate for digitisation, but treat its output as an investigator-made artifact whose provenance you must document.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fastscanner-app-mobile-android |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
