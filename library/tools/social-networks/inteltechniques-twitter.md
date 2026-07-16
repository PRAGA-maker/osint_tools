---
id: inteltechniques-twitter
name: IntelTechniques Twitter/X Search Tool
description: Use when you have an X/Twitter `username` or `name` and want to run advanced searches across many operators at once — returns profile, posts, media, and network leads.
url: https://inteltechniques.com/tools/Twitter.html
category: social-networks
path:
- social-networks
bestFor: A one-page launcher for advanced X/Twitter searches (posts, media, dates, location, network) around a handle.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- geolocation
status: degraded
pricing: free
costNote: Free to use (part of the maintained IntelTechniques tools, updated Nov 2024). Effectiveness is capped by X's own restrictions — since X locked down search and its API, some query types that need login or the API return little.
opsec: passive
opsecNote: The tool only builds and opens X/Twitter search URLs — it holds no data and never contacts the subject. When a query opens X, do so in a sock-puppet-logged-in browser if X demands a login; your searches are then attributed to that account, not you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A reputable query launcher by Michael Bazzell; it dispatches to X's own search, so results depend entirely on what X currently exposes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- IntelTechniques Twitter
- Bazzell Twitter tool
- X search tool
tags:
- twitter
- x
- advanced-search
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- email-assumptions
- email-search-tool-by-inteltechniques
- google-document-dorks-inteltechniques-method
- instagram-search-inteltechniques-method
- instagram-tool-inteltechniques-com
- inteltechniques-business-search-tool
- inteltechniques-facebook
- inteltechniques-osint
- inteltechniques-telephone
- inteltechniques-tools-search-engines-suite
- user-name-search-intel-techniques
---

# IntelTechniques Twitter/X Search Tool

> Michael Bazzell's X/Twitter launcher — enter a handle or term and it builds the advanced searches (by date, media, location, keyword, network) that X's own UI buries.

## When to use
You have an X/Twitter `username` or a `name`/keyword and want to interrogate the account or topic with the full range of search operators — posts within a date range, media-only, geotagged, replies, from/to a handle — without hand-writing each `from:`/`since:`/`until:`/`filter:` query. Useful for building a timeline, finding a subject's media (faces, locations), and mapping who they talk to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://inteltechniques.com/tools/Twitter.html`.
2. Enter the handle/name/keyword; fill optional fields (dates, location, media).
3. Click a query type — it opens X's search pre-built with the right operators.
4. Because X now gates much of search behind login, run the opened queries in a **sock-puppet** X session for best coverage.
5. Pivot: media posts → faces/locations for reverse-image (`[[yandex-images]]`) and `geolocation`; frequent interlocutors → `associate`; the handle → cross-platform `[[nexfil]]`.

## Inputs → Outputs
- **In:** `username`, `name`/keyword
- **Out:** `social-profile` (X account/results), `image` (media posts), `geolocation` (geotagged posts), network/interaction leads
- **Empty/negative result looks like:** X returns few/no results — increasingly common since X restricted search and requires login for many queries. A thin result reflects X's limits, not necessarily the subject's absence.

## Gotchas & OpSec
- Degraded by platform: X's post-API lockdown means several query types now need a login or return little; don't read emptiness as fact.
- It's a launcher — results are X's; the tool just builds the URL.
- OpSec: **passive** toward the subject; if X forces a login, use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[nexfil]]` and reverse-image tools — this drives deep X search; username enumeration finds the same handle elsewhere and reverse-image ties X media to other accounts.

## Trust & verifiability
`trust: community` — a reputable launcher; the data is X's own, so verify on X and account for how much X now hides behind login.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inteltechniques-twitter |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
