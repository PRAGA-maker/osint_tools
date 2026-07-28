---
id: etherpad-collaborative-editing
name: Etherpad
description: Use when a team needs to co-write case notes in real time on infrastructure you control — an open-source, self-hostable collaborative editor; a workflow tool, not a data source.
url: https://etherpad.org
category: documents-metadata
path:
- documents-metadata
bestFor: Real-time multi-investigator note-taking on a self-hosted pad, keeping case notes off third-party clouds.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; self-host it, or use a public instance (public pads are NOT private).
opsec: passive
opsecNote: Public Etherpad instances store your notes on someone else's server and pads are often reachable by URL guessing — never put case-sensitive material on a public pad. Self-host (or use a trusted private instance) for any real investigation notes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Mature open-source project; trustworthy as software, but the privacy of your notes depends entirely on which instance you use and how it's configured.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- etherpad.org
- Etherpad Lite
tags:
- Useful Websites, Tools & Documents
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Etherpad

> An open-source, self-hostable real-time collaborative editor — a workflow tool for teams to co-write case notes on infrastructure they control, not an investigative data source.

## When to use
This is a **collaboration/OpSec workflow tool**, not a lookup. Use it when two or more investigators need to write and edit shared notes, timelines, or link-lists together in real time, and you want to keep that material off Google Docs / commercial clouds by running your own instance. It returns nothing about a subject; its role is keeping *your* working notes collaborative and under your control.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Self-host** Etherpad (Docker or npm) on infrastructure you trust — this is the point of using it over a commercial editor.
2. Create a pad; share the pad URL with your team (protect it — knowing the URL grants access on most setups).
3. Co-edit in real time; use color-coded authorship, chat, and revision history/time-slider to review who changed what.
4. Export the finished notes (HTML, Markdown, plain text) into your case file.
5. Delete/lock the pad when done; don't leave sensitive notes on a long-lived shared URL.

## Inputs → Outputs
- **In:** your own notes/text (no investigative selector)
- **Out:** a shared, versioned document (no investigative selector)
- **Empty/negative result looks like:** N/A — it's an editor; the only "failure" is using a public instance and exposing notes you meant to keep private.

## Gotchas & OpSec
- **Public pads are not private** — many public instances let anyone with (or guessing) the URL read/edit. Self-host for real cases.
- Revision history retains everything typed, including mistakes/pasted secrets — clean up before sharing exports.
- Access control is URL-based on default setups; add authentication for sensitive work.

## Overlaps ("do both")
- Complements OpSec tools like `[[onionshare-file-sharing-tool]]` — Etherpad handles collaborative note-taking, OnionShare handles anonymous file transfer; together they keep a team's workflow off third-party clouds.

## Trust & verifiability
`trust: community` — a mature, reputable open-source editor; the software is trustworthy, but the confidentiality of your notes rests entirely on choosing a self-hosted or vetted private instance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | etherpad-collaborative-editing |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
