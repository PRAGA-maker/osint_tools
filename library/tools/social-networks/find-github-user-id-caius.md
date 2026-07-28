---
id: find-github-user-id-caius
name: Find GitHub User ID (caius)
description: Use when you have a GitHub `username` and want its stable numeric user ID — returns the immutable ID that survives renames, letting you track an account across username changes.
url: http://caius.github.io/github_id
category: social-networks
path:
- social-networks
bestFor: Converting a GitHub username to its permanent numeric user ID (and vice-versa) to defeat renames.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free client-side page; uses the public GitHub API.
opsec: passive
opsecNote: The lookup calls GitHub's public API for the username — passive and unauthenticated. It does not notify the account owner. Runs in your browser; nothing is stored by the tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A tiny single-purpose utility by GitHub user Caius Durling; it just wraps the official GitHub API, so results are as authoritative as the API itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- github user id lookup
- caius github_id
tags:
- social-networks
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Find GitHub User ID (caius)

> A one-field utility that turns a GitHub username into its permanent numeric user ID — the identifier that stays constant even when the account is renamed.

## When to use
You're tracking a GitHub account and worry it may be (or has been) renamed. GitHub usernames are mutable, but the numeric **user ID is permanent**. Resolve a `username` to its ID so you can re-find the same account after a rename, correlate it across your notes, or confirm two handles are the same underlying account. Small but genuinely useful for durable account tracking.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://caius.github.io/github_id.
2. Enter the GitHub `username` and submit; it returns the numeric user ID (it queries the public GitHub API).
3. Record the ID alongside the username in your case notes.
4. To re-find the account later, open `https://api.github.com/user/<ID>` — GitHub returns the *current* username for that ID, revealing any rename.
5. Pivot: a stable ID lets you monitor the account and detect handle changes; the profile feeds repo/commit-email analysis.

## Inputs → Outputs
- **In:** `username` (GitHub handle)
- **Out:** `social-profile` (the numeric user ID / canonical account reference)
- **Empty/negative result looks like:** an error or no ID means the username doesn't currently exist on GitHub (never existed, deleted, or already renamed) — try known aliases.

## Gotchas & OpSec
- Only as current as the GitHub API — a just-renamed handle resolves to the new owner; use the ID (not the name) as the durable key.
- Tiny third-party page; if it ever breaks, the same result comes from `https://api.github.com/users/<username>` directly.
- Passive: the account owner isn't notified.

## Overlaps ("do both")
- Pairs with `[[github-search-engine]]` and commit-email tools — the ID gives you a durable handle on the account; the others find what that account has published and leaked.

## Trust & verifiability
`trust: community` — a minimal wrapper over the official GitHub API, so the ID is authoritative; verify anytime by hitting the GitHub API endpoint yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-github-user-id-caius |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
