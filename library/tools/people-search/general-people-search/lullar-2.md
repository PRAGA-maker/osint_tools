---
id: lullar-2
name: Lullar
description: Use when you have an `email`, `username`, or `name` and want a fast sweep of public social-media profiles under it — returns links to matching profiles across 175+ platforms.
url: https://com.lullar.com/
category: people-search
path:
- people-search
- general-people-search
bestFor: Quick anonymous enumeration of public social profiles by email, username, or name across many platforms.
selectorsIn:
- email
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: 100% free, no signup, no account — anonymous searches over HTTPS.
opsec: passive
opsecNote: Lullar builds and runs profile-lookup queries; per the site it keeps no logs and requires no account, and the target is not notified. Still, open discovered profiles from a sock-puppet browser and avoid engaging them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-standing free profile-search aggregator; results are pattern/URL guesses across platforms, so expect false positives and misses. Verify each hit manually.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- lullar
aliases:
- Lullar Profile Search
- com.lullar.com
tags:
- username
- email
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Lullar

> A free, no-signup profile-search aggregator — feed it an email, username, or name and it sweeps 175+ platforms for matching public profiles in one shot.

## When to use
You have an `email`, `username`, or `name` and want a fast first pass at where that identity has public profiles — the classic "spread an identifier across social media" step, done anonymously with no account. A good quick complement to CLI enumerators when you want a browser-only, zero-setup check.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://com.lullar.com/ (no login).
2. Choose the search type — email, name, or username — and enter the value.
3. It runs parallel lookups and returns links to candidate profiles across many platforms (Instagram, TikTok, X, LinkedIn, Reddit, GitHub, etc.).
4. Open each hit from a sock-puppet browser and verify it's actually your subject (handles collide).
5. Pivot: confirmed profiles feed name/photo enrichment; a recurring avatar/bio across sites strengthens attribution.

## Inputs → Outputs
- **In:** `email`, `username`, or `name`
- **Out:** links to candidate `social-profile`s / `username`s across 175+ platforms
- **Empty/negative result looks like:** few or no hits — the identifier is unused publicly, unique to one site, or the aggregator's URL patterns are stale. Common usernames yield false-positive collisions.

## Gotchas & OpSec
- Guess-based: many results are constructed profile-URL guesses, not confirmed matches — always click through and verify.
- Coverage claims: "175+ platforms" includes many low-signal sites; focus on the platforms that matter for your subject.
- OpSec: passive and anonymous per the site, but treat every discovered profile as something to view via sock puppet.

## Overlaps ("do both")
- Pairs with `[[blackbird]]` and other enumerators — Lullar is the fast browser-only sweep, CLI tools go deeper with live existence checks; run both and merge, since their site lists differ.

## Trust & verifiability
`trust: unverified` — a free aggregator returning candidate matches, not confirmed identities; verify each profile manually before attributing it to your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lullar-2 |
| category | people-search |
| selectorsIn → selectorsOut | email, username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
