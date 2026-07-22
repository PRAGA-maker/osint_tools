---
id: mit-pgp-public-key-server
name: MIT PGP Public Key Server
description: Use when you have an `email` or `name` and want to check for an associated PGP public key — the key's user IDs reveal linked `email`s and the owner's stated `name`.
url: http://pgp.mit.edu
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Confirming a target uses PGP and harvesting the names/emails/key dates bound to their public key.
selectorsIn:
- email
- name
selectorsOut:
- email
- name
status: degraded
pricing: free
costNote: Free public keyserver run by MIT; no account.
opsec: passive
opsecNote: Searching for a key is a passive lookup — the key owner is not notified. Do NOT upload or certify anything; only search/extract. The keyserver operator sees your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing MIT-operated keyserver; keys and their user IDs are self-published by owners, so a UID proves someone published that name/email, not that it's genuine.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- mit-pgp-key-server
aliases:
- pgp.mit.edu
- MIT keyserver
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# MIT PGP Public Key Server

> MIT's public PGP keyserver — used in OSINT to check whether a subject has published a PGP key and to read the names, emails and dates bound to it.

## When to use
You have an `email` or `name` and want to know if the person uses PGP and what identity data their key carries. A PGP key's user IDs (UIDs) often list several `email`s and a stated `name`, and the key's creation date and signatures can hint at when/where they were active and who they interact with (web of trust). Confirms an address is real enough that someone bound a key to it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://pgp.mit.edu.
2. In "search string" enter the target `email`, `name`, or key ID and search.
3. Read each returned key's UIDs (all bound `name`s/`email`s), creation date, and signatures (other keys that signed it → associates).
4. STOP at reading — never submit or sign a key. Pivot the extra emails/names into email- and name-OSINT.

## Inputs → Outputs
- **In:** `email` / `name` / key ID
- **Out:** matching keys → bound `email`s and `name` (UIDs), key dates, signer relationships
- **Empty/negative result looks like:** "no keys found" — means no key on *this* server for that term; try keys.openpgp.org / keyserver.ubuntu.com before concluding the person has no PGP.

## Gotchas & OpSec
- The old SKS keyserver network is largely deprecated and pgp.mit.edu is frequently slow or down (hence `status: degraded`); use keys.openpgp.org as the modern alternative, and check both.
- Anyone can upload a key with any UID — a name/email in a UID is a claim, not proof of ownership.
- Keyservers are append-only; a key may be years stale or belong to a superseded address.

## Overlaps ("do both")
- Pairs with keys.openpgp.org and email-OSINT: query multiple keyservers for coverage, then run the harvested UIDs' emails through breach/account-existence checks.

## Trust & verifiability
`trust: trusted` — MIT-operated infrastructure, so the keys are genuinely as-published; the identities inside them are self-asserted, so corroborate before attributing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mit-pgp-public-key-server |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | email, name → email, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
