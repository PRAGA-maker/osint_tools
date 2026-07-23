---
id: wetransfer
name: WeTransfer
description: Use when you need to receive or send large files during an investigation (evidence, media, documents) — a free no-account file-transfer service; also the source of shared links you may need to analyse.
url: https://www.wetransfer.com
category: documents-metadata
path:
- documents-metadata
bestFor: Free ad-hoc transfer of large files to/from a collaborator or source.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier transfers up to ~2GB without an account (links expire, historically ~3 days); paid plans add larger sizes, longer retention and password protection.
opsec: passive
opsecNote: Files uploaded to WeTransfer sit on its servers and the download link is a bearer token — anyone with the link can fetch it. Never transfer sensitive material unencrypted; encrypt first, share the link and passphrase out-of-band, and use a sock-puppet email so transfers aren't tied to your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A mainstream commercial file-transfer service; reliable for delivery, but a third-party host — treat anything uploaded as leaving your control.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- wetransfer.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- file-transfer
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# WeTransfer

> No-friction big-file transfer: send or receive up to ~2GB with just an email and a link — and the platform behind many shared links you'll be handed.

## When to use
You need to move large files in an investigation — send collected media/evidence to a colleague, or receive a document/photo set from a source or tipster — without a shared account or cloud setup. WeTransfer's free, no-registration transfer is the low-friction option. You'll also encounter WeTransfer links as *inputs*: a source shares one, and you need to retrieve and preserve its contents before it expires.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.wetransfer.com. To send: add files (≤~2GB free), enter recipient + your email (sock-puppet), and send — the recipient gets a download link.
2. To receive: open the WeTransfer link you were given and download promptly — free links expire (historically ~3 days).
3. Preserve incoming files immediately: download, hash, and record the link + timestamp for chain-of-custody, since the link will die.
4. For sensitive content, encrypt the files locally first and share the passphrase over a separate channel.
5. Pivot: analyse received files (metadata/EXIF, OCR, media) as the next step.

## Inputs → Outputs
- **In:** files to send, or a WeTransfer download link to retrieve
- **Out:** a shareable download link (sending) / the downloaded files (receiving)
- **Empty/negative result looks like:** an expired or "transfer not found" link — free transfers are short-lived; a dead link usually means it lapsed, so always grab shared files immediately.

## Gotchas & OpSec
- Links are bearer tokens — anyone with the URL can download; treat them as secrets and don't post them anywhere indexable.
- Free transfers expire quickly — retrieve and preserve at once.
- OpSec: uploaded files leave your control onto a third-party server; encrypt sensitive material and use a sock-puppet email.

## Overlaps ("do both")
- Complements downloaders/preservation tools — once you've received files via WeTransfer, run metadata/EXIF and OCR analysis on them before the link expires.

## Trust & verifiability
`trust: unverified` — a reliable mainstream transfer service, but a third-party host; it delivers files faithfully, yet anything uploaded should be considered outside your control.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wetransfer |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
