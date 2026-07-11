---
id: fold3-us-military-records
name: Fold3 (US Military Records)
description: Use when you have a `name` of a US veteran/service member (often historical) and want military records — returns service records, casualty/unit info, and historical images/documents.
url: http://www.fold3.com
category: people-search
path:
- people-search
bestFor: Researching a person's US military service history via digitized service, casualty, and unit records.
selectorsIn:
- name
selectorsOut:
- document-id
- associate
- image
status: live
pricing: freemium
costNote: Ancestry-owned; indexes are browsable but most record images sit behind a paid Fold3/Ancestry subscription (periodic free-access windows, e.g. around Veterans Day/Memorial Day).
opsec: passive
opsecNote: Searching an archival records site is passive and does not notify anyone. A subscription account ties queries to you — use a research account if separation matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Ancestry; records are digitized from official archives (NARA and others), so source documents are authoritative though indexing/transcription can contain errors.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Fold3
- Fold3 by Ancestry
tags:
- people-investigations
- military-records
- genealogy
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Fold3 (US Military Records)

> Ancestry's military-records archive: digitized US service, casualty, and unit records — strongest for historical (WWI/WWII-era) veterans.

## When to use
Your subject is (or a relative is) a US veteran or service member and you want their military footprint: enlistment/service records, casualty and POW lists, unit rosters, and period photographs/documents. Fold3's strength is historical depth — it's a genealogy/records archive more than a live locator — so it's best for older cases, corroborating family history, or building context on a named service member.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.fold3.com and search by `name` (add war/era, service branch, or state to narrow).
2. Scan the indexed hits across collections (service records, casualty lists, unit histories, photos).
3. Open a record — the index is often visible free, but the document image typically requires a Fold3/Ancestry subscription (watch for free-access windows around military holidays).
4. Pivot: a service `document-id` and unit anchor identity and timeline; named comrades are `associate` leads; a period `image` feeds face/photo comparison; a home-of-record ties to a place.

## Inputs → Outputs
- **In:** `name` (+ era/branch/state)
- **Out:** service records / `document-id`, unit and casualty info, `associate`s (comrades/unit), historical `image`s
- **Empty/negative result looks like:** no matching record — common for very recent service members (modern records are restricted/privacy-protected) or name-spelling variants. Absence skews by era: Fold3 is deep on historical conflicts, thin on living/recent personnel.

## Gotchas & OpSec
- Paywall: indexes tease, images charge — budget for a subscription or use free-access windows.
- Best for historical service; recent/living personnel records are largely restricted by privacy law and won't appear.
- Transcription/index errors happen — read the source image, and try spelling variants.
- OpSec: **passive**; archival search notifies no one.

## Overlaps ("do both")
- Pairs with the National Archives (NARA), the VA's gravesite/BIRLS data, and Ancestry proper — Fold3 digitizes many NARA holdings, but cross-checking NARA and VA sources fills gaps and confirms details.

## Trust & verifiability
`trust: trusted` — records derive from official archives, so the source documents are authoritative; treat Fold3's indexed transcriptions as pointers and verify against the imaged original.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fold3-us-military-records |
| category | people-search |
| selectorsIn → selectorsOut | name → document-id, associate, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
