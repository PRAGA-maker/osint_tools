---
id: pixel-block
name: PixelBlock
description: Use when you (the investigator) read email in Gmail and want to block tracking pixels so senders can't learn you opened their message — an opsec/counter-surveillance utility, and it also flags which senders track.
url: https://chrome.google.com/webstore/detail/pixelblock/jmpmfcjnflbcoidlgapblgpgbilinlem
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Blocking and flagging email tracking pixels in Gmail to protect your read-status privacy.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension; no account required.
opsec: passive
opsecNote: This is defensive opsec for your side — it stops open-tracking pixels from firing so a sender can't confirm you (or your sock-puppet) opened their email or capture your IP/user-agent at open time. It also shows a marker when a message contains a tracker, which is itself a small intel signal about the sender.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A widely-used (30k+ installs) free Gmail privacy extension; the developer states no personal-data collection, but as with any extension, verify permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Pixel Block
- PixelBlock Gmail
tags:
- privacy-and-encryption-tools
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# PixelBlock

> A Gmail extension that blocks email tracking pixels — so opening a message doesn't quietly tell the sender you read it (and flags who's tracking you).

## When to use
Counter-surveillance opsec, not a lookup. When you correspond from an investigation/sock-puppet Gmail account, senders can embed invisible tracking pixels that fire on open — revealing that you read the mail, when, and sometimes your IP/user-agent. PixelBlock stops those pixels from loading and marks tracked emails with a "red eye," protecting your read-status and giving you a heads-up that a given sender uses tracking.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install PixelBlock into the browser profile you use for your investigation Gmail.
2. It runs automatically — tracking pixels are blocked on incoming mail.
3. Watch for its indicator on messages that contained a tracker (a signal about the sender's tooling/intent).
4. Continue reading email without leaking open-events back to senders.
5. Pivot: knowing a sender tracks opens can inform how you handle correspondence with a target/source.

## Inputs → Outputs
- **In:** none (runs passively over your Gmail)
- **Out:** none as selectors — it prevents leakage and flags tracked messages
- **Empty/negative result looks like:** no indicator on a message means no tracker was detected in it (or it used a technique the extension doesn't catch).

## Gotchas & OpSec
- **Gmail-focused** (Chrome) — it won't protect other clients/webmail; use client-level image blocking there.
- No blocker is total: novel or non-pixel tracking techniques can slip past, so keep "load external images off" as a backstop for sensitive mail.
- It's an extension in your investigation browser — vet its permissions and keep it in a dedicated profile.

## Overlaps ("do both")
- Complements disabling remote-image loading in your mail client and using a VPN — layered, these ensure opening a message leaks neither a read-event nor your IP.

## Trust & verifiability
`trust: community` — a popular, actively-updated privacy extension with a no-data-collection claim; verify its store permissions yourself, since it reads your mail content to detect trackers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pixel-block |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
