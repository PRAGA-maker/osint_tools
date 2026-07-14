---
id: wechat-dump
name: wechat-dump
description: Use when you have lawful access to a subject's rooted Android device and want to decrypt and preserve their local WeChat history — returns associate (contacts), name, and metadata-exif from the message database.
url: https://github.com/ppwwyyxx/wechat-dump
category: messaging
path:
- messaging
- wechat-line
bestFor: Decrypting and exporting the local WeChat message database and media from an authorized/seized rooted Android device.
selectorsIn:
- device-id
selectorsOut:
- associate
- name
- metadata-exif
status: live
pricing: free
costNote: Free and open-source Python tooling; no fees.
opsec: passive
opsecNote: Operates entirely on local device data — no network contact with the target or WeChat servers, so it leaks nothing outward. The gate is legal, not technical: only run it on a device you are lawfully authorized to examine (consent, warrant, or your own device).
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source WeChat forensics project (ppwwyyxx); the decryption approach is documented and widely referenced, though it targets older WeChat Android storage and may not fit current app versions.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- wechatsogou
aliases:
- wechat-dump
- WeChat message decrypt
tags:
- wechat
- forensics
- open-source
- cli
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# wechat-dump

> A device-forensics tool that decrypts and exports the local WeChat message database from a rooted Android phone — for when you lawfully hold the subject's device, not their live account.

## When to use
You have **authorized** physical/forensic access to a subject's Android device (consent, legal seizure, or it's your own) and need their WeChat history — a closed messenger with no external OSINT lookup. wechat-dump decrypts WeChat's local `EnMicroMsg.db` and extracts messages, contacts, and media. In a missing-persons case where the person's phone is recovered, this reconstructs their WeChat contacts (`associate`), display names, and conversation content and timestamps.

## How to use it (`bestInteractionPattern`: cli)
1. On a **rooted** Android device you are authorized to examine, locate WeChat's data directory and pull the encrypted DB and resources.
2. Clone https://github.com/ppwwyyxx/wechat-dump and follow its steps to derive the DB key (from the device IMEI + WeChat uin) and decrypt `EnMicroMsg.db`.
3. Export: it can render chat history to HTML and extract media/voice artifacts.
4. Review the output: contacts (`associate`), display names (`name`), timestamps, and media metadata (`metadata-exif`).
5. Pivot: contact names/IDs feed WeChat-account and cross-platform lookups; media EXIF feeds location analysis.

## Inputs → Outputs
- **In:** `device-id` (the authorized device's WeChat data + IMEI/uin for the key)
- **Out:** `associate` (contacts), `name` (display names), `metadata-exif` (media), decrypted chat history
- **Empty/negative result looks like:** decryption fails or DB not found — usually a WeChat version whose storage differs from what the tool expects, or a non-rooted device. It won't work without root and the correct key inputs.

## Gotchas & OpSec
- **Legal gate:** only for devices you are lawfully authorized to examine — this is forensic extraction of private data.
- Requires **root** and targets older WeChat Android storage; newer versions may not be supported.
- Passive in the network sense (all local), so the risk is legal/ethical, not detection.

## Overlaps ("do both")
- Pairs with `[[wechatsogou]]` — that discovers public WeChat accounts from the outside; wechat-dump reconstructs the private message history from the inside of an authorized device. Different access models for the same platform.

## Trust & verifiability
`trust: community` — a respected open-source forensics project with a documented method. Verify it supports the target's WeChat version, and treat extracted data with the chain-of-custody care its legal context demands.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wechat-dump |
| category | messaging |
| selectorsIn → selectorsOut | device-id → associate, name, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
