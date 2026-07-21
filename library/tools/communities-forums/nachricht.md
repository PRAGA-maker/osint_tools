---
id: nachricht
name: Nachricht
description: Use when you (as investigator) need to send a source or tipster a one-time, self-destructing encrypted message via a shareable link — an OpSec comms utility, not a lookup/discovery tool.
url: https://nachricht.co/
category: communities-forums
path:
- communities-forums
bestFor: Sending a burn-after-reading encrypted note to a contact without leaving a stored, server-readable copy.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free service; no account, no payment.
opsec: passive
opsecNote: Designed for OpSec: AES-256, key in the URL, no personal data or IP stored, message self-destructs after one read (unread notes auto-delete in ~48h). Anyone with the link can read it once, so send the link over a separate secure channel and never include case-identifying detail beyond what the recipient needs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 2014) privnote-style ephemeral-message service; reputable for its niche, but a closed-source third party you must take on trust for the "we store nothing" claim.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- nachricht.co
tags:
- secure-messaging
- ephemeral
- opsec
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Nachricht

> A burn-after-reading encrypted note service — an investigator OpSec/comms utility for reaching a source, not a tool for finding information about a subject.

## When to use
You need to pass something sensitive to a **source, tipster, or teammate** — a meeting detail, a link, a short instruction — without it persisting on a server or in an inbox. Nachricht generates a one-time, self-destructing, AES-256-encrypted note behind a shareable link. It appears in OSINT tool lists for its OpSec value; it does **not** search, scrape, or reveal anything about a target, so it holds no discovery value on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nachricht.co/.
2. Type the message and set a deadline (2 hours to 14 days).
3. Generate the unique link; the decryption key rides in the link fragment (the server can't read the content).
4. Send the link to your recipient over a *separate* secure channel (Signal, in person) — whoever opens it first reads it once, then it self-destructs (unread notes auto-delete in ~48h).
5. There is no pivot: the tool produces no intelligence, only a delivered-or-not outcome.

## Inputs → Outputs
- **In:** plaintext you type (no target selectors)
- **Out:** a single-use encrypted link; the recipient gets the message once, then it's gone
- **Empty/negative result looks like:** the recipient sees "message already read / expired" — someone (possibly an interceptor) already opened it, or the deadline passed.

## Gotchas & OpSec
- **Not a lookup tool** — it finds nothing about anyone; its MP relevance is purely operational (secure contact with sources).
- One-read model doubles as tamper-evidence: if your recipient gets "already read", assume interception and rotate the channel.
- Closed-source and third-party — the no-logs/no-IP claims are unverifiable; for high-stakes comms prefer end-to-end tools you control.

## Overlaps ("do both")
- Comparable to other ephemeral-note services (privnote-style); pick one and pair it with an out-of-band channel to deliver the link.

## Trust & verifiability
`trust: community` — an established, well-known ephemeral-message service, but you are trusting its unverifiable privacy claims; treat it as convenience-grade OpSec, not guaranteed security.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nachricht |
| category | communities-forums |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
