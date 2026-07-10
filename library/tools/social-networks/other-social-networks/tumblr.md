---
id: tumblr
name: Tumblr
description: Use when you have a `username`, tag or keyword and want Tumblr content/blogs — returns public posts, blogs and user profiles matching the tag or search term.
url: https://www.tumblr.com/tagged/search
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Finding Tumblr blogs and posts by tag/keyword, and inspecting a known blog's public content.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to browse public blogs and tag/search results; an account is only needed to follow/interact (not to read public content).
opsec: passive
opsecNote: Browsing public blogs and tag search doesn't notify the blogger and isn't tied to a user unless you log in. Tumblr has no "who viewed" for logged-out browsing; if you must log in, use a sock-puppet account. Note asks/messages are active and attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An authentic major blogging/social platform; content is user-generated and pseudonymous, and its search/tag surface is imperfect, so it's a lead source rather than authoritative.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Tumblr
- tumblr.com
tags:
- major-social-networks
- blogging
- tag-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Tumblr

> A pseudonymous blogging network — find a subject's blog by handle, or surface content and communities by tag/keyword.

## When to use
Your subject may keep a Tumblr, or you want to find content/communities around a topic, fandom, or interest they're tied to. Tumblr blogs are often long-lived and candid (interests, art, personal writing, location hints) under a pseudonymous handle — valuable for building a personality/interest picture and for finding a handle that reuses across platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open a known blog directly at `https://www.tumblr.com/<username>` (or the legacy `<username>.tumblr.com`), or use tag search at https://www.tumblr.com/tagged/search.
2. For discovery, search a tag/keyword (interest, location, event) to surface public posts and the blogs behind them.
3. Read a blog's public posts, its "About"/description, linked sites, and reblog network.
4. Note the reblog/interaction graph as `associate`/interest signals.
5. Pivot: the handle feeds `[[user-searcher]]`/`[[instant-username]]`; linked sites feed domain/WHOIS; images feed `[[reverse-image-search]]`; content gives interests/locations.

## Inputs → Outputs
- **In:** `username` (blog), tag, or keyword
- **Out:** public posts, blog `social-profile`, display `name`/description, linked accounts and reblog network
- **Empty/negative result looks like:** no blog at the handle, or thin tag results — the person isn't on Tumblr under that handle, the blog is deleted/private, or tag search (which is partial) missed it. Absence is not conclusive.

## Gotchas & OpSec
- **Pseudonymous by norm** — real names are rare; treat Tumblr as an interest/behaviour source and a handle-to-cross-reference, not an identity source.
- Tag/search coverage is imperfect and flagged-content may be hidden; try direct handle URLs and external search (`site:tumblr.com`).
- OpSec: **passive** when logged out; sending an "ask" is active and attributable — don't. Use a sock puppet if you log in.

## Overlaps ("do both")
- Pairs with `site:tumblr.com` search engine dorks and username tools (`[[user-searcher]]`) — external search often finds Tumblr content its own search misses, and username tools tie the handle to other platforms. Do both.

## Trust & verifiability
`trust: community` — an authentic platform, but pseudonymous and user-generated; verify identity by cross-referencing the handle, linked sites, and image matches rather than trusting a blog's self-description.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tumblr |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
