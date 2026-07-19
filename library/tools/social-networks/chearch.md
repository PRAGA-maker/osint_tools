---
id: chearch
name: Chearch
description: Use when you have a Reddit `username` or keyword and want to query historical Reddit posts/comments with filters — returns matching posts/comments (a `social-profile` timeline), if you hold a Pushshift token.
url: https://adhesivecheese.github.io/chearch/
category: social-networks
path:
- social-networks
bestFor: Filtered search of a Reddit user's or subreddit's historical posts and comments via Pushshift.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: The web front end is free, but it queries the Pushshift API, which since 2023 is restricted to verified Reddit moderators — without an approved Pushshift token you cannot run searches.
opsec: passive
opsecNote: Queries go to Pushshift's archive, not to Reddit or the subject — the target is not notified. It's a static client-side page hosted on GitHub Pages; your searches are seen by Pushshift under whatever token/account you authenticate with, so use a research account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source hobby front end (adhesivecheese on GitHub) over the third-party Pushshift archive; only as current/complete as Pushshift's data and your access to it.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Chearch Reddit search
tags:
- social-networks
- reddit
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Chearch

> A lightweight Pushshift front end for searching Reddit history by user, subreddit, term, score and date — powerful when you have Pushshift access, inert when you don't.

## When to use
You have a Reddit `username` (or a subreddit / keyword) and want to reconstruct a user's activity — old posts and comments, including ones deleted from live Reddit — with filters on score, date range and result count. Reddit's own search is shallow and drops deleted content; Pushshift-backed tools like Chearch reach the archive.

## How to use it (`bestInteractionPattern`: web-manual)
1. Confirm you have a Pushshift API token first — since 2023 Pushshift restricts access to verified Reddit moderators, so Chearch returns nothing without one.
2. Open https://adhesivecheese.github.io/chearch/ and paste your access token where prompted.
3. Set the query: target `username` or subreddit, optional search term, min/max score, since/until dates, and result count.
4. Choose Posts or Comments and run; toggle markdown rendering, term highlighting and thumbnails for readability.
5. Read the returned items as a `social-profile` timeline. Pivot: usernames, linked accounts, place names and photos in old comments feed further searches.

## Inputs → Outputs
- **In:** `username` (or subreddit / keyword) plus filters
- **Out:** matching Reddit posts/comments — a reconstructed `social-profile` activity trail
- **Empty/negative result looks like:** an auth error (no valid Pushshift token) or zero results — distinguish "no access" from "no data," because without a token everything looks empty.

## Gotchas & OpSec
- Human-in-the-loop: you must supply a Pushshift `api-key`/token; that gate is the main blocker and is why this tool is marked **degraded**.
- Pushshift's index has gaps and stops at whatever it last ingested — absence is not proof.
- OpSec: passive toward the subject; Pushshift sees your queries under your token, so authenticate with a research identity.

## Overlaps ("do both")
- Pairs with any live-Reddit username scanner and general username tools like [[whatsmyname]] — Chearch reaches *archived/deleted* Reddit history, while live tools show the current, un-deleted profile. Do both to compare then-vs-now.

## Trust & verifiability
`trust: community` — an open-source front end over a third-party archive; verify recovered posts against live Reddit or [[wayback-machine]] where the content still exists, since Pushshift data can be stale or partial.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chearch |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
