---
id: xtorx
name: Xtorx
description: Use when you have a `name` or `username` and want to check whether it surfaces in torrent metadata — returns torrent listings (titles, release handles) aggregated from multiple indexes.
url: https://www.xtorx.com
category: search-engines
path:
- search-engines
bestFor: A quick meta-search across torrent indexes for a keyword, filename, or release handle.
selectorsIn:
- name
- username
selectorsOut:
- username
status: live
pricing: freemium
costNote: Free to search; ad-supported, no account required.
opsec: passive
opsecNote: Searching is passive and does not touch the subject. Do NOT download anything — torrent files can carry malware and downloading reveals your IP to swarm peers and may be unlawful. Treat this strictly as a metadata search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party torrent meta-search aggregating other indexes; results are unmoderated and ad-heavy. Low direct person-finding value.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- xtorx.com
tags:
- Search engines
- Filesharing Search Engines
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Xtorx

> A clean, ad-supported meta-search over multiple torrent indexes — for OSINT it is a narrow metadata check, not a locator.

## When to use
You have a `name`, `username`, or release handle and want to see whether it appears in torrent metadata — e.g. a subject's alias reused as a release-group handle, or leaked/self-distributed content tied to a screen name. This is a fringe pivot with low yield; reach for it only when a filesharing angle is specifically in play, not as a general people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.xtorx.com in a sandboxed/sock-puppet browser (expect aggressive ads and redirect pop-ups — use an ad-blocker).
2. Enter the keyword: a `username`/handle, a `name`, or a filename of interest.
3. Read the aggregated listing — titles, sizes, seed/leech counts, and the source index each result came from.
4. Note release handles or naming patterns; a reused alias is the only real OSINT signal here.
5. Pivot: take a matching `username`/handle back to username-search and social tools. **Do not download.**

## Inputs → Outputs
- **In:** `name`, `username` (as search keywords)
- **Out:** `username` (release/uploader handles that may match a known alias)
- **Empty/negative result looks like:** no listings, or only unrelated media matching the keyword — meaning nothing in indexed torrent metadata ties to the subject.

## Gotchas & OpSec
- Heavy ads, pop-ups, and redirects — use an ad-blocker and never click download/"play now" bait.
- Results are unmoderated and often mislabeled; a keyword match is weak evidence at best.
- Passive only while searching; downloading would expose your IP and carry legal/malware risk — stay at the metadata layer.

## Overlaps ("do both")
- Redundant with other filesharing search engines in this category; if Xtorx is empty, another aggregator may index different sources, so try one alternative before concluding nothing exists.

## Trust & verifiability
`trust: unverified` — an anonymous third-party aggregator; treat any hit as an unconfirmed lead and verify the underlying handle through independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xtorx |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → username |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
