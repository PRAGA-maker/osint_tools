---
id: uvrx
name: UVRX Social Search
description: Use when you have a person `name` or `username` and want to search across many social networks at once through one Google-custom-search front-end — returns social-profile links.
url: http://www.uvrx.com/social.html
category: social-networks
path:
- social-networks
bestFor: One-box search across Facebook, LinkedIn, Twitter, Instagram, Tumblr and more via a Google custom search.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; it's a Google Custom Search front-end, no account or payment required.
opsec: passive
opsecNote: Searches run through Google's index, so you never touch the target's profiles and nobody is alerted. Opening any profile the results surface is a separate active step — do that from a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing free community tool built on Google Custom Search; only as fresh and complete as Google's index of each platform.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- urvx
- urvx-com
aliases:
- uvrx.com
- UVRX Social Search
tags:
- social-media-search
- meta-search
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# UVRX Social Search

> A one-box meta-search that fires a `name` or `username` across many social platforms at once using Google Custom Search.

## When to use
You have a subject's `name` or `username` and want a fast first sweep of their social footprint without querying each network individually. UVRX bundles Google custom-search engines for Facebook, LinkedIn, Twitter/X, Instagram, Tumblr, LiveJournal and more, so a single query returns cross-platform `social-profile` leads to triage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.uvrx.com/social.html.
2. Enter the target `name` (in quotes for exact match) or `username`; optionally pick a specific network tab (there are dedicated pages, e.g. the Facebook custom search).
3. Read the results — they render as Google search hits scoped to social domains; each hit is a candidate profile.
4. Pivot: open promising profiles from a sock-puppet, confirm identity, and feed handles/images into deeper per-platform tools.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` links across multiple networks
- **Empty/negative result looks like:** few or no hits — means Google hasn't indexed matching public profiles under that term, not that the person has no accounts; try name variants and quotes.

## Gotchas & OpSec
- It only reaches what Google has indexed; privacy-locked or noindexed profiles won't appear.
- Because it's a Google CSE, results overlap heavily with a manual `site:` dork — its value is convenience, not unique coverage.
- OpSec: passive (queries hit Google, not the target); heavy use may trigger a Google CAPTCHA.

## Overlaps ("do both")
- Pairs with a targeted dork like `[[company-or-organisation]]` and dedicated username tools — UVRX gives the broad first pass, those go deep on a confirmed handle or employer.

## Trust & verifiability
`trust: community` — a durable free community tool riding on Google's index; reliable as far as Google's coverage goes, so treat empty results as "not indexed," not "does not exist."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uvrx |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
