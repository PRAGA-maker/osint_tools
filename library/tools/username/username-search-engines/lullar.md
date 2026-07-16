---
id: lullar
name: Lullar Profile Search
description: Use when you have a `username`, `email` or `name` and want to sweep many social platforms at once for matching profiles — returns `social-profile` links across 100+ sites.
url: https://com.lullar.com
category: username
path:
- username
- username-search-engines
bestFor: One-shot social-profile discovery across 100+ platforms from a single username, email, or name — a fast breadth-first "where does this identity exist" check.
selectorsIn:
- username
- email
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free with no signup, per the site ("100% Free, No Signup"). Anonymous searches over HTTPS.
opsec: passive
opsecNote: Queries are routed through Lullar's servers rather than sent to each platform from you, so the target platforms don't see your IP. Lullar claims no logs/tracking, but you are still handing the selector to a third party — assume it could be logged; use a puppet identity for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running free profile-search aggregator. It generates/checks profile-URL guesses across many sites, so hits need manual confirmation — false positives (unclaimed handles, name collisions) are common.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Lullar
- com.lullar.com
tags:
- username
- profile-search
- social-networks
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- lullar-2
---

# Lullar Profile Search

> A breadth-first identity sweep: enter a username, email, or name and it checks 100+ social platforms at once for matching profiles.

## When to use
You have a `username`, `email`, or `name` and want a quick map of where that identity appears online before drilling into any one platform. Reach for Lullar early in username/identity work to generate a candidate list of profiles (Instagram, TikTok, X, LinkedIn, Reddit, GitHub, etc.) to then verify. It's a starting-point tool: fast and broad, but you confirm each hit yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://com.lullar.com in a clean/puppet browser.
2. Pick the search mode — by `username`, by `email`, or by `name` — and enter the selector.
3. It returns links to profiles across its platform list. Because it largely constructs/probes profile URLs, treat the list as candidates.
4. Open and verify each hit: does the bio/photo/activity actually match your subject, or is it an unclaimed handle / different person?
5. Pivot: confirmed handles → deep-dive per platform; a reused username → run a dedicated enumerator (Sherlock/WhatsMyName) for coverage this misses.

## Inputs → Outputs
- **In:** `username`, `email`, or `name`
- **Out:** `social-profile` links across many platforms
- **Empty/negative result looks like:** few or no links — either the identity isn't widely reused, or (common) the aggregator's checks are stale for some sites. A sparse result is weak evidence of absence; corroborate with another enumerator.

## Gotchas & OpSec
- **False positives:** URL-guessing aggregators list handles that may be unclaimed or belong to someone else — verify before attributing.
- Coverage drifts as platforms change their URL schemes; some listed sites may be dead links.
- OpSec: **passive** — routed through Lullar, so target platforms don't see you; still a third party receiving your selector.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`/WhatsMyName-style enumerators and `[[whatsmyname-python]]` — Lullar is fast and web-based; those are more rigorous and scriptable. Run both, since coverage differs.

## Trust & verifiability
`trust: unverified` — a free aggregator that guesses/probes profile URLs; results are leads, not confirmations. Verify every hit on the actual platform before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lullar |
| category | username |
| selectorsIn → selectorsOut | username, email, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
