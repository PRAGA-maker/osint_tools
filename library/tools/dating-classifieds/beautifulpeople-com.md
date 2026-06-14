---
id: beautifulpeople-com
name: BeautifulPeople.com
description: Use when checking a niche, member-voted dating community for a subject's profile by `username` or `image` — a small, vetting-gated platform.
url: https://www.beautifulpeople.com/en-US
category: dating-classifieds
path:
- dating-classifieds
bestFor: Checking a small vetting-gated dating community for a subject's profile
selectorsIn:
- username
- image
selectorsOut:
- social-profile
- physical-description
status: live
pricing: freemium
costNote: Free to apply/join (subject to member voting); messaging and premium features are paid.
opsec: active
opsecNote: Joining requires submitting a photo and passing a member vote; your own puppet profile becomes visible. Activity is logged.
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: BeautifulPeople is a real niche dating site; small user base limits coverage, and per-subject presence is unverified.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- dating
- niche
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# BeautifulPeople.com

> A small, "members vote you in" dating community — low coverage, but worth a targeted check if a subject is known to use exclusive/niche platforms.

## When to use
Use it only when you have a strong reason to think the subject used this specific niche site, and you have a `username` or `image` to match. Coverage is small, and the vetting gate makes access slow, so it is a low-priority pivot rather than a primary search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Apply with a sock-puppet profile and photo; access is gated by a member voting/approval step (manual-review), so this is not instant.
2. Once in, search by username/location and compare photos and handles to your subject.
3. Inspect a matching profile for self-disclosed details and a `physical-description`.
4. Pivot: confirmed photo → reverse-image search; handle → username enumeration.

## Inputs → Outputs
- **In:** `username`, `image`
- **Out:** `social-profile`, `physical-description`
- **Empty/negative result looks like:** no match (likely, given the small base) or your puppet not being approved — treat absence as inconclusive given low coverage.

## Gotchas & OpSec
- Human-in-the-loop: account login plus a member-vote approval gate; premium features paywalled.
- OpSec: active — to look you must expose a puppet profile and photo that others can see/rate. Use disposable photos that aren't reverse-searchable to you.

## Overlaps ("do both")
- Pairs with mainstream apps (`[[badoo]]`, `[[bumble]]`, `[[hinge]]`) which have far higher coverage; use this only for targeted niche checks.

## Trust & verifiability
`trust: unverified` — a genuine niche platform, but small reach and a slow access gate make per-case results unverified and low-yield.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | beautifulpeople-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, image → social-profile, physical-description |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
