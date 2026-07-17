---
id: dfw1n-osint
name: DFW1N-OSINT
description: Use when you have an Australian `name`, `address`, or `domain` and need the right AU registry/people resource — a curated, missing-persons-oriented directory of Australia-focused OSINT tools.
url: https://github.com/DFW1N/DFW1N-OSINT
category: public-records
path:
- public-records
bestFor: A jump-off directory of Australia-specific OSINT resources — registries, people finders, vehicle/rego lookups, government and police links — assembled for missing-persons work.
selectorsIn:
- name
- address
- domain
selectorsOut:
- address
- associate
status: live
pricing: free
costNote: Free, open GitHub repository. The linked resources have their own (mostly free) access terms; some AU government registries may charge per search.
opsec: passive
opsecNote: Reading the list is passive. OpSec depends entirely on which linked tool you then use — evaluate each destination's leakage before querying, and use a sock puppet where the target could be alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated repository (~420★) explicitly built for AU missing-persons/ethical-OSINT work, reportedly with law-enforcement input; last major update ~2019, so verify individual links still resolve.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- DFW1N OSINT
tags:
- australia
- public-records
- directory
- regional
source: gh-topic-osint-framework
lastVerified: '2026-07-17'
enrichment: full
---

# DFW1N-OSINT

> A curated GitHub directory of Australia-focused OSINT resources — the fast way to find the right AU registry, people finder, or rego lookup when a case has an Australian nexus.

## When to use
Your case touches Australia and you need country-specific starting points that generic global tools miss: state vehicle-registration lookups, AU people-search databases, government and police services, and breach/geolocation resources. Instead of guessing which Australian registry to use, browse this list — it was assembled specifically for missing-persons and ethical-OSINT investigations in the AU context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/DFW1N/DFW1N-OSINT and skim the README's category sections (person search, AU government/registries, social media, geolocation, breach data).
2. Pick the resource matching your selector — e.g. an AU people finder for a `name`, a rego service for a vehicle, a registry for a `domain`/business.
3. Follow the link and run your query in that destination tool (mind its own auth/cost/OpSec).
4. Because the repo is a few years old, confirm each link still resolves; substitute a current equivalent if a service has moved or closed.
5. Pivot: an AU registry hit → `address`/`associate` → feed into people-search and cross-reference with other records.

## Inputs → Outputs
- **In:** `name`, `address`, `domain` (used in the destination AU tools)
- **Out:** routes to `address`, `associate`, and registry data via the linked services
- **Empty/negative result looks like:** the repo lists a resource but the link is dead, or the destination tool returns nothing — treat as "this pointer is stale," check archive.org, and try a current AU registry.

## Gotchas & OpSec
- It is a **directory, not a search tool** — it holds no data itself; all results come from the destinations you follow.
- Last significant update was ~2019: expect some dead links; verify before relying.
- Your OpSec is whatever the destination tool leaks — evaluate each one individually.

## Overlaps ("do both")
- Pairs with global people-search and records tools — DFW1N narrows you to the correct AU-specific source, which you then combine with international lookups for a full picture.

## Trust & verifiability
`trust: community` — a well-regarded, purpose-built AU OSINT directory. The curation is trustworthy; individual links may have rotted with age, so confirm each destination is live and authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dfw1n-osint |
| category | public-records |
| selectorsIn → selectorsOut | name, address, domain → address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
