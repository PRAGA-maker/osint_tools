---
id: thekyb-com
name: thekyb.com
description: Use when you have a company `name` or `employer-org` and want verified registry data — legal name, address, officers, and beneficial owners across 250+ jurisdictions; returns employer-org, address, and associate links.
url: https://thekyb.com/blog/how-to-verify-a-company-in-spain-an-ultimate-guide/
category: public-records
path:
- public-records
bestFor: Global Know-Your-Business verification — pulling official registry records, officers, and UBOs for a company across 250+ countries/states.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Commercial KYB platform. A free trial / limited "Try Now" lookups exist, but sustained or bulk use requires a paid subscription or API key. Treat as paid-gated beyond the trial.
opsec: passive
opsecNote: You query corporate registry data, not the subject. No target-side signal. Account/API sign-up ties your queries to your subscription — use appropriate attribution hygiene if that matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial KYB aggregator sourcing from official registries worldwide; data is registry-derived (authoritative) but coverage/freshness varies by jurisdiction and the aggregation layer is vendor-run.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- opencorporates-com
- gleif-org
- belgium
aliases:
- The KYB
- thekyb
tags:
- companysites
- Company Related Sites
- kyb
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# thekyb.com

> A global Know-Your-Business platform: one interface over official company registries in 250+ jurisdictions, returning legal entity data, officers, and beneficial owners.

## When to use
You have a company `name`, `employer-org`, or address and need verified corporate data — legal name, registration number, registered `address`, directors/officers, and ultimate beneficial owners — especially across borders where checking each national registry is slow. Useful for tying a subject to companies they run or own, and for piercing to the natural persons (`associate`) behind an entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to thekyb.com and use the "Try Now" lookup, or sign up for a trial / API key for repeated use.
2. Enter the company `name` (and jurisdiction if known) or a registration number.
3. Review the returned profile: legal name, status, incorporation date, registered address, officers/directors, and UBOs where the jurisdiction exposes them.
4. Retrieve source registry documents where offered.
5. Pivot: officer/UBO names become `associate` leads for people-search; the registration number and address feed the national registry or [[opencorporates-com]] for cross-checking.

## Inputs → Outputs
- **In:** `name` / `employer-org` (company) or `address`
- **Out:** `employer-org` (verified legal entity), `address` (registered), `associate` (officers, UBOs)
- **Empty/negative result looks like:** no entity match, or a match with officers-only and no UBO data — many jurisdictions don't publish beneficial ownership, so a UBO blank reflects the registry, not the platform.

## Gotchas & OpSec
- Coverage and data depth vary widely by country; a "verified" profile in one jurisdiction may be thin in another.
- Beyond the free trial it is paid — budget for it, or fall back to free registries first.
- Human-in-the-loop: sign-up and payment/API key for anything beyond a demo lookup.
- OpSec: passive toward the subject; your queries are tied to your account.

## Overlaps ("do both")
- Pairs with [[opencorporates-com]] (free, broad officer data) and [[gleif-org]] (authoritative LEI/relationships); use the free tools to scope, then thekyb for consolidated cross-border UBO/registry pulls. For Belgian UBOs specifically, see [[belgium]].

## Trust & verifiability
`trust: community` — the underlying records come from official registries (authoritative where present), but this is a commercial aggregation layer with variable freshness; verify decision-critical facts against the primary national registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thekyb-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, api-key) |
