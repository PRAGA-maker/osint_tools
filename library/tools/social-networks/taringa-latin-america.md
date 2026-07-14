---
id: taringa-latin-america
name: Taringa (Latin America)
description: Use when you have a `name`/`username` tied to Latin America and want historical posts/profiles from the defunct Taringa network — returns archived social-profile leads.
url: http://www.taringa.net
category: social-networks
path:
- social-networks
bestFor: Recovering historical Hispanophone social-media activity from Taringa, which closed in 2024 — now an archive-only source.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: The live site is shut down; archived copies (Wayback Machine, ArchiveTeam) are free to access.
opsec: passive
opsecNote: You are querying web archives, not a live platform, so there is nothing target-facing to leak. Standard passive-browsing hygiene through an archive front-end.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Taringa was a genuine, major Latin American social network (once the region's #2 by traffic) but ceased operating on 25 March 2024; only archived data remains, so completeness is not guaranteed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- web-archive-org
aliases:
- Taringa!
- taringa.net
tags:
- major-social-networks
- latin-america
- defunct
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Taringa (Latin America)

> Once Latin America's second-biggest social network, Taringa shut down in March 2024 — reach for it only through web archives, as a source of historical Hispanophone profiles and posts.

## When to use
You have a `name` or `username` for a subject active in the Spanish-speaking Americas (especially Argentina) in the 2008–2018 window, and you need their older social footprint. Taringa hosted 27M+ registered users sharing daily posts; that history can still be recovered from archives even though the live site is gone. Treat it as a cold-case / historical-timeline source, not a current-activity check.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do NOT expect `taringa.net` to load — it closed on 25 March 2024.
2. Query the Wayback Machine (`web.archive.org`) for `taringa.net/<username>` or profile/post URLs, and check ArchiveTeam's Taringa grabs.
3. Read archived profiles/posts for handles, linked accounts, locations, dates and associates.
4. Pivot: recovered `username`/links feed cross-platform username search; named associates and locations feed the rest of the case.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** archived `social-profile` content (posts, handles, linked accounts)
- **Empty/negative result looks like:** the archive never captured that profile/URL — very common, since crawls are incomplete. Absence in the archive is not proof the account never existed.

## Gotchas & OpSec
- The platform is dead; anyone pointing you to a "live" Taringa lookup is mistaken or running a clone — verify against archives.
- Archive coverage is patchy and frozen in time; dates reflect capture, not necessarily posting.
- OpSec: passive; you touch archives, not the subject.

## Overlaps ("do both")
- Pairs with `[[web-archive-org]]` (the actual retrieval mechanism here) and with cross-platform username tools to carry any recovered handle forward to still-live networks.

## Trust & verifiability
`trust: community` — the underlying network was real and significant, but with the site defunct every result depends on third-party archive fidelity; corroborate before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | taringa-latin-america |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
