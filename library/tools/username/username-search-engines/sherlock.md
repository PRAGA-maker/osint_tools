---
id: sherlock
name: Sherlock
description: Use when you have a `username` and want to find every site where that handle is registered — returns a list of `social-profile` URLs.
url: https://github.com/sherlock-project/sherlock
category: username
path:
- username
- username-search-engines
bestFor: Mass username enumeration across 400+ sites from the command line.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open source (MIT); install locally with pip/pipx or run via Docker. No account, no keys.
opsec: active
opsecNote: Sherlock directly requests a profile URL on each of 400+ sites to test whether the username exists — those sites (and any that log referrers) see the hits. It does NOT contact the person, but it does touch every platform. Route through Tor/a proxy (--tor / --proxy) for sensitive work and expect some sites to rate-limit or false-positive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: The de-facto standard open-source username enumerator (sherlock-project); very widely used and actively maintained, but community-run and prone to per-site false positives/negatives as sites change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- sherlock-project
tags:
- username
- enumeration
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Sherlock

> The standard open-source username hunter: give it a handle, it checks 400+ sites and returns every profile it finds.

## When to use
You have a `username` (or a shortlist of candidate handles) and want to map the subject's footprint across social networks, forums, dev sites, and niche platforms in one shot. It is the workhorse first step after you learn a handle — turning one username into a spread of `social-profile` URLs you then read manually. Ideal early in a missing-persons trace when you have a screen name but not much else.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pipx install sherlock-project` (or `pip install sherlock-project`, or run the Docker image).
2. Run: `sherlock <username>` — add several handles to check at once: `sherlock user1 user2`.
3. For OpSec, add `--tor` or `--proxy socks5://…`; write results to file with `--output` / `--folderoutput`.
4. Read the printed list of found accounts (each a `social-profile` URL); open each to confirm it's really your subject (handle reuse ≠ same person).
5. Pivot: confirmed profiles feed reverse-image/face tools, `[[namechk]]` for availability cross-check, and manual profile review.

## Inputs → Outputs
- **In:** `username` (one or many)
- **Out:** list of `social-profile` URLs where the handle exists, plus the `username` confirmed per site
- **Empty/negative result looks like:** "Not Found" on all/most sites — the handle is unused, or the person uses different handles per platform. Also watch for false positives on sites that return 200 for any profile path.

## Gotchas & OpSec
- Human-in-the-loop: none to run, but **you must manually verify** each hit — same username on two sites doesn't prove same person.
- OpSec: **active** — Sherlock probes every target site directly. Use Tor/proxy for sensitive subjects; heavy runs get rate-limited.
- Site adapters rot as platforms change; expect occasional false positives/negatives. Keep Sherlock updated.

## Overlaps ("do both")
- Pairs with `[[namechk]]` (availability cross-check) and `[[osrframework-jaykali-fork]]` (usufy module) — run more than one enumerator; each covers sites the others miss.

## Trust & verifiability
`trust: community` — the best-known open-source enumerator, actively maintained, but community-run and inherently noisy per-site. Treat every hit as a lead to confirm on the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sherlock |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
