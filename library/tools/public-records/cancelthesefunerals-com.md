---
id: cancelthesefunerals-com
name: Cancelthesefunerals.com
description: Use when you have a `name` and want to check whether a person appears in the US Social Security Death Master File — returns death record fields (dob, date of death, last-residence ZIP, partial SSN).
url: http://cancelthesefunerals.com/
category: public-records
path:
- public-records
bestFor: Checking a name against a public copy of the Social Security Death Master File to confirm (or rule out) a US death record.
selectorsIn:
- name
selectorsOut:
- dob
- address
- document-id
status: degraded
pricing: free
costNote: Free public-interest project; no account or payment. The site is intermittently reachable and its data is a historical DMF copy, not a live feed.
opsec: passive
opsecNote: Read-only search of a static death-index copy hosted by a third party. You submit only a name; nothing is sent to the subject. As with any third-party mirror, assume the operator can log queries — use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-operator activist project (created by Tom Alciere) republishing the government Death Master File; the underlying DMF is authoritative but this mirror is unofficial, possibly stale, and known to be flaky.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- sortedbybirthdate
- legacy-com
aliases:
- Cancel These Funerals
- Death Master File mirror
- DMF lookup
tags:
- death-records
- vital-records
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Cancelthesefunerals.com

> A public, free-text-searchable mirror of the US Social Security Death Master File (DMF) — a fast way to check whether a name carries a federal death record.

## When to use
You have a `name` (ideally with an approximate age/DOB or state) and need to establish whether that person is recorded as deceased in the US Social Security system. This is decisive in missing-persons work: a DMF hit strongly indicates the person is dead (and gives a date/place to corroborate against obituaries and cemetery records), while a clean check keeps a living-person line of inquiry open. The site was set up specifically to expose the ~12,000 people/year the SSA *wrongly* marks dead — so a hit is a lead to verify, not proof.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://cancelthesefunerals.com/ (may be slow or intermittently down — retry).
2. Search by `name`; narrow with any date/place detail the interface allows.
3. Read the record: DMF entries typically expose `dob`, date of death, last-residence ZIP (`address`), and a partial SSN (`document-id`).
4. Corroborate: cross-check the date/place of death against `[[legacy-com]]` obituaries and cemetery/find-a-grave records — do not treat a single DMF hit as conclusive given the known false-positive rate.
5. Pivot: a last-residence ZIP + DOB feeds people-search and vital-records lookups; a confirmed death closes or redirects the case.

## Inputs → Outputs
- **In:** `name` (+ optional DOB/state)
- **Out:** `dob`, date of death, last-residence ZIP (`address`), partial SSN (`document-id`)
- **Empty/negative result looks like:** no matching record — meaning either the person is not in the DMF (likely alive, or death not reported to SSA) or the name/dates are off. Absence is not proof of life.

## Gotchas & OpSec
- The mirror is **flaky** (intermittent 503s) and the data is a static, possibly outdated DMF copy — hence `status: degraded`. If unreachable, use another DMF/SSDI front end.
- The DMF itself contains errors (living people listed as dead); always corroborate before acting on a hit.
- Recent deaths (last ~3 years) are restricted in the official DMF and may be absent here.
- OpSec: **passive** — a name search against a static index.

## Overlaps ("do both")
- Pairs with `[[sortedbybirthdate]]` (another SSDI/DMF-style front end for cross-checking) and `[[legacy-com]]` (obituaries) — use the DMF for the federal death record and obituaries for the human detail (family, service location) that confirms it.

## Trust & verifiability
`trust: community` — the source data is the authoritative federal Death Master File, but this is an unofficial single-operator mirror that may be stale and is known to be intermittently offline; corroborate every hit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cancelthesefunerals-com |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
