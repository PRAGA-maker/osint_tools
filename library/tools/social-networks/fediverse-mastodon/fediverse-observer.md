---
id: fediverse-observer
name: Fediverse Observer
description: Use when you're hunting a subject across the Fediverse and need to map instances — returns a filterable list of Mastodon/Fediverse servers by software, country, size, and status.
url: https://fediverse.observer/
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: Discovering and filtering Fediverse/Mastodon instances (by software, country, language, size) to know where to look for a decentralized-network subject.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free directory/monitoring of Fediverse instances; a public API is available. No account needed to browse.
opsec: passive
opsecNote: Querying the Observer's aggregated database is passive and does not touch individual instances or users. Actual profile hunting on a specific instance is a separate, potentially active step — apply precautions there, not here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community monitoring service tracking Fediverse instance metadata (uptime, user counts, software); reliable for instance discovery, though it maps servers, not individual accounts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mastodon
- blueskydirectory-com
aliases:
- Fediverse Observer
- fediverse.observer
tags:
- fediverse
- mastodon
- instance-directory
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Fediverse Observer

> A directory and health monitor of the Fediverse — filter thousands of Mastodon/Pleroma/etc. instances by software, country, language, and size to figure out *where* a decentralized-network subject might be.

## When to use
Your subject may be on the Fediverse (Mastodon and friends), where there's no central search, so identity hunting means knowing which instances exist and which fit a subject's country/language/interest. Fediverse Observer maps the instance landscape — helping you shortlist servers to search a `username` on, or understand the community/region an instance serves.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fediverse.observer/ and filter instances by software type, country, language, or size.
2. Read the per-instance metadata: user counts, uptime, software version, registration status, and location.
3. Use the shortlist to decide where to search the subject's `username` (Fediverse has no global search, so instance choice matters).
4. For automation, use the Observer's API to pull instance lists programmatically.
5. Pivot: candidate instances feed per-instance profile lookups and `[[mastodon]]` search; a country filter helps target a region-linked subject.

## Inputs → Outputs
- **In:** filters — a `geolocation`/country, language, software, or size
- **Out:** a list of instances (`social-profile` hosts) with `metadata-exif`-style server metadata
- **Empty/negative result looks like:** overly narrow filters return few/no instances — loosen them; the tool maps servers, so it won't itself find a person, only where to look.

## Gotchas & OpSec
- It indexes **instances, not accounts** — it narrows the haystack but doesn't find the needle; you still search each instance for the person.
- Instance metadata (user counts, status) is a snapshot and can be stale.
- OpSec: passive at the directory; searching a specific instance for a target is a separate step with its own footprint.

## Overlaps ("do both")
- Pairs with `[[mastodon]]` (searching within instances) and `[[blueskydirectory-com]]` (the parallel Bluesky/AT-proto ecosystem) — decentralized subjects may be on either; map both.

## Trust & verifiability
`trust: community` — a reliable community monitor of instance metadata. Trust it for instance discovery; verify any individual account by visiting the instance itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fediverse-observer |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
