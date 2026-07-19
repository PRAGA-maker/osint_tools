---
id: north-american-sic-structure-united-states
name: North American SIC Structure (United States)
description: Use when you have a SIC `document-id` code (or an industry name) and want to decode the industrial sector — returns the classified industry/employer-org context.
url: https://www.osha.gov/pls/imis/sic_manual.html
category: dark-web
path:
- dark-web
bestFor: Decoding a US Standard Industrial Classification (SIC) code into the industry it represents, or finding the code for an industry.
selectorsIn:
- document-id
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free, public-domain US Department of Labor / OSHA reference; no account or payment.
opsec: passive
opsecNote: Static US government reference page; reading it has no target footprint and no subject notification.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official OSHA (US Dept. of Labor) SIC manual — authoritative for the SIC coding scheme, though SIC itself is a legacy system largely superseded by NAICS.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OSHA SIC manual
- SIC code lookup
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# North American SIC Structure (United States)

> OSHA's official Standard Industrial Classification manual — a reference for turning a SIC code found in a business filing into the industry it denotes (and back).

## When to use
You have a US SIC code (a legacy industry classifier that shows up in old business registrations, corporate filings, OSHA inspection records, and some regulatory databases) and need to know what industry it means — or you have an industry and want its SIC code to search coded datasets. This decodes an employer/business classification when you're profiling a subject's workplace or a company tied to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osha.gov/pls/imis/sic_manual.html.
2. Browse the Division → Major Group hierarchy, or use the site's "SIC Search" link to look up a specific code or keyword.
3. Read the mapped industry description; the two-digit Major Group gives the broad sector, the four-digit code the specific industry.
4. Pivot: use the decoded industry to interpret a subject's `employer-org` filing, or convert to the modern NAICS code for datasets that use NAICS instead.

## Inputs → Outputs
- **In:** `document-id` (SIC code) or industry keyword
- **Out:** industry/sector description behind the code (`employer-org` context)
- **Empty/negative result looks like:** code not found — likely a NAICS code (SIC's replacement) or a typo; SIC has a fixed 4-digit range, so out-of-range numbers aren't SIC.

## Gotchas & OpSec
- SIC is a legacy scheme; most current US datasets use NAICS. Confirm which system your source record uses before decoding.
- The manual is a classifier reference, not a company directory — it won't name businesses, only categorize them.
- OpSec: passive government-reference read.

## Overlaps ("do both")
- Complements business-registry and corporate-record tools: use those to find the SIC/NAICS code attached to a company, then this to interpret it.

## Trust & verifiability
`trust: trusted` — authoritative first-party OSHA/DOL reference for the SIC scheme itself; the coding is definitive even though SIC is a legacy standard.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | north-american-sic-structure-united-states |
| category | dark-web |
| selectorsIn → selectorsOut | document-id → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
