---
id: xeuledoc-fetch-metadata-about-any-public-google-document
name: xeuledoc
description: Use when you have a public Google Doc/Sheet/Drive URL and want its owner and history — returns the creator's Google ID, creation/modification dates and permission info.
url: https://github.com/Malfrats/xeuledoc
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Attributing a public Google document (Docs, Sheets, Slides, Drive, My Maps, Apps Script) to its owner and pulling its timestamps.
selectorsIn:
- document-id
selectorsOut:
- name
- metadata-exif
- email
status: live
pricing: free
costNote: Free and open-source (Python CLI); no account or key needed for public documents.
opsec: passive
opsecNote: It reads publicly-shared document metadata via Google's own endpoints without any authentication bypass, so the document owner is not notified. Your requests go to Google infrastructure; use a sock-puppet network context for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-known OSINT tool (Malfrats, ~1k stars); it surfaces metadata Google exposes for public docs — reliable, but what's revealed (owner name vs. just an ID) depends on the doc's sharing settings.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- online-exif-viewer
- commit-stream
aliases:
- Malfrats/xeuledoc
- xeuledoc
tags:
- google-docs
- metadata
- document-attribution
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# xeuledoc

> A CLI that fetches metadata about any **public** Google document — Docs, Sheets, Slides, Drive files, My Maps, Apps Script — to attribute it to its owner and reveal its creation/modification history.

## When to use
You have a link to a publicly-shared Google document (from a website, email, or investigation) and want to know **who created it** and **when**. xeuledoc pulls the owner's Google account identifier (and, where the doc exposes it, the owner's name/email), plus creation and last-modified timestamps and permission details. It's the standard way to de-anonymise a "shared with anyone" Google doc back to a person.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install xeuledoc` (or from https://github.com/Malfrats/xeuledoc).
2. Run `xeuledoc <public-google-doc-URL>`.
3. Read the output: creation date, last-modified date, owner's Google ID, and — if the sharing settings expose it — the owner's name/email and permission list.
4. If only a numeric Google ID appears, that ID is still a pivot (searchable, tied to other Google surfaces).
5. Pivot: an owner `email`/`name` feeds email/people-search; a Google ID can link to other documents; timestamps help build a timeline. For code identities, compare with `[[commit-stream]]`.

## Inputs → Outputs
- **In:** `document-id` (public Google Doc/Sheet/Slide/Drive URL)
- **Out:** owner `name`/Google ID, `email` (when exposed), and `metadata-exif` (created/modified dates, permissions)
- **Empty/negative result looks like:** the document isn't public (permission denied) or reveals only an opaque ID with no name/email — meaning restricted sharing; you get attribution only to the extent the owner exposed it.

## Gotchas & OpSec
- Only works on **publicly accessible** documents — no auth bypass; a private doc returns nothing.
- What's revealed varies with sharing settings — sometimes just a Google ID, sometimes a full name/email.
- OpSec: passive (reads Google's public metadata); the owner isn't alerted.

## Overlaps ("do both")
- The document analog of `[[online-exif-viewer]]` (metadata attribution for files) and `[[commit-stream]]` (identity from code) — use whichever matches the artifact you hold; combine when a subject leaves multiple digital trails.

## Trust & verifiability
`trust: community` — a widely-used tool surfacing Google's own metadata, so the data is authentic; just confirm a revealed name/email is current before relying on it, and note attribution depth depends on the doc's settings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xeuledoc-fetch-metadata-about-any-public-google-document |
| category | image-video-face |
| selectorsIn → selectorsOut | document-id → name, metadata-exif, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
</content>
