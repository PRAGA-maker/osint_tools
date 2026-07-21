---
id: plentyoffish-online-dating
name: PlentyOfFish (POF)
description: Use when you have a `username`, `name` or photo and want to check for a POF dating profile — returns the linked `social-profile` and self-disclosed detail (age, area, photos).
url: https://www.pof.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Checking whether a subject has a Plenty of Fish dating profile and reading its public detail.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to join and browse; some messaging/visibility features are paid. Viewing profiles requires a (sock-puppet) account.
opsec: active
opsecNote: POF shows other users who viewed their profile and is a live social platform — browsing while logged in can alert the target and leaves a footprint. Always use a fully isolated sock-puppet account, disable "recent visitors" exposure where possible, and never use a real identity or photo.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A large, real dating platform (Match Group). Profiles are self-authored — ages, locations, and photos are unverified and often deliberately vague; treat as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- forums-plentyoffish-com
aliases:
- Plenty of Fish
- POF
- pof.com
tags:
- dating
source: metaosint
lastVerified: '2026-07-21'
enrichment: full
---

# PlentyOfFish (POF)

> One of the largest free dating platforms — searchable (once logged in) for a subject's dating profile, photos, and self-disclosed area and details.

## When to use
You suspect a subject is on a dating site and want to confirm a POF presence: to find current photos (for reverse-image/face work), a self-stated age and city/region, a username that may match other platforms, and lifestyle detail. Relevant in relationship investigations, locating someone who has gone quiet on other channels, and corroborating a person's current appearance and area.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a fully isolated sock-puppet account, log in to https://www.pof.com (browsing profiles requires an account).
2. Use POF's search/filters (username if known, else age + location + attributes) to find candidate profiles.
3. Compare photos (run them through reverse-image/face tools) and self-stated details against what you already know.
4. Note the username, stated area, age, and any linked handles or distinctive phrasing.
5. Pivot: the username feeds cross-platform handle tools (`[[sherlock]]`, `[[whatsmyname]]`); a photo feeds `[[pimeyes-com]]`; stated city narrows people-search.

## Inputs → Outputs
- **In:** `username` / `name` / `image` (photo to match)
- **Out:** `social-profile` (POF profile), photos, self-stated age/area
- **Empty/negative result looks like:** no matching profile — the person may not be on POF, may use a different handle/photos, or may have set the profile hidden. Absence is not proof.

## Gotchas & OpSec
- **Active** platform: profile views can be surfaced to the target and you must be logged in — isolate everything in a sock puppet, never a real identity/photo.
- Profile fields are self-authored and often intentionally vague or dated — treat age/location as claims to corroborate.
- Reverse-image on the profile photos is often more reliable than the text fields.

## Overlaps ("do both")
- Pairs with `[[pimeyes-com]]` (match the profile photo across the web) and `[[sherlock]]`/`[[whatsmyname]]` (confirm the username elsewhere) — POF gives current photos and area; those confirm identity and spread.

## Trust & verifiability
`trust: unverified` — a real platform but entirely self-reported profiles; use it to obtain current photos and leads, and verify identity via reverse-image and cross-platform correlation rather than trusting the profile text.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | plentyoffish-online-dating |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, image → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
