---
id: footprintiq
name: FootprintIQ
description: Use when you have a `username`, `email`, or `phone` and want a one-shot exposure scan — returns matched `social-profile`s across 500+ platforms, breach hits, data-broker listings, and reverse image/face matches.
url: https://footprintiq.app
category: username
path:
- username
- username-search-engines
bestFor: A fast single-selector footprint scan that fans a username/email/phone across 500+ platforms and cross-references breaches and data-broker listings.
selectorsIn:
- username
- email
- phone
selectorsOut:
- social-profile
- email
- image
- address
status: live
pricing: freemium
costNote: A basic exposure scan is free with no card and no sign-up. Deep scans, image intelligence, continuous monitoring and broker-removal automation are Pro (paid).
opsec: active
opsecNote: Queries route through FootprintIQ's infrastructure and out to target platforms, which may log the lookup. It is marketed for scanning your OWN footprint — running it on a third party is fine for OSINT but assume the query is attributable to FootprintIQ, not you; still use a sock-puppet where the selector is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial exposure-scanning SaaS; cross-platform username matching is inherently noisy (name collisions), so treat hits as candidates to confirm, not identity proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- xsint
aliases:
- footprintiq.app
tags:
- username
- footprint
- breach
- data-broker
- aggregator
source: arf-seed
lastVerified: '2026-07-13'
enrichment: full
---

# FootprintIQ

> A digital-footprint scanner: feed it one selector and it fans out across 500+ platforms, breach corpora, data brokers and reverse-image search in a single pass.

## When to use
You have a single `username`, `email`, or `phone` and want breadth fast — a first-pass map of where that selector shows up online, whether it appears in breaches, and which data brokers list it. It is a good opening sweep before you commit time to any one platform, and its data-broker and reverse-image angles catch surfaces a pure username checker misses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://footprintiq.app and choose "Run a Free Scan".
2. Enter the `username`, `email`, or `phone`; the free basic scan runs without an account.
3. Read the results: matched `social-profile`s (500+ platforms), email-breach hits, data-broker listings (Spokeo, BeenVerified, etc.), phone reputation, and reverse image/face matches.
4. For deep scans, image intelligence and monitoring, upgrade to Pro.
5. Pivot: confirmed profiles feed platform-specific enrichment; a data-broker listing feeds people-search; a reverse-image hit feeds face search.

## Inputs → Outputs
- **In:** `username`, `email`, or `phone`
- **Out:** `social-profile` matches, breach `email` exposure, data-broker `address` listings, reverse `image`/face matches
- **Empty/negative result looks like:** a scan returning few/no matches — common for very generic usernames (collision-filtered) or for someone with a small footprint; absence is weak evidence, and some depth is gated behind Pro.

## Gotchas & OpSec
- Username matching across 500+ sites is noisy: a "hit" can be a different person who reused the handle — confirm each with corroborating detail.
- Free tier is shallow by design; a null there does not mean a Pro deep scan would also be empty.
- OpSec: **active** — lookups traverse FootprintIQ and target platforms; treat as attributable and use throwaway inputs where needed.

## Overlaps ("do both")
- Pairs with `[[xsint]]` and dedicated username enumerators — FootprintIQ adds broker/breach/image angles, while a CLI enumerator gives you raw, un-paywalled per-site checks to cross-verify.

## Trust & verifiability
`trust: unverified` — a commercial scanner with opaque sourcing; useful for leads and breadth, but confirm any load-bearing match independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | footprintiq |
