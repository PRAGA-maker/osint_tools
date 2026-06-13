---
id: enumerate-a-known-handle-across-many-platforms
name: Enumerate a known handle across many platforms
description: Use when As soon as you have a candidate handle, especially a distinctive one the person reuses.
type: technique
summary: When you know the subject's preferred online handle/username, enumerate it across as many sites as possible to map their digital footprint. A single reused username often unlocks profiles on platforms the person never publicly linked, each of which can carry fresh photos, location hints, and an associate network. TOFM names whatsmyname.app as the go-to enumeration tool.
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- username
pivotTo:
- social-profile
- username
- image
- associate
platforms:
- instagram
- tiktok
- twitter
- reddit
- facebook
steps:
- Take the known handle.
- Run it through whatsmyname.app to surface accounts on hundreds of sites.
- Open each hit and capture profile photos, bios, linked accounts, and follower circles.
- Feed any new handles/links discovered back into enumeration (iterate).
signals:
- The same handle appears on multiple platforms with consistent photos or bios
pitfalls:
- Assuming every hit belongs to your subject — a username can be shared by unrelated people
- Stopping after one platform instead of mapping the full footprint
toolsUsed:
- whatsmyname.app
tags:
- enumeration
- username-pivot
- footprint
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: 'TOFM: ''If you know a person''s preferred online handle, you will want to enumerate that handle across as many sites as possible.'''
trust: community
source: tofm
---

# Enumerate a known handle across many platforms

> When you know the subject's preferred online handle/username, enumerate it across as many sites as possible to map their digital footprint. A single reused username often unlocks profiles on platforms the person never publicly linked, each of which can carry fresh photos, location hints, and an associate network. TOFM names whatsmyname.app as the go-to enumeration tool.

**When to use:** As soon as you have a candidate handle, especially a distinctive one the person reuses.

## Steps
- Take the known handle.
- Run it through whatsmyname.app to surface accounts on hundreds of sites.
- Open each hit and capture profile photos, bios, linked accounts, and follower circles.
- Feed any new handles/links discovered back into enumeration (iterate).

## Signals it's working
- The same handle appears on multiple platforms with consistent photos or bios

## Pitfalls
- Assuming every hit belongs to your subject — a username can be shared by unrelated people
- Stopping after one platform instead of mapping the full footprint

**Tools:** whatsmyname.app

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
