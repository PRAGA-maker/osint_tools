---
id: rebel-news
name: Rebel News
description: Use when you have a `name` tied to Canadian right-wing politics/activism and want to search a partisan outlet's coverage for mentions, footage, or event context — returns `social-profile` / `name` corroboration.
url: https://www.rebelnews.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a subject's appearances, quotes, or event footage in Canadian right-wing/populist media coverage that mainstream outlets did not carry.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Articles and videos are free to read/watch; some content solicits donations or membership but is not hard-paywalled for viewing.
opsec: passive
opsecNote: Reading and searching the site is passive and reveals nothing to your subject. Treat the outlet's framing as partisan — verify any factual claim elsewhere before relying on it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A partisan Canadian media/activist outlet; useful only as a primary record of what it published (who appeared, when, where), not as a neutral factual source. Corroborate everything.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- RebelNews
- Rebel Media
tags:
- toddington
- news-journalism
- canada
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Rebel News

> A Canadian right-wing media/activist outlet — searchable as a *primary record* of protests, rallies, and figures it covered, not as an impartial news source.

## When to use
Your subject is connected to Canadian populist/right-wing politics, protest movements (e.g. convoy-style events), or activism, and you want to know whether they appeared in Rebel News coverage — named in an article, filmed at an event, quoted, or profiled. Because the outlet documents gatherings and personalities that legacy media often skip, its footage/reporting can place a `name` at a specific time and event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.rebelnews.com.
2. Use the site search (or a scoped engine query `site:rebelnews.com "Full Name"`) for your subject's `name`.
3. Review matching articles and videos for date, location, event, associates in frame, and any linked social accounts.
4. Note the publication date and event — that is the corroborating fact, independent of the outlet's spin.
5. Pivot: a named associate or an on-screen handle → social/username tools; an event + date → other coverage of the same event for cross-confirmation.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` / event corroboration, occasional `social-profile` links, video footage placing a person at a time/place
- **Empty/negative result looks like:** no matching articles or videos — simply means this outlet didn't cover the subject; not evidence of anything.

## Gotchas & OpSec
- Heavily partisan: use it for *what it published and when*, never as a neutral factual authority. Cross-check every claim.
- Passive; no interaction reaches the subject.
- Content is editorial/advocacy — be alert to selective framing when interpreting footage.

## Overlaps ("do both")
- Pairs with mainstream news-archive searches — running the same `name`/event against neutral outlets separates verifiable fact from partisan framing.

## Trust & verifiability
`trust: unverified` — treat as a partisan primary source. Its value is documentary (it recorded X at event Y on date Z); always corroborate the underlying facts elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rebel-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
