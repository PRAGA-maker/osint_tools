---
id: everypolitician
name: EveryPolitician
description: Use when you have a `name` (and maybe a country) and want to check whether they are or were a political office-holder — returns positions, party, terms, and identifiers for PEP screening.
url: https://everypolitician.org/
category: public-records
path:
- public-records
- sanctions-pep
bestFor: PEP (politically-exposed-person) screening — confirming whether a subject holds/held political office anywhere in the world.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- dob
status: live
pricing: free
costNote: Free open data (Creative Commons BY-NC), built on Wikidata and now maintained within the OpenSanctions ecosystem; commercial licensing available separately.
opsec: passive
opsecNote: You query an open, public database built from Wikidata — no subject is ever notified and nothing touches the person's infrastructure. Only your own request is logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Community/OpenSanctions project sourced from Wikidata with hundreds of thousands of office-holders; data is crowd-curated so cross-check specifics, but provenance is transparent and citable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- every-politician
- everypolitician-org
aliases:
- Every Politician
tags:
- pep
- politicians
- sanctions-screening
- wikidata
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# EveryPolitician

> A free, global database of political office-holders — the fast PEP check to see whether a `name` maps to a current or former politician anywhere in the world.

## When to use
You have a subject `name` and need to know whether they are a politically-exposed person: an elected official, minister, legislator, judge, or ruler — currently or historically, in any country. This is a core due-diligence and background step; a hit tells you the person holds public office (raising the stakes and opening official-record avenues), while positions, party, and term dates give you dates and affiliations to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://everypolitician.org/.
2. Browse to the relevant country, or search for the subject `name` (try name variants — the data includes alternate spellings).
3. Open the matched profile: read positions held (`employer-org`/legislature), party affiliation, term start/end dates, and where available `dob`/birthplace and identifiers.
4. Confirm identity carefully — match on country, term dates, and party, not name alone (common names collide).
5. Pivot: a confirmed office → official parliamentary/government records and news; the linked Wikidata ID → further structured data; term dates → timeline anchoring.

## Inputs → Outputs
- **In:** `name` (optionally with country)
- **Out:** political positions (`employer-org`), party, term dates, `dob`/identifiers where present
- **Empty/negative result looks like:** no matching politician — the subject likely isn't (and wasn't) an office-holder in the covered data, or the name variant differs; absence is not proof, since coverage depends on Wikidata completeness for that country.

## Gotchas & OpSec
- Human-in-the-loop: none; open access, with an API for bulk use.
- OpSec: **passive** — public open data; no subject contact.
- Data is Wikidata-sourced and crowd-curated: coverage and freshness vary by country, and a same-name match is not identity. Verify specifics against an official register before treating someone as a PEP.

## Overlaps ("do both")
- Pairs with the broader OpenSanctions database and national gazettes — EveryPolitician confirms *office-holding* while sanctions/PEP lists add watchlist status and official registers add authoritative detail; run all three for real due diligence.

## Trust & verifiability
`trust: trusted` — transparent, Wikidata-backed open data within the OpenSanctions ecosystem; every fact traces to a public source you can re-check, but crowd-curation means verify the specifics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | everypolitician |
