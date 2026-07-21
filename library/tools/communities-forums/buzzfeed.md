---
id: buzzfeed
name: BuzzFeed / BuzzFeed News archive
description: Use when you have a `name` and want to check whether a person was profiled or named in BuzzFeed's viral or investigative coverage — returns article mentions and associate leads.
url: http://www.buzzfeed.com/?country=us
category: communities-forums
path:
- communities-forums
bestFor: Checking a subject against BuzzFeed's viral culture and (archived) investigative journalism.
selectorsIn:
- name
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free to read; no account required. BuzzFeed News (the investigative arm) shut down in 2023, but its archive remains online.
opsec: passive
opsecNote: Reading published articles is fully passive and reveals nothing to the subject; use site-scoped web search rather than any on-site account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A mass-media publisher; its former BuzzFeed News unit did award-winning investigations, but general BuzzFeed content is entertainment, not vetted record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- BuzzFeed
- BuzzFeed News
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# BuzzFeed / BuzzFeed News archive

> A large-audience media site whose (now-archived) BuzzFeed News unit produced serious investigative journalism alongside viral culture content — occasionally the only public write-up naming a person.

## When to use
A minor, corroborating news source. When a `name` may have surfaced in viral coverage or in a BuzzFeed News investigation (data journalism, extremism, tech, missing-persons features), a search can surface an article that names the person, quotes associates, or links their social profiles. Treat it as one media source among many, strongest for people tied to internet culture or stories BuzzFeed News covered.

## How to use it (`bestInteractionPattern`: web-manual)
1. Run a site-scoped search: `site:buzzfeed.com "Full Name"` (and `site:buzzfeednews.com` for the investigative archive).
2. Open matching articles; note how the subject is described and who is quoted alongside them.
3. Follow any embedded social links or named `associate`s.
4. Cross-check facts against the article's own sourcing and other outlets.
5. Pivot: named associates and linked profiles feed people- and social-search.

## Inputs → Outputs
- **In:** `name` (person, handle, or topic)
- **Out:** article mentions, quoted `associate`s, embedded `social-profile` links
- **Empty/negative result looks like:** no articles — expected for most people, since coverage is selective; absence means "not covered," not exonerating.

## Gotchas & OpSec
- Mixed reliability: separate BuzzFeed News investigations (edited, sourced) from viral/listicle content (entertainment).
- BuzzFeed News closed in 2023; use the archive and web caches for its older reporting.
- OpSec: passive; prefer a search engine over browsing logged-in.

## Overlaps ("do both")
- Pairs with mainstream news search and Google — BuzzFeed occasionally covers internet-culture figures other outlets ignore, but always corroborate elsewhere.

## Trust & verifiability
`trust: community` — a publisher, not a record; its journalism arm was credible, but treat any single article as a lead to verify against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buzzfeed |
| category | communities-forums |
| selectorsIn → selectorsOut | name → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
