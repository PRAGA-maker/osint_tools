---
id: oregon-offender-search
name: Oregon Offender Search
description: Use when you have a `name` and want Oregon DOC custody/offender records — returns the offender's name, DOB, ID number, photo and status/location.
url: https://docpub.state.or.us/oos/intro.jsf
category: public-records
path:
- public-records
bestFor: Checking whether a person is or was in Oregon Department of Corrections custody and pulling their offender record and photo.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- image
- physical-description
status: live
pricing: free
costNote: Free official Oregon DOC public offender lookup; no account or payment.
opsec: passive
opsecNote: An official state public-records search; the subject is not notified. Custody data is public record; use it lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Oregon Department of Corrections; the offender data is authoritative state record.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sex-offender-us
aliases:
- Oregon DOC offender lookup
- OOS Oregon
tags:
- court
- inmate
- corrections
- oregon
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Oregon Offender Search

> Oregon's Department of Corrections public lookup: is this person in (or recently released from) Oregon custody, and what does their record show?

## When to use
You have a `name` and need to check Oregon incarceration/custody status — to locate someone in the corrections system, confirm identity via booking photo and DOB, or establish that a subject was in custody during a period of interest (which can explain a gap in a missing-persons or activity timeline). Returns the offender's `name`, DOB, DOC ID (`document-id`), photo (`image`), and physical description/status.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://docpub.state.or.us/oos/intro.jsf.
2. Search by offender `name` (add DOB or ID if known to narrow).
3. Read the record: `name`, `dob`, DOC identification number, photo, physical description, and custody status/location.
4. Disambiguate same-name results using DOB, ID, and photo.
5. Pivot: a confirmed custody period anchors a timeline; the photo feeds face comparison; cross-check registries like `[[sex-offender-us]]` for related records.

## Inputs → Outputs
- **In:** `name` (± DOB/ID)
- **Out:** `name`, `dob`, DOC `document-id`, `image` (photo), `physical-description`, custody status
- **Empty/negative result looks like:** no matching offender. That means no Oregon DOC record under that name — the person may have no Oregon custody history, be in a county jail (not state DOC), or use a different name/spelling. Absence isn't proof of no criminal history.

## Gotchas & OpSec
- Covers **Oregon state DOC** only — county jail, federal (BOP), and other states are separate systems.
- Records reflect state custody; released individuals may still appear historically.
- Confirm identity by DOB/photo, not name alone.
- OpSec: passive; an official public-records read.

## Overlaps ("do both")
- Pairs with `[[sex-offender-us]]` and other state DOC/inmate locators — corrections and registry systems are separate; check the relevant one for the jurisdiction, plus federal BOP for federal custody.

## Trust & verifiability
`trust: trusted` — this is the Oregon Department of Corrections' own system, so the data is authoritative for Oregon state custody. The only caveat is jurisdictional scope (state DOC only) — widen to county/federal/other-state systems as needed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oregon-offender-search |
</content>
