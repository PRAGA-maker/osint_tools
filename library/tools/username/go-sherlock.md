---
id: go-sherlock
name: Go Sherlock
description: Use when you have a `username` and want a fast local enumeration across ~1000 sites — returns the sites where the handle exists, as a Go port of Sherlock.
url: https://github.com/Longwater1234/go-sherlock
category: username
path:
- username
bestFor: Fast, concurrent command-line username enumeration (a Go reimplementation of Project Sherlock) run from your own machine.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (Go); compile once and run locally, no account.
opsec: active
opsecNote: Unlike hosted enumerators, this runs from YOUR machine, so target sites see your IP making the existence checks. Route through a VPN/proxy and use a sock-puppet context if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community Go port of the well-known Sherlock project; accuracy depends on how current its site list is — an unmaintained fork can drift, so corroborate hits.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname-web
- whatsmyname-python
- gosearch
aliases:
- Longwater1234/go-sherlock
tags:
- Nicknames
- username
- cli
- golang
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Go Sherlock

> A Go reimplementation of Project Sherlock — checks whether a `username` exists across ~1000 sites in seconds, run locally from the command line.

## When to use
You have a `username` and want a fast, scriptable, offline-capable enumeration you control, rather than a hosted checker. Being a compiled Go binary, it's quick and easy to drop into pipelines. It fills the same role as Sherlock/WhatsMyName; choose it when you want local execution and speed, and cross-check against a hosted tool for coverage.

## How to use it (`bestInteractionPattern`: cli)
1. Clone/build from https://github.com/Longwater1234/go-sherlock (Go toolchain).
2. Run the binary with the target `username`; it concurrently checks its site list and prints the hits.
3. Because checks originate from your IP, run behind a VPN/proxy for sensitive work.
4. Confirm each hit on the actual site (shared handle ≠ same person).
5. Pivot: profiles feed name/photo/email extraction; also run `[[whatsmyname-web]]` to catch sites this fork's list may miss.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` links where the handle exists (with `username`)
- **Empty/negative result looks like:** few/no hits, or false negatives if the fork's site signatures are stale — don't treat a miss as proof; verify with a second enumerator.

## Gotchas & OpSec
- **Runs from your IP** — target sites see you; use a proxy/VPN, unlike hosted `[[whatsmyname-web]]`.
- Fork freshness matters: if unmaintained, its site list drifts and accuracy drops.
- OpSec: **active** on your side — plan attribution accordingly.

## Overlaps ("do both")
- Same job as `[[whatsmyname-python]]`/`[[whatsmyname-web]]` and `[[gosearch]]`; run at least two, since each tool's site list covers a slightly different set.

## Trust & verifiability
`trust: community` — a community port; results are only as good as its (possibly stale) site list, so confirm hits on the real platforms and corroborate coverage with a maintained enumerator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | go-sherlock |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
</content>
