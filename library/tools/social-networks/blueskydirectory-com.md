---
id: blueskydirectory-com
name: blueskydirectory.com
description: Use when you have a `name`, `username`, or interest and want to find or search Bluesky (bsky/AT Protocol) profiles, lists, and starter packs — returns `social-profile`s on Bluesky.
url: https://blueskydirectory.com/profiles
category: social-networks
path:
- social-networks
bestFor: Discovering and searching Bluesky profiles, starter packs, and lists — plus an advanced Bluesky search query builder.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free directory; no account required to browse or use the search tools.
opsec: passive
opsecNote: Browsing the directory queries blueskydirectory.com, not the target's Bluesky account — passive, no notification. Bluesky content is public via the AT Protocol; viewing a profile leaves no trace. Use a sock-puppet browser for tidiness.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built directory for the Bluesky ecosystem (by independent developers); it aggregates public Bluesky/AT Protocol data and links out to bsky.app.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bluesky Directory
- blueskydirectory
tags:
- bluesky
- BlueSky / BSky Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# blueskydirectory.com

> The community directory for Bluesky — find and search profiles, starter packs, and lists on the AT Protocol network, with an advanced Bluesky search builder.

## When to use
You have a `name`, `username`, or interest and want to locate a subject on Bluesky (a fast-growing X alternative), or discover the communities/lists/starter-packs they might belong to. Because Bluesky's native discovery is still maturing, this directory (and its query builder) is a useful way to find and filter profiles across the network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://blueskydirectory.com/profiles.
2. Browse or look up profiles by `name`/handle; explore lists (blueskydirectory.com/lists) and starter packs for communities.
3. Use the advanced search tool (e.g. the `bskysrch` utility) to build precise Bluesky queries and jump straight to results on bsky.app.
4. Open a candidate profile on bsky.app to read posts, follows, and linked accounts.
5. Pivot: reuse the handle across `[[whatsmyname-python]]`/`[[spy]]`; note the Bluesky handle often mirrors a domain the subject owns (custom-domain handles) — a strong identity link.

## Inputs → Outputs
- **In:** `name`, `username`/handle, or interest/topic
- **Out:** `social-profile`s (Bluesky accounts), plus relevant lists and starter packs; `name`/handle
- **Empty/negative result looks like:** no matching profiles — the subject may not be on Bluesky, or uses an unrelated handle. Bluesky is smaller than X, so absence is common; also search directly on bsky.app.

## Gotchas & OpSec
- Community-maintained; coverage depends on what's been indexed/submitted.
- Bluesky custom-domain handles (e.g. `name.com`) are a strong OSINT signal — they tie the account to a domain the person controls; check WHOIS on it.
- Passive; all Bluesky data is public via the AT Protocol.

## Overlaps ("do both")
- Pairs with direct bsky.app search and AT Protocol tools — the directory aids discovery and query-building, while native search/API give the fullest, freshest results.

## Trust & verifiability
`trust: community` — an independent ecosystem directory over public Bluesky data. Reliable for discovery; verify identity on the live bsky.app profile and via any custom-domain handle.
