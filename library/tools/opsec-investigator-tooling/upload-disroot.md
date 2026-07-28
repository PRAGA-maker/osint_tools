---
id: upload-disroot
name: Upload | Disroot
description: Use when you need to share an evidence file with a source or teammate via a privacy-respecting, expiring link — an investigator OpSec transfer tool, not a lookup on a subject.
url: https://disroot.org/en/services/upload
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Uploading a file to get a self-destructing, optionally password-protected share link from a privacy-focused non-profit host.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, no account; run by the Disroot non-profit collective (donation-supported). Per-file size and retention limits apply.
opsec: passive
opsecNote: Protects your workflow, not a target — it lets you move a file without a Big-Tech account or link tracking. Set an expiry and, for sensitive files, a password and client-side encryption; a plain link is still guessable-by-whoever-has-it. Don't upload material you're not authorized to hold, and remember Disroot's servers process the file in transit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Disroot is an established privacy-focused non-profit running libre services (this is their Lufi-based upload); trustworthy operator, but it's still third-party hosting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Disroot Upload
- Disroot Lufi
tags:
- opsec
- file-sharing
- privacy
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Upload | Disroot

> A privacy-respecting file-drop from the Disroot non-profit — hand someone an expiring, optionally encrypted download link without spinning up a Google/Dropbox account. OpSec plumbing, not subject research.

## When to use
You need to move an evidence file, a document, or a media capture to a source, a teammate, or another machine, and you'd rather not route it through a Big-Tech account tied to you or one that trackers/links can profile. Disroot's upload service gives you a shareable link with an expiry (and optional password/encryption). It's about how *you* transfer files safely; it returns no data about any subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://disroot.org/en/services/upload (their Lufi-based uploader; no account needed).
2. Drag in the file; set an **expiry** (delete-after time or after-first-download) and, for sensitive files, a **password** / enable client-side encryption.
3. Copy the generated link (and password, shared over a separate channel).
4. Send it to your recipient; the file self-destructs per your expiry setting.

## Inputs → Outputs
- **In:** none (you upload your own file; you supply nothing about a target)
- **Out:** an expiring, optionally password-protected share link (operational, not a harvested selector)
- **Empty/negative result looks like:** upload refused for exceeding the size/retention limit, or an expired link returning "not found" — expected behaviour, not a fault.

## Gotchas & OpSec
- Set an **expiry** and a **password** for anything sensitive — a bare link is accessible to anyone who obtains it.
- It's still third-party hosting: the file passes through Disroot's servers; use client-side encryption for material that must stay confidential.
- Size/retention limits apply; large evidence sets may need another channel.
- Only upload files you're authorized to handle.

## Overlaps ("do both")
- Pairs with encryption tools (encrypt locally first) and other privacy hosts: encrypt the file, then use Disroot's expiring link so neither the host nor an intercepted link exposes the contents.

## Trust & verifiability
`trust: community` — Disroot is a well-regarded privacy-focused non-profit running libre software. The operator is trustworthy, but treat it as third-party hosting: encrypt sensitive files and rely on expiry, not obscurity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | upload-disroot |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
