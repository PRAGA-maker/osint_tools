---
id: aws-public-datasets
name: AWS Public Datasets
description: Use when you need a large open dataset (satellite imagery, geospatial, genomic, web-crawl, etc.) to support an investigation — a catalog of free AWS-hosted data; returns bulk data, not selectors.
url: https://registry.opendata.aws/
category: public-records
path:
- public-records
bestFor: Finding and accessing large free public datasets (imagery, geospatial, crawl data) hosted on AWS for bulk analysis.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: The datasets are free to access; you only pay standard AWS costs if you process them inside AWS. Downloading/browsing many datasets is free.
opsec: passive
opsecNote: You are pulling published open datasets from Amazon's registry — no subject is contacted, so it is passive. Access via AWS ties usage to your AWS account; use appropriate account hygiene for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official AWS Registry of Open Data; each dataset is published by a named provider (NASA, NOAA, Common Crawl, etc.), so authority rests with the individual data owner.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- AWS Registry of Open Data
- registry.opendata.aws
tags:
- public-records
- open-data
- datasets
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# AWS Public Datasets

> Amazon's Registry of Open Data — a catalogue of large, free public datasets (satellite imagery, geospatial, genomic, web-crawl and more) you can pull for bulk analysis.

## When to use
This is a data source, not a selector lookup. Reach for it when an investigation needs raw material at scale: satellite/aerial imagery for geolocation, geospatial layers, Common Crawl web-scrape corpora for domain/mention hunting, weather/terrain data for chronolocation, or scientific datasets. Rather than any single answer about a person, it supplies the underlying datasets other analysis runs on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://registry.opendata.aws/.
2. Search or filter by topic/tag (satellite imagery, geospatial, climate, genomics, web crawl, etc.).
3. Open a dataset's entry to see its description, license, the responsible provider, and access methods (usually an S3 bucket, sometimes an API).
4. Access the data via the documented method — browse/download from S3, or process in AWS for very large sets.
5. Pivot: use the dataset in the relevant workflow (e.g. imagery into a geolocation analysis; Common Crawl into a domain/keyword search).

## Inputs → Outputs
- **In:** none (a dataset catalogue you browse by topic)
- **Out:** none directly — pointers to and access for large open datasets (imagery, geospatial, crawl, scientific)
- **Empty/negative result looks like:** no dataset matching your topic in the registry (it's broad but not exhaustive), or a dataset whose access requires AWS tooling you'd need to set up. It never contains data about a specific individual.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; using very large datasets requires data-engineering setup (S3/AWS).
- OpSec: **passive** — published open data, no subject contact. AWS access is tied to your account.
- Scope and size: datasets are big and general-purpose; check each dataset's license and provider, and be ready for the compute/storage needed to work with terabyte-scale sources.

## Overlaps ("do both")
- Complements other open-data catalogs (data.gov, `[[open-data-network]]`, Google/UN datasets) — AWS's registry skews toward large machine-readable/imagery datasets, while place-focused portals give tabular civic statistics.

## Trust & verifiability
`trust: trusted` — the official AWS Registry of Open Data. Each dataset lists a named, authoritative provider (NASA, NOAA, Common Crawl, etc.); verify licensing and provenance per dataset before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aws-public-datasets |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
