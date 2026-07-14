---
id: grave-info-us
name: GraveInfo.com (Snake Hill / Potter's Field burials)
description: Use when you have a `name` possibly buried in a pauper's grave in the NJ/NY Snake Hill (Secaucus) area — a niche potter's-field burial index returning burial listing and approximate date.
url: http://www.graveinfo.com
category: public-records
path:
- public-records
bestFor: Checking the Snake Hill / Secaucus Potter's Field pauper burial lists for an unclaimed/indigent death.
selectorsIn:
- name
selectorsOut:
- name
- dob
status: live
pricing: free
costNote: Free to browse the published burial lists; no account.
opsec: passive
opsecNote: Reading a static historical burial list is fully passive; nothing is submitted about a living subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A narrow, volunteer/enthusiast burial-index site (est. 2002) focused on Snake Hill potter's field — genuine but very limited in scope; the name "Grave Info (US)" overstates its coverage.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Grave Info US
- Snake Hill Potter's Field
tags:
- death
- obituary
- burial
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# GraveInfo.com (Snake Hill / Potter's Field burials)

> A narrow historical burial index — specifically the Snake Hill (Secaucus, NJ) potter's-field pauper/unclaimed burial lists — not a general US grave search despite its name.

## When to use
Only in a specific scenario: a subject may have died indigent, unclaimed, or unidentified in the New Jersey / New York City area and been buried in a potter's field. This site publishes burial lists (notably Snake Hill/Secaucus) that mainstream cemetery databases often omit — exactly the population that "falls through the cracks" in a long-term missing-person case. For anything else, use a broad death/cemetery database instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.graveinfo.com and open the relevant burial list (browse by state — NJ/NY — rather than expecting a slick name search).
2. Scan/CTRL-F the list for the subject's `name` and variants.
3. Note the burial listing and any date/plot detail.
4. Because coverage is tiny and hyper-local, treat a hit as a strong lead and a miss as inconclusive.
5. Pivot: a potter's-field burial → county medical examiner / unclaimed-persons records, NamUs, and the burying authority for identity confirmation.

## Inputs → Outputs
- **In:** `name` (and variants)
- **Out:** burial listing, approximate burial `dob`/date, plot context (very limited)
- **Empty/negative result looks like:** no match — expected for almost everyone, since the index covers only specific potter's-field lists; it does NOT rule out death or burial elsewhere.

## Gotchas & OpSec
- Extremely narrow scope: this is not a nationwide grave finder; do not treat a miss as meaningful.
- Historical/volunteer data with limited search UX; browse the lists manually.
- Pair with the ME/coroner and NamUs for the unidentified/unclaimed-deceased angle.

## Overlaps ("do both")
- Pairs with `[[findagrave-com]]`/BillionGraves (broad cemetery coverage) and NamUs (unidentified persons) — this fills the specific potter's-field gap those can miss.

## Trust & verifiability
`trust: community` — an authentic but niche enthusiast index; a match is a genuine lead to confirm through official ME/burial-authority records, and a non-match proves little given the narrow coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grave-info-us |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
