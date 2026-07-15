---
id: google-com
name: "Bluesky Google dork (site:bsky.app)"
description: Use when you have a `username`/`name`/phrase and want to find Bluesky profiles and posts via Google — a `site:bsky.app` dork that returns `social-profile` and post links.
url: https://www.google.com/search?client=firefox-b-d&q=site%3Absky.app
category: social-networks
path:
- social-networks
bestFor: Surfacing Bluesky profiles and posts through Google's index using a site: dork.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free — a Google search with a `site:` operator; no account.
opsec: passive
opsecNote: The dork runs against Google, not Bluesky, so it is passive toward the target. Opening a bsky.app profile is where you may be observed — do it logged out. Bluesky posts are largely public/federated, but treat the click-through as the active step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A saved Google query, not a data source of its own — coverage depends on how much of bsky.app Google has indexed, which changes over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- google-com-86
- searchenginejournal-com
aliases:
- bluesky google dork
- site:bsky.app
tags:
- bluesky
- BlueSky / BSky Related Sites
- google-dorking
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Bluesky Google dork (site:bsky.app)

> A pre-built Google dork — `site:bsky.app` — that surfaces Bluesky profiles and posts through Google, useful because Bluesky's own search is limited and Google indexes public bsky.app pages.

## When to use
You want to find a subject's Bluesky presence, or public Bluesky posts mentioning a `name`/topic, and you'd rather leverage Google's index than Bluesky's weaker native search. Add the handle or a phrase to the base dork to target it: `site:bsky.app "displayname"` or `site:bsky.app "search phrase"`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL, or run `site:bsky.app` in Google.
2. Append your selector to focus it, e.g. `site:bsky.app "Jane Doe"`, `site:bsky.app/profile/ jane`, or a quoted phrase from a post.
3. Review the indexed profile (`/profile/...`) and post (`/post/...`) URLs in the results.
4. Open a profile logged out to read the public feed.
5. Pivot: a confirmed handle feeds cross-platform username enumeration; Bluesky DIDs/handles can be resolved further with Bluesky-specific tools.

## Inputs → Outputs
- **In:** `username` / `name` / phrase (as query terms)
- **Out:** Bluesky `social-profile` and post URLs, with `name`/handle mentions
- **Empty/negative result looks like:** few results — Google's coverage of bsky.app is partial and lags, so a thin result set reflects the index, not necessarily absence. Cross-check with Bluesky's native search and a firehose/atproto tool.

## Gotchas & OpSec
- Index-dependent: Google indexes only part of Bluesky and with delay; treat a null as inconclusive.
- Handles on Bluesky can change while the DID stays constant — a stale dork may miss a renamed account.
- The dork finds pages; reading feeds still means visiting bsky.app — do so without your real account for sensitive work.

## Overlaps ("do both")
- Pairs with `[[google-com-86]]` (same technique for Snapchat) and `[[searchenginejournal-com]]` for operator syntax; also run Bluesky-native and atproto tools, which see content Google hasn't indexed.

## Trust & verifiability
`trust: community` — a search recipe, not a data source; verify by opening the actual Bluesky profile and corroborating identity from its posts and links.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
