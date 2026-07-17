---
id: built-with-flarum
name: Built With Flarum
description: Use when you want to discover forums/communities to search — a showcase directory of live discussion boards running the Flarum software, browsable by name and topic.
url: https://builtwithflarum.com/
category: communities-forums
path:
- communities-forums
bestFor: Finding niche discussion forums (Flarum-powered) that a subject might post on, to search for their `username`.
selectorsIn: []
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free public showcase; no account needed to browse the directory.
opsec: passive
opsecNote: Browsing the directory is passive and reveals nothing about your target. OPSEC comes into play only when you then visit and search the individual forums it lists — register there with a sock puppet if a forum needs login to search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run showcase of the Flarum ecosystem; it lists real live forums but is a curated/self-submitted directory, not exhaustive.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BuiltWithFlarum
- builtwithflarum.com
tags:
- forums-and-discussion-boards-search
- flarum
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Built With Flarum

> A showcase directory of forums running Flarum — a way to *discover* the niche discussion boards where a subject might be active, so you can go search them for their handle.

## When to use
Forum posts are a rich OSINT source, but you first have to know which forums to look at. Built With Flarum lists live communities built on the Flarum forum platform, grouped/searchable by topic, so it's useful in the discovery phase: if your subject's interests point at a niche community (a hobby, game, tech stack, region), this directory helps you find candidate Flarum boards to then search for their `username`. It's a pivot-to-forums index, not a people search itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://builtwithflarum.com/ and browse or filter the showcased forums by theme/name.
2. Shortlist boards matching your subject's interests, language or region.
3. Visit each shortlisted forum and search it for the subject's `username`/`name` (Flarum forums have on-site search; also try `site:<forumdomain> "<handle>"` in a search engine).
4. On any hit, read the member's profile and post history for selectors (location clues, other handles, `associate`s, timestamps → routine).
5. Pivot: confirmed handles feed username tools; the forum `domain`s feed further site-specific dorking.

## Inputs → Outputs
- **In:** — (browse by topic/interest; you supply the subject's interests, not a selector)
- **Out:** a list of live forum `domain`s to search, and — after you search them — candidate `social-profile`s/posts
- **Empty/negative result looks like:** no directory entry fits your subject's niche — Flarum is only one of many forum engines, so absence just means "look at boards on other platforms" (phpBB, Discourse, XenForo, etc.), not that no forum exists.

## Gotchas & OpSec
- Only covers Flarum-based forums and only those submitted/curated into the showcase — far from a complete forum index.
- It's a discovery aid; the actual OSINT happens on the forums it points to, where login/OPSEC rules apply.
- Board membership changes; a listed forum may have moved platforms or gone offline.

## Overlaps ("do both")
- Complements search-engine dorking and username tools: use it to *find* forums, then run your handle across them. Pair with other forum-directory/discussion-board search resources for platforms beyond Flarum.

## Trust & verifiability
`trust: community` — a genuine, community-maintained showcase of the Flarum ecosystem. The forums it lists are real and live, but the directory is curated/self-submitted and non-exhaustive, so treat it as a starting set, not the full universe of relevant forums.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | built-with-flarum |
| category | communities-forums |
| selectorsIn → selectorsOut |  → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
