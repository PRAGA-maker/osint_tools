---
id: statflux
name: Statflux
description: Use when you have an Instagram `username` and want a public-facing analytics snapshot of the account — returns `social-profile` metrics and recent `image` activity.
url: http://statflux.com/
category: social-networks
path:
- social-networks
bestFor: A quick third-party analytics view of a public Instagram account's activity and engagement.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: degraded
pricing: freemium
costNote: Advertised as a free Instagram analytics viewer; deeper reports may sit behind sign-up or paid tiers. Live functionality could not be fully confirmed at last check (page rendered no readable content), so treat availability as uncertain.
opsec: passive
opsecNote: You query a third-party analytics site about a public Instagram handle, not Instagram's authenticated surface — the subject is not notified. Use a sock-puppet browser; some such viewers inject ads or trackers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small third-party Instagram-analytics service (listed on Crunchbase, San Francisco); ownership and data sourcing are opaque and its live status is inconsistent — verify each figure independently.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- statflux.com
tags:
- instagram
- analytics
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Statflux

> A third-party Instagram analytics viewer that surfaces public-account metrics and recent activity from a handle.

## When to use
You have an Instagram `username` and want a fast, unauthenticated read on the account's public posture — follower/following counts, posting cadence, and recent media — without logging into Instagram yourself. It is a lightweight corroboration step: does the handle exist, is it active, and does its output (images, captions) match the person you are profiling?

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://statflux.com/ in a sock-puppet browser.
2. Enter the target Instagram `username`.
3. Read the returned snapshot: follower/following counts, engagement/activity indicators, and recent posts/thumbnails.
4. If the site prompts to sign up for deeper stats, weigh whether the free view already answers your question before creating an account.
5. Pivot: confirmed recent images and captions feed reverse-image search and geolocation; the live handle links back to the real Instagram `social-profile`.

## Inputs → Outputs
- **In:** `username` (Instagram handle)
- **Out:** `social-profile` metrics (counts, activity), recent `image` thumbnails
- **Empty/negative result looks like:** the handle returns no data / an error page, or the account is private (no public metrics) — not proof the account is fake.

## Gotchas & OpSec
- Live status is inconsistent — the page did not render readable content at last check, so it may be intermittently down or JS-gated; have a fallback Instagram viewer ready.
- Third-party metrics can lag or be estimated; treat counts as approximate, not authoritative.
- OpSec: passive, but expect ads/trackers on this class of site — isolate the session.

## Overlaps ("do both")
- Overlaps with other Instagram profile/analytics viewers; because any single one of these goes down often, keep a couple in rotation and cross-check the numbers.

## Trust & verifiability
`trust: unverified` — an opaque third-party service with uncertain data sourcing and flaky availability; use it only to corroborate what you can also see directly on the live Instagram profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | statflux |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
