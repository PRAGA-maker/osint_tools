---
id: facebook-first-canvass-for-missing-persons
name: Facebook-first canvass for missing persons
description: Use when As the primary platform once you have a candidate profile, before spreading to secondary networks.
type: pattern
summary: Across many writeups, Facebook is repeatedly called 'a goldmine' and the single highest-yield platform for missing-persons OSINT, with other platforms (Twitter, Instagram, Snapchat, TikTok, Strava) acting as support. Investigators extract usernames, location data, images and videos, event attendance, group membership, and comment/reaction patterns. Recent posts and the friends list (especially Facebook's 'Recently Added', which exposes roughly a 3-week window) are the richest pivot surfaces because they reveal current associates and recent geolocation.
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- name
- username
- image
pivotTo:
- associate
- geolocation
- username
- employer-org
- image
- social-profile
platforms:
- facebook
steps:
- Locate the subject's Facebook profile by name/handle and confirm via face comparison.
- Read the visible timeline for recent posts and life events.
- Walk the friends list, prioritizing 'Recently Added' for current associates.
- Open tagged photos and check-ins for location and lifestyle data.
- Note groups joined and events attended as community/interest pivots.
- Identify recurring commenters/reactors as close relationships to investigate next.
signals:
- A post dated shortly before or after the disappearance
- Recurring commenters who are clearly close family/friends
- Tagged location data on recent photos
pitfalls:
- Treating Twitter/Instagram as primary when Facebook usually carries most points
- Missing the 'Recently Added' friends window that reveals current contacts
tags:
- facebook
- network-analysis
- platform-priority
- pivot
evidence:
- type: writeup
  url: https://shandyman.online/blog/on-a-mission-a-tracelabs-ctf-missing-persons-writeup/
  note: Facebook is a goldmine; majority of points came through Facebook with other platforms picking up the slack
- type: writeup
  url: https://www.aaroncti.com/trace-labs-august-2020/
  note: Extract usernames, location, images, events, groups, comment patterns from Facebook
- type: writeup
  url: https://jack.bio/blog/tracelabs
  note: Facebook 'Recently Added' friends exposes ~3-week window of current associates
trust: community
source: searchparty-writeups
---

# Facebook-first canvass for missing persons

> Across many writeups, Facebook is repeatedly called 'a goldmine' and the single highest-yield platform for missing-persons OSINT, with other platforms (Twitter, Instagram, Snapchat, TikTok, Strava) acting as support. Investigators extract usernames, location data, images and videos, event attendance, group membership, and comment/reaction patterns. Recent posts and the friends list (especially Facebook's 'Recently Added', which exposes roughly a 3-week window) are the richest pivot surfaces because they reveal current associates and recent geolocation.

**When to use:** As the primary platform once you have a candidate profile, before spreading to secondary networks.

## Steps
- Locate the subject's Facebook profile by name/handle and confirm via face comparison.
- Read the visible timeline for recent posts and life events.
- Walk the friends list, prioritizing 'Recently Added' for current associates.
- Open tagged photos and check-ins for location and lifestyle data.
- Note groups joined and events attended as community/interest pivots.
- Identify recurring commenters/reactors as close relationships to investigate next.

## Signals it's working
- A post dated shortly before or after the disappearance
- Recurring commenters who are clearly close family/friends
- Tagged location data on recent photos

## Pitfalls
- Treating Twitter/Instagram as primary when Facebook usually carries most points
- Missing the 'Recently Added' friends window that reveals current contacts

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
