---
id: masto
name: Masto
description: Use when you have a Mastodon handle (`username`@instance) and want to profile the account — returns social-profile, associate (followers/following), and metadata-exif (account creation, activity).
url: https://github.com/C3n7ral051nt4g3ncy/Masto
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: Enumerating a Mastodon account's profile, posts, follower/following graph, and account metadata from the command line.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: free
costNote: Free and open-source Python CLI; uses public Mastodon instance APIs, no paid tier.
opsec: active
opsecNote: Queries the target's Mastodon instance API directly, so that instance's admins can see your requests in logs. Run from a sock-puppet IP/host; Mastodon instances are small and admins often notice unusual query patterns.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source OSINT tool by a known fediverse-OSINT author (C3n7ral051nt4g3ncy); reads public instance data, so accuracy tracks whatever the instance exposes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- mastodon-github-com
- osrframework-2
aliases:
- Masto
- Mastodon OSINT
tags:
- mastodon
- fediverse
- open-source
- cli
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Masto

> A command-line Mastodon investigator: point it at `user@instance` and it pulls the profile, toots, follower/following graph, and account metadata.

## When to use
Your subject has a Mastodon/fediverse presence and you have their handle in `username@instance` form. Mastodon has no central search, so per-account tooling matters. Masto queries the account's home instance API to return the profile, recent toots, who they follow and who follows them (`associate` leads), and account metadata like creation date and activity patterns — useful for timeline-building and network mapping in the fediverse.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/C3n7ral051nt4g3ncy/Masto and install its Python requirements.
2. Run it against the handle, e.g. `user@mastodon.social` (the tool resolves the instance and calls its public API).
3. Read the output: display name/bio, avatar, account creation date, post count and recent toots, and follower/following lists.
4. Analyse: creation date + activity cadence help build a timeline; the follow graph surfaces `associate` accounts.
5. Pivot: followed/following accounts feed further fediverse lookups; a reused handle feeds username enumeration.

## Inputs → Outputs
- **In:** `username`@instance
- **Out:** `social-profile` (profile + toots), `associate` (followers/following), `metadata-exif` (creation date, activity metadata)
- **Empty/negative result looks like:** account not found or an instance that blocks/limits API queries — the handle may be wrong, deleted, or on a locked/defederated instance. Absence there isn't absence across the fediverse.

## Gotchas & OpSec
- **Active:** you hit the target's instance API directly; small-instance admins can see and notice your queries — use a sock-puppet host.
- Locked accounts and privacy-focused instances expose little via the public API.
- Data is only as complete as that instance chooses to serve.

## Overlaps ("do both")
- Pairs with the broader `[[mastodon-github-com]]` resource set (fediverse OSINT techniques) and username tools like `[[osrframework-2]]` — Masto profiles one account deeply; the others help find where the handle exists across the fediverse and beyond.

## Trust & verifiability
`trust: community` — an open-source tool by a recognised fediverse-OSINT author, reading public instance data. Inspectable and generally reliable; confirm findings against the live profile since instances can restrict what the API returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | masto |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
