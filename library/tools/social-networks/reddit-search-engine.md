---
id: reddit-search-engine
name: Reddit Search Engine (Google CSE)
description: Use when you have a `username`, `name` or keyword and want Reddit posts/comments indexed by Google — returns Reddit `social-profile` and thread links.
url: https://cse.google.com/cse?cx=0728740ab68a619ba
category: social-networks
path:
- social-networks
bestFor: Searching Reddit content through a Google Custom Search Engine when Reddit's native search is too weak.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account. Powered by Google's index, so coverage is whatever Google has crawled from reddit.com.
opsec: passive
opsecNote: Queries go to Google, not to Reddit or the subject — passive. Nothing you search alerts the account owner. Use a clean browser/VPN if you want the queries unattributable to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Programmable Search Engine (branded with the osintme.com logo); it's just a scoped Google search, so results are Google's, but the CSE config could change or lapse over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- reddit CSE
- reddit programmable search
tags:
- reddit
- social-search
- custom-search-engine
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Reddit Search Engine (Google CSE)

> A Google Programmable Search Engine scoped to Reddit — Google's index doing what Reddit's own search does poorly.

## When to use
You want to find Reddit activity for a subject: a `username` (people often reuse the same handle on Reddit), a real `name`, an email prefix, or a distinctive phrase. Reddit's native search is notoriously weak at surfacing old comments and cross-subreddit mentions; this CSE leans on Google's crawl of reddit.com to find posts, comments, and profiles Reddit's own search buries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cse.google.com/cse?cx=0728740ab68a619ba.
2. Search the `username`, `name`, or keyword. Standard Google operators work — quote exact phrases, and Reddit URLs like `/user/<handle>` or `/r/<subreddit>` narrow results.
3. Read the hits: links into Reddit threads, comments, and `u/` profile pages.
4. Open the profile/thread on Reddit itself and pivot: posting history, subreddits (interests/location clues), other linked handles, and `associate` interactions.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword/phrase
- **Out:** Reddit `social-profile` and thread/comment links from Google's index
- **Empty/negative result looks like:** no results — either the handle/term isn't on Reddit, or Google hasn't indexed it (recent or deleted content, or content Reddit blocks from crawling). Absence here is not proof of absence on Reddit; also try Reddit's own search and a general web search.

## Gotchas & OpSec
- You're limited to what Google has crawled: very recent, deleted, or quarantined content may be missing.
- A CSE is a third-party config that can be changed or removed by its owner; if it stops returning results, fall back to a plain Google `site:reddit.com <query>` search, which does the same thing.
- Passive toward the subject; queries are visible to Google.

## Overlaps ("do both")
- Do both with a plain `site:reddit.com` Google search and with Reddit-native/third-party history tools — the CSE and `site:` search share Google's index, while dedicated Reddit tools can reach comment history and deleted-content archives Google misses.

## Trust & verifiability
`trust: community` — it is a community-configured wrapper around Google search, so the underlying results are Google's (reliable), but the scoping config is third-party and may drift; verify important hits by opening them on Reddit directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
