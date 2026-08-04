---
id: proboards
name: ProBoards
description: Use when you have a `username`, `name`, or topic and want to find hosted community forums and member profiles across the largest free forum platform — returns `social-profile`s and community discussions.
url: https://www.proboards.com
category: communities-forums
path:
- communities-forums
bestFor: Discovering niche community forums and their public member profiles/posts via the ProBoards directory.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free forum-hosting platform; browsing public forums and the directory needs no account (posting/messaging does).
opsec: passive
opsecNote: Reading public forums and profiles is passive and doesn't alert members. The moment you register or message a member it becomes active and identity-linked — use a sock-puppet account and never interact from your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A large, legitimate forum host (3M+ forums, 22M+ users); content is user-generated and unverified, and individual forums may be private or require registration.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Proboards forums
- proboards.com
tags:
- forums
- communities
- user-profiles
source: metaosint
lastVerified: '2026-08-04'
enrichment: full
---

# ProBoards

> The largest free forum host (millions of niche communities) — a hunting ground for a subject's forum footprint, member profile, and post history.

## When to use
You have a `username`, `name`, or a niche interest/topic and want to find where the subject participates in community discussion. ProBoards hosts millions of small special-interest forums; a reused handle there can expose a profile, join date, post history, and interests that other platforms don't surface. Reach for it when a subject's mainstream social presence is thin but they're likely active in a hobbyist/fan community.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the ProBoards forum **directory** and general web search (`site:proboards.com "<username>"`) to find forums and member pages.
2. Open a member's public profile: look for join date, post count, signature (often full of external links/handles), and recent posts.
3. Read post history for interests, location tells, and reused aliases.
4. To go deeper (private boards, messaging) you must register — do so with a sock puppet.
5. Pivot: a reused `username` cross-checks against username-enumeration tools; profile links feed further social OSINT.

## Inputs → Outputs
- **In:** `username` or `name` (or topic)
- **Out:** `social-profile` (member pages, post history), reused `username`s
- **Empty/negative result looks like:** no matching member/forum — the handle isn't on ProBoards, or the relevant board is private; try search-operator variants before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: reaching private boards or messaging requires an account (`account-login`) — always a sock puppet.
- Content is user-generated and unverified; corroborate any claim from a post.
- Site-wide member search is limited; Google `site:` dorks are usually the fastest way in.

## Overlaps ("do both")
- Pairs with cross-platform username tools and forum-search engines: ProBoards covers its own huge forum ecosystem, while a username checker tells you where else the same handle lives — do both to map a subject's full community footprint.

## Trust & verifiability
`trust: community` — a legitimate, long-running platform, but everything on it is user-generated; treat profiles and posts as leads to verify, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proboards |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
