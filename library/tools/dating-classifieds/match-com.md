---
id: match-com
name: Match.com
description: Use when you have a `username`, photo or profile detail and want to confirm a subject's dating presence — returns dating profile, photos and self-reported details.
url: https://match.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Locating or confirming a subject's Match.com dating profile and its photos, location and self-described details.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
- image
- physical-description
- geolocation
status: live
pricing: freemium
costNote: Free to register and browse/search profiles; messaging and some filters require a paid subscription. Profile discovery is doable on a free account.
opsec: active
opsecNote: Searching requires a logged-in account, and Match shows profiles you view to its matching engine — never use your real identity. Create a dedicated sock-puppet account with a burner email and neutral photos. Viewing a profile can surface you in the target's "who viewed you" style signals, so tread carefully and never message the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Match Group, a major established dating platform; profiles are self-reported and often embellished, so treat content as claims, not verified facts.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- match
aliases:
- Match
- Match.com dating
tags:
- dating
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Match.com

> A major mainstream dating platform — search it (from a sock-puppet account) to confirm a subject's dating presence, photos and self-reported location/details.

## When to use
You suspect a subject is active on dating apps and you have a `username`, a `name`, a photo (`image`) to match, or details like age/location. Match.com profiles carry self-reported `geolocation` (city/region), a `physical-description`, photos, and lifestyle details that can confirm someone is alive and active, reveal a current city, or corroborate identity via reused photos/handles. Especially relevant in locate cases where a person has intentionally moved but stays active online.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a dedicated sock-puppet account (burner email, neutral non-identifying photos, plausible but non-real profile) — searching requires being logged in.
2. Use the search/browse filters (age, location, keywords) to narrow toward the subject; scan photos and self-descriptions for a match.
3. Confirm identity by cross-matching photos (reverse-image), reused `username`, or distinctive details — do not rely on the display name alone.
4. Pivot: a photo feeds reverse-image/face tools; a reused handle feeds cross-platform username search; a stated city narrows other location work. Do NOT message the subject.

## Inputs → Outputs
- **In:** `username` / `name` / `image` / age+location details
- **Out:** `social-profile` (dating profile), `image` (photos), `physical-description`, `geolocation` (self-reported city)
- **Empty/negative result looks like:** no matching profile in the searched area — the subject may not be on Match, may be hidden/paused, or may use different details; absence is not proof.

## Gotchas & OpSec
- Human-in-the-loop: account login is mandatory; you cannot search anonymously.
- Profiles are self-reported and frequently embellished or stale — verify photos and details independently.
- OpSec: **active** — viewing profiles can expose your sock puppet to the target; use neutral bait, never your real identity, and never initiate contact.

## Overlaps ("do both")
- Pairs with reverse-image/face tools and cross-platform username search — Match supplies the photos and handle; those tools confirm the same person across other sites.

## Trust & verifiability
`trust: trusted` — the platform is legitimate and major, but every profile field is self-reported; confirm identity through photo and handle matching, not the profile's own claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | match-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, image → social-profile, image, physical-description, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
