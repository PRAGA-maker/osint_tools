---
id: alfred-osint
name: Alfred OSINT
description: Use when you have a `username` and want to find where it exists across social platforms — returns a list of matching profile URLs (a Sherlock-family enumerator).
url: https://github.com/Alfredredbird/alfred
category: username
path:
- username
bestFor: Enumerating social-media and web accounts across many sites from a single username, from the command line.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source; you run it yourself, so cost is only your compute/time.
opsec: passive
opsecNote: The tool requests each candidate profile URL directly from the target sites, so those sites see traffic from YOUR IP (not the subject's). Run it from a VPS/VPN or sock-puppet network if you don't want your address in those sites' logs. It does not notify the subject.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: unverified
trustNote: A community-maintained open-source project by GitHub user Alfredredbird; not independently audited. Like all username enumerators it produces false positives (default profile pages) and false negatives (login-walled sites) — verify each hit by hand.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Alfred
- Alfredredbird alfred
tags:
- username-search
- account-enumeration
- python
- sherlock-family
source: osintambition-social
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- tookie-osint
---

# Alfred OSINT

> A command-line username enumerator in the Sherlock/Maigret family: given one handle, it checks many sites and reports where that name resolves to a profile.

## When to use
You have a `username`/handle and want to map the subject's footprint across platforms fast. Alfred queries a large list of sites for the handle and returns the ones where an account appears — the classic first move for pivoting a single username into many `social-profile`s that then leak real names, photos, locations and linked accounts.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/Alfredredbird/alfred` and install its Python dependencies.
2. Run it against the handle (see the repo's `-h`/README for the exact entrypoint and flags), e.g. passing the `username` to check.
3. Read the output list of hits — each is a candidate `social-profile` URL where the handle exists.
4. Open each hit and confirm it's the same person (avatar, bio, linked accounts) — enumerators over-report.
5. Pivot: confirmed profiles feed name/photo extraction, `[[sherlock]]`/`[[maigret]]` cross-checks, and reverse-image/face searches on the avatars.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` URLs where the handle resolves to an account
- **Empty/negative result looks like:** few or no hits — the handle is uncommon, the subject uses different handles per site, or login-walled sites (Instagram, Facebook) simply can't be checked this way. Absence is weak evidence; cross-run with another enumerator.

## Gotchas & OpSec
- Human-in-the-loop: expect **rate-limiting/blocking** from sites during a run, and manual verification of every hit (false positives on sites that return a generic page for any name).
- Enumerators go stale as sites change their "user not found" behaviour — check the repo is recently maintained and cross-check with a second tool.
- Traffic originates from your host; use a VPN/VPS if attribution matters.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`, `[[maigret]]` and WhatsMyName-based tools — each carries a different site list and different detection logic, so running two or three catches accounts any single tool misses.

## Trust & verifiability
`trust: unverified` — a solo-maintained open-source project; the code is inspectable but unaudited. Reliability depends on how current its site definitions are, so corroborate hits and prefer recently-updated forks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alfred-osint |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
