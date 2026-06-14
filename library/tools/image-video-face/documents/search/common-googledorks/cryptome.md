---
id: cryptome
name: Cryptome
description: Use when you want to search the Cryptome leak/document archive for a name or term via a Google site: dork — returns matching documents hosted on cryptome.org.
url: https://www.google.com/search?q=site:cryptome.org+%3Csearchterm%3E
category: image-video-face
path:
- image-video-face
- documents
- search
- common-googledorks
bestFor: Dork-search the Cryptome archive of leaked/sensitive documents for a name or keyword.
input: A search term (name, org, topic) appended to a Google site:cryptome.org query
output: Google results linking to documents and pages hosted on cryptome.org
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- name
status: live
pricing: free
costNote: Free; uses Google search over a public archive.
opsec: passive
opsecNote: Runs as a normal Google query; you never touch the subject. The query goes to Google, so use a clean session/VPN if the search term itself is sensitive.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Cryptome is a long-running, well-known document repository; relevance to everyday missing-persons cases is narrow, so the documents found should be corroborated.
missingPersonsRelevance: low
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cryptome.org
tags:
- document-search
- google-dork
- leaks
source: arf-seed
lastVerified: ''
enrichment: full
---

# Cryptome

> A Google `site:` dork over cryptome.org — the long-running archive of leaked, suppressed, and sensitive documents.

## When to use
Niche. You want to check whether a `name` or `employer-org` appears anywhere in Cryptome's document archive (intelligence leaks, surveillance disclosures, sensitive filings). For typical missing-persons casework this is a low-yield, last-resort source; it pays off mainly when the subject has an intelligence, activist, or government-adjacent profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Replace `<searchterm>` in the URL with your term (URL-encode spaces), or just run `site:cryptome.org "Full Name"` in Google.
2. Review the results — each links to a document or index page on cryptome.org.
3. Open promising hits and read the actual document.
4. Pivot: extract any `document-id`, associated `name`s, or dates and corroborate against primary sources.

## Inputs → Outputs
- **In:** `name`, `employer-org` (the search term)
- **Out:** `document-id`, `name` (documents/pages on cryptome.org mentioning the term)
- **Empty/negative result looks like:** zero Google hits — the term simply is not in the archive, which is the common case for ordinary individuals.

## Gotchas & OpSec
- This is mislabeled under `image-video-face`; it is a document-search dork, not an image tool.
- Human-in-the-loop: Google may throw a CAPTCHA on repeated dorking.
- OpSec: passive toward the subject. The query is visible to Google; if the term is sensitive, use a clean browser/VPN.

## Overlaps ("do both")
- One of a family of `common-googledorks`; pair with broader leak/breach and document-dork searches rather than relying on Cryptome alone.

## Trust & verifiability
`trust: community` — Cryptome itself is an established, decades-old archive, and every result is a live document you can open and read. `missingPersonsRelevance: low` because the corpus rarely intersects with routine missing-persons work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cryptome |
| category | image-video-face |
| selectorsIn → selectorsOut | name, employer-org → document-id, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
