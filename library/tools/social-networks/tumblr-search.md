---
id: tumblr-search
name: Tumblr Search
description: Use when you have a `username`, `name` or keyword and want related Tumblr blogs and posts — returns social-profile and username leads.
url: http://www.tumblr.com/search
category: social-networks
path:
- social-networks
bestFor: Searching Tumblr's public posts and tags to find a subject's blog, aliases, or interest-based communities.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to search; viewing all results and adult-flagged content may prompt a login.
opsec: passive
opsecNote: Searching public Tumblr content is passive and doesn't notify anyone. Browsing while logged in ties views to your account and can surface you in "who to follow"/analytics — use a sock-puppet account or logged-out browsing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: First-party on-site search of a major blogging platform; results are real Tumblr content, though the ranking is opaque and tag-driven.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- tumblr
- tumblr-com
aliases:
- tumblr.com/search
tags:
- tumblr
- social-media-search
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Tumblr Search

> Tumblr's built-in search over public posts and tags — a way to find a subject's blog, recover aliases, and map the interest communities they post in.

## When to use
You have a `username`, a real `name`, or a distinctive keyword/handle and want to see if the subject has a Tumblr presence or posts in a given community. Tumblr skews toward fandom, art, and identity-community content; searching a handle or a distinctive phrase they use can surface a blog, reblog trail, or tag network that links back to them. Good for alias discovery and interest profiling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.tumblr.com/search and enter the term. For a specific person, try the exact `username` and known handle variants.
2. To reach a suspected blog directly, try `https://<username>.tumblr.com` (the classic blog URL form).
3. Filter results by tags vs. posts; scan reblogs and the blog's "following"/tags for `associate` and interest leads.
4. Note: Google dorking `site:tumblr.com "<term>"` often beats on-site search for precision.
5. Pivot: a found blog's cross-posted links, shared usernames, or bio → other platforms; recurring tags → community mapping.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword/phrase
- **Out:** matching Tumblr blogs/posts (`social-profile`), handle variants (`username`), tag/interest context
- **Empty/negative result looks like:** no relevant blogs/posts — the term isn't used publicly on Tumblr, the blog is private/deactivated, or the handle differs; try dorking and handle variants before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: adult-flagged blogs and some results require a logged-in account to view — use a sock puppet.
- On-site search ranking is opaque and tag-weighted; a search-engine `site:tumblr.com` dork is often more reliable for finding a specific person.
- Deactivated/private blogs vanish from search but may persist in web archives.
- OpSec: passive; avoid logging in with a real account.

## Overlaps ("do both")
- Pairs with `[[tumblr]]` / `[[tumblr-com]]` (platform-level tooling) and username-enumeration tools — Tumblr search confirms the blog, a username checker confirms the same handle elsewhere.

## Trust & verifiability
`trust: community` — first-party platform search returning genuine Tumblr content; the content is authentic even if ranking is opaque, so verify a blog is the right person via corroborating detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tumblr-search |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
