---
id: thorndyke
name: Thorndyke
description: Use when you have a `username` and want a fast CLI account sweep — checks the handle's availability across 200+ websites and returns the `social-profile`s where it exists.
url: https://github.com/rlyonheart/thorndyke
category: username
path:
- username
bestFor: Command-line username enumeration across 200+ sites to find where a handle is registered.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (rlyonheart); a Python CLI installed locally. No account or key.
opsec: passive
opsecNote: Thorndyke requests each site's profile URL from your host, so those sites see your IP hit many URLs quickly. Run behind a proxy/VPN from a sock-puppet environment; it does not log into or notify the target accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community username-availability checker; like all such tools its site list and detection logic drift, so hits are heuristic and need visual confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname-web
- sherlock-2
- go-sherlock
- 0xdork
- open-corporates-command-line-client-occli
- thedevilseye
- thelordeye
aliases:
- thorndyke
- rlyonheart thorndyke
tags:
- Nicknames
- username-check
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Thorndyke

> A lightweight CLI that checks a `username` against 200+ websites and reports where it's registered — a fast, scriptable account-enumeration sweep.

## When to use
You have a `username` and want a quick command-line pass to find where the handle exists across 200+ sites, especially inside a scripted/automated workflow. It's in the same family as Sherlock/WhatsMyName — use it as one lens in a multi-tool username sweep, since no single checker's site list is complete.

## How to use it (`bestInteractionPattern`: cli)
1. Install from `https://github.com/rlyonheart/thorndyke` (Python; e.g. `pip install thorndyke` per the repo).
2. Run against the handle: `thorndyke <username>` (see `--help` for output/format options).
3. Read the reported hits — sites where the `username` appears to be registered.
4. Open each hit to confirm it's actually your subject (avatar, bio, activity), not a namesake.
5. Pivot: confirmed `social-profile`s feed per-platform enrichment; run the same handle through `[[whatsmyname-web]]` and `[[sherlock-2]]` and union the results.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` hits across 200+ sites
- **Empty/negative result looks like:** few/no hits — the handle may be unused, your subject uses a variant, or detectors are stale; try name variants and a second tool before concluding absence.

## Gotchas & OpSec
- Hits are heuristic (existence checks, not identity) — always open and verify.
- Site lists/detectors drift as platforms change; a miss can be a broken detector rather than a real absence — cross-run.
- A burst of requests to 200+ sites is noisy; use a proxy/VPN and pace runs to avoid blocks.
- OpSec: passive toward targets (no login/notify); mask your host IP.

## Overlaps ("do both")
- Overlaps with `[[whatsmyname-web]]`, `[[sherlock-2]]`, and `[[go-sherlock]]` — different, overlapping site sets and detection logic; run several and union.

## Trust & verifiability
`trust: community` — a functional open-source checker, but its output is algorithmic availability, not verified identity. Confirm every actionable hit by eye before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thorndyke |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
