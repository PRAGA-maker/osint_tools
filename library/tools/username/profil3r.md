---
id: profil3r
name: Profil3r
description: Use when you have a `username` and want to enumerate matching accounts across social networks plus derive and breach-check likely emails — returns social-profile, email and breach hints.
url: https://github.com/Rog3rSm1th/Profil3r
category: username
path:
- username
bestFor: One-shot username-to-accounts-and-emails sweep with automatic breach lookup and a JSON/HTML report.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- email
- username
status: degraded
pricing: free
costNote: Free and open-source (Python). No paid tier; the only cost is local setup.
opsec: passive
opsecNote: Enumeration runs from your host and hits many target platforms directly. Run from a sock-puppet IP/VPN; each checked site sees your address. The breach-check step queries third-party leak indexes with the derived email — avoid on sensitive investigations where that lookup itself is a tell.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Widely forked, well-known OSINT project by Rog3rSm1th. The original upstream repo is currently unreachable (404); use an actively maintained fork/mirror and review the code before running.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- sherlock
- maigret
aliases:
- Profil3r
tags:
- Nicknames
- username-enumeration
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# Profil3r

> A Python username-to-identity sweeper: give it a nickname, get back candidate social accounts, likely email permutations, and whether those emails appear in breaches — all in one report.

## When to use
You have a `username` (or a `name` to permute) and want a fast, breadth-first pass across social networks and email providers before doing careful manual verification. Its differentiator over pure username checkers is that it also generates likely email addresses and flags breach presence, giving you pivots into email-OSINT in the same run.

## How to use it (`bestInteractionPattern`: cli)
1. Clone a maintained fork/mirror (the original `github.com/Rog3rSm1th/Profil3r` currently returns 404 — see the Internet Archive snapshot or forks such as Greyjedix/Profil3r). Review the source first.
2. Install: `pip install -r requirements.txt` (Python 3), configure `config.json` for the modules you want.
3. Run: `python3 profil3r.py <username>`.
4. Read the generated JSON/HTML report: confirmed vs. probable accounts, generated email permutations, and breach flags.
5. Pivot: confirmed `social-profile` links feed manual review; breach-flagged `email` feeds dedicated email/breach tooling.

## Inputs → Outputs
- **In:** `username` (or `name` to build permutations)
- **Out:** `social-profile`, generated `email` candidates + breach hits, `username` matches
- **Empty/negative result looks like:** all modules return "not found" — common for very generic or very rare handles, and increasingly common as platforms harden against enumeration. Treat probable/derived emails as leads, not confirmed addresses.

## Gotchas & OpSec
- Human-in-the-loop: platforms rate-limit and change markup, so modules go stale and false-negative; corroborate every hit manually.
- The original repo is gone — pin to a fork you have read, since supply-chain risk is real for run-locally OSINT scripts.
- OpSec: your host contacts every checked platform directly; use a VPN/sock-puppet and be aware the breach-check leaks the queried email to a third party.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` and `[[maigret]]` — those cover a larger and better-maintained site list for pure username presence; Profil3r adds the email-generation + breach angle they lack. Run one broad checker plus Profil3r and reconcile.

## Trust & verifiability
`trust: community` — popular open-source project, but unofficially maintained and with the original upstream currently down; verify by reading the fork's code and confirming each account hit by hand.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | profil3r |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile, email, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
