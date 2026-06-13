---
id: x-twitter
name: platform-x-twitter
description: Use when the subject is on X/Twitter — a largely public, real-time, text-heavy platform; full timeline search reveals location, routine, and opinions, with strong archive recovery for deleted posts.
type: technique
phase: pivot
pivotFrom: [username, social-profile, name]
pivotTo: [geolocation, name, associate, image, social-profile]
platforms: [x, twitter]
summary: X/Twitter is largely public and real-time, which makes it strong for last-known-activity and routine. The full public timeline is searchable (advanced operators filter by date, place, and keyword), tweets often carry place context, and replies/mentions expose the associate graph. Deleted tweets are unusually recoverable via archives. Recent API/access changes have degraded some third-party tooling, so expect more manual and login-gated work than a few years ago.
missingPersonsRelevance: high
whenToUse: You have an X/Twitter handle, or a name/handle that might be there.
steps:
  - Use advanced search operators — filter the timeline by from:user, since/until dates, and place/keyword to pull location and activity.
  - Read replies and mentions for the associate graph — who they talk to repeatedly is their network (`[[pivot-network-triangulation]]`).
  - Harvest location context — geotags (rare now), readable backgrounds in image tweets, and place mentions (`[[pivot-image-to-geolocation]]`).
  - Build last-known-activity from the timeline — X's real-time nature makes recency signals strong (`[[pattern-timeline-anchoring]]`).
  - Recover deleted tweets via archives — Wayback and tweet-archive tools often hold removed posts.
signals:
  - Recent tweets with place context give a current-location/last-active signal.
  - A consistent reply network corroborates the subject's identity and associates.
pitfalls:
  - Geotagging is mostly off by default now — rely on content/backgrounds over tweet geotags.
  - API changes have broken many third-party scrapers — expect manual, login-gated access.
  - Retweets/quotes aren't the subject's own content or location — separate original tweets.
toolsUsed: [twitter-advanced-search, wayback-machine, nitter-mirror]
evidence: []
trust: trusted
relatedStrategies: [username-reuse-enumeration, pivot-network-triangulation, pattern-timeline-anchoring, pivot-image-to-geolocation]
tags: [platform, x, twitter, real-time, text]
source: ""
---

# Platform: X / Twitter

## What's publicly enumerable
X/Twitter is **largely public and real-time**, which makes it one of the better platforms for **last-known-activity** and **routine**. The full timeline is searchable, tweets carry place and time context, and the **reply/mention graph** exposes who the subject actually interacts with. Deleted tweets are unusually recoverable through archives.

## The good pivots
- **Advanced search operators** — `from:user`, `since:`/`until:`, place and keyword filters slice the timeline for location and activity. This is the platform's signature technique.
- **Reply/mention network** — repeated conversation partners are the associate graph (`[[pivot-network-triangulation]]`).
- **Location from content** — explicit geotags are mostly gone, so lean on readable **backgrounds** in image tweets and **place mentions** (`[[pivot-image-to-geolocation]]`).
- **Timeline** — real-time posting makes recency signals strong (`[[pattern-timeline-anchoring]]`).
- **Deleted-tweet recovery** — Wayback and tweet archives.

## Gotchas
- **Geotagging mostly off by default** now — don't rely on tweet geotags; use content.
- **API/access changes** have broken many third-party scrapers and degraded mirrors; expect more **manual, login-gated** work than historically.
- **Retweets/quotes** aren't the subject's own content or location — isolate original tweets.

## OpSec
Mostly passive to read. Don't follow, reply, like, or quote from a traceable account; logged-in activity and follows are detectable. Use a sock puppet where login is required. `[[antipattern-contaminating-the-subject]]`, `[[phase-opsec]]`.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| platform | x / twitter |
| MP relevance | high |
| tools | twitter-advanced-search, wayback-machine, nitter-mirror |
