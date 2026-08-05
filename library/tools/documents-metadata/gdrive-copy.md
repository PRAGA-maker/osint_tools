---
id: gdrive-copy
name: Gdrive-copy
description: Use when you have a shared Google Drive folder you need to preserve or clone (you cannot copy folders natively) — returns a full copy owned by you, with subfolders and files.
url: https://script.google.com/macros/s/AKfycbxbGNGajrxv-HbX2sVY2OTu7yj9VvxlOMOeQblZFuq7rYm7uyo/exec
category: documents-metadata
path:
- documents-metadata
bestFor: Cloning an entire shared Google Drive folder tree into your own account for preservation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free open-source Google Apps Script web app (ericyd/gdrive-copy); no payment, only Google OAuth.
opsec: active
opsecNote: Copying reads the source folder with YOUR authenticated Google account — the copy operation and access can appear in the owner's Drive activity/audit log if they own or watch the folder. To preserve evidence quietly, prefer downloading files individually, or use a dedicated sock-puppet Google account that you have deliberately given access. The app itself stores no data about your account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by ericyd; the source is public on GitHub and the app declares it stores no user data, but you are granting a third-party Apps Script broad Drive OAuth scope — review before authorizing.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- gdrive-copy
- Google Drive folder copier
tags:
- Files
- evidence-preservation
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Gdrive-copy

> An open-source web app that does the one thing native Drive cannot — recursively copy an entire shared folder (subfolders and all) into an account you control, for preservation.

## When to use
You have located a subject's or organization's shared Google Drive folder (leaked link, public share, a folder you have been given access to) and you want your own snapshot before it can be edited or revoked. Native Drive only lets you copy individual files; gdrive-copy walks the whole tree. It is a preservation utility, not a lookup — it does not find anything, it captures what you already found.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the app URL and sign in with the Google account (ideally a sock puppet) that will own the copy.
2. Authorize the Drive OAuth scope, then paste the source folder's share URL/ID.
3. Click "Copy Folder"; the job runs server-side and you can close the tab. You become owner of the new folder and all contents.
4. Preserve: hash and archive the copied files; note the capture time.
5. Pivot: metadata inside the copied documents (authors, timestamps, EXIF) feeds document-metadata analysis.

## Inputs → Outputs
- **In:** a Google Drive folder URL/ID you can access
- **Out:** a full duplicated folder tree owned by your account — no personal selectors of its own
- **Empty/negative result looks like:** the job stalls or partially copies on very large folders (Apps Script quotas), or fails if your account lacks access — not an intelligence result, a permissions/quota issue.

## Gotchas & OpSec
- Human-in-the-loop: Google login and OAuth consent are required.
- OpSec: this is **active** — you read the source with a real Google identity, which can surface in the owner's audit trail. Use a puppet account and consider per-file download for stealth.
- Broad OAuth scope: you are trusting a third-party Apps Script with Drive access; the code is open source, but treat it accordingly and revoke the grant afterward.

## Overlaps ("do both")
- Pairs with any document-metadata/EXIF workflow — gdrive-copy captures the files; the metadata tools then mine authorship, timestamps, and geolocation out of them.

## Trust & verifiability
`trust: community` — a transparent open-source tool that reliably does what it claims; the trust caveat is the OAuth grant you must give it, not the copy fidelity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gdrive-copy |
| category | documents-metadata |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
