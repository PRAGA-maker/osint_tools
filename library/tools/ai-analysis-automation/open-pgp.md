---
id: open-pgp
name: OpenPGP (Enigmail)
description: Use when an investigator needs to encrypt/sign email or verify a subject's PGP signature/key — returns encrypted comms and key/identity verification for opsec; Enigmail itself is now superseded.
url: https://www.enigmail.net/index.php/en
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Encrypting investigator email and verifying PGP-signed messages/keys tied to a subject or persona.
selectorsIn:
- email
selectorsOut:
- email
status: degraded
pricing: free
costNote: Free and open-source. Note that Enigmail no longer supports Thunderbird — modern users should use Thunderbird's built-in OpenPGP or GnuPG directly.
opsec: passive
opsecNote: Encrypting/signing your own mail is a defensive opsec measure. Verifying a subject's public key or signature is passive (offline crypto), but publishing your own key or emailing the subject is an active, attributable step — keep persona keys separate from real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: community
trustNote: OpenPGP is an open standard with strong tooling (GnuPG); Enigmail specifically is legacy — its Thunderbird role was absorbed into the client, so prefer the maintained path.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Enigmail
- PGP
- GnuPG
tags:
- privacy-and-encryption-tools
- opsec
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# OpenPGP (Enigmail)

> Email encryption and signature verification via the OpenPGP standard — an investigator opsec tool, with the caveat that the Enigmail add-on this entry points to is now legacy.

## When to use
Two cases. (1) **Your own opsec:** encrypt/sign sensitive email so case comms can't be read in transit. (2) **Verification:** a subject or persona publishes a PGP `email`/public key or sends a signed message, and you want to confirm the signature and tie a key fingerprint to an identity. OpenPGP is the standard; the tooling below is how you use it. It's a defensive/verification tool, not a discovery source.

## How to use it (`bestInteractionPattern`: desktop-app)
1. **Use the maintained path:** in current Thunderbird, OpenPGP is built in (Enigmail was merged into it) — enable it in Account Settings → End-to-End Encryption. For CLI/other clients, install **GnuPG** (`gpg`).
2. Generate or import your keypair; keep any persona key strictly separate from your real identity.
3. To verify a subject: import their public key, then check a signed message with `gpg --verify` — a good signature ties the message to that key's fingerprint.
4. Compare a claimed key fingerprint against keyservers/prior appearances to corroborate identity reuse across contexts.
5. Pivot: a key's UID `email`/name and fingerprint → search for the same fingerprint elsewhere to link personas.

## Inputs → Outputs
- **In:** your `email`/keypair, or a subject's public key / signed message.
- **Out:** encrypted+signed mail you send; verification results and a key fingerprint/UID (`email`, name) for a subject.
- **Empty/negative result looks like:** a bad/failed signature (message altered or key mismatch), or no key found for an address — meaning the identity isn't confirmed, not that it's fake.

## Gotchas & OpSec
- **Enigmail is legacy:** it dropped Thunderbird support, so don't install the old add-on — use Thunderbird's native OpenPGP or GnuPG. That's why this is `status: degraded`.
- Key UIDs are self-asserted; a matching name/email in a key proves control of the key, not of that real-world identity — corroborate.
- Never sign investigator email with a key linked to your real identity when working a persona.

## Overlaps ("do both")
- Complements persona/sock-puppet tooling: OpenPGP secures and authenticates the comms, while identity-management tools keep the persona's key and footprint separated from your own.

## Trust & verifiability
`trust: community` — OpenPGP/GnuPG are mature, audited, open standards; the Enigmail brand specifically is legacy, so rely on the maintained implementations for anything current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-pgp |
