---
id: export-comments
name: Export Comments
description: Use when you have a public post/video URL and want every comment with handles and timestamps as a spreadsheet — returns commenter `username`s and comment text for network and evidence analysis.
url: https://exportcomments.com/
category: evidence-capture
path:
- evidence-capture
bestFor: Bulk-extracting all comments (and commenter handles) from a social post/video into Excel/CSV/JSON.
selectorsIn:
- social-profile
selectorsOut:
- username
status: live
pricing: freemium
costNote: Free tier exports a capped number of comments per post with no account/credit card; larger exports and scheduling require a paid plan.
opsec: passive
opsecNote: It reads publicly visible comments via the post URL — no interaction with the target or commenters. You are handing the post URL to a third-party service, so avoid using it on access-restricted content you shouldn't redistribute.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial comment-export service; data is a direct pull of public comments, but completeness depends on the platform's API/limits at export time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- ExportComments
tags:
- social-media
- comments
- evidence
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Export Comments

> A bulk comment-exporter for 20+ social platforms — used in OSINT to turn a post's comment section into a structured dataset of handles, timestamps and text for network and sentiment analysis.

## When to use
You have a public post/video URL (YouTube, Instagram, TikTok, Facebook, X, LinkedIn, Reddit, Trustpilot, etc.) and want the whole comment thread as a spreadsheet: who commented (`username`), when, how many likes, and the full text. Ideal for mapping who engages with a subject's content, spotting a target in a comment section, or preserving a thread as evidence before it's deleted.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://exportcomments.com/.
2. Paste the public post/video URL and start the export.
3. Download the result as Excel/CSV/JSON — columns include commenter `username`, timestamp, likes and comment text.
4. Pivot: feed recurring commenter handles into username-search; sort by timestamp/likes to find the most engaged accounts.

## Inputs → Outputs
- **In:** `social-profile` (a public post/video URL)
- **Out:** `username` list + comment text, timestamps, like counts (Excel/CSV/JSON)
- **Empty/negative result looks like:** partial or empty export — the post has comments disabled, is private, or the free-tier cap truncated it; check the count against the visible thread.

## Gotchas & OpSec
- Free-tier caps mean big threads are truncated — note the exported count vs the platform's stated total so you don't treat a partial pull as complete.
- Handles in comments are not unique identities; confirm before attributing.
- OpSec: passive; preserve exports with capture dates for evidentiary use.

## Overlaps ("do both")
- Pairs with username-enumeration and social-search tools: this yields the commenter handles, those resolve each handle into a cross-platform profile.

## Trust & verifiability
`trust: community` — a reputable commercial service returning direct pulls of public comments; completeness is bounded by platform limits and your plan tier.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | export-comments |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile → username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
