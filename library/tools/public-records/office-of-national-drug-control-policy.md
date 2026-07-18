---
id: office-of-national-drug-control-policy
name: US Office of National Drug Control Policy (ONDCP)
description: Use for US drug-policy context and program/directory references — a government information site, not a person search (no personal records).
url: http://www.whitehouse.gov/ondcp
category: public-records
path:
- public-records
bestFor: Official US drug-policy information — programs, prevention/treatment directories, drug facts and state/local links (reference, not a people database).
selectorsIn: []
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free US government site; no account needed.
opsec: passive
opsecNote: Browsing a public policy site reveals nothing about any subject and contains no personal records. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official White House/Executive Office agency site; authoritative for policy and program references, not individuals.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- white-house-disclosures
aliases:
- ONDCP
- whitehouse.gov/ondcp
tags:
- government
- drug-policy
- reference
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# US Office of National Drug Control Policy (ONDCP)

> The federal drug-policy agency's site — a policy and program reference with directories of prevention/treatment resources, and no personal records.

## When to use
A narrow, context-only resource. Use it to reach official US drug-policy information, national program details, drug-fact references, and links to state/local prevention and treatment directories — background that can frame a case touching substance use, or route you toward local service directories. It holds **no individual records** and cannot search for a person; treat any linked program/facility as a lead to pursue through proper channels.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.whitehouse.gov/ondcp and browse Information & Resources.
2. Follow to national programs, drug-fact pages, or the state/local directory links relevant to your area.
3. Note program/agency names (`employer-org`) and official contacts as reference leads.
4. Pivot: state/local directory links → county-level service and facility references; program contacts → lawful welfare/enforcement channels.

## Inputs → Outputs
- **In:** (none — a topic/area of interest; not a person lookup)
- **Out:** `employer-org` (programs/agencies), policy references and directory links — no personal selectors
- **Empty/negative result looks like:** only high-level policy content with no local directory for your area — go to state/county health and enforcement resources directly.

## Gotchas & OpSec
- **No personal data** — a policy/reference site, not a records search; its investigative use is limited to context and directory routing.
- Federal sites reorganize across administrations — links can move; use site search or the archive if a page 404s.
- OpSec: passive; nothing disclosed.

## Overlaps ("do both")
- Pairs with state/county behavioral-health directories (e.g. `[[ohio-mhas]]`) and lawful welfare channels — ONDCP gives national context and links; the local directories and proper channels are where any person-level follow-up happens.

## Trust & verifiability
`trust: trusted` — an authoritative federal agency; reliable for policy/program facts, but it offers no individual data to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | office-of-national-drug-control-policy |
| category | public-records |
| selectorsIn → selectorsOut | (none) → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
