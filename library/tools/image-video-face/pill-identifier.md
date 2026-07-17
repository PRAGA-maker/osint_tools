---
id: pill-identifier
name: WebMD Pill Identifier
description: Use when you have a `physical-description` of a pill (colour, shape, imprint) or an `image` of one and want to identify the medication — returns the drug name (no person selectors).
url: https://www.webmd.com/pill-identification/default.htm
category: image-video-face
path:
- image-video-face
bestFor: Identifying an unknown pill from its colour, shape, and imprint code — useful when medication is found among a subject's effects or at a scene.
selectorsIn:
- physical-description
- image
selectorsOut: []
status: live
pricing: free
costNote: Free WebMD tool; no account or payment. Ad-supported.
opsec: passive
opsecNote: A reference lookup — you query WebMD's drug database, not any person. Nothing reaches a subject. Do not upload identifiable case photos to a commercial site; describe the pill (colour/shape/imprint) rather than uploading scene imagery.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: WebMD's pill identifier is built on a licensed pharmaceutical database (US drug imprints); authoritative for US-marketed medications.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- webmd-medical-sciences-search
aliases:
- WebMD pill ID
- pill imprint lookup
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# WebMD Pill Identifier

> WebMD's imprint-based pill identifier — turns a pill's colour, shape and imprint code into a named medication, a small but useful forensic aid when unknown pills turn up in an investigation.

## When to use
You have a `physical-description` of a tablet/capsule (colour, shape, and the imprint stamped on it) — or an `image` you can read the imprint from — and need to know what drug it is. In a missing-persons context, medication found among a subject's belongings can indicate a health condition, a prescribing doctor, or a pharmacy to follow up, and helps assess urgency and welfare.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the pill identifier page.
2. Enter the imprint code (letters/numbers on the pill), then select the colour and shape from the dropdowns.
3. Submit to get candidate matches, each with the drug name, strength, and manufacturer.
4. Confirm by comparing the pictured pill to the WebMD image and imprint.
5. Pivot: a named prescription drug can point to a condition, a treating clinician, or a pharmacy — investigative leads to pursue through proper channels.

## Inputs → Outputs
- **In:** `physical-description` (colour + shape + imprint) or `image` to read the imprint from
- **Out:** medication name(s), strength, and manufacturer — a substance identification, not a person selector.
- **Empty/negative result looks like:** no match — the pill may be non-US, a supplement, a compounded/illicit product, or the imprint was misread; try alternate imprint characters or a second identifier (e.g. Drugs.com).

## Gotchas & OpSec
- Coverage is US-marketed prescription/OTC drugs; foreign, veterinary, illicit, or unmarked pills often won't match.
- Imprints are easily misread (0/O, 1/I, worn stamps) — try variants.
- Ethics/OpSec: passive lookup, but treat any medical inference cautiously and lawfully; never diagnose. Don't upload identifiable case photos to a commercial site.

## Overlaps ("do both")
- Pairs with `[[webmd-medical-sciences-search]]` — identify the pill here, then research the drug/condition there. Cross-check the ID against another identifier (Drugs.com) for confidence.

## Trust & verifiability
`trust: trusted` — backed by a licensed US pharmaceutical imprint database; identifications are reliable for US medications and independently verifiable against the manufacturer's imprint.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pill-identifier |
| category | image-video-face |
| selectorsIn → selectorsOut | physical-description, image → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
