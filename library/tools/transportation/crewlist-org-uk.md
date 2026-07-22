---
id: crewlist-org-uk
name: Crewlist.org.uk (CLIP)
description: Use when you have a `name` of a British merchant seafarer (c.1855–1950s) and want their crew-list records — returns ships served, dates and voyage details.
url: https://www.crewlist.org.uk/#Data
category: transportation
path:
- transportation
bestFor: Genealogical/historical tracing of British merchant navy seafarers via transcribed crew lists and ship records.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- dob
status: live
pricing: freemium
costNote: The site's own indexes and data are free to search; some fuller records are only available for sale via findmypast.
opsec: passive
opsecNote: A historical genealogical database of long-past records; you query names, not living targets. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The Crew List Index Project (CLIP), a long-running volunteer transcription effort; transcriptions can contain errors, so treat records as leads to confirm against original documents.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- CLIP
- Crew List Index Project
- crewlist.org.uk
tags:
- maritime
- genealogy
- crew-lists
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Crewlist.org.uk (CLIP)

> The Crew List Index Project — a volunteer database of ~1M transcribed British merchant-seafarer crew-list entries and 200k ships, mainly 1863–1913.

## When to use
You are tracing a British merchant seafarer from roughly the mid-19th to mid-20th century — a genealogical or historical missing-person/ancestry line — and have a `name`. CLIP lets you find which ships they served on, when, and voyage details, which can anchor a person to places and dates. Not for contemporary subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.crewlist.org.uk/#Data and pick a people database (e.g. "Seafarers names from crew lists", masters' indexes).
2. Search by surname/name; browse matches, mindful of spelling variants in old transcriptions.
3. Open a record for the ship, official number, dates and (sometimes) age/birthplace — useful for confirming a `dob`/origin.
4. Note that some fuller records are only for sale via findmypast; the CLIP indexes point you to them.
5. Pivot: a ship + date feeds ship-history and archive records (TNA), and a birthplace/age feeds general genealogy tools.

## Inputs → Outputs
- **In:** `name` (of a British merchant seafarer, c.1855–1950s)
- **Out:** ship(s) served, dates, voyage details; sometimes age/birthplace supporting `dob`/origin
- **Empty/negative result looks like:** no match — the person may pre/post-date coverage, be spelled differently, or not appear in transcribed lists; try variants and the pre-1860 TNA route.

## Gotchas & OpSec
- Coverage is time-bounded (mainly 1863–1913, shipping 1855–1950s) and UK merchant navy only.
- Volunteer transcriptions carry errors — confirm against original documents before relying on a record.
- Some data sits behind findmypast's paywall.

## Overlaps ("do both")
- Pairs with The National Archives (TNA) maritime records and general genealogy platforms (findmypast, Ancestry) to obtain the full documents CLIP indexes.

## Trust & verifiability
`trust: community` — a respected long-running volunteer project; treat transcribed entries as strong leads and verify decisive facts against the original crew lists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crewlist-org-uk |
