---
id: posthaven
name: Posthaven
description: Use when you have a `name`, `username` or `email` and want to check for a personal blog on Posthaven — returns blog posts revealing biography, `associate` and location context.
url: https://posthaven.com
category: communities-forums
path:
- communities-forums
bestFor: Finding and reading a subject's Posthaven blog for self-published biographical detail.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- associate
- geolocation
status: live
pricing: freemium
costNote: Reading public Posthaven blogs is free; publishing a blog is a paid subscription (irrelevant to OSINT reading).
opsec: passive
opsecNote: Reading public blog posts is passive and invisible to the author. Don't comment or subscribe from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Posthaven is a legitimate long-term blog host (successor to Posterous); content is self-published by the blogger, so it's first-person but unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- posthaven.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- blog
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Posthaven

> A durable personal-blog host ("posts forever," the successor to Posterous) — a place a subject may have self-published biography, opinions, and life detail.

## When to use
You have a `name`, `username`, or `email` and want to find a subject's personal blog. Self-published blogs are gold for OSINT: people disclose their own timeline, relationships, locations, employers, and opinions in their own words. Posthaven's selling point is permanence, so old posts persist. Reach for this when a subject is the blogging type and you want first-person material.

## How to use it (`bestInteractionPattern`: web-manual)
1. Guess likely subdomains (`<handle>.posthaven.com`) from known usernames, or
2. Dork a search engine: `site:posthaven.com "<name>"` / `"<username>"` / `"<email>"`.
3. Open matching blogs and read posts for self-disclosed biography, relationships, and locations.
4. Note names, places, and dates mentioned in the writing.
5. Pivot: mentioned people become `associate` leads; stated places feed geolocation; the blog's style/handle links to other platforms.

## Inputs → Outputs
- **In:** `name`, `username`, or `email`
- **Out:** blog posts → biographical detail, `associate`s, `geolocation`, linked `social-profile`s
- **Empty/negative result looks like:** no blog found — most people don't have a Posthaven; absence just means try other blog platforms, not that the subject doesn't blog.

## Gotchas & OpSec
- No strong native search: reach content via search-engine dorks or subdomain guessing.
- Self-published = unverified: treat claims as the author's assertions, corroborate facts.
- OpSec: passive; never interact (comment/subscribe) from an attributable identity.

## Overlaps ("do both")
- Pairs with other blog-platform searches (Medium, WordPress, Blogger) and username-search — run the same selectors across platforms since you don't know which host a subject chose.

## Trust & verifiability
`trust: unverified` — a legitimate blog host, but the content is self-published by the subject; reliable as a record of what they chose to say, not as independently verified fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | posthaven |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username, email → social-profile, associate, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
