---
id: myplan-ie
name: myplan.ie
description: Use when you have an Irish property `address`/location and want planning applications there (applicant names, addresses) — returns name, address, and employer-org leads.
url: https://myplan.ie/national-planning-application-map-viewer/
category: public-records
path:
- public-records
bestFor: Searching Ireland's national planning-application map for applications at a location — surfacing applicant names, addresses, and development details from the last ~10 years.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free official government tool; planning data is public and downloadable with no account.
opsec: passive
opsecNote: Official government planning portal — searching does not notify anyone and reveals only your IP. Fully passive. Planning records are public by law, but treat any personal details found (applicant home addresses) responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Irish government resource (Department of Housing, Local Government and Heritage) aggregating local-authority planning data.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ros-gov-uk-2
- cro-ie-2
aliases:
- MyPlan
- myplan.ie planning map
- national planning application map viewer
tags:
- propertysites
- Property Related Sites
- planning
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# myplan.ie

> Ireland's official national planning-application map viewer — search any location for planning applications from the last ~10 years and read the applicant and development details.

## When to use
You have an Irish property `address`/location (or a `name`/`employer-org` you want to place at one) and want to see planning-application activity. Planning records are a rich, under-used identity source: they name the applicant (often the property owner or developer), give a contact `address`, describe the works, and carry dates — tying a person or company to a specific property and timeline. Useful for confirming residence/ownership, finding a developer's other projects, or corroborating an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://myplan.ie/national-planning-application-map-viewer/ (an ArcGIS map app).
2. Navigate/zoom to the area or search by address/location; planning applications appear as map points.
3. Click an application to read: applicant `name`, applicant `address`, development description, decision status, and the local-authority planning reference.
4. For full case files, follow through to the relevant local authority's planning portal.
5. Pivot: applicant name/address feeds people-search and [[cro-ie-2]] (if a company); the site location feeds [[ros-gov-uk-2]]-style land/property checks (Scotland) or Irish property registers.

## Inputs → Outputs
- **In:** property `address`/location (or a `name`/`employer-org` to look for as an applicant)
- **Out:** applicant `name`, applicant `address`, development details, `employer-org` (if a company applied), planning reference and dates
- **Empty/negative result looks like:** no applications at a location — most properties have no recent planning activity, so absence tells you nothing about who lives/owns there; it only means no application in the covered window.

## Gotchas & OpSec
- Coverage is planning applications from roughly the last ten years across Irish local authorities — older or non-planning matters won't appear.
- Applicant ≠ current owner necessarily (could be an agent, developer, or prior owner) — treat the name as a strong lead to confirm.
- OpSec: passive — a public government portal with no notification.

## Overlaps ("do both")
- Pairs with [[cro-ie-2]] (if the applicant is a company) and property/land registers — planning data names people/companies tied to a site; the registers confirm ownership.

## Trust & verifiability
`trust: trusted` — first-party Irish government data aggregating official local-authority planning records. Application details are authoritative public records; interpret "applicant" carefully before equating it with the current owner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myplan-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
