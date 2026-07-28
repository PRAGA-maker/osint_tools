---
id: mailing-list-archives-search-engine
name: Mailing List Archives Search Engine
description: Use when you have a `name`/`email`/keyword and want their posts in public mailing-list archives — returns matching list threads and messages.
url: https://cse.google.com/cse/publicurl?cx=013991603413798772546:sipriovnbxq
category: search-engines
path:
- search-engines
bestFor: Searching across many public mailing-list archives at once for a person's posts or an email address.
selectorsIn:
- name
- email
selectorsOut:
- email
- social-profile
status: degraded
pricing: free
costNote: Free Google Custom Search Engine; no account needed to search.
opsec: passive
opsecNote: Passive — results are served from Google's index, so you never touch the mailing-list servers directly and the subject gets no signal. Standard Google-query hygiene (puppet browser) applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Google Custom Search Engine over a curated set of list archives; coverage is defined by whoever built the CSE and can drift or break over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- mailing list search
- listserv archive search
tags:
- mailing-lists
- google-cse
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Mailing List Archives Search Engine

> A Google Custom Search Engine scoped to public mailing-list archives — find where a `name`, `email`, or handle has posted to technical/community lists.

## When to use
Public mailing lists (open-source projects, technical communities, listservs) are a rich, often-overlooked source: people post under real names and real email addresses, sometimes for decades. When you have a `name` or `email` and want their list activity — or want to confirm an address is real and see how it's used — this CSE searches across many archives at once instead of one at a time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (a Google Custom Search Engine over mailing-list archives).
2. Search the `email`, full `name`, or a distinctive keyword; quote exact phrases.
3. Read hits: each links to an archived message showing the poster's display name, address, timestamp, and thread context.
4. Pivot: a confirmed archival `email` feeds breach/username lookups; recurring co-posters feed `associate` mapping; signatures often leak employer, location, or PGP keys.

## Inputs → Outputs
- **In:** `name`, `email`, or keyword
- **Out:** archived list messages exposing `email`, display name, and `social-profile`-style context (project affiliation, signature details)
- **Empty/negative result looks like:** no hits — the person may not post to lists in this CSE's scope; try a broader Google `site:` search or a specific project's own archive.

## Gotchas & OpSec
- It's a CSE with a fixed, curator-defined scope — coverage is partial and can silently degrade if the config or indexed sites change; treat gaps as "not covered here," not "doesn't exist."
- Archives are old — an address that posted years ago may be dead now.
- Corroborate a claimed identity: mailing lists can carry spoofed From-headers.

## Overlaps ("do both")
- Pairs with direct Google `site:` dorking of a specific archive (e.g. `site:lists.debian.org`) — the CSE casts wide, while a targeted dork goes deep on one list.

## Trust & verifiability
`trust: community` — a third-party Google CSE; the underlying archived messages are as trustworthy as their host, but the search scope is opaque and maintained by an unknown curator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailing-list-archives-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, email → email, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
