---
id: avvo-north-america
name: Avvo (North America)
description: Use when you have a `name` (of a US lawyer) or a location and want their professional profile — returns `employer-org` (firm), practice area, office `address`, contact details and disciplinary record.
url: http://www.avvo.com
category: search-engines
path:
- search-engines
bestFor: Profiling a US attorney — firm, location, contact, licence and disciplinary history.
selectorsIn:
- name
- geolocation
selectorsOut:
- employer-org
- address
- social-profile
status: live
pricing: free
costNote: Free directory and profiles; lawyers pay for enhanced listings, but public search and profile viewing cost nothing.
opsec: passive
opsecNote: Public directory browsing — no notification to the person profiled. Avvo profiles are search-engine indexed and self-/firm-maintained; simply reading them leaks nothing about you beyond a normal web visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Large, established US legal directory (1M+ attorneys) combining bar-record data with self-supplied profiles and user reviews; licence/discipline data is reliable, reviews and bios are not independently verified.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Avvo
- avvo.com lawyer directory
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Avvo (North America)

> A large US directory of lawyers with profiles, ratings, reviews and disciplinary records — the go-to when a subject is (or claims to be) an attorney.

## When to use
Your subject is a US lawyer, or presents themselves as one, and you want to verify and enrich that. Avvo confirms whether an attorney by that `name` exists, in which state, and surfaces their firm (`employer-org`), office `address`, practice areas, bar admission year, contact details, client reviews, and — importantly — any **disciplinary record**. Also useful in reverse: search by location + practice area to enumerate lawyers, or to confirm a claimed legal credential is real.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.avvo.com and use the lawyer search (by `name`, or by practice area + `geolocation`).
2. Open the matching profile and read: firm name, office address and phone, practice areas, jurisdictions/bar admission, years licensed, the Avvo rating, client reviews, and the **licence & disciplinary** section.
3. Verify credentials: cross-check the bar number/status against the relevant state bar's official lookup — Avvo mirrors it but the state bar is authoritative.
4. Pivot: firm + address feeds workplace/geolocation work; the name + jurisdiction feeds court-record and bar searches; reviews sometimes name cases or clients.

## Inputs → Outputs
- **In:** `name` (attorney) or `geolocation` + practice area
- **Out:** `employer-org` (firm), office `address`, contact, `social-profile` (the Avvo profile), practice areas, disciplinary history
- **Empty/negative result looks like:** no profile for the name — the person may not be a US-licensed attorney, may be licensed under a different name, or simply has a minimal/claimed-but-unverified listing. Absence isn't proof they aren't a lawyer; check the state bar directly.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — profiles are public and the subject isn't alerted.
- Profiles are partly self-/firm-supplied, so bios, photos and claimed specialties are marketing; the **licence and discipline** data (sourced from bar records) is the trustworthy part.
- US-focused. For non-US lawyers this won't help.

## Overlaps ("do both")
- Do both with the official **state bar** attorney lookup — Avvo is richer and faster for context (firm, reviews, contact), the state bar is authoritative for licence status and discipline.

## Trust & verifiability
`trust: community` — a legitimate, large directory; treat licence/disciplinary fields as reliable (bar-sourced) and the self-authored profile content and reviews as unverified leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | avvo-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | name, geolocation → employer-org, address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
