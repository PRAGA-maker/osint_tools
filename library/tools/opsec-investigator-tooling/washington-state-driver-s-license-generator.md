---
id: washington-state-driver-s-license-generator
name: Washington State Driver's License Number Generator
description: Use when you have a subject's `name` and `dob` and want to derive their Washington State driver's license number — returns a candidate `document-id` (WA DL number).
url: https://mmarvick.github.io/wa-drivers-license/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Reconstructing or validating a Washington State DL number, which WA encodes deterministically from a person's name and date of birth.
selectorsIn:
- name
- dob
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free static web page; no account, no payment.
opsec: passive
opsecNote: Runs entirely client-side in your browser (a GitHub Pages static app) — the name/DOB you enter are not sent to any server, so nothing about the subject leaves your machine. Still enter data in a clean browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community project implementing WA's publicly-documented DL check-digit/encoding scheme (adapted from Marist College's Identification Numbers materials). Output is an algorithmic prediction, not a state record — verify against an authoritative source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WA drivers license generator
- Washington DL number tool
tags:
- document-id
- identification-numbers
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Washington State Driver's License Number Generator

> Washington encodes its driver's license numbers deterministically from the holder's name and date of birth; this tool runs that algorithm so you can derive (or check) a WA DL number from those two selectors.

## When to use
You have a subject's `name` and `dob` and are in Washington State, and you want their likely driver's license `document-id` — or you have a claimed WA DL number and want to confirm it is consistent with a given name/DOB. Because WA's format is name+DOB-derived (unlike states that assign random numbers), this turns two common selectors into a document identifier that can corroborate records, match against leaked/breached datasets, or validate an ID a subject provided.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mmarvick.github.io/wa-drivers-license/ (loads as a static page; works offline once loaded).
2. Enter the subject's first, middle, and last name and date of birth in the fields.
3. Read the generated WA DL number in the Results section.
4. Validate/pivot: compare the derived `document-id` against any WA DL number you already hold; a match strongly corroborates the name↔DOB pairing. Feed a confirmed number into records checks.

## Inputs → Outputs
- **In:** `name` (first/middle/last), `dob`
- **Out:** `document-id` (candidate Washington State DL number)
- **Empty/negative result looks like:** if a claimed WA DL number does NOT match the number derived from the name/DOB, the identity claim is suspect (or the number is from another state/format). Note the algorithm produces the base encoding; real cards can carry a sequence suffix, so treat a near-match on the encoded stem as significant.

## Gotchas & OpSec
- This predicts the number from the public algorithm — it is not a query against Washington DOL and does not confirm the license actually exists or is valid.
- Middle name / suffix handling and duplicate-name sequence digits can cause the tail of the number to differ; compare the name-encoded portion.
- Only Washington State uses this exact scheme — don't apply the output to other states.
- Client-side only: nothing is transmitted, so it's safe for sensitive selectors.

## Overlaps ("do both")
- Pairs with any public-records or DMV-record lookup: use this to derive/validate the number, then confirm existence and status through an authoritative records source.

## Trust & verifiability
`trust: community` — an open community implementation of a publicly-documented state encoding. The math is reproducible, but the result is a *prediction*: always confirm a derived DL number against an authoritative record before treating it as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | washington-state-driver-s-license-generator |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, dob → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
