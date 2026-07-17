---
id: aol-search-databse
name: AOL Search Log Database (search-id)
description: Use when you have an AOL-era `username`/anonymised user-id or a distinctive `name`/place and want to mine the leaked 2006 AOL search logs — returns a person's search queries as a behavioural/identity lead.
url: https://search-id.com
category: search-engines
path:
- search-engines
bestFor: Searching the notorious 2006 AOL query-log leak (~650k users, ~20M searches) by keyword or user id to reconstruct what an individual searched for.
selectorsIn:
- name
- username
selectorsOut:
- name
- address
status: degraded
pricing: free
costNote: Free to search. search-id.com now redirects to searchids.com; the front-end was intermittently unreachable at last check (Cloudflare 522), so availability is not guaranteed.
opsec: passive
opsecNote: You query a static historical dataset, not any live person — nothing reaches a subject. Remember this is leaked private data from 2006; handle ethically and within your legal authority, and treat "personality analysis" features as speculative.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party front-end over the 2006 AOL data leak; the underlying dataset is authentic and historically documented, but this particular mirror's uptime and completeness are not guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- search-id
- searchids.com
- AOL Stalker
tags:
- toddington
- specialty-search
- historical-leak
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# AOL Search Log Database (search-id)

> A searchable window into the 2006 AOL search-log leak — the (in)famous release of ~20M queries from ~650k anonymised users, browsable by keyword or user id.

## When to use
Strictly a historical/cold-case aid: if your subject was an AOL user around 2006 and you can tie them to a distinctive search behaviour, real name, or place name that would appear in queries, this dataset can reconstruct their search history. AOL only "anonymised" users to numeric ids, and many were re-identified because people searched their own names, addresses, and neighbours — so a user-id can leak identity. Niche, but occasionally decisive for old cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search-id.com (redirects to searchids.com). If it is down (a Cloudflare 522 has been seen), retry later or use an alternate mirror of the AOL dataset.
2. Search by keyword (a `name`, town, phone, or distinctive term) to find queries containing it, or by numeric user id to pull one user's full query stream.
3. Read a user's queries as a behavioural profile — self-searches, local place names, and repeated terms often re-identify the person.
4. Cross-reference distinctive queries (an address, an employer, a rare name) against other records.
5. Pivot: a re-identified `name`/`address` → people-search and public-records tools; a locale → geographically-scoped searches.

## Inputs → Outputs
- **In:** `name`, `username`/user-id, or distinctive keyword
- **Out:** the matching AOL search queries; via self-searches, often a re-identified `name`/`address`
- **Empty/negative result looks like:** no matching queries — the term simply isn't in the 2006 dataset, or this mirror is incomplete/offline. Absence says nothing about the person today.

## Gotchas & OpSec
- **Frozen in 2006:** nothing after the leak; useless for current activity. Treat strictly as historical.
- Ethically sensitive leaked personal data — use only within your legal authority; the "personality analysis" framing is speculative, not evidence.
- Mirror reliability is shaky (redirects, intermittent 522s); have a fallback copy of the dataset.

## Overlaps ("do both")
- Pairs with contemporary people-search tools — this supplies a 2006 behavioural snapshot / re-identified name, which you then bring forward with present-day address and records lookups.

## Trust & verifiability
`trust: unverified` — the dataset is authentic and well documented, but this front-end's uptime and completeness are not guaranteed. Corroborate any re-identification against an independent source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aol-search-databse |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → name, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
