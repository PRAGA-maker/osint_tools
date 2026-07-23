---
id: us-data-and-statistics
name: US Data and Statistics
description: Use when you have a place, agency, or topic and want the official US federal source for that statistic — returns links to Census, BLS, and other authoritative datasets.
url: https://www.usa.gov/statistics
category: public-records
path:
- public-records
bestFor: A signposting gateway from USA.gov to authoritative US federal statistical agencies and their data.
selectorsIn:
- address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free official US government portal; no account needed.
opsec: passive
opsecNote: A public government directory page — browsing it reveals nothing to any target and requires no login. Standard sock-puppet browsing hygiene is more than sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official USA.gov page run by the US General Services Administration; it curates links to first-party federal statistical agencies (Census, BLS, etc.).
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- state-local-tribal-gov-page-search
- usa-gov
aliases:
- USA.gov statistics
- US federal statistics directory
tags:
- data-and-statistics
- government
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# US Data and Statistics

> USA.gov's official signpost to federal statistics: it points you to the authoritative agency for population, labor, economic, and geographic data rather than serving the numbers itself.

## When to use
You need an authoritative US federal figure or dataset — Census demographics for an `address`/area, Bureau of Labor Statistics employment data, economic indicators — and want the official source rather than a secondary aggregator. Useful for contextualizing a location or an `employer-org` sector, or for confirming which government agency owns a given data domain. It is background/context tooling, not a person-locator, so missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.usa.gov/statistics.
2. Scan the curated categories (population/Census, jobs/economy, health, crime, etc.) and follow the link to the responsible agency.
3. On the destination agency site (e.g. Census QuickFacts, BLS), drill into the specific place or industry you're researching.
4. Use the figures as verifiable context to corroborate or challenge claims about a location or organization.

## Inputs → Outputs
- **In:** `address`/place or a topic area
- **Out:** links to authoritative federal datasets; area demographics and `employer-org`/industry statistics on the destination sites
- **Empty/negative result looks like:** the category you want isn't listed — it's a curated directory, not exhaustive; go to the agency (Census, BLS) directly for granular data.

## Gotchas & OpSec
- This page is a directory/gateway, not a dataset — the actual data lives on the agency sites it links to.
- Statistics are aggregate (area/industry level); they contextualize an investigation, they do not identify individuals.
- OpSec: fully passive public browsing; nothing is disclosed to any subject.

## Overlaps ("do both")
- Pairs with [[usa-gov]] and [[state-local-tribal-gov-page-search]] — this one routes you to federal *statistics*, while those route you to services and to state/local/tribal government pages for jurisdiction-specific records.

## Trust & verifiability
`trust: trusted` — an official GSA-run USA.gov page linking only to first-party federal agencies; the data it points to is as authoritative as US public statistics get.
