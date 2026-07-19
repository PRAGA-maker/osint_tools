---
id: list-org
name: List-Org
description: Use when you have a Russian company `name`, tax ID, or a director's `name` and want the linked officers, address and business connections — returns employer-org, address, associate.
url: https://www.list-org.com/
category: public-records
path:
- public-records
bestFor: Free lookup of Russian legal entities and sole proprietors — directors, founders, address, procurement and litigation links.
selectorsIn:
- name
- employer-org
- document-id
- phone
- address
selectorsOut:
- employer-org
- address
- associate
- phone
status: live
pricing: free
costNote: Explicitly free with no registration — "все данные отдаем без регистрации и абсолютно бесплатно" (all data given without registration, absolutely free).
opsec: passive
opsecNote: Aggregator of already-public Russian registry data; queries hit List-Org, not the subject, so it is passive. Use a sock-puppet browser/VPN out of general caution when researching Russian entities, but no notification reaches the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party aggregator (not an official registry) compiling data from 20+ official Russian sources including the FTS tax service, Rosstat, courts and the patent office; cross-check critical facts against the primary source.
missingPersonsRelevance: medium
coverage:
- ru
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- list-org.com
- ЛистОрг
tags:
- company-search
- russia
- business-registry
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# List-Org

> A free, no-registration aggregator of Russian company and sole-proprietor records — search by name, INN, OGRN, phone or address to reach directors, founders and business links.

## When to use
You have a Russian company `name`, tax ID (`document-id`: INN/OGRN), a director/founder `name`, a `phone` or an `address`, and want to map the people and entities around it — who runs it, who founded it, the registered address, and connected companies. Useful for pivoting from a business a missing person or associate is tied to in Russia (15M companies, 24M entrepreneurs indexed).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.list-org.com/ (interface is Russian — use browser translation if needed).
2. Enter the selector in the search box: company `name`, INN, OGRN, director surname, `phone`, or `address`.
3. Open the entity card. Read: director/manager, founders, registration date, registered `address`, related/successor entities, and any procurement, litigation or bankruptcy records.
4. Pivot: a director surname → repeat the search on that `name` to find their other companies (`associate` network); an `address` → find co-located entities.

## Inputs → Outputs
- **In:** `name` / `employer-org`, INN or OGRN (`document-id`), `phone`, `address`
- **Out:** `employer-org` details, registered `address`, officers/founders (`associate`), sometimes `phone`
- **Empty/negative result looks like:** "не найдено" / no entity card — the identifier isn't in the Russian registry mirror, or the entity is dissolved and dropped; try the OGRN/INN directly rather than the name.

## Gotchas & OpSec
- Data is a mirror of official registries — it can lag behind current filings; verify a critical fact against the primary FTS/EGRUL source.
- Russian-language UI; company forms (ООО, ИП, АО) matter for disambiguation.
- OpSec: passive — the subject is not notified. Still, route Russian-entity research through a sock-puppet/VPN as general hygiene.

## Overlaps ("do both")
- Complements Western corporate-registry tools when a subject's business footprint spans jurisdictions — List-Org covers the Russian side that OpenCorporates-style sources thin out on.

## Trust & verifiability
`trust: community` — a third-party aggregator, not a government registry; it consolidates 20+ official sources but is not itself authoritative, so treat officer/link data as leads to confirm against EGRUL.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | list-org |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, document-id, phone, address → employer-org, address, associate, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
