---
id: meawfy
name: Meawfy
description: Use when you have a `name`, title, or keyword and want to find publicly-shared MEGA.nz files/folders about it — returns MEGA links to documents, media, and archives.
url: https://meawfy.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Searching the MEGA.nz cloud for publicly-shared files by keyword when a target may have hosted material there.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to search and browse; no account required. It indexes links only and hosts nothing itself.
opsec: passive
opsecNote: Searching is passive — you query Meawfy's index, not the file owner, who is not notified. Actually opening a MEGA link is a separate step that fetches from mega.nz over your IP and may expose you to unknown/hostile content; do that in a sandbox/VM from a sock-puppet IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party crawler of public MEGA links with no accountable operator; index freshness and result legitimacy vary, and results may point to pirated or malicious material.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Meawfy
- MEGA search engine
- meawfy.my
tags:
- file-search
- cloud-storage
- documents-metadata
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Meawfy

> A search engine over publicly-shared MEGA.nz links — type a keyword and get MEGA files/folders that match, without trawling MEGA by hand.

## When to use
You suspect a subject (or the material around a case) has been stashed on MEGA.nz — leaked document sets, media dumps, archives, courseware — and you want to search MEGA's otherwise-unsearchable public share space by `name`/title/keyword. MEGA itself has no content search; Meawfy crawls public links and indexes them, so it's the entry point when your lead is "there might be a MEGA folder for this."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://meawfy.com/ (mirrors exist at meawfy.my / meawfy.surf if the main domain is blocked).
2. Enter a keyword — a person/handle, a title, a filename fragment, or a topic.
3. Browse the returned MEGA links (files and folders), filtered by category (documents, media, software, etc.).
4. Before opening anything, move to a disposable VM on a sock-puppet IP — MEGA links can lead to malware or illegal content.
5. Pivot: filenames and folder structures (`document-id`, dates, embedded names) become new selectors for the rest of your workflow.

## Inputs → Outputs
- **In:** `name` / keyword / filename fragment
- **Out:** MEGA.nz links to public files/folders (`document-id`, titles, categories)
- **Empty/negative result looks like:** no matches, or only unrelated bulk-media results — the index skews toward pirated media/courses, so niche or personal material is often absent. Absence is not proof nothing was shared.

## Gotchas & OpSec
- Third-party index of **unvetted** content: expect piracy and the risk of malware; never open links on your working machine.
- Index can be stale or return dead links; MEGA also removes reported shares.
- OpSec: **passive** to search, but *opening* a link fetches from MEGA over your IP — sandbox it.

## Overlaps ("do both")
- Complements general file-search and document-metadata tools in this category — Meawfy covers the MEGA.nz surface specifically, which broad web search and other file engines miss.

## Trust & verifiability
`trust: unverified` — anonymous operator, opaque crawling, and results dominated by piracy; useful as a lead generator, but corroborate anything you find and handle links defensively.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | meawfy |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
