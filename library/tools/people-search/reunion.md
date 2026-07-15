---
id: reunion
name: Reunion.com
description: Use when you follow an old Reunion.com people-finder link — the brand is retired and now redirects to MyLife, a US people-search returning `address`, `phone`, and `associate` data.
url: http://reunion.com
category: people-search
path:
- people-search
bestFor: (Legacy brand) reconnecting-with-people search; now redirects to the MyLife people-search platform.
selectorsIn:
- name
selectorsOut:
- address
- phone
- associate
status: degraded
pricing: freemium
costNote: The Reunion.com brand is retired; the domain 301-redirects to mylife.com. MyLife shows teaser results free and gates full reports/contact data behind a paid subscription.
opsec: passive
opsecNote: Searching is passive, but MyLife is a reputation/people-search operator known for aggressive upsells and for compiling profiles; use a sock-puppet identity and never enter your own details or pay from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: The original Reunion.com no longer exists as a standalone service; it now points to MyLife, whose data accuracy is inconsistent and which has faced criticism over its profile/reputation practices. Verify anything it surfaces elsewhere.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- reunion.com
- MyLife (redirect target)
tags:
- people-investigations
- people-search
- defunct-brand
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Reunion.com

> A retired "find old friends/relatives" brand whose domain now redirects to MyLife, a US people-search and reputation-profile service.

## When to use
You have an old reference or bookmark to Reunion.com. Know that it no longer operates as its own reconnection network — `reunion.com` 301-redirects to **mylife.com**. If you land there, you are using MyLife: a US people-search that indexes name, age, past/present `address`, `phone`, relatives and `associate`s, and a proprietary "reputation score." Treat it as one more aggregator, not the classmate-finder it once was.

## How to use it (`bestInteractionPattern`: web-manual)
1. Expect the redirect from `reunion.com` to `mylife.com`.
2. Search by `name` (add a US city/state to narrow) in a sock-puppet browser.
3. Read the free teaser: age, city, and partial relatives/associates.
4. Stop before paying — full contact data sits behind a subscription; usually a free people-search (e.g. TruePeopleSearch, FastPeopleSearch) yields the same leads without a paywall.
5. Pivot: names of relatives/associates and prior cities become new search seeds elsewhere.

## Inputs → Outputs
- **In:** `name` (+ optional US location)
- **Out:** `address` history, `phone`, relatives/`associate` links (full data paywalled)
- **Empty/negative result looks like:** no matching profile, or only unrelated same-name people — common; MyLife's coverage and matching are imperfect.

## Gotchas & OpSec
- Brand is defunct — do not describe Reunion.com as an active reconnection service.
- MyLife is aggressive with upsells and builds profiles on people it lists; opt for free alternatives first and never pay from an attributable account.

## Overlaps ("do both")
- Substitute free US people-search tools (TruePeopleSearch, FastPeopleSearch, ThatsThem) which typically return the same address/phone/relative leads without a paywall; use MyLife only to cross-check.

## Trust & verifiability
`trust: unverified` — the original service is gone and the redirect target (MyLife) has inconsistent accuracy and a contested reputation. Corroborate every lead through an authoritative or free source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reunion |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
