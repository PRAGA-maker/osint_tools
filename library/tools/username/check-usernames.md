---
id: check-usernames
name: Check Usernames
description: Use when you have a `username` and want to see which social networks it is registered on — returns a taken/available grid across ~150+ platforms.
url: https://checkusernames.com/
category: username
path:
- username
bestFor: Quick visual sweep of which social platforms a single username is taken on.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: The basic checkusernames.com availability grid is free; deeper checks, monitoring and auto-registration are upsold through its parent service KnowEm (paid).
opsec: passive
opsecNote: Checks run server-side from KnowEm's infrastructure, not your IP, so the target platforms don't see you directly — but you hand the target handle to KnowEm, which logs the query. It only tells you a handle is taken, not who owns it, so leakage about the subject is minimal. Use a sock-puppet if even the lookup should be unattributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running KnowEm-operated brand-protection tool (formerly the original CheckUserNames). Built for brand/handle availability, so a "taken" mark means the handle exists — not that it belongs to your subject.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- knowem
- whatsmyname
- namechk
aliases:
- CheckUsernames
- checkusernames.com
tags:
- username-enumeration
- brand-protection
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Check Usernames

> A one-box username availability checker (KnowEm's original brand) that shows, across ~150+ social networks, whether a handle is taken — i.e. an account likely exists.

## When to use
You have a `username` and want a fast, visual read on which platforms it's registered on. Because a "taken/unavailable" result means an account with that handle exists, this doubles as a coarse account-enumeration sweep — a quick first pass before running a heavier, link-yielding enumerator. Best treated as a signpost ("this handle is used on X, Y, Z"), not as identity confirmation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://checkusernames.com/.
2. Enter the `username` and run the check; it queries ~150+ networks server-side.
3. Read the grid: red/"not available" (or "taken") = an account exists on that platform; green/"available" = the handle is free (no account).
4. For each "taken" platform, go to that site and load the profile to confirm it's your subject — this tool marks existence, not ownership, and gives no direct profile link on the free tier.
5. Pivot: the list of platforms-in-use feeds targeted profile pulls and cross-account correlation; deeper coverage is on KnowEm.

## Inputs → Outputs
- **In:** `username`
- **Out:** a taken/available map implying `social-profile` existence per platform
- **Empty/negative result looks like:** all platforms showing "available" — meaning the handle is unused across its list (try handle variants). Note it reports availability, not URLs, so you still resolve each hit manually.

## Gotchas & OpSec
- "Taken" ≠ "your subject." A common handle will be taken by many unrelated people; always open and verify the actual profile.
- It reports availability status, not clickable profile links (that's the free-tier limitation); expect a manual step to reach each account.
- Passive and run from KnowEm's servers, so target platforms don't see your IP — but KnowEm sees your query.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` and `[[namechk]]` — those return actual profile URLs and are better for confirmation, while Check Usernames gives a broad availability snapshot. Its parent `[[knowem]]` extends coverage and monitoring.

## Trust & verifiability
`trust: community` — a well-established KnowEm-run service, but built for brand/handle protection rather than investigation, so its "taken" signal only proves an account exists. Confirm ownership on the platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | check-usernames |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
