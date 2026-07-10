---
id: scribd
name: Scribd
description: Use when you have a `name`, `email` or `employer-org` and want documents mentioning them — returns uploaded PDFs/spreadsheets/resumes that can leak addresses, IDs and associates.
url: https://www.scribd.com/
category: image-video-face
path:
- image-video-face
- documents
- search
bestFor: Searching a huge library of user-uploaded documents (resumes, court filings, spreadsheets, manuals) for a subject's name or identifiers.
selectorsIn:
- name
- email
- employer-org
selectorsOut:
- document-id
- metadata-exif
- address
- associate
status: live
pricing: freemium
costNote: Searching and previewing is free; full document download/reading often requires a paid subscription or an upload-to-unlock, though many documents are fully public.
opsec: passive
opsecNote: Searching Scribd is passive and doesn't alert anyone. If you download, that ties to your account; use a sock-puppet account. Prefer viewing via Google cache/`site:scribd.com` to avoid logging in.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Scribd is a legitimate large document-hosting platform; documents are user-uploaded so authenticity varies — a leaked or scanned document must be verified, not taken at face value.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-reverse-image-search
aliases:
- scribd.com
tags:
- documents
- document-search
- pdf
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Scribd

> A massive library of user-uploaded documents — resumes, court filings, spreadsheets, manuals, contact lists — searchable for a subject's name or identifiers, which can leak addresses, IDs and associates buried in files.

## When to use
You have a `name`, `email`, or `employer-org` and want documents that mention them. People and organisations upload (or accidentally expose) resumes, member lists, legal filings, financial spreadsheets and reports to Scribd, and these often contain rich personal detail — home addresses, phone numbers, document IDs, colleagues — not found on social media. It's a strong source when standard people-search runs dry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search on https://www.scribd.com/ for the `name`/`email`/`employer-org` in quotes; try variants and add a location or org to focus.
2. Better still, use a search engine: `site:scribd.com "<name>"` — this indexes Scribd content and lets you preview via cache without logging in.
3. Open promising documents; scan for `address`, phone, `document-id`, and named `associate`s.
4. Downloading full documents may hit a paywall/upload-to-unlock — use a sock-puppet account or rely on the cached preview.
5. Pivot: extracted identifiers feed people-search; scanned images/photos in a document can go to `[[google-reverse-image-search]]`.

## Inputs → Outputs
- **In:** `name`, `email`, or `employer-org`
- **Out:** matching documents (`document-id`), `metadata-exif` (author/upload info), and leaked `address`/`associate` details inside files
- **Empty/negative result looks like:** no documents mention the subject — common for private individuals; absence just means nothing was uploaded/indexed, not that no documents exist.

## Gotchas & OpSec
- User-uploaded content — authenticity and currency vary; verify any document before relying on it.
- Human-in-the-loop: full download is often **paywalled**; the `site:scribd.com` + cache route usually avoids logging in.
- OpSec: searching is passive; downloading ties to your account, so use a sock puppet.

## Overlaps ("do both")
- Complements people-search and breach sources — Scribd surfaces *documents* others miss; feed images inside them to `[[google-reverse-image-search]]`. Do both to combine document leaks with record-based data.

## Trust & verifiability
`trust: community` — a legitimate platform, but the documents are uploaded by users, so treat contents as leads to verify against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scribd |
| category | image-video-face |
| selectorsIn → selectorsOut | name, email, employer-org → document-id, metadata-exif, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
</content>
