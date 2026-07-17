---
id: digg
name: Digg
description: Use when you have a `name`, `username` or topic and want to see what trending stories and links people have shared/submitted about it — returns aggregated news links and submitter handles.
url: https://digg.com
category: communities-forums
path:
- communities-forums
bestFor: Scanning a curated news-aggregator feed for trending stories or links related to a person, handle, or event.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to browse and search; no account needed to read. An account is only needed to submit or comment.
opsec: passive
opsecNote: Browsing/searching Digg is passive and does not alert anyone. If you log in to comment or submit you create an attributable trail — read-only unless you deliberately engage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A social news aggregator; the site is legitimate but the shared content is user/editor curated, so treat linked stories as leads to their original sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- diggreader
- reddit
aliases:
- digg.com
tags:
- news-journalism
- aggregator
- social-news
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Digg

> A curated social-news aggregator — a lightweight way to see which stories and links the web has surfaced around a name, topic, or event.

## When to use
You want a quick pulse on trending coverage of a subject, event, or topic, or you're chasing what links/discussions have circulated about a `name` or online `username`. Digg surfaces editor- and community-curated stories, so it's a discovery layer that points you to underlying articles and, occasionally, to the handles of people sharing or discussing a subject. It's a supporting/leads source rather than a direct identity resolver.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://digg.com.
2. Use the site search (or a scoped web search `site:digg.com "term"`) for the subject's `name`, handle, or a topic keyword.
3. Read the surfaced stories; note the original outlet each links to and any submitter/commenter handles.
4. Follow through to the primary source — Digg is the pointer, the linked article is the evidence.
5. Pivot: linked articles feed news-archive work; submitter/commenter `username`s feed username-search and `[[reddit]]`-style social pivots.

## Inputs → Outputs
- **In:** `name`, `username`, or topic keyword
- **Out:** aggregated news links, `social-profile`/`username` of submitters, and `name` mentions in coverage
- **Empty/negative result looks like:** few or no results — Digg indexes a curated slice of the web, so most people/topics simply won't appear; absence is not meaningful.

## Gotchas & OpSec
- Coverage is a curated highlight reel, not a comprehensive index — never treat "not on Digg" as significant.
- Content is user/editor selected; always verify against the linked primary source.
- OpSec: passive to browse; don't log in during an investigation.

## Overlaps ("do both")
- Pairs with `[[reddit]]` for a broader, deeper social-discussion index, and with `[[diggreader]]` if you want to follow feeds over time. Digg is the quick-scan curated layer; those are the deep ones.

## Trust & verifiability
`trust: community` — a legitimate aggregator, but the value is in the primary sources it links to. Confirm any claim against the original article, not the Digg summary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digg |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
