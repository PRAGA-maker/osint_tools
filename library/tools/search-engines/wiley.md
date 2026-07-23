---
id: wiley
name: Wiley Online Library
description: Use when you have a `name` (an author) or research topic and want scholarly articles and books that tie a person to a field, institution, and co-authors — returns affiliation and `associate` leads.
url: https://www.wiley.com
category: search-engines
path:
- search-engines
bestFor: Searching Wiley's journals and books to anchor an academic name to affiliations, co-authors, and dates.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
status: live
pricing: freemium
costNote: Searching and reading abstracts/author metadata is free on onlinelibrary.wiley.com; most full-text is paywalled or needs institutional access.
opsec: passive
opsecNote: Passive keyword search of a public academic publisher. Wiley logs searches under your session/IP; use a clean browser for sensitive queries. No contact with the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: John Wiley & Sons is a major, long-established academic publisher; the Wiley Online Library carries authoritative bibliographic metadata.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- oxford-journals
- academic-journals
- google-scholar
aliases:
- Wiley
- Wiley Online Library
- onlinelibrary.wiley.com
tags:
- academic-resources-and-grey-literature
- scholarly-search
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Wiley Online Library

> John Wiley & Sons' scholarly platform — journals and books that yield authoritative author affiliations, co-authorship networks, and publication timelines.

## When to use
You have a `name` that may belong to a researcher, clinician, engineer, or scholar and want to confirm and enrich it: what they publish, the institution they list, who they co-author with, and when. Publication records give a durable, hard-to-fake trail of a person's professional identity and network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the Wiley Online Library search at https://onlinelibrary.wiley.com (linked from https://www.wiley.com).
2. Enter the author `name` (quoted) plus a discipline or keyword to disambiguate.
3. Open matching results and read the free front matter: author list, affiliations, corresponding-author institution/email, and publication date.
4. Record co-authors (`associate` leads) and the affiliation (`employer-org`).
5. Pivot: co-authors and affiliations feed people-search and institutional directories; corroborate across `[[google-scholar]]` and `[[oxford-journals]]`.

## Inputs → Outputs
- **In:** `name` (author) or topic
- **Out:** author affiliations (`employer-org`), co-author (`associate`) lists, publication dates, corresponding-author contact hints
- **Empty/negative result looks like:** no article hits — the person likely doesn't publish with Wiley; check Scholar or another publisher.

## Gotchas & OpSec
- Full text is usually paywalled; the free abstract + author metadata is normally sufficient for identity/affiliation work.
- Common names collide — disambiguate with field, institution, or a known co-author before attributing a paper.
- OpSec: passive; searches are logged by Wiley. Use a clean browser for sensitive queries.

## Overlaps ("do both")
- Pairs with `[[google-scholar]]`, `[[oxford-journals]]`, and `[[academic-journals]]` — Scholar spans all publishers with citation graphs, while Wiley gives its own authoritative first-party metadata; run both so you don't miss non-Wiley work.

## Trust & verifiability
`trust: trusted` — a major, long-established academic publisher; the bibliographic and affiliation metadata are authoritative even where full text is paywalled.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wiley |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
