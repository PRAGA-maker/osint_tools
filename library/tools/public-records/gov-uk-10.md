---
id: gov-uk-10
name: GOV.UK Find Driving Instructors (DVSA)
description: Use when you have a `name` or `geolocation` for a UK subject who may be a driving instructor and want to confirm DVSA approval — returns approved-instructor listing, grade, and business location.
url: https://www.gov.uk/find-driving-schools-and-lessons
category: public-records
path:
- public-records
bestFor: Confirming whether a person is a DVSA-approved UK driving instructor (ADI) and their grade/location.
selectorsIn:
- name
- address
- geolocation
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free UK government service; no account or payment required.
opsec: passive
opsecNote: This is a public GOV.UK lookup — the instructor is not notified. Only ADIs who opt in are listed, so absence is not evidence. Searches are anonymous; no sock-puppet needed beyond ordinary browsing hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Driver and Vehicle Standards Agency (DVSA), the UK statutory regulator of driving instructors — a first-party authoritative source.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Find driving instructors
- DVSA approved driving instructor search
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# GOV.UK Find Driving Instructors (DVSA)

> The DVSA's public directory of approved UK driving instructors — a licensing check that ties a name to an approval status, grade, and business location.

## When to use
You have a UK subject who may work (or has claimed to work) as a driving instructor, and you want to confirm they are DVSA-approved and where they operate. Useful for corroborating a stated occupation, placing someone in a `geolocation` (their instruction area), or linking a person to a driving-school `employer-org`. Best treated as a confirmation/enrichment step rather than a discovery tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/find-driving-schools-and-lessons and follow the "find driving instructors" service link.
2. Enter a postcode or town (`geolocation`/`address`) to list approved ADIs in that area.
3. Read the results: instructor/business name, DVSA approval status, and grade (if the instructor chose to publish it).
4. To verify a specific named instructor who isn't listed (listing is voluntary), the page directs you to contact DVSA directly with the instructor's name and ADI number.
5. Pivot: a confirmed instructor + business name feeds company/records lookups; the area of operation narrows a `geolocation`.

## Inputs → Outputs
- **In:** `geolocation`/`address` (postcode or town); `name`/ADI number for direct verification
- **Out:** approved-instructor `name`, business/school `employer-org`, service `address`/area, DVSA grade
- **Empty/negative result looks like:** no listed instructors nearby, or your named subject absent — because listing is opt-in, this is NOT proof the person is not an approved instructor; verify with DVSA.

## Gotchas & OpSec
- Coverage gap: only ADIs who volunteer to be listed appear, so absence proves nothing.
- Scope: strictly UK (England, Scotland, Wales) driving instructors — irrelevant outside that occupation and country.
- OpSec: passive public lookup; nothing is disclosed to the subject.

## Overlaps ("do both")
- Pairs with UK companies/records tools like `[[gov-im]]` or Companies House when the instructor trades through a limited company — the licensing record and the company record corroborate the person from different angles.

## Trust & verifiability
`trust: trusted` — a first-party DVSA regulator directory; a listing is authoritative confirmation of approval, though absence is inconclusive because listing is voluntary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-10 |
| category | public-records |
| selectorsIn → selectorsOut | name → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
