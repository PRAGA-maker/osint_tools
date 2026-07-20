---
id: mybuilder-north-america
name: MyBuilder (United Kingdom)
description: Use when you have a UK tradesperson's `name` or business and want to verify their trade profile and reviews — returns `social-profile`, trade/company details, and customer-review context.
url: https://www.mybuilder.com
category: search-engines
path:
- search-engines
bestFor: Verifying a UK tradesperson or builder — their trade, service area, and customer reviews — from a name or business.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- address
status: live
pricing: free
costNote: Free to browse tradesperson profiles and reviews; posting a job or hiring is free to homeowners (tradespeople pay for leads).
opsec: passive
opsecNote: Browsing public tradesperson profiles and reviews is passive. Do NOT post a fake job to draw out a target's contact details — that is active deception with a footprint and possible ToS issues.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: MyBuilder is an established UK trades marketplace; profiles are self-created by tradespeople and reviews are customer-submitted, so treat details as claims to corroborate.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- mybuilder.com
- MyBuilder
tags:
- toddington
- curated-directory
- specialty-search
- trades-directory
source: toddington-resources
lastVerified: '2026-07-20'
---

# MyBuilder (United Kingdom)

> A UK trades marketplace — a way to verify a builder/tradesperson's profile, service area, and review history from a name or business. (Despite the library id, coverage is the **UK**, not North America.)

## When to use
You have a UK tradesperson's `name`, trade, or `employer-org` and want to confirm they're a real operating tradesperson: what work they do, roughly where they operate, how long they've been active, and what customers say. Useful for vetting a person who claims a building trade, corroborating a service-area location, or finding a business identity behind a name. Its direct missing-persons value is low; it's a corroboration/verification source for a specific occupational profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.mybuilder.com (may block automated fetchers; use a real browser).
2. Search the tradesperson's `name` or business, or browse by trade + town.
3. Open the profile: trade categories, service area (→ approximate `address`/region), years active, job count, and customer reviews.
4. Note reviewer locations and job descriptions — they can pin the tradesperson's operating area.
5. Pivot: business name feeds Companies House / registry checks; review locations corroborate a claimed area.

## Inputs → Outputs
- **In:** `name`, trade, or `employer-org`
- **Out:** `social-profile` (trade profile), service area / region (`address`), review history, business identity
- **Empty/negative result looks like:** no profile — the person may simply not use MyBuilder (many tradespeople don't); absence proves nothing about whether they trade.

## Gotchas & OpSec
- UK-only despite the "North America" label in the id — don't apply it elsewhere.
- Profiles are self-authored and reviews customer-submitted; verify claims against independent records.
- OpSec: browse passively; never post a decoy job to elicit contact details.

## Overlaps ("do both")
- Pairs with UK Companies House and general people-search — MyBuilder gives the trade profile and reviews; registries confirm the legal business entity.

## Trust & verifiability
`trust: community` — an established marketplace, but the profile and review content is user-generated; corroborate identity and location before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mybuilder-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → social-profile, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
