---
id: tracxn
name: Tracxn
description: Use when you have a company or `name` and want private-market intelligence — returns startup profiles, funding, founders, and investor/associate links.
url: https://tracxn.com
category: public-records
path:
- public-records
bestFor: Profiling private companies and startups — funding history, founders, and investor relationships.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- associate
status: live
pricing: freemium
costNote: Freemium — signup gives limited free access, and public company profile pages are indexed (readable via Google); full data (funding rounds, contacts, exports) is behind paid plans.
opsec: passive
opsecNote: Passive research against Tracxn's database; you query companies, not individuals directly. Creating a free account ties queries to your login — use a sock-puppet email if that matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial private-market data aggregator with human-in-the-loop curation; broadly reliable for funded companies but coverage/accuracy thins for small or obscure entities.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- Tracxn
- tracxn.com
tags:
- company-research
- startup-intelligence
- private-markets
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Tracxn

> A private-market intelligence database (7M+ companies) — the tool for tying a person to the startup they founded or funded, and mapping the investors and co-founders around a company.

## When to use
You have an `employer-org` (a startup or private company) or a `name` you suspect is a founder/investor, and you want structured business intelligence: what the company does, its funding rounds and dates, who founded it, and which investors back it. This surfaces `associate` links (co-founders, board members, investors) and can corroborate a subject's claimed role or wealth. Strongest for venture-funded companies; weaker for tiny or unfunded entities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the company or person at https://tracxn.com; even without an account, individual company/founder profile pages are often indexed — reach them via Google (`site:tracxn.com "<name>"`).
2. Read the profile: sector, funding history, founders, key people, and investors.
3. Note co-founders and investors as `associate` pivots and the funding timeline as corroboration.
4. Recognise the paywall: headline facts are visible; deep data, contacts, and exports require a paid plan.
5. Pivot: founders/investors become new `name`s for people-search and LinkedIn; the company feeds official corporate registries for authoritative records.

## Inputs → Outputs
- **In:** `employer-org` / `name`
- **Out:** `employer-org` profile (funding, sector), founder/investor `name`s and `associate` links
- **Empty/negative result looks like:** no profile, or a stub with little data — the entity is too small/unfunded for Tracxn's coverage, or the detail sits behind the paywall. Absence here is not proof the company doesn't exist; check official registries.

## Gotchas & OpSec
- Partial paywall: much detail requires a paid subscription; the free/indexed layer gives headline facts only.
- Coverage skews to funded startups and tech; obscure or non-VC entities may be missing or thin.
- Aggregated data can lag reality — verify current status against a primary corporate registry.

## Overlaps ("do both")
- Pairs with Crunchbase/PitchBook-style databases and official corporate registries — Tracxn gives the private-market narrative and relationships; registries give the authoritative legal record and current filings.

## Trust & verifiability
`trust: community` — a commercial aggregator with human curation; reliable for well-funded companies but incomplete for the long tail, so corroborate roles and status against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tracxn |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
