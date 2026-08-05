---
id: manta
name: Manta
description: Use when you have a business name, person, or location and want US small-business directory data — company profile, address, phone, and sometimes owner/officer — returns employer-org, address, and phone.
url: https://www.manta.com/business
category: public-records
path:
- public-records
bestFor: Looking up US small businesses for address, phone, and basic company/owner details.
selectorsIn:
- employer-org
- name
- geolocation
selectorsOut:
- address
- phone
- employer-org
status: live
pricing: freemium
costNote: Free to search and view basic business listings; Manta also sells marketing services to businesses, but lookups don't require payment.
opsec: passive
opsecNote: A public business directory — searching discloses nothing about a target beyond your query to Manta. Use a clean/sock-puppet browser; nothing here notifies the business.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running US small-business directory; listings are partly self-submitted/aggregated, so details can be outdated or promotional — corroborate against official registries.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- manta-north-america
aliases:
- manta.com
tags:
- corporate
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# Manta

> A large US small-business directory — quick lookups of company profiles, addresses, phones, and sometimes the owner behind a small business.

## When to use
You have a small-business `employer-org` name, an owner's `name`, or a `geolocation`, and want contact/company details: address, phone, category, and occasionally the proprietor. Manta is strongest on small and local US businesses that may not appear in formal registries, making it useful for tying a person to a business or finding a business's real-world address/phone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.manta.com/business.
2. Search by business name, category + location, or owner name.
3. Open a listing to read the profile — address, phone, category, description, and any named contact.
4. Corroborate the address/phone against an official source before relying on it.
5. Pivot: the `address`/`phone` feeds reverse-phone/address OSINT; an owner `name` feeds people-search; the business feeds corporate-registry lookups.

## Inputs → Outputs
- **In:** `employer-org` name, owner `name`, or `geolocation`
- **Out:** `address`, `phone`, `employer-org` profile (sometimes owner/contact)
- **Empty/negative result looks like:** no listing or a bare stub — the business may be too new, closed, non-US, or simply never listed itself here.

## Gotchas & OpSec
- Listings are partly **self-submitted/aggregated** and can be stale or promotional — verify against Secretary-of-State/registry data.
- US-focused; weak coverage elsewhere.
- Passive public search; nothing notifies the business.

## Overlaps ("do both")
- Pairs with official corporate registries and reverse-phone/address tools — Manta surfaces the small-business contact details, registries confirm the legal entity and officers.

## Trust & verifiability
`trust: community` — a useful aggregate directory, but its data is not authoritative; treat addresses/phones/owners as leads to confirm with primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manta |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name, geolocation → address, phone, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
