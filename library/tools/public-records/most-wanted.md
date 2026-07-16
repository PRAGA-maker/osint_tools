---
id: most-wanted
name: FBI Most Wanted
description: Use when you have a `name` (or are working an image/case) and want to check whether the person appears on the FBI's wanted/most-wanted lists — returns official name, DOB, physical description, photos and case identifiers.
url: https://www.fbi.gov/wanted
category: public-records
path:
- public-records
bestFor: Checking whether a subject is a wanted fugitive, missing person, or seeking-information subject on the FBI's official lists.
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
costNote: Free official US government resource. No account, no payment.
opsec: passive
opsecNote: Fully passive — you browse a public FBI web page; no query about the subject reaches anyone but the FBI's public server. No alert is sent to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US Federal Bureau of Investigation site — authoritative for the persons it lists (fugitives, missing persons, seeking-information cases).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fbi-common-fraud-schemes-united-states
- fbi-information-technology-united-states
- federal-bureau-of-investigations-value
- most-wanted-criminal-pages
- sex-offender-registry-websites
- vault-fbi-gov
aliases:
- FBI Wanted
- fbi.gov/wanted
- Most Wanted
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# FBI Most Wanted

> The FBI's official wanted/missing/seeking-information lists — an authoritative check on whether a subject is a fugitive or one of the Bureau's missing-person cases.

## When to use
You have a `name` (or a face/case you're working) and want to know whether the FBI has a public notice on that person. The site covers not just Ten Most Wanted fugitives but many categories including Kidnappings & Missing Persons, Seeking Information, and crimes against children — directly relevant to missing-persons work. Each notice carries authoritative identity detail you can use to confirm or enrich.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.fbi.gov/wanted.
2. Use the site search or browse the relevant category (e.g. "Kidnappings & Missing Persons," "Seeking Information").
3. Search/scan for the subject `name` and open the matching notice.
4. Read the output: official `name` and aliases, `dob`, `physical-description` (height, weight, eyes, hair, scars/marks), photos (`image`), and case/field-office reference (`document-id`), plus the reward and contact field office.
5. Pivot: aliases and DOB feed people-search and records tools; the field office/case reference is the official contact for tips; photos feed reverse-image/face tools.

## Inputs → Outputs
- **In:** `name` (or category browse)
- **Out:** `name`/aliases, `dob`, `physical-description`, `image`, `document-id` (case reference)
- **Empty/negative result looks like:** no matching notice — meaning the person is not currently on an FBI public list (not proof they have no record). Notices are also removed once resolved.

## Gotchas & OpSec
- Covers only FBI federal notices — a subject can be wanted/missing at state or local level without appearing here. Combine with state and NamUs-type resources.
- Notices are added and removed over time; absence is not conclusive.
- OpSec: fully passive; public government page.

## Overlaps ("do both")
- Pairs with state missing-persons/most-wanted registries and inmate locators — the FBI list is federal and selective; those cover the far larger state/local population. Run both.

## Trust & verifiability
`trust: trusted` — first-party FBI content, authoritative for the persons it lists. Always follow the notice's official contact for reporting rather than acting independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | most-wanted |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, image, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
