---
id: pivot-through-profile-links-friend-follower-lists-and-comments
name: Pivot through profile links, friend/follower lists, and comments
description: Use when Once you have at least one confirmed or strong-candidate profile and need to expand the network or find fresher activity.
type: technique
summary: 'Pivoting means using one discovered fact to reach the next. TOFM highlights three concrete pivot surfaces on social media: (1) linked accounts shown on a profile page, (2) friend/follower networks, and (3) mentions and tags inside comments. For missing-persons work this is the highest-yield move: a subject''s own profiles may be sparse, but the people around them (friends, who they comment with, who tags them) leak location, recent activity, and additional handles.'
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- social-profile
- username
- associate
pivotTo:
- social-profile
- associate
- username
- image
- geolocation
platforms:
- instagram
- facebook
- tiktok
- twitter
steps:
- Open the confirmed profile and harvest any linked/cross-posted accounts (link-in-bio, linktree, cross-platform handles).
- Walk the friend/follower list for accounts belonging to the subject or close associates.
- Read the comments on the subject's and associates' posts for mentions, tags, and replies that reveal new handles or whereabouts.
- Validate each new account against the source of truth before pivoting further.
signals:
- A friend's or associate's public post tags or references the subject with recent date/location info
pitfalls:
- Forgetting that you must not interact (no friend requests, likes, or comments) while doing this
- Trusting a tagged identity without validating it
tags:
- pivoting
- social-network
- associates
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: 'TOFM lists pivot sources: linked accounts on profile pages, friend/follower networks, and mentions in comments.'
trust: community
source: tofm
---

# Pivot through profile links, friend/follower lists, and comments

> Pivoting means using one discovered fact to reach the next. TOFM highlights three concrete pivot surfaces on social media: (1) linked accounts shown on a profile page, (2) friend/follower networks, and (3) mentions and tags inside comments. For missing-persons work this is the highest-yield move: a subject's own profiles may be sparse, but the people around them (friends, who they comment with, who tags them) leak location, recent activity, and additional handles.

**When to use:** Once you have at least one confirmed or strong-candidate profile and need to expand the network or find fresher activity.

## Steps
- Open the confirmed profile and harvest any linked/cross-posted accounts (link-in-bio, linktree, cross-platform handles).
- Walk the friend/follower list for accounts belonging to the subject or close associates.
- Read the comments on the subject's and associates' posts for mentions, tags, and replies that reveal new handles or whereabouts.
- Validate each new account against the source of truth before pivoting further.

## Signals it's working
- A friend's or associate's public post tags or references the subject with recent date/location info

## Pitfalls
- Forgetting that you must not interact (no friend requests, likes, or comments) while doing this
- Trusting a tagged identity without validating it

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
