---
id: tweet-finder
name: Tweet Finder (Google CSE)
description: Use when you have a keyword, `name`, or `username` and want tweets/profiles indexed by Google — returns Google-indexed twitter.com/x.com links matching your terms.
url: https://cse.google.com/cse/publicurl?cx=016621447308871563343:u4r_fupvs-e
category: social-networks
path:
- social-networks
bestFor: Keyword/name/handle search scoped to Google-indexed Twitter/X content via a Custom Search Engine.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
status: degraded
pricing: free
costNote: Free hosted Google Custom Search Engine; no account required.
opsec: passive
opsecNote: Queries go to Google, not to X, so the target isn't touched or notified. Standard search-engine hygiene (sock-puppet browser) is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party Google Custom Search Engine over twitter.com/x.com; coverage is only what Google has indexed and has degraded as X restricts indexing and login-gates content.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Tweet Finder CSE
tags:
- twitter
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Tweet Finder (Google CSE)

> A pre-built Google Custom Search Engine scoped to Twitter/X — a keyword-to-tweet shortcut that leans on Google's index when X's own (login-gated) search won't cooperate.

## When to use
You have a keyword, `name`, or `username` and want to find Google-indexed tweets or profiles — handy when you can't or don't want to log into X, or when native search is dropping older content. A useful complement to `[[twitter-search]]` for surfacing publicly indexed posts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL in a sock-puppet browser.
2. Enter the `name`/`username`/keyword (add a distinctive term or date to cut noise).
3. Read the results: Google-indexed twitter.com/x.com links — profiles and individual tweets.
4. Because it only sees Google's (shrinking) index of X, open hits directly and corroborate with native search/archives.
5. Pivot: a found account feeds `[[tinfoleak-web]]` and username enumeration; specific posts anchor a timeline.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** Google-indexed X `social-profile`/tweet links, matched `username`s
- **Empty/negative result looks like:** few/no hits — X increasingly blocks indexing and gates content behind login, so misses often reflect the index, not the person's absence from X.

## Gotchas & OpSec
- Index-limited & degrading: only publicly Google-indexed X content appears; coverage shrinks as X restricts crawlers (`status: degraded`).
- Stale CSE: a fixed third-party configuration that may not track current X URL patterns.
- OpSec: passive — queries hit Google, not X.

## Overlaps ("do both")
- Pairs with `[[twitter-search]]` and Twitter archives — native search and archives recover what Google's index drops; run all three and merge.

## Trust & verifiability
`trust: unverified` — a third-party CSE whose coverage depends entirely on Google's X index and the config's freshness; verify each hit on-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweet-finder |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
