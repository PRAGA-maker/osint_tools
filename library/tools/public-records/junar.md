---
id: junar
name: Junar
description: Use when you want to browse government/agency open-data catalogs — Junar powers many public data portals whose datasets you can search and export, no account.
url: http://junar.com
category: public-records
path:
- public-records
bestFor: Recognizing and searching Junar-powered open-data portals (city/agency datasets, tables, APIs) as a public-records source.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: The Junar platform itself is a paid B2B product sold to governments/agencies, but the public open-data portals it hosts are free for anyone to browse, filter, download, and query via API.
opsec: passive
opsecNote: Browsing a public open-data portal is passive — you query published datasets, not any individual, and nothing reaches a subject. Note that portal operators can log downloads/API calls; use a neutral connection if you'd rather not have bulk pulls tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Junar is an established open-data platform (used by governments such as the City of Palo Alto and agencies in Chile and Argentina); the data is published by the hosting authority, so authority rests with the source agency, not Junar.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Junar Data Platform
- junar.com
tags:
- data-and-statistics
- open-data
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Junar

> A commercial open-data platform that powers public government/agency data portals. For OSINT it's a *source-recognition* tool: know the platform, and you know how to search and export the datasets it hosts.

## When to use
You're doing public-records/data research and land on (or want to find) an open-data portal — city budgets, permits, procurement, transport, energy, demographic tables. Many such portals worldwide run on Junar (often at `opendata.<org>` or `data.<city>` addresses). Recognizing it tells you the portal offers consistent search, dataset downloads (CSV/JSON), visualizations, and a data API you can query directly. Useful for jurisdiction-level facts that corroborate a case, not for looking up an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Identify a Junar-powered portal (Junar's own site lists customers; portals expose Junar's dataset/table UI and an API).
2. Search the catalog by keyword, category, or agency for the dataset you need.
3. Open a dataset to view the table, filter/pivot it, and note its update cadence and source agency.
4. Export CSV/JSON, or hit the portal's data API for programmatic pulls.
5. Attribute findings to the **publishing agency** (the authority), citing the portal URL and dataset version/date.

## Inputs → Outputs
- **In:** a topic/dataset query within an open-data portal (jurisdiction-level, not a person selector)
- **Out:** downloadable datasets, tables, and API endpoints of public records
- **Empty/negative result looks like:** the portal has no dataset covering your topic, or the data is aggregated too coarsely to answer your question — pivot to the agency's primary site.

## Gotchas & OpSec
- Junar hosts data; it doesn't vouch for it — accuracy and freshness are the publishing agency's, so cite the source and dataset date.
- The paid platform ≠ the free portals; you don't need a Junar account to use the public data.
- Coverage is wherever an org chose Junar; it's not a universal open-data index — combine with CKAN/Socrata portals and national data catalogs.

## Overlaps ("do both")
- Complements other open-data platform portals (CKAN, Socrata) and national statistics sites — different governments pick different platforms, so search several to find the dataset that answers your question.

## Trust & verifiability
`trust: trusted` — a mature, government-adopted platform; the data's authority comes from the publishing agency, so verify each dataset's source and update date rather than trusting the portal wrapper alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | junar |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
