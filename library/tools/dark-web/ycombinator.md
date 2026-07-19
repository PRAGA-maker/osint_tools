---
id: ycombinator
name: Hacker News (Y Combinator)
description: Use when you have a `username` (or name) in the tech world and want their Hacker News posts/comments — returns a `social-profile` and a searchable trail of opinions, links and disclosures.
url: https://news.ycombinator.com/ask
category: dark-web
path:
- dark-web
bestFor: Searching Hacker News for a tech-adjacent subject's posts, comments, and profile — often candid disclosures about employers, projects, and locations.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- employer-org
- associate
status: live
pricing: free
costNote: Free to read and search; no account required to browse (only to post/comment).
opsec: passive
opsecNote: Reading HN is passive. The best search route (Algolia HN Search) queries a third party, not the user. Stay logged out; use a sock-puppet browser if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Hacker News is a legitimate, widely used tech community run by Y Combinator; posts are genuine user content, but identities are self-asserted handles — corroborate before attributing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Hacker News
- HN
- news.ycombinator.com
tags:
- toddington
- curated-directory
- tech-community
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Hacker News (Y Combinator)

> The Y Combinator tech community forum — for a developer/founder/tech-adjacent subject, their Hacker News trail can be a candid record of employers, projects, opinions, and location hints.

## When to use
Your subject works in or around tech (engineer, founder, researcher) and may use Hacker News. HN comments are often unusually candid — people mention their employer, city, side projects, and views. Given a `username` (or `name`), you can pull their profile and full comment history to corroborate identity, infer `employer-org`/location, and find `associate`s from interactions.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you have the exact handle, open `https://news.ycombinator.com/user?id=<username>` for their profile (karma, account age, about text).
2. To search content, use HN Search (Algolia): `https://hn.algolia.com/` — query the `name`, handle, employer, or a distinctive phrase.
3. Read comment history for disclosures: employer, city/time zone, projects, other handles/links.
4. The "Ask HN" section (this entry's URL) is where people post questions/discussions — useful for topical threads.
5. Pivot: linked sites/handles → username enumeration; stated employer → company OSINT; interacting users → `associate` leads.

## Inputs → Outputs
- **In:** `username` or `name` (tech-adjacent subject)
- **Out:** HN `social-profile`, comment history revealing `employer-org`, location hints, and `associate` interactions
- **Empty/negative result looks like:** no profile/comments for the handle — the subject isn't on HN (most people aren't). A common handle may also belong to someone else; verify by content.

## Gotchas & OpSec
- Niche audience — only relevant for tech-adjacent subjects.
- Handles are self-asserted; confirm identity via corroborating detail, not name collision.
- Use HN Search (Algolia) for reliable full-text search — the on-site search is limited.

## Overlaps ("do both")
- Pairs with GitHub analytics like `[[open-source-software-insight]]` and cross-platform username search — HN adds candid prose/opinions, while GitHub adds code activity, together painting a fuller developer profile.

## Trust & verifiability
`trust: community` — a legitimate, long-running community; content is real, but attribution rests on self-asserted handles, so corroborate any identity link before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ycombinator |
| category | dark-web |
| selectorsIn → selectorsOut | username, name → social-profile, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
