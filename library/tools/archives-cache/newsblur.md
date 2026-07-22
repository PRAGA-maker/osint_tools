---
id: newsblur
name: NewsBlur
description: Use when you want to monitor news sites, blogs and RSS feeds about a subject in one filtered stream — an open-source feed reader with training/hide filters — returns new posts.
url: http://newsblur.com
category: archives-cache
path:
- archives-cache
bestFor: Building a filtered RSS/news monitoring dashboard with per-feed "training" to surface only relevant stories.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier caps the number of sites (currently ~64) and lacks some features; a low-cost Premium tier lifts limits. It is open source and can be self-hosted for free.
opsec: passive
opsecNote: Aggregating public feeds is passive — you read published content and the subject sees nothing. Your subscriptions live in a NewsBlur account, so use a dedicated investigative login (or self-host).
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running open-source feed reader (Samuel Clay); it relays publishers' own feeds, so content authority is the underlying source's.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
relatedTools:
- newsblur-rss-feeder
- feedly
aliases:
- NewsBlur
tags:
- web-monitoring
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# NewsBlur

> An open-source RSS/news reader with per-feed "training" and intelligence filters — a monitoring dashboard that learns to surface stories about your subject and hide the noise.

## When to use
You need ongoing awareness of coverage about a person, org or topic and want more control than a plain reader: NewsBlur lets you "train" each feed (thumbs-up/down tags, keywords, authors) so relevant items float to a Focus view. Good when a subject's name appears in high-volume feeds and you only want the matching stories.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a (dedicated) account at https://newsblur.com — or self-host the open-source stack — and log in.
2. Add sites/RSS feeds relevant to the case; organise them into folders.
3. Train feeds: tag keywords, authors or tags as liked/disliked so the "Focus" filter shows only matching stories.
4. Monitor the river of new posts; use the story-change and shared "Blurblog" features to track updates.
5. Pivot: entities, dates and links in surfaced stories feed name/domain/geolocation searches; use the API for programmatic pulls.

## Inputs → Outputs
- **In:** RSS/news feed URLs + training rules (monitoring setup, not a target selector)
- **Out:** a filtered, chronological stream of new posts from your sources
- **Empty/negative result looks like:** an over-aggressive hide filter can bury relevant items — loosen training if the Focus view goes empty; a quiet feed genuinely means no new coverage.

## Gotchas & OpSec
- Human-in-the-loop: account required; the free tier caps site count and some features.
- Like any RSS reader, it only covers sources that expose feeds — pages without RSS need a change-monitor instead.
- OpSec: passive reading of public content; keep the account separate from your identity, or self-host.

## Overlaps ("do both")
- Pairs with `[[feedly]]` and dedicated web-change monitors — NewsBlur's edge is granular per-feed training/filtering; change-detection tools cover feedless pages it can't.

## Trust & verifiability
`trust: trusted` as a reader — it faithfully relays publisher feeds; the credibility of any story is that of its original source, which you still assess.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | newsblur |
