---
id: urlwatch
name: urlwatch
description: Use when you have a `domain`/URL (or JSON API) you want to monitor for changes over time — a self-hosted CLI that alerts you when a page's content changes; returns diffs of what changed.
url: https://github.com/thp/urlwatch
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- change-detection
bestFor: Automated, self-hosted monitoring of web pages/APIs for content changes, with notifications.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source Python CLI (install via pip); you run it yourself.
opsec: active
opsecNote: Each check fetches the target URL from YOUR host, so the site's server sees your requests on your polling schedule — that repetition can be noticed. Route through a proxy/sock-puppet and use a sane interval; add filters so you only diff the content you care about.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Mature, well-maintained open-source project (thp/urlwatch) with a large user base; reliable and transparent.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- urlwatch
- thp urlwatch
tags:
- Domain/IP/Links
- change-detection
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# urlwatch

> A self-hosted command-line watcher that fetches a list of URLs on a schedule, diffs each against the last run, and notifies you when the content changes.

## When to use
You need to know **when** something changes rather than what it says right now — a subject's profile or bio page, a company's staff/leadership list, a court-docket or notice page, a marketplace listing, a status page. urlwatch polls the pages you give it and surfaces exactly what changed since last time, so you catch edits, additions, and removals you'd otherwise miss.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install urlwatch`.
2. Add targets: `urlwatch --edit` (list URLs; you can add filters like CSS selectors, `html2text`, or JSON filters to watch only the relevant part of a page).
3. Configure notifications: `urlwatch --edit-config` (email, Telegram, Slack, webhook, etc.).
4. Run on a schedule (cron/systemd timer); each run prints/sends a diff of anything that changed.
5. Pivot: a detected change (new name on a page, updated contact, edited bio) is your lead — capture/archive the page immediately when alerted.

## Inputs → Outputs
- **In:** `domain`/URL(s) (or JSON API endpoints) to monitor
- **Out:** `domain` (change diffs — the added/removed/changed content per URL)
- **Empty/negative result looks like:** "no changes" on a run means the watched content is identical to last time — nothing to act on, which is the normal steady state.

## Gotchas & OpSec
- **Active/repeated fetching:** predictable polling of a target is detectable — proxy it, randomize/space intervals, and filter to the minimal content so noisy dynamic elements don't trigger false diffs.
- You must self-host and keep it running; it's not a hosted service.
- Pages behind logins/JS may need extra config (browser/`pyppeteer` jobs) to capture correctly.

## Overlaps ("do both")
- Overlaps with hosted change-monitoring (e.g. changedetection.io, Visualping) — do the self-hosted urlwatch when you want control/privacy, a hosted one when you want zero maintenance; both solve "tell me when this page changes".

## Trust & verifiability
`trust: trusted` — a mature, transparent open-source tool; it fetches real pages and shows real diffs you can verify by visiting the URL yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urlwatch |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
