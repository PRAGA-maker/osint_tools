---
id: investigative-dashboard
name: Investigative Dashboard
description: Use when you have a company or person and want to find the right corporate/land/court registry to trace ownership across borders — returns a global index of 1,000+ record sources plus research support.
url: https://id.occrp.org/
category: transportation
path:
- transportation
bestFor: OCCRP's global index of business, land, and court registries in 180+ countries — the starting point for cross-border ownership tracing.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- associate
- address
status: live
pricing: free
costNote: The Global Registry Search is free and open to anyone; expert research-desk assistance and full accounts are reserved for OCCRP member centers and reporting partners.
opsec: passive
opsecNote: Browsing OCCRP's registry index is passive. Following a link to a national registry may load a site that logs searches — apply OpSec there, and note some registries reveal that a filing was viewed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Organized Crime and Corruption Reporting Project (OCCRP), a respected investigative-journalism consortium; it curates authoritative official registry sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- catalogue-of-research-databases-occrp-id
- occrp-aleph
- data-occrp-org
- occrp-org
- organized-crime-and-corruption-reporting-project
- the-pegasus-project-occrp
- visual-investigative-scenarios
tags:
- toddington
- curated-directory
- specialty-search
- corporate-records
- occrp
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Investigative Dashboard

> OCCRP's Investigative Dashboard (ID) — a one-stop index of company, land, and court registries across 180+ countries, so you always know which official source to check to trace ownership and assets.

## When to use
You have a company name, or a person you suspect is tied to businesses/assets, and need to trace ownership — especially across borders where you don't know which national registry to use. ID's Global Registry Search tells you which of 1,000+ official sources holds the records for a given country and record type, turning "where do I even look?" into a direct link to the right registry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://id.occrp.org/ and open the Global Registry Search (free, no login).
2. Filter by country and record type (company, land, court, etc.) to find the authoritative registry for that jurisdiction.
3. Follow the linked source and search it for your `employer-org` or person's `name`.
4. Read the filing: directors/officers, shareholders, registered address, and related entities.
5. If you're an OCCRP member/partner, request research-desk help for hard-to-reach jurisdictions; otherwise use the source links directly.
6. Pivot: officer/shareholder `name`s → people-search and `associate` mapping; registered `address` → address/property tools; related companies → repeat the trace.

## Inputs → Outputs
- **In:** `employer-org` (company) or a `name` you're tracing to businesses
- **Out:** the correct registry source(s), and from them officers, shareholders, `associate` links, and registered `address`es
- **Empty/negative result looks like:** no registry indexed for a jurisdiction/record type, or a registry that exists but is offline/paywalled — ID points you to the source but can't guarantee that source is free or digitized. That's a routing answer, not a dead end.

## Gotchas & OpSec
- ID is an index and research service, not a single searchable database of companies — the actual record lookup happens on the linked national registry, whose access/cost varies widely.
- Full research-desk assistance is gated to OCCRP members/partners; the public gets the registry index.
- Miscategorized here under transportation, but its real domain is corporate/asset tracing.
- OpSec: browsing ID is passive; national registries you follow into may log or even notify on access.

## Overlaps ("do both")
- Pairs with `[[occrp-aleph]]` (OCCRP's searchable database of leaks, filings, and public records) — use ID to find the right official registry and Aleph to search aggregated documents and datasets.

## Trust & verifiability
`trust: trusted` — OCCRP is a leading investigative consortium and ID curates official government registries; the ownership data is authoritative once you reach the primary source it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | investigative-dashboard |
| category | transportation |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
