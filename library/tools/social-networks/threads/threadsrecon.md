---
id: threadsrecon
name: ThreadsRecon
description: Use when you have a Threads `username` and want an automated scrape + analysis of their profile, posts, and network — returns social-profile data, associates, and PDF/JSON investigation reports.
url: https://github.com/offseq/threadsrecon
category: social-networks
path:
- social-networks
- threads
bestFor: One-command Threads profile investigation with sentiment and network-graph reporting.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- image
status: live
pricing: free
costNote: Free, open-source (offseq/threadsrecon) on GitHub. No paid tier.
opsec: active
opsecNote: Makes direct automated requests to threads.net for the target profile; scraping at volume can require a logged-in session and may trip Meta's anti-bot/rate limits. Run from a sock-puppet Threads/Instagram account and a non-attributable IP, never your own.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Open-source project (offseq) with active commit history (~79 commits); inspectable but unaudited, and dependent on Threads' HTML which changes without notice.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- threads-net
- soig
aliases:
- offseq/threadsrecon
tags:
- threads
- social-media-scraper
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# ThreadsRecon

> A CLI tool that scrapes a Threads profile, runs sentiment and network analysis, and generates JSON data, visualizations, and PDF investigation reports.

## When to use
You have a subject's Threads (`username`) and want more than the profile page: a structured dump of posts and engagement, a map of who they interact with (associates), and a shareable report. The network graph is the standout for missing-persons work — it surfaces the accounts the subject engages with most, which are candidate contacts.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/offseq/threadsrecon` (Python; Docker also supported).
2. Add the target username(s) to `settings.yaml` and configure any scraping/session options.
3. Run the pipeline: `python main.py all` — or run stages individually (`scrape`, `analyze`, `visualize`, `report`).
4. Read the outputs: JSON post data, sentiment scores, network graphs, and a PDF report (optional Telegram alerts).
5. Pivot: associates from the network graph feed per-account lookups; media/images feed reverse-image search.

## Inputs → Outputs
- **In:** `username` (Threads handle, via config)
- **Out:** `social-profile` (posts, engagement, sentiment), `associate` (interaction network), `image` (scraped media)
- **Empty/negative result looks like:** an empty scrape or auth error usually means the profile is private, the handle is wrong, or Threads blocked the requests — not that the account is inactive.

## Gotchas & OpSec
- Human-in-the-loop: bulk scraping may demand a logged-in Threads session and manual rate-limit tuning; expect breakage when Meta changes the site.
- OpSec: **active** — requests hit Threads tied to your IP/session. Use a sock-puppet account; never your real one.
- Reports are only as good as what's public; private accounts yield little.

## Overlaps ("do both")
- Pairs with `[[threads-net]]` — manual Threads profile review to confirm/contextualize what the scraper reports.
- Pairs with `[[soig]]` — Threads and Instagram share Meta identity; run both to correlate the subject's presence across the two.

## Trust & verifiability
`trust: community` — open source and inspectable, but unaudited and reliant on scraping a hostile, fast-changing target; verify key findings against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threadsrecon |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
