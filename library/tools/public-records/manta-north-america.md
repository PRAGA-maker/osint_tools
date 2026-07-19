---
id: manta-north-america
name: Manta (North America)
description: Use when you have a US small-business `name` or `employer-org` and want its address, phone and category listing — returns address, phone, employer-org.
url: http://www.manta.com
category: public-records
path:
- public-records
bestFor: Looking up a US small/local business by name to get its listed address, phone and industry category.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: freemium
costNote: Free to search the directory and view company profiles; owners can claim a free listing. A Premium listing upgrade (~$99/mo) is seller-side only and irrelevant to lookups.
opsec: passive
opsecNote: Public business-directory search; queries hit Manta, not the subject. Passive — no notification reaches the business or owner. Nothing to sock-puppet, but a clean browser avoids ad/tracking noise.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Crowd/aggregator directory — profiles are built from public sources and owner submissions; "claimed" profiles are owner-verified, unclaimed ones may be stale or auto-generated.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- manta
aliases:
- manta.com
tags:
- toddington
- curated-directory
- company-search
- business-directory
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Manta (North America)

> A long-running US small-business directory — search a company name to pull its listed address, phone and industry category, with owner-"claimed" profiles carrying more reliable detail.

## When to use
You have a small or local US business `name` (or `employer-org`) tied to your subject — a shop they own, a company they list as an employer — and you want the business's registered address, contact phone, and industry classification. Manta indexes millions of US small businesses that don't appear in formal state registries, making it a useful complement for the mom-and-pop end of the market.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.manta.com/ and use the search bar (business name; optionally add a city/state).
2. Open the matching company profile. Read: business `address`, `phone`, category/industry, and whether the profile is "claimed" (owner-verified) or not.
3. Cross-check the address/phone against other sources — unclaimed listings can be years out of date.
4. Pivot: the phone/address feeds reverse-phone and address lookups; the industry + location feeds state corporate-registry searches to reach owner/officer names.

## Inputs → Outputs
- **In:** `name` / `employer-org`
- **Out:** `employer-org` profile, business `address`, `phone`, industry category
- **Empty/negative result looks like:** no profile or only unrelated same-name businesses — Manta skews toward businesses that opted in or were auto-listed, so absence doesn't mean the business doesn't exist.

## Gotchas & OpSec
- Unclaimed profiles are auto-generated and frequently stale (dead phones, moved addresses) — verify before relying.
- Common business names return many hits; disambiguate by city/state.
- Owner personal names are usually NOT shown; use a state registry (Secretary of State) for officers.
- OpSec: passive — no target notification.

## Overlaps ("do both")
- Pairs with `[[manta]]` (same provider, overlapping index) and with state corporate-registry lookups that supply the owner/officer names Manta omits.

## Trust & verifiability
`trust: unverified` — an aggregator directory, not an authoritative registry; treat unclaimed data as leads and confirm claimed-profile contact details independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manta-north-america |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, phone |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
