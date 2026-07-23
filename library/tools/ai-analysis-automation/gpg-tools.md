---
id: gpg-tools
name: GPG Suite (GPGTools)
description: Use for investigator-side encryption on macOS — sign/encrypt files and email with OpenPGP, and inspect PGP keys/signatures you encounter (which can carry a name/email).
url: https://gpgtools.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: OpenPGP encryption/signing on macOS, and inspecting PGP keys/signatures for the identity they embed.
selectorsIn: []
selectorsOut:
- email
- name
status: live
pricing: freemium
costNote: The GPG Suite core (GPG, GPG Keychain, Services) is free and open source; "GPG Mail" (the Apple Mail plugin) requires a paid support license on current macOS. Command-line GnuPG is fully free.
opsec: passive
opsecNote: This is your own opsec tooling — it protects your communications/files and lets you verify signatures. Handle keys locally; a private key is sensitive. When you inspect a PGP public key or signed message from a subject, the key's user ID (name + email) is a lead, but user IDs are self-asserted and can be forged, so verify rather than trust them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-standing, reputable macOS packaging of GnuPG; the underlying GnuPG is a widely-audited open-source standard.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- GPGTools
- GPG Suite
- gpgtools.org
tags:
- encryption
- pgp
- opsec
- privacy-and-encryption-tools
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# GPG Suite (GPGTools)

> The standard macOS packaging of OpenPGP/GnuPG — encrypt and sign your own files and mail, and inspect the PGP keys and signatures you come across, whose user IDs carry a name and email.

## When to use
Mainly investigator opsec: use it to encrypt sensitive case files, sign/verify communications, and manage keys on macOS so your own comms are protected. Secondarily, when you encounter a subject's PGP public key or a signed/encrypted message, GPG Suite lets you inspect it — a key's user ID embeds a claimed `name` and `email`, and the key ID/fingerprint can be matched against keyservers, giving weak identity leads. (On Linux/Windows the same underlying GnuPG applies.)

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install GPG Suite from https://gpgtools.org (macOS); it provides GPG Keychain, command-line GPG, and Services.
2. For opsec: generate your keypair, import correspondents' keys, and encrypt/sign files or (with the paid GPG Mail) email.
3. To inspect a subject's key/signature: import the public key or verify the signed message and read its user ID(s) — name, email, creation date, and fingerprint (`selectorsOut`).
4. Pivot: search the key ID/email on public keyservers for linked identities; treat user-ID name/email as unverified claims.

## Inputs → Outputs
- **In:** none as an OSINT selector for the encryption use; for inspection, a PGP key or signed message
- **Out:** protected/verified data, and (from an inspected key) `name` + `email` user-ID leads and a fingerprint
- **Empty/negative result looks like:** a signature that won't verify or a key you don't have — meaning you lack the counterpart key or the signature is invalid, not necessarily malicious.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: this is defensive tooling; keep private keys secure. PGP user IDs are self-asserted — a name/email in a key is a claim, not proof; anyone can put any identity on a key.
- The GPG Mail plugin is paid on current macOS; the core GPG and CLI are free.

## Overlaps ("do both")
- Pairs with public keyserver lookups (keys.openpgp.org, keyserver.ubuntu.com) — GPG Suite inspects/verifies a key locally, while keyservers help you find other keys/identities tied to an email or fingerprint.

## Trust & verifiability
`trust: trusted` — a reputable, long-standing macOS packaging of the widely-audited GnuPG standard. The tool is trustworthy; the *identities* inside PGP keys are self-asserted, so any name/email you read from a key must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gpg-tools |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → email, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
