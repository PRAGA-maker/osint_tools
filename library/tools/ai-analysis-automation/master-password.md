---
id: master-password
name: Master Password (Spectre)
description: Use when you need per-account passwords for many sock-puppet identities without a stored vault — returns deterministic passwords generated on demand from one master secret.
url: http://masterpasswordapp.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Generating unique, reproducible sock-puppet passwords statelessly, with nothing to sync or breach.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (now branded "Spectre"); apps for desktop and mobile.
opsec: passive
opsecNote: An investigator-OPSEC utility, not a lookup tool. It computes passwords locally from your master secret and a site/account name — nothing is stored or transmitted, so there is no vault to leak. Protect the single master secret accordingly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source stateless password generator by Maarten Billemont; the algorithm is public and auditable. It is an OPSEC hygiene tool, unrelated to data collection.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Spectre
- masterpasswordapp.com
tags:
- privacy-and-encryption-tools
- opsec
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Master Password (Spectre)

> A stateless password generator: instead of storing a vault, it *recomputes* each account's password from one master secret plus the account name — useful for managing many sock-puppet logins.

## When to use
You run multiple sock-puppet/research identities and need a unique, strong password per account without a synced vault that could be seized or breached. Master Password derives each password deterministically, so you can reproduce it on any device from your one master secret. This is investigator OPSEC hygiene, not an intelligence-gathering tool — it finds nothing about a subject.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install the app (desktop/mobile) from masterpasswordapp.com / masterpassword.app (now "Spectre"), open source.
2. Set your single master secret (your name + a strong master password) — commit this to memory; it is never stored.
3. For each account, enter the site/account name and choose a password type; the app derives that account's password on the spot.
4. Re-enter the same master secret + account name on any device to regenerate the identical password — no sync, no stored vault.
5. Use per-sock-puppet identifiers so each research persona gets distinct, reproducible credentials.

## Inputs → Outputs
- **In:** none (an OPSEC utility — you supply a master secret + account name, not a subject selector)
- **Out:** none (a generated password; no data about any person)
- **Empty/negative result looks like:** N/A — it deterministically produces a password; there is no query that "fails."

## Gotchas & OpSec
- The master secret is the single point of failure — if it's weak or exposed, every derived password is exposed; if forgotten, nothing is recoverable (there's no vault to fall back on).
- Some legacy sites reject generated formats or force resets — you must record per-site type/counter tweaks.
- Not an OSINT data source: it collects and reveals nothing about targets.

## Overlaps ("do both")
- Complements sock-puppet/persona-management practices in the opsec toolkit — this handles the credential layer; separate tools handle browser/identity isolation.

## Trust & verifiability
`trust: community` — an open-source tool with a published, auditable algorithm; its correctness is verifiable, and it makes no claims about any subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | master-password |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
