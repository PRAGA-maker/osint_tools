---
id: the-weapons-id-database
name: The Weapons ID Database
description: Use when you have an `image` or `physical-description` of a firearm/ammunition and want to identify make, model and markings — returns weapon identification leads.
url: http://www.smallarmssurvey.org/weapons-and-markets/tools/weapons-id-database.html
category: public-records
path:
- public-records
bestFor: Identifying a small arm, light weapon or round of ammunition visible in a photo or described by a witness.
selectorsIn:
- image
- physical-description
selectorsOut:
- physical-description
- document-id
status: live
pricing: free
costNote: Free reference material published by the Small Arms Survey; downloadable as a full PDF or per-chapter, no account or payment required.
opsec: passive
opsecNote: You are reading a static reference document hosted by a research institute. No target-specific query is made, so there is nothing to leak; standard passive-browsing hygiene is sufficient.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the Small Arms Survey, a Geneva-based research project; authored by recognised arms-identification specialists (N.R. Jenzen-Jones, Matt Schroeder).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Small Arms Survey Weapons Identification Guide
- Weapons ID Handbook
tags:
- weapons
- arms-identification
- reference
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# The Weapons ID Database

> The Small Arms Survey's weapons-identification handbook: a reference for naming the firearm or ammunition you can see but can't identify.

## When to use
You have an `image` of a weapon (from a social-media photo, CCTV frame, or an item recovered near a scene) or a witness `physical-description`, and you need to turn "some kind of rifle" into a make/model, calibre, or marking that can anchor further records work. In a missing-persons or threat context, identifying a weapon in a subject's photos can corroborate location, affiliation, or timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and download the handbook (full PDF or the relevant chapter — identification, ammunition, or field data collection).
2. Compare your `image`/`physical-description` against the guide's identification features: overall silhouette, magazine type, stock, selector markings, headstamps on ammunition.
3. Read out the candidate make/model/calibre and any `document-id`-style markings (serials, headstamps, proof marks) the guide teaches you to locate.
4. Pivot: a confirmed model or headstamp feeds trace requests, arms-transfer databases, or corroboration of where/when a photo was taken.

## Inputs → Outputs
- **In:** `image` or `physical-description` of a weapon or round
- **Out:** `physical-description` (make/model/calibre) and `document-id` (markings/headstamps to look for)
- **Empty/negative result looks like:** the item isn't covered by the guide's examples, or the photo lacks the distinguishing features (obscured receiver, no visible markings) — treat as "not identified here," not as an exclusion.

## Gotchas & OpSec
- Human-in-the-loop: identification is a manual visual-comparison task; the handbook is a teaching tool, not an image-recognition engine.
- The authors state explicitly that no single guide covers every weapon — absence from the guide is not proof of anything.
- OpSec: fully passive; you are only reading a static document.

## Overlaps ("do both")
- Pairs with reverse-image and metadata tools (e.g. `[[fotoforensics]]`) — those tell you about the photo, while this tells you about the object inside it.

## Trust & verifiability
`trust: trusted` — first-party publication of the Small Arms Survey by named subject-matter experts; the identification methodology is authoritative even though it is a reference rather than a searchable database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-weapons-id-database |
| category | public-records |
| selectorsIn → selectorsOut | image, physical-description → physical-description, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
