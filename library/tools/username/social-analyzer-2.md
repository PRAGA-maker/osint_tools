---
id: social-analyzer-2
name: social-analyzer
description: Use when you have a `username` (or `name`) and want to sweep 1000+ sites for matching profiles with a confidence rating — returns ranked `social-profile` hits.
url: https://pypi.org/project/social-analyzer/
category: username
path:
- username
bestFor: High-coverage username enumeration across 1000+ sites with a detection-confidence score to cut false positives.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (qeeqbox/social-analyzer). Install via `pip install social-analyzer`; no account or key. Runs as CLI, importable API, or a local web UI.
opsec: active
opsecNote: The scan sends requests to hundreds of sites from your host/IP, so each target site sees your traffic — this is active reconnaissance. Route through a VPN/proxy or managed-attribution host; the *subject* is not directly notified, but the platforms are queried.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Well-known open-source project by qeeqbox with a large maintained site list; detection uses multiple methods (profile, HTTP, dynamic) and returns a confidence rating rather than raw exists/doesn't.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- social-analyzer
- qeeqbox social-analyzer
tags:
- username-check
- python
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# social-analyzer

> An open-source API/CLI/web tool that hunts a username (and can rate names/emails) across 1000+ sites, scoring each hit's confidence instead of just returning a raw "exists" — cutting the false-positive noise that plagues simpler enumerators.

## When to use
You have a `username` and want the widest possible net across social, gaming, dev, and niche sites in one run. Its edge over quick checkers is the **detection rating**: it weighs multiple signals (profile content, HTTP behavior, string matching) so you spend verification time on likely-true hits, not on every 200-OK. Feed it a `name` and it can also generate and test username permutations.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install social-analyzer` (Python 3).
2. Run a scan — CLI: `python -m social-analyzer --username "target" --metadata`, or import the module, or launch its local web UI.
3. Read the ranked output — each candidate `social-profile` with a detection score; filter to high-confidence.
4. Manually open the top hits (a score is a lead, not proof) and confirm it's the same person.
5. Pivot: confirmed profiles feed photo/reverse-image, employer, and cross-platform handle checks.

## Inputs → Outputs
- **In:** `username` (or `name` for permutation mode)
- **Out:** ranked list of candidate `social-profile`s with per-site confidence scores
- **Empty/negative result looks like:** all low-confidence / no hits — the handle likely isn't in wide use; but common handles produce many false matches, so always eyeball the top results.

## Gotchas & OpSec
- OpSec: **active** — it fans out real requests to every checked site from your IP. Use a proxy/VPN or managed-attribution browser for sensitive work.
- Site lists drift as platforms change their profile URLs/anti-bot; some checks will be stale — corroborate, don't trust a single hit.
- Common usernames yield false positives; the confidence score helps but manual verification is mandatory.

## Overlaps ("do both")
- Pairs with other username enumerators and reverse-image tools — run more than one enumerator (each has different site coverage), then confirm identity with a photo match.

## Trust & verifiability
`trust: community` — a reputable, actively used open-source project; the confidence scoring reduces noise but is heuristic, so treat outputs as ranked leads requiring human confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-analyzer-2 |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | no |
