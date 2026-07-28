---
id: zotero
name: Zotero
description: Use when you need to capture, snapshot, organize, and cite web pages and documents during an investigation — builds a searchable, timestamped evidence library.
url: https://www.zotero.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Collecting, snapshotting, organizing, and citing web pages/PDFs into a searchable research/evidence library.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free, open-source app; online sync includes a limited free storage tier with paid upgrades (or self-hosted WebDAV).
opsec: passive
opsecNote: Saving a page is an ordinary page fetch (logged by that site) — capture from a clean/sock-puppet session. If you enable Zotero cloud sync, your library lives on Zotero's servers; for sensitive case material keep it local or sync via self-hosted WebDAV.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Established open-source reference manager from the Corporation for Digital Scholarship; widely used and reliable for evidence capture and citation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Zotero
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- evidence-management
- citation
- research
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Zotero

> A free, open-source research library that snapshots web pages the moment you find them — so your evidence survives even after the source is edited or deleted.

## When to use
You're gathering sources across an investigation and need to **preserve and organize** them: capture a full snapshot of a page (not just a fragile link), tag and group items by subject, add notes, and later cite or export them. Critical for OSINT where pages change or vanish — a saved snapshot with a capture timestamp is far stronger than a URL you can't re-open.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install the Zotero desktop app plus the **Zotero Connector** browser extension (Firefox/Chrome/Safari/Edge).
2. On a page worth keeping, click the Connector — Zotero saves the item's metadata and a **snapshot** of the page into your library.
3. Organize with collections, tags, and notes; the full-text is searchable.
4. Decide your storage posture: local-only, Zotero cloud sync, or self-hosted WebDAV (see OpSec).
5. Pivot: your organized library becomes the evidence base you cite/export in a report — and the snapshots are your hedge against link rot.

## Inputs → Outputs
- **In:** N/A — you feed it web pages/PDFs as you work
- **Out:** a searchable, tagged library with page snapshots, metadata, notes, and export/citation
- **Empty/negative result looks like:** N/A — if a capture is thin (JS-heavy or paywalled page), supplement with a manual PDF/print-to-PDF or an archive service.

## Gotchas & OpSec
- Snapshots capture what your session sees — login-gated or heavily-scripted pages may snapshot incompletely; pair with a formal archive (e.g. Wayback save) for defensibility.
- Cloud sync stores your library on Zotero's servers — for sensitive investigations keep it local or use self-hosted WebDAV.
- Capturing a page is normal traffic to that site; use a clean session where attribution matters.

## Overlaps ("do both")
- Complements web-archiving services — Zotero gives you a private, organized, annotatable copy; a public archive gives an independent, third-party-verifiable timestamp. Capture to both for important evidence.

## Trust & verifiability
`trust: trusted` — a mature, open-source, widely-relied-on tool; snapshots are faithful to what was served, and local storage keeps you in control of the chain of custody.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zotero |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
