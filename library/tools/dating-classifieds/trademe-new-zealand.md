---
id: trademe-new-zealand
name: Trade Me (New Zealand)
description: Use when you have a `username`/`name` tied to New Zealand and want their marketplace footprint — returns a member's listings, feedback, join date and region from NZ's dominant classifieds site.
url: https://www.trademe.co.nz
category: dating-classifieds
path:
- dating-classifieds
bestFor: Profiling a New Zealand subject via their Trade Me member page — listings, feedback history and approximate location.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- address
- associate
status: live
pricing: freemium
costNote: Browsing listings and viewing public member/feedback pages is free. Buying/selling and messaging need a (free) account; there is no charge to look.
opsec: passive
opsecNote: Viewing listings and public member/feedback pages is passive and anonymous. Do not log in with a real account to snoop; if you must sign in (to message a seller), use a sock-puppet account — Trade Me shows some activity to other members.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: New Zealand's largest, long-established online marketplace (the local eBay); member pages and feedback are first-party platform data.
missingPersonsRelevance: medium
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TradeMe
- trademe.co.nz
tags:
- classifieds
- marketplace
- new-zealand
- toddington
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Trade Me (New Zealand)

> New Zealand's dominant marketplace/classifieds (the local eBay + Craigslist) — a member's page ties a handle to listings, feedback history, region and join date.

## When to use
Your subject has a New Zealand connection and you have a `username` or `name` that might match a Trade Me member. Trade Me is where most of NZ buys, sells, rents and job-hunts, so a member page can reveal what someone is selling (goods that place them, disclose a car/`vehicle-plate` context, hint at a move), their feedback timeline (activity over years), and the region they operate in. Marketplace listings often leak location, contact style, and lifestyle details useful for corroboration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.trademe.co.nz and use the search box; to check a member directly, open `https://www.trademe.co.nz/a/marketplace/members/<memberid>` or search the handle.
2. On a member page read: current/closed listings, feedback given/received (with dates and counterparties = `associate`s), member-since date, and stated region.
3. Inspect individual listings for photos and descriptions — background details, addresses in pickup instructions, and phone numbers sometimes appear.
4. Use category search (Motors, Property, Jobs) with a name/location to find listings that aren't linked from the profile.
5. Pivot: a region + listing details feed address/geolocation work; feedback counterparties are `associate` leads; a listed vehicle/property feeds transport/property tools.

## Inputs → Outputs
- **In:** `username`/member handle or `name` (best combined with a NZ location)
- **Out:** listings, feedback history, `associate` counterparties, member-since date, region (`address` clues), sometimes contact info in listings
- **Empty/negative result looks like:** no member match or an empty/withheld profile — Trade Me lets members hide feedback/listings, so absence isn't proof of no account. Try category searches by name/region.

## Gotchas & OpSec
- NZ-only in practice; useless for subjects with no New Zealand footprint.
- Common names/handles collide — disambiguate with region, feedback dates, or listing details.
- Some profile detail is member-hidden or needs login; keep to public pages for passive OpSec and use a sock puppet if you must sign in.

## Overlaps ("do both")
- Pairs with general people-search and social-username tools for the identity anchor; Trade Me adds the NZ marketplace/behavioural layer they miss. Run alongside other classifieds (e.g. local Facebook Marketplace) for fuller coverage.

## Trust & verifiability
`trust: trusted` — Trade Me is New Zealand's established, mainstream marketplace; member pages, feedback and listings are authentic first-party data. Listing *content* (descriptions/photos) is user-supplied, so verify specific claims independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trademe-new-zealand |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
