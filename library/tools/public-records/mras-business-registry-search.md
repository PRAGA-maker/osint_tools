---
id: mras-business-registry-search
name: Canada's Business Registries (MRAS)
description: Use when you have a company `name` or corporation number in Canada and want its official registry record — returns jurisdiction, status, registered office, and identifiers.
url: https://canadasbusinessregistries.ca
category: public-records
path:
- public-records
bestFor: Searching businesses/corporations across participating Canadian jurisdictions from one official portal.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- document-id
status: live
pricing: free
costNote: Free official Government of Canada service (Multi-jurisdictional Registry Access Service); no account for basic search.
opsec: passive
opsecNote: An official public registry — you search a business, not a private person, and nothing about your investigation is disclosed to the subject. Fully passive. The registered addresses returned are public filings, not necessarily current personal residences.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Government of Canada (ISED) aggregating official provincial/federal corporate registries; authoritative primary-source data for participating jurisdictions.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
aliases:
- MRAS
- Canada's Business Registries
- canadasbusinessregistries.ca
tags:
- public-records
- corporate-registry
- canada
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Canada's Business Registries (MRAS)

> The Government of Canada's aggregated corporate-registry search — look up a business across participating federal and provincial jurisdictions from one authoritative portal.

## When to use
You have a Canadian business `name`, corporation number, or an `employer-org` tied to your subject and want the official registry record: which jurisdiction it's registered in, its status (active/dissolved), registered office `address`, and corporate identifiers (`document-id`). In a people investigation this ties a subject to a company, confirms a business is real and active, provides an official address, and gives corporation numbers to pull deeper filings from the underlying provincial registry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://canadasbusinessregistries.ca (Government of Canada / MRAS portal).
2. Search by business `name` or corporation number.
3. Open a result: registering jurisdiction, status, registration date, registered office `address`, and identifiers.
4. For officers/directors and full filings, follow through to that jurisdiction's own registry (coverage varies by province).
5. Pivot: the registered `address` and corporation `document-id` feed property/court/registry lookups and connect the subject to the entity.

## Inputs → Outputs
- **In:** business `name` / corporation number (`employer-org`)
- **Out:** jurisdiction, status, registered office `address`, corporation `document-id`
- **Empty/negative result looks like:** no match — the entity may be registered only in a non-participating jurisdiction, dissolved and purged, or named differently; check the specific provincial registry directly.

## Gotchas & OpSec
- **Coverage is by participating jurisdiction** — not every province exposes full data here; a miss may just mean "not in this aggregator," so go to the provincial registry.
- Registered office ≠ a person's home address; treat it as a corporate filing.
- OpSec: **passive** — official public record; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` — OpenCorporates aggregates company data globally with officer links; MRAS is the authoritative Canadian primary source. Use MRAS to confirm the official record, OpenCorporates to map directors/associates across entities.

## Trust & verifiability
`trust: trusted` — a government-operated aggregator of official registries; the data is primary-source and citable for participating jurisdictions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mras-business-registry-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
