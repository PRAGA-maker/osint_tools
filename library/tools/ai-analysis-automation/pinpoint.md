---
id: pinpoint
name: Google Pinpoint
description: Use when you have a large `document-id` collection (PDFs, scans, audio) and want to search and extract entities across all of it — returns indexed text, people/orgs/locations, transcripts.
url: https://journaliststudio.google.com/pinpoint/about
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: OCR-ing, transcribing, and entity-searching big document/media collections in one place.
selectorsIn:
- document-id
selectorsOut:
- name
- employer-org
- geolocation
status: live
pricing: free
costNote: Free to use, but access is gated — Google grants accounts to journalists, academic researchers, and university students who apply/qualify.
opsec: passive
opsecNote: You upload documents you already hold into Google's cloud; it does not query any subject. Collections are private by default, but this is Google's infrastructure — do not upload material you're not comfortable storing with a third party, and mind source-protection obligations.
humanInLoop: true
humanInLoopReason:
- legal-gate
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google (Journalist Studio) tool used by major newsrooms (AP, NYT, Le Figaro); OCR/transcription are machine-generated, so verify extracted text against the source page.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: true
deprecated: false
relatedTools: []
aliases:
- Pinpoint
- Journalist Studio Pinpoint
tags:
- document-analysis
- ocr
- entity-extraction
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Google Pinpoint

> Google's document-intelligence workbench: upload thousands of PDFs, scans, images, emails, and audio files and search across all of them, with automatic OCR, transcription, and people/org/location extraction.

## When to use
You have a large document dump tied to a case — leaked archives, court records, FOIA releases, a hard drive of scans and recordings — and reading it manually is infeasible. Pinpoint OCRs and transcribes everything, indexes it for full-text search, and surfaces recurring `name`s, `employer-org`s, and `geolocation`s so you can find the person or thread that matters. Strong for missing-persons work when the lead is buried in bulk documents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Apply for access at Journalist Studio (journalist/researcher/student eligibility) and log in.
2. Create a private collection and upload your documents/media (PDFs, images, audio, email archives).
3. Let Pinpoint process — OCR on scans/handwriting, speech-to-text on audio/video.
4. Search across the collection with exact/exclude/keyword filters; browse the auto-extracted people, organizations, and locations.
5. Extract structured tables to spreadsheets; pivot named entities into people/org OSINT.

## Inputs → Outputs
- **In:** a collection of `document-id`s (files/media you upload)
- **Out:** searchable full text, transcripts, and extracted `name`s / `employer-org`s / `geolocation`s
- **Empty/negative result looks like:** no hits for a term, or garbled OCR on poor scans — the term may be phrased differently or the scan quality too low; verify by opening the source page, since extraction is machine-made.

## Gotchas & OpSec
- Access-gated: you must qualify and be approved; not open to the general public (`legal-gate` + login).
- OCR/transcription errors are common on handwriting, low-quality scans, and noisy audio — always confirm load-bearing quotes against the original.
- Uploads live in Google's cloud; weigh source-protection and confidentiality before uploading sensitive material.

## Overlaps ("do both")
- Pairs with local OCR/document tools for material you can't upload to a third party, and with EXIF/metadata tools for the files' technical provenance Pinpoint doesn't focus on.

## Trust & verifiability
`trust: trusted` — a first-party Google tool relied on by major investigative newsrooms; the platform is authoritative, but treat every OCR/transcript/entity as a machine inference to verify against the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pinpoint |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | document-id → name, employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate, account-login) |
