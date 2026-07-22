---
id: mailvelope
name: Mailvelope
description: Use when you need to send or read OpenPGP-encrypted email in a webmail account (or manage PGP keys) — a browser extension that adds end-to-end encryption.
url: https://www.mailvelope.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Adding OpenPGP encryption/decryption and key management to browser webmail (Gmail, Outlook, etc.) for secure investigator comms.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; no account with Mailvelope required.
opsec: passive
opsecNote: This is defensive/opsec tooling for the investigator, not a query against a target. It encrypts your own mail so intermediaries can't read it; keep your private key and passphrase off shared machines and use it in a dedicated investigative browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Open-source (audited in the past), widely recommended OpenPGP browser extension maintained by Mailvelope GmbH; source is public on GitHub.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Mailvelope PGP
tags:
- privacy-and-encryption-tools
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Mailvelope

> A browser extension that bolts OpenPGP end-to-end encryption onto ordinary webmail, plus a built-in key manager — investigator opsec, not a lookup tool.

## When to use
You need to exchange sensitive information by email — with a source, a family contact, or a partner agency — and want it encrypted end-to-end so the mail provider and any interceptor can't read the body. Mailvelope lets you do that inside Gmail/Outlook/other webmail without a desktop mail client, and manages the PGP keypairs involved.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Mailvelope extension for Chrome/Firefox/Edge from https://www.mailvelope.com (or the browser store).
2. In the extension's key ring, generate a new OpenPGP keypair or import your existing key; import your correspondent's public key.
3. Open your webmail — Mailvelope overlays an encryption editor button on the compose window.
4. Write the message in the Mailvelope editor, encrypt to the recipient's public key, and send; incoming encrypted mail is decrypted in place with your passphrase.
5. Share your public key (or fingerprint) with correspondents so they can encrypt to you.

## Inputs → Outputs
- **In:** plaintext email + recipient public key (defensive use; not a target selector)
- **Out:** OpenPGP-encrypted/decrypted email in the browser
- **Empty/negative result looks like:** you can't encrypt to someone whose public key you don't hold — obtain and import their key first; a "no matching key" error is a missing key, not a bug.

## Gotchas & OpSec
- Recorded as a browser extension via `bestInteractionPattern` — install only in a trusted, ideally dedicated, browser profile.
- Guard the private key and passphrase; anyone with both can read your encrypted mail. Never install on a shared/public machine.
- It secures *your* comms — it does not decrypt a subject's traffic and is not an investigative lookup.

## Overlaps ("do both")
- Complements standalone PGP key tools and keyservers — those find/analyse a person's public key; Mailvelope is where you actually use keys to send and read encrypted mail.

## Trust & verifiability
`trust: trusted` — open-source, widely used, and previously security-audited OpenPGP implementation; its behaviour is inspectable in the public repository.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailvelope |
