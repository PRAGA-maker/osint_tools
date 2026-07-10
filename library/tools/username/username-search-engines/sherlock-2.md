---
id: sherlock-2
name: Sherlock
description: Use when you have a `username` and want to enumerate that handle across 400+ sites at once — returns a list of social-profile URLs where the account exists.
url: https://github.com/sherlock-project/sherlock
category: username
path:
- username
- username-search-engines
bestFor: Fast, comprehensive CLI enumeration of one username across hundreds of sites.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (sherlock-project). No account or key.
opsec: active
opsecNote: Sherlock queries each target site directly from your machine to test whether the handle exists, so your IP touches every checked site. Route through Tor/proxy (built-in support) and avoid your attributable IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: The de-facto standard username enumerator — large, actively maintained open-source project. Some site checks false-positive/false-negative as sites change; verify each hit.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname-web
- maigret
- name-checkr
aliases:
- sherlock-project
tags:
- username-search
- account-enumeration
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Sherlock

> The standard command-line username enumerator — feed it a handle and it checks 400+ sites in parallel, returning every profile URL where the account appears to exist.

## When to use
You have a `username` and want the broadest possible one-shot map of where that handle exists online. Sherlock is the workhorse first step of username OSINT: it turns a single handle into a list of candidate profiles to review, which is exactly what you want when trying to locate a missing person's active accounts.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install sherlock-project` (or clone https://github.com/sherlock-project/sherlock). Python 3.
2. Run `sherlock <username>` (or several usernames). Use `--tor`/`--proxy` for anonymity and `--csv`/output flags to save results.
3. Read the printed list of found profile URLs.
4. Open each hit and confirm it is your subject — handles are reused, and some checks misfire.
5. Pivot: confirmed profiles feed content review, face-image capture, and bio-mining for further selectors.

## Inputs → Outputs
- **In:** `username` (one or many)
- **Out:** `social-profile` URLs where the handle exists
- **Empty/negative result looks like:** few/no hits — either a rare handle or sites rate-limited/blocked the checks. Re-run (optionally via Tor) and cross-check with a second enumerator before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none, but expect some false positives/negatives as sites change their responses.
- OpSec: **active** — your IP hits every checked site; use `--tor`/`--proxy`.
- Verify: always open hits; a "found" is existence, not proof of ownership by your subject.

## Overlaps ("do both")
- Pairs with `[[maigret]]` — deeper per-site data extraction and an even larger site list; run alongside Sherlock for coverage.
- Pairs with `[[whatsmyname-web]]` — the web/data-driven equivalent; cross-check to catch sites Sherlock misses.

## Trust & verifiability
`trust: community` — the leading open-source enumerator, widely used and maintained; results are reliable as leads but each hit must be opened and confirmed, since site checks drift over time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sherlock-2 |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
