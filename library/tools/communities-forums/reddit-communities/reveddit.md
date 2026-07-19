---
id: reveddit
name: Reveddit
description: Use when you have a Reddit username or thread and want content moderators/admins removed — returns the removed comments/posts, restoring a fuller activity picture.
url: https://www.reveddit.com/
category: communities-forums
path:
- communities-forums
- reddit-communities
bestFor: Recovering a Reddit user's removed/deleted comments and posts to see what a profile no longer shows.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free, open-source, ad-free; no account needed. Runs on public Reddit data plus the Pushshift-style archive it queries.
opsec: passive
opsecNote: You query archives and Reddit's public API, never the target's account — no DM, vote, or follow is generated, so the user isn't alerted. Reading is safe; only your own IP touches Reveddit/Reddit, not the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known independent open-source project; accuracy depends on the availability of the underlying archive, which has degraded as Reddit restricted third-party data access.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- reveddit.com
- removeddit successor
tags:
- reddit
- deleted-content
- content-recovery
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Reveddit

> Shows the removed side of Reddit — the comments and posts a moderator or admin took down that no longer appear on a user's public profile.

## When to use
You have a Reddit `username` (or a specific thread) tied to a subject and want to see what they said that has since been removed — by moderators, admins, or the user's own later deletion. Removed content often carries the most revealing detail (location tells, real names, personal admissions, conflict) precisely because it got taken down. Use it to reconstruct a fuller activity history than the live profile shows, and to catch a still-live account that has been quietly scrubbed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.reveddit.com/.
2. Enter the target `username` (the user page is `reveddit.com/user/<name>`), or paste a thread/subreddit URL.
3. Reveddit lists the user's comments/posts and flags which were **removed** (by mods) vs **deleted** (by the user), showing the removed text where the archive captured it.
4. Read the removed items for selectors: self-disclosed `geolocation`, `name`, employer, other usernames, links. Pivot: cross-reference the same handle on `[[reddit-user-analyser]]`-style tools and other platforms; a mentioned location/name feeds broader search.

## Inputs → Outputs
- **In:** `username` (or a Reddit thread/subreddit URL)
- **Out:** removed/deleted comments and posts with subreddit, timestamp and (where archived) full text — restoring a fuller `social-profile` activity picture
- **Empty/negative result looks like:** nothing removed, or "no data" — the account is clean, too new/old for the archive, or the content predates/postdates archive coverage; absence of removed content is not absence of activity.

## Gotchas & OpSec
- Human-in-the-loop: none; but archive coverage has shrunk since Reddit's 2023 API restrictions, so older or very recent removed content may not be recoverable.
- OpSec: fully passive — the user gets no notification; you never interact with their account.
- Removed text is captured at archive time; if it was edited before removal you see the archived version, not necessarily the final one. Verify sensitive claims against other sources.

## Overlaps ("do both")
- Pairs with live-profile tools and `[[reddit-user-analyser]]`-style analytics — the live tools show what's public now, Reveddit shows what was taken down; together they give the full arc of an account.

## Trust & verifiability
`trust: community` — a respected independent open-source tool, but it depends on third-party archives whose completeness varies; treat recovered text as a lead to corroborate, not proof on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reveddit |
| category | communities-forums |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
