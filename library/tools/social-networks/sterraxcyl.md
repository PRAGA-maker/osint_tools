---
id: sterraxcyl
name: Sterraxcyl
description: Use when you have an Instagram `username` and want their followers/following exported with details — returns each connection's `username`, full `name`, bio and counts (a social graph of `associate`s). Archived/unmaintained.
url: https://github.com/novitae/sterraxcyl
category: social-networks
path:
- social-networks
bestFor: Bulk-exporting an Instagram account's followers/following (with names and bios) to Excel/CSV/JSON to map its social graph.
selectorsIn:
- username
selectorsOut:
- username
- name
- associate
status: degraded
pricing: free
costNote: Free, open-source (GPL-3.0); install via `pip install sterra`. No paid tier — but the repo was archived in Oct 2024 and is unmaintained.
opsec: active
opsecNote: It authenticates to Instagram (GraphQL) and pulls another user's connections — that is active, account-linked activity Instagram can rate-limit or flag. Use a burner/sock-puppet Instagram account and a clean IP; never your real login. Expect the target's account to be public for best results.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: cli
trust: unverified
trustNote: A single-author open-source project, now archived (read-only since Oct 2024); Instagram API changes break such tools quickly, so verify it still works before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- sterra
- novitae sterraxcyl
tags:
- Social Media
- Instagram
- follower-export
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- tenai
---

# Sterraxcyl

> A command-line Instagram follower/following exporter — turn a handle into a spreadsheet of its social graph. Powerful, but archived and prone to breaking as Instagram changes.

## When to use
You have an Instagram `username` and want to **map who they're connected to** — followers, following, and the mutuals between two accounts — with each connection's username, full name, bio, and follower/following counts. That social graph is often the fastest route to family, friends, and associates in a missing-persons or vetting case. It can also filter a list down to likely *personal* accounts (the close circle) and diff two accounts for shared connections.

## How to use it (`bestInteractionPattern`: cli)
1. Set up a **burner Instagram account** and a clean IP (never your real login).
2. Install: `pip install sterra` (or clone the repo and run `python setup.py install`), and read the source first — it's archived, so confirm it still runs.
3. Authenticate with the sock-puppet session, then run it against the target `username` to export followers/following to Excel/CSV/JSON.
4. Use its analysis modes: flag likely personal accounts, or compare two exports for common/unique users.
5. Pivot: each connection's `name` + bio feeds people-search and cross-platform username enumeration; mutuals between the subject and a known relative strengthen an `associate` link.

## Inputs → Outputs
- **In:** an Instagram `username` (target account, ideally public)
- **Out:** a table of connections — `username`, full `name`, bio, follower/following counts — i.e. a graph of likely `associate`s
- **Empty/negative result looks like:** an error or empty export — Instagram changed its API, rate-limited/blocked the burner, or the target is private; treat a failure as a tooling/OPSEC problem, not proof the account has no connections.

## Gotchas & OpSec
- **Archived & unmaintained (Oct 2024)** — Instagram's frequent API changes mean it may already be broken; test before depending on it, and have a manual/alternative method ready.
- **Active with login**: pulling connections is exactly what Instagram polices — burner account, rate-limit yourself, expect challenges/blocks (human-in-the-loop).
- Private targets expose little; large accounts hit rate limits fast.

## Overlaps ("do both")
- Pairs with `[[tenai]]` and other Instagram-graph tools — if one breaks against a current API, another may still work; corroborate the connection list across tools.

## Trust & verifiability
`trust: unverified` — community code, archived; every exported connection is checkable by opening the profile directly, so verify key `associate`s manually rather than trusting the export wholesale.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sterraxcyl |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, name, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
