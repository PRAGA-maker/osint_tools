---
id: sesac-com
name: sesac.com
description: Use when you have a songwriter/performer `name` or publisher `employer-org` and want to confirm their affiliation and linked works — returns name, employer-org, and associate links.
url: https://www.sesac.com/repertory/
category: public-records
path:
- public-records
bestFor: Confirming a songwriter/artist's affiliation with the SESAC performing-rights organization and linking them to publishers and works.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free public repertory search; no account needed. Terms forbid bulk data-mining and redistribution.
opsec: passive
opsecNote: Public catalog lookup — you query song/rights data, not the subject. No target-side signal. The site prohibits scraping, so search manually rather than automating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by SESAC, a US performing-rights organization; the repertory is its own authoritative record of works it represents.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ascap-com
- bmi-com
aliases:
- SESAC Repertory
- SESAC repertory search
tags:
- professionlicensing
- Profession & Licensing Sites
- music-rights
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# sesac.com

> SESAC's public repertory database: confirm that a songwriter, performer, or publisher is affiliated with SESAC and surface the works and business relationships that tie them together.

## When to use
You have a `name` you believe belongs to a songwriter or recording artist, or a publisher `employer-org`, and you want to confirm a professional music affiliation and pull linked parties. A hit ties a person to specific song titles, co-writers, and a SESAC-represented publisher — useful for establishing a subject's real profession, business associates, or a publishing entity they operate through.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sesac.com/repertory/ and accept the usage terms.
2. Choose a search mode: by song title, SESAC work number, writer/artist, or publisher.
3. Enter the `name` or `employer-org` and submit.
4. Read the result rows: each work shows the title, SESAC's represented share, the SESAC-affiliated songwriter(s), and the SESAC-affiliated publisher(s).
5. Pivot: co-writers and the publisher become `associate` / `employer-org` leads; if the person is not found here, repeat at the other US PROs [[ascap-com]] and [[bmi-com]].

## Inputs → Outputs
- **In:** `name` (writer/artist) or `employer-org` (publisher)
- **Out:** `name` (confirmed affiliated writers), `employer-org` (publisher), `associate` (co-writers on shared works)
- **Empty/negative result looks like:** "no results" — SESAC only lists works it represents, so a miss usually means the person is affiliated with a different PRO (ASCAP, BMI, GMR), not that they're not a songwriter.

## Gotchas & OpSec
- Coverage is SESAC-only and comparatively small (SESAC is invitation-based). Always check ASCAP and BMI before concluding someone isn't a rights-holder.
- Some works carry direct-license arrangements not reflected in the search.
- OpSec: passive; no target signal. Respect the no-scraping terms — search by hand.

## Overlaps ("do both")
- Pairs with [[ascap-com]] and [[bmi-com]] — the three US PROs partition songwriters between them, so a subject absent from one often appears in another; run all three to avoid a false negative.

## Trust & verifiability
`trust: trusted` — this is SESAC's first-party record of the works and writers it represents, so affiliation hits are authoritative for SESAC's catalog (though silent on non-SESAC relationships).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sesac-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
