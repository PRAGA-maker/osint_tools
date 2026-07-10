---
id: wechat-text-backup
name: wechat-text-backup
description: Use when you have local access to a subject's Windows WeChat data and want to decrypt and export their chat history — returns readable message archives (contacts, timestamps, message text).
url: https://github.com/zhaofeng-shu33/wechat-text-backup
category: messaging
path:
- messaging
- wechat-line
bestFor: Decrypting and exporting the local (Windows) WeChat SQLite message databases into readable chat history.
selectorsIn: []
selectorsOut:
- associate
status: degraded
pricing: free
costNote: Free and open-source (GitHub). Requires local Python/toolchain and a Windows debugger; no paid service.
opsec: active
opsecNote: This is a forensic action against a device you must already lawfully control — it reads and decrypts local WeChat databases and requires extracting a 32-byte key from WeChat's process memory with a debugger. Only run on an image/device you are authorized to examine; never against an account or device you don't own or have legal authority over.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: A community GitHub forensics utility; works only for specific older WeChat Windows versions and is not a maintained commercial product — verify on a test dataset before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- wechat text backup
tags:
- wechat
- forensics
- chat-export
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# wechat-text-backup

> A GitHub forensics utility that decrypts the local Windows WeChat databases and exports readable chat history — device-forensics only, not a remote lookup.

## When to use
You have lawful local access to a subject's Windows machine or a forensic image of it, and you need to recover their WeChat conversations — contacts, timestamps, and message text — that are otherwise stored in encrypted SQLite databases. This is an on-device forensics step, not something you run against a live/remote account.

## How to use it (`bestInteractionPattern`: cli)
1. On the authorized Windows host (or image), locate the WeChat data directory containing the encrypted `.db` files (e.g. `MSG*.db`).
2. Extract the 32-byte database key from WeChat's process memory: attach a debugger (x64dbg), search string references in `wechatwin.dll`, and read the key from the register — the README's `decrypt.md` documents the procedure and notes an old WeChat build (e.g. 2.6.8.x / 2.8.0.112) is often needed.
3. Use the repo's scripts (`copy.sh`, `extract.py`) with the recovered key to decrypt and export the messages.
4. Review the exported text; named contacts/participants become `associate` leads.

## Inputs → Outputs
- **In:** local encrypted WeChat database files + the in-memory decryption key (obtained on-device)
- **Out:** decrypted, readable chat history — contacts (`associate`), timestamps, message content
- **Empty/negative result looks like:** decryption fails or only `Multi/MSG0.db` partially decrypts — expected on WeChat 2.9+, which the tool doesn't fully support. Failure usually means a version/key mismatch, not absence of data.

## Gotchas & OpSec
- **Version-fragile:** reliable only for specific older WeChat Windows builds; 2.9+ yields partial/no decryption.
- Requires obtaining a key from live process memory — you need the running client or a memory capture, plus debugger skill.
- Strictly for authorized device forensics; unauthorized use is unlawful. Human review of exported content is required.

## Overlaps ("do both")
- Pairs with mobile WeChat forensics (Android `EnMicroMsg.db` decryption) and general chat-app extraction tools — this covers the Windows client; the phone holds the fuller record.

## Trust & verifiability
`trust: community` — an unmaintained-risk GitHub utility. Validate its output against a known test conversation before relying on any extracted message as evidence.
