---
id: fansearch
name: Fansearch
description: Use when you have a `username`, `name`, or `geolocation` and want to find a subject's OnlyFans creator profile — returns a `social-profile` link plus display name and location.
url: https://www.fansearch.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Locating a person's OnlyFans creator account from a handle, display name, or country.
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to browse and search the creator index; no account required. The OnlyFans creators it links to may charge their own subscription fees.
opsec: passive
opsecNote: This is a third-party index, not OnlyFans itself — searching here does not touch the target's account and sends no notification. Browsing returns adult content; use a sock-puppet browser/profile and expect NSFW results. Do not log into or subscribe to a linked OnlyFans page from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent scraper/aggregator of public OnlyFans data, not affiliated with OnlyFans. Index is large but unverified and may be stale or SEO-padded; confirm any hit against the live OnlyFans profile.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- fansearch.com
tags:
- onlyfans
- creator-search
- adult
source: osintambition-social
lastVerified: '2026-07-18'
enrichment: full
---

# Fansearch

> Third-party OnlyFans search index — pivot a username, display name, or country into a subject's adult-creator profile.

## When to use
You have a `username`, real/display `name`, or a target `geolocation` (Fansearch groups creators by 70+ countries) and want to check whether the subject runs an OnlyFans page. Useful for corroborating an alias, tying a handle to a location, or surfacing a monetised alias a subject keeps separate from their mainstream profiles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.fansearch.com/ in a sock-puppet browser (adult content).
2. Search the `username` or display `name`, or browse by country/category if you only have a `geolocation` and physical description.
3. Read the result cards: profile image, display name, follower/post counts, subscription price, and a link out to the OnlyFans page.
4. Confirm a hit by opening the linked OnlyFans profile — match the avatar, bio, and any cross-linked Instagram/TikTok handles the card shows.
5. Pivot: a confirmed handle feeds cross-platform username tooling; the linked Instagram/TikTok feeds social-network OSINT.

## Inputs → Outputs
- **In:** `username`, `name`, or `geolocation`
- **Out:** `social-profile` (OnlyFans page + any linked IG/TikTok), `username`, display name, follower/price metadata
- **Empty/negative result looks like:** no matching cards, or only generic "top creators" filler unrelated to the query — treat as "not indexed here," not proof the subject has no OnlyFans.

## Gotchas & OpSec
- Adult content throughout; isolate the session and expect NSFW imagery.
- The index is scraped and SEO-optimised — display names collide and stale/renamed accounts persist, so always verify against the live OnlyFans profile before attributing.
- OpSec is passive here (you query Fansearch, not the target), but never subscribe to or message the linked creator from an attributable account — that IS active and notifies the owner.

## Overlaps ("do both")
- Pairs with broad cross-platform username checkers because Fansearch covers the adult niche those tools usually skip, while they cover the mainstream platforms Fansearch ignores.

## Trust & verifiability
`trust: community` — an unaffiliated aggregator of public OnlyFans data. Good for discovery, weak for confirmation: treat every hit as a lead to verify on the source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fansearch |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, geolocation → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
