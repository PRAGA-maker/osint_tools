---
id: gaddr
name: Gaddr
description: Use when you have a `username` and want to find every social platform where that handle is registered, aggregated under one profile view — returns linked social profiles and name/identity hints.
url: https://gaddr.me
category: username
path:
- username
bestFor: Aggregating one handle's presence across many social platforms into a single account map.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: freemium
costNote: Historically free to check a handle; advanced/aggregated features may sit behind an account or paid tier. At last check the site was intermittently unavailable (HTTP 503), so availability is not guaranteed.
opsec: passive
opsecNote: Passive — it queries platforms' public presence for a handle, not the subject directly. As with any hosted aggregator, your query is processed on the operator's servers; use a sock-puppet browser and don't log in with a real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A username-aggregation service recommended across several curated OSINT source lists (MetaOSINT cites 4), but operator identity is thin and the site has shown uptime issues — corroborate every hit.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- gaddr.me
tags:
- username
- username-enumeration
- social-aggregation
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Gaddr

> A username-centric aggregator that gathers the social platforms where a single handle is used and presents them together — turning one `username` into a map of a subject's accounts.

## When to use
You have a `username` and want a fast, consolidated view of which platforms that handle appears on, rather than checking each site by hand. It's a strong early move in a missing-person workup once you've recovered a handle (from an email, a bio, a screenshot): a confirmed cluster of same-handle accounts links a person's online identity together and surfaces new profiles to mine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gaddr.me in a browser (sock-puppet session; expect occasional downtime — retry if it's unavailable).
2. Enter the exact `username`.
3. Read the aggregated result: the platforms where the handle resolves to an account, with links.
4. Open each linked `social-profile` and confirm it's the same person (avatar, bio, activity) — a shared handle can belong to different people.
5. Pivot: cross-check the same handle in a second enumerator (`[[360username-com]]`, `[[username-check]]`); reverse-image the avatars; extract names/locations from bios.

## Inputs → Outputs
- **In:** `username`
- **Out:** aggregated `social-profile` links, `name`/identity hints from the matched profiles
- **Empty/negative result looks like:** the handle resolves nowhere, or the service is down (503) and returns nothing — treat "nothing" here as inconclusive and fall back to other enumerators, not as proof the handle is unused.

## Gotchas & OpSec
- Uptime is unreliable (observed 503s) — don't build a workflow that depends solely on it; keep alternative enumerators ready.
- Handle collisions are common: same string ≠ same person. Confirm each hit before attributing.
- It checks the exact handle only; try variants (underscores, digits, name+year) separately.
- Operator accountability is thin; enter only the handle, never personal data or a real login.

## Overlaps ("do both")
- Pairs with `[[360username-com]]`, `[[username-check]]` and `[[username-checker]]` — run several, because each covers a different platform set and different sites false-negative on each.
- Feed confirmed profiles into face/image tooling and into `[[wayback-machine-2]]` to recover deleted versions.

## Trust & verifiability
`trust: community` — cited in multiple curated OSINT lists but operator-thin and intermittently down. Useful as a lead generator; every profile it returns must be independently confirmed as belonging to your subject before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gaddr |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
