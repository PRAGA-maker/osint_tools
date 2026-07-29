---
id: netflix-codes-com
name: netflix-codes.com
description: Use when you need Netflix's hidden genre/category codes to browse its catalogue by micro-genre — a reference index of streaming metadata, not a people-search tool.
url: https://netflix-codes.com
category: communities-forums
path:
- communities-forums
bestFor: Looking up Netflix's secret genre codes to reach niche category listings not shown in the normal menu.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free reference site; the codes themselves are used on your own Netflix account (which requires a subscription to view content).
opsec: passive
opsecNote: The code directory is a static public reference and reveals nothing about any subject. Actually browsing the genres happens inside your own logged-in Netflix session — use your own/sock account, not a target's.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained catalogue of Netflix's genre codes; unofficial and dependent on Netflix not changing the scheme.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Netflix secret codes
- Netflix genre codes
tags:
- Movies
- Netflix
- reference
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# netflix-codes.com

> A reference index of Netflix's hidden genre codes — a streaming-metadata lookup, with only tangential OSINT value.

## When to use
Niche and marginal: you want to browse Netflix by a micro-genre it doesn't surface in the normal UI (e.g. a specific national cinema or sub-genre), typically for media-research or content-context tasks rather than investigating a person. It returns catalogue metadata (category codes), not any selector about a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://netflix-codes.com and browse or search the category you want.
2. Copy the numeric code for that micro-genre.
3. In your own logged-in Netflix session, go to `https://netflix.com/browse/genre/<code>` to see that hidden category's listings.
4. Use the resulting catalogue view for content/media research.

## Inputs → Outputs
- **In:** none (a genre you want to reach)
- **Out:** Netflix genre code(s) and the corresponding hidden category listing
- **Empty/negative result looks like:** a code that returns an empty Netflix page — the genre may be region-locked or retired, since codes are unofficial and can break.

## Gotchas & OpSec
- Unofficial: Netflix can change or remove the code scheme at any time, and availability is region-dependent.
- Not an investigative tool — it yields no personal data; include it only for media/content-context work.
- Requires your own Netflix login to actually view the categories; never use a target's account.

## Overlaps ("do both")
- Sits alongside general streaming/media reference resources; there's no identity-OSINT tool it meaningfully pairs with.

## Trust & verifiability
`trust: community` — a community-maintained mirror of Netflix's internal genre taxonomy; accurate when Netflix's scheme is stable, but unofficial and unverifiable against a first-party source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netflix-codes-com |
| category | communities-forums |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
