---
id: instagramprivsniffer
name: InstagramPrivSniffer
description: Use when you have a private Instagram `username` and want to recover posts exposed through the Collaboration feature — returns a `social-profile` link and `image` media.
url: https://github.com/obitouka/InstagramPrivSniffer
category: social-networks
path:
- social-networks
bestFor: Recovering posts from a private Instagram account when it has collaborated on a post with a public account.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free open-source CLI (obitouka/InstagramPrivSniffer). No paid tier.
opsec: active
opsecNote: The tool queries Instagram's endpoints on your behalf; activity is attributable to whatever session/IP it runs from. It only surfaces content the private account itself co-posted with a public account (Meta confirmed this is intended Collaboration behavior, not a breach). Run from a sock-puppet context and treat retrieved media as sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source proof-of-concept from an individual researcher; it relies on Instagram's Collaboration feature exposing co-posts, which Meta has acknowledged. Reliability varies as Instagram changes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Instagram Priv Sniffer
tags:
- instagram
- private-account
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- obitouka
---

# InstagramPrivSniffer

> A CLI that pulls posts a *private* Instagram account made public by collaborating on them with a public account — a narrow but real crack in the privacy wall.

## When to use
You have a private Instagram `username` you can't view directly, but the account has used Instagram's Collaboration ("Collab") feature to co-author a post with a public account. Those co-posts are reachable via the public collaborator, and this tool enumerates and downloads them — recovering `image` media and post links a locked profile would otherwise hide. Useful when a subject's own account is private but they tag along on public content.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install dependencies (Python).
2. Enumerate exposed post links: `python main.py -n <username>` — lists private-account posts revealed via collaboration.
3. Download a specific post: `python main.py -d <URL>`.
4. Review the retrieved `image`/media and the collaborating public `social-profile`.
5. Pivot: the collaborating public account and the co-posted media feed reverse-image search, face matching, and mapping of the private user's associates.

## Inputs → Outputs
- **In:** private Instagram `username`
- **Out:** links to collaboration posts (`social-profile` context), downloadable `image`/media
- **Empty/negative result looks like:** no results — the account has no public collaboration posts (the common case). This does NOT expose the account's normal private content; only co-posts are reachable.

## Gotchas & OpSec
- Scope is narrow: it only works when the private account collaborated on a post with a public one. Most private accounts return nothing.
- Depends on Instagram's Collaboration behavior; Instagram can change this at any time, breaking the tool.
- OpSec: **active** — it hits Instagram's endpoints from your session/IP. Use a sock puppet; treat any recovered media as sensitive and mind your authorization.

## Overlaps ("do both")
- Pairs with mainstream Instagram OSINT (profile metadata, story/highlight viewers) and reverse-image search — those cover public accounts and photo provenance, while this specifically recovers collaboration co-posts from private accounts.

## Trust & verifiability
`trust: community` — an individual researcher's proof-of-concept exploiting an acknowledged Instagram feature, not a maintained product. Confirm any recovered content and identity link against a second source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagramprivsniffer |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
