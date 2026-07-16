---
id: redditsfinder
name: redditsfinder
description: Use when you have a Reddit `username` and want to pull that account's full public post/comment history and metadata — returns social-profile activity, geolocation and name leads.
url: https://pypi.org/project/redditsfinder/
category: social-networks
path:
- social-networks
bestFor: Bulk-dumping one or many Reddit users' public post/comment history to JSON for offline analysis.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
- name
status: live
pricing: free
costNote: Free and open-source; installs from PyPI with pip. Reads Reddit's public JSON, no API key needed.
opsec: passive
opsecNote: Reads public Reddit data only; the target is not notified. Requests hit Reddit's servers from your IP — run from a VPN/sock-puppet host when polling many accounts, and respect Reddit rate limits to avoid a temporary block.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Small community-maintained OSS project on PyPI; it wraps Reddit's own public endpoints, so the data is authoritative even though the wrapper is unaudited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- reddits finder
- reddit finder
tags:
- reddit
- social-media
- username
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# redditsfinder

> A one-command Reddit user dumper: give it a username and it archives that account's entire public post and comment history to JSON.

## When to use
You have a Reddit `username` (from a breach, a cross-platform handle match, or a sock-puppet linked to your subject) and want the account's full activity in one pass rather than clicking through Reddit's paginated UI. Post and comment bodies frequently leak a real `name`, a home `geolocation` (local subreddits, "my city" posts), an employer, or other `social-profile` handles the person reuses.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install redditsfinder`.
2. Run against one user: `redditsfinder <username>` — prints the profile summary and activity.
3. Dump to JSON for analysis: `redditsfinder -j <username>`, or `redditsfinder --pretty <username>` for readable output.
4. Batch mode: `redditsfinder -f users.txt` to process a file of usernames at once.
5. Pivot: grep the JSON for city names, workplaces, other usernames, and outbound links, then feed those to a username enumerator like `[[whatsmyname]]` or an image tool for any avatars.

## Inputs → Outputs
- **In:** `username` (single, or a file of usernames)
- **Out:** account metadata (cake-day, karma), full post/comment history, and — mined from the text — `name`, `geolocation`, and linked `social-profile` handles.
- **Empty/negative result looks like:** an error that the user does not exist / is suspended, or an account with zero public posts (deleted or shadowbanned) — the tool returns the shell profile with no history to mine.

## Gotchas & OpSec
- Suspended, deleted, or brand-new accounts return little or nothing; that is a real signal, not a tool failure.
- Reddit rate-limits unauthenticated JSON requests; large batches can throttle your IP — pace runs and use a VPN.
- The tool only sees what is still public; content the user deleted is gone here — use a Reddit archive/cache tool for that.

## Overlaps ("do both")
- Pairs with a cross-platform username checker like `[[whatsmyname]]` — this dumps one account's history in depth, while an enumerator tells you *where else* the same handle exists.

## Trust & verifiability
`trust: community` — an unaudited open-source wrapper, but it pulls straight from Reddit's public JSON endpoints, so the underlying data is authoritative; verify any high-stakes claim against the live Reddit thread.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redditsfinder |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
