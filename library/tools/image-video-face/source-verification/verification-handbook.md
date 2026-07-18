---
id: verification-handbook
name: Verification Handbook
description: Use when you need a methodology (not a lookup) for verifying user-generated photos, video, and breaking-news claims — returns free workflows, checklists, and case studies.
url: https://verificationhandbook.com/
category: image-video-face
path:
- image-video-face
- source-verification
bestFor: Learning and applying repeatable verification workflows for images, video, and UGC during breaking news.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to read online and download (PDF/ePub/Kindle) in multiple languages; a European Journalism Centre project.
opsec: passive
opsecNote: Passive — a static documentation site with no investigative target interaction; reading it leaks nothing. It's a reference, not a query tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by verification specialists and journalists from the BBC, Storyful, ABC, AP and others, published by the European Journalism Centre; a widely cited standard reference.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- verificationhandbook.com
- The Verification Handbook
tags:
- verification
- methodology
- source-verification
- UGC
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Verification Handbook

> Not a tool that answers a query — the reference that teaches the method: how to verify photos, video, and eyewitness claims, with checklists and real case studies. Read it to sharpen how you use every other tool.

## When to use
You're weighing user-generated content — a photo, a video, an eyewitness account, a viral claim — and need a disciplined process to establish whether it's real, when/where it originated, and whether it can be trusted. Reach for the Handbook to structure a verification: it frames the questions (source, date, location, provenance, manipulation) and points to the techniques and tools that answer each. In missing-persons and breaking-event work, it's the methodology backbone behind reverse-image, geolocation, and metadata tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://verificationhandbook.com/ and read online or download (PDF/ePub/Kindle; multiple languages).
2. Pick the relevant volume/chapter — core verification, investigative methods, or disinformation — and its checklists.
3. Work a piece of content through the process: identify and contact the original source, confirm date and location, check for manipulation, and corroborate independently.
4. Use its case studies as worked examples of the workflow on real events.
5. Pivot: each verification step points you to a concrete tool — reverse image search, EXIF/metadata extraction, chronolocation, weather/shadow analysis — which you run separately.

## Inputs → Outputs
- **In:** a verification question or a piece of UGC to assess (no machine selector — it's a reference)
- **Out:** structured guidance — workflows, checklists, and case studies that tell you *how* to verify and *which* tools to apply
- **Empty/negative result looks like:** N/A — it returns methodology, not lookups; the "failure" mode is skipping it and verifying ad hoc.

## Gotchas & OpSec
- **It's a guide, not a database:** it won't reverse-search an image or geolocate a photo — it tells you how, then you use the appropriate tool.
- Some specific tools referenced in older editions may have changed or died; apply the *method* and substitute current equivalents.
- Journalism-oriented, but the workflow generalizes to any OSINT verification task.

## Overlaps ("do both")
- Underpins the whole image-verification toolset — pair the Handbook's method with reverse-image search, EXIF extraction (`[[forensic-analyzer]]`), and weather/terrain chronolocation (`[[ventusky-com]]`, `[[worldofo-com]]`) that execute the steps it prescribes.

## Trust & verifiability
`trust: trusted` — a European Journalism Centre publication authored by named verification experts from major newsrooms; it is a widely adopted, well-regarded standard reference.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verification-handbook |
| category | image-video-face |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
