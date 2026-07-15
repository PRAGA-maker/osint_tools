---
id: graph-tips-fb-search
name: Graph Tips FB Search
description: Use when you have a `name`/`username` and want to search Facebook for a person, their photos, places and connections — returns Facebook profiles, images and associates via a rebuilt graph-search interface.
url: https://graph.tips/beta
category: social-networks
path:
- social-networks
bestFor: Running structured Facebook people/photo/place/post searches after Facebook removed native Graph Search.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Completely free and open-source; no account or payment for the query-builder itself (you view results on Facebook, which may prompt its own login).
opsec: active
opsecNote: The tool only builds/redirects the query, but clicking through runs the search on Facebook while you are (or aren't) logged in. Use a sock-puppet Facebook account and browser — Facebook logs searches and profile views against whatever session you use, never your real account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by @sowdust (also known as whopostedwhat.com), widely cited across 23+ OSINT source lists; experimental and dependent on Facebook's ever-changing search behaviour.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- graph.tips
- whopostedwhat
- Facebook graph search
tags:
- facebook
- graph-search
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Graph Tips FB Search

> @sowdust's free rebuild of Facebook Graph Search — a query interface that lets you search Facebook by person, photo, place, post and connection after Facebook killed native graph search.

## When to use
You have a `name` or `username` (or an entity/place/date) and want to interrogate Facebook the way the old Graph Search allowed: people filtered by city/school/employer, photos taken at or of a location, posts mentioning a term in a date range, or the events/pages someone is tied to. Invaluable for missing-persons work, where Facebook's own search bar deliberately hides these pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool at https://graph.tips/ (the working entry point; the `/beta` path may 404).
2. Pick a search type — People, Posts, Photos, Places, Videos, Events, Pages.
3. Fill the filters (name, city, school, employer, location, date range) and submit; the tool constructs the Facebook search and sends you to the results.
4. Read the results on Facebook and pivot: profiles feed username/associate mapping, photos feed reverse-image/face tools, place-tagged results feed geolocation work.

## Inputs → Outputs
- **In:** `name` / `username` (plus optional city, school, employer, place, date)
- **Out:** `social-profile` (Facebook profiles/pages), `image` (tagged photos), `associate` (friends/mutuals, co-tagged people)
- **Empty/negative result looks like:** Facebook returning "no results," a login wall, or a stripped-down result set — Facebook has narrowed graph-search over time, so a blank result may reflect its restrictions rather than genuine absence. Re-try alternate filters before concluding.

## Gotchas & OpSec
- **Facebook does the searching**, so an active, logged-in session is effectively required for most result types — always use a sock-puppet account (`account-login` human-in-loop).
- Experimental & moving target: Facebook periodically breaks these query patterns; if one search type returns nothing, others may still work.
- The security note from the author applies: don't paste ID values from untrusted sources into the tool.

## Overlaps ("do both")
- Pairs with [[sowdust-fb-search]] (the same author's SOWsearch, now at sowsearch.info) and other Facebook search front ends — run both, since each tracks Facebook's changes slightly differently and one often works when the other is broken.

## Trust & verifiability
`trust: community` — a respected open-source community tool, but it only *reaches into* Facebook; result accuracy and completeness are entirely Facebook's, and the interface is admittedly experimental. Verify any hit on the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | graph-tips-fb-search |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
