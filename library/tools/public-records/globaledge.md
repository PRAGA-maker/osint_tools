---
id: globaledge
name: globalEDGE
description: Use when you have an `employer-org`, industry or country in an investigation and want authoritative business/economic context — returns country profiles, trade statistics, industry data and links to official registries.
url: https://globaledge.msu.edu
category: public-records
path:
- public-records
bestFor: Background research on a company's country, industry and trade environment, plus pointers to official corporate data sources.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- domain
status: live
pricing: free
costNote: Free public academic resource operated by Michigan State University; no account required.
opsec: passive
opsecNote: You read published reference data; nothing about your subject is submitted. Fully passive and anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michigan State University's International Business Center; a long-standing, reputable academic reference used widely in trade and business research.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- central-and-eastern-european-business-directory
- global-edge-resource-directory
- globaledge-database-of-international-business-statistics
- national-company-registers
aliases:
- global Edge
- globaledge.msu.edu
tags:
- company-research
- trade
- country-profiles
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# globalEDGE

> Michigan State University's international-business knowledge portal — the context layer for a corporate or cross-border investigation: country profiles, trade stats, industry data and links onward to official sources.

## When to use
Your case touches a company (`employer-org`), an industry, or a specific country, and you need reliable background rather than a person lookup. globalEDGE gives statistical and structural context — a country's economy/politics/regulatory setup, an industry's landscape, trade-bloc memberships, and curated directories that point to official company registries and business-data sources. It won't identify an individual, but it grounds a corporate/geographic investigation and routes you to the authoritative primary sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://globaledge.msu.edu.
2. Use the section that fits your question:
   - **Global Insights → Countries** for a country's economy, history, and business environment.
   - **Industries** for sector context around a target company.
   - **Trade blocs** for regional trade relationships.
   - **Reference Desk / resource directories** for curated links to official registries, statistics and databases.
3. Read the profiles/stats for context, and follow the curated links out to primary sources.
4. Pivot: use the directory links (and `[[national-company-registers]]`) to reach the official register for the company's jurisdiction, then confirm officers/filings there.

## Inputs → Outputs
- **In:** `employer-org` / industry / country of interest
- **Out:** country and industry context, trade statistics, and curated `domain` links to official business/registry sources
- **Empty/negative result looks like:** thin or dated coverage for a very small country/niche — globalEDGE is a reference portal, not a live database, so treat it as background and go to the primary source it links for current facts.

## Gotchas & OpSec
- It's context/reference, not a person or company *record* lookup — don't expect to search a specific business's filings here; use the registries it links.
- Statistics are periodically updated academic aggregates; for current figures, follow through to the cited primary source.
- Low direct missing-persons relevance; most useful in fraud/corporate/cross-border cases as scaffolding.

## Overlaps ("do both")
- Feeds naturally into `[[national-company-registers]]` and `[[opencorporates]]`: globalEDGE frames the country/industry and points you to the official register, which then yields the actual corporate record and officers.

## Trust & verifiability
`trust: trusted` — a reputable, long-running Michigan State University resource. Its context and statistics are academically curated; for point-in-time accuracy, verify specific figures against the primary sources globalEDGE cites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | globaledge |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
