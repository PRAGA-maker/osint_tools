---
id: behance
name: Behance
url: https://www.behance.net
category: social-networks
path:
- social-networks
description: Use when you have a `name` or `username` of a creative professional and want their portfolio profile — returns a `social-profile` with work, location, employer and linked accounts.
bestFor: Finding a designer/artist/photographer's portfolio profile and the identity details creatives publish alongside their work.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
- geolocation
- name
status: live
pricing: free
costNote: Free to browse and search profiles and projects; an Adobe account is only needed to appreciate/comment/follow, not to view.
opsec: passive
opsecNote: Browsing public profiles is passive and anonymous while logged out. Following, appreciating or messaging requires an Adobe login and is visible to the target — stay logged out (or use a sock puppet) for read-only work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Owned and operated by Adobe; profiles are self-published by the creatives themselves, so identity claims are self-asserted but the platform itself is authentic.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- behance.net
- Adobe Behance
tags:
- toddington
- curated-directory
- social-media
- portfolio
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Behance

> Adobe's portfolio network for creatives — a rich source of self-published identity, location and employer detail for designers, illustrators, photographers and other visual professionals.

## When to use
You have a `name` or `username` for someone in a creative field and want their portfolio profile. Creatives on Behance tend to publish a real name, city/country, current employer or freelance status, linked social accounts, and a body of dated work — a lot of pivotable identity for one lookup. Especially useful when a handle turns up nowhere on mainstream networks but the person is a working creative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.behance.net (stay logged out for passive work).
2. Search the `name` or `username` in the top search, or try `behance.net/<username>` directly.
3. Open the profile: read the About/location, employer/"On the job" field, linked social/website links, and project captions.
4. Inspect project images for EXIF/location clues and cross-post links to other platforms.
5. Pivot: linked website/social accounts feed username enumeration; a stated employer feeds `[[northdata-com]]`/LinkedIn; project locations feed geolocation.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile`, `employer-org`, `geolocation` (city/country), linked accounts, real `name`
- **Empty/negative result looks like:** no matching profile, or a stub with no projects/links — the person may not be a Behance creative, or uses a different handle here. Absence is not disproof of identity.

## Gotchas & OpSec
- Profile detail is self-asserted; treat employer/location as claims to corroborate.
- OpSec: viewing is anonymous when logged out; any appreciate/follow/comment/DM requires an Adobe login and notifies the target. Keep it read-only.
- The same person may use a different handle here than elsewhere — search by real name too.

## Overlaps ("do both")
- Pairs with `[[username-search-tool]]` and `[[deepfind-me]]` to check whether the Behance handle is reused elsewhere, and with reverse-image search on the avatar/project images.

## Trust & verifiability
`trust: trusted` — Behance is a genuine Adobe-operated platform, so profiles are real accounts; the caveat is only that biographical fields are self-published and should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | behance |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org, geolocation, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
