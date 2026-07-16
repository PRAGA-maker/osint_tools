---
id: taxpolicy-org-uk
name: Tax Policy Associates UK PSC Map
description: Use when you have a person `name`, `address` or company `employer-org` and want to map UK companies' Persons with Significant Control geographically — returns employer-org, associate and address links to beneficial owners.
url: https://taxpolicy.org.uk/wp-content/assets/pscs_map_v3.html
category: public-records
path:
- public-records
bestFor: Mapping UK beneficial owners (PSCs) to companies and locations on an interactive map.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- associate
- address
- name
status: live
pricing: free
costNote: Free interactive tool published by Tax Policy Associates; no account or payment required.
opsec: passive
opsecNote: A static, client-side map served from a public site; searching and filtering happen in your browser, so no query reaches the subject and nothing is logged against them. Standard public-records browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Tax Policy Associates (Dan Neidle), a well-regarded independent UK tax-transparency body, from official Companies House PSC data; derivative of primary data but reputably assembled.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- PSC map
- Tax Policy Associates persons with significant control map
tags:
- company
- beneficial-ownership
- uk
- public-records
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Tax Policy Associates UK PSC Map

> An interactive map of UK companies' Persons with Significant Control, letting you find beneficial owners by name, company or geography from Companies House data.

## When to use
You're investigating a UK corporate footprint and have a person `name`, an `address`/area, or a company `employer-org`, and you want to see the beneficial-ownership picture spatially — who controls which companies and where they're clustered. It draws on Companies House PSC filings but adds map-based search and location context that the raw register doesn't, making it good for spotting an individual's web of controlled entities and co-located associates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://taxpolicy.org.uk/wp-content/assets/pscs_map_v3.html and let the company dataset load (it can take a minute).
2. Search for a company, person, or draw/zoom to an area on the map to filter PSCs by location.
3. Read the output: pins/records show a PSC linked to a UK company plus its location; toggle filters (active, dormant, in default, former PSC, dissolved) to focus.
4. Pivot: note controlled `employer-org`s and co-located `associate`s, then confirm each against the authoritative Companies House record before relying on it.

## Inputs → Outputs
- **In:** person `name`, `address`/area, or company `employer-org`
- **Out:** `employer-org` (controlled companies), `associate` (co-owners/controllers), `address` (PSC/company locations), `name`
- **Empty/negative result looks like:** no pins/records for the search — means no matching PSC in the dataset (or the entity is outside the map's snapshot); verify against Companies House rather than concluding absence.

## Gotchas & OpSec
- Derivative dataset: it's a snapshot of Companies House PSC data, so it can lag live filings — treat it as a lead layer and confirm on the official register.
- Large in-browser dataset; slow to load and best on desktop.
- OpSec: fully passive, client-side public-records browsing.

## Overlaps ("do both")
- Pairs with authoritative registry lookups like `[[company-check]]` and `[[companies-and-orgs-search-engine]]` — the map surfaces the ownership cluster and geography, those confirm each company's live record.

## Trust & verifiability
`trust: trusted` — assembled by a reputable independent transparency body from official Companies House data; the map is a well-built derivative, so verify specific findings against the primary register for currency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | taxpolicy-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, associate, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
