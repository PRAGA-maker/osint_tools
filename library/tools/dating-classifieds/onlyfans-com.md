---
id: onlyfans-com
name: onlyfans.com
description: Use when you have a `username` and want to confirm/read a subject's public OnlyFans creator profile — returns `social-profile`, `name`, sometimes `geolocation`.
url: https://onlyfans.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Confirming a creator handle exists on OnlyFans and reading the public profile header (display name, bio, avatar, linked socials) without paying.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Viewing a creator's public profile page (display name, bio, avatar, banner, free posts) is free; the paywalled feed requires a subscription/payment.
opsec: active
opsecNote: A logged-out visit to onlyfans.com/<handle> is largely passive, but interacting (subscribing, tipping, messaging, following) is attributable and notifies the creator. If you must log in, use a sock-puppet account and payment method, never an attributable one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party platform — the profile header it serves is authentic; display names and bios are self-asserted by the creator, so treat them as claims.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- coomer-st
aliases:
- OnlyFans
tags:
- onlyfans
- adult
- creator-platforms
- OnlyFans Related Sites
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# onlyfans.com

> The primary creator subscription platform — its public profile pages act as a username-existence check that also leaks a display name, bio, avatar and linked socials without paying.

## When to use
You have a `username` and want to know whether it maps to an OnlyFans creator, and to harvest the public header: display name, bio text, profile/banner images (reverse-image fodder), pinned free posts, and any external links the creator lists (Instagram, Twitter/X, Linktree). Useful for corroborating an alias, confirming a person's online-work presence, or getting a `name`/photo pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go directly to `https://onlyfans.com/<handle>` (guess from a known username; handles are lowercase, no spaces).
2. Read the public header without logging in: display `name`, bio, subscription price, free/preview posts, and the avatar/banner. Save the images for reverse-image search.
3. Note any external social links or a location/timezone hint in the bio.
4. Pivot: run the avatar/banner through face/image search; feed listed socials into `social-profile` tools; a confirmed handle strengthens username enumeration across other sites.

## Inputs → Outputs
- **In:** `username` (creator handle)
- **Out:** `social-profile` (the profile + linked accounts), `name` (self-asserted display name), avatar/banner images, occasionally a `geolocation` hint in the bio
- **Empty/negative result looks like:** a "user not found" page (handle doesn't exist) or a bare profile with a paywall and no free content — existence is still confirmed even when the feed is locked.

## Gotchas & OpSec
- Display names and bios are self-asserted — treat the `name` as a claim to corroborate, not proof.
- Do not subscribe, tip, message, or follow from an attributable account; those actions notify the creator. Use a dedicated sock puppet if login is unavoidable.
- Mirror/aggregator sites exist but are legally and ethically fraught and often stale — prefer the first-party public header for a clean, current check.

## Overlaps ("do both")
- Pairs with `[[coomer-st]]` — a known aggregator index of creator handles; cross-check it to catch handles or archived content the locked first-party feed hides, but treat the first-party page here as the authoritative existence check.

## Trust & verifiability
`trust: trusted` — it is the genuine first-party platform, so the profile is real; the caveat is that identity fields are creator-supplied, so verify names/locations independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlyfans-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
