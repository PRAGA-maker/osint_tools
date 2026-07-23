---
id: off-the-record-instant-messaging-plug-in
name: Off-The-Record (OTR) Instant Messaging Plug-In
description: Use when you need end-to-end encrypted, deniable IM for investigator communications over XMPP/Pidgin — provides encryption, authentication, deniability and forward secrecy (not an investigative lookup).
url: https://otr.cypherpunks.ca/index.php
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Adding encrypted, deniable, forward-secret messaging to a desktop IM client for secure investigator-to-investigator comms.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free and open source (libotr / pidgin-otr under GPL).
opsec: passive
opsecNote: This is a defensive comms tool for the investigator, not a way to query a target. It encrypts your own IM traffic; metadata (who you talk to, when) is still visible to the network. The project's last release (libotr 4.1.1, pidgin-otr 4.0.2) dates to 2016 — mature but no longer actively developed, so prefer a modern Signal/Matrix-based channel for new setups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: OTR is a well-studied academic protocol (Borisov, Goldberg, Brewer) and libotr is a long-established open-source reference implementation; the code is auditable and widely reviewed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- OTR
- pidgin-otr
- libotr
- Off-the-Record Messaging
tags:
- toddington
- encryption
- opsec
- messaging
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Off-The-Record (OTR) Instant Messaging Plug-In

> A plug-in (libotr / pidgin-otr) that adds encrypted, authenticated, deniable, forward-secret messaging on top of a desktop IM client.

## When to use
You need a secure back-channel to talk to a co-investigator or source over instant messaging and want encryption plus **deniability** (no third-party-verifiable signatures) and **forward secrecy** (past chats stay safe if a key later leaks). This is investigator OpSec — it protects your own communications; it does not find or enrich anything about a subject.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install a supported IM client (e.g. Pidgin) and add the OTR plug-in: `sudo apt install pidgin-otr`, or build libotr from the source at the URL.
2. In the client, enable the Off-the-Record Messaging plug-in and generate your private key.
3. Start a conversation with your contact, then click "Start private conversation" to negotiate OTR.
4. Verify your contact out-of-band using the Socialist Millionaire Protocol (a shared secret) or fingerprint comparison — this defeats man-in-the-middle.
5. Confirm the session shows "private/verified" before exchanging anything sensitive.

## Inputs → Outputs
- **In:** none (a communications tool, not a selector lookup)
- **Out:** an encrypted, authenticated IM session
- **Empty/negative result looks like:** the session stays "not private" / "unverified" — your contact's client lacks OTR or negotiation failed; do not treat the channel as secure.

## Gotchas & OpSec
- **Metadata leaks:** OTR hides message *content*, not *who/when* — the underlying network still sees your contact graph and timing.
- **Stale project:** last updated 2016; fine for existing setups but for new secure comms prefer Signal or a Matrix/OMEMO client.
- Always verify the contact's fingerprint out-of-band; unverified sessions are MITM-able.

## Overlaps ("do both")
- Complements full-disk/VM OpSec and VPN/Tor — OTR secures the message layer while those secure the storage and network layers; combine them for a clean investigator footprint.

## Trust & verifiability
`trust: trusted` — OTR is a peer-reviewed protocol with an open, long-audited reference implementation; the encryption guarantees are well established even though the project is now in maintenance-only status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | off-the-record-instant-messaging-plug-in |
