---
id: comicvine
name: Comic Vine
description: Use when you have a `username` seen elsewhere and want to check for a matching comics-community profile — returns `social-profile` and forum/activity history.
url: https://comicvine.gamespot.com
category: search-engines
path:
- search-engines
bestFor: Checking a handle against a large comics fan-community's user profiles and forum activity as a username-reuse pivot.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read profiles, wiki, and forums; a free account is only needed to post. API access is free with a registered key.
opsec: passive
opsecNote: Reading public profiles and forum posts is passive and does not notify the user. Only creating an account or posting would expose you. Browse from a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Established comics database/community owned by a major media publisher; profile content is user-generated and pseudonymous, so a handle match is a lead, not an identity confirmation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- comicvine.gamespot.com
- Comic Vine
tags:
- toddington
- curated-directory
- specialty-search
- fan-community
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Comic Vine

> A large comics encyclopedia and fan community (owned by GameSpot/Fandom) — in OSINT terms, one more site to test a reused `username` against and to read a hobbyist's public posting history.

## When to use
You have a `username` recovered from a cross-platform search and want to see whether the same handle belongs to an active member here, and if so what their public profile and forum activity reveal. Niche-interest communities like this are where people reuse a favorite handle and talk freely — a matching profile can yield an avatar `image`, interests, a rough timezone from posting times, and links they've shared, all corroborating (or breaking) a suspected identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://comicvine.gamespot.com in a sock-puppet browser.
2. Search the site for the target `username`, or go directly to `comicvine.gamespot.com/profile/<username>/` to test the handle.
3. If a profile exists, read the "About Me", join date, avatar, and activity/forum tabs — note posting cadence, topics, and any external links or other handles mentioned.
4. Use the free API with a key if you want to script handle checks across many usernames.
5. Pivot: reverse-image the avatar (`[[pimeyes]]`-style) to link the same photo elsewhere; feed any mentioned handles/links back into a cross-platform username sweep.

## Inputs → Outputs
- **In:** `username`
- **Out:** matching `social-profile` (bio, join date, avatar, forum/activity history)
- **Empty/negative result looks like:** a 404 profile page or no search hit — the handle isn't used here; weak evidence, since the person simply may not be into comics.

## Gotchas & OpSec
- Content is pseudonymous and user-generated — a handle match confirms handle reuse, not the person's real identity; corroborate before concluding.
- Niche relevance: only useful when your subject plausibly engages with comics/pop-culture fandom, or when you're brute-forcing a handle across many communities.
- OpSec: passive when reading; only account creation/posting would expose you.

## Overlaps ("do both")
- Pairs with cross-platform username finders (`[[sherlock]]`/`[[whatsmyname]]`-style) — those flag that the handle *might* exist here, and this is where you read the actual profile content.

## Trust & verifiability
`trust: unverified` — the platform is legitimate and long-running, but profiles are self-reported and anonymous, so treat any match as a lead to verify by content, not as identity proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | comicvine |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
