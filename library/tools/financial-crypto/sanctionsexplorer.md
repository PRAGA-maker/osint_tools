---
id: sanctionsexplorer
name: Sanctions Explorer
description: Use when you have a `name` or `employer-org` and want to check current/historical OFAC, UN and EU sanctions listings — returns employer-org, associate and identifier details.
url: https://sanctionsexplorer.org/
category: financial-crypto
path:
- financial-crypto
bestFor: Searching consolidated current and historical sanctions lists (OFAC/UN/EU) for a person or entity.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free public database built by C4ADS; no account required.
opsec: passive
opsecNote: Passive read of a public sanctions database; you disclose only your own query, nothing to the subject. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by C4ADS (a respected non-profit) on official OFAC/UN/EU sanctions data; the underlying listings are authoritative government records, and it adds historical versions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SanctionsExplorer
- C4ADS Sanctions Explorer
tags:
- sanctions
- companies-finance
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Sanctions Explorer

> A searchable, consolidated database of OFAC, UN and EU sanctions — including historical (delisted) entries — for checking whether a person or entity is, or ever was, sanctioned.

## When to use
You have a `name` or `employer-org` and need to know whether it appears on major sanctions lists, now or in the past. Sanctions listings are rich identity records: they carry aliases, dates of birth, passport/ID numbers, addresses, and links to associated people and companies. That makes this useful both to flag risk and to harvest strong identifiers and `associate` links for someone who happens to be listed. The historical coverage lets you catch entries that were later removed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sanctionsexplorer.org/ and search the `name`/`employer-org` (try alias/transliteration variants).
2. Open a matching listing to read the identifiers — aliases, DOB, ID/passport numbers, addresses — and the issuing programme.
3. Note linked persons/entities as `associate`/`employer-org` pivots.
4. Check historical versions for delisted or amended entries.
5. Pivot: verify against the primary source (OFAC SDN / UN / EU consolidated list), and feed identifiers/associates into people- and corporate-search tools.

## Inputs → Outputs
- **In:** `name` or `employer-org` (with alias/spelling variants)
- **Out:** sanctions listing details — aliases, DOB, ID numbers, addresses, programme — and linked `associate`/`employer-org`
- **Empty/negative result looks like:** no match — the subject isn't on the covered lists (or is listed under a different spelling/alias); absence is not proof of clean status, only of not-listed-here.

## Gotchas & OpSec
- OpSec: passive; nothing reaches the subject.
- Name matching is fuzzy across transliterations — try multiple spellings/aliases before concluding "not listed."
- Confirm hits against the official primary lists before acting; and remember these are government designations, not proof of any specific unlisted allegation.

## Overlaps ("do both")
- Do both with corporate registries via `[[catalogue-of-research-databases-occrp-id]]` and PEP databases — Sanctions Explorer flags the designation and identifiers; registries and PEP tools expand the entity/associate network.

## Trust & verifiability
`trust: trusted` — built by C4ADS on official OFAC/UN/EU data; authoritative, though always corroborate a specific hit against the primary source list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sanctionsexplorer |
| category | financial-crypto |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
