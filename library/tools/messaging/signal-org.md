---
id: signal-org
name: Signal Transparency ("Big Brother")
description: Use when your subject uses Signal and you need to know what data is recoverable — the page documents that Signal retains only registration date and last-connection date, nothing more.
url: https://signal.org/bigbrother/
category: messaging
path:
- messaging
bestFor: Calibrating expectations about Signal — confirming that message/contact/metadata content is not obtainable, and that only registration + last-seen dates exist even under legal process.
selectorsIn:
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public transparency page from Signal; no account needed to read it. (Confirming a number is registered on Signal requires the free Signal app.)
opsec: passive
opsecNote: Reading the transparency page is fully passive. If you separately use the Signal app to test whether a number is registered, that check is done from your app install — use a sock-puppet account on a burner number and never initiate a message, which would notify the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party page published by the Signal Foundation, reproducing the actual subpoenas received and Signal's responses; authoritative on what data Signal does and does not hold.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Signal Big Brother
- Signal government requests
tags:
- messengerapps
- Messenger Apps
- transparency
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Signal Transparency ("Big Brother")

> Signal's own record of the subpoenas it receives and the near-nothing it can answer with — the definitive reference for what a Signal-using subject leaves behind.

## When to use
Your subject communicates on Signal and you need to plan realistically. This page (and the reality behind it) tells you that Signal, by design, cannot hand over messages, contacts, group info, profile data or metadata — only "the date and time a user registered" and "the last date of a user's connectivity." Reach for it to (a) set expectations before pursuing a legal-process route that will come back near-empty, and (b) redirect effort toward the endpoints/devices, which are where Signal content actually lives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://signal.org/bigbrother/ and read the published requests and Signal's standardized responses.
2. Note the only two fields Signal can produce: account registration timestamp and last-connectivity timestamp.
3. Conclude what is NOT available: no message content, no contact lists, no metadata — everything else is end-to-end encrypted.
4. Practical adjunct: to check whether a `phone` number is even on Signal, add it as a contact in a sock-puppet Signal app; a Signal-registered number shows as reachable. Do NOT send a message.
5. Pivot: since server-side data is minimal, focus on device forensics, iCloud/Google backups of the app, and human sources; use `[[account-live-com]]`-style checks for the linked identity.

## Inputs → Outputs
- **In:** `phone` (a number you suspect uses Signal)
- **Out:** confirmation that a number is a registered Signal account (`social-profile` existence) and the knowledge that no further server-side content is obtainable
- **Empty/negative result looks like:** a number not registered on Signal (the app shows it as not reachable via Signal), or — for the transparency page — simply the standing conclusion that Signal holds no content to disclose.

## Gotchas & OpSec
- Don't over-read: registration/last-seen dates are only obtainable by Signal via valid legal process, not by you directly.
- The app-based existence check must use a sock-puppet number and must never message the target.
- OpSec: passive for the page; the app check is low-touch but still originates from your install.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` and phone-OSINT — Signal confirms the number is active/used; other tools attach an identity to it.
- Pairs with device-forensics and cloud-backup workflows, which are where Signal message content is actually recoverable.

## Trust & verifiability
`trust: trusted` — an authoritative first-party disclosure from the Signal Foundation, reproducing genuine legal requests; it is the reference of record for Signal's (minimal) data retention.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | signal-org |
