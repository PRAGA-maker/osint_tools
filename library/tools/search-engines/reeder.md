---
id: reeder
name: Reeder
description: Use when you have a set of `domain`/feed sources on a subject and want to monitor them continuously — returns a unified timeline of new posts, videos, and podcasts.
url: https://reederapp.com
category: search-engines
path:
- search-engines
bestFor: Continuously monitoring RSS/Atom feeds, YouTube channels, podcasts, and social sources tied to a subject in one timeline.
selectorsIn:
- domain
- social-profile
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: The current Reeder (rebuilt, iOS 17+/macOS 14+) is free to download and use with iCloud sync; an optional subscription adds premium sync/features. Legacy "Reeder Classic" is a one-time paid app.
opsec: passive
opsecNote: Reeder fetches public feeds directly from the source servers, so subscribing to a subject's feed sends requests from your device/IP to their host — recurring, low-volume, and indistinguishable from any RSS reader, but not zero-footprint. For sensitive monitoring, front it with a feed proxy. It does not require logging into the monitored platforms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Long-established (15+ years) independent reader app by Silvio Rizzi; reputable, privacy-respecting, widely reviewed. It is a client, not a data source — reliability is that of the feeds you add.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- feedly
- inoreader
aliases:
- Reeder app
- reederapp.com
tags:
- rss
- feed-monitoring
- news-digest-and-discovery-tools
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Reeder

> A polished Apple-platform feed reader — aggregate a subject's RSS/Atom feeds, YouTube channels, and podcasts into one synced timeline for ongoing monitoring.

## When to use
You have identified sources tied to a subject — a blog `domain`, a YouTube channel, a podcast, a Mastodon/social feed — and want to watch them over time rather than re-checking manually. Reeder turns those into a single, deduplicated, cross-device timeline, useful for longitudinal monitoring of a person or organisation's public output during an investigation.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Reeder from the Mac App Store (macOS 14+) or App Store (iOS 17+).
2. Add sources: paste a feed URL, a site `domain` (Reeder discovers its feed), a YouTube channel, or a podcast; group them into folders per subject/case.
3. Reeder polls the sources and builds a timeline; enable iCloud sync to share state across your devices.
4. Review new items as they arrive; open the original link to capture/evidence anything relevant.
5. Pivot: a monitored post that links out or names accounts feeds link-extraction and social-profile tools; the subject's own new content is a fresh lead stream.

## Inputs → Outputs
- **In:** `domain`/feed URLs, `social-profile`/channel URLs to subscribe to
- **Out:** a running timeline of new items from those sources (a monitoring feed, not a one-shot lookup)
- **Empty/negative result looks like:** a source you add never produces items — the site has no discoverable RSS/Atom feed, or the channel is inactive; find the feed URL manually or use a feed-generator service.

## Gotchas & OpSec
- Apple-only (macOS/iOS) — no Windows/Linux/web client. If you need cross-platform or team monitoring, use a web-based reader instead.
- It is a client, not a discovery engine: you must already know the sources. It finds nothing on its own.
- Subscribing pulls from the source host directly and repeatedly; for sensitive targets, proxy the feeds so your IP is not fetching them on a schedule.

## Overlaps ("do both")
- Alternatives on other platforms: `[[feedly]]` and `[[inoreader]]` are web/cross-platform readers with search and rules. Use Reeder for a fast native Apple workflow; use those when you need team access, alerting rules, or a browser client.

## Trust & verifiability
`trust: trusted` — reputable, long-lived app. It faithfully relays feed content; verify facts at the original source, since a reader only mirrors what the feed publishes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reeder |
