---
id: skype-search-engine
name: Skypli (Skype Search Engine)
description: Use when you have a `username`, `email` or `name` and want to find a Skype account's profile, avatar and location — now largely historical after Skype's 2025 retirement — returns social-profile, image and geolocation.
url: https://www.skypli.com/
category: social-networks
path:
- social-networks
bestFor: Resolving a Skype username/email/name to a Skype profile (display name, avatar, country) — chiefly a historical/legacy lookup after Skype shut down.
selectorsIn:
- username
- email
- name
selectorsOut:
- social-profile
- image
- geolocation
status: degraded
pricing: freemium
costNote: Basic lookups are free; some sites in this space gate bulk/extra results behind payment. The bigger limiter is that Skype itself was retired, so live directory data is no longer refreshed.
opsec: passive
opsecNote: Querying a Skype search engine does not message or add the target — passive. With Skype retired, treat any result as historical; do not attempt to add/contact a legacy account, which is both unlikely to work and potentially alerting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party Skype directory scraper; historically effective, but Microsoft retired Skype in May 2025, so its data is now legacy and increasingly stale.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Skypli
- Skype resolver
- Skype search engine
tags:
- skype
- legacy
- account-search
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Skypli (Skype Search Engine)

> A Skype account lookup — resolve a username, email or name to a Skype profile (display name, avatar, country). Now mostly a historical tool, since Microsoft retired Skype in May 2025.

## When to use
You have a legacy Skype identifier (a Skype `username`/Live ID, an `email` once tied to Skype, or a `name`) and want to recover the associated profile: display name, avatar (`image`), and the country/region Skype exposed (`geolocation`). This is valuable for *historical* identity work — linking an old Skype handle to a real person, an avatar for reverse-image search, or a country hint — but understand the platform itself is gone, so data is frozen and cannot be refreshed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.skypli.com/ and search by Skype `username`/Live ID, `email`, or `name`.
2. Read the returned profile: Skype display name, handle, avatar, and country/region.
3. Save the avatar for reverse-image search and note the country as a location hint.
4. Treat everything as historical — verify against other sources rather than assuming it's current.
5. Pivot: the avatar feeds reverse-image/face tools; the linked email/username feeds cross-platform enumeration; the country narrows geolocation.

## Inputs → Outputs
- **In:** Skype `username`/Live ID, `email`, or `name`
- **Out:** `social-profile` (Skype display name/handle), `image` (avatar), `geolocation` (country/region)
- **Empty/negative result looks like:** no match or a stale/blank profile — expected now, since Skype's live directory is retired; absence is not proof the person never had Skype.

## Gotchas & OpSec
- **Skype is retired (May 2025):** data is legacy; do not rely on it as current, and don't try to contact/add accounts.
- These resolver sites come and go and vary in freshness; corroborate any hit.
- OpSec: passive; never message a legacy account.

## Overlaps ("do both")
- Pairs with reverse-image search and username-enumeration tools — a recovered Skype avatar/handle is most useful as a bridge to a person's other, still-live accounts.

## Trust & verifiability
`trust: community` — a historically useful third-party resolver, now serving legacy data after Skype's shutdown; confirm any identity via the avatar and cross-platform links rather than the Skype record alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skype-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | username, email, name → social-profile, image, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
