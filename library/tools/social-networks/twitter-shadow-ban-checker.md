---
id: twitter-shadow-ban-checker
name: Twitter Shadow Ban Checker
description: Use when you have an X/Twitter `username` and want to know whether that account is being algorithmically suppressed (search-banned, ghost-banned, reply-deboosted) — returns a per-test shadowban status for the profile.
url: https://shadowban.yuzurisa.com/
category: social-networks
path:
- social-networks
bestFor: Checking whether a public X/Twitter handle is search-banned, ghost-banned, or reply-deboosted.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to use; the page carries an optional PayPal donation link, no account or payment required.
opsec: passive
opsecNote: You query a third-party checker, not the target's account. The target is not notified and nothing is posted. The checker itself sees the handle you look up, so use a sock-puppet session if you don't want that handle tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community rebuild of the original open-source shadowban.eu tester (made in Germany by @shadowban_eu, rebuilt by @Sena_n_Karin); it probes X's public search/reply surfaces rather than any private data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- shadowban.eu
- Twitter shadowban test
- X shadowban checker
tags:
- Social Media
- Twitter
- account-analysis
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Twitter Shadow Ban Checker

> A one-box tester that tells you whether a public X/Twitter handle is being algorithmically suppressed — search-banned, ghost-banned, or reply-deboosted.

## When to use
You have an X/Twitter `username` and the account's tweets look invisible in search or replies — you want to confirm whether X is suppressing it. In a missing-persons context this helps explain why a subject's (or a tip-line's) posts aren't surfacing in normal search, so you know to pull their timeline directly instead of trusting search results.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://shadowban.yuzurisa.com/ in a browser (a sock-puppet session if you don't want the lookup tied to you).
2. Type the target handle (without the `@`) into the box and submit.
3. Read the per-test results:
   - **Search Ban** — the account doesn't appear in search results at all.
   - **Search Suggestion Ban** — the handle is hidden from search auto-suggestions.
   - **Ghost Ban / Reply Deboosting** — the account's replies are hidden or down-ranked behind "Show more replies."
   A green/OK on every test means no suppression detected; a red flag on any test names the specific suppression.
4. Pivot: if the account is search-banned, don't rely on X search to find its content — open the profile timeline directly, or feed the handle to a dedicated timeline scraper.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (a suppression-status report for that account: search-ban / suggestion-ban / ghost-ban / reply-deboost flags)
- **Empty/negative result looks like:** "User not found" (handle is misspelled, suspended, or deleted) or all-clear with every test passing — meaning no shadowban was detected, not that the account is inactive.

## Gotchas & OpSec
- The tool only works on public, non-protected accounts; a protected/locked account returns nothing.
- Results are a point-in-time probe of X's surfaces — X's ranking changes constantly, so a flag can appear or clear within hours.
- OpSec: **passive** — the target is never notified. Only the third-party checker sees your query; nothing touches the target's account.

## Overlaps ("do both")
- Pairs with a dedicated timeline/username scraper — this tells you *whether* content is suppressed; a scraper actually *pulls* the content the suppression is hiding.

## Trust & verifiability
`trust: community` — an open-source community rebuild of the well-known shadowban.eu tester. It infers status from X's own public search and reply behavior, so treat flags as strong indicators rather than confirmations from X.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-shadow-ban-checker |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
