---
id: social-profiles-finder
name: Social Profiles Finder
description: Use when you have a `name` or `username` and want to surface a person's public social profiles across major networks in one place — returns social-profile links and display names.
url: https://www.social-searcher.com/search-users/
category: social-networks
path:
- social-networks
bestFor: A free, no-login sweep of indexed public social profiles for a name or handle across many networks at once.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: The users-search feature is free with no registration and no daily cap. (Social Searcher's separate real-time keyword monitoring has paid tiers, but profile/user search is free.)
opsec: passive
opsecNote: It only queries what search engines have already indexed — you are not touching the target's accounts, and the subject is not notified. Passive; still run it from a sock-puppet browser to keep the query out of your own ad/search profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Social Searcher, a commercial social-monitoring service; results are limited to publicly indexed content and need manual confirmation that a profile is the right person.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Social Searcher Users Search
- social-searcher.com users search
tags:
- social-networks
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Social Profiles Finder

> Social Searcher's free "users" search: enter a name or handle and it gathers the public profiles, posts, and mentions that search engines have already indexed into one view.

## When to use
You have a `name` or a `username` and want a fast, free, no-account first pass at a subject's cross-network public presence — profiles and mentions on Instagram, Facebook, TikTok, LinkedIn, Reddit, X/Twitter, YouTube and others, plus blogs/forums. Good early-stage breadth step to decide which platforms to investigate deeply.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.social-searcher.com/search-users/ (or `/users-search`) in a sock-puppet browser.
2. Enter the subject's `name` or `username`.
3. Read the aggregated hits: profile links and mentions grouped by network. Open each candidate profile directly to confirm it is your subject, not a same-name/same-handle stranger.
4. Pivot: a confirmed profile's display `name` feeds people-search; a confirmed handle feeds `[[user-sherlock]]` and username-variant expansion (`[[username-generation-guide]]`) for platforms not indexed here.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` links across networks, display `name`, plus indexed public mentions
- **Empty/negative result looks like:** few or no indexed hits — which for a private or low-footprint person means "not indexed," not "no accounts." It cannot see private accounts, DMs, or anything behind a login.

## Gotchas & OpSec
- Index-limited: results are only what search engines have already crawled, so recent or privacy-restricted profiles are invisible here.
- Disambiguation is on you: common names return many unrelated profiles; verify each before attributing.

## Overlaps ("do both")
- Pairs with `[[user-sherlock]]` — this finds indexed public profiles by name/handle, while a namechecker brute-tests a specific handle against site-by-site account existence, catching accounts search engines never indexed.

## Trust & verifiability
`trust: community` — a commercial aggregator surfacing indexed public content; treat each profile as a lead to confirm by opening it, not as an attributed fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-profiles-finder |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
