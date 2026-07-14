---
id: en-wikipedia-org-4
name: Gab (Wikipedia reference)
description: Use when you have a `username` or `name` possibly active on the alt-tech network Gab and want to understand the platform before pivoting to a profile search — returns platform context that feeds a `social-profile`.
url: https://en.wikipedia.org/wiki/Gab_(social_network)
category: social-networks
path:
- social-networks
bestFor: Orienting on Gab (far-right Twitter alternative) before searching gab.com for a subject's profile and posts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Wikipedia is free; the Gab platform it describes (gab.com) is also free to read publicly, no account needed for most profiles.
opsec: passive
opsecNote: Reading the Wikipedia article is fully passive. When you pivot to gab.com itself, browsing public profiles is low-risk but the platform is small and operator-monitored — use a sock-puppet browser session and do not log in with an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The reference is a Wikipedia article (well-sourced, community-maintained). Treat the described platform (Gab) as the actual data source; Wikipedia is orientation, not the primary record.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Gab
- gab.com
- Gab social network
tags:
- rightwingsocialmediasites
- Right Wing Social Media Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Gab (Wikipedia reference)

> A background reference on Gab — the far-right "alt-tech" Twitter clone — used to decide whether and how to hunt a subject's profile on gab.com.

## When to use
You have a `username` or `name` and suspect the subject participates in far-right / alt-tech online spaces, or a lead trail points to Gab. Start here to understand what Gab is (a Twitter-style microblog founded 2016 by Andrew Torba, ~5M registered accounts but only ~100k active, headquartered in Pennsylvania, widely used by people banned from mainstream platforms), then pivot to searching the live site. Knowing the platform's culture and public-content model tells you what a profile there implies about a subject and what data (public posts, groups, bio) you can expect to recover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the Wikipedia article at the URL for orientation: platform history, moderation stance, the 2021 "GabLeaks" breach (40M+ posts/DMs/profiles leaked to researchers), and current status.
2. Pivot to the live platform to find the actual subject: open `https://gab.com/<username>` in a sock-puppet browser, or run a search-engine dork `site:gab.com "<name>"` / `site:gab.com <username>`.
3. Read the profile (`social-profile`): public posts, join date, groups, display `name`, and linked accounts are visible without login for most profiles.
4. Pivot: a confirmed Gab handle feeds username-reuse checks across other alt-tech sites and cross-references to the GabLeaks dataset if you have authorized research access.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** platform context; on pivot to gab.com, a `social-profile` (posts, bio, groups) and confirmed display `name`
- **Empty/negative result looks like:** no matching handle on gab.com and no `site:gab.com` hits — the subject likely has no Gab presence (or uses an unlinked handle). The Wikipedia article itself never returns a person; it only orients you.

## Gotchas & OpSec
- This card is a reference, not a lookup — do not expect to type a name into Wikipedia and get a subject. The real search happens on gab.com or via a search engine.
- OpSec: passive to read Wikipedia. On gab.com, browse logged-out from a sock-puppet session; the platform is small and its operators are known to monitor and publicize scrutiny.
- The GabLeaks data is sensitive and legally fraught; only touch it under proper authorization.

## Overlaps ("do both")
- Pairs with a username-enumeration sweep (e.g. `[[nqntnqnqmb]]` for LinkedIn or broad username checkers) — those find the handle elsewhere; Gab tells you the alt-tech footprint. Cross-reference display names and post content to confirm it is the same person.

## Trust & verifiability
`trust: trusted` — Wikipedia is a well-sourced community reference for orientation. The authoritative data lives on gab.com; verify any claim about a subject against their actual public posts, not the encyclopedia summary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | en-wikipedia-org-4 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
