---
id: searchisback
name: SearchIsBack
description: Use when you have a `name` plus attributes (location, school, employer, interests) and want to find matching Facebook people, events and posts — returns social-profile leads.
url: https://searchisback.com
category: social-networks
path:
- social-networks
bestFor: Building structured Facebook people/event/post searches by attribute (location, relationship, school, workplace, birth date) — a graph-search-style helper.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free tool. Functionality is intermittently limited because Facebook keeps changing/removing the search surfaces it relies on; the author has repeatedly had to rebuild it.
opsec: passive
opsecNote: SearchIsBack builds a Facebook search URL/query; the actual searching happens on Facebook, so log in with a sock-puppet Facebook account, never your real one. Viewing profiles from a real account risks "People You May Know" correlation with the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent tool that reconstructs Facebook's removed graph-search; reliability tracks Facebook's ever-changing restrictions, so expect breakage.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- intelligence-x
- graph-tips
aliases:
- Search Is Back
- searchisback.com
tags:
- facebook
- facebook-graph-search
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# SearchIsBack

> A Facebook graph-search helper — turn a name plus attributes into structured searches for people, events, posts, and tagged photos.

## When to use
You have a `name` and some attributes (city, school, `employer-org`, interests, relationship status, birth date) and want to find the matching Facebook profile, or discover people/events tied to a place or organisation. It rebuilds the attribute-filtered searching Facebook removed with graph search — valuable when a plain name search returns too many people to sift.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet Facebook account in the same browser.
2. Open https://searchisback.com and fill the People (or Events/Posts/Photos) form: name plus filters like location, school, workplace, gender, birth date.
3. Submit — it constructs and runs the corresponding Facebook search.
4. Read results on Facebook; refine filters to disambiguate.
5. Pivot: a confirmed `social-profile` feeds friend-list/associate mapping and photo analysis.

## Inputs → Outputs
- **In:** `name` + attributes (`employer-org`, school, location, birth date, interests)
- **Out:** `social-profile` (Facebook people/events/posts matching the filters)
- **Empty/negative result looks like:** no results or a Facebook error — increasingly caused by Facebook disabling the underlying search rather than the person's absence. Note the tool's own banners about broken features.

## Gotchas & OpSec
- Degraded by design: Facebook repeatedly breaks these search surfaces; features come and go. Confirm the specific search type still works before trusting a null result.
- Human-in-the-loop: requires a logged-in Facebook session — use a burner account only.
- OpSec: the query runs on Facebook under your session; a real account risks PYMK correlation with the target.

## Overlaps ("do both")
- Pairs with `[[intelligence-x]]` Facebook tools and `[[graph-tips]]` — different reconstructions of Facebook search break at different times, so keep more than one in rotation.

## Trust & verifiability
`trust: community` — a reputable independent tool, but wholly dependent on Facebook's shifting search access; verify each hit directly on Facebook.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchisback |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
