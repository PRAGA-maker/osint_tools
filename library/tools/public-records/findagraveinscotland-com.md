---
id: findagraveinscotland-com
name: findagraveinscotland.com
description: Use when you have a `name` of someone buried in Scotland and want their grave/headstone record — returns headstone `image`, dates (`dob`), cemetery `address`, and family `associate`s on the memorial.
url: https://www.findagraveinscotland.com/
category: public-records
path:
- public-records
bestFor: Locating a Scottish grave and its headstone inscription (dates, family names) via a grave-photography service.
selectorsIn:
- name
selectorsOut:
- image
- dob
- address
- associate
status: live
pricing: freemium
costNote: First consultation/search enquiry is free; viewing/downloading the high-resolution headstone photograph costs a small fee (around £3 per photo).
opsec: passive
opsecNote: Requesting a grave search is passive — you contact a genealogy service, not the subject's family, and it concerns a deceased person. You do disclose the name you're researching (and your contact email) to the service; use a research-only email if attribution matters.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A privately owned Scottish grave-photography service, unaffiliated with local councils; it has visited/photographed hundreds of cemeteries but coverage is partial and results come via manual fulfilment.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: true
aliases:
- Find A Grave in Scotland
- findagraveinscotland
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# findagraveinscotland.com

> A Scottish grave-photography and headstone-search service — confirm a burial and read the inscription (dates, family names) for someone interred in Scotland.

## When to use
You are tracing a deceased Scottish subject or ancestor and want to confirm a burial, capture the headstone inscription, or extract family details a memorial records (spouse, children, dates). Grave inscriptions frequently name multiple family members on one stone (`associate`) and give birth/death dates (`dob`), which extend a family tree and corroborate a death — valuable in genealogy-driven missing-persons work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.findagraveinscotland.com/ and use the search/enquiry (first consultation is free); you can register and email `enquiries@findagraveinscotland.com` with the `name` and any known details (cemetery, town, dates).
2. The service checks its records/photos (it covers hundreds of Scotland's 3000+ cemeteries) and responds — this is a manual, human-fulfilled step.
3. Review the headstone `image` and inscription: dates (`dob`/death), cemetery `address`/location, and other names on the stone (`associate`).
4. Pay the small fee to view/download the high-resolution photo if you need the full inscription.
5. Pivot: family names from the stone feed genealogy searches; confirmed dates feed BDM/obituary records.

## Inputs → Outputs
- **In:** `name` (+ any cemetery/town/date context)
- **Out:** headstone `image`, dates (`dob`/death), cemetery `address`, family `associate`s named on the memorial
- **Empty/negative result looks like:** no record/photo yet for that person — coverage is partial (not every cemetery/grave is photographed), so a null means "not in their collection," not "no such grave." Unmarked graves have no inscription to recover.

## Gotchas & OpSec
- Manual fulfilment: results arrive via human response, not an instant database — plan for turnaround.
- Partial coverage and a paywall for high-res photos; the free step confirms whether they hold anything.
- Privately run and unaffiliated with councils — for official records also check ScotlandsPeople.

## Overlaps ("do both")
- Pairs with `[[findagrave]]`/`[[billiongraves]]` and ScotlandsPeople — the global grave sites and the official Scottish registry cover records this niche service may lack, and vice versa.

## Trust & verifiability
`trust: community` — a genuine, useful private service, but coverage is incomplete and fulfilment is manual; cross-check dates against official Scottish BDM records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findagraveinscotland-com |
| category | public-records |
| selectorsIn → selectorsOut | name → image, dob, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
