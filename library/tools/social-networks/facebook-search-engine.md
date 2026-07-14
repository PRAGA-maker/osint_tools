---
id: facebook-search-engine
name: Facebook Search Engine
description: Use when you have a `name`/`username` or keyword and want to search public Facebook content via a prebuilt Google Custom Search Engine — returns candidate social-profile hits, coverage permitting.
url: https://cse.google.com/cse?cx=95ae46262a5f2958e
category: social-networks
path:
- social-networks
bestFor: Keyword/name searching of indexed public Facebook content via a Google CSE.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free Google Custom Search Engine. No account needed.
opsec: passive
opsecNote: You query Google's index of Facebook, not Facebook directly — the subject is not notified. Passive; use a sock-puppet session to keep queries out of your own Google profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google CSE; results depend on what Google has indexed of Facebook, which is limited and shrinking as Facebook restricts public indexing.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Facebook CSE
tags:
- facebook
- custom-search-engine
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Search Engine

> A prebuilt Google Custom Search Engine scoped to public Facebook content — a name/keyword dork that reaches whatever Google has indexed of Facebook.

## When to use
You have a `name`, `username`, or keyword and want to find public Facebook profiles, pages, or posts without relying on Facebook's own limited search. Best as one indexed-search angle to surface a candidate profile; Facebook exposes little to search engines, so treat coverage as partial.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at the URL in a sock-puppet browser.
2. Enter a `name`, vanity `username`, or keyword; add a location/employer/school to disambiguate a common name.
3. Read the hits: indexed public Facebook URLs matching your query; open each to confirm identity.
4. Pivot: a found profile URL feeds `[[find-my-facebook-id-3]]` to get the stable numeric ID, then Facebook graph/scraper tools.

## Inputs → Outputs
- **In:** `name` / `username` / keyword
- **Out:** indexed public Facebook `social-profile` hits (profiles, pages, posts)
- **Empty/negative result looks like:** few or no results — expected, since Facebook blocks most public indexing; absence means "not indexed," not that the person has no Facebook.

## Gotchas & OpSec
- CSE decay: Facebook's anti-indexing and stale CSE config mean thin, shrinking coverage — hence `status: degraded`.
- Verify every hit on Facebook itself; indexed snapshots may be old or misattributed.

## Overlaps ("do both")
- Chains into `[[find-my-facebook-id-3]]` (resolve the profile to a numeric ID) and `[[social-profiles-finder]]` (expand across networks) once you have a candidate profile.

## Trust & verifiability
`trust: community` — an unofficial Google CSE; value is convenience, and every result must be confirmed on the live platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
