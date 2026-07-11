---
id: lullar-com-3-appspot-com
name: Lullar Profile Search
description: Use when you have an `email`, `username`, or `name` and want to sweep 175+ platforms for matching public profiles in one query — returns social-profile and name.
url: https://lullar-com-3.appspot.com/en
category: people-search
path:
- people-search
bestFor: One-shot parallel profile lookup across 175+ social/web platforms by email, username, or name.
selectorsIn:
- email
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: 100% free, no signup. The operator advertises anonymous, no-log searches over HTTPS.
opsec: passive
opsecNote: Lullar checks each platform for a matching public profile on your behalf; the target is not notified. Only your query and IP touch Lullar. Verify hits yourself, as platform "profile exists" checks can false-positive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-standing but lightly-documented profile-search front-end; it aggregates per-platform existence checks, which are convenient but not authoritative — confirm each result.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Lullar
- Lullar Com
- lullar-com-3.appspot.com
tags:
- people-search
- profile-search
- username-enumeration
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Lullar Profile Search

> A free, no-signup profile finder that fans an email, username, or name out across 175+ platforms in a single pass.

## When to use
You have an `email`, a `username`, or a `name` and want a quick breadth sweep for public profiles across a large platform list (Instagram, TikTok, X, LinkedIn, Reddit, GitHub, and many more). It is a fast early-stage discovery step: run the handle or address through Lullar to collect candidate profiles, then verify and enrich the real ones.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lullar-com-3.appspot.com/en.
2. Pick the search mode — email, username, or name — and enter your `selectorsIn`.
3. Submit; Lullar queries the platforms in parallel and returns candidate profile links grouped by service.
4. Open each candidate and confirm it is your subject (a username collision is not a match); discard placeholders.
5. Pivot: confirmed `social-profile` links feed platform-specific enrichment; a matched `name` becomes a new selector; run the same handle through a second sweep tool to catch platforms Lullar misses.

## Inputs → Outputs
- **In:** `email`, `username`, or `name`
- **Out:** `social-profile` links across 175+ platforms, candidate `name`
- **Empty/negative result looks like:** no candidate links, or only generic same-name pages — the identifier may be unused on the covered platforms, or the check may have missed a private profile; not proof of absence.

## Gotchas & OpSec
- Automated per-platform existence checks can report a "hit" for handles that merely resolve to a placeholder page — verify manually.
- Same-name / same-handle collisions are common when searching by name or a generic username.
- Passive: the target isn't notified; only your IP reaches Lullar.

## Overlaps ("do both")
- Pairs with `[[usersherlock-com]]` and other username sweeps — Lullar's platform list differs from theirs, so running both widens coverage and cross-confirms hits.
- Pairs with `[[idcrawl]]` — Lullar leans on username/email checks; IDCrawl adds public-records context.

## Trust & verifiability
`trust: unverified` — a convenient aggregator with little transparency about how each platform is probed. Treat every returned profile as a candidate to confirm, not a verified account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lullar-com-3-appspot-com |
| category | people-search |
| selectorsIn → selectorsOut | email, username, name → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
