---
id: proxynova-comb
name: ProxyNova COMB
description: Use when you have an `email`, `username`, or `password` and want to check the COMB aggregated-breach dataset — returns leaked email:password pairs tied to that selector.
url: https://www.proxynova.com/tools/comb/
category: email
path:
- email
bestFor: Free search of the COMB (Compilation of Many Breaches) credential dataset by email, username, or password.
selectorsIn:
- email
- username
- password
selectorsOut:
- email
- password
- username
status: live
pricing: free
costNote: Free web tool and free JSON API (`api.proxynova.com/comb?query=...`); no account or key. Capped at ~100 results per query and ~100 requests/minute. ProxyNova states searches are not logged or stored.
opsec: passive
opsecNote: You query ProxyNova's servers, not the target — the subject is never contacted or notified. You are, however, submitting a selector (and possibly a password) to a third party over the internet; use a sock-puppet IP and never enter live credentials you need to keep secret.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ProxyNova is a long-running proxy/tools site; the COMB corpus is a 2021 aggregation of many older breaches. Hits confirm a credential appeared in that compilation, not that it is current.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- COMB
- Compilation of Many Breaches
tags:
- breach
- comb
- credentials
- email
source: inteltechniques-tools
lastVerified: '2026-07-19'
enrichment: full
---

# ProxyNova COMB

> A free web + API front-end to the COMB (Compilation of Many Breaches) dataset — search an email, username, or password and get back the leaked pairs that contain it.

## When to use
You have an `email` (or `username`) for a subject and want to know whether it appears in the massive COMB credential compilation, and what other data (associated usernames, an old password, or additional emails) surfaces alongside it. A hit corroborates that an address is real and historically used, and the associated username/password fragments can pivot to other accounts and platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Web: open https://www.proxynova.com/tools/comb/ and enter the `email`/`username`. Use the `@` prefix for domain-wide views (e.g. `@example.com`).
2. API: `curl "https://api.proxynova.com/comb?query=TARGET&start=0&limit=15"` — returns JSON with a match count and `email:password` lines. Paginate with `start`/`limit` (≤100 results, ~100 req/min).
3. Read the output: each line pairs an identifier with a leaked password; multiple lines for one email suggest reuse or multiple breaches.
4. Pivot: reused usernames/passwords feed username-enumeration and other-account checks; a confirmed email feeds account-existence oracles like `[[account-live-com]]`.

## Inputs → Outputs
- **In:** `email`, `username`, or `password`
- **Out:** matching leaked `email` / `username` / `password` pairs from COMB
- **Empty/negative result looks like:** a zero count / empty result set — the selector isn't in COMB. That is NOT proof the person was never breached; COMB is a fixed 2021 snapshot and misses everything after it and many breaches before it.

## Gotchas & OpSec
- COMB is aggregated and dated (2021) — passwords may be years old and already rotated; treat them as historical leads, never for live access attempts.
- Results are capped (~100) and rate-limited; a domain query only samples.
- Legal/ethical: this is breach data. Use only for legitimate investigation; do not attempt to authenticate with recovered credentials.
- OpSec: passive toward the target, but you are sending selectors to a third party — sock-puppet IP.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — COMB confirms an address was breached and surfaces old creds; account.live.com confirms the address is a live Microsoft account today.

## Trust & verifiability
`trust: community` — a free third-party interface to a public breach compilation. Any hit should be corroborated (the same email/username via other breach indexes) before you rely on it; the data quality is inherited from the original breaches, not curated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proxynova-comb |
| category | email |
| selectorsIn → selectorsOut | email, username, password → email, password, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
