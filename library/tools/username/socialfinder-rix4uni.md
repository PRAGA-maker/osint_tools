---
id: socialfinder-rix4uni
name: socialfinder (rix4uni)
description: Use when you have a `username` and want to enumerate which social/dev/gaming sites it exists on — returns a streamed list of `social-profile` URLs.
url: https://github.com/rix4uni/socialfinder
category: username
path:
- username
bestFor: Fast command-line username-to-account enumeration across a couple dozen platforms.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open source (Go). No account or API key.
opsec: passive
opsecNote: Requests come from your IP directly to each target platform, one per site. It is passive reconnaissance (no login, no interaction with the target), but the checked sites see your IP and user-agent — run from a VPN/sock-puppet host if you don't want your address in their logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small single-author Go tool (rix4uni) with a modest star count; useful but not widely audited. Confirm every hit manually — username collisions and false positives are common.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- sherlock
- maigret
- whatsmyname
aliases:
- socialfinder
- rix4uni socialfinder
tags:
- username-enumeration
- cli
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# socialfinder (rix4uni)

> A fast Go CLI that checks a single username across ~24+ social, developer and gaming platforms and streams back the profile URLs where it exists.

## When to use
You have a `username` (a handle, gamertag, or email localpart used as a handle) and want a quick first pass at which platforms it is registered on. Good as a lightweight, scriptable enumerator when you don't want to spin up a heavier framework — but treat its output as leads to confirm, not proof.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/rix4uni/socialfinder@latest` (or grab a prebuilt binary from the releases page).
2. Run: `socialfinder <username>` — results stream in real time with the platform name and matching URL.
3. Useful flags: `-file` to supply your own URL list, `-nsfw` to include adult sites, `-silent` for clean/pipeable output.
4. Open each returned URL and confirm the account is really your subject (photo, bio, linked accounts) — the tool only checks existence, not identity.
5. Pivot: confirmed `social-profile` hits feed profile-enrichment and cross-account correlation; a common bio/avatar across sites strengthens attribution.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` URLs on each platform where the handle resolves, plus a total count
- **Empty/negative result looks like:** no platform lines and a zero count — meaning the handle wasn't found on its built-in list, not that the person has no online presence (try handle variants and other enumerators).

## Gotchas & OpSec
- Existence ≠ identity: the same handle on GitHub and TikTok may be two different people. Always corroborate.
- Coverage is modest (~two dozen sites) and hard-coded, so it misses many networks; run alongside a broader enumerator.
- Passive but not invisible — each checked site logs your request. Use a VPN/sock-puppet if attribution matters.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`, `[[maigret]]` and `[[whatsmyname]]` — those cover hundreds of sites and reduce false negatives; socialfinder is the fast first sweep, they are the thorough follow-up.

## Trust & verifiability
`trust: community` — a small, single-maintainer open-source project. The code is inspectable and passive, but coverage and accuracy are unaudited, so verify each hit by hand.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialfinder-rix4uni |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
