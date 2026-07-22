---
id: keys-openpgp-org
name: keys.openpgp.org
description: Use when you have an `email` or PGP key fingerprint and want to confirm a linked OpenPGP key and its self-declared identities — returns email, name.
url: https://keys.openpgp.org/
category: search-engines
path:
- search-engines
bestFor: Confirming whether an email or fingerprint has a published PGP key and pulling the identities bound to it.
selectorsIn:
- email
- document-id
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free public keyserver run by a non-profit; no account or payment.
opsec: passive
opsecNote: Searching queries a public keyserver, not the target — no notification reaches them. Note the server's privacy model: it only returns identity (email/name) info for addresses whose owner opted in via email verification, and it deliberately strips third-party signatures, so absence of a result is not proof no key exists.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the OpenPGP keyserver non-profit as a verifying keyserver; identity data is only shown after the address owner confirmed it, so returned email↔key bindings are reliable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Hagrid keyserver
- OpenPGP keyserver
tags:
- pgp
- keyserver
- email
- crypto
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- openpgp-org
---

# keys.openpgp.org

> The modern verifying OpenPGP keyserver: confirm that an email or fingerprint has a published PGP key and read the identities the owner chose to bind to it.

## When to use
You have an `email` address (or a key fingerprint / `document-id`) and want to know whether the subject uses PGP and what identities are attached to their key. A hit confirms the address is real and technically active, may reveal an associated `name` or alternate `email` the owner added to the same key, and gives you the fingerprint as a durable identifier to correlate elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://keys.openpgp.org/.
2. Search by the target `email`, by full key fingerprint, or by Key ID.
3. Read the result: if a key is returned, note its fingerprint, creation date, and any user IDs (email/name) attached — these are addresses the owner verified.
4. Distinguish the two search types: fingerprint/Key-ID search returns the key regardless; **email search only returns a result if the owner opted in** by confirming that address, so a "not found" on email does not rule out a key.
5. Pivot: a fingerprint correlates the person across mailing lists, git commits, and other keyservers; an additional user-ID email feeds email-OSINT.

## Inputs → Outputs
- **In:** `email` or key fingerprint / Key ID (`document-id`)
- **Out:** `email` (verified user-ID addresses on the key), `name` (user-ID names), key fingerprint/creation date
- **Empty/negative result looks like:** "No key found" — for an email this only means no *verified opt-in*, not that the person lacks PGP; retry via fingerprint or another keyserver (e.g. openpgp.org / SKS-style servers) before concluding.

## Gotchas & OpSec
- Privacy-by-design: identity (email/name) is withheld unless the owner verified it, and third-party certifications are stripped — so you can't map a web-of-trust here.
- A key's user-ID name is self-declared and unverified as a legal name; treat it as a lead.
- OpSec: fully passive; the keyserver is the only party that sees your query.

## Overlaps ("do both")
- Pairs with `[[openpgp-org]]` and other keyservers — key.openpgp.org is the verified/opt-in view, while older SKS-style servers may hold keys and signatures this one omits; query both to avoid false negatives.

## Trust & verifiability
`trust: trusted` — a well-run non-profit verifying keyserver; because email identities appear only after owner confirmation, a returned email↔key binding is trustworthy, though the opt-in model makes non-results uninformative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | keys-openpgp-org |
| category | search-engines |
| selectorsIn → selectorsOut | email, document-id → email, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
