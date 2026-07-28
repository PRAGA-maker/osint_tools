---
id: pdfmyurl
name: PDFmyURL
description: Use when you have a `domain`/URL and want to capture the live web page as a PDF for evidence preservation — returns a timestamped PDF snapshot.
url: https://pdfmyurl.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Quickly saving a live web page as a PDF to preserve it before it changes or disappears.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: freemium
costNote: Free ad-hoc single-page conversions in the browser; higher-volume/API and watermark-free use are paid. No account needed for a one-off.
opsec: active
opsecNote: PDFmyURL's servers fetch the target URL, so the request reaches the site from PDFmyURL's IP, not yours — that hides you, but it also means a third party sees what you're capturing. For sensitive or authenticated pages, use a local capture (browser print-to-PDF) instead so the content never touches a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party conversion service; the PDF is only as trustworthy as your provenance notes — record the URL, capture time and method, since a rendered PDF is easy to alter.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- pdf-my-url
aliases:
- PDF my URL
tags:
- evidence-capture
- documents
- curated-directory
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# PDFmyURL

> A web-to-PDF service for grabbing a live page as a document — useful for preserving evidence before it's edited or deleted.

## When to use
You've found a page on a `domain` (a profile, a listing, a post, a company page) that matters to your case and you want a fixed copy before it changes or vanishes. PDFmyURL renders the live page to a PDF you can file as evidence. Reach for it for quick, public-page preservation; for anything sensitive or behind a login, prefer a local capture so content doesn't pass through a third party. It preserves pages; it doesn't find people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pdfmyurl.com/.
2. Paste the target page URL (`domain`/path) and generate the PDF.
3. Download the PDF and immediately record provenance: the exact URL, the capture date/time, and that PDFmyURL was the method.
4. For fidelity or authenticated pages, also do a local browser "Print → Save as PDF" and/or an archive.org / archive.today capture as corroboration.
5. Pivot: file the PDF in your case record; treat the archived copy, not the PDF alone, as the durable evidence anchor.

## Inputs → Outputs
- **In:** a page URL (`domain`)
- **Out:** a PDF snapshot of the rendered page (no person-level `selectorsOut`)
- **Empty/negative result looks like:** a blank/partial PDF or a login/consent wall captured instead of content — the service couldn't render the page; capture locally or via an archiving service instead.

## Gotchas & OpSec
- OpSec: **active** in that PDFmyURL's servers fetch the URL — this hides your IP from the target but exposes what you're capturing to a third party. Use local capture for sensitive/authenticated pages.
- A PDF is trivially editable, so it is weak evidence on its own — always pair it with an independent timestamped archive (archive.today / Wayback) and a provenance note.
- The free tier watermarks/limits; it can't reach pages behind authentication.

## Overlaps ("do both")
- Do both with archive.today / the Wayback Machine — those give a tamper-resistant, independently-hosted record, while PDFmyURL gives a portable document; together they make the capture defensible.

## Trust & verifiability
`trust: unverified` — a third-party renderer; the evidentiary value depends entirely on your provenance discipline and independent corroboration, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pdfmyurl |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
