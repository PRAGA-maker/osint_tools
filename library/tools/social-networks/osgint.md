---
id: osgint
name: OSGINT
description: Use when you have a GitHub `username` or `email` and want to pivot between them plus profile intel — returns commit-leaked `email`s, linked `username`s, and account metadata.
url: https://github.com/hippiiee/osgint
category: social-networks
path:
- social-networks
bestFor: Turning a GitHub username into associated emails (and vice-versa) by mining public commits, keys, and profile data.
selectorsIn:
- email
- username
selectorsOut:
- email
- username
- social-profile
status: live
pricing: free
costNote: Free, open-source (Python) on GitHub; self-hosted, no API key required.
opsec: passive
opsecNote: Passive — it reads GitHub's public API/pages (profiles, public commits, GPG/SSH keys, .patch data); it does not notify the target. Heavy use may hit GitHub rate limits; add a personal access token to raise them. Run from research infrastructure if the subject is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source OSINT tool (hippiiee, ~500+ stars); technique is sound (commit/GPG email leakage) but unaudited — verify results.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- osgint
tags:
- Social Media
- Github
- python
- email-enumeration
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# OSGINT

> A Python tool that pivots a GitHub username to the emails hidden in its public commits and keys — and back again.

## When to use
Your subject has a GitHub presence and you want to (a) turn their `username` into `email` addresses leaked through public commits/GPG keys, (b) reverse an `email` to the GitHub `username` that used it, or (c) pull profile metadata (creation date, repos, followers, linked Twitter). A commit author email is often a person's real/primary address — a strong pivot.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/hippiiee/osgint` and `pip3 install -r requirements.txt`.
2. Run by username: `python3 osgint.py -u <username>` — or by email: `python3 osgint.py -e <email>`. Add `--json` for machine-readable output.
3. Read the output: user ID, profile URL, bio, repo/follower counts, account timestamps, linked Twitter, and any `email`s recovered from commits/GPG keys.
4. Pivot: feed recovered emails into breach/email-OSINT tools and the linked Twitter/username into social tools.

## Inputs → Outputs
- **In:** GitHub `username` or `email`
- **Out:** associated `email`s, `username`, and profile `social-profile` metadata
- **Empty/negative result looks like:** no emails found when the account uses GitHub's private-email (noreply) setting and has no GPG key — the username may still be valid; absence of leaked email ≠ no account.

## Gotchas & OpSec
- Email recovery depends on the target having leaked one via a public commit or key; disciplined users leak nothing.
- Human-in-the-loop: none, but add a GitHub token to avoid rate limits on bulk use.
- OpSec: passive; only GitHub sees the (unauthenticated or token) API reads.

## Overlaps ("do both")
- Do both with email-breach and username-enumeration tools — OSGINT produces the email/username pivots; those enrich them across other platforms.

## Trust & verifiability
`trust: community` — well-known technique and tool; every recovered email/username is checkable directly against GitHub's public commit/key data, so verify before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osgint |
| category | social-networks |
| selectorsIn → selectorsOut | email, username → email, username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
