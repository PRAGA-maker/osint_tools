---
id: fotki
name: Fotki
description: Use when you have a `username` and want to find a long-running photo-sharing profile and its galleries — returns a `social-profile` and the subject's uploaded `image`s.
url: http://www.fotki.com
category: image-video-face
path:
- image-video-face
bestFor: Recovering a subject's personal photo galleries on a legacy photo-community when the handle is reused there.
selectorsIn:
- username
selectorsOut:
- image
- social-profile
status: live
pricing: freemium
costNote: Free to view public galleries and browse; uploading and some premium features require a (free or paid) account.
opsec: passive
opsecNote: Viewing public gallery URLs is passive and the subject isn't notified. Commenting/following ties activity to an account — use a sock puppet and browse read-only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established (since 1998) photo-sharing community; genuine user content, but an older/niche platform, so coverage is spotty and many accounts are dormant.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fotki.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- photo-sharing
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- fotki-image-search
- search-fotki-com
---

# Fotki

> A veteran (since 1998) photo-sharing community — worth checking during a username sweep because older subjects sometimes have long-lived galleries of personal photos here that survive nowhere else.

## When to use
You have a `username` and are hunting for a subject's photos, especially for an older or long-standing online persona. Fotki predates most modern platforms, so it can hold years of personal images (family, travel, events) with location and associate context that newer accounts don't. Treat it as one node in a broad username/photo search — a hit can be a goldmine, a miss is unremarkable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the profile URL pattern `http://public.fotki.com/<username>/` or search Fotki for the handle.
2. Open the public galleries; browse albums for personal `image`s, captions, dates, and tagged locations.
3. Note album titles, comments, and linked friends (potential `associate`s).
4. Download/reverse-image key photos to connect them to other platforms and confirm identity.
5. Pivot: reused handle → cross-platform username tools; faces/backgrounds in photos → facial-recognition and geolocation.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (Fotki page), the subject's uploaded `image`s, captions, and gallery context
- **Empty/negative result looks like:** no profile for the handle, or a dormant/empty account — expected given the platform's age; not proof the person shares no photos elsewhere.

## Gotchas & OpSec
- Aging, niche platform: most subjects won't be here; low base-rate but high value when present.
- Handle collisions happen; confirm identity via faces/context before attributing.
- Some galleries are private/friends-only and won't show publicly.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` and other username enumerators (they flag the Fotki hit) and with reverse-image tools (to link the photos outward).

## Trust & verifiability
`trust: community` — authentic user-uploaded content on a legacy platform; images are genuine, but confirm the account belongs to your subject before relying on what the galleries imply.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fotki |
| category | image-video-face |
| selectorsIn → selectorsOut | username → image, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
