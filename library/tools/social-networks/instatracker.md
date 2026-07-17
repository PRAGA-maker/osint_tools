---
id: instatracker
name: instatracker
description: Use when you have an Instagram `username` and want to monitor it over time — returns a timestamped log of changes to followers, following, posts and bio, surfacing new `associate` links.
url: https://github.com/ibnaleem/instatracker
category: social-networks
path:
- social-networks
bestFor: Continuously logging changes (followers/following/posts/bio) on a target Instagram account during an active case.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free and open-source (MIT). No cost; you run the Python script yourself. Requires your own Instagram login for scraping.
opsec: active
opsecNote: The script authenticates with YOUR Instagram account to poll the target via Instaloader, so activity is tied to that account and can be rate-limited or blocked by Instagram — always use a dedicated sock-puppet Instagram login, never your real one. Following/viewing during monitoring can expose you to the target; keep the puppet account uninvolved.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Community Instagram change-logger (~100 stars) by the author of gosearch. Open-source and inspectable; output reliability depends on Instagram not blocking the polling account.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- gosearch
aliases:
- insta-tracker
tags:
- instagram
- monitoring
- change-detection
source: gh-topic-osint-framework
lastVerified: '2026-07-17'
enrichment: full
---

# instatracker

> A change-detection watcher for a single Instagram account: it snapshots followers, following, posts and bio, then logs every change with a timestamp.

## When to use
You have a target Instagram `username` and want to watch it over time rather than take one snapshot. instatracker records when the account gains/loses followers or following, posts or deletes, or edits its bio — the follower/following deltas are especially useful, since a newly-followed account is a fresh `associate` lead and bio edits can leak new contact info or locations. Reach for it during an active case where a known account is worth continuous monitoring.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/ibnaleem/instatracker` and install its requirements (Python 3 + Instaloader).
2. Run `python3 main.py -u <target_username>`; log in with a **dedicated sock-puppet** Instagram account when prompted (credentials aren't stored, but the session is tied to that account).
3. Leave it running — it polls roughly every 5 minutes and writes changes to a timestamped log file and the terminal.
4. Review the log for follower/following/post/bio changes over the monitoring window.
5. Pivot: newly-followed/following accounts are `associate`/`social-profile` leads; bio changes feed contact/geolocation follow-ups; post deletions flag content worth having archived.

## Inputs → Outputs
- **In:** `username` / `social-profile` (a target Instagram account)
- **Out:** timestamped change log; new `associate`/`social-profile` links from follower/following deltas
- **Empty/negative result looks like:** no changes logged (a dormant account), or the run halts because Instagram blocked/challenged the polling account — the latter is a tooling failure, not "no activity."

## Gotchas & OpSec
- OpSec: **active** — you poll via your own logged-in account; Instagram sees that account's traffic. Use a burner Instagram, expect rate-limits/challenges, and never authenticate with your real identity.
- Private accounts require the polling account to already follow the target (which is itself intrusive and attributable) — best suited to public accounts.
- Continuous polling can trip anti-bot defences; the ~5-minute interval is a deliberate throttle — don't shorten it.

## Overlaps ("do both")
- Pairs with `[[gosearch]]` (same author) — use gosearch/username tools to establish the account and cross-platform presence first, then instatracker to monitor the confirmed account over time.

## Trust & verifiability
`trust: community` — open-source and inspectable; the change log is generated from Instaloader's view of the public account, so entries are verifiable against the live profile. Reliability hinges on the polling account staying unblocked.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instatracker |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
