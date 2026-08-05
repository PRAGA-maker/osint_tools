---
id: the-old-reader
name: The Old Reader
description: Use when you have a `domain`/blog or social feed and want to monitor its new posts over time — returns a chronological RSS/Atom feed reader for passive change-watching.
url: https://theoldreader.com
category: archives-cache
path:
- archives-cache
bestFor: Aggregating and monitoring RSS/Atom feeds (blogs, news, forums) to watch a subject's or site's output over time.
selectorsIn:
- domain
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier supports a limited number of subscriptions/folders; a low-cost Premium tier raises limits and adds features. Free account required to save feeds.
opsec: passive
opsecNote: Subscribing to a public RSS feed pulls content server-side via The Old Reader's infrastructure, so the target's site sees requests from the reader, not from you — a useful buffer. Your feed list is tied to your account, so use a sock-puppet registration for sensitive monitoring.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent RSS reader launched as a Google Reader replacement (2013); a stable, well-known service run by a small team, not a data vendor.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- theoldreader.com
tags:
- web-monitoring
- rss
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# The Old Reader

> A Google Reader-style RSS/Atom aggregator: subscribe to a target's blog, news source, or forum feed and passively collect every new post in one timeline.

## When to use
You have a `domain`, blog, subreddit, YouTube channel, or news site that publishes an RSS/Atom feed and you want to watch it for new activity without repeatedly visiting it. Good for long-running monitoring of a subject's public output, an organization's press page, or a topic across many sources — the reader pulls updates so you don't have to poll manually and leave a trail on the site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account at https://theoldreader.com (use a sock-puppet email for sensitive work).
2. Add subscriptions by pasting a site URL or its feed URL; group them into folders by case/topic.
3. Read the unified timeline — newest posts surface as they publish; mark/star items of interest.
4. Check back (or watch the unread count) to catch new posts over days/weeks.
5. Pivot: a new post links to a `social-profile`, event, or location to chase; export/OPML your feed list to share or back up.

## Inputs → Outputs
- **In:** `domain` / site or feed URL that exposes RSS/Atom
- **Out:** a chronological stream of that source's new posts; links onward to profiles/content
- **Empty/negative result looks like:** "no feed found" (the site publishes no RSS) or a feed that never updates — absence of RSS is common on modern sites; fall back to a change-detection tool that watches raw HTML.

## Gotchas & OpSec
- Human-in-the-loop: account-login required to save feeds; free-tier subscription limits apply.
- Coverage gap: only works where a site exposes a feed; many social platforms have dropped public RSS, so pair with HTML change-detection for those.
- OpSec: passive and buffered — the reader fetches the feed, insulating your IP from the target site; keep monitoring under a sock-puppet account.

## Overlaps ("do both")
- Pairs with HTML change-detection/monitoring tools: RSS readers catch feed-publishing sites cleanly, while change-detectors watch pages that have no feed — together they cover both.

## Trust & verifiability
`trust: community` — a stable, long-lived independent RSS service; it faithfully relays each source's own feed, so data fidelity tracks the origin site, and the tool itself just aggregates and timestamps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-old-reader |
