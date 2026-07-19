---
id: github-com-skarlso-rscrap
name: Github.com/Skarlso/rscrap
description: Use when you want to monitor a subreddit and get new posts pushed to Telegram — a small open-source Ruby bot that scrapes a subreddit and forwards items to a Telegram chat.
url: https://github.com/skarlso/rscrap
category: messaging
path:
- messaging
bestFor: Automatically forwarding new posts from a subreddit into a Telegram chat for monitoring.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (Ruby); you self-host it and supply your own Telegram bot token (and optional bit.ly key).
opsec: passive
opsecNote: The bot reads public subreddit content and pushes it to your own Telegram — it does not interact with the subject. Running it exposes nothing to targets, but it does require a Telegram bot token and pulls Reddit via your host's IP; run it from infrastructure not tied to your identity if monitoring sensitive communities.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A small personal open-source project (skarlso/rscrap), minimally maintained; useful as a self-hosted monitor, not a supported product — read the code before running.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- rscrap
- skarlso rscrap
tags:
- telegram
- open-source
- cli
- reddit
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Github.com/Skarlso/rscrap

> A minimal self-hosted Ruby bot that watches a subreddit and relays new posts into a Telegram chat — set-and-forget monitoring rather than an interactive lookup.

## When to use
You want passive, ongoing monitoring of a subreddit tied to an investigation — a community a subject frequents, a topic, a local board — and you'd rather have new posts arrive in Telegram than keep refreshing Reddit. rscrap scrapes the subreddit on a schedule and forwards items to a Telegram user/channel you control. It's an automation/alerting tool, not a people-search.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (`git clone https://github.com/skarlso/rscrap`) and review the code — it's a small Ruby project.
2. Install Ruby dependencies per the README.
3. Create a Telegram bot via @BotFather to get a bot token; note your target chat ID. Optionally add a bit.ly key for URL shortening.
4. Configure the target subreddit and your token(s), then run the bot on a host/VPS so it polls continuously.
5. Pivot: forwarded posts surface `username`s, links and content to investigate; feed usernames into Reddit history and cross-platform username tools.

## Inputs → Outputs
- **In:** a subreddit to monitor (`social-profile` context) + your Telegram bot token
- **Out:** new subreddit posts delivered to Telegram (a running feed of `social-profile` activity)
- **Empty/negative result looks like:** no messages arriving — usually a misconfigured token/chat ID, a private/empty subreddit, or Reddit rate-limiting; check the bot logs.

## Gotchas & OpSec
- Human-in-the-loop: you must provision a Telegram bot `api-key`/token and host the process yourself — this is not a hosted service.
- Minimally maintained personal project — audit the code and pin dependencies before running; behavior may drift with Reddit changes.
- OpSec: passive toward the subject, but Reddit sees your host IP polling — use non-attributable infrastructure for sensitive monitoring.

## Overlaps ("do both")
- Pairs with interactive Reddit history tools like [[chearch]] — rscrap gives you *ongoing* alerts on new activity, while a history tool lets you dig *backwards* through a user's or subreddit's past.

## Trust & verifiability
`trust: community` — a small open-source bot with no guarantees; trust rests on reading the code yourself, and forwarded content is raw Reddit data to be verified downstream.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-com-skarlso-rscrap |
| category | messaging |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
