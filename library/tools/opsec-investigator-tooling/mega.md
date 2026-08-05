---
id: mega
name: MEGA
description: Use when you have a MEGA share link (from a breach dump, dark-web post, or a subject's shared folder) and want to inspect/preserve its contents — or need encrypted storage for case files.
url: https://mega.io/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Accessing/preserving files behind MEGA share links, and end-to-end-encrypted storage for your own case data.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier gives several GB of encrypted storage (periodically adjusted); paid plans add capacity and transfer.
opsec: passive
opsecNote: Opening a MEGA link decrypts client-side using the key in the URL fragment, so MEGA's server does not see contents — but visiting still connects your IP to MEGA and, for a private link, may signal the sharer that it was accessed. Use a sock-puppet account and VPN. Never upload a victim's private data to a third-party cloud, and treat downloaded files as potentially hostile.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: MEGA is a large, established end-to-end-encrypted cloud provider; the platform is legitimate, though the content behind any given link is user-supplied and unvetted.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
aliases:
- MEGA.nz
- MEGA.io
tags:
- cloud-storage
- file-hosting
- encrypted-storage
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# MEGA

> A major end-to-end-encrypted cloud-storage service — in OSINT it shows up two ways: as the host behind leaked/shared MEGA links you need to inspect, and as encrypted storage for your own evidence.

## When to use
Two cases. First (investigative): you have a `mega.nz` share URL surfaced in a breach dump, a dark-web forum post, or a subject's public profile, and you need to open, review, and preserve what it holds. Second (OpSec/utility): you need encrypted, off-machine storage for case files that only you can decrypt. MEGA does not find people; it stores and serves files, and the link is your lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. For a share link: open it in a sock-puppet browser over a VPN. The decryption key rides in the URL after `#` — without it, nothing decrypts.
2. Review the file/folder listing; download only what you need, into an isolated environment.
3. Preserve: hash downloaded files and record the capture time; links are often deleted quickly.
4. For your own storage: register a free account and upload case files (never a victim's private data to a third-party cloud).
5. Pivot: filenames, embedded metadata (EXIF, document authors), and folder structure feed document-metadata analysis and can identify the sharer.

## Inputs → Outputs
- **In:** a MEGA share link (with key) — or your own files to store
- **Out:** the shared files/folders; no personal selectors of its own, but the contents may carry many
- **Empty/negative result looks like:** "the folder you are trying to access has been terminated/removed" or a missing decryption key — the link is dead or you have only half of it.

## Gotchas & OpSec
- Human-in-the-loop: downloading large sets or using storage needs an account/login; browsers throttle big transfers.
- OpSec: content decrypts client-side (server-blind), but access still ties your IP to MEGA and may alert a private sharer. Use puppet + VPN; sandbox downloads.
- The decryption key is part of the URL — a link without the `#...` fragment is useless; preserve the full link.

## Overlaps ("do both")
- Pairs with document-metadata/EXIF tools and archive tools — MEGA delivers the files; those tools mine authorship, timestamps, and geolocation, and you archive copies before the link vanishes.

## Trust & verifiability
`trust: trusted` — MEGA the platform is reputable and its crypto is well-documented; the *content* behind any link, however, is unvetted user data — verify and handle it as untrusted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mega |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
