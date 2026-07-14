---
id: neutrosint
name: NeutrOSINT
description: Use when you have an `email` or `username` and want to confirm whether it exists as a Proton Mail address (and get its PGP key-creation date) — returns account existence, an approximate creation date, and public key metadata.
url: https://github.com/Kr0wZ/NeutrOSINT
category: people-search
path:
- people-search
bestFor: Confirming a Proton Mail address exists and pulling its PGP-key creation date without alerting the owner.
selectorsIn:
- email
- username
selectorsOut:
- metadata-exif
- social-profile
status: live
pricing: free
costNote: Free and open-source. Light (API) mode needs no account; the Selenium bulk mode requires your own ProtonMail credentials.
opsec: passive
opsecNote: Light mode uses Proton's public key-lookup API and does NOT alert the target — a genuinely passive existence check. It is rate-limited (~100 requests/hour). Selenium mode logs into a ProtonMail account (use a sock-puppet account, never your own). Do not send mail to the target.
humanInLoop: true
humanInLoopReason:
- rate-limit
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool (Kr0wZ) featured in the Bellingcat toolkit. Relies on Proton's public key-lookup behaviour, which could change; verify results against a second method.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- account-live-com
- protonmail
aliases:
- NeutrOSINT
- Proton Mail OSINT
tags:
- bellingcat-toolkit
- people
- email
- protonmail
source: bellingcat-toolkit
lastVerified: '2026-07-14'
enrichment: full
---

# NeutrOSINT

> A CLI that checks whether an address exists on Proton Mail — passively — and returns its PGP key-creation date as an account-age signal.

## When to use
You have an `email` or `username` and want to know if it's a Proton Mail account, and roughly how old it is. Proton exposes public PGP keys for its addresses, so their presence confirms the account exists and the key's generation date approximates when the account was created — a useful age/authenticity signal, and a way to confirm a Proton address is real before pivoting. The check is passive: the owner is not notified.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install -e .` (or `pip install -r requirements.txt`); Chrome is required for Selenium mode.
2. Light mode (API, no login, recommended): `neutrosint -e 'address_or_username'` — returns existence + key-creation date. Add `-k` for the public key.
3. Bulk mode (many addresses): `neutrosint -u 'USER' -p 'PASS' -f 'list.txt'` using a **sock-puppet** ProtonMail login and Selenium.
4. Pivot: a confirmed Proton address feeds identity correlation; cross-check existence on other providers with `[[account-live-com]]`.

## Inputs → Outputs
- **In:** `email` or `username` (tested across Proton domains: protonmail.com, proton.me, pm.me)
- **Out:** existence boolean, `metadata-exif`-style account signal (PGP key-creation date ≈ account age), optional public key
- **Empty/negative result looks like:** "does not exist" — no Proton key for that address; note the key date is the *key's* creation, which usually but not always tracks account creation.

## Gotchas & OpSec
- Human-in-the-loop: **rate-limit** (~100/hr in light mode) and **account-login** for the Selenium bulk path.
- OpSec: light mode is **passive** and non-alerting — its main strength. Keep the ProtonMail login (bulk mode) on a burner account.
- The "creation date" is the PGP key generation date, a proxy for account age — treat as approximate.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (Microsoft-account existence) and other provider checks — run the address across providers to map which ecosystems it's real in.

## Trust & verifiability
`trust: community` — an open-source, Bellingcat-listed tool built on Proton's public key lookup. Existence results are reliable while Proton's behaviour holds; corroborate the age signal before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | neutrosint |
| category | people-search |
| selectorsIn → selectorsOut | email, username → metadata-exif, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
