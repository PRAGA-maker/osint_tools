---
id: finland
name: Finland PRH/YTJ Business Register
description: Use when you have a `name` or `employer-org` linked to Finland and want registered companies, officers and addresses — returns `employer-org`, `associate`, `address`, `name`.
url: https://www.prh.fi/en/kaupparekisteri/beneficial_owner_details/information_services_and_details.html
category: public-records
path:
- public-records
bestFor: Tying a Finnish company or person to registered officers and addresses via the PRH trade register (with free basic search on YTJ/BIS).
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- associate
- address
- name
status: live
pricing: freemium
costNote: Free basic company search via the Business Information System (ytj.fi/BIS) — company name, ID, address, status. Detailed extracts and beneficial-owner data are paid and/or access-restricted (post-2022 EU ruling limits public BO access).
opsec: passive
opsecNote: Official Finnish registry data; searching hits PRH/YTJ, not the subject, and basic search needs no login. Ordering paid extracts requires an account/payment, attaching your identity to the request.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Finnish Patent and Registration Office (PRH); authoritative primary source. Beneficial-owner access is now curtailed.
missingPersonsRelevance: medium
coverage:
- fi
auth: none
api: true
localInstall: false
registration: false
aliases:
- PRH
- Patentti- ja rekisterihallitus
- YTJ
- Finnish Business Information System
tags:
- companysites
- Company Related Sites
- corporate-registry
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Finland PRH/YTJ Business Register

> Finland's official company register (PRH), with free basic search through the Business Information System (YTJ/BIS): the authoritative source for Finnish companies, their officers and addresses.

## When to use
You have a `name` or company `employer-org` with a Finnish connection and want the corporate footprint — companies a person is an officer of, co-officers (`associate`), and registered addresses. Use the free YTJ/BIS search for existence and basics; order paid PRH extracts for full officer detail, and note beneficial-owner data is now access-limited.

## How to use it (`bestInteractionPattern`: web-manual)
1. For free search, use the Business Information System at **https://tietopalvelu.ytj.fi/** (or ytj.fi) — search by company name or Business ID (Y-tunnus).
2. Read the free result: company name, Business ID, registered address, status, line of business.
3. For officers/signatories and certified extracts, order a paid PRH trade-register extract.
4. Beneficial-owner details (the stub's URL) are access-restricted for the public post-2022 EU ruling.
5. Pivot: run co-officers back through the register; cross-check addresses and against EU BRIS/OpenCorporates.

## Inputs → Outputs
- **In:** `name`, company `employer-org`, or Business ID (Y-tunnus)
- **Out:** `employer-org`, `associate` (officers, via paid extract), `address`, `name`
- **Empty/negative result looks like:** no matching company/ID — no Finnish company under that name; person-name search is limited, so try the company angle and Finnish name/spelling variants.

## Gotchas & OpSec
- Free YTJ/BIS search is thin (company basics); officer detail and certified data sit behind paid PRH extracts.
- Beneficial-ownership register access is now restricted for the general public.
- A registered address is the company's, not necessarily a home.
- PRH/YTJ offer open-data APIs for programmatic access.

## Overlaps ("do both")
- Pairs with OpenCorporates and the EU BRIS — use the Finnish primary source to confirm what aggregators report.

## Trust & verifiability
`trust: trusted` — the official Finnish register; free basic data is authoritative and paid extracts are the legal record. Confirm a common name maps to the right person before asserting a link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | finland |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, associate, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
