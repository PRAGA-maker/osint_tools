---
id: mixi
name: mixi
description: Use when you have a Japanese `username` or `name` and want to check for a mixi social profile — returns a social-profile, but most content is login-gated and the platform has declined.
url: https://mixi.jp/
category: social-networks
path:
- social-networks
bestFor: Checking for a legacy/current mixi profile of a Japanese subject.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to join; viewing member content requires a registered (and historically Japan-phone-verified) account.
opsec: active
opsecNote: Most profiles are members-only, so you must log in to view them — that account is attributable, and mixi historically required a Japanese mobile number to register. Use a dedicated sock-puppet account; viewing a profile can be visible ("ashiato"/footprints feature historically logged visitors).
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: mixi was Japan's dominant SNS in the late 2000s but has declined sharply (the company pivoted to mobile games); surviving profiles are self-asserted and often dormant.
missingPersonsRelevance: high
coverage:
- jp
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- whatsmyname-web
- wayback-machine
- mixi-japan
aliases:
- mixi.jp
- sns.mixi.co.jp
tags:
- toddington
- curated-directory
- social-media
- japan
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# mixi

> Japan's once-dominant social network, now largely dormant — of OSINT value mainly for recovering a Japanese subject's late-2000s online identity and connections.

## When to use
You have a Japanese subject's `name` or `username` and want to reconstruct an older online footprint. For people active online in Japan circa 2005–2012, mixi may hold a real-name-ish profile, diary entries, communities, and a friend network — leads that predate their current, more locked-down accounts. Expect dormancy: mixi's active user base has collapsed as the company moved to mobile games.

## How to use it (`bestInteractionPattern`: web-manual)
1. Recognize the gate: most profiles are members-only, so meaningful access needs a logged-in (sock-puppet) account; registration historically required a Japanese mobile number.
2. Search within mixi for the name/handle once logged in; or try known profile URLs directly.
3. Because of the login wall and decline, also query the Wayback Machine and search engines (`site:mixi.jp` + name) for archived/public fragments.
4. Be aware of the historical "footprints" (足あと) feature that showed profile owners who visited them.
5. Pivot: a recovered handle feeds cross-platform username enumeration; communities/friends feed an associate map.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (diary, communities, friends) — mostly behind login
- **Empty/negative result looks like:** no profile or a login wall with nothing public — expected given the decline. Fall back to archives before concluding nothing existed.

## Gotchas & OpSec
- Human-in-the-loop: account login required for most content; Japanese-number registration hurdle historically.
- OpSec: **active** — viewing under an account can be logged/visible; use a sock puppet.
- Decline: low current activity; the archive is often more useful than the live site.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` — recover archived mixi content the login wall now hides.
- Pairs with `[[whatsmyname-web]]` — carry a recovered mixi handle across other platforms.

## Trust & verifiability
`trust: unverified` — a declined platform with self-asserted, often-dormant profiles; treat anything found as a historical lead to corroborate elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mixi |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
