---
id: mastodon-search-engine
name: Mastodon Search Engine
description: Use when you have a `username`, `name`, or keyword and want to find posts/profiles across the Mastodon fediverse — returns `social-profile` and post mentions via a scoped Google Custom Search.
url: https://cse.google.com/cse?cx=334aec4c3c73ed945
category: social-networks
path:
- social-networks
bestFor: Keyword/handle search across many Mastodon instances at once, since Mastodon has no global search.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account needed to run a query.
opsec: passive
opsecNote: Passive — you query Google's index of public Mastodon pages, not any instance directly, so no fediverse account is notified. Only Google sees your search terms. Clicking through to a profile is a normal public web visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained Google Custom Search Engine scoped to a curated set of Mastodon instances; coverage depends on which instances the CSE includes and on Google's index, so it is inherently partial.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Mastodon CSE
- fediverse search
tags:
- mastodon
- fediverse
- custom-search
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Mastodon Search Engine

> A Google Custom Search Engine scoped to Mastodon instances — a workaround for the fediverse's deliberate lack of global search, letting you sweep many servers for a handle or keyword at once.

## When to use
You have a `username`, real `name`, or keyword and want to find where it appears across Mastodon. Because Mastodon intentionally has no cross-instance full-text search, finding a person or topic normally means guessing the right server. Reach for this CSE to search Google's index of public Mastodon pages spanning many instances in one query — useful for locating a subject's fediverse profile or public posts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=334aec4c3c73ed945.
2. Enter the target `username` (with or without `@instance`), real name, or a distinctive keyword.
3. Review results — public profile pages (`instance/@user`) and post permalinks across the included instances.
4. Click through to the profile/post on its home instance to confirm and read context.
5. Pivot: a confirmed handle feeds cross-platform username checks; profile text/links can expose other accounts, a real name, or a location.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword
- **Out:** `social-profile` links and public post URLs across indexed Mastodon instances
- **Empty/negative result looks like:** no hits — the person may be on an instance the CSE doesn't cover, may have a non-public profile, or simply isn't indexed by Google; absence is not proof.

## Gotchas & OpSec
- Coverage is doubly limited: by which instances the CSE is configured to include *and* by Google's index freshness — expect gaps, and CSE configs can drift/degrade over time.
- Only public content is searchable; followers-only and private posts never appear.
- OpSec: passive; only Google sees your query.

## Overlaps ("do both")
- Complements native single-instance search and dedicated fediverse tools — use this to *find* which instance a handle lives on, then that instance's own search for depth. Cross-check with a general username enumerator for non-Mastodon accounts.

## Trust & verifiability
`trust: community` — a third-party Google CSE with no guarantee of complete instance coverage; the profile/post pages it links are authoritative, so always click through and verify on the home instance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mastodon-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
