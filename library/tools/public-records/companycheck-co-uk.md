---
id: companycheck-co-uk
name: companycheck.co.uk
description: Use when you have a UK company `name` or a person's `name` and want directorships, filings and registered addresses — returns `employer-org`, `address`, `associate` (co-directors).
url: https://www.companycheck.co.uk/
category: public-records
path:
- public-records
bestFor: UK company and director intelligence built on Companies House data, with cross-linked director networks.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Basic company profiles and director listings are viewable free (a free account unlocks more); full financials, credit reports and director-network detail sit behind paid plans.
opsec: passive
opsecNote: Passive — data comes from Companies House filings via Company Check's index; the company/directors are not notified. Viewing full detail may require a free login, which creates an account trail on your side; use a sock-puppet account for sensitive work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A well-established UK company-data reseller sourcing from Companies House; the underlying registry data is authoritative, but the value-add (credit scores, network maps) is Company Check's own analysis.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: true
aliases:
- Company Check
- companycheck.co.uk
tags:
- companysites
- Company Related Sites
- uk-companies-house
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# companycheck.co.uk

> UK company and director intelligence over Companies House data — with the key OSINT feature of mapping a person to every company they direct.

## When to use
You have a UK company `name`, or (more powerfully for people-tracing) a person's `name`, and want their directorship footprint: which companies they run/ran, co-directors (`associate` leads), registered office `address`, and filing history. Excellent for building out a UK subject's business network and surfacing addresses of record when standard people-search comes up short.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.companycheck.co.uk/ and search by company `name` or by a director's personal `name`.
2. For a company: read the profile — status, registered `address`, incorporation date, and the director list.
3. For a person: open their director page to see the full list of companies they're linked to, and the co-directors on each (`associate` pivots).
4. Log in (free account) or upgrade for deeper financials/network detail; use a puppet account if attribution matters.
5. Pivot: cross-check the same people on Companies House directly, and run non-UK entities through `[[info-clipper-com]]`.

## Inputs → Outputs
- **In:** UK company `name` or director `name`
- **Out:** `employer-org` (companies), registered `address`, `associate` (co-directors), filing/status detail
- **Empty/negative result looks like:** no match, or a dissolved-company shell with no active detail — the person holds no UK directorships, or you need to log in/upgrade to see more. UK-only: no coverage of overseas entities.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — full detail needs a (free) account; deeper data is paywalled.
- OpSec: **passive** to the target; your login/subscription is a trail on your side. Use a sock-puppet account.
- Value-add scores are Company Check's own; treat the raw Companies House facts (directors, addresses, filings) as the reliable part.

## Overlaps ("do both")
- Pairs with `[[info-clipper-com]]` (non-UK companies) and `[[familytree]]`-style people search — this nails the UK directorship network; the others extend geography and personal detail.

## Trust & verifiability
`trust: community` — reputable reseller of authoritative Companies House data. Cross-check critical director/address facts against Companies House itself; treat credit/network analytics as secondary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | companycheck-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
