---
id: google-document-dorks-inteltechniques-method
name: Google Document Dorks (IntelTechniques method)
description: Use when you have a `name` or `domain` and want to surface documents, spreadsheets, and cloud files naming the subject — returns document-id, metadata-exif, and name leads.
url: https://inteltechniques.com/tools/Documents.html
category: documents-metadata
path:
- documents-metadata
bestFor: Filetype- and site-targeted Google dorks (PDF/DOC/XLS/PPT, cloud buckets, Scribd/SlideShare) to find documents mentioning a person or tied to a domain.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
- metadata-exif
- name
status: live
pricing: free
costNote: Free web tool from IntelTechniques; it just builds Google/search queries — no account or payment.
opsec: passive
opsecNote: The tool itself only assembles search-engine queries locally; the actual searching happens on Google/other engines from your browser. Passive, but the documents you then open may log your visit — open sensitive hits via cache/archive or a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Michael Bazzell's IntelTechniques, a widely-respected OSINT resource; the dork templates are sound, though results depend entirely on what search engines currently index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-dorks
- metagoofil
- exiftool
aliases:
- IntelTechniques Documents tool
- Bazzell document search
tags:
- dorks
- documents
- filetype
- cloud-buckets
source: inteltechniques-tools
lastVerified: '2026-07-14'
enrichment: full
---

# Google Document Dorks (IntelTechniques method)

> IntelTechniques' document-search tool — a form that assembles filetype- and site-targeted search-engine dorks to surface documents, spreadsheets, and cloud files that name your subject.

## When to use
You have a `name` (or a `domain`/organisation) and want documents rather than web pages: a PDF roster listing the person, an XLS with their contact details, a PPT/Scribd/SlideShare deck mentioning them, or files sitting in an exposed cloud bucket. Documents often carry richer, less-curated data than web pages — full names, addresses, phone numbers, and author metadata — making them high-value in a person hunt.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inteltechniques.com/tools/Documents.html.
2. Enter the subject `name` (in quotes) or a `domain`.
3. Fire the prebuilt queries: filetype dorks (`filetype:pdf`, `:doc`, `:xls`, `:ppt`), document hosts (Scribd, SlideShare, DocumentCloud), and cloud-storage/bucket patterns.
4. Open promising hits — then check each document's **author/created/modified metadata** (`metadata-exif`) for the real author and software, which can leak an identity behind an anonymous file.
5. Pivot: extracted metadata feeds identity attribution; contents feed address/phone/associate leads. Use `[[exiftool]]` on downloaded files for full metadata.

## Inputs → Outputs
- **In:** `name` or `domain`
- **Out:** `document-id` (found files), `metadata-exif` (author/created/modified in the files), `name` (mentions and document authors)
- **Empty/negative result looks like:** dorks return nothing or only unrelated files — the subject may not appear in indexed documents; broaden name variants or try other engines (Bing/Yandex index different files).

## Gotchas & OpSec
- It's a **query builder**, not a database — results are only as good as current search-engine indexing.
- Opening a hit can log your visit to the host; use cache/archive or a sock-puppet session for sensitive files.
- Document metadata is gold but can be spoofed/stripped — corroborate before attributing.

## Overlaps ("do both")
- Pairs with raw `[[google-dorks]]` (broader operators), `[[metagoofil]]` (bulk-download documents from a domain and extract metadata), and `[[exiftool]]` (read the metadata). Use this to find files, the others to harvest and analyse them.

## Trust & verifiability
`trust: community` — a respected IntelTechniques resource; the dork templates are reliable, but every hit is a lead whose data (and metadata) you must verify against the source file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-document-dorks-inteltechniques-method |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, domain → document-id, metadata-exif, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
