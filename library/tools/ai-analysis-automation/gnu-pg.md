---
id: gnu-pg
name: GNU PG
description: Use when you need to verify a PGP signature, decrypt a message, or inspect a target's PGP public key (which carries an email, name, and creation date) — supports opsec and yields email/name identifiers from keys.
url: https://www.gnupg.org/download/index.html
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Verifying signatures, decrypting messages, and extracting identity fields from PGP public keys.
selectorsIn:
- email
- document-id
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free and open-source (GnuPG / GPL); available for Linux, macOS, and Windows.
opsec: passive
opsecNote: All crypto operations run locally, so nothing leaves your machine. Caveat: fetching a key from a public keyserver by email/keyid is a network lookup that the keyserver logs — do that over a VPN/sock-puppet if the query itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: GnuPG is the canonical, widely-audited free implementation of the OpenPGP standard, maintained by the GnuPG project.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- gnupg-pgp-encryption
aliases:
- GnuPG
- GPG
- GNU Privacy Guard
tags:
- privacy-and-encryption-tools
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# GNU PG

> The standard free OpenPGP toolkit — for the investigator it's both opsec infrastructure (encrypt your notes, verify signatures) and a small identity source (PGP public keys embed an email, name, and dates).

## When to use
Two roles. **Opsec:** encrypt sensitive case files, verify the PGP signature on a tool/download to confirm it's genuine, or decrypt a message you've been given. **Investigative:** when a target uses PGP, their **public key** is a mini-dossier — it carries the `email`(s) and `name`/label the owner chose plus the key's creation date, all pivotable. GnuPG is how you import, inspect, and validate those keys.

## How to use it (`bestInteractionPattern`: cli)
1. Install GnuPG from https://www.gnupg.org/download/index.html (or your OS package manager).
2. **Inspect a key:** import a target's public key (from a file, a website, or a keyserver by email/keyid) and list it — the User ID(s) reveal `email` + `name`, and the key shows its creation date and any signatures from other keys (a web-of-trust graph of associates).
3. **Verify a signature:** `gpg --verify` a signed file/message against the signer's public key to confirm authorship/integrity.
4. **Decrypt:** decrypt messages/files you legitimately hold keys for.
5. Pivot: extracted emails/names feed email-OSINT; cross-signatures on a key hint at `associate` links.

## Inputs → Outputs
- **In:** a PGP public key or keyserver query (`email`/keyid), or a signed/encrypted artifact (`document-id`)
- **Out:** `email` and `name` from key User IDs, key dates, and signature/trust relationships
- **Empty/negative result looks like:** no key found on the keyserver, or a User ID with only a handle and no real name/email — many keys are deliberately minimal.

## Gotchas & OpSec
- The identity fields in a key are **self-asserted** — anyone can put any name/email on a key they generate, so treat them as claims, not proof.
- Keyserver lookups are network events that can be logged; use a VPN/sock-puppet for sensitive queries.
- Local operations (verify/decrypt/inspect an already-held key) are fully passive.

## Overlaps ("do both")
- Directly complements `[[gnupg-pgp-encryption]]`; use keyserver-search tools to find the key, then GnuPG to import and dissect it.

## Trust & verifiability
`trust: trusted` — GnuPG itself is the reference OpenPGP implementation and its cryptographic verdicts (signature valid/invalid) are authoritative; the *identity claims inside* a key are only as trustworthy as the key's owner made them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gnu-pg |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, document-id → email, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
