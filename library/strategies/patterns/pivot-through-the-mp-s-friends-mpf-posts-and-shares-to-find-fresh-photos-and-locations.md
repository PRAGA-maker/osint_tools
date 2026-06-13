---
id: pivot-through-the-mp-s-friends-mpf-posts-and-shares-to-find-fresh-photos-and-locations
name: Pivot through the MP's friends' (MPF) posts and shares to find fresh photos and locations
description: Use when When the MP's own account is sparse, or to find recent media the MP appears in; whenever a shared post on the MP profile traces back to a friend.
type: pattern
summary: 'Some of the most valuable evidence about an MP lives not on the MP''s own account but on their friends'' accounts. In the documented case, the MP''s most useful recent content was originally posted by a missing-person''s-friend (MPF) and then shared onto the MP''s profile, and the two key geolocatable media (a video and a photoshoot image) both originated on the MPF account. Treat friends''/associates'' public posts as a primary content source: they tag, photograph, and locate the MP even when the MP posts little themselves.'
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- associate
- social-profile
pivotTo:
- image
- geolocation
- social-profile
platforms:
- facebook
- instagram
steps:
- For each shared post on the MP profile, identify and visit the original poster's account.
- Enumerate friends'/associates' public posts for photos, videos, and tags of the MP.
- 'Note origination dates: a friend''s post can predate the MP''s share and add timeline context.'
- Extract any geolocatable media (signage, structures, backgrounds) from friend-originated content.
- Cross-link MPF content back to the MP timeline to reconstruct movement and recency.
signals:
- Shared posts on the MP profile trace back to a friend's original post
- Friend accounts contain photos/videos of the MP with usable backgrounds
- Friend-originated media carries geolocation clues the MP's own posts lack
pitfalls:
- Confusing the friend's location/identity with the MP's
- Over-relying on share dates instead of original post dates for timeline
toolsUsed:
- Facebook
tags:
- associate-pivot
- friends-of-target
- shared-posts
- social-media-first
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Both the geolocated video and the photoshoot image were 'originally posted via the MPF FB account' and later shared by the MP.
trust: community
source: osinti4l-mvo-writeup
---

# Pivot through the MP's friends' (MPF) posts and shares to find fresh photos and locations

> Some of the most valuable evidence about an MP lives not on the MP's own account but on their friends' accounts. In the documented case, the MP's most useful recent content was originally posted by a missing-person's-friend (MPF) and then shared onto the MP's profile, and the two key geolocatable media (a video and a photoshoot image) both originated on the MPF account. Treat friends'/associates' public posts as a primary content source: they tag, photograph, and locate the MP even when the MP posts little themselves.

**When to use:** When the MP's own account is sparse, or to find recent media the MP appears in; whenever a shared post on the MP profile traces back to a friend.

## Steps
- For each shared post on the MP profile, identify and visit the original poster's account.
- Enumerate friends'/associates' public posts for photos, videos, and tags of the MP.
- Note origination dates: a friend's post can predate the MP's share and add timeline context.
- Extract any geolocatable media (signage, structures, backgrounds) from friend-originated content.
- Cross-link MPF content back to the MP timeline to reconstruct movement and recency.

## Signals it's working
- Shared posts on the MP profile trace back to a friend's original post
- Friend accounts contain photos/videos of the MP with usable backgrounds
- Friend-originated media carries geolocation clues the MP's own posts lack

## Pitfalls
- Confusing the friend's location/identity with the MP's
- Over-relying on share dates instead of original post dates for timeline

**Tools:** Facebook

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
