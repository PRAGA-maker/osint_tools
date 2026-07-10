---
id: i-cyprus-com
name: i-cyprus.com
description: Use when you have a company or director `name` in Cyprus and want corporate-registry detail — returns directors, shareholders, secretaries, `address`es and full company history.
url: https://i-cyprus.com/
category: public-records
path:
- public-records
bestFor: Pulling Cyprus company records — directors, shareholders, addresses and history — to link a person to a company.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- associate
- address
- name
status: live
pricing: freemium
costNote: Company name search is free; full reports (directors, shareholders, document scans, history) are paid and delivered within ~12 hours. Operated by Dataset SIA (Latvia), not the Cyprus government.
opsec: passive
opsecNote: Read-only registry search; the subject/company is not notified. Ordering a paid report requires payment details — use appropriate billing hygiene. It is a third-party reseller of Cyprus registry data, so queries are logged by a commercial operator.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator (Dataset SIA) reselling Cyprus corporate-registry data — the underlying registry is official, but this is not the government source and full data is paywalled.
missingPersonsRelevance: high
coverage:
- cy
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- infogreffe-fr
aliases:
- iCyprus
- i-Cyprus company search
tags:
- companysites
- Company Related Sites
- corporate-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# i-cyprus.com

> A searchable front end to the Cyprus corporate registry — link a person to companies via directorships, shareholdings, and registered addresses.

## When to use
You have a `name` (of a person or a company) tied to Cyprus and want the corporate picture: what companies a person directs/owns, who else is on the board (`associate`), the registered `address`es, and the full history of former officers and names. Cyprus is a common corporate-domicile jurisdiction, so this is valuable for mapping a subject's business footprint, co-directors, and address links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://i-cyprus.com/ and use "Find a company" / company search.
2. Search by company `name` (or a director's `name` where supported) to locate the entity.
3. Free tier: confirm the company exists and see basic identifiers. For directors, shareholders, secretaries, addresses, document scans, and full history, order the paid report (delivered ~12h).
4. Read the report: officers (`associate`), shareholding, registered `address`, and historical changes.
5. Pivot: a co-director's `name` feeds people-search; an address feeds property/mapping; compare with other national registries.

## Inputs → Outputs
- **In:** company or director `name` / `employer-org` (optionally `address`)
- **Out:** `employer-org` (companies), `associate` (directors/shareholders/secretaries), `address`, `name`, full company history
- **Empty/negative result looks like:** no company match — the entity isn't in the Cyprus registry, or the name/spelling is off. A free-tier match with no detail just means the detail is paywalled, not absent.

## Gotchas & OpSec
- Human-in-the-loop: full data is **paywalled** (`payment-wall-partial`) — the free search only confirms existence/basics.
- Third-party reseller (Dataset SIA, Latvia), not the official Cyprus registry — cross-check against the official Department of Registrar of Companies where possible.
- Cyprus-only.
- OpSec: **passive** — a registry read; mind billing hygiene when ordering reports.

## Overlaps ("do both")
- Pairs with `[[infogreffe-fr]]` and other national corporate registries — a person's companies often span jurisdictions, so run the registry matching each domicile and cross-link co-directors.

## Trust & verifiability
`trust: community` — reliable resale of official Cyprus registry data, but not the primary government source and largely paywalled; verify critical facts against the official registrar.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i-cyprus-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, associate, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
