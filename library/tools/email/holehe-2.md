---
id: holehe-2
name: holehe
description: Use when you have an `email` and want to know which sites it's registered on — returns a list of accounts (`social-profile`) tied to that address via password-reset/registration probes.
url: https://pypi.org/project/holehe/
category: email
path:
- email
bestFor: Enumerating which of 120+ online services an email address has an account on.
selectorsIn:
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (Python, MIT). Install via pip; no account, API key, or payment.
opsec: active
opsecNote: For each site, holehe probes the registration/password-reset endpoint using the target's email — an ACTIVE query against those services. Most checks are silent, but some providers can trigger a notification email or log the reset attempt to the account owner. Run from a sock-puppet IP; be aware you are touching real login infrastructure with the target's address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely-used open-source tool by megadose, standard in the OSINT toolkit. It only observes each site's own responses; accuracy depends on each site's current behaviour (modules break as sites change).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- account-live-com
- whatsmyname-app
aliases:
- holehe
- megadose holehe
tags:
- email-recon
- account-enumeration
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# holehe

> A command-line account-enumeration tool: feed it an email and it tells you, across 120+ sites, where that address is already registered — without alerting the owner in most cases.

## When to use
You have an `email` and want to map the subject's online footprint fast. holehe queries each site's "email already in use?" / password-reset behaviour and reports registered vs not-registered per service (Twitter/X, Instagram, Spotify, Adobe, Amazon, etc.). The resulting list of `social-profile`s points you at the platforms worth investigating and corroborates that an address is real and actively used.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install holehe` (Python 3).
2. Run: `holehe target@example.com`.
3. Read the output: each module prints `[+]` (email used/registered), `[-]` (not used), or `[x]` (rate-limited/error). Use `--only-used` to show only hits.
4. Note which platforms return `[+]` and whether any expose recovery hints (some modules surface partial phone/email masks).
5. Pivot: each registered service becomes a target for username/profile work; confirmed Microsoft accounts pair with `[[account-live-com]]`; cross-reference usernames via `[[whatsmyname-app]]`.

## Inputs → Outputs
- **In:** `email`
- **Out:** per-site registration status → a set of `social-profile`s the email is tied to (occasionally partial recovery hints)
- **Empty/negative result looks like:** all modules `[-]` or `[x]` — either the address genuinely has few accounts, or (common) many modules are rate-limited/broken by site changes. A wall of `[x]` means "couldn't check", not "no account".

## Gotchas & OpSec
- Human-in-the-loop: none to run, but interpret carefully — module accuracy decays as sites change their reset flows.
- OpSec: **active** — holehe hits each provider's real registration/reset endpoint with the target's email. Most are silent; some may email or log the attempt. Use a VPN/sock-puppet network context, and never trigger an actual password reset.
- Rate-limiting causes false negatives; re-run failed modules later or from a different IP.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (Microsoft-account existence oracle) and `[[whatsmyname-app]]` (username enumeration) — holehe works from an *email*, WhatsMyName from a *username*; run both to cover the identity from both selectors.

## Trust & verifiability
`trust: trusted` — an established, open-source, widely-audited tool. Its findings are only as current as its site modules, so treat `[+]` hits as strong leads to confirm on the platform itself, and `[x]` results as inconclusive rather than negative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | holehe-2 |
| category | email |
| selectorsIn → selectorsOut | email → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
