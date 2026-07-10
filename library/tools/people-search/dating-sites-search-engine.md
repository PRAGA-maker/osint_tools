---
id: dating-sites-search-engine
name: Dating Sites Search Engine
description: Use when you have a `name`, `username` or `email` and want to sweep multiple dating platforms at once via a curated Google Custom Search Engine — returns `social-profile` links on dating sites.
url: https://cse.google.com/cse?cx=c7b340447e1e12653
category: people-search
path:
- people-search
bestFor: Running one query across a pre-selected list of dating/hookup sites (Google CSE) to find a subject's dating-profile presence.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free — it's a hosted Google Custom Search Engine. No account needed.
opsec: passive
opsecNote: You query Google's index, not the dating sites, so no target profile is touched or notified. Clicking through to a dating profile may register a view on some platforms — open results in a puppet browser/incognito, not while logged into any dating account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community-built Google Custom Search Engine; its site list and freshness are opaque and can drift or break silently, since it depends entirely on Google's index and the (unknown) creator's config.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- dating CSE
- dating sites search
tags:
- people-search
- dating
- google-cse
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Dating Sites Search Engine

> A Google Custom Search Engine scoped to a curated list of dating/hookup platforms — one query to check whether a subject has a dating profile without hitting each site individually.

## When to use
You have a `name`, `username`, or `email` fragment and want to know whether the subject appears on dating platforms — a rich source of photos, self-described location, age, and habits that people rarely lock down. Dating profiles are high-value in relationship, fraud, and missing-person contexts. Use this CSE to fan one query across many sites Google has indexed, then verify hits directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cse.google.com/cse?cx=c7b340447e1e12653 in a clean/puppet browser.
2. Enter the selector — a `username` or distinctive display name works best; a full `name` or an `email`/handle fragment also works. Quote exact phrases.
3. Read results: they are Google-indexed pages on the CSE's dating-site list (`social-profile` hits). Click through only in an incognito/puppet session.
4. Refine: add a city, age, or second term to disambiguate common names.
5. Pivot: a found profile → reverse-image the profile photo, extract stated location/age, and cross-match the username elsewhere.

## Inputs → Outputs
- **In:** `name`, `username`, or `email` fragment
- **Out:** `social-profile` (dating-site pages Google has indexed)
- **Empty/negative result looks like:** zero results — but because CSEs only see what Google has crawled *and* what the site allows indexing (many dating sites block crawlers behind login), a blank result is weak evidence of absence, not proof. Confirm with an on-platform search where possible.

## Gotchas & OpSec
- **Opaque and fragile:** you can't see which sites the CSE covers or when it was last tuned; a stale CSE can silently return nothing. Treat it as one probe among several, not authoritative.
- Many dating platforms hide profiles behind login and block search engines, so the biggest sites may be under-represented here.
- OpSec: passive at the Google layer; opening a profile can leave a footprint on the dating site — use a puppet browser and never a logged-in dating account.

## Overlaps ("do both")
- Pairs with username-enumeration tools that check dating handles directly, and with reverse-image search on any profile photo you find — the CSE finds candidates; those confirm identity.
- Cross-check any hit on the platform itself, since indexed cache may be outdated.

## Trust & verifiability
`trust: unverified` — a third-party Google CSE with an undisclosed, possibly stale site list. Results are real Google-indexed pages, but coverage and freshness are unknowable; verify every hit directly on the source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dating-sites-search-engine |
| category | people-search |
| selectorsIn → selectorsOut | name, username, email → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
