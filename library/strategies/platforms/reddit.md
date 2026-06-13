---
id: reddit
name: platform-reddit
description: Use when the subject has a Reddit handle — pseudonymous but extremely leaky; full public post history reveals location, interests, routine, and self-disclosed personal facts.
type: technique
phase: pivot
pivotFrom: [username, social-profile]
pivotTo: [geolocation, name, social-profile, associate, image]
platforms: [reddit]
summary: Reddit feels anonymous but is one of the leakiest platforms, because a user's ENTIRE public comment and post history is browsable in one place. People disclose their city (local subreddits), job, age, relationships, and routine across years of comments without realizing the aggregate. The whole history is the pivot: read it for self-disclosed location and personal facts, and check whether the handle is reused elsewhere. Pushshift-style archives recover deleted comments.
missingPersonsRelevance: high
whenToUse: You have a Reddit username, or a handle that might be reused on Reddit.
steps:
  - Pull the full public history — read across all comments/posts, not just recent ones; the aggregate is where people leak.
  - Mine local-subreddit activity for location — posting in r/<city> or about local events/businesses self-discloses geography.
  - Harvest self-disclosed facts — age, job, relationships, vehicles, schedule mentioned offhand across years.
  - Check handle reuse off-Reddit — Reddit handles are often reused; enumerate elsewhere (`[[username-reuse-enumeration]]`).
  - Recover deleted content via archives — Pushshift-style tools surface comments the user later removed.
signals:
  - Repeated posting in a city/region subreddit converges on a location.
  - Self-disclosed facts across different threads independently corroborate each other.
pitfalls:
  - People discuss places they don't live (travel, hometown nostalgia) — distinguish "lives in" from "talks about".
  - Throwaway accounts are deliberately disconnected — don't assume a throwaway links to the main identity.
  - Old self-disclosures may be stale (a job/city from years ago) — date them against the timeline.
toolsUsed: [redective, reddit-search, pushshift-archive]
evidence: []
trust: trusted
relatedStrategies: [username-reuse-enumeration, pivot-image-to-geolocation, pattern-timeline-anchoring, pattern-selector-discipline]
tags: [platform, reddit, pseudonymous, text, high-yield]
source: ""
---

# Platform: Reddit

## What's publicly enumerable
Reddit *feels* anonymous and is the opposite of it in practice, because a user's **entire public history** — every comment and post, going back years — is browsable from one page. People treat each thread as ephemeral and disclose, piecemeal, their city, job, age, relationships, vehicle, and daily routine. None of it feels revealing in isolation; the **aggregate** is a detailed profile. That aggregation is the platform's defining pivot.

## The good pivots
- **Full-history read** — the single most valuable move. Read across the whole comment history, not just recent posts; the leak is cumulative.
- **Local-subreddit geolocation** — posting in `r/<city>`, asking about local businesses, or commenting on regional events self-discloses location more reliably than almost anything else.
- **Self-disclosed facts** — age, employer, relationships, schedule, dropped offhand. Each is a selector (`[[pattern-selector-discipline]]`).
- **Handle reuse** — Reddit handles are frequently reused; enumerate the handle off-platform (`[[username-reuse-enumeration]]`).
- **Deleted-content recovery** — Pushshift-style archives surface removed comments.

## Gotchas
- **"Talks about" ≠ "lives in"** — people post about travel and hometowns; separate residence from mention.
- **Throwaways** are deliberately disconnected; don't assume a throwaway links to a main identity without evidence.
- **Staleness** — a job or city mentioned years ago may be outdated; date disclosures against the timeline (`[[pattern-timeline-anchoring]]`).

## OpSec
Reading public history is fully passive — Reddit doesn't notify on profile views. The lines are the usual ones: don't comment, message, or post to the subject or relevant subs from any traceable account. Engagement is `[[antipattern-contaminating-the-subject]]`.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| platform | reddit |
| MP relevance | high |
| tools | redective, reddit-search, pushshift-archive |
