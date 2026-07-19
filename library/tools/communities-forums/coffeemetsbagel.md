---
id: coffeemetsbagel
name: Coffee Meets Bagel
description: Use when you already know a subject uses this dating app and want to confirm their in-app profile — but note it offers no public search, so it is a weak, account-gated lookup.
url: https://coffeemeetsbagel.com
category: communities-forums
path:
- communities-forums
bestFor: Context on a subject's presence on the Coffee Meets Bagel dating app; NOT a way to search for a specific person.
selectorsIn:
- name
selectorsOut:
- social-profile
- image
status: live
pricing: freemium
costNote: Free to join and match; premium ("Beans"/subscription) unlocks extra likes and visibility. No public, non-member profile search at any tier.
opsec: active
opsecNote: There is no public search — you must create an account and can only ever see algorithmically served matches, so you cannot reliably look up a named person. Any in-app action (like/pass/message) can be surfaced to the other user. Use a sock-puppet account and never interact with a real target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: unverified
trustNote: A legitimate mainstream dating app, but from an OSINT standpoint it exposes almost nothing — no public profiles, no search — so its investigative value is minimal.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- CMB
- coffeemeetsbagel.com
tags:
- toddington
- curated-directory
- dating
- online-communities-blogs
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Coffee Meets Bagel

> A mainstream "serious dating" app — listed for completeness, but a poor OSINT source: it has no public profiles and no way to search for a specific person, only algorithmic matches inside a logged-in account.

## When to use
Reach for this only when you already have strong reason to believe a subject actively dates on Coffee Meets Bagel and you are willing to run a sock-puppet account in the hope the app happens to serve their profile as a match. Unlike a public dating directory, CMB has no browse or name search — you cannot look someone up — so it is a last-resort, low-yield check rather than a lookup tool. Prefer searchable dating/classifieds sources first.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the app and create a **sock-puppet** account (registration is mandatory; there is no web profile search).
2. Set discovery preferences (location, age, gender) as close to the subject's as possible to raise the chance their profile is served.
3. Watch the daily curated matches ("bagels") for the subject; you cannot search or jump to a specific person.
4. If served, record the profile photos (`image`) and self-described details — but do NOT like, pass or message, as those actions can be exposed to the user.
5. Pivot: any profile photo obtained feeds reverse-image/face search to confirm identity.

## Inputs → Outputs
- **In:** `name` (only as context; the app cannot be queried by it)
- **Out:** at best a served `social-profile` with `image`s and a short self-description
- **Empty/negative result looks like:** the subject is simply never served to you — the overwhelmingly likely outcome, and not evidence they are absent from the app.

## Gotchas & OpSec
- Human-in-the-loop: account + mobile app required; no desktop/public access.
- OpSec: **active** — in-app interactions notify the other user; stay strictly read-only from a burner.
- Fundamental limitation: no search means you cannot target a specific individual. Treat this as informational, not a working investigative tool.

## Overlaps ("do both")
- Pairs with searchable dating/adult directories and reverse-image tools, which — unlike CMB — let you actually query for a person.

## Trust & verifiability
`trust: unverified` — a real app, but it surfaces no public data and cannot be searched, so it yields little verifiable OSINT; anything obtained must be confirmed by reverse-image search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coffeemetsbagel |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
