---
id: github-user
name: Github User
description: Use when you have a GitHub `username` and want their recent public activity — returns a JSON feed of pushes, PRs, issues, and comments with timestamps and repo names, exposing `associate` and timezone signals.
url: https://api.github.com/users/%3Cusername%3E/events/public
category: username
path:
- username
- specific-sites
bestFor: Pulling a GitHub user's recent public event timeline (activity, repos, collaborators, timing) from the unauthenticated API.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: free
costNote: Free public GitHub REST API; unauthenticated calls are rate-limited to 60/hour per IP (5000/hr with a token).
opsec: passive
opsecNote: A read of a public JSON endpoint. GitHub does not notify the user, but your IP is subject to GitHub's rate limits and logs. No token is needed; if you use one, use a burner account's token, not your own.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: First-party GitHub REST API — the event data is authoritative (it is GitHub's own record of public activity), though it only spans roughly the last 90 days / 300 events.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- commit-stream
- gosearch
aliases:
- GitHub public events API
- github user events
tags:
- github
- activity-timeline
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Github User

> The unauthenticated GitHub events API as an OSINT feed: a JSON timeline of a user's recent public pushes, PRs, issues, and comments — good for activity patterns, collaborators, and timezone inference.

## When to use
You have a GitHub `username` (confirmed as your subject's) and want to profile their behaviour: which repos they touch, who they collaborate with (`associate`), commit email addresses surfaced in push payloads, and the clock/day pattern of their activity (a strong timezone/lifestyle signal). This turns a static profile into a behavioural timeline.

## How to use it (`bestInteractionPattern`: api)
1. Substitute the handle into the URL: `https://api.github.com/users/<username>/events/public`.
2. Fetch it (browser, `curl`, or code) — returns a JSON array of recent public events.
3. Parse for signal:
   - `PushEvent` payloads often expose commit author `name`/email and the repos worked on.
   - `PullRequestEvent`/`IssueCommentEvent` reveal collaborators and projects (`associate` links).
   - Event `created_at` timestamps cluster by the user's active hours → infer timezone/routine.
4. Note the ~90-day / 300-event ceiling; for older history use commit search tools.
5. Pivot: commit emails feed email OSINT; collaborator handles feed more `[[github-user]]` pulls; cross-reference commit emails with `[[commit-stream]]`.

## Inputs → Outputs
- **In:** GitHub `username`
- **Out:** `social-profile` activity timeline, `associate` (collaborators), and `metadata-exif`-style event metadata (timestamps, commit emails, repos)
- **Empty/negative result looks like:** `[]` (empty array) means no recent public events — an inactive or private-activity account, not a nonexistent user (a 404 means the username doesn't exist).

## Gotchas & OpSec
- Only ~90 days / last 300 public events are returned; it is a recent-activity feed, not full history.
- Private activity and private repos never appear; a quiet feed can hide heavy private work.
- Unauthenticated rate limit is 60 req/hr per IP — pace bulk pulls or use a burner token (5000/hr).
- OpSec: passive; no notification to the user. Still, mask your IP and avoid using your own authenticated token.

## Overlaps ("do both")
- Pairs with `[[commit-stream]]` — that surfaces commit author emails across GitHub; use it to extend the email/identity picture beyond the 90-day event window.
- Feed a confirmed handle into `[[gosearch]]` for cross-platform presence.

## Trust & verifiability
`trust: trusted` — it is GitHub's first-party API, so the events themselves are authoritative. The caveat is completeness (recent-only, public-only), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-user |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, associate, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
