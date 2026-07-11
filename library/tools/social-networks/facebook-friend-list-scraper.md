---
id: facebook-friend-list-scraper
name: Facebook Friend List Scraper
description: Use when you have a target's Facebook profile and want their friend network — returns the names and usernames of accounts on a large friend list without hitting rate limits.
url: https://github.com/narkopolo/fb_friend_list_scraper
category: social-networks
path:
- social-networks
bestFor: Extracting names/usernames from a target's Facebook friend list at scale.
selectorsIn:
- social-profile
- username
selectorsOut:
- name
- username
- associate
status: live
pricing: free
costNote: Free and open-source (pip-installable CLI). No fees; you supply a Facebook login.
opsec: active
opsecNote: It logs in with a real Facebook account and scrapes the target's friends from your session — Facebook can detect this and may flag/ban the account used. ALWAYS use a dedicated sock-puppet Facebook account and a proxy, never your real identity. Scraping friend lists may breach Facebook's terms.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Community open-source scraper (~300 stars). Works only while it matches Facebook's current page markup, which changes often — expect breakage.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- fb_friend_list_scraper
- fbfriendlistscraper
tags:
- facebook
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Facebook Friend List Scraper

> A CLI that harvests the names and usernames from a Facebook profile's friend list — turning one target into a map of their social circle.

## When to use
You have a subject's Facebook profile (with a visible friend list) and want to enumerate their `associate`s — friends' names and usernames — to identify family, close contacts, and people to interview in a missing-person case. Best when the friend list is public or visible to your sock-puppet account.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `python -m pip install fb-friend-list-scraper`.
2. Prepare a **sock-puppet** Facebook account (and optionally a proxy).
3. Run `fbfriendlistscraper` with the target profile and your sock-puppet credentials; flags let you output only usernames/IDs, run headless, set sleep intervals, and route through a proxy.
4. Read the output text file: friend `name`s and `username`s. Options exist to dump IDs only.
5. Pivot: each friend `username` feeds profile lookups and username enumeration; recurring surnames hint at family/`associate` clusters.

## Inputs → Outputs
- **In:** target Facebook `social-profile`/`username` (+ your sock-puppet login)
- **Out:** list of friends' `name`s and `username`s (`associate` network)
- **Empty/negative result looks like:** empty file or an error — the friend list is hidden/friends-only, the account got challenged, or Facebook changed its markup and broke the parser. An empty result is usually access/tooling, not "no friends."

## Gotchas & OpSec
- Human-in-the-loop: requires a working Facebook login; expect checkpoints/CAPTCHAs on the account you use.
- OpSec: **active** and detectable — Facebook may ban the scraping account; isolate it and use a proxy. This is the most account-risky tool in a FB workflow.
- Fragility: markup changes break it regularly; verify against a known profile before trusting a run.

## Overlaps ("do both")
- Pairs with Facebook graph-search and photo tools — the friend list gives you the network, while graph/photo search enriches each associate into a fuller profile.

## Trust & verifiability
`trust: community` — an unaudited community scraper dependent on Facebook's mutable markup; results are reliable only when the tool is current, so spot-check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-friend-list-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes |
