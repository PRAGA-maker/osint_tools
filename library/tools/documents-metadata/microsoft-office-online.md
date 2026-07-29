---
id: microsoft-office-online
name: Microsoft Office Online
description: Use when you have a suspect Office `document-id` (a .docx/.xlsx/.pptx file or link) and want to open and inspect it safely in-browser — returns embedded `metadata-exif` and author `name` fields.
url: https://www.office.com/start/default.aspx
category: documents-metadata
path:
- documents-metadata
bestFor: Opening and reading Office documents (and their properties) in a sandboxed browser without local software.
selectorsIn:
- document-id
selectorsOut:
- metadata-exif
- name
status: live
pricing: free
costNote: Free web tier (Office on the web) with a Microsoft account; desktop Microsoft 365 is a separate paid product.
opsec: passive
opsecNote: Uploading a target's document to Microsoft's cloud sends its contents to a third party and may leave a copy in your OneDrive. For sensitive evidence prefer an offline viewer; when you do use it, work from a sock-puppet Microsoft account, not your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Microsoft service; renders documents faithfully and exposes the same document properties as desktop Office.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Office on the web
- Office.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- document-metadata
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Microsoft Office Online

> Free browser-based Office (Word/Excel/PowerPoint) — useful as a sandboxed viewer that renders suspect documents and exposes their author/metadata without installing anything.

## When to use
You have an Office file (`.docx`, `.xlsx`, `.pptx`) tied to a subject and want to read it — and inspect its document properties (author, last-modified-by, company, timestamps) — on a machine without desktop Office, or without executing macros locally.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://www.office.com with a sock-puppet Microsoft account.
2. Upload the document (or open a link) into the relevant web app.
3. Read the content in the browser renderer — macros do not auto-execute in the web viewer, so it is safer than opening locally.
4. Open **File → Info / Document properties** to read author `name`, "last modified by", company, and created/modified timestamps (`metadata-exif`).
5. Pivot: feed a recovered author name into people-search, and timestamps/company into corroboration of when and where the file originated.

## Inputs → Outputs
- **In:** `document-id` (an Office file or its link)
- **Out:** `metadata-exif` (author, editors, timestamps, company), author `name`
- **Empty/negative result looks like:** a scrubbed document whose properties are blank or show a generic account — no personal attribution recoverable here.

## Gotchas & OpSec
- Human-in-the-loop: a Microsoft account login is required (`account-login`).
- OpSec: **passive** toward the target, but the file is uploaded to Microsoft's cloud — treat that as disclosure to a third party and keep sensitive evidence offline.
- The web viewer strips/limits macros; do not assume it reveals macro payloads — use a dedicated sandbox for that.

## Overlaps ("do both")
- Pairs with a dedicated document-metadata extractor for a fuller property dump, and with an offline malware sandbox when the file may be weaponised.

## Trust & verifiability
`trust: trusted` — first-party Microsoft rendering; the properties it shows are the document's own embedded fields, which can still be forged, so corroborate before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | microsoft-office-online |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → metadata-exif, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
