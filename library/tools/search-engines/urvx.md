---
id: urvx
name: URVX
description: Use when you have a filename or keyword and want to search across popular file-hosting services (MediaFire, 4shared, etc.) via a Google-powered custom search — returns file-hosting links to documents/media.
url: https://uvrx.com
category: search-engines
path:
- search-engines
bestFor: Searching many file-storage/hosting sites at once for a named file via a Google CSE.
selectorsIn:
- name
selectorsOut:
- name
status: degraded
pricing: free
costNote: Free Google-Custom-Search-based file-search portal; no account required. The site has been intermittently unreachable — confirm it loads before relying on it.
opsec: passive
opsecNote: It's a Google Custom Search over file-hosting domains — you query Google, not the file hosts, so it's passive. Downloading anything you find contacts that host and can carry malware; fetch only in a sandboxed/sock-puppet environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party Google CSE wrapper focused on file-sharing sites; results are Google's (over a curated site list), but the portal is lightly maintained (status degraded).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- uvrx
aliases:
- uvrx.com
- UVRX Search
tags:
- Search engines
- Filesharing Search Engines
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# URVX

> A Google-Custom-Search portal scoped to popular file-hosting services — search many file lockers at once for a named file.

## When to use
When your lead is a *file* — a specific document, archive, media filename, or leaked dataset name — and you want to know whether it's hosted on public file-sharing services (MediaFire, 4shared, and similar). URVX runs a Google CSE restricted to file-host domains, so one query checks many lockers. It finds files, not people, but a located document may contain selectors to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://uvrx.com (confirm it loads — the service is intermittently up).
2. Enter your filename/keyword; optionally use the per-host search variants it offers.
3. Read results as Google hits pointing to files on hosting sites.
4. Download only in a sandboxed/sock-puppet environment, treating any file as potentially malicious.
5. Pivot: a recovered document → extract embedded `metadata-exif`/names/emails; the hosting account → further OSINT.

## Inputs → Outputs
- **In:** `name` (a filename or keyword)
- **Out:** `name` (links to matching files on hosting services)
- **Empty/negative result looks like:** no hits — the file isn't indexed on the covered hosts, which doesn't rule out other services; try a general filesharing search.

## Gotchas & OpSec
- **Uptime is unreliable** (status degraded) — don't build a workflow that depends on it.
- Results are only as fresh as Google's index of those file hosts; dead links are common.
- Downloading is the risky step — sandbox everything and never open unknown files on your host.

## Overlaps ("do both")
- Related to its sibling `[[uvrx]]` (social-search variant of the same site) and to other filesharing search engines; try several, since each covers different hosts.

## Trust & verifiability
`trust: unverified` — a lightly-maintained CSE wrapper; results come from Google (reliable) but the portal and its host list are unvetted, so treat every hit as a lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urvx |
| category | search-engines |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
