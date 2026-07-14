---
id: forceswarrecords-com
name: Forces War Records
description: Use when you have a `name` of someone who served in the UK/Commonwealth military and want their service history — returns military `document-id` records with regiment/unit (`employer-org`), rank, `dob` and next-of-kin `associate` links.
url: https://uk.forceswarrecords.com/
category: public-records
path:
- public-records
bestFor: Tracing a person's UK/Commonwealth military service history (regiment, rank, medals, casualty records) from a name for genealogy and identity work.
selectorsIn:
- name
selectorsOut:
- name
- dob
- employer-org
- associate
status: live
pricing: freemium
costNote: Name index is searchable free, but viewing full transcribed/original records requires a paid subscription (a genealogy site, now part of the Ancestry group).
opsec: passive
opsecNote: A read-only historical-records search; no living subject is contacted or notified. You create an account to subscribe, which ties activity to that login — use a research account for sensitive work.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial military-genealogy database of transcribed and scanned records; transcription errors happen, so treat individual fields as leads to confirm against the original scan.
missingPersonsRelevance: high
coverage:
- uk
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- forceswarrecords.com
- Forces War Records
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- military
- uk
- genealogy
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Forces War Records

> A large UK/Commonwealth military-records database — turns a service member's name into regiment, rank, medals and casualty records for genealogy and identity tracing.

## When to use
You have a `name` and evidence the person (or their ancestor) served in the British or Commonwealth armed forces, and you want to establish service history: unit/regiment, rank, service number, medals, and casualty/next-of-kin details. This is most useful for historical/genealogical tracing (WWI, WWII, and earlier) and for corroborating a claimed military background.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://uk.forceswarrecords.com/ and use the records search.
2. Enter the subject's name (add birth year, regiment, or service number to narrow).
3. Free search returns index hits; open a record and subscribe to view the full transcription/scan.
4. Read the record: unit (`employer-org`), rank, service number (`document-id`), `dob`, and next-of-kin (`associate`).
5. Pivot: next-of-kin names feed family-tree/associate mapping; a service number and unit feed other military and archive sources.

## Inputs → Outputs
- **In:** `name` (+ optional birth year / regiment / service number)
- **Out:** military service `document-id`, unit/regiment (`employer-org`), rank, `dob`, next-of-kin `associate`
- **Empty/negative result looks like:** no index match — the person may not appear in the digitised collections (coverage is broad but not total), or the name is spelled differently in the original record; try variants.

## Gotchas & OpSec
- Human-in-the-loop: the free tier only shows index hits — full records are behind a subscription paywall.
- Transcriptions can contain errors; verify names/dates against the original scanned image where available.
- OpSec: passive; historical records, no living-subject contact.

## Overlaps ("do both")
- Pairs with national archives and genealogy registries (births/deaths/marriages) — Forces War Records supplies the service dimension, while civil registers anchor identity and family.

## Trust & verifiability
`trust: community` — a commercial genealogy database; authoritative-ish because it digitises official records, but confirm load-bearing fields against the source image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forceswarrecords-com |
