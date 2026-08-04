---
id: lockbin
name: Lockbin
description: Use when you need to send sensitive findings/files to a recipient securely — returns an encrypted, browser-accessible message the recipient opens without an account (an OpSec delivery tool).
url: https://lockbin.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Sending an encrypted one-off message or file to someone without either side standing up a secure-mail system.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier ("10 messages free, no card required"); paid plans for higher volume/compliance features. Aimed at HIPAA-style secure email but usable for any sensitive one-off delivery.
opsec: passive
opsecNote: This is a defensive delivery tool, not a lookup — it never touches your target. Note that Lockbin (the service) processes your message metadata and recipient contact, so it is a trusted third party in the chain; for the highest-sensitivity material prefer end-to-end tools you control. Recipients open messages via an emailed/SMS browser link.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial secure-messaging service marketed for healthcare/finance; encryption claims are the vendor's own and not independently audited here, so treat trust as commercial-grade, not verified end-to-end.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Lockbin secure email
tags:
- privacy-and-encryption-tools
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Lockbin

> A secure send-and-forget message/file service — the OpSec *delivery* side of investigative work: get a sensitive report or document to a recipient encrypted, without either party running their own secure-mail stack.

## When to use
Not a discovery tool. Reach for it when you have sensitive material — a report, a document, credentials to hand off — and need to send it to someone (a client, a colleague, a tip line) more safely than plain email, and the recipient can't or won't install anything. Lockbin delivers an encrypted message the recipient opens in a browser via a one-time link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lockbin.com and compose a secure message (attach files if needed).
2. Set the recipient's email/phone; Lockbin encrypts the payload and notifies them.
3. The recipient opens the message over HTTPS through the emailed/SMS link — no account needed on their end.
4. Track the free-tier quota (10 messages) or upgrade for volume.
5. Pivot: use as the outbound-comms layer of an engagement; keep the actual investigative data in tools you control.

## Inputs → Outputs
- **In:** none (your own message/file content — no subject selector)
- **Out:** a delivered encrypted message/file — a capability, not data about a person
- **Empty/negative result looks like:** N/A — failure is a bounced/unopened link (wrong contact) rather than a "no result."

## Gotchas & OpSec
- **Third party in the loop:** Lockbin brokers the message, so it is a trust dependency; for maximum sensitivity use end-to-end encryption you control (e.g. PGP/age) instead.
- Encryption is the vendor's implementation and not independently verified here — treat as commercial-grade transport security, not audited E2EE.
- It's a *sending* tool; it returns nothing investigative and belongs in your OpSec/comms workflow, not your collection workflow.

## Overlaps ("do both")
- Complements the privacy/encryption tooling in this library — pair with your own PGP/age keys for content you must not entrust to a broker, and with a hardened browser like [[gnu-icecat]] on the sending side.

## Trust & verifiability
`trust: community` — an established commercial service, but its encryption is self-attested; suitable for routine sensitive delivery, not as a verified end-to-end guarantee for high-threat material.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lockbin |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
