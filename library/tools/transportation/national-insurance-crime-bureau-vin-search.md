---
id: national-insurance-crime-bureau-vin-search
name: NICB VINCheck
description: Use when you have a `vin` and want to know if the vehicle was reported stolen (and not recovered) or declared a salvage/total loss — returns theft and salvage flags from participating U.S. insurers.
url: https://www.nicb.org/theft_and_fraud_awareness/vincheck
category: transportation
path:
- transportation
bestFor: Free U.S. VIN check for outstanding theft records and salvage/total-loss history from insurer data.
selectorsIn:
- vin
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free public service from the National Insurance Crime Bureau; limited to a small number of searches per day per user (anti-abuse cap).
opsec: passive
opsecNote: You query NICB's database about a VIN, not the owner; nothing is disclosed to any vehicle owner. A CAPTCHA gates each lookup. Passive.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the NICB, a not-for-profit backed by U.S. insurers; theft/salvage flags come from participating insurance-company data, so it is authoritative for what those insurers report (not a complete national record).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NICB VINCheck
- VINCheck
tags:
- transportation
- vehicles
- vin
- theft
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- vincheck
---

# NICB VINCheck

> The National Insurance Crime Bureau's free VIN lookup — flags whether a U.S. vehicle has an outstanding theft report or a salvage/total-loss record in participating-insurer data. A quick integrity check on a vehicle tied to a subject.

## When to use
You have a `vin` (from a title, a photo of a dashboard/door-jamb plate, or a paper trail) and want to know if the vehicle is flagged as stolen-and-unrecovered or as a salvage/total loss. Useful when a subject's vehicle history matters: verifying a car isn't stolen, spotting a hidden salvage title behind a "clean" sale, or corroborating an insurance/theft claim in a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.nicb.org/theft_and_fraud_awareness/vincheck.
2. Enter the 17-character `vin`, accept the terms, and solve the CAPTCHA.
3. Read the two results: a **theft** record (reported stolen and not recovered, per participating insurers) and a **salvage/total-loss** record.
4. Respect the daily search cap (a handful of lookups); it is meant for individual, not bulk, use.
5. Pivot: a salvage/theft flag feeds a fuller paid VIN history (NMVTIS/Carfax) and, combined with owner records, supports the vehicle side of a subject profile.

## Inputs → Outputs
- **In:** `vin`
- **Out:** `document-id` — theft flag (stolen/unrecovered) and salvage/total-loss flag
- **Empty/negative result looks like:** "no records found" — this only means participating insurers reported nothing; it is NOT proof the vehicle is clean (non-member insurers and non-insured losses aren't covered). Absence is weak evidence.

## Gotchas & OpSec
- Human-in-the-loop: a **CAPTCHA** gates every search; solve it manually.
- OpSec: **passive** — you query NICB about a VIN, not the owner; no notification.
- Coverage limits: data is only from NICB-member insurers and only the two flag types (theft, salvage). It is not a full title/ownership history — pair with NMVTIS-based reports for that.
- Daily cap: heavy/automated use is blocked by design.

## Overlaps ("do both")
- Pairs with NMVTIS-based VIN reports (VINCheck flags theft/salvage; NMVTIS/commercial reports give title brands, odometer, and ownership count) and with plate/registry tools — run VINCheck first as a free screen, then a paid history if the flags or the case warrant it.

## Trust & verifiability
`trust: trusted` — the NICB is an authoritative not-for-profit fed by insurer data; its flags are reliable for what member insurers report, with the key caveat that a clean result reflects only that member data, not a nationwide guarantee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-insurance-crime-bureau-vin-search |
| category | transportation |
| selectorsIn → selectorsOut | vin → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
