---
id: ukbmd-org-uk
name: UKBMD
description: Use when you have a `name` and want UK births/marriages/deaths records — a portal routing you to local transcribed civil-registration indexes (1837 onward) for dates, family links, and districts.
url: https://www.ukbmd.org.uk/index.php?form_action=local
category: public-records
path:
- public-records
bestFor: Finding the right local UK BMD index for a person and pulling birth/marriage/death dates, registration districts, and family connections.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
- address
status: live
pricing: free
costNote: Free directory; the linked local BMD index searches are free. Ordering an official certificate from a register office costs a fee.
opsec: passive
opsecNote: A directory plus public genealogical indexes — read-only and notifies no one. Passive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing portal to local UK register-office index transcriptions; UKBMD curates links, the underlying local BMD projects hold the (transcribed) data.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- UK BMD
- ukbmd.org.uk
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- civil-registration
- uk
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# UKBMD

> The gateway to UK civil-registration indexes: from a name to local birth, marriage, and death records (1837→), with the district and family links they reveal.

## When to use
You have a `name` tied to the UK and want the genealogical backbone: when they were born/married/died, in which registration district, and who they connect to (a marriage record names a spouse; deaths give an age/DOB). This anchors identity, gives an approximate `dob`, places the person geographically, and surfaces `associate`/family links — the groundwork for a fuller person search or for locating living relatives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ukbmd.org.uk/ and choose the Local BMD / county section for the area of interest.
2. Follow the link to the relevant local BMD project or county index site.
3. Search that index by `name` (and year range/district); read the transcribed entry — event type, date, district, and reference.
4. If needed, order the official certificate from the register office (fee) for full detail.
5. Pivot: a marriage entry's spouse is an `associate`; a registration district narrows other searches; a death age yields an approximate `dob` for people-search disambiguation.

## Inputs → Outputs
- **In:** `name` (+ approximate year/area)
- **Out:** BMD event `name`s, dates (`dob`/death), registration district (`address`), family `associate` links
- **Empty/negative result looks like:** no index entry — the county may not be covered by a local BMD project, the record predates 1837, or the spelling differs. UKBMD's coverage is patchy by area, so absence here isn't proof no record exists; try the GRO index or FreeBMD.

## Gotchas & OpSec
- Two-hop and uneven: UKBMD is a *directory* to local projects whose coverage varies widely by county — a gap is a coverage gap, not a data gap.
- Indexes are transcriptions — confirm critical facts against the certificate or GRO index.
- OpSec: **passive**, read-only genealogical data.

## Overlaps ("do both")
- Pairs with FreeBMD and the GRO online index — UKBMD routes to local transcriptions (often with more district detail), while FreeBMD/GRO give national coverage; cross-check for completeness.

## Trust & verifiability
`trust: community` — a curated portal to volunteer/local transcriptions; treat entries as reliable leads and verify anything decisive against the official certificate or GRO record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukbmd-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
