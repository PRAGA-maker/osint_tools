---
id: selfoss
name: Selfoss
description: Use when you want a private, self-hosted feed of many sources (RSS/Atom, scraped pages, social feeds) to monitor a subject or topic over time — returns a unified, archived stream you control.
url: https://selfoss.aditu.de
category: archives-cache
path:
- archives-cache
bestFor: Self-hosted aggregation and archiving of RSS/Atom and custom source feeds for ongoing monitoring.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GPL); costs only the hosting you provide (lightweight PHP + SQLite/MySQL).
opsec: passive
opsecNote: Because you self-host, your monitoring interests never touch a third-party reader's servers — a strong OpSec win over cloud RSS services. Fetch through your own server/VPN; the target sees only your server's IP polling their public feed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: trusted
trustNote: Long-running open-source project (self-hostable, auditable code on GitHub, active releases); it only aggregates public feeds, so no third-party data-quality risk.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
relatedTools: []
aliases:
- selfoss RSS reader
tags:
- rss
- monitoring
- self-hosted
source: uk-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Selfoss

> A lightweight, self-hosted feed aggregator: pull RSS/Atom and custom-scraped sources into one private stream you own — ideal for standing monitoring of a person, org or topic.

## When to use
You need to watch many public sources continuously — a subject's blog, news mentions, forum/social feeds, a site's changes — without handing your watchlist to a commercial reader. Selfoss runs on your own server, aggregates everything into one timeline, and keeps items so you have an archive of what appeared and when.

## How to use it (`bestInteractionPattern`: docker / self-host)
1. Deploy it: upload the PHP app to a host, or run a community Docker image; point it at SQLite (default) or MySQL.
2. Log in and add sources — RSS/Atom URLs, plus spouts (built-in connectors) for pages/services without native feeds.
3. Let it poll on a schedule; read the unified stream, star/tag items worth keeping, and use the mobile/API access for on-the-go review.
4. Pivot: export or link out interesting items to your case notes; combine with change-detection tools for sources that lack a feed.

## Inputs → Outputs
- **In:** none as a selector — you configure source feeds/URLs to monitor
- **Out:** none as a selector — a unified, archived stream of items from those sources
- **Empty/negative result looks like:** a source that never produces items usually means a broken feed URL or a site with no feed — verify the feed or add a scraping spout.

## Gotchas & OpSec
- Human-in-the-loop: initial setup (hosting + adding sources) is technical; day-to-day use is passive.
- Self-hosting is the point — a cloud RSS reader would expose your monitoring targets; keep Selfoss on infrastructure you control.
- It aggregates public feeds only; it won't reach content behind logins without a suitable spout/credentials.

## Overlaps ("do both")
- Pair with a change-detection/website-monitoring tool for feedless pages, and with archiving tools to preserve items Selfoss surfaces before they vanish.

## Trust & verifiability
`trust: trusted` — mature open-source software you run yourself; the reliability question is your hosting, not a vendor, and it only relays public feed content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | selfoss |
| category | archives-cache |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
