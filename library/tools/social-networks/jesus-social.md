---
id: jesus-social
name: Jesus Social
description: Use when you have a `name` or `username` and want to check for a profile on this niche Christian social network — returns a `social-profile`.
url: https://www.jesus.social
category: social-networks
path:
- social-networks
bestFor: Locating a subject's profile on a niche Christian faith-community social network by name or username.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: 100% free to join and browse; a free member account is needed to view the full member directory.
opsec: passive
opsecNote: Browsing public profiles is passive. The member directory generally requires a (free) login, which is active — create the account with a sock-puppet identity, never your own, since the platform can see who viewed a member.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small independent Christian social-networking site; self-reported profile data with no identity verification, so treat any match as a lead, not confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- jesus.social
- Jesus Social Network
tags:
- toddington
- curated-directory
- social-media
- niche-social-network
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Jesus Social

> A niche Christian faith-community social network — a place to check whether a religiously-active subject keeps a profile the mainstream platforms won't surface.

## When to use
You have a `name` or `username` for a subject with a known church/faith connection, and mainstream platforms (Facebook, Instagram) came up empty. Faith-based niche networks like this are where some people stay active who don't appear elsewhere — useful for corroborating a religious community, a city, or an associate list around a missing person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.jesus.social in a clean/sock-puppet browser.
2. Register a free member account (the members directory at `/members` requires login).
3. Use the member search / directory to look up the subject's `name` or `username`.
4. Read the result: a matching profile may show a display name, city/location, posts, and connections (`social-profile`, `name`).
5. Pivot: take the location or listed friends (`associate`) into people-search or map tools; take a confirmed username into a cross-platform username search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile`, display `name`, and any self-listed location/connections
- **Empty/negative result looks like:** the directory search returns no member matching the name/username — common, since this is a small platform; absence here says nothing about the person's other accounts.

## Gotchas & OpSec
- Human-in-the-loop: the full member directory is gated behind a free account-login; register with a sock puppet.
- Small user base — most subjects will NOT have a profile here; only meaningful for the religiously-active.
- Profile fields are self-reported and unverified; corroborate before relying on any detail.

## Overlaps ("do both")
- Pairs with broad username-enumeration tools (e.g. a cross-platform username checker) — this covers a faith niche those miss, while they cover the mainstream platforms this doesn't.

## Trust & verifiability
`trust: unverified` — an independent, self-run Christian social site with no identity checks; matches are investigative leads, not confirmed identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jesus-social |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
