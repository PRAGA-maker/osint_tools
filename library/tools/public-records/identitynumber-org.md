---
id: identitynumber-org
name: IdentityNumber.org (South Africa)
description: Use when you have a South African `name` or ID number (`document-id`) and want identity verification plus genealogy/death records — returns confirmed `name`, `dob`, `address` and family `associate` links.
url: https://www.identitynumber.org/
category: public-records
path:
- public-records
bestFor: Verifying a South African ID number and pulling SA death-notice, marriage and family-finder records for identity and genealogy tracing.
selectorsIn:
- name
- address
- document-id
selectorsOut:
- name
- dob
- address
- associate
- document-id
status: live
pricing: freemium
costNote: Free "Silver" tier does basic ID verification; fuller access to death records, marriage transcriptions, immigration and contact details is gated behind Gold/Platinum/Diamond paid tiers (~$20–$50).
opsec: passive
opsecNote: You submit the subject's name/ID to a third-party South African service, which logs the query and requires signup for anything beyond the free tier — use a research account. No notification reaches the subject.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party South African genealogy/verification platform (transcribed death notices, family-finder). Useful for SA-specific leads but not an official government register; verify critical facts against Home Affairs / official sources.
missingPersonsRelevance: high
coverage:
- za
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- identitynumber.org
- SA ID verification
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- south-africa
- id-verification
- death-records
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# IdentityNumber.org (South Africa)

> A South African identity-verification and genealogy platform — ties an SA ID number or name to `dob`, death-notice records, marriages and family links.

## When to use
You have a South African subject — a `name`, an address, or a 13-digit SA `document-id` (ID number) — and want to verify the ID, extract the encoded `dob`/gender, or trace family via transcribed death notices, marriage records and the family-finder. This is a strong SA-specific supplement where Western people-search tools have little coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.identitynumber.org/ and use the ID verification / family-finder / death-record tools.
2. Enter the ID number or name/surname; the free Silver tier returns basic verification.
3. For death notices, marriage transcriptions, immigration and contact details, sign up for a paid tier.
4. Read outputs: confirmed name, `dob` (also derivable from the SA ID number itself), addresses, and named relatives.
5. Pivot: relatives feed associate mapping; a confirmed ID/`dob` anchors identity across other SA sources.

## Inputs → Outputs
- **In:** `name`, `address`, or SA ID number (`document-id`)
- **Out:** confirmed `name`, `dob`, `address`, family `associate` links, `document-id`
- **Empty/negative result looks like:** no record — the person may not be in the transcribed collections, the ID may be invalid, or the data sits behind a higher paid tier than you hold; a Silver-tier null is not conclusive.

## Gotchas & OpSec
- Human-in-the-loop: only basic checks are free; genealogy/contact records require a paid membership.
- Not an official government register — it aggregates and transcribes; confirm anything load-bearing against SA Home Affairs or primary records.
- OpSec: passive toward the subject, but you must register an account and disclose queries to the operator.

## Overlaps ("do both")
- Pairs with other genealogy and death-record sources — IdentityNumber.org is SA-focused, so combine it with global obituary/records tools when the subject has cross-border ties.

## Trust & verifiability
`trust: community` — a useful third-party SA aggregator, not a first-party authority; treat outputs as leads to verify officially.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | identitynumber-org |
