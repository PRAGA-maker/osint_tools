---
id: namint
name: NAMINT
description: Use when you have a `name` (first / middle / nickname / last) and want ready-made search patterns and pivot links across Google, Yandex, Facebook, Twitter, LinkedIn and more — returns `username`, `social-profile` leads.
url: https://seintpl.github.io/NAMINT/
category: username
path:
- username
bestFor: Turning a real name into candidate usernames, email patterns and pre-built social/search-engine query links.
selectorsIn:
- name
- username
selectorsOut:
- username
- social-profile
- email
status: live
pricing: free
costNote: Free, open-source, runs entirely client-side in the browser (GitHub Pages); no account or payment.
opsec: passive
opsecNote: The page runs locally in your browser and only assembles links — nothing is submitted to the target until YOU click a generated link. Clicking a link then queries that third party (Google/Facebook/etc.) directly, so treat each pivot with normal sock-puppet hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Wiktor (seintpl), author of several well-known OSINT name/username tools; open-source and hosted on GitHub Pages, so the logic is inspectable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Name Intelligence
- seintpl NAMINT
tags:
- Nicknames
- username-enumeration
- name-permutation
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- amireal
- imagston
- seintpl-github-io
---

# NAMINT

> A client-side name-to-selectors generator: type a person's name and it hands you candidate usernames, email patterns and pre-built search links across the major engines and social networks.

## When to use
You have a subject's `name` (ideally first + middle/nickname + last, and optionally a birth year) and want to expand it into the derived selectors an investigation actually pivots on: likely `username` handles, `email` patterns, and one-click search queries against Google, Yandex, Facebook, Twitter/X, LinkedIn and others. Use it early, right after you learn a real name, to seed username and social-profile discovery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://seintpl.github.io/NAMINT/ (loads and runs entirely in your browser).
2. Enter first name, middle name or nickname, last name, and year if known. Optionally edit the default email domains list to match the target's likely region/provider.
3. Press **Go!** — the page renders sets of name permutations, candidate usernames, avatar/email guesses and clickable search-engine and social-network links.
4. Read the output: use the username permutations as input to `[[namint]]`-style handle checkers, and click through the pre-built links to look for matching profiles.
5. Pivot: feed generated `username` candidates into a username-enumeration tool and the `email` patterns into email-existence checks.

## Inputs → Outputs
- **In:** `name` (first / middle / nickname / last, + optional year)
- **Out:** candidate `username` handles, `email` patterns, and `social-profile` search links
- **Empty/negative result looks like:** it always generates patterns (it is generative, not a lookup) — "empty" really means the generated links return no matching profiles when you click them.

## Gotchas & OpSec
- The tool itself never contacts the target; it only builds links. The exposure happens when you click a generated link and query that third party — apply sock-puppet hygiene there.
- Output is combinatorial guesses, not confirmed hits: every username/email is a hypothesis to be verified, not a fact.
- Very common names produce huge, noisy permutation sets; add the middle name/year to constrain.

## Overlaps ("do both")
- Pairs with any username-enumeration checker — NAMINT invents the handle candidates, the checker confirms which exist.

## Trust & verifiability
`trust: community` — an open-source tool by a recognized OSINT author (seintpl), hosted on GitHub Pages so its logic is fully inspectable; it generates leads rather than authoritative data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | namint |
| category | username |
| selectorsIn → selectorsOut | name, username → username, social-profile, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
