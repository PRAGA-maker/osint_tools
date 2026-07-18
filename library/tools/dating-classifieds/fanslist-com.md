---
id: fanslist-com
name: fanslist.com
description: Use when you have a `username` or `name` and want to find a matching OnlyFans creator profile — returns the creator's `social-profile` and linked handles.
url: https://fanslist.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching a large index of OnlyFans creators by handle/name to locate a profile and its stats.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to search and browse; the site aggregates public OnlyFans profile data (1.2m+ indexed accounts).
opsec: passive
opsecNote: Passive — you query a third-party aggregator, not OnlyFans, so the creator is not notified. The site operator sees your search terms. It indexes only public profile metadata; do not treat presence here as anything beyond a public account existing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent aggregator, explicitly not affiliated with OnlyFans; indexes public data and its coverage/accuracy is unverified against the source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FansList
tags:
- onlyfans
- OnlyFans Related Sites
- creator-search
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# fanslist.com

> A free, searchable index of 1.2M+ OnlyFans creators — pivot a username or name to a public creator profile and its linked handles.

## When to use
You have a `username` (or display `name`) and suspect the subject maintains an OnlyFans presence, or you want to check whether a reused handle maps to a creator account. Useful for linking an alias across platforms: an OnlyFans creator often cross-promotes the same handle on Twitter/X, Instagram, Telegram, etc., so a hit here can open new `social-profile` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fanslist.com/.
2. Use the search box / advanced search to enter the `username` or `name`; optionally filter by country or account type.
3. Open a matching result to view the creator's profile card: display name, handle, country, and links back to the OnlyFans page and any cross-linked socials.
4. Pivot: take the confirmed handle and linked profiles into username-enumeration and social-network tools; note the country as a geolocation lead.

## Inputs → Outputs
- **In:** `username` or `name`.
- **Out:** matching creator `social-profile`(s), canonical `username`/handle, country, and cross-linked accounts.
- **Empty/negative result looks like:** no matching creator card — meaning the handle/name isn't in FansList's index (which covers only creators it has crawled, not all OnlyFans users).

## Gotchas & OpSec
- Third-party index: coverage is a subset of OnlyFans and may be stale; absence is not proof the subject has no account.
- Adult content: results are NSFW creator profiles — handle within your authorization and evidence-handling rules.
- Identity caution: many creators use stage names; a matching handle is a lead, not proof of identity — corroborate before asserting.
- OpSec: passive; the creator is not notified, but the aggregator logs your queries.

## Overlaps ("do both")
- Pairs with username-enumeration tools (e.g. Sherlock-style handle checkers) — those tell you *where* a handle exists broadly, while FansList confirms and enriches the OnlyFans-specific profile.

## Trust & verifiability
`trust: community` — an independent aggregator not affiliated with OnlyFans; treat its data as an unverified public-data mirror and confirm any live profile directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fanslist-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
