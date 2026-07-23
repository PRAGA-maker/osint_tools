---
id: hacker-news-algolia
name: Hacker News Search (Algolia)
description: Use when you have a `name`, `username`, `domain`, or product and want every Hacker News post/comment mentioning it — returns dated mentions, HN handles, and linked profiles.
url: https://hn.algolia.com/
category: search-engines
path:
- search-engines
bestFor: Full-text search of all Hacker News posts and comments to surface mentions of a person, handle, company, or domain.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free full-text HN search powered by Algolia; no account. A free public API mirrors every query.
opsec: passive
opsecNote: Passive search of a public archive; the HN users you find are not notified. Queries hit Algolia's servers — use a clean browser for sensitive terms. Reading a user's HN profile is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Hacker News search, run by Algolia in partnership with Y Combinator; indexes the authentic HN corpus.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-advanced-search
aliases:
- HN Search
- Algolia HN
- hn.algolia.com
tags:
- Search engines
- Bugbounty/vulnerabilities search tools
- hacker-news
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Hacker News Search (Algolia)

> Full-text search over the entire Hacker News archive — the fastest way to find everything the tech community (and often a subject themselves) has said about a person, handle, company, or domain.

## When to use
Your subject is plausibly in tech — a developer, founder, or someone active in startup/security circles. HN often surfaces a person's own `username`, their `employer-org`, projects they launched (Show HN), job posts naming them, and candid comments. Search a `name`, `username`, `domain`, or company to pull every dated mention and the HN handles attached.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://hn.algolia.com/.
2. Enter the query; toggle **Stories** vs **Comments** and sort by **Date** or **Popularity**. Use the filters (date range, author) to narrow.
3. Read hits for the poster's HN `username`, linked profiles, employer mentions, and "Who is hiring / Who wants to be hired" threads (which often contain real names, emails, and CVs).
4. Click a username to open their HN profile — some list a real name, email, website, or social links.
5. Pivot: an HN handle → username-search across platforms; a linked personal site/email → domain/email OSINT. For programmatic pulls, hit the free API `http://hn.algolia.com/api/v1/search?query=...`.

## Inputs → Outputs
- **In:** `name`, `username`, `domain`, or product/company
- **Out:** dated HN posts/comments, poster `username`s and profile links (`social-profile`), employer/affiliation mentions (`employer-org`), self-posted contact details
- **Empty/negative result looks like:** no hits — the subject likely has no HN footprint; try a broader term or a different community.

## Gotchas & OpSec
- Only indexes Hacker News — absence here says nothing about other platforms.
- HN usernames are pseudonymous; a matching handle isn't proof of identity without corroboration.
- OpSec: passive; queries go to Algolia. The API is unauthenticated and rate-limited but ideal for bulk/automated searches.

## Overlaps ("do both")
- Pairs with `[[google-advanced-search]]` — a `site:news.ycombinator.com` dork catches things Algolia ranks low, while Algolia gives structured author/date filtering; run both for full coverage.

## Trust & verifiability
`trust: trusted` — the official HN search built by Algolia with Y Combinator; it indexes the genuine, unaltered Hacker News corpus, so mentions are authentic (identity attribution still needs corroboration).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hacker-news-algolia |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, domain → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
