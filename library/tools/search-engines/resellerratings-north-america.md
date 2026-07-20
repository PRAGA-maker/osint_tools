---
id: resellerratings-north-america
name: ResellerRatings (North America)
description: Use when you have a `username`/reviewer handle or a company and want customer-review context — returns reviewer `social-profile` fragments and store reputation tied to a `name`/`employer-org`.
url: http://www.resellerratings.com
category: search-engines
path:
- search-engines
bestFor: Checking a company's customer-review reputation and mining reviewer handles/history on an online-store rating platform.
selectorsIn:
- employer-org
- username
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to read store ratings and reviews; brands pay for the reputation-management product, but public reviews are open.
opsec: passive
opsecNote: Reading public reviews and store pages is passive. Do NOT leave reviews or contact reviewers to probe a target — that is active and attributable. Use a sock-puppet if you interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running consumer review platform; reviews are user-submitted and can be incentivized or astroturfed, so treat individual reviews as unverified.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- resellerratings.com
- ResellerRatings
tags:
- toddington
- curated-directory
- specialty-search
- reviews
source: toddington-resources
lastVerified: '2026-07-20'
---

# ResellerRatings (North America)

> A consumer store-review platform — useful for a company's reputation trail and for mining a reviewer handle's post history when that handle is a subject's.

## When to use
Two angles: (1) you have an `employer-org`/online store and want its customer-review reputation and complaints; or (2) you have a `username`/reviewer handle you suspect belongs to a subject and want to read their review history for pivots (products bought, locations, timing, writing style). ResellerRatings aggregates buyer reviews of online sellers. Direct missing-persons relevance is low; it's a corroboration source for a business reputation or a reused handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.resellerratings.com (may block automated fetchers; use a real browser).
2. Search the store/company `name` to read its rating and reviews, or search/dork a reviewer `username`.
3. For a handle match, read the reviewer's history: products, dates, and any location or personal detail disclosed.
4. Dork it too: `site:resellerratings.com "username"` to surface indexed reviews.
5. Pivot: a reused handle feeds username-enumeration; disclosed details corroborate other findings.

## Inputs → Outputs
- **In:** `employer-org`/store name, or a reviewer `username`
- **Out:** store reputation, reviews; reviewer `social-profile` fragments and history
- **Empty/negative result looks like:** no store or handle match — expected for most subjects; absence proves nothing.

## Gotchas & OpSec
- Reviews are user-submitted and can be incentivized/fake — never treat a single review as fact.
- Reviewer handles are pseudonymous; corroborate before attributing to a real person.
- OpSec: read passively; do not post reviews or contact reviewers.

## Overlaps ("do both")
- Pairs with other review platforms (Trustpilot-style) and username-enumeration — run the same handle across several review sites; cross-check store reputation against multiple sources.

## Trust & verifiability
`trust: community` — established platform but user-generated, gameable content; treat reviews and handles as leads to corroborate, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | resellerratings-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, username → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
