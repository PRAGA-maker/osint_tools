---
id: friend-and-tag-enumeration-to-find-a-low-footprint-subject
name: Friend-and-tag enumeration to find a low-footprint subject
description: Use when When the subject's own profile is private, deleted, inactive, or non-existent but they are young/socially active.
type: playbook
summary: When the subject (often a runaway teen) has a locked, sparse, or absent profile, you find them through their social graph rather than directly. Start from one confirmed account, follow links to spam/backup accounts, scan the friends/follower list for similar names and shared faces, locate the best friend's account, and harvest cross-tagged images and co-appearances. Teens commonly run 4+ accounts on a single platform under name variations, and their location/lifestyle leaks through friends who tag them. This indirect graph pivot is the canonical way solved cases are cracked when the subject th
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- username
- social-profile
- associate
pivotTo:
- associate
- image
- geolocation
- social-profile
- physical-description
platforms:
- instagram
- snapchat
- tiktok
- facebook
steps:
- Find any one confirmed account belonging to the subject.
- Follow the bio/linktree to spam, finsta, or backup accounts (people reuse handle variants).
- Scan the friends/follower list for similar names and recurring faces.
- Identify the best friend(s) and pivot into their public account.
- Harvest photos where the subject is tagged or appears, even if their own account is locked.
- Read comments and tagged check-ins on friends' posts for location and recent activity.
- Note physical descriptors (tattoos, piercings, hair) and lifestyle signals visible in friends' photos.
signals:
- Subject appears in a friend's recent tagged photo
- A backup/finsta account surfaces from a linktree or bio
- Several accounts share the same best-friend follower set
pitfalls:
- Giving up when the subject's main profile is private instead of going through friends
- Assuming one account is the only account when teens run several
- Ignoring photos because they are on someone else's profile
tags:
- instagram
- snapchat
- teens
- runaway
- graph-pivot
- tagged-photos
evidence:
- type: writeup
  url: https://medium.com/@cyberbychase/osint-methodology-and-tradecraft-tips-for-winning-the-trace-labs-black-badge-from-team-federal-ebe737d70c6a
  note: 'Rae''s Instagram enumeration: backup accounts, friends-of-friends, best friend cross-tagged images, 4+ accounts per platform'
- type: writeup
  url: https://wondersmithrae.medium.com/finding-missing-people-with-tracelabs-ctf-d5617c7cd659
  note: Learning to pivot is key; when the subject has zero social media, branch through related contacts (family -> email -> location)
trust: community
source: searchparty-writeups
---

# Friend-and-tag enumeration to find a low-footprint subject

> When the subject (often a runaway teen) has a locked, sparse, or absent profile, you find them through their social graph rather than directly. Start from one confirmed account, follow links to spam/backup accounts, scan the friends/follower list for similar names and shared faces, locate the best friend's account, and harvest cross-tagged images and co-appearances. Teens commonly run 4+ accounts on a single platform under name variations, and their location/lifestyle leaks through friends who tag them. This indirect graph pivot is the canonical way solved cases are cracked when the subject th

**When to use:** When the subject's own profile is private, deleted, inactive, or non-existent but they are young/socially active.

## Steps
- Find any one confirmed account belonging to the subject.
- Follow the bio/linktree to spam, finsta, or backup accounts (people reuse handle variants).
- Scan the friends/follower list for similar names and recurring faces.
- Identify the best friend(s) and pivot into their public account.
- Harvest photos where the subject is tagged or appears, even if their own account is locked.
- Read comments and tagged check-ins on friends' posts for location and recent activity.
- Note physical descriptors (tattoos, piercings, hair) and lifestyle signals visible in friends' photos.

## Signals it's working
- Subject appears in a friend's recent tagged photo
- A backup/finsta account surfaces from a linktree or bio
- Several accounts share the same best-friend follower set

## Pitfalls
- Giving up when the subject's main profile is private instead of going through friends
- Assuming one account is the only account when teens run several
- Ignoring photos because they are on someone else's profile

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
