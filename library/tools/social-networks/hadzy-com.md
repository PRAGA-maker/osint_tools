---
id: hadzy-com
name: Hadzy.com
description: Use when you have a YouTube `username` or a specific video and want to search and analyse its public comments — returns matching comments, authors, timestamps, and engagement patterns.
url: https://hadzy.com/
category: social-networks
path:
- social-networks
bestFor: Searching and filtering the comment section of any public YouTube video by keyword or author.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Completely free; no account, registration, or install required.
opsec: passive
opsecNote: Hadzy reads YouTube's public comment data via its own API access — you never interact with the video, its owner, or the commenters, so nothing is signalled to the target. Pasting a URL and searching leaves only ordinary web logs on Hadzy's side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-purpose third-party YouTube comment tool; it surfaces genuine public comments, but the index is only as complete as YouTube's API returns and the tool's operator maintains it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Hadzy YouTube comment search
tags:
- youtube
- comment-search
- social-networks
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Hadzy.com

> A free YouTube comment search and analytics tool — pull, search, and filter the full comment section of any public video, Short, or live-stream replay.

## When to use
You have a target's YouTube channel/`username`, or a specific video they posted or engaged with, and you need to work the comments. Two common cases: (1) find every comment a particular author left on a video, or (2) search a video's comments for a keyword, phone number, name, or handle a subject may have dropped. Native YouTube has no comment search, so this fills a real gap when a person's YouTube footprint is a lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hadzy.com/.
2. Paste the YouTube video URL (or search for the video) to load its comments.
3. Search within the loaded comments by keyword/phrase, or by **author name** to isolate one commenter's activity.
4. Filter by date range, like count, or reply count; switch between list, table, and timeline views to spot activity patterns.
5. Read the output: matching comments with author handle (`username`/`social-profile`), timestamp, and the video timecode referenced.
6. Pivot: an author handle feeds username-search tools; a comment's content may leak another `social-profile`, a location, or contact detail.

## Inputs → Outputs
- **In:** a YouTube video URL, plus a search keyword or an author `username`
- **Out:** matching public comments with author `social-profile`/`username`, timestamps, engagement counts
- **Empty/negative result looks like:** "no comments" (comments disabled or private video), or zero keyword matches — meaning the term isn't in that video's comments, not that the person is absent from YouTube.

## Gotchas & OpSec
- It analyses **one video's comments at a time** — it is not a cross-YouTube search for everywhere a handle has commented; you must feed it individual videos.
- Only public videos with comments enabled work; private/unlisted or comment-disabled videos return nothing.
- Very large comment sections can be slow or partially loaded; verify counts look complete before concluding a term is absent.
- OpSec: fully passive — you never touch the target's channel or notify anyone.

## Overlaps ("do both")
- Pairs with a channel/username-search tool: use that to find the videos a subject posts or frequents, then run each through [[hadzy-com]] to mine the comments.

## Trust & verifiability
`trust: community` — Hadzy is an independent third-party tool surfacing genuine public YouTube comments. The comments are authentic, but completeness depends on YouTube's API and the tool's upkeep, so treat a null result as "not found here", not proof of absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hadzy-com |
