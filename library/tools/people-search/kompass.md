---
id: kompass
name: Kompass
description: Use when you have a company `employer-org` or a business `name` and want firmographics and business contacts — returns company address, phones, and named executives/associates.
url: https://www.kompass.com
category: people-search
path:
- people-search
bestFor: Linking a person to a company (or vice versa) via a global B2B business directory.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- phone
- associate
status: live
pricing: freemium
costNote: Basic company listings (name, address, sector, some contacts) are free to browse; full contact lists and detailed firmographics sit behind a paid B2B subscription.
opsec: passive
opsecNote: Browsing business listings is passive and does not notify anyone. It is business data, not private personal data, but named executives on a listing are still individuals — handle the personal pivots (names, direct contacts) with the usual care. Use a sock-puppet account if you register for extended access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established international B2B directory; company data is generally reliable but can be outdated for small firms and self-submitted listings.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Kompass
- kompass.com
tags:
- people-investigations
- business-directory
- b2b
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Kompass

> A global B2B business directory — the bridge between a person and the company they run, work for, or founded.

## When to use
You have an `employer-org` (a company name) and want its address, phones, sector, and the executives listed against it; or you have a person's `name` and a hint they own/run a business and want to find that company. Kompass is strong for corporate-affiliation mapping across many countries — useful when a missing or subject person is tied to a business rather than easily found as an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.kompass.com` and choose your country/region.
2. Search by company name (`employer-org`), sector, or executive `name`.
3. Open a company listing: registered address, phone, activity/sector codes, size, and listed executives/contacts (`associate`).
4. For fuller contact detail you may hit a paid gate — the free listing is often enough to confirm the affiliation.
5. Pivot: a named executive → people-search; the company address/phone → records and reverse-phone; the sector/registration → national company registries.

## Inputs → Outputs
- **In:** `employer-org`, `name`
- **Out:** `employer-org` (confirmed company), `address`, `phone`, `associate` (executives/contacts)
- **Empty/negative result looks like:** no company match, or a bare listing with no contacts — small or informal businesses are thinly covered. Absence here doesn't mean the company doesn't exist; check the national registry.

## Gotchas & OpSec
- Coverage and freshness vary by country and firm size; small firms are often stale or self-submitted.
- The richest contact data is paywalled; plan around the free tier.
- OpSec: **passive** — business data, no subject notification; still treat named individuals carefully.

## Overlaps ("do both")
- Pairs with national company registries and people-search — Kompass surfaces the affiliation and contacts; registries give the authoritative filing, people-search expands the named executive.

## Trust & verifiability
`trust: community` — an established directory with broad reach, but listings can be outdated or self-submitted; corroborate a company-person link against an official registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kompass |
| category | people-search |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, phone, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
