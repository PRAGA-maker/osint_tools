---
id: oletools
name: oletools
description: Use when you have an Office document (doc/xls/ppt) and need its embedded metadata, authorship, timestamps, or to triage macros — returns author/org names, dates, and indicators.
url: https://github.com/decalage2/oletools
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Extracting authorship/metadata and triaging macros/embedded objects from MS Office (OLE/OOXML/RTF) files.
selectorsIn:
- document-id
- metadata-exif
selectorsOut:
- name
- employer-org
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (BSD); pip-installable, runs locally.
opsec: active
opsecNote: Runs locally so it does not leak the document, but it is malware-analysis tooling — analyze unknown/possibly-malicious documents only in an isolated/sandboxed environment.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by Philippe Lagadec (decalage2), a recognised DFIR researcher; oletools is a standard, widely-used open-source toolkit (olevba, oleid, olemeta, oletimes).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- olevba
- olemeta
- oleid
tags:
- document-metadata
- forensics
source: arf-seed
lastVerified: ''
enrichment: full
---

# oletools

> A standard open-source Python toolkit for pulling metadata out of — and security-triaging — Microsoft Office documents.

## When to use
You obtained a Microsoft Office file in a case (a `document-id` such as a Word/Excel/PowerPoint attachment, RTF, or legacy .doc) and want to know **who created it and when**: author/last-modified-by `name`, company/`employer-org`, created/modified timestamps, template path, and any embedded objects. `olemeta`/`oletimes` surface document metadata that can attribute a file to a person or organization; `olevba`/`oleid` flag macros if the file is suspicious. More of a documents/metadata pivot than a face/image tool.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install -U oletools` (Python 3).
2. Metadata: `olemeta suspicious.doc` → author, company, created/modified times. Timestamps: `oletimes suspicious.doc`.
3. Triage/indicators: `oleid file.docx` (risk flags), `olevba file.docm` (extract/deobfuscate macros), `oleobj file.doc` (embedded objects/links).
4. Record the author/`employer-org` and dates; cross-reference the name against people-search and the org against business records.
5. Run unknown samples inside a sandbox/VM.

## Inputs → Outputs
- **In:** an Office `document-id` (file) and its `metadata-exif`
- **Out:** `name` (author / last-modified-by), `employer-org` (company field), full document `metadata-exif` (timestamps, template, embedded objects)
- **Empty/negative result looks like:** blank author/company fields and no macros — metadata was stripped or never set; fall back to file system timestamps and content analysis.

## Gotchas & OpSec
- Human-in-the-loop: interpreting macro output and judging authenticity of metadata (which can be forged) is manual.
- OpSec: **active** in the sense that you are handling possibly-malicious files — always analyze in an isolated VM; the tool itself runs locally and does not exfiltrate the document.
- Metadata can be spoofed; treat author/company as a lead, not proof.

## Overlaps ("do both")
- Complements image/EXIF metadata tools — oletools covers Office files specifically, where generic EXIF tools do not reach the OLE/OOXML property streams.

## Trust & verifiability
`trust: trusted` — authored and actively maintained by Philippe Lagadec (decalage2), a well-known DFIR researcher; it is a de-facto standard in document forensics with open, auditable source.

---
## Metadata
| field | value |
|---|---|
| id | oletools |
| category | image-video-face |
| selectorsIn → selectorsOut | document-id, metadata-exif → name, employer-org, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes |
