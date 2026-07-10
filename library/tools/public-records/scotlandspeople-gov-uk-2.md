---
id: scotlandspeople-gov-uk-2
name: scotlandspeople.gov.uk
description: Use when you have a `name` and approximate date/place in Scotland and want official birth/marriage/death/census records to confirm identity and family links — returns `name`, `dob`, `address`, `associate` (parents/spouse).
url: https://www.scotlandspeople.gov.uk/order-certificate
category: public-records
path:
- public-records
bestFor: Authoritative Scottish statutory (BMD), census, and old parish records for identity confirmation and family-tree building.
selectorsIn:
- name
- dob
- address
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: freemium
costNote: Searching the indexes is free but viewing a record image costs pay-per-view credits (currently ~£1.50 each, sold in packs); ordering an official certificate costs £12. No subscription.
opsec: passive
opsecNote: Requires a free ScotlandsPeople account to view/purchase records, so activity is tied to your registered identity and payment card — use a dedicated research account, not a personal one. Queries do not touch the target; this is a records archive.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Scottish Government service run by National Records of Scotland (the statutory registrar); records are authoritative source documents.
missingPersonsRelevance: high
coverage:
- scotland
auth: account
api: false
localInstall: false
registration: true
aliases:
- ScotlandsPeople
- National Records of Scotland
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- birth-marriage-death
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# scotlandspeople.gov.uk

> The official Scottish Government genealogy archive — statutory birth/marriage/death, census, and parish records straight from National Records of Scotland.

## When to use
You have a `name` with an approximate date and place in Scotland and need authoritative records to confirm identity, establish `dob`, or map family relationships (parents, spouse, children). Ideal for anchoring a Scottish subject's genealogy or resolving a common-name ambiguity with a verified source document.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free (research) account at scotlandspeople.gov.uk and log in.
2. Choose the record type (statutory births 1855+, marriages, deaths; census 1841–1921; old parish registers; wills).
3. Search the free index by `name`, year range, and place; narrow common surnames with parents' names or mother's maiden name.
4. Buy pay-per-view credits to open the matching record image (or order a £12 certificate for an official copy).
5. Read out `dob`, place, parents/spouse (`associate`), and `address` details; pivot family names into further ScotlandsPeople searches or UK people-search tools.

## Inputs → Outputs
- **In:** `name` + approximate `dob`/year + place (`address`/parish)
- **Out:** `name`, `dob`, `address`, `associate` (parents, spouse, informant)
- **Empty/negative result looks like:** the free index returns no matching entries for the name/date/place — meaning no Scottish statutory record under those terms (check spelling variants and Soundex before concluding absence).

## Gotchas & OpSec
- Index search is free but seeing the actual record costs credits; budget accordingly.
- Scotland-only — English/Welsh events are on GRO/FreeBMD, not here.
- Account + card tie activity to you; use a dedicated research identity.
- Statutory records are closed for recent years (privacy windows), so very recent events may be unavailable.

## Overlaps ("do both")
- Pairs with `[[freecen-org-uk]]` (free UK census transcriptions) and English/Welsh BMD sources — ScotlandsPeople is authoritative for Scotland, while those cover the rest of Britain and cost nothing to view.

## Trust & verifiability
`trust: trusted` — operated by National Records of Scotland, the statutory registrar. Records are primary-source images, making this one of the most reliable genealogy sources for Scotland.
