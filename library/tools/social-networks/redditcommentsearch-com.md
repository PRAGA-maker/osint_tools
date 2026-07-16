---
id: redditcommentsearch-com
name: redditcommentsearch.com
description: Use when you have a Reddit `username` and want to keyword-filter that user's entire comment history — returns matching comments revealing location, employer, and habits.
url: http://redditcommentsearch.com
category: social-networks
path:
- social-networks
bestFor: Searching one Reddit user's comment history for a keyword (e.g. a city, employer, or name) to surface self-disclosures.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free single-purpose web tool; no account. Bounded by Reddit's API limits on how many comments it can pull.
opsec: passive
opsecNote: The tool queries Reddit's public API for already-public comments; the target is not notified. Passive. Use a sock-puppet browser out of habit, though you're only reading public content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small third-party utility over Reddit's public API; results are only as complete as Reddit exposes (recent comments, not deleted ones).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- reddit-comment-search
- search-reddit-comments-by-user
aliases:
- Reddit Comment Search
tags:
- Social Media
- Reddit
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# redditcommentsearch.com

> A focused utility that keyword-filters a single Reddit user's comment history — the fast way to find where in thousands of comments they mentioned a city, job, or name.

## When to use
You have a Reddit `username` (from a bio link, cross-platform reuse, or a username search) and want to mine what they've said. Reddit's native profile view is chronological and unsearchable; this tool lets you grep one user's comments for a term — a hometown, employer, school, pet's name, or a real name they let slip — which is often where OSINT gold hides.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site in a sock-puppet browser.
2. Enter the target Reddit `username` and a search query (a keyword or phrase).
3. Optionally toggle case-sensitivity / whole-word matching.
4. Read the returned comments — each hit shows the comment text and its subreddit/context, exposing self-disclosed details.
5. Pivot: a mentioned city/workplace feeds geolocation and employer verification; subreddit patterns profile interests and routines.

## Inputs → Outputs
- **In:** Reddit `username` + keyword
- **Out:** matching comments (`social-profile` activity) that can reveal `geolocation`, employer, and personal details
- **Empty/negative result looks like:** no comments returned — the user has few/no public comments, the keyword doesn't appear, or the account is deleted/shadow-limited; try broader terms or scan without a filter.

## Gotchas & OpSec
- Only public, non-deleted comments within Reddit's API reach are searchable — deleted or very old comments may be missing (use a Pushshift-style archive for those).
- One user at a time; it doesn't find *which* account is the subject — pair with a username-discovery tool first.
- OpSec: passive read of public data.

## Overlaps ("do both")
- Pairs with `[[reddit-comment-search]]` / `[[search-reddit-comments-by-user]]` and Pushshift-style archives — this covers live comments; archives recover deleted/historical ones the API won't return.

## Trust & verifiability
`trust: community` — a lightweight third-party wrapper over Reddit's public API; the comments are authentic Reddit content, but completeness depends on what Reddit still exposes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redditcommentsearch-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
