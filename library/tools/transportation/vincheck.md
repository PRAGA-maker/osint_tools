---
id: vincheck
name: VINCheck®
description: Use when you have a `vin` and want to know if the vehicle is recorded as stolen/unrecovered or a salvage/total-loss — returns theft and salvage-title flags from insurer data.
url: https://www.nicb.org/vincheck
category: transportation
path:
- transportation
bestFor: Free check of whether a US vehicle (by VIN) is flagged as stolen-and-unrecovered or a salvage/total-loss record.
selectorsIn:
- vin
selectorsOut:
- vin
status: live
pricing: free
costNote: Free public service from the National Insurance Crime Bureau (NICB). Limited to a small number of searches (about 5) per IP address per day; no account needed.
opsec: passive
opsecNote: You query the NICB database by VIN — no vehicle owner is contacted or notified. NICB logs the query/IP and enforces a daily cap. Fully passive; use a clean session if the VIN is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the NICB, a US nonprofit backed by insurers; theft/salvage flags come directly from participating member insurance companies.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- national-insurance-crime-bureau-vin-search
- vehicle-enquiry-service-gov-uk
aliases:
- NICB VINCheck
- nicb.org/vincheck
tags:
- vehicle
- vin
- theft
- salvage
- us
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# VINCheck®

> The NICB's free VIN oracle: is this US vehicle recorded as stolen-and-unrecovered, or as a salvage / total-loss?

## When to use
You have a `vin` (from a plate lookup, a title, a photo of the dash/door jamb, or an ad) and want two specific, authoritative facts: whether the vehicle is currently flagged **stolen and unrecovered**, and whether it has a **salvage/total-loss** record from an insurer. In an investigation this can corroborate or contradict a subject's story about a vehicle, flag a car tied to a theft, or expose an undisclosed write-off. It's a narrow but high-quality signal drawn straight from insurance-industry data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nicb.org/vincheck.
2. Enter the 17-character `vin` and accept the terms.
3. Read the two results: theft record (stolen/unrecovered as reported by a member insurer) and total-loss/salvage record.
4. Mind the daily cap (~5 searches per IP/day) — batch your most important VINs.
5. Pivot: a theft/salvage flag feeds law-enforcement or title follow-up; a clean result plus a plate/VIN decode builds the vehicle's provenance picture alongside other vehicle tools.

## Inputs → Outputs
- **In:** `vin` (17-character US vehicle identification number)
- **Out:** theft (stolen/unrecovered) flag and salvage/total-loss flag for that `vin`
- **Empty/negative result looks like:** "no records found" — the VIN isn't flagged by a participating insurer. Because only NICB-member insurers report, absence is not a guarantee the car is clean; it's "not flagged in NICB's data."

## Gotchas & OpSec
- US-only and insurer-sourced: it reflects data from NICB member companies, so non-member or out-of-scope records won't appear.
- Hard daily search cap (~5/IP) — plan your queries.
- It reports theft/salvage status only — not owner, mileage, or full history. Combine with a full VIN-history tool for those.
- OpSec: passive; no owner is contacted.

## Overlaps ("do both")
- Pairs with `[[national-insurance-crime-bureau-vin-search]]` (same NICB data) and vehicle-history/decoder tools — VINCheck gives the authoritative theft/salvage flag, while a decoder gives specs and a paid history report gives ownership/mileage.

## Trust & verifiability
`trust: trusted` — a first-party NICB service fed by member insurers, so a positive theft/salvage flag is authoritative. The only caveat is coverage (member insurers only), which affects negatives, not positives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vincheck |
| category | transportation |
| selectorsIn → selectorsOut | vin → vin |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
