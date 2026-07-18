---
id: afd-co-uk
name: afd.co.uk
description: Use when you have a UK `address`, `phone`, or `email` and want to validate it and pull matching reference data — returns confirmed address, phone status, and geographic codes.
url: https://www.afd.co.uk/try-it/
category: financial-crypto
path:
- financial-crypto
bestFor: Validating a UK address, phone number, email, or bank sort-code and enriching it with postcode/geographic reference data.
selectorsIn:
- address
- phone
- email
selectorsOut:
- address
- phone
- geolocation
status: live
pricing: freemium
costNote: The public "Try It" demo is free with a small daily evaluation-credit allowance; volume/API use requires a paid AFD account.
opsec: passive
opsecNote: Queries hit AFD's own reference databases (Royal Mail PAF, phone/bank validation data), not the target's infrastructure — the subject is never contacted. Nothing you type identifies you beyond normal web logging; use a clean browser if you want the lookup unattributable.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: AFD Software is a long-established UK data-quality vendor; the address data is licensed from Royal Mail PAF, so the reference set is authoritative.
missingPersonsRelevance: medium
coverage:
- uk
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- AFD Software Try It
- AFD address validation
tags:
- banksites
- Banking Related Sites
- address-validation
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# afd.co.uk

> AFD Software's free "Try It" demo: a UK address / phone / email / bank-sort-code validation and enrichment oracle backed by Royal Mail PAF.

## When to use
You have a partial or claimed UK `address`, `phone`, or `email` and need to confirm it is real and standardise it. Good for corroborating that a postcode resolves to a genuine street address, that a phone number is a live UK landline/mobile, or that a sort code belongs to a named bank branch — the kind of validation that tells you whether a lead is worth pursuing before you spend effort on it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.afd.co.uk/try-it/ in a browser.
2. Pick the relevant tab — Address, Phone, Email, or Bank.
3. Enter the value you want to check (`selectorsIn`): a postcode or partial address, a phone number, an email, or a sort code + account number.
4. Read the result (`selectorsOut`):
   - **Address:** full standardised address, coordinates, ward/constituency/authority codes, what3words.
   - **Phone:** valid/invalid, line type (landline vs mobile), region.
   - **Email:** deliverable / throwaway / malformed.
   - **Bank:** the branch a sort code maps to, and whether an account number is structurally valid.
5. Pivot: a validated `address` + coordinates feeds mapping and neighbour-tracing; a confirmed live `phone` feeds phone-OSINT tools.

## Inputs → Outputs
- **In:** `address` / `phone` / `email` (or a bank sort code)
- **Out:** standardised `address`, `phone` line-type/status, `geolocation` (lat/long + admin codes), sort-code-to-branch
- **Empty/negative result looks like:** "no match" for an address, "invalid" for a phone/sort code, or your daily evaluation credits running out ("evaluation credits left for today: 0") — none of which prove the datum is fake, only that this reference set didn't confirm it.

## Gotchas & OpSec
- Human-in-the-loop: the free tier is rate-limited to a handful of daily evaluation credits; space out queries or you'll be locked out until the next day.
- Coverage is UK-first — address validation is authoritative for the UK/Ireland and thin-to-absent elsewhere despite the "250+ countries" claim.
- OpSec: passive. You query AFD's data, never the subject; nothing is sent to the person being checked.

## Overlaps ("do both")
- Pairs with a dedicated phone/caller-ID lookup: AFD confirms a UK number is a real, correctly-formatted line and its region, then a reverse-lookup service attaches a name.

## Trust & verifiability
`trust: trusted` — AFD is an established commercial data-quality provider and its address layer is licensed Royal Mail PAF data, so matches are authoritative rather than crowd-sourced guesses.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | afd-co-uk |
