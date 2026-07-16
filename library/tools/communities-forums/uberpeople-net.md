---
id: uberpeople-net
name: uberpeople.net
description: Use when you have a `username` or a rideshare-driver subject and want their forum posts — returns a `social-profile` with location hints, activity and `associate` connections.
url: https://uberpeople.net/
category: communities-forums
path:
- communities-forums
bestFor: Searching the largest independent Uber/Lyft rideshare-driver forum for a subject's posts, location, and community ties.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
- geolocation
- associate
status: live
pricing: free
costNote: Free to read and search publicly; registration (free) only needed to post.
opsec: passive
opsecNote: Reading and searching public threads is passive and needs no login — nothing reaches the subject. If you register to see gated boards, use a sock-puppet account; posting or messaging would be active.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A large community forum (XenForo); posts are self-reported and pseudonymous, so treat identity and claims as leads to corroborate.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UberPeople
- uberpeople.net
tags:
- forums
- rideshare
- Forums
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# uberpeople.net

> The busiest independent rideshare-driver forum — if your subject drives for Uber/Lyft, their posts here often leak city, schedule, vehicle, and grievances they'd never put on mainstream social.

## When to use
Your subject is (or claims to be) a rideshare/delivery driver, and you have a `username`, `name`, or handle to chase. Forum regulars post in city-specific subforums and casually reveal their operating area (`geolocation`), vehicle, working hours, and disputes — plus a reusable `username` and community `associate` ties. Useful for placing a gig-economy subject geographically and cross-linking a handle to other platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://uberpeople.net/ (no login needed to read).
2. Search the `username`/handle in the forum search; also try a Google site search: `site:uberpeople.net "<handle>"`.
3. Review the member's post history and which **city subforum** they post in — that's a strong location signal.
4. Read posts for vehicle, schedule, employer complaints, and named contacts (`associate`).
5. Pivot: reuse the `username` across platforms (username-enumeration tools); take the city/vehicle into local records and mapping.

## Inputs → Outputs
- **In:** `username`/handle or `name`
- **Out:** `social-profile` (forum member page + post history), reused `username`, city/`geolocation` hints, community `associate`
- **Empty/negative result looks like:** no member/posts for the handle — the subject isn't active here or uses a different name; a generic handle may also collide with unrelated members (verify by content/city).

## Gotchas & OpSec
- Pseudonymous by design — a handle here may not match the same handle elsewhere; confirm via posted details, not the name alone.
- Self-reported: drivers vent and exaggerate; treat location/vehicle claims as leads.
- Some boards may require a free login; if so, use a sock puppet and only read.

## Overlaps ("do both")
- Pairs with username-enumeration tools (to reuse the handle) and with other gig/occupation forums — a driver active here is often on Reddit's rideshare subs and Facebook driver groups too.

## Trust & verifiability
`trust: unverified` — a real, active forum of self-reported, pseudonymous posts; corroborate any location or identity claim against a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uberpeople-net |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username, geolocation, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
