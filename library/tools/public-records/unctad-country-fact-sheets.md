---
id: unctad-country-fact-sheets
name: UNCTAD Country Fact Sheets
description: Use when you have a country (`geolocation`) and want its foreign-investment profile — FDI flows, M&A activity, largest TNCs and regulatory changes — returns `employer-org` leads and context.
url: http://unctad.org/en/Pages/DIAE/World%20Investment%20Report/Country-Fact-Sheets.aspx
category: public-records
path:
- public-records
bestFor: Getting a country's FDI indicators and its largest transnational corporations for economic/corporate context.
selectorsIn:
- geolocation
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free official UN (UNCTAD) publication; fact sheets and statistical annexes downloadable without registration.
opsec: passive
opsecNote: You are reading published UN economic statistics — nothing touches any subject and there is no login. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party UN Conference on Trade and Development data; authoritative for FDI and investment figures at the country level.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- unctad-stat
aliases:
- UNCTAD World Investment Report Country Fact Sheets
tags:
- public-records
- economic-data
- fdi
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# UNCTAD Country Fact Sheets

> Official UN per-country investment snapshots — FDI flows and stocks, M&A, the largest transnational corporations operating there, and regulatory changes.

## When to use
This is country-level economic context, not a people finder. Reach for it when an investigation touches cross-border business, a company operating in a given country, or the investment climate of a `geolocation`. Each fact sheet names the largest transnational corporations (TNCs) active in a country and summarizes FDI activity and recent regulatory changes — useful for corporate due diligence, understanding who the major foreign investors/employers are, or corroborating a business's plausibility in a jurisdiction.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the World Investment Report Country Fact Sheets page (link above; if UNCTAD's site has reorganized, search "UNCTAD World Investment Report country fact sheets" for the current location).
2. Select the target country from the dropdown (195+ countries, plus regional sheets).
3. Download/read the PDF fact sheet: FDI inflows/outflows and stocks, cross-border M&A, largest TNCs, and regulatory changes.
4. Extract the named TNCs (`employer-org`) and FDI trends relevant to your subject or company of interest.
5. Pivot: run named corporations through company-registry and corporate-OSINT tools; use FDI/regulatory context to frame a business or individual's economic footprint.

## Inputs → Outputs
- **In:** a country (`geolocation`)
- **Out:** `employer-org` (largest TNCs operating in-country), plus `geolocation`-level FDI statistics and regulatory context
- **Empty/negative result looks like:** a country with sparse data or an older fact-sheet vintage. It reports macro/corporate aggregates only — it never contains individuals.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive**; published statistics, no subject interaction.
- Data is periodic (tied to the annual World Investment Report), so figures lag real time. It is aggregate/corporate — do not expect anything about a specific person.

## Overlaps ("do both")
- Pairs with company registries and other UN/World-Bank economic datasets — UNCTAD supplies the FDI and TNC layer, while registries give the concrete corporate records for the firms it names.

## Trust & verifiability
`trust: trusted` — it is first-party UNCTAD (United Nations) data, authoritative for country-level investment statistics and published with methodology in the World Investment Report.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unctad-country-fact-sheets |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
