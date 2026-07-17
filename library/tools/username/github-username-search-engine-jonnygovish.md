---
id: github-username-search-engine-jonnygovish
name: GitHub Username Search Engine (jonnygovish)
description: Use when you have a `username` and want to check whether it exists on GitHub and view its public repositories — returns the matching GitHub profile and repo list (social-profile).
url: https://jonnygovish.github.io/Github-username-search-engine
category: username
path:
- username
bestFor: Quickly confirming a GitHub account for a username and listing its public repositories.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free static web app hosted on GitHub Pages; no account or API key required from the user.
opsec: passive
opsecNote: The lookup queries GitHub's public API for the username; the target is not notified. It is a thin front-end over data GitHub already exposes publicly, so nothing is leaked beyond a normal API read.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small open-source hobby project (GitHub Pages) that wraps the official GitHub API; the underlying data is authoritative even though the wrapper is unaffiliated with GitHub.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Github username search engine
tags:
- github
- username-search
source: osintambition-social
lastVerified: '2026-07-17'
enrichment: full
---

# GitHub Username Search Engine (jonnygovish)

> A minimal web front-end over GitHub's public API: type a username, see whether the account exists and what public repositories it owns.

## When to use
You have a `username` and want to know, quickly, whether it maps to a GitHub account and what that account works on. Confirming a GitHub presence corroborates a technical persona, and the repo list, bios, pinned projects, and linked sites become pivot points (real name in commits, personal domains, other linked accounts).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://jonnygovish.github.io/Github-username-search-engine.
2. Type the target `username` into the "Github Username Search" field and submit.
3. Read the result: an existing account returns the profile and its **public repos**; a non-existent one returns nothing.
4. For real depth, take the confirmed username straight to github.com/<username> — browse the profile, README, followers/following, and (via commit history) the email/name attached to commits.
5. Pivot: a confirmed handle feeds cross-platform username tools; commit emails feed email lookups; linked websites feed domain tools.

## Inputs → Outputs
- **In:** `username`
- **Out:** matching GitHub `social-profile` and its public repository list
- **Empty/negative result looks like:** no profile / empty repo list — the handle isn't a GitHub account (or is a brand-new empty one). Confirm directly at github.com/<username> before concluding.

## Gotchas & OpSec
- This is a thin, single-purpose wrapper; it does not cross-reference other platforms and can be flaky (GitHub Pages, rate limits, minimal UI). For anything serious, go to GitHub directly or use a multi-platform username checker.
- Only public data is shown; private repos and hidden email settings won't appear.
- OpSec: **passive** — a normal public GitHub API read; the target is not alerted.

## Overlaps ("do both")
- Pair with a broad multi-site username enumerator (e.g. a Sherlock/WhatsMyName-style tool) so GitHub is one confirmed node among many; this tool only answers the GitHub question.

## Trust & verifiability
`trust: community` — an unaffiliated open-source hobby project, but it simply surfaces GitHub's own public API data, so a positive hit is authoritative once you confirm it on github.com itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-username-search-engine-jonnygovish |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
