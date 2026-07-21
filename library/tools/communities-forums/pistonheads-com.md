---
id: pistonheads-com
name: pistonheads.com
description: Use when you have a `username` (or a car/plate a subject is known to own) and want to find their PistonHeads forum posts, profile and classified/auction listings — returns `social-profile`, `associate` and vehicle/`address`-adjacent leads.
url: https://www.pistonheads.com/gassing/
category: communities-forums
path:
- communities-forums
bestFor: Pivoting a UK car-enthusiast subject from a forum handle to years of posts, garage details, and vehicles for sale.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
- associate
status: live
pricing: free
costNote: Reading forums, profiles and classifieds is free; an account (free) is needed only to post or message.
opsec: passive
opsecNote: Browsing threads, profiles and listings while logged out is passive. Do NOT register or message a member from a real identity — use a sock-puppet account, since PistonHeads shows "last active" and can notify a user of profile views/DMs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: PistonHeads is a long-running (since 1998) UK automotive community now owned by CarGurus; content is user-generated, so treat individual claims as unverified.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- PistonHeads
- Gassing Station
tags:
- forums
- Forums
- automotive
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# pistonheads.com

> The UK's largest car-enthusiast forum and marketplace — a rich place to turn a motoring subject's handle into posts, vehicles, locations, and social circle.

## When to use
The subject is a UK-based car enthusiast and you have a likely `username`, or you know a vehicle/registration they own or discuss. PistonHeads members post over years — often leaking home region, cars owned (with plates visible in photos), meet-ups attended, and who they associate with — making it a strong corroboration and social-graph source when a subject is into cars.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.pistonheads.com/gassing/ (the "Gassing Station" forums) in a sock-puppet browser.
2. Search a candidate `username` via the site search, or run a site-scoped Google dork: `site:pistonheads.com "handle"`.
3. Open the member's profile for join date, post count, last-active, and location field; then read their post history for cars owned, area, events, and named friends.
4. Check the Classifieds / Live Auctions for anything they're selling — listings expose vehicle details, photos (with plates/backgrounds), and sometimes a rough location or contact route.
5. Pivot: a plate seen in a photo feeds `[[vehicle-plate]]`-style lookups; named associates feed people-search; a location field narrows geolocation.

## Inputs → Outputs
- **In:** `username` (or a known vehicle/plate to search post text)
- **Out:** `social-profile` (forum profile + post history), corroborating `username`, `associate` links, and vehicle/location leads
- **Empty/negative result looks like:** no profile for the handle, or a profile with near-zero posts and no location — common, since many handles are unique-per-site; a miss here does not rule the person out elsewhere.

## Gotchas & OpSec
- Handles are not guaranteed to be the same person as on other platforms — corroborate (writing style, cars, timeframe) before linking identities.
- Logged-out browsing avoids leaving a footprint; registering or DMing exposes you and alerts the member.
- User-generated content: boasts about cars/locations may be aspirational, not factual.

## Overlaps ("do both")
- Pairs with cross-platform username enumeration to confirm the same handle exists elsewhere, and with vehicle/plate lookups for cars surfaced in posts or listings.

## Trust & verifiability
`trust: unverified` — a legitimate, well-established community, but the intelligence value is user-authored posts, which must be corroborated rather than taken at face value.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pistonheads-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, username, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
