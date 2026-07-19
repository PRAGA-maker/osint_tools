---
id: biggerpockets
name: BiggerPockets
description: Use when you have a `name`/`username` linked to US real-estate investing and want their member profile — returns bio, location, activity and connections.
url: https://www.biggerpockets.com/meet
category: communities-forums
path:
- communities-forums
bestFor: Finding a real-estate investor's community profile — bio, location, forum/blog activity, and network — on the largest US property-investing platform.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- address
- associate
status: live
pricing: freemium
costNote: Free membership lets you search members and read most forum/profile content; a paid Pro tier adds tools/data but isn't needed for basic OSINT.
opsec: passive
opsecNote: Browsing and searching profiles is passive, but a free account is generally needed to see full member details — use a sock-puppet account, and note that following/messaging is attributable to it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A large, established US real-estate-investor community. Profiles are self-authored, so treat bios/locations as self-reported claims to corroborate.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Bigger Pockets
tags:
- toddington
- curated-directory
- online-communities-blogs
- real-estate
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# BiggerPockets

> The largest US real-estate-investing community — a rich source of self-authored member profiles, forum history, and networks for anyone active in property investing.

## When to use
You have a `name` or `username` for someone connected to US real-estate investing (landlords, flippers, agents, wholesalers) and want their community footprint: a bio, stated location/market, forum and blog activity revealing interests and deals, and their connections to other members. Useful for enriching an identity, corroborating a profession/location, or mapping associates in the property world.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in with a (sock-puppet) free account at https://www.biggerpockets.com — the member directory/"meet" and full profiles generally require login.
2. Search by `name`/`username`, or browse members by location/market.
3. Read the profile: bio, stated location/`address` market, join date, forum posts, blog articles, and connections (`associate`s).
4. Mine their forum/blog history for deal locations, partners, and details that corroborate identity or reveal other accounts.
5. Pivot: a stated market/location narrows property-record searches; named partners feed associate mapping; a reused username feeds cross-platform enumeration.

## Inputs → Outputs
- **In:** `name` / `username` tied to real-estate investing
- **Out:** member `social-profile` (bio, stated location/`address` market, activity, `associate`s)
- **Empty/negative result looks like:** no matching member — the person isn't on BiggerPockets or uses a different handle; absence says nothing about their real-estate involvement offline.

## Gotchas & OpSec
- US-centric: coverage is overwhelmingly US real estate; limited value elsewhere.
- Self-reported: bios, locations, and claimed track records are user-authored — corroborate against property records and other sources.
- Human-in-the-loop: full profile/directory access needs an account — use a sock-puppet; interacting (following/messaging) exposes it.
- OpSec: passive to read; don't engage from a real identity.

## Overlaps ("do both")
- Complements property-records tools — BiggerPockets gives the self-authored persona and network; deeds/assessor records confirm actual ownership and locations.

## Trust & verifiability
`trust: community` — a legitimate large community, but profile content is self-authored. Treat bios and claimed deals as leads and verify locations/ownership against authoritative property records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | biggerpockets |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username → social-profile, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
