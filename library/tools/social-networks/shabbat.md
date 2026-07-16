---
id: shabbat
name: Shabbat.com
description: Use when you have a `name` or `username` for someone in the Jewish community and want to find their member profile and location on this social network — returns social-profile, name and approximate geolocation.
url: http://www.shabbat.com
category: social-networks
path:
- social-networks
bestFor: Locating a person within the global Jewish community via a niche social network that ties members to a city.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: free
costNote: Free to join and use; funded as a community/non-profit network, no paywall for member search.
opsec: active
opsecNote: Member profiles and the host/traveler directory are visible only after you register and log in, so browsing is attributable to your account and other members may see that you viewed them. Register a sock-puppet profile rather than using a real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate long-running Jewish community network, but a niche third-party platform whose member data is self-reported.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Shabbat.com
- The Jewish Social Network
tags:
- toddington
- curated-directory
- social-media
- community
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Shabbat.com

> "The Jewish Social Network" — a free, worldwide community site where members list a home city and host/attend Shabbat and holiday meals, usable as a niche people-locator inside the Jewish community.

## When to use
You have a `name` or `username` for a subject with ties to the Jewish community and mainstream social networks come up empty. Because members register a city to find local hosts, meals, and community, a profile here can place a person geographically and confirm community affiliation — useful when a subject is active in observant/community circles but low-profile elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free sock-puppet account at shabbat.com (member directory and profiles are gated behind login).
2. Use the member / community search to look up the subject by name or username, or browse the host / "Shabbat meals" directory by city.
3. Open matching member profiles and read: display `name`/`username`, home city (`geolocation`), photo, and any community/organisation ties shown.
4. Pivot: a confirmed city + name narrows local record searches; a linked organisation feeds employer/community lookups; the photo feeds face-search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (member profile URL), `name`, approximate `geolocation` (registered city)
- **Empty/negative result looks like:** no member matches, or matches with common names you can't disambiguate — meaning the subject likely isn't a member, not that they aren't Jewish/community-affiliated.

## Gotchas & OpSec
- Human-in-the-loop: search and profiles require a logged-in account (free registration) — use a sock puppet.
- OpSec: **active** — this is a small community where members can see profile visits and requests; over-contacting or joining local groups can expose your interest, so observe, don't interact.
- Data is self-reported and the network is niche; treat a city/affiliation as a lead to corroborate, not a confirmed fact.

## Overlaps ("do both")
- Complements mainstream social-network people-search: run those first, and reach for Shabbat.com when a subject is community-embedded but absent from the big platforms.

## Trust & verifiability
`trust: unverified` — a legitimate, long-established community network, but third-party and built on self-reported member data, so corroborate any location or affiliation elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shabbat |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
