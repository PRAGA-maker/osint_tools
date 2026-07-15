---
id: slack-web-scraper
name: slack-web-scraper
description: Use when you have access to a Slack workspace and want to archive a channel's messages for offline analysis — returns JSON exports of posts, threads, participants and timestamps.
url: https://github.com/iulspop/slack-web-scraper
category: messaging
path:
- messaging
- slack
bestFor: Archiving Slack channel/DM content you can already access into local JSON for evidence and analysis, without API keys or admin.
input: Slack-authenticated browser/session context
output: Scraped channel messages and related metadata exports
selectorsIn:
- username
selectorsOut:
- username
- associate
- social-profile
status: degraded
pricing: free
costNote: Free open-source (Node.js) project; no Slack paid plan or API key required. Repository was archived by its author in September 2024.
opsec: active
opsecNote: It logs in as YOUR Slack account via a headless browser and drives the workspace UI — Slack (and any workspace admin/audit log) can see that session's activity, and rapid navigation may be rate-limited or flagged. Only run against workspaces you are lawfully a member of; use with care and expect the account to be attributable.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: A single-developer project, now archived (Sept 2024); the author himself recommends intercepting network requests over HTML scraping, so expect breakage against current Slack.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- iulspop/slack-web-scraper
tags:
- slack
- scraper
- archiving
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# slack-web-scraper

> A Puppeteer-driven Node.js scraper that logs into Slack as you and archives a channel's messages to JSON — no API key, no app install. Now archived/unmaintained.

## When to use
You are a member of a Slack workspace (an investigation group, a leaked/joined community, your own org) and need a durable offline copy of a channel or DM — for evidence preservation, timeline building, or mapping who talks to whom. Because it uses your normal login rather than the Slack API, it works where you lack admin rights or an API token, capturing what your account can already see.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/iulspop/slack-web-scraper` and `npm install` (Node.js).
2. Configure your Slack login/session as the README directs; the tool launches a Puppeteer headless browser and authenticates as you.
3. Run `npm run collect` to scrape the target channel/DM, then `npm run parse` to convert the captured HTML into JSON.
4. Read the JSON: posts, threads, author `username`s and timestamps. Pivot: participant handles feed cross-platform username searches; reply structure maps `associate` relationships.

## Inputs → Outputs
- **In:** a Slack workspace you can log into (channel/DM `username` context)
- **Out:** JSON of messages/threads, author `username`s, participant `associate` links, and profile references (`social-profile`)
- **Empty/negative result looks like:** login failure, an empty scrape, or a parse error — increasingly likely since the repo is archived and Slack's UI/DOM has moved on. A blank export usually means the scraper broke, not that the channel was empty.

## Gotchas & OpSec
- **Archived (Sept 2024) & brittle:** built on HTML scraping, which the author now advises against in favor of network-request interception; assume it needs fixing to run against today's Slack.
- **Active & attributable:** it drives your logged-in account (`account-login` human-in-loop); workspace audit logs and Slack itself see the activity. Only scrape workspaces you're lawfully in.
- Rate-limiting/anti-automation can throttle or block a fast scrape.

## Overlaps ("do both")
- Pairs with Slack's official export (if you have admin/Corporate Export) and with network-capture approaches — those are more reliable when available; this fills the gap when you have only ordinary member access.

## Trust & verifiability
`trust: unverified` — a small, now-archived personal project. Inspect the code before running, verify captures against the live Slack UI, and treat it as a best-effort archiver rather than a guaranteed-complete export.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slack-web-scraper |
| category | messaging |
| selectorsIn → selectorsOut | username → username, associate, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
