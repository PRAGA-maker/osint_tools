---
id: ascap-com
name: ascap.com (ACE Repertory)
description: Use when you have a `name` who may be a songwriter/composer/publisher and want to confirm it — ASCAP's ACE database returns registered works, co-writers (`associate`), and publisher (`employer-org`).
url: https://www.ascap.com/ace-title-search/restored-works
category: public-records
path:
- public-records
bestFor: Confirming a person is a registered songwriter/composer/publisher via ASCAP's ACE repertory and mapping their works and collaborators.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
- name
status: live
pricing: free
costNote: Free public ACE (ASCAP Clearance Express) title/writer search; no account needed.
opsec: passive
opsecNote: Querying a public music-rights database is passive and does not notify the person. Standard sock-puppet browsing is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party database of ASCAP, a major US performing-rights organisation; registration data (writers, publishers, works) is authoritative for ASCAP-affiliated music.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- setlist-fm
- companieshouse-im
aliases:
- ASCAP ACE
- ACE Repertory
- ascap.com
tags:
- professionlicensing
- Profession & Licensing Sites
- music-rights
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ascap.com (ACE Repertory)

> ASCAP's ACE (ASCAP Clearance Express) repertory — a searchable database of musical works and their writers/publishers, used to confirm a subject is a songwriter/composer and map their collaborators.

## When to use
You have a `name` who may be a songwriter, composer, or music publisher and want to confirm that professional identity and enumerate their catalogue. ACE returns the works registered to a writer, their co-writers (`associate`), and the publisher/company (`employer-org`) behind them — corroborating a music-industry link and opening a network of collaborators and business entities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open ASCAP's ACE search (https://www.ascap.com/ace-title-search) and choose to search by Writer/Performer or Title.
2. Enter the subject `name` (as a writer or performer).
3. Review results: registered works, co-writers, and the associated publisher(s).
4. Note that ACE covers ASCAP-affiliated works; a writer registered with BMI/SESAC instead won't appear here.
5. Pivot: co-writers are `associate` leads; publisher names are `employer-org` leads for company-registry lookups; song titles corroborate a claimed career.

## Inputs → Outputs
- **In:** `name` (writer/performer) or a song title
- **Out:** registered works, co-writers (`associate`), publisher (`employer-org`), confirmed writer `name`
- **Empty/negative result looks like:** no works found — the person may not be an ASCAP writer (could be BMI/SESAC or unaffiliated), or the name differs from their registered credit; absence isn't proof they're not in music.

## Gotchas & OpSec
- ASCAP-only: US songwriters registered with **BMI** or **SESAC** won't appear — check those PROs too.
- Credited names may differ from legal/common names (stage names, spelling); try variants.
- OpSec: passive; a public database query with no notification.
- Moderate MP value: strongest when the subject has a music-industry angle; otherwise it's a niche corroboration source.

## Overlaps ("do both")
- Pairs with `[[setlist-fm]]` (performance history) for musicians; publisher entities can be run through company-registry tools like `[[companieshouse-im]]` and equivalents.

## Trust & verifiability
`trust: trusted` — a first-party PRO database, so registration data is authoritative for ASCAP works. Its only limit is scope (ASCAP-affiliated only); corroborate across BMI/SESAC for completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ascap-com |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
