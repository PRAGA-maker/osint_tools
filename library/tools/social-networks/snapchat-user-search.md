---
id: snapchat-user-search
name: SoVIP — Snapchat User Search
description: Use when you have a `username`/`name` or a city and want to find Snapchat users — returns member profiles with age, location, and photos (self-listed on SoVIP).
url: https://sovip.io/
category: social-networks
path:
- social-networks
bestFor: Discovering Snapchat users by name/handle or by city/age filters via a third-party directory of self-listed Snapchatters.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to browse and search; a free account (email or social sign-in) unlocks full access.
opsec: passive
opsecNote: SoVIP indexes profiles that users voluntarily submitted TO SoVIP — it is not Snapchat's official data, and searching it does not touch the person's Snapchat account or notify them (passive). Register with a sock-puppet, not a real identity, since sign-up wants an email/social login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party, user-submitted Snapchat directory — anyone can list (or impersonate) a handle, and the site itself warns about fraudulent listings, so treat every entry as unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- SoVIP
- sovip.io
- Snapchat user search
tags:
- snapchat
- people-search
- social-networking
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# SoVIP — Snapchat User Search

> A third-party directory of self-listed Snapchat users — searchable by handle/name or by city/age — filling the gap left by Snapchat's own lack of a public user search.

## When to use
You have a `username`, `name`, or just a city/age profile and want to find a Snapchat account, which Snapchat itself makes hard to search. SoVIP lets you look up handles or browse by location/age, returning member cards with photos, stated age, and `geolocation` — useful leads when your only foothold is a Snapchat handle or a demographic sketch.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sovip.io/ and register a free sock-puppet account (email or social sign-in unlocks full access).
2. Search by username/name, or filter by city, sex, and age.
3. Read the profile card: photos, age, location, and the Snapchat handle it claims.
4. Pivot: the claimed Snapchat `username` feeds cross-platform enumeration; photos → reverse-image/face search; stated city → `geolocation`. Verify the handle actually exists on Snapchat before trusting it.

## Inputs → Outputs
- **In:** `username`, `name`, or city/age filters
- **Out:** `social-profile` cards (photos, age, claimed handle), stated `geolocation`
- **Empty/negative result looks like:** no match — the person never self-listed on SoVIP (most Snapchat users haven't), so absence means nothing about their actual Snapchat presence.

## Gotchas & OpSec
- NOT official Snapchat data — profiles are self-submitted to SoVIP and can be fake or impersonated (the site itself flags fraud). Verify on Snapchat directly.
- Coverage is limited to people who opted into SoVIP, heavily skewed toward those seeking followers.
- Human-in-the-loop: a free login is required; passive toward the subject regardless.

## Overlaps ("do both")
- Complements username-enumeration and reverse-image/face tools — SoVIP surfaces a candidate handle/photo; those confirm the person and link other accounts.

## Trust & verifiability
`trust: unverified` — a self-submitted third-party directory; every listing is a lead to confirm against Snapchat itself, never proof of identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapchat-user-search |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
