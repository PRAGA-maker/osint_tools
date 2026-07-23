---
id: snoopsnoo
name: SnoopSnoo
description: Use when you have a Reddit `username` and want a behavioural profile of that account — returns inferred interests, activity patterns, top subreddits, and self-disclosed hints (`social-profile`).
url: https://snoopsnoo.com
category: communities-forums
path:
- communities-forums
bestFor: Profiling a Reddit user's interests, activity times, and top communities from their public comment/post history.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: Reads a user's public Reddit history via SnoopSnoo's servers — the target is not notified and you never touch their account. Only public data is analysed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community-built analytics (open source, hosted best-effort); has had extended outages tied to upstream API changes, so treat availability as unreliable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- snoopsnoo.com
tags:
- reddit
- user-profiling
source: metaosint
lastVerified: '2026-07-23'
---

# SnoopSnoo

> A Reddit user analyser: feed it a username and it summarises what that account is into — interests, active hours, and most-used subreddits — from public post/comment history.

## When to use
You have a Reddit `username` linked to a subject and want a fast behavioural read: what topics they engage with, when they're active (a rough timezone signal), which subreddits they frequent, and any self-disclosed details their posting habits surface. It compresses months of scrolling into a profile page — a strong lead-generator for interests, location hints, and other-platform pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://snoopsnoo.com and enter the target `username` (or visit `snoopsnoo.com/u/<username>`).
2. Wait for it to crawl the public history.
3. Read the report: inferred interests/topics, activity heatmap (day/hour → possible timezone), top subreddits and posting split, and any parsed self-references (jobs, places, gear, relationships).
4. Pivot: subreddit mix and self-disclosures feed location/employment hypotheses; the username feeds cross-platform account search; an activity heatmap corroborates or challenges a claimed timezone.

## Inputs → Outputs
- **In:** `username` (Reddit account)
- **Out:** `social-profile` (interest/activity profile), possible `geolocation` hints (timezone from activity, place mentions)
- **Empty/negative result looks like:** "not enough data" for low-activity/new accounts, an error for suspended/deleted users, or a stale profile if the service is lagging — sparse output means thin history, not necessarily a fake account.

## Gotchas & OpSec
- Availability is unreliable (hence `status: degraded`): it has been down for long stretches when Reddit's API shifted — have a fallback ready (`[[reddit-user-analyser]]`-style tools or manual review, or the `snoosnoop.com` revival).
- Inferences are heuristic: a timezone from activity or a "location" from a comment is a hypothesis, not a fact.
- OpSec: **passive** — public data only, no notification to the target.

## Overlaps ("do both")
- Pairs with manual Reddit history review and other Reddit analytics/username tools — SnoopSnoo summarises fast; manual review catches the specific disclosure that resolves the case.

## Trust & verifiability
`trust: unverified` — community-hosted analytics with a spotty uptime record; verify any actionable inference against the user's actual comments before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snoopsnoo |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
