---
id: planningsystemni-gov-uk
name: NI Planning Register (planningsystemni.gov.uk)
description: Use when you have an `address` (or applicant/agent `name`) in Northern Ireland and want planning-application records tying a person to a property — returns name, address and employer-org (agents/architects).
url: https://planningregister.planningsystemni.gov.uk/simple-search
category: public-records
path:
- public-records
bestFor: Linking a Northern Ireland property address to the people who applied to develop it (owners, agents, architects).
selectorsIn:
- address
- name
- employer-org
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Official NI government planning portal; searching and viewing/downloading application documents is free with no account.
opsec: passive
opsecNote: Public government register; searching is anonymous and does not notify anyone. To comment on or track an application you must register, which is attributable — only use the anonymous search for OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NI's Department for Infrastructure / district councils on the Idox public-access platform; the authoritative statutory planning record for Northern Ireland.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- NI Planning Portal
- Northern Ireland Planning Register
- planningregister.planningsystemni.gov.uk
tags:
- propertysites
- Property Related Sites
- planning
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# NI Planning Register (planningsystemni.gov.uk)

> The official Northern Ireland planning register — search planning applications by address or name and read the documents, which routinely expose applicant and agent identities.

## When to use
You have a Northern Ireland `address` and want to know who has applied to build, extend, or change use on that property — or you have an applicant/agent `name` and want to find the properties tied to them. Planning application documents (forms, drawings, correspondence) frequently name the property owner, the applicant, the agent, and the architect/firm, making this a strong address↔person bridge for NI.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://planningregister.planningsystemni.gov.uk/simple-search.
2. Enter a keyword, application reference, or postcode/address, or use the Advanced search to search by applicant/agent name and date range.
3. Open a matching application. The **Details/Dates** tabs show applicant and agent names and the site address; the **Documents** tab holds the submitted forms and plans, which often carry fuller names, contact details, and firm/`employer-org` names.
4. Pivot: an applicant name feeds people-search and companies registries; an agent/architect firm feeds business lookups; the property address anchors neighbour/associate work.

## Inputs → Outputs
- **In:** `address` (or applicant/agent `name`, application ref)
- **Out:** `name` (applicant/owner/agent), `address` (site), `employer-org` (agent/architect firm)
- **Empty/negative result looks like:** "No results" for the search term — the property may simply have no planning history, not that the address is wrong.

## Gotchas & OpSec
- Names/contact detail in scanned documents can be redacted or partial; check multiple documents in the application bundle.
- The site runs the Idox public-access engine — search is anonymous; only commenting/tracking needs a login, which you should avoid for OSINT.
- Covers Northern Ireland only; England/Wales/Scotland use separate council portals.

## Overlaps ("do both")
- Pairs with a UK companies/registry lookup — use the agent or architect `employer-org` from the application to enrich the professionals involved, and cross-check owner names against property/electoral sources.

## Trust & verifiability
`trust: trusted` — a statutory government register on the standard Idox platform; the records are authoritative for what was formally applied for, though the personal detail within scanned documents varies in completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | planningsystemni-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | address, name, employer-org → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
