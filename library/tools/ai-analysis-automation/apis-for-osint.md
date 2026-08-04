---
id: apis-for-osint
name: APIs for OSINT
description: Use when you have a `phone`, `email`, `domain` or `ip-address` and want an API to enrich it — returns a curated directory of OSINT APIs mapped to what each looks up.
url: https://github.com/cipher387/API-s-for-OSINT
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding the right API to automate a lookup (phone, email, domain, IP, breach, crypto, social) instead of hunting for one ad hoc.
selectorsIn:
- phone
- email
- domain
- ip-address
selectorsOut:
- address
- name
- social-profile
- domain
status: live
pricing: free
costNote: The directory itself is a free, open GitHub repo; the individual APIs it lists vary — many have free tiers, some are paid (monthly or pay-per-request). Check each API's own pricing before relying on it.
opsec: passive
opsecNote: Reading the list is passive. Actually calling any listed API is a live query that may register your key/IP with that provider and, for some services, could touch the target's infrastructure — assess each API's OpSec separately before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known community-maintained catalogue by cipher387 (100+ commits, active); it curates third-party APIs but does not vouch for each one, so verify any specific API's provenance and terms.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- advanced-search-operators-list
- awesome-grep
- code-understanding-tools-list
- dorks-collections-list
- grep-for-osint
- maltego-transforms-list
- python-osint-automation-examples
aliases:
- API-s-for-OSINT
- cipher387 APIs for OSINT
tags:
- My Projects
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# APIs for OSINT

> A curated GitHub catalogue of 70+ APIs across 30+ categories — the "which API do I call to enrich this selector?" reference for automating OSINT.

## When to use
You want to automate an enrichment — turn a `phone`, `email`, `domain`, `ip-address`, hash or wallet into structured data — and need to pick the right API rather than search blindly. This directory groups APIs by task (phone/address verification, DNS/IP/domain lookup, breach/leak search, IoT search engines like Shodan/Censys, crypto explorers, malware analysis, social APIs) with links and notes, so you can jump straight to a fitting service.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/cipher387/API-s-for-OSINT and read the categorised README.
2. Find the category matching your selector (e.g. "Phone numbers", "Domain/DNS/IP", "Data leaks").
3. Pick an API; open its linked docs and check its pricing, free tier, and terms.
4. Call the API (via curl/Python/your pipeline) with your selector as input.
5. Pivot: chain outputs into further APIs or into the automation examples in [[python-osint-automation-examples]].

## Inputs → Outputs
- **In:** `phone`, `email`, `domain`, `ip-address` (and more — the selector you want to enrich)
- **Out:** depends on the API chosen — commonly `address`, `name`, `social-profile`, `domain`, breach hits, infra data
- **Empty/negative result looks like:** no listed API for your exact need, or a listed API that has since gone paid/offline — the catalogue can lag individual services' changes.

## Gotchas & OpSec
- It's a **directory, not a service** — it returns no data itself; each linked API has its own auth, pricing, rate limits and reliability.
- Free-tier claims drift; confirm current pricing and terms on the provider's own page.
- Calling an API is active with respect to that provider (and sometimes the target) even though browsing the list is passive.

## Overlaps ("do both")
- Sits with the rest of cipher387's automation toolkit — pair with [[python-osint-automation-examples]] for calling patterns and [[dorks-collections-list]]/[[grep-for-osint]] for non-API discovery.

## Trust & verifiability
`trust: community` — an actively maintained, widely used catalogue, but it aggregates third-party APIs without endorsing each; vet any specific API's operator, terms and data quality before depending on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apis-for-osint |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | phone, email, domain, ip-address → address, name, social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
