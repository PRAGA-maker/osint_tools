---
id: facebook-profile-directory
name: Facebook Public Profile Directory
description: Use when you have a `name` and want to browse Facebook's alphabetical public directory of profiles/pages — returns public profile links you can open and enumerate.
url: https://www.facebook.com/directory/
category: social-networks
path:
- social-networks
bestFor: Browsing/enumerating public Facebook profiles and pages via the platform's alphabetical directory.
selectorsIn:
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: freemium
costNote: Free, but Facebook increasingly gates the directory behind a logged-in session and limits what's browsable.
opsec: active
opsecNote: Browsing the directory largely requires being logged in, tying activity to that Facebook account. Use a sock-puppet account, and don't view target profiles in a way that leaves a footprint (e.g. avoid friend requests, story views).
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A genuine Facebook feature (public directory of profiles/pages that opted into listing), but coverage is partial and access is increasingly login-gated and rate-limited.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- facebook.com/directory
- FB people directory
tags:
- facebook
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Facebook Public Profile Directory

> Facebook's own alphabetical directory of public profiles and pages — a browse-and-enumerate entry point when you have a name but no direct profile link.

## When to use
You have a `name` and want to find the Facebook profile(s) behind it by browsing the platform's public directory, especially when in-app search is noisy or you want to enumerate similarly-named accounts. A supporting discovery step in a Facebook workup, useful for surfacing profiles that opted into public listing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** Facebook account and open https://www.facebook.com/directory/.
2. Browse alphabetically or drill into the people/pages listings to locate the `name`.
3. Open candidate profiles and confirm identity from photos, location, and mutuals.
4. Because the directory is login-gated and partial, combine with in-app search and Google `site:facebook.com` dorks.
5. Pivot: a confirmed profile feeds `[[facebook-friend-list-scraper]]` (network) and `[[fulldp-co]]`/photo tools (face search).

## Inputs → Outputs
- **In:** `name`
- **Out:** public Facebook `social-profile` links matching the name
- **Empty/negative result looks like:** no listing — the person's profile isn't public/opted-in, uses a different name, or the directory won't load without login. Absence here doesn't mean they're not on Facebook.

## Gotchas & OpSec
- Login-gated & partial: only opted-in public profiles appear, and access increasingly needs a session — `status: degraded`.
- OpSec: **active** via the required login; use a throwaway account and avoid any interaction that notifies the target.
- Name collisions: many people share names — verify each candidate before attributing.

## Overlaps ("do both")
- Pairs with `[[facebook-photo-search-engine]]` and native Facebook search — the directory browses opted-in profiles, CSE/dorks catch Google-indexed pages the directory misses.

## Trust & verifiability
`trust: community` — a real but partial Facebook feature; a listed profile is genuine, but absence is inconclusive and access is unreliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-profile-directory |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
