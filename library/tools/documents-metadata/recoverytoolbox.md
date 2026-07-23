---
id: recoverytoolbox
name: Recovery Toolbox
description: Use when you have a corrupted or damaged file (document, archive, image, mailbox) and want to repair it enough to extract its contents and `metadata-exif` — returns recovered text/images/metadata.
url: https://recoverytoolbox.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Repairing corrupted evidence files (Office docs, RAR/ZIP, PDF, PST mailboxes, images) to recover readable content.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free online repair previews and three freeware desktop tools (File Undelete, Mail Undelete, CD/DVD recovery); full recovery/export of most repair tools is paid.
opsec: passive
opsecNote: The ONLINE repair service uploads your file to Recovery Toolbox's servers — never send sensitive/evidential material that way. For anything confidential use the offline desktop tools so the file never leaves your machine. Passive toward any subject.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running commercial ISV (since 2003); legitimate but third-party, and the online tier requires uploading your file to them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- exiftool
aliases:
- RecoveryToolBox
- recoverytoolbox.com
tags:
- Files
- file-repair
- data-recovery
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Recovery Toolbox

> A suite of file-repair utilities — the fallback when a piece of evidence (a mailbox, an Office doc, a damaged image) won't open and you need its contents and metadata.

## When to use
You have a corrupted file that matters to a case — a PST/OST mailbox, a truncated JPEG, a broken ZIP/RAR of documents, a damaged Office file or PDF — and standard applications refuse to open it. Recovery Toolbox's per-format repairers can often reconstruct enough to read the text, extract embedded images, or recover a mailbox's messages (and with them their headers and `metadata-exif`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://recoverytoolbox.com/ and pick the tool matching the file type (Excel, Word, PDF, RAR, ZIP, Outlook, photo, etc.).
2. Choose the **offline desktop app** for sensitive files, or the **online service** only for non-confidential ones.
3. Load the corrupted file; the tool analyses it and shows a preview of recoverable content for free.
4. Read the recovered content/metadata in the preview. Full export/save of the repaired file usually requires a paid licence.
5. Pivot: recovered images → run through `[[exiftool]]` for EXIF/GPS; recovered mailbox → mine headers for addresses and IPs.

## Inputs → Outputs
- **In:** a corrupted file (image, document, archive, mailbox)
- **Out:** recovered readable content, extracted images, and their `metadata-exif`/headers
- **Empty/negative result looks like:** the preview shows nothing recoverable, or the file type isn't supported — the corruption is too severe or it's the wrong tool.

## Gotchas & OpSec
- Human-in-the-loop: the free tier previews but paywalls the actual export of most repairers — the preview is often enough to read what you need.
- OpSec: the **online** service uploads your file to a third party. For evidential or confidential material, use only the offline desktop tools.
- It repairs, not forensically preserves — work on a copy and keep the original untouched for chain-of-custody.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` — Recovery Toolbox gets a broken file open again; ExifTool then extracts the metadata/GPS from whatever images or documents you recovered.

## Trust & verifiability
`trust: unverified` — a legitimate, long-established commercial vendor, but third-party software with a paid tier and an upload-based online mode; verify recovered content against the case rather than trusting the tool blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recoverytoolbox |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
