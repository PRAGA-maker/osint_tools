---
id: world-legal-information-institute
name: World Legal Information Institute
description: Use when you have a `name` and want free access to court decisions and legal materials across jurisdictions — returns case `document-id`, `associate` (parties), and sometimes `address`.
url: https://worldlii.org
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Free, cross-jurisdiction case-law and legal-materials search spanning the global LII (Legal Information Institute) network.
selectorsIn:
- name
selectorsOut:
- document-id
- associate
- address
status: live
pricing: free
costNote: Free to search and read; WorldLII is a non-profit consortium (AustLII, BAILII, CanLII, and other LIIs) with no paywall.
opsec: passive
opsecNote: Searching a public legal database queries published court/legal records, not the subject, so it is fully passive and needs no login. No signal reaches the person of interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Free Access to Law Movement / LII consortium (hosted with AustLII); an authoritative aggregator of primary legal materials, though coverage and recency vary by member jurisdiction.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WorldLII
- WorldLII.org
tags:
- legal-research
- case-law
- court-records
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# World Legal Information Institute

> A free, non-profit gateway to court decisions and legal materials from dozens of jurisdictions — search a name across the world's case law without a paywall.

## When to use
You have a subject's `name` and want to check whether they appear in litigation, court judgments, tribunal decisions, or legal materials anywhere the LII network reaches. Court records can confirm a person's location at a point in time, name co-parties and relatives (`associate`), and surface disputes (family, probate, criminal) directly relevant to locating a missing person or understanding their circumstances.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://worldlii.org.
2. Use the search box; enter the subject's `name` (quote exact names, add a jurisdiction/keyword to narrow).
3. Optionally browse by country/database to target a specific jurisdiction's courts.
4. Read hits: case title, court, date, and full text — note parties, addresses, and dates.
5. Pivot: co-parties/relatives (`associate`) feed people-search; a case `document-id` feeds the originating court's registry; a jurisdiction narrows other record searches.

## Inputs → Outputs
- **In:** `name` (party/person), optionally a jurisdiction or keyword
- **Out:** matching case decisions/legal materials — `document-id` (citation), party `associate` names, sometimes an `address`
- **Empty/negative result looks like:** no results — the name isn't in any indexed decision (common; most people are never litigants), or that jurisdiction's court isn't covered. Absence is not exoneration or proof of anything.

## Gotchas & OpSec
- Coverage is uneven — some jurisdictions/courts are deep, others thin or absent; a gap reflects the database, not reality.
- Common names return many false hits; disambiguate with jurisdiction, date, or a middle name.
- Many decisions anonymize private parties (esp. family/juvenile matters) — you may see initials, not full names.

## Overlaps ("do both")
- Pairs with jurisdiction-specific court portals (CanLII, BAILII, PACER, etc.) — WorldLII gives global breadth; the national portal gives depth and the latest filings. Search both.

## Trust & verifiability
`trust: trusted` — a long-standing Free-Access-to-Law consortium serving primary legal texts; sources are authoritative, but always cite the original decision and confirm the party is your subject, not a namesake.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-legal-information-institute |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
