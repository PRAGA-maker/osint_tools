---
id: zerobin
name: ZeroBin
description: Use when you find a ZeroBin/PrivateBin paste link in a subject's messages, or need to share case data securely — a zero-knowledge, browser-encrypted pastebin whose content is only readable with the full URL + key.
url: https://sebsauvage.net/paste/
category: communities-forums
path:
- communities-forums
bestFor: Recognising and opening client-side-encrypted paste links, and sharing sensitive findings without the server (or a subpoena of it) being able to read them.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free and open-source. This original instance (sebsauvage.net/paste) is explicitly a "test service — data may be deleted anytime"; for real use, self-host or use a maintained PrivateBin instance.
opsec: passive
opsecNote: Content is AES-256 encrypted/decrypted in the browser — the server has zero knowledge of the plaintext, and the decryption key lives in the URL fragment (after #), which is never sent to the server. Anyone with the full link can read it, so treat the link itself as the secret and share it out-of-band.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ZeroBin (by Sébastien Sauvage) is the original open-source client-side-encrypted pastebin; it has largely been superseded by its actively-maintained fork, PrivateBin. The code model is well understood; this specific test instance is not guaranteed persistent.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- 0bin
- PrivateBin
- zero-knowledge pastebin
tags:
- pastebins
- opsec
- encrypted
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# ZeroBin

> A zero-knowledge, browser-encrypted pastebin — the server can't read the paste, and the decryption key rides in the URL fragment.

## When to use
Two cases. **Recognising it:** you find a ZeroBin/PrivateBin-style paste link in a subject's chats, emails, or a forum post and need to understand it — the content is encrypted and only openable with the *complete* URL including the part after the `#`; without that fragment there's nothing to recover, and the server holds no plaintext to request. **Using it:** you need to hand teammates sensitive case material without a third-party server being able to read it (or being compellable to hand over readable data). Note: you cannot *search* other people's ZeroBin pastes — it has no index — so it is not a monitorable source; its value is link comprehension and secure sharing rather than as a searchable lead source.

## How to use it (`bestInteractionPattern`: web-manual)
1. **To read a found link:** open the *entire* URL including everything after the `#`. If the fragment (the key) is missing or truncated, the paste is unrecoverable — note that in your record.
2. **To share securely:** open the paste service, paste your text, set an expiry / "burn after reading" if desired, and create the paste.
3. Copy the resulting full link (with the `#key`) and send it to your recipient over a separate secure channel — the link *is* the password.
4. Prefer a maintained **PrivateBin** instance or a self-hosted one over this original test instance, which may delete data at any time.
5. Pivot: a paste link found on a subject → try to obtain the full URL (with key) from where it was shared; a leaked paste's content → treat as any other document lead.

## Inputs → Outputs
- **In:** none as a *source* (no search); as a tool, the text you paste or a full paste URL you were given
- **Out:** an encrypted paste + shareable link (creating), or the decrypted content (opening a link with its key)
- **Empty/negative result looks like:** a link without its `#` fragment, or after expiry/burn, yields nothing decryptable — that's by design, not a bug; there is no server-side copy to recover.

## Gotchas & OpSec
- **Not searchable:** you cannot enumerate or monitor others' ZeroBin pastes — do not treat it as a breach/paste *source* like a public pastebin.
- The key is in the URL fragment: anyone with the full link can read the content, and a shortened/logged link can leak the key — share links carefully and out-of-band.
- This original instance is a "test service" that may delete data anytime; use PrivateBin or self-host for anything you need to persist.

## Overlaps ("do both")
- Contrast with public, indexed paste sites (`[[pastebin-com]]`-style) — those are *searchable sources* you monitor for leaks; ZeroBin is the opposite (unsearchable, encrypted) and is a link-comprehension / secure-sharing tool, not a source.

## Trust & verifiability
`trust: community` — the open-source zero-knowledge model is well understood and its successor PrivateBin is actively maintained; this particular demo instance is explicitly non-persistent, so rely on the model, not this URL, for anything durable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zerobin |
| category | communities-forums |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
