---
id: safenote
name: SafeNote
description: Use when you have found a `safenote.co` link in a subject's trail and want to read it — opens a one-time, self-destructing encrypted note (you likely get a single view).
url: https://safenote.co/
category: communities-forums
path:
- communities-forums
bestFor: Opening a specific self-destructing SafeNote link you already possess; NOT a searchable index (encrypted, one-time, link-only).
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free web service; no account, password or email required to read or create a note.
opsec: passive
opsecNote: SafeNote notes are end-to-end encrypted and self-destruct after one view or on expiry, so opening a link consumes it — the sender/recipient loses access afterward, and reading it may tip off that it was opened. Open in a sandbox, snapshot immediately, and never paste a target's data into it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A privacy-focused self-destructing-note service (Privnote-style). The encryption/expiry model is its stated design; you must trust the operator not to tamper. Content is anonymous unless the sender added identifying info.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- safenote.co
- Safenote secure notes
tags:
- pastebins
- self-destructing
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# SafeNote

> A self-destructing, end-to-end-encrypted note service — for OSINT it is a one-shot *decoder*: you can open a SafeNote link you already have, but it burns after one view and cannot be searched.

## When to use
You have found a `safenote.co/...` link (in a message, a bio, a dump) and need to read it before it self-destructs. Because notes are encrypted, link-only, and delete themselves after one view or a set expiry, you cannot search SafeNote for a subject's data, and opening the link likely gives you exactly one chance to read it. Treat this as a time-critical, one-time read, not a discovery source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Have the complete SafeNote URL ready; decide before opening that you are ready to capture it (you may only get one view).
2. Open it in a sandboxed/sock-puppet browser.
3. Immediately screenshot/copy the content — the note may self-destruct on this view and be unrecoverable.
4. Be aware that opening it consumes the note, so the intended recipient may notice it was read early; weigh that against your objective.
5. Pivot: any selectors inside (credentials, handles, addresses) feed the relevant breach-check/username tools.

## Inputs → Outputs
- **In:** `document-id` (a complete SafeNote link you already hold)
- **Out:** the decrypted note text/file (`document-id` content), captured before it self-destructs
- **Empty/negative result looks like:** "this note has been destroyed / expired" — it was already viewed or timed out; there is no server copy to recover.

## Gotchas & OpSec
- Human-in-the-loop: none, but the single-view/self-destruct behaviour makes capture time-critical.
- OpSec: **passive** to read, but opening burns the note and may alert the recipient. Snapshot instantly; never create SafeNotes containing a target's data.
- Not searchable or indexed — useless for proactive discovery; it only decodes a link you already have.

## Overlaps ("do both")
- Behaves like [[verybin]], [[defuse]] and [[nopaste]] (encrypted, link-only) but with an added one-time self-destruct; pair with indexed leak/pastebin search when the goal is to *find* a subject's data.

## Trust & verifiability
`trust: community` — a real privacy service whose self-destruct/encryption model is as described; the decrypted content is authentic to what was sent, subject to trusting the operator not to tamper.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | safenote |
| category | communities-forums |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
