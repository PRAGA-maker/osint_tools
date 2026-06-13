---
id: check-most-recent-post-timestamp-to-confirm-the-mp-is-digitally-active-and-on-which-platform
name: Check most-recent post timestamp to confirm the MP is digitally active and on which platform
description: Use when Immediately after confirming a profile belongs to the MP, while triaging which accounts deserve deep enumeration.
type: technique
summary: 'Once a confirmed MP profile is found, look at the timestamp of the most recent post or activity. A post within the last 24 hours tells you two high-value facts: the person is currently digitally active (so live leads exist) and this specific platform is one they actually use to post. This shapes where you spend the rest of your time, biasing effort toward the platforms with fresh activity rather than dormant accounts.'
missingPersonsRelevance: high
phase: triage
pivotFrom:
- social-profile
pivotTo:
- social-profile
- metadata-exif
platforms:
- facebook
- instagram
- tiktok
steps:
- Open the confirmed MP profile's post / activity history.
- Note the timestamp of the most recent post or share.
- Classify the account as active (recent activity) vs dormant.
- Prioritize deep enumeration on the platform showing the freshest activity.
signals:
- A post dated within ~24 hours of the investigation indicates a live, active subject
- Fresh activity concentrated on one platform points you to where the MP communicates
pitfalls:
- Shares can resurface old content; check whether the original post (not just the share) is recent
- A dormant account is not proof of inactivity elsewhere; the MP may have moved platforms
toolsUsed:
- Facebook
tags:
- recency
- triage
- activity-signal
- social-media
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: '''a shared post... dated less than 24 hours prior... allowed us to conclude that the MP was 1. Digitally active, and 2. Was active on this specific platform.'''
trust: community
source: osinti4l-mvo-writeup
---

# Check most-recent post timestamp to confirm the MP is digitally active and on which platform

> Once a confirmed MP profile is found, look at the timestamp of the most recent post or activity. A post within the last 24 hours tells you two high-value facts: the person is currently digitally active (so live leads exist) and this specific platform is one they actually use to post. This shapes where you spend the rest of your time, biasing effort toward the platforms with fresh activity rather than dormant accounts.

**When to use:** Immediately after confirming a profile belongs to the MP, while triaging which accounts deserve deep enumeration.

## Steps
- Open the confirmed MP profile's post / activity history.
- Note the timestamp of the most recent post or share.
- Classify the account as active (recent activity) vs dormant.
- Prioritize deep enumeration on the platform showing the freshest activity.

## Signals it's working
- A post dated within ~24 hours of the investigation indicates a live, active subject
- Fresh activity concentrated on one platform points you to where the MP communicates

## Pitfalls
- Shares can resurface old content; check whether the original post (not just the share) is recent
- A dormant account is not proof of inactivity elsewhere; the MP may have moved platforms

**Tools:** Facebook

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
