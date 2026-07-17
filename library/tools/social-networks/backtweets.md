---
id: backtweets
name: Backtweets
description: Use when you have a `domain`/URL or `username` and want archived tweets that linked back to it — returns social-profile handles and tweet references.
url: http://backtweets.com
category: social-networks
path:
- social-networks
bestFor: Finding which Twitter accounts historically tweeted a link to a given URL/domain, as a frozen backlink-style tweet archive.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to search; no account required.
opsec: passive
opsecNote: You query a third-party tweet archive, not Twitter/X or the subject, so nothing is disclosed to the target. Use a research browser; plain HTTP site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A relaunched remnant of the original BackType/Twitter-era service; its index is frozen (largely pre-2012) and no longer reflects the live Twitter/X firehose, so treat it as a historical archive only.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- backtweets.com
tags:
- twitter
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Backtweets

> A frozen tweet archive that answers "who tweeted a link to this URL" — historical Twitter backlinks, not live search.

## When to use
You want to know which Twitter accounts historically shared a link to a specific `domain`/URL, or to find old tweets tied to a handle — for building a picture of a subject's past web presence or the accounts that amplified a site. Because the index is frozen (largely the original BackType era, pre-2012), use it as a historical/archival lead source, not for anything recent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://backtweets.com.
2. Enter a URL/`domain` (to find tweets that linked to it) or a handle/keyword.
3. Review returned tweets and the accounts (`social-profile`) that posted them.
4. Note any handles and linked pages as historical pivots.
5. Pivot: take a discovered Twitter handle into a live X search or username-search tool; take linked domains into WHOIS/archive lookups.

## Inputs → Outputs
- **In:** `domain`/URL, `username`, or keyword
- **Out:** archived tweets and the `social-profile` handles that posted them
- **Empty/negative result looks like:** no matches — expected for anything post-2012 or low-volume; absence is not evidence, given the frozen index.

## Gotchas & OpSec
- The archive is stale (`status: degraded`) — it does not see modern Twitter/X activity, so never use it to conclude something didn't happen recently.
- Availability is intermittent and the site is plain HTTP.
- Coverage was always link-centric (who linked a URL), so it is strongest for URL/domain queries, weaker as a general tweet search.

## Overlaps ("do both")
- Pairs with a live X/Twitter advanced search — Backtweets covers the frozen historical tail, live search covers the present.

## Trust & verifiability
`trust: unverified` — a relaunched remnant of a defunct service with a frozen, opaque index; useful only as a historical lead, and every hit should be confirmed against the archived tweet or Wayback.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | backtweets |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
