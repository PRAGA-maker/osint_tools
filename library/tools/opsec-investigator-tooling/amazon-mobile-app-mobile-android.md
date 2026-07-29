---
id: amazon-mobile-app-mobile-android
name: Amazon Mobile App (Mobile – Android)
description: Use when you have a `name`, `email`, or `username` and want to surface a subject's public Amazon presence — returns wishlist-derived `address` (ship-to city) and a confirmed `name`.
url: https://play.google.com/store/apps/details?id=com.amazon.mShop.android.shopping&hl=en
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Reaching a subject's public Amazon wishlists, reviews and profile from a mobile device to pull a first name + ship-to city.
selectorsIn:
- name
- email
- username
selectorsOut:
- address
- name
status: live
pricing: free
costNote: The app is free; an Amazon account (free to create) is needed to log in and browse most features, but public wishlist/profile pages are reachable without it.
opsec: passive
opsecNote: Browsing another person's public Amazon wishlist or reviewer profile is passive and does not notify them. Do NOT add items to a cart from their list, message the seller, or browse while logged into a personal account — use a clean sock-puppet Amazon account so your own name/recommendations never leak into the session and purchases are never accidentally tied to the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Official Amazon.com shopping client published by Amazon; the underlying data (wishlists, reviews, profiles) is first-party and only as public as the subject chose to make it.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Amazon Shopping app
- Amazon Android app
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Amazon Mobile App (Mobile – Android)

> Amazon's shopping client — an OSINT surface only insofar as it reaches a subject's public wishlists, reviewer profile, and ship-to hints.

## When to use
You have a `name`, `email`, or `username` and want to check whether the subject exposes anything on Amazon: a public **wish list** (often shows a first name and a ship-to city/state), a **reviewer profile** (a stable pseudonym with a review history that can leak location, purchases, and interests), or a seller storefront. This is a corroboration/enrichment surface, not a primary people-search — reach for it once you already suspect an Amazon identity.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the Amazon Shopping app and sign in with a **sock-puppet** Amazon account (never a personal one — Amazon personalizes and logs the session).
2. Public **wish lists**: use the "Find a List or Registry" search (or the web equivalent at `https://www.amazon.com/hz/wishlist/ls`) and search the subject's `name`/`email`; a matching public list shows the owner's stated first name and, at add-to-cart visibility, a shipping city/state.
3. Reviewer **profile**: if you have a review byline (`username`/name), open the reviewer's profile to read their review and location history.
4. Read the output: a ship-to city, a confirmed first name, or a purchase/interest pattern that corroborates identity.
5. Pivot: the city feeds address/people-search tools; the reviewer pseudonym feeds `username` cross-platform search.

## Inputs → Outputs
- **In:** `name`, `email`, or `username`
- **Out:** `address` (ship-to city/state inferred from a wishlist), `name` (confirmed first name / reviewer byline)
- **Empty/negative result looks like:** no matching public list or profile — the subject either has no Amazon presence or (far more likely) kept it private. Absence is not proof of no account.

## Gotchas & OpSec
- Human-in-the-loop: an Amazon account login is required for most browsing; solve any device verification manually.
- OpSec: passive reading only. Never purchase from a target's list, message them, or browse while logged into your own identity — Amazon's "recommended for you" and order history will contaminate the trail.
- Most wishlists are private by default; the technique only works when the subject opted into public sharing.

## Overlaps ("do both")
- Pairs with `[[twitter-social-networking-mobile-ios]]` and other social apps — cross-reference a reviewer pseudonym or wishlist first name against the same handle elsewhere.

## Trust & verifiability
`trust: trusted` — the app is Amazon's genuine first-party client, so any data it surfaces is authentic; the only reliability limit is how much the subject chose to make public.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-mobile-app-mobile-android |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, email, username → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | yes (account-login) |
