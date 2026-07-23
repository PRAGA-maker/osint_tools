---
id: generate-sa-id-numbers
name: Generate SA ID Numbers
description: Use when you have a `dob` (and gender/citizenship) and want to construct or sanity-check the structure of a South African national ID number — returns a validly-formatted `document-id`.
url: https://chris927.github.io/generate-sa-idnumbers/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Understanding and checksum-validating the structure of South African ID numbers (date/gender/citizenship digits + Luhn check).
selectorsIn:
- dob
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free static web page; runs entirely client-side, no account.
opsec: passive
opsecNote: Fully client-side and offline-capable — nothing you type is sent anywhere. It generates SAMPLE numbers; it does not look up or validate real people. Never present a generated number as a real person's identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source demo (chris927 on GitHub Pages) illustrating the documented SA ID number algorithm; the format/checksum logic is publicly specified and verifiable.
missingPersonsRelevance: low
coverage:
- za
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- SA ID number generator
- South African ID generator
tags:
- south-africa
- identity
- test-data
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Generate SA ID Numbers

> A client-side generator that builds validly-formatted South African national ID numbers from a date of birth, gender and citizenship status.

## When to use
You have a South African `dob` (plus gender/citizenship) and want to see what a correctly-structured 13-digit ID number looks like, or you want to understand how an ID number decomposes so you can sanity-check one you already hold (birth-date digits, gender band, citizenship digit, and the trailing Luhn checksum). It produces **sample** numbers for learning/testing — it is not a lookup of any real individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://chris927.github.io/generate-sa-idnumbers/.
2. Enter the birth `dob` (year/month/day), select gender and citizen/resident status, and any sequence option.
3. Submit to get a generated 13-digit `document-id`.
4. To validate an existing number instead, decompose it by hand: `YYMMDD` (birth date) + `SSSS` (gender: <5000 female, ≥5000 male) + `C` (citizen 0 / resident 1) + `A` + Luhn check digit — and confirm the checksum.

## Inputs → Outputs
- **In:** `dob`, gender, citizenship status
- **Out:** a validly-formatted South African `document-id` (sample)
- **Empty/negative result looks like:** an out-of-range date is rejected — the tool only builds structurally valid numbers, it cannot confirm a number belongs to a real person.

## Gotchas & OpSec
- Output is **synthetic** — a generated number that passes the checksum is not evidence anyone with that ID exists. Never treat it as a real identity.
- Runs entirely in the browser; safe to use offline for structure-checking.
- Only applies to South African ID numbers; the digit layout is country-specific.

## Overlaps ("do both")
- Use alongside a Luhn/checksum validator when you want to *verify* rather than *generate* — this explains the structure, a validator confirms a specific number's check digit.

## Trust & verifiability
`trust: community` — an open GitHub-Pages implementation of the publicly documented SA ID format; you can read the source and re-derive the checksum to confirm correctness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | generate-sa-id-numbers |
