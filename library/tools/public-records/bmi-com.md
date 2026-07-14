---
id: bmi-com
name: BMI / Songview Repertoire Search
description: Use when you have a `name` (songwriter, performer, or publisher) or a song title and want to link a person to musical works, co-writers, and publishing companies — returns songwriter names, publishers, and co-writer associates.
url: https://repertoire.bmi.com/StartPage.aspx
category: public-records
path:
- public-records
bestFor: Linking a songwriter/composer to their registered works, publishers, and co-writers via the BMI/ASCAP Songview database.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free public repertoire search; no account or payment required.
opsec: passive
opsecNote: A public copyright-database query; anonymous and server-side, with no notification to any writer or rights-holder. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by BMI (a performing-rights organization) jointly with ASCAP via Songview; authoritative copyright-ownership data for ~40M works.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Songview
- BMI repertoire
- ASCAP/BMI Songview
tags:
- professionlicensing
- Profession & Licensing Sites
- music
- copyright
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# BMI / Songview Repertoire Search

> The BMI/ASCAP Songview copyright database: link a songwriter, performer, or publisher name to their registered musical works, co-writers, and publishing companies.

## When to use
You have a subject who is (or claims to be) a songwriter, composer, or music publisher, and you want to corroborate that work, find their publishing company (`employer-org`), or surface co-writers (`associate`s). One writer credit often exposes a real legal name, a publisher affiliation, and a network of collaborators — useful when a subject operates under a stage name but registers works under their legal identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://repertoire.bmi.com/StartPage.aspx (Songview).
2. Search by writer/composer `name`, performer, publisher, song title, BMI Work ID, or ISWC. Keep the default "Songview" scope for the widest coverage (BMI + ASCAP + reconciled societies).
3. Read the work records: each lists songwriters, publishers, and their ownership share splits.
4. Pivot: co-writers on the same works are `associate` leads; the publisher `employer-org` and any administrator can be looked up in corporate registries; a legal name found here can break a stage-name alias.

## Inputs → Outputs
- **In:** `name` (songwriter / performer / publisher) or a song title / work ID
- **Out:** songwriter `name`(s), publisher `employer-org`, co-writer `associate`s, ownership shares
- **Empty/negative result looks like:** no works found — the subject may register with a different PRO (SESAC, GMR, or a foreign society), use a variant name spelling, or not be a registered writer at all.

## Gotchas & OpSec
- Songview covers BMI and ASCAP (and reconciled societies) but **not** SESAC/GMR or many foreign PROs — absence here is not proof the person has no music credits.
- Name matching is literal; try stage names, legal names, and spelling variants.
- OpSec: passive; no notification to anyone.

## Overlaps ("do both")
- Do both with ASCAP's own repertoire and foreign PRO databases for subjects who may be registered elsewhere, and with corporate registries to resolve the publisher `employer-org` to real people.

## Trust & verifiability
`trust: trusted` — first-party performing-rights data from BMI/ASCAP; ownership records are authoritative for registered works.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bmi-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
