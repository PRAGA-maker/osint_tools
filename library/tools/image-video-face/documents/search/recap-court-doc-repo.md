---
id: recap-court-doc-repo
name: RECAP Archive (Free Law Project)
description: Use when you have a `name` and want to find US federal court cases and filings involving them — returns docket entries, case document-ids, parties, and filed PDFs.
url: https://www.courtlistener.com/recap/
category: image-video-face
path:
- image-video-face
- documents
- search
bestFor: Searching US federal (PACER) court dockets and filed documents free, via the crowd-sourced RECAP archive.
selectorsIn:
- name
selectorsOut:
- document-id
- name
- associate
- employer-org
status: live
pricing: free
costNote: Free. RECAP (by the non-profit Free Law Project) mirrors PACER documents that users have already paid for and donated, so you avoid PACER's per-page fees. The old archive.recapthelaw.org now lives inside CourtListener's RECAP Archive.
opsec: passive
opsecNote: Searching RECAP/CourtListener is a passive query against an archive of already-public court records — the subject is never contacted or notified. Nothing touches PACER when you read RECAP. Use a sock-puppet browser for hygiene; installing the RECAP browser extension is optional and only affects your own PACER sessions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the non-profit Free Law Project; documents are authentic mirrors of PACER filings, though the archive is a partial (crowd-sourced) subset of all federal cases.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- RECAP
- CourtListener RECAP
- recapthelaw.org
tags:
- court-records
- legal
- federal-litigation
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- courtlistener
- courtlistener-recap
- free-law-recap-archive
---

# RECAP Archive (Free Law Project)

> A free, searchable mirror of US federal (PACER) court documents — find litigation, bankruptcies, and criminal cases naming your subject without paying PACER's fees.

## When to use
You have a `name` and want to know whether the person appears in US federal court records — as a party, defendant, plaintiff, or filer in civil, criminal, or bankruptcy matters. Court filings are a rich, authoritative source: they carry addresses, employers, associates/co-parties, financial detail, and a dated narrative. RECAP lets you search and read the actual filed PDFs for free.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.courtlistener.com/recap/` (the current home of the RECAP Archive).
2. Search the `name` (use quotes; try name variants); filter by court, date, or nature-of-suit.
3. Open a matching docket: read the docket entries and download the filed documents already in RECAP (free).
4. For documents not yet in RECAP, note the PACER docket ID — the RECAP browser extension auto-donates any you later pull from PACER.
5. Pivot: co-parties/attorneys → `associate`; an employer named in filings → `[[kompass]]`/registries; addresses → property/records; case IDs → the court's own PACER record.

## Inputs → Outputs
- **In:** `name` (party/filer)
- **Out:** `document-id` (docket/case numbers), `name`, `associate` (co-parties/counsel), `employer-org`, filed PDFs
- **Empty/negative result looks like:** no dockets match — either the person has no federal cases, the case isn't in the crowd-sourced RECAP subset yet, or it's a *state* matter (RECAP is federal only). Absence ≠ no litigation; check state courts and PACER directly.

## Gotchas & OpSec
- Federal only: state and local cases are elsewhere. And RECAP is a **partial** mirror — a missing document may exist on PACER but not yet be donated.
- Common names need disambiguation by locale/case detail; sealed records won't appear.
- OpSec: fully **passive** — public court records, no subject notification.

## Overlaps ("do both")
- Pairs with PACER (the authoritative federal source) and state court portals — RECAP is the free first sweep; PACER fills gaps RECAP hasn't mirrored, and state portals cover what federal search misses.

## Trust & verifiability
`trust: trusted` — Free Law Project mirrors are authentic PACER filings you can cite; the only caveat is completeness (crowd-sourced subset), not authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recap-court-doc-repo |
| category | image-video-face |
| selectorsIn → selectorsOut | name → document-id, name, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
