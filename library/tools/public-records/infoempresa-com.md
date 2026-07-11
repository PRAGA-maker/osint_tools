---
id: infoempresa-com
name: infoempresa.com
description: Use when you have a `name` or company and want to find a subject's Spanish company directorships, shareholdings, or registered addresses — returns corporate roles drawn from official Spanish registries.
url: https://www.infoempresa.com/en-in/es/
category: public-records
path:
- public-records
bestFor: Linking a person to Spanish companies (as director/shareholder) and pulling registered company addresses from official sources.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Basic company existence and headline details are viewable free; full reports (directors, shareholders, accounts, credit) sit behind paid reports/subscription.
opsec: passive
opsecNote: Queries official-registry-derived data and does not alert the subject. Deeper reports may require registration, which ties the lookup to your account — use a sock-puppet identity if you buy a report.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates data from the Spanish Commercial Registry and BORME (official gazette); the underlying sources are authoritative though the presentation is a commercial reseller.
missingPersonsRelevance: high
coverage:
- es
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Infoempresa
tags:
- companysites
- Company Related Sites
- spain
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# infoempresa.com

> A commercial front-end to Spain's Commercial Registry and BORME — use it to tie a person to Spanish companies, directorships, and shareholdings, and to pull registered company addresses.

## When to use
You have a `name` or a company and want to know a subject's business footprint in Spain: which companies they direct, own, or represent, and the addresses and co-directors attached to those companies. Corporate filings are a strong locate/identity lead — a director address, a fellow shareholder (`associate`), or an incorporation date can reopen a cold trail. Reach for this when a subject has (or claims) Spanish business ties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.infoempresa.com/ (the site auto-routes by region).
2. Search by **company name**, **CIF** (tax ID), or **director name**.
3. On the free tier, read the headline: company existence, legal status, sector, and location. For directors/shareholders/accounts/credit, open the full report (paid).
4. Read the output: corporate roles, shareholding structure, legal representatives, registered address, BORME events (appointments, capital changes, insolvency).
5. Pivot: a registered `address` and co-directors (`associate`) feed people/address tools; BORME events date-stamp a person's activity.

## Inputs → Outputs
- **In:** `name` (director) or `employer-org` / CIF
- **Out:** `employer-org` (companies + roles), `address` (registered), `associate` (co-directors/shareholders)
- **Empty/negative result looks like:** no company or no directorship match — means no Spanish registered role under that name/ID, not that the person has no business abroad. Try name variants and cross-check the free official BORME.

## Gotchas & OpSec
- Human-in-the-loop: full detail is **paywalled** — the free tier confirms existence and location but not the people links; budget for a report if you need directors/shareholders.
- Coverage is **Spain only**; the same underlying data is free (if clunkier) via the official Registro Mercantil / BORME — verify critical facts there.
- OpSec: passive; buying a report may require registration, so use a sock-puppet account.

## Overlaps ("do both")
- Pairs with OpenCorporates and the official BORME — cross-check the free authoritative sources against this reseller's aggregated, more searchable view.

## Trust & verifiability
`trust: trusted` — the data originates from Spain's official Commercial Registry and BORME; treat the reseller's convenience layer as accurate but confirm high-stakes facts against the primary registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infoempresa-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
