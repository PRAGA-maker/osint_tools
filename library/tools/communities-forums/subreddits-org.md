---
id: subreddits-org
name: Subreddits.org
description: Use when you have a topic or `name`/keyword and want to find the relevant Reddit communities to monitor — returns matching subreddits as `social-profile` leads.
url: http://subreddits.org
category: communities-forums
path:
- communities-forums
bestFor: Discovering the right subreddits on a topic so you know which communities to search or monitor.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free searchable directory of subreddits; no account, no payment.
opsec: passive
opsecNote: Browsing the directory touches only subreddits.org, not Reddit or any subject — no exposure. Actually reading the subreddits it points you to is a separate, direct Reddit visit; use a sock-puppet Reddit session for that step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent third-party directory of Reddit communities; a convenient discovery index, not affiliated with Reddit and not an authoritative or exhaustive list.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- subreddits
aliases:
- Subreddits
tags:
- reddit
- directory
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# Subreddits.org

> A searchable, topic-categorized directory of Reddit communities — the fastest way to find *which* subreddits matter for a subject before you dig into Reddit itself.

## When to use
You're investigating a person, place, hobby, scam, or event and want to know where on Reddit the relevant conversation happens — which niche communities to search, monitor, or lurk in. Subreddits.org turns a topic or `name`/keyword into a shortlist of communities, so you aren't guessing subreddit names or missing a small-but-central one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://subreddits.org.
2. Search a keyword/topic (or the subject's interest, location, employer, hobby) or browse the categorized sections (technology, gaming, life, music, etc.).
3. Read the returned list of subreddits with their focus/size.
4. Note the promising communities.
5. Pivot: take each subreddit into a Reddit-search tool or Reddit itself and look for the subject's `username`, posts, or local knowledge — do that step from a sock-puppet account.

## Inputs → Outputs
- **In:** topic / interest / `name` keyword
- **Out:** a list of relevant subreddits → `social-profile` (community) leads to search next
- **Empty/negative result looks like:** few or no listed communities for a niche term — the directory isn't exhaustive, so fall back to Reddit's own search rather than concluding no community exists.

## Gotchas & OpSec
- It's a discovery index, not people-search — it points you to communities, it does not find a person. The real work happens once you enter those subreddits.
- Coverage is a curated snapshot and can lag new or renamed subreddits.
- OpSec: passive to browse; the follow-on Reddit reading is a direct visit — use a throwaway Reddit session, don't upvote/comment from an attributable account.

## Overlaps ("do both")
- Pairs with `[[subreddits]]` and dedicated Reddit-search/scraping tools — this finds *which* communities to look at, and those tools search *inside* them for the subject's activity.

## Trust & verifiability
`trust: unverified` — a handy independent directory with no stated maintenance guarantees; treat its list as a starting map of Reddit, not a definitive one.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subreddits-org |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
