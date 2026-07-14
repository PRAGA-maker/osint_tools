---
id: protonmail-domains
name: ProtonMail Domains
description: Use when you have an `email` (on any domain) and want to know whether it is hosted on Proton Mail — the public HKP key-lookup returns a PGP key index (existence, key-creation timestamp) if the address is a Proton account.
url: https://api.protonmail.ch/pks/lookup?op=index&search=<email_address>
category: username
path:
- username
- specific-sites
bestFor: Passively confirming an address (including custom domains) is a Proton Mail account via the public key-server endpoint.
selectorsIn:
- email
selectorsOut:
- metadata-exif
- domain
status: live
pricing: free
costNote: Free unauthenticated public key-server (HKP) endpoint; no account, no key needed.
opsec: passive
opsecNote: A public PGP key-lookup — the target is NOT notified and nothing is sent to their mailbox. You query Proton's key server directly; use a sock-puppet browser/IP to avoid tying the query to you. This is the manual version of what NeutrOSINT automates.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: The endpoint is Proton's own public key server, so an existence/key result is authoritative. Interpretation is on you — a returned key proves the address is a Proton account.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- neutrosint
- account-live-com
aliases:
- ProtonMail key lookup
- proton HKP lookup
tags:
- email
- protonmail
- account-existence
- pgp
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# ProtonMail Domains

> Proton's public PGP key-lookup endpoint used as an account-existence oracle: query an address and, if a key comes back, it's a Proton Mail account — including custom domains hosted on Proton.

## When to use
You have an `email` and want to confirm, passively, whether it's a Proton Mail account. Because Proton publishes each address's public PGP key, a key result confirms the account exists and the key's creation timestamp gives an approximate account age. Critically, it also works for **custom domains** hosted on Proton — a hit tells you a bespoke domain runs on Proton infrastructure, a strong provider-fingerprint and identity signal.

## How to use it (`bestInteractionPattern`: api)
1. In a sock-puppet browser (or via curl), request: `https://api.protonmail.ch/pks/lookup?op=index&search=TARGET@example.com`.
2. Read the response: a PGP key index (fingerprint, algorithm, creation time, email UID) means the address is a Proton account; an empty/"no results" response means it is not Proton-hosted.
3. Note the key **creation timestamp** as an approximate account-age signal.
4. Pivot: for bulk/scripted checks and cleaner output, use `[[neutrosint]]`; cross-check existence on other providers with `[[account-live-com]]`.

## Inputs → Outputs
- **In:** `email` (any domain)
- **Out:** `metadata-exif`-style key metadata (existence + key-creation timestamp), and confirmation the `domain` is Proton-hosted
- **Empty/negative result looks like:** no key index returned — the address isn't a Proton account (or the domain isn't on Proton); absence is not proof the person has no email.

## Gotchas & OpSec
- Human-in-the-loop: none — a single GET request.
- OpSec: **passive** and non-alerting — its key strength; still sock-puppet the query.
- The timestamp is the *key's* creation, a proxy for account age — treat as approximate. Endpoint behaviour could change if Proton alters key publishing.

## Overlaps ("do both")
- Pairs with `[[neutrosint]]` (automates exactly this across Proton domains at scale) and `[[account-live-com]]` (Microsoft-account existence) — run the address across providers to see where it's real.

## Trust & verifiability
`trust: trusted` — it's Proton's first-party key server, so a returned key authoritatively confirms a Proton account. The only judgement needed is reading "no result" as not-Proton rather than not-existent-anywhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | protonmail-domains |
| category | username |
| selectorsIn → selectorsOut | email → metadata-exif, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
