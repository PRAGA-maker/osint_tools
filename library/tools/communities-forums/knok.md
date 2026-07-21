---
id: knok
name: Knok (now HomeExchange)
description: Use when you have a name or location and want to check a home-exchange community for a member profile or listed property — returns social-profile, address-area, and image leads from home-swap listings.
url: http://www.knok.com
category: communities-forums
path:
- communities-forums
bestFor: Checking a home-exchange/home-swap community for a member's profile and listed property.
selectorsIn:
- name
- address
selectorsOut:
- social-profile
- address
- image
status: degraded
pricing: freemium
costNote: Registration is free; a paid annual membership (~€160) unlocks unlimited exchanges. Browsing member/property listings is largely gated behind an account.
opsec: active
opsecNote: Knok was acquired by and folded into HomeExchange — www.knok.com now redirects there. Meaningfully browsing listings requires an account, and viewing a member/property may be visible to the community (hosts can see interest). Use a sock-puppet membership; do not contact the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: The original Knok brand is defunct; the URL redirects to HomeExchange, a live home-swap platform. Member-authored profiles/listings are self-reported and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- knok.com
- HomeExchange
tags:
- toddington
- curated-directory
- online-communities-blogs
- travel
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Knok (now HomeExchange)

> A home-exchange/home-swap community — Knok was absorbed into HomeExchange, so the URL now resolves there. Niche value: a member profile or listed property can tie a subject to a home location and photos.

## When to use
Your subject may be part of the home-swap community — travellers who list their own home for exchange. If so, a HomeExchange member profile can reveal a `name`, a property location (`address`-area, usually town-level rather than exact), interior/exterior `image`s of their home, travel patterns, and a public profile (`social-profile`). Use it as a niche community check when mainstream social platforms come up empty and there is reason to think the person swaps homes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.knok.com — it redirects to HomeExchange.
2. Register a free account (sock-puppet email/identity) — listing search is gated behind login.
3. Search by location or browse listings for the target's town; scan member names and property photos.
4. If you find a plausible match, read the public profile (name, home area, photos, verification badges) — but do **not** send an exchange request or message, which would alert the member.
5. Pivot: property photos and town-level location feed reverse-image and geolocation workflows; the profile name feeds people-search.

## Inputs → Outputs
- **In:** `name` or `address`/location.
- **Out:** `social-profile` (member page), property `address`-area, home `image`s, travel history.
- **Empty/negative result looks like:** no matching member — the norm, since only a small slice of people use home-exchange platforms. Absence tells you nothing beyond "not a member here."

## Gotchas & OpSec
- Human-in-the-loop: **account-login** required to browse listings meaningfully.
- OpSec: treat as **active** — the platform is a social community; expressing interest or messaging is visible to the host. Stay in read-only reconnaissance and use a sock-puppet account.
- The "Knok" brand is defunct; do not expect Knok-specific features — you are on HomeExchange. Locations shown are usually approximate for member safety.

## Overlaps ("do both")
- Pairs with reverse-image and geolocation tools — a listing's home photos are strong material for confirming a location that the profile only shows at town level.

## Trust & verifiability
`trust: unverified` — the original site is defunct and now redirects to HomeExchange; profiles and listings are self-authored by members. Corroborate any home location or identity against an independent source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | knok |
| category | communities-forums |
| selectorsIn → selectorsOut | name, address → social-profile, address, image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
