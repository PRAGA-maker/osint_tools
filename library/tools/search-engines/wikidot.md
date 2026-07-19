---
id: wikidot
name: Wikidot
description: Use when you have a `username` or topic and want content or profiles hosted on the Wikidot wiki farm — returns wiki pages and author profiles.
url: http://www.wikidot.com
category: search-engines
path:
- search-engines
bestFor: Finding niche community wikis and their contributor profiles across the Wikidot hosting platform.
selectorsIn:
- username
- name
selectorsOut:
- username
- social-profile
status: live
pricing: freemium
costNote: Free to read all public wikis and to view member profiles; Pro features start at about $4/month but are not needed for OSINT reading.
opsec: passive
opsecNote: Browsing public Wikidot pages and profiles is passive. Creating an account to reach members-only areas is logged; use a sock puppet if you must join a wiki.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A hosting platform, not a data source — content quality depends entirely on the individual wiki's community; treat user-authored pages as unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- wikidot.com
tags:
- toddington
- curated-directory
- specialty-search
- wiki
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Wikidot

> A free wiki-hosting farm running 100M+ pages; for OSINT it matters as a place to search for niche community content and to enumerate a `username`'s contributor profile and edit history.

## When to use
Your subject participates in a hobbyist, fan, gaming, or special-interest community, and that community runs its site on Wikidot. Use it two ways: (1) as a content source to read wikis a person contributes to, and (2) as a `username` enumeration surface — Wikidot member profiles and per-page author/edit attributions can tie a handle to activity, timing, and interests.

## How to use it (`bestInteractionPattern`: web-manual)
1. To find a member: try `http://www.wikidot.com/user:info/<username>` or search the platform for the handle; a hit gives a profile with join date, karma, and wikis they belong to.
2. To find content: because Wikidot's own search is weak, use a search engine with `site:wikidot.com <term>` (or `site:<subdomain>.wikidot.com`) to locate relevant wikis and pages.
3. Open a wiki page and check its history/discussion tab for author usernames, timestamps, and edit comments.
4. Note recurring handles, avatars, and the topics they edit — these are pivots to other platforms.
5. Pivot: run the discovered `username` through cross-platform username checkers; use the topic focus to guide further community searches.

## Inputs → Outputs
- **In:** `username` (or a topic/`name`)
- **Out:** member profile, wikis joined, page authorship/edit history, `social-profile`-style handle links
- **Empty/negative result looks like:** `user:info` returns no such member, or `site:wikidot.com` searches surface nothing relevant — the subject likely isn't active on this platform. Absence here says little given how many other wiki hosts exist.

## Gotchas & OpSec
- Native search is poor; rely on external `site:` queries to actually find content.
- It's a platform, not a vetted source — anyone can create a wiki, so content is unverified and can be abandoned or spammy.
- Low individual-locator value: most useful for corroborating a handle and interests, not for finding an address.
- OpSec: reading is passive; joining a wiki with an account is logged — use a sock puppet.

## Overlaps ("do both")
- Complements general username-enumeration tools — Wikidot is one more platform to check a handle against, and its edit histories add timing/interest context a bare username checker won't show.

## Trust & verifiability
`trust: community` — Wikidot only hosts; the reliability of anything you find is that of the specific wiki's authors, so corroborate claims elsewhere and treat handles as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikidot |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → username, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
