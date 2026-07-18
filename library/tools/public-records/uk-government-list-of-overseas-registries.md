---
id: uk-government-list-of-overseas-registries
name: UK Government List of Overseas Registries
description: Use when you need the official company registry for a given country — returns links to worldwide corporate registries so you can pivot to employer-org filings, directors, and addresses.
url: https://www.gov.uk/government/publications/overseas-registries
category: public-records
path:
- public-records
bestFor: A country-by-country index of official company registries worldwide, curated by UK Companies House.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free GOV.UK publication; no account. (It is a directory of links — the registries it points to may have their own fees.)
opsec: passive
opsecNote: Just a reference list on GOV.UK; you read it, nothing is queried about a subject. OpSec considerations apply to the individual registries you then visit, not to this page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by UK Companies House; the list itself is authoritative, though it was last refreshed in 2018 so some links may have moved.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Companies House overseas registries
- gov.uk overseas registries
tags:
- public-records
- company-search
- registries
- reference
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# UK Government List of Overseas Registries

> A GOV.UK directory from Companies House pointing to the official company registry of nearly every country — your jumping-off point when you need corporate records in a jurisdiction you don't know.

## When to use
You have an `employer-org` registered abroad (or a subject linked to a foreign company) and need the authoritative registry to pull filings, directors, and the registered `address`. Rather than guessing each country's system, this page lists them grouped by region with links, so you can go straight to the right official source and pivot from a company name to its statutory record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/government/publications/overseas-registries.
2. Find the country of interest (the list is grouped by region) and follow the link to that jurisdiction's official company registry.
3. On the registry, search the company/person to retrieve incorporation details, directors/officers, and the registered address (each registry differs in fields and cost).
4. Pivot: named directors become `associate`/`name` leads; the registered address corroborates location; cross-reference against `[[crunchbase]]` and OpenCorporates-style aggregators.

## Inputs → Outputs
- **In:** the country + `employer-org` you need records for
- **Out:** a link to the correct official registry → (there) `employer-org` filings and registered `address`
- **Empty/negative result looks like:** a country not listed, or a link that has since moved/broken — the page dates from 2018, so confirm the registry's current URL if a link fails.

## Gotchas & OpSec
- Human-in-the-loop: none for the list; individual registries may require accounts or fees.
- OpSec: passive — it's a reference page. Apply OpSec to the registries you visit next.
- Staleness: last updated 2018; some registry URLs have changed. If a link 404s, search for the country's current official corporate registry and verify it's the government source.

## Overlaps ("do both")
- Pairs with OpenCorporates and `[[crunchbase]]` — this points you to the primary official registry, while aggregators give a faster cross-jurisdiction search and additional context.

## Trust & verifiability
`trust: trusted` — it is an official Companies House publication listing government registries; the destinations are authoritative, but re-verify any link that has aged out.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-government-list-of-overseas-registries |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
