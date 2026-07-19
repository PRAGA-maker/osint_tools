---
id: match
name: Match (Match.com)
description: Use when you have a `name`/`username`/`image` and want to check for a dating profile — a major dating site you can browse for photos, first names, ages, and location clues.
url: https://www.match.com/
category: communities-forums
path:
- communities-forums
bestFor: Discovering or confirming a subject's dating profile (photos, first name, age, city, self-described details) on a mainstream dating platform.
selectorsIn:
- name
- username
- image
selectorsOut:
- social-profile
- image
- physical-description
status: live
pricing: freemium
costNote: Free to register and browse/search profiles; messaging and some features require a paid subscription.
opsec: active
opsecNote: ACTIVE — you generally need an account to search, and Match shows profiles you view / may surface you to them ("who viewed you", suggested matches). Use a sock-puppet account, never your own; never message or interact with the subject. Assume viewing can leave a trace.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate mainstream dating site (Match Group); profiles are self-authored and often embellished or partly anonymised, so treat details as claims.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- match-com
aliases:
- Match.com
tags:
- toddington
- dating
- social-profile
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Match (Match.com)

> A mainstream dating platform — browse for a subject's profile to recover photos, a first name, age, and location clues.

## When to use
You suspect a subject uses online dating and want to find or confirm their profile. Dating profiles often expose a recent `image`, first `name`, age, city/neighbourhood, occupation, and lifestyle details a person keeps off other public profiles — valuable for identification and locating.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a sock-puppet account (dedicated email, plausible persona) — searching generally requires login.
2. Set search filters approximating the subject: age range, gender, location radius.
3. Browse results; match on `image` (reverse-image the photos), first name, age, and self-described details.
4. Read the output: a candidate `social-profile` with photos, `physical-description`, and location clues. Pivot: reverse-image the photos, and cross-check the same photos/handle on other dating/social platforms.

## Inputs → Outputs
- **In:** `name` / `username` / `image` + approximate location & age
- **Out:** a dating `social-profile` — photos (`image`), first name, age, `physical-description`, city
- **Empty/negative result looks like:** no matching profile means they don't use Match (try other dating apps) or their filters/visibility exclude your search — absence isn't proof.

## Gotchas & OpSec
- **Active and account-gated:** never use a personal account; viewing profiles can notify or resurface you. Do not interact with the subject.
- Profiles are self-reported — names/ages/photos may be false or dated; corroborate.
- Human-in-the-loop: account login required.

## Overlaps ("do both")
- Do both with reverse-image search and other dating platforms — the same photo often appears across sites, confirming identity and surfacing more detail.

## Trust & verifiability
`trust: community` — real platform, but user-authored content; verify photos via reverse image and details against independent sources before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | match |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username, image → social-profile, image, physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
