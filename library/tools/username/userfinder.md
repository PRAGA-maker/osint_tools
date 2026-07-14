---
id: userfinder
name: UserFinder
description: Use when you have a `username` and want to enumerate matching profiles across social platforms — returns links to accounts reusing that handle as social-profile leads.
url: https://github.com/mishakorzik/UserFinder
category: username
path:
- username
bestFor: Quick shell-based enumeration of a username across social and other sites.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: degraded
pricing: free
costNote: Free and open-source (Bash). No account; needs git, curl, and jq installed.
opsec: passive
opsecNote: The tool sends HTTP requests to many sites checking for the username — those requests come from your IP, so run it from a sock-puppet/VPN context. No target account is contacted or notified; it only probes public profile URLs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Single-author open-source shell tool (mishakorzik), last meaningfully updated around 2021. Site lists rot over time, so expect false positives/negatives; inspect the script before running.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- sherlock
- maigret
aliases:
- UserFinder
- mishakorzik/UserFinder
tags:
- Nicknames
- username-enumeration
- cli
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# UserFinder

> A lightweight Bash username-enumerator: give it a handle and it checks many sites for a matching profile.

## When to use
You have a `username` and want a fast, dependency-light sweep for where that handle exists online. It's a simpler, shell-based alternative to the big Python enumerators — handy on a minimal box where you just need quick hits to pivot from. Because it's unmaintained, treat it as a supplementary sweep rather than an authoritative one.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/mishakorzik/UserFinder && cd UserFinder` (ensure git, curl, jq are installed).
2. Run `bash UserFinder.sh` and provide the target username.
3. Read the reported profile URLs; open each to confirm it's genuinely the same person (handle reuse ≠ same individual).
4. Pivot: corroborate and expand with the better-maintained `[[sherlock]]` / `[[maigret]]`, which cover far more sites and reduce false positives.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` links (candidate accounts reusing the handle)
- **Empty/negative result looks like:** few or no hits, or false hits on sites that returned soft-200 pages — the site list is dated, so a miss here doesn't mean the handle is unused; re-run through a maintained tool.

## Gotchas & OpSec
- Human-in-the-loop: none, but manual verification of each hit is essential.
- OpSec: **passive** — it probes public URLs from your IP; sock-puppet/VPN it.
- **Degraded:** ~2021-era site definitions rot; expect both misses and false positives.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` and `[[maigret]]` — those are the maintained, higher-coverage enumerators; UserFinder is a quick shell-only supplement whose hits you fold into theirs.

## Trust & verifiability
`trust: community` — an unmaintained single-author script. Read it before running, and verify every reported profile manually, since dead site definitions produce both false positives and negatives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | userfinder |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
