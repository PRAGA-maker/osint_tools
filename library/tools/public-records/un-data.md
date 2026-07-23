---
id: un-data
name: UN Data
description: Use when you have a country/region and topic and want authoritative UN statistics — returns official demographic, economic, and social datasets for context and corroboration.
url: http://data.un.org
category: public-records
path:
- public-records
bestFor: A single search portal across the UN's official statistical databases (population, trade, social indicators, etc.).
selectorsIn:
- address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free official United Nations data portal; no account needed.
opsec: passive
opsecNote: "A public UN statistics portal — browsing it discloses nothing to any subject and needs no login. The data is aggregate (country/region level) with no personal information, so there's no privacy exposure in querying it. Standard sock-puppet browsing is more than sufficient."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UN Statistics Division portal (UNdata) aggregating first-party UN-system databases; authoritative for international statistics, though some series lag by a year or more.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- statistics-and-data
- un-comtrade-database
- un-security-council-consolidated-list
- unstats-social-indicators
aliases:
- UNdata
- data.un.org
tags:
- data-and-statistics
- united-nations
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# UN Data

> The UN's central statistics portal (UNdata): one search across dozens of official UN-system databases — population, trade, labor, health, energy — for authoritative country/region context.

## When to use
You need reliable international statistics to contextualize an investigation — demographics for a country/region tied to an `address`, trade flows, labor/industry (`employer-org` sector) data, social indicators — and want first-party UN figures rather than a secondary aggregator. Background/context tooling for corroborating claims about places and economies. Aggregate data only, so no direct person-finding value; missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://data.un.org and search a topic or country, or browse by database (UN Comtrade, Population Division, ILOSTAT, etc.).
2. Select a dataset and filter by country/region, year, and indicator.
3. Read/export the figures (many series download as CSV) for the specific place/period.
4. Use the numbers to corroborate or challenge claims about a location, economy, or sector in your case.
5. For entity/sanctions context, pivot to the related UN lists rather than expecting them here.

## Inputs → Outputs
- **In:** country/region (`address`) + topic
- **Out:** official UN statistics (demographic, economic, social); sector/`employer-org` context on the destination databases
- **Empty/negative result looks like:** no series for that country/period — the indicator isn't collected/reported there, or lags; it's aggregate reference data, so it never returns anything about an individual.

## Gotchas & OpSec
- It's a **portal** over many databases — the actual series live in the source database (Comtrade, ILOSTAT); note which one a figure comes from and its methodology.
- Data can lag a year or more and country reporting quality varies — cite the source series and year.
- Aggregate only: this contextualizes, it never identifies people.

## Overlaps ("do both")
- Pairs with its UN siblings [[un-comtrade-database]], [[unstats-social-indicators]], and [[un-security-council-consolidated-list]] — UNdata is the general statistics gateway; the siblings go deep on trade, social indicators, and sanctioned entities respectively.

## Trust & verifiability
`trust: trusted` — the official UN Statistics Division portal aggregating first-party UN databases; figures are authoritative, with the usual caveats of reporting lag and cross-country methodology differences.
