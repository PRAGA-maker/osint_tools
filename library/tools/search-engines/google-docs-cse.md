---
id: google-docs-cse
name: Google Docs CSE
description: Use when you have a `name`, `email`, or keyword and want to find publicly exposed Google Docs/Sheets/Slides — a Google Custom Search Engine scoped to docs.google.com.
url: https://cse.google.com/cse/publicurl?cx=013991603413798772546:rse-4irjrn8#gsc.tab=0
category: search-engines
path:
- search-engines
bestFor: Surfacing public/exposed Google Docs, Sheets, and Slides that mention a person, email, or keyword.
selectorsIn:
- name
- email
selectorsOut:
- document-id
- name
- email
status: live
pricing: free
costNote: Free Google Programmable Search Engine (Custom Search); no account needed to run the public search page.
opsec: passive
opsecNote: You query Google's index, not the documents themselves, so the doc owners are not notified by the search. Opening a returned doc, however, may register a view for shared files — open with a sock-puppet Google session and avoid requesting access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine restricted to docs.google.com; the results are Google's, but the CSE scope was set by an unknown author, so confirm what domains it actually covers.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Google Docs Custom Search
- docs.google.com CSE
tags:
- google-dork
- exposed-documents
- search
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Google Docs CSE

> A Google Custom Search Engine narrowed to `docs.google.com`, turning "search the whole web" into "search only publicly shared Google Docs/Sheets/Slides."

## When to use
You have a `name`, `email`, phone, or organization keyword and suspect it may appear in a Google Doc that someone set to "anyone with the link" and that Google has since indexed — leaked contact lists, rosters, planning sheets, resumes. This CSE constrains the search to Google Docs surfaces so you don't have to wade through the entire web.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE public URL.
2. Enter your `name` / `email` / keyword (quote exact phrases; combine terms to cut noise).
3. Review hits — each is a publicly accessible Google Docs/Sheets/Slides file matching the term.
4. Open promising files in a sock-puppet Google session; do **not** click "request access" (that emails the owner).
5. Pivot: an exposed doc can yield rosters of `associate`s, contact `email`s, and a `document-id` to cite.

## Inputs → Outputs
- **In:** `name`, `email`, or keyword
- **Out:** links to public Google Docs/Sheets/Slides (`document-id`) containing that term; often `name`/`email` lists inside
- **Empty/negative result looks like:** no results — nothing matching is publicly shared *and* indexed; it does not prove no such doc exists (private/unindexed docs won't appear).

## Gotchas & OpSec
- Only finds docs set to public/link-shared **and** crawled by Google; private docs are invisible here.
- The CSE's exact scope was defined by a third party — sanity-check that hits really are docs.google.com URLs.
- Opening a shared file may log a view; never request access, which notifies the owner.

## Overlaps ("do both")
- Pairs with manual Google dorking (`site:docs.google.com "term"`) — the CSE is a saved, convenient version; a raw dork lets you tune scope (add `filetype`, other Google surfaces like Drive) the CSE fixes for you.

## Trust & verifiability
`trust: community` — results come from Google's index (authoritative), but the search scope was configured by an unknown author, so verify the returned domains and treat exposed-doc contents as unvetted until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-docs-cse |
| category | search-engines |
| selectorsIn → selectorsOut | name, email → document-id, name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
