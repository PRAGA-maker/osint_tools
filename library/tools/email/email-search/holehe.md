---
id: holehe
name: Holehe
description: Use when you have an email and want to learn which of 120+ websites have an account registered to it.
url: https://github.com/megadose/holehe
category: email
path:
- email
- email-search
bestFor: Enumerating which online services an email is registered on, without alerting the target.
selectorsIn:
- email
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (Python).
opsec: passive
opsecNote: Uses each site's forgot-password / registration check to detect account existence WITHOUT sending an email or notifying the target. Some checks may trip rate limits or CAPTCHAs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source tool by megadose (also maintains toutatis/ignorant); ~9k GitHub stars and a standard in email OSINT. Some site modules silently break as targets change their flows.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- have-i-been-pwned
- h8mail
- hudson-rock
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# Holehe

> Email account-enumeration tool: give it an email and it checks 120+ sites (Instagram, Twitter/X, Spotify, Amazon, etc.) for a registered account — silently, via password-reset/registration probes.

## When to use
You have an `email` for a missing person or associate and want to know *which platforms they actually use* — a map of their online footprint that pivots straight into per-platform profile lookups. Especially valuable early: it turns one email into a list of `social-profile`s to investigate.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install holehe`.
2. Run: `holehe target@example.com`.
3. Read the table: each site is marked as account exists / no account / rate-limited. Use `--only-used` to show only positives.
4. As a Python lib: `import holehe.modules...` to script bulk checks.
5. Pivot: for each "exists" hit, go to that platform and look up the profile (username/name enumeration).

## Inputs → Outputs
- **In:** `email`
- **Out:** list of services with an account (implying `social-profile` / `username` presence on each)
- **Empty/negative result looks like:** every module returns "no account" or "rate limited"; "rate limited" is NOT a true negative — rerun later or from a different IP.

## Gotchas & OpSec
- Some modules return false negatives when a site changes its flow; absence of a hit isn't proof of absence.
- Rate limiting/CAPTCHA on some sites can mask results — distinguish "rate limited" from "no account".
- OpSec: genuinely passive — the target receives no email and no notification. Still run from a research IP.

## Overlaps ("do both")
- Pairs with `[[have-i-been-pwned]]` (breach history of the same email) and `[[h8mail]]` / `[[hudson-rock]]` (credentials/infostealer data) — Holehe finds live accounts, those find leaked data.

## Trust & verifiability
`trust: community` — mature, widely-used open-source tool; reliable in aggregate, but verify individual hits since site modules drift over time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | holehe |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
