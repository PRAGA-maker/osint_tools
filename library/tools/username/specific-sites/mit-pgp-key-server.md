---
id: mit-pgp-key-server
name: MIT PGP Key Server
description: Use when you have an `email`, `name`, or key ID and want to find a subject's published PGP public key and the identities (UIDs/emails) attached to it — returns linked emails, names, and key metadata.
url: https://pgp.mit.edu/
category: username
path:
- username
- specific-sites
bestFor: Looking up a person's PGP public key by email/name and reading the other identities and emails bound to that key.
selectorsIn:
- email
- name
- username
selectorsOut:
- email
- name
status: degraded
pricing: free
costNote: Free public key server; no account or payment.
opsec: passive
opsecNote: A public key-server query is passive — the key owner is not notified and the server logs only ordinary web requests. No sock puppet needed, though use a clean session as a matter of habit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running keyserver operated by MIT; the key data itself is user-submitted and unverified, but the server is a legitimate first-party host.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- pgp.mit.edu
- MIT public key server
tags:
- pgp
- keyserver
- email
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# MIT PGP Key Server

> A long-standing public PGP keyserver: given an email or name, find a person's published key and the other identities (UIDs, emails) they bound to it.

## When to use
You have an `email`, `name`, or `username` for a privacy- or crypto-aware subject and want to check whether they publish a PGP key. A key's User IDs (UIDs) frequently bundle several `email` addresses and a real `name` under one identity — so one known address can surface additional addresses and confirm a name. The key's creation date and fingerprint also help anchor a timeline and cross-match against keys referenced elsewhere (Keybase, git commits, email headers).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pgp.mit.edu/.
2. In "Extract a key", enter the search string — an `email`, `name`, or key ID / fingerprint — and submit (enable "verbose index" and "show fingerprints" for more detail).
3. Read the index: each hit lists the key ID, creation date, and every UID (name + email) attached.
4. Pivot: additional `email`s in the UIDs feed email-OSINT; the `name` corroborates identity; the fingerprint cross-matches keys on other keyservers/Keybase/git.

## Inputs → Outputs
- **In:** `email`, `name`, or `username` / key ID
- **Out:** linked `email` addresses and `name`s from the key's UIDs, plus key ID, fingerprint, and creation date
- **Empty/negative result looks like:** "No results found" — the subject may never have published a key, may have used a different keyserver, or the SKS-era record may not have propagated here.

## Gotchas & OpSec
- **Reliability is degraded.** pgp.mit.edu was part of the SKS keyserver network, which was effectively deprecated around 2019–2021; the server is often slow, intermittently unreachable, and no longer well-synchronised. If it fails, retry against modern keyservers (keys.openpgp.org, keyserver.ubuntu.com) — note keys.openpgp.org hides email UIDs unless verified, so it is worse for this pivot.
- Key data is **user-submitted and unverified** — anyone could upload a key claiming any name/email, so treat UID identities as claims to corroborate, not proof.
- Old SKS servers cannot delete keys, so results may include long-abandoned addresses.
- OpSec: passive; the owner is not notified.

## Overlaps ("do both")
- Do both with keys.openpgp.org and keyserver.ubuntu.com — coverage differs per keyserver, and a key absent here may be present there (and vice versa).

## Trust & verifiability
`trust: trusted` — MIT is a legitimate first-party host, but the *content* is unverified user submissions; rate the server trusted and each key's identities as unconfirmed leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mit-pgp-key-server |
| category | username |
| selectorsIn → selectorsOut | email, name, username → email, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
