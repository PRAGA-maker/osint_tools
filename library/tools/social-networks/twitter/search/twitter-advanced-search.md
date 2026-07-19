---
id: twitter-advanced-search
name: Twitter/X Advanced Search
description: Use when you have a `username`, `name` or keywords and want precisely-filtered public posts — returns tweets narrowed by account, date, location and content.
url: https://twitter.com/search-advanced
category: social-networks
path:
- social-networks
- twitter
- search
bestFor: Pinpoint discovery of specific public tweets using native operators (from/to account, exact dates, phrases, media, location).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free native feature. X now generally requires being logged in to run searches, so a (free) account is effectively needed.
opsec: passive
opsecNote: Searching does not interact with target accounts or notify them. Because X requires login, searches occur under whatever account you're signed into — use a sock-puppet account, not your real one, and never follow/like from it while investigating.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Twitter/X's own first-party search — the authoritative source for its public posts. Coverage of older tweets can be incomplete, and login is now required.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- memory-lol
- global-terriorism-database
- murph-live
- parrot-security
- tormap
- twitter
- twitter-analytics
- twitter-com
- twitter-date-search
- twitter-image-search
- twitter-name-search-twitter-name-search
- twitter-x-location-search
aliases:
- X Advanced Search
- Twitter search operators
tags:
- twitter
- x
- advanced-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Twitter/X Advanced Search

> Twitter/X's built-in advanced search: slice public posts down to a single account, date window, phrase, place, or media type — the native precision tool for tweet discovery.

## When to use
You have a subject's `username` (or a `name`/keywords) and want *specific* public posts, not a firehose: everything they said in a date range, tweets mentioning a place or person, exact phrases, replies to someone, or posts with media/geolocation. Because it uses X's own index, it's the most authoritative way to find and cite a public tweet, and its operators let you build very targeted queries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign into a **sock-puppet** X account (search now generally requires login) and open https://twitter.com/search-advanced.
2. Fill the form (or type operators directly): `from:handle`, `to:handle`, `"exact phrase"`, `since:YYYY-MM-DD until:YYYY-MM-DD`, `filter:media`, `near:"city" within:10km`, `-filter:replies`, etc.
3. Run it and read the result set — sort between "Top" and "Latest."
4. Refine iteratively: tighten dates, add/remove operators, combine account + keyword.
5. Pivot: geotagged posts (`geolocation`) feed mapping; referenced accounts feed further profiling; an old handle from `[[memory-lol]]` can be searched here for pre-rename content.

## Inputs → Outputs
- **In:** `username`/`name` + operators (dates, phrases, place, media)
- **Out:** filtered public tweets → `social-profile` activity and `geolocation` (from geotagged posts)
- **Empty/negative result looks like:** no tweets. Note that X's search index does not reliably surface very old tweets, deleted content is gone, and protected accounts won't appear — an empty result can mean "not indexed," not "never posted."

## Gotchas & OpSec
- **Login required:** X now gates search behind an account — use a sock puppet, never your real profile.
- Historical coverage is patchy; for old/deleted tweets, combine with archive tools.
- Operators are powerful but finicky — verify date filters actually applied.
- OpSec: passive toward targets, but everything runs under your logged-in account; do not interact (follow/like) while investigating.

## Overlaps ("do both")
- Pairs with `[[memory-lol]]` — recover prior handles there, then search each here for content posted before a rename. Combine with archived-tweet/Wayback tools for deleted or un-indexed posts.

## Trust & verifiability
`trust: trusted` — this is X's first-party search, so returned posts are authoritative. The caveats are coverage (old tweets under-indexed) and the login requirement, not data authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-advanced-search |
</content>
