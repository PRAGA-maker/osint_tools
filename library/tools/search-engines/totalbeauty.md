---
id: totalbeauty
name: TotalBeauty
description: Use when you have a `username` and want to check a beauty-review community profile — returns social-profile confirmation and associate-style reviewer activity.
url: http://www.totalbeauty.com/reviews
category: search-engines
path:
- search-engines
bestFor: Confirming a username against a beauty-review community and reading a member's public review history.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse reviews and public member profiles; writing reviews requires a free account, but reading does not.
opsec: passive
opsecNote: You read public member/review pages; the member is not notified. If you log in to interact, that ties activity to your account — use a sock-puppet account, and avoid any action that alerts the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A consumer beauty-review site; member content is self-submitted and unverified, useful only as a username/social-footprint signal.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- totalbeauty.com
tags:
- toddington
- curated-directory
- specialty-search
- username-enumeration
- community-profile
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# TotalBeauty

> A consumer beauty-review community — niche value in OSINT as one more site where a reused `username` may resolve to a public member profile and review trail.

## When to use
You are enumerating a `username` across platforms and want to check whether the subject has a footprint on this beauty-review community. A hit gives you a public member profile, a review history (products bought, opinions, timing), and sometimes location or demographic hints in the profile — small but corroborating pieces when building a persona.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the member-profile path directly: `http://www.totalbeauty.com/community/members/<username>`, or use the site's search.
2. If a profile exists, read the reviewer's public activity: points, review count, product categories, and any self-described bio/location.
3. Compare writing style, timing, and interests against the subject's footprint on other platforms to judge whether it's the same person.
4. Note reviewed products/timeline as lifestyle signal.
5. Pivot: a confirmed handle feeds cross-platform username searches; profile text may leak a real name or location.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (member page + public review history)
- **Empty/negative result looks like:** a 404 or no matching member — the handle isn't used here (or is spelled differently). A miss is expected; this is a low-population niche site.

## Gotchas & OpSec
- Low base rate: most subjects have no account here, so treat this as a supplementary username check, not a primary source.
- Member content is self-reported and unverified — a username match is a lead, not identity confirmation.
- OpSec: passive when reading; don't log in with a real account or take actions that notify the member.

## Overlaps ("do both")
- Use inside a broader username-enumeration sweep (Sherlock-style tools and other community sites): this covers one niche those may not include.

## Trust & verifiability
`trust: community` — a consumer review community with no identity verification; corroborate any real-name/location inference against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | totalbeauty |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
