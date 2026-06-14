---
id: googledocs
name: GoogleDocs
description: Use when you want to find publicly shared Google Docs mentioning a name, email, phone, or org — a Google dork (site:docs.google.com) returning indexed, link-shared documents.
url: https://www.google.com/?q=site:docs.google.com+%3Csearchterm%3E
category: image-video-face
path:
- image-video-face
- documents
- search
- common-googledorks
bestFor: Finding publicly shared/indexed Google Docs that mention a search term.
input: Google dork query site:docs.google.com + <searchterm>
output: Public Google Docs (rosters, sign-up sheets, spreadsheets, notes) mentioning the term
selectorsIn:
- name
- email
- phone
- employer-org
selectorsOut:
- name
- email
- phone
- address
- associate
status: live
pricing: free
costNote: Free; just a Google search query.
opsec: passive
opsecNote: Keyword query against Google's index; you never touch the target. Opening a found doc requests it from Google's servers (logged by Google, not the document owner unless they have analytics).
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Standard, well-documented Google dork technique; reliability depends on what Google has indexed, which changes over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- googledrive
aliases:
- 'dork: site:docs.google.com'
tags:
- google-dork
source: arf-seed
lastVerified: ''
enrichment: full
---

# GoogleDocs

> A Google dork (`site:docs.google.com`) for surfacing publicly shared or accidentally indexed Google Docs that mention your subject.

## When to use
You have a `name`, `email`, `phone`, or `employer-org` and want to find link-shared documents — club rosters, volunteer sign-up sheets, contact lists, meeting notes, spreadsheets — that people published as "anyone with the link" and Google then indexed. These often contain `address`, `phone`, and `associate` data not found elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run: `site:docs.google.com "John Smith"` (replace the search term; the URL's `<searchterm>` placeholder is filled here).
2. Add identifiers to narrow: `site:docs.google.com "john.smith@email.com"` or a phone number; combine with org names.
3. Scan result titles/snippets, open documents, and read for contact details and named contacts (`selectorsOut`).
4. Pivot found emails/phones/associates into people-search and social tools; run the same dork against `[[googledrive]]` for folders and other file types.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, `employer-org`
- **Out:** `name`, `email`, `phone`, `address`, `associate`
- **Empty/negative result looks like:** zero results or only unrelated public templates — the subject's docs are private/unindexed; vary the term and try `[[googledrive]]`.

## Gotchas & OpSec
- Only finds documents shared as link-accessible *and* indexed by Google; most personal docs are private and will not appear.
- Index is volatile — a doc found today may be removed/de-indexed tomorrow; screenshot/archive promptly.
- OpSec: passive search. Opening a doc is logged by Google; the owner generally cannot see who viewed a link-shared file unless they added tracking. Use a clean account for sensitive work.

## Overlaps ("do both")
- Pairs with `[[googledrive]]` (folders, sheets, slides, PDFs) — run the same query against both surfaces.

## Trust & verifiability
`trust: trusted` — standard, reproducible Google dork; the technique is reliable, but specific hits depend on Google's current index, so document findings immediately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | googledocs |
| category | image-video-face |
| selectorsIn → selectorsOut | name, email, phone, employer-org → name, email, phone, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
