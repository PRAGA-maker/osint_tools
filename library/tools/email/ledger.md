---
id: ledger
name: Ledger
description: Use when working through the POPPY OSINT toolkit and you reach the "Ledger" page — purpose unverified; likely an email/identity lookup helper but not confirmed.
url: https://bloopbase.keybase.pub/POPPY/LEDGER/index.html
category: email
path:
- email
bestFor: Unverified — a page within the keybase-hosted "POPPY" OSINT toolkit, exact function not confirmed.
selectorsIn:
- email
selectorsOut: []
status: down
pricing: free
costNote: Static page hosted on keybase.pub; no paywall observed, but the host was unreachable at check time.
opsec: unknown
opsecNote: Function unverified. Pages like this are often static link-collections or query-redirectors that pass your input to third-party sites — if so, those third parties would see your query. Treat as active until confirmed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Obscure page in the keybase-hosted "POPPY" toolkit, harvested from osint4all. Could not load the page to confirm function (host unreachable / connection refused at check time). Not identified — no feature claims are made.
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags: []
source: osint4all
lastVerified: ''
enrichment: full
---

# Ledger

> Unidentified page within the keybase-hosted "POPPY" OSINT toolkit; its exact function is not verified. This is NOT the Ledger hardware-wallet brand.

## When to use
Use only if you are deliberately working through the "POPPY" toolkit and have reached its "Ledger" page. Its specific function (what selector it takes and what it returns) could not be confirmed — the host was unreachable at check time. Given its category (`email`), it most plausibly accepts an `email` or username and links/redirects to a lookup, but this is not verified. Do not rely on it as a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bloopbase.keybase.pub/POPPY/LEDGER/index.html (may be offline — keybase.pub hosting can be intermittent).
2. Inspect the page to determine what input it expects before entering anything.
3. If it is a redirector to a third-party service, verify where your input is sent before submitting subject data.

## Inputs → Outputs
- **In:** likely `email` (unconfirmed)
- **Out:** unknown — not verified
- **Empty/negative result looks like:** unknown; the page may simply be offline (connection refused at check time).

## Gotchas & OpSec
- Unverified tool: do not assume capabilities. The page may be dead, a static link list, or a redirector to external sites.
- OpSec: if it forwards your query to third parties, those services see your input. Treat as active until you confirm otherwise; use a sock puppet.

## Overlaps ("do both")
- Prefer verified breach/email tools like [[leakcheck]] and [[intelligence-x-2]] over this until its function is confirmed.

## Trust & verifiability
`trust: unverified` — obscure keybase-hosted page in the "POPPY" toolkit; could not be loaded to confirm what it does, so no feature claims are made. Maintainer and provenance unknown.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ledger |
| category | email |
| selectorsIn → selectorsOut | email → (unknown) |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | unknown |
| human-in-loop | no |
