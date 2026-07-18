---
id: oscar-job-function-codes-united-kingdom
name: Oscar Research Job Function Codes (UK)
description: Use when you have a UK public-sector role code or job title and want to decode it — returns the standardized function/category that maps a postholder's title to their organizational role.
url: http://www.oscar-research.co.uk/databases/categorycodes
category: transportation
path:
- transportation
bestFor: Decoding Oscar's UK public-sector function/category codes to interpret a postholder's role.
selectorsIn: []
selectorsOut:
- employer-org
status: live
pricing: free
costNote: The category-code reference/data dictionary is free to view/download; Oscar's underlying contact databases are a paid commercial product.
opsec: passive
opsecNote: Reading a public reference/data dictionary is passive and anonymous; you are decoding a classification scheme, not querying any individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by Oscar Research, a UK public-sector data/marketing vendor; the code list is their proprietary classification, authoritative for their own datasets only.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Oscar Research category codes
- Oscar function codes
tags:
- toddington
- curated-directory
- specialty-search
- reference
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Oscar Research Job Function Codes (UK)

> Oscar Research's data dictionary of UK public-sector role/function codes — a reference for translating a coded job classification into the actual organizational function a postholder performs.

## When to use
You've encountered Oscar Research data (or a dataset that uses its scheme) describing a UK public-sector contact by a category/function code, and you need to know what that code means — e.g. which tier of manager, which service area (children's services, housing, IT, finance), or which elected role. This reference maps hundreds of standardized function categories to plain descriptions, letting you interpret a coded role and understand where a named postholder sits in an organisation. It's a decoding aid, not a person-search tool, and its value is narrow: it only makes sense of Oscar's own classification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.oscar-research.co.uk/databases/categorycodes and open (or download) the category-codes guide.
2. Look up the code or the function description you're trying to interpret.
3. Read the mapped category — seniority level plus service/functional area — to understand the role.
4. Pivot: knowing a postholder's precise function within a council/public body (`employer-org`) sharpens directory and registry searches for that named individual.

## Inputs → Outputs
- **In:** an Oscar function/category code or a job title/function
- **Out:** the standardized role/function description that situates the postholder within a public-sector `employer-org`
- **Empty/negative result looks like:** a code/title not in the guide — it may be from a different scheme (SOC/SIC) entirely; use the appropriate classification instead of forcing a match.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a reference document.
- This is a *classification key*, not a database of people — it explains role codes; it will not name individuals. Oscar's actual contact database is a separate paid commercial product.
- The scheme is proprietary to Oscar and UK-public-sector specific; don't apply it to private-sector or non-UK roles.

## Overlaps ("do both")
- Pairs with official UK role classifications (SOC codes) and council directories — Oscar's codes decode Oscar-sourced data, while public council/registry directories name the actual postholders in a given function.

## Trust & verifiability
`trust: community` — an authoritative key for Oscar's own data but a proprietary vendor scheme; when interpreting non-Oscar data, verify against the classification that dataset actually uses.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oscar-job-function-codes-united-kingdom |
| category | transportation |
| selectorsIn → selectorsOut |  → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
