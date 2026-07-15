---
id: fubar
name: Fubar
description: Use when you have a `username` or `name` and want to check Fubar, a long-running social/dating "online bar" network — returns `social-profile` pages with photos, location, and interests.
url: http://fubar.com
category: social-networks
path:
- social-networks
bestFor: Searching Fubar members by handle or name to find an adult-leaning social/dating profile a mainstream search misses.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Free to join and browse; some features are paywalled. A member account is needed to see full profiles and to search effectively.
opsec: active
opsecNote: Meaningful use requires logging in, and Fubar surfaces "who viewed you", so visiting a target's profile can notify them. Use a sock-puppet account with no real details and avoid interacting.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A real, long-running niche social network (formerly LostCherry / CherryTAP); profile data is self-reported by users, so treat details as claims, not facts.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- fubar.com
- LostCherry
- CherryTAP
tags:
- toddington
- curated-directory
- social-media
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Fubar

> Fubar — a long-running, adult-leaning social/dating network styled as an "online bar" (formerly LostCherry/CherryTAP) — a place to check for a subject's profile when they're absent from mainstream platforms.

## When to use
You have a `username` or `name` and want to cover a niche social network people don't think to search. Fubar users often reuse a handle from elsewhere and fill profiles with photos, a stated city, age, and interests — useful corroboration or a fresh photo of a subject who keeps other accounts locked down.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a sock-puppet Fubar account (registration is required to search/view meaningfully) with no attributable detail.
2. Use member search for the target `username` or `name`; add a location if the search supports it.
3. Open matching `social-profile`s — read stated city (`geolocation`), age, photos, and linked interests/friends. **Do not** interact; Fubar shows profile visitors.
4. Pivot: a reused handle feeds username-search tools; a fresh photo feeds reverse-image/face search; a stated city narrows people-search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** Fubar `social-profile` → photos, self-stated `geolocation`, age, interests, connections
- **Empty/negative result looks like:** no member matches — expected for most people, since Fubar is a niche platform; absence is no signal.

## Gotchas & OpSec
- Human-in-the-loop / **account-login**: you must register to search; use a burner account.
- OpSec: **active** — logged-in browsing plus "who viewed you" means a careless visit can alert the target. Stay a passive lurker on the sock account.
- Adult-oriented content and self-reported data — verify anything you'd rely on.

## Overlaps ("do both")
- Pairs with username-search tools and `[[imvu]]` — niche social/gaming networks each catch a slice of a subject's online life; cross-check reused handles across them.

## Trust & verifiability
`trust: unverified` — the platform is genuine and live, but every profile field is user-supplied; corroborate location, age, and photos before treating them as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fubar |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
