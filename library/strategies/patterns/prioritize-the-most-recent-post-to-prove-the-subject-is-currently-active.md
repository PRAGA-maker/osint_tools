---
id: prioritize-the-most-recent-post-to-prove-the-subject-is-currently-active
name: Prioritize the most recent post to prove the subject is currently active
description: Use when Immediately after verifying a profile, when timeline activity could establish that the subject is alive/active.
type: pattern
summary: 'The team flagged a post shared by the MP less than 24 hours before the CTF started as a critical finding, because recency is itself intelligence: it proves the account is live and the subject (or someone with access) is currently active. In missing-persons work, demonstrating recent activity on a verified profile is high-value both for narrowing a search window and for the report. The most recent media is therefore worth analyzing first, even if the image''s content (e.g., an interior bedroom shot) ultimately yields no geolocation, because confirming live activity still moves the case forward.'
missingPersonsRelevance: high
phase: triage
pivotFrom:
- social-profile
pivotTo:
- metadata-exif
- geolocation
platforms:
- facebook
- instagram
- tiktok
steps:
- Sort the verified profile's posts by recency.
- Examine the newest post for an activity timestamp relative to your case window.
- Log recency as a finding even if the post has no geolocatable content.
- Then analyze the post content for location clues as a separate step.
signals:
- A post timestamp falls inside or near your active case window
- Engagement (comments/tags) from associates appears on the recent post
pitfalls:
- Discarding a recent post because its image has no location clues - the timestamp itself is the finding
- Confusing post-shared time with capture time
toolsUsed:
- Facebook
tags:
- recency
- timeline
- proof-of-life
- triage
- tracelabs
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Post shared <24h before CTF flagged as critical proof of active digital presence
trust: community
source: osinti4l-user
---

# Prioritize the most recent post to prove the subject is currently active

> The team flagged a post shared by the MP less than 24 hours before the CTF started as a critical finding, because recency is itself intelligence: it proves the account is live and the subject (or someone with access) is currently active. In missing-persons work, demonstrating recent activity on a verified profile is high-value both for narrowing a search window and for the report. The most recent media is therefore worth analyzing first, even if the image's content (e.g., an interior bedroom shot) ultimately yields no geolocation, because confirming live activity still moves the case forward.

**When to use:** Immediately after verifying a profile, when timeline activity could establish that the subject is alive/active.

## Steps
- Sort the verified profile's posts by recency.
- Examine the newest post for an activity timestamp relative to your case window.
- Log recency as a finding even if the post has no geolocatable content.
- Then analyze the post content for location clues as a separate step.

## Signals it's working
- A post timestamp falls inside or near your active case window
- Engagement (comments/tags) from associates appears on the recent post

## Pitfalls
- Discarding a recent post because its image has no location clues - the timestamp itself is the finding
- Confusing post-shared time with capture time

**Tools:** Facebook

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
