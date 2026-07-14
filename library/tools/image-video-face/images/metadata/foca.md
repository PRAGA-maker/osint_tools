---
id: foca
name: FOCA
description: Use when you have a `domain` and want to harvest public documents from it and extract their metadata — returns usernames, emails, software/paths and EXIF metadata that map an organization's internals.
url: https://github.com/ElevenPaths/FOCA
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Corporate document-metadata reconnaissance against a target domain.
selectorsIn:
- domain
selectorsOut:
- username
- email
- metadata-exif
- employer-org
status: live
pricing: free
costNote: Free and open-source (ElevenPaths/Telefónica). No license fee; Windows-only and requires .NET + SQL Server to run.
opsec: active
opsecNote: FOCA searches Google/Bing/DuckDuckGo for documents then downloads them — the download of files from the target's own servers can be logged by that infrastructure. Route through a VPN/sock-puppet network and expect the fetches to be attributable if the target inspects logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Well-known open-source tool from ElevenPaths (Telefónica); last release ~2021, Windows-only, still widely used but no longer actively developed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Fingerprinting Organizations with Collected Archives
- ElevenPaths FOCA
tags:
- metadata
- document-metadata
- exif
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# FOCA

> A Windows tool that finds an organization's public documents and mines their metadata — usernames, emails, software versions, internal paths — to fingerprint the people and systems behind a domain.

## When to use
You have a `domain` (or organization) and want to expand it into human and system selectors: the authors, editors, and machine/usernames baked into published Office/PDF/InDesign/SVG files, plus software versions and internal directory paths. Strong for tying a person to an `employer-org`, harvesting real `username`/`email` patterns for enumeration, and pulling EXIF/GPS from graphics.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install FOCA on Windows (64-bit; needs .NET Framework 4.7.1+ and SQL Server 2014+). Download from the ElevenPaths GitHub releases.
2. Create a project and enter the target `domain`.
3. Let FOCA search Google, Bing, and DuckDuckGo for indexed documents on that domain, then download the ones you select.
4. Run metadata extraction: FOCA parses author/username fields, creation software, file paths, printers, and EXIF/GPS from images, and can cluster them into a network of users, folders, and machines.
5. Pivot: harvested `username`/`email` conventions feed `[[username-generation-guide]]` and namecheckers; author names feed people-search; EXIF GPS feeds geolocation.

## Inputs → Outputs
- **In:** `domain` (target organization)
- **Out:** `username`, `email`, `metadata-exif` (incl. GPS), software/path fingerprints, internal server/`employer-org` structure
- **Empty/negative result looks like:** no indexed documents found, or documents scrubbed of metadata (increasingly common) — meaning the org sanitizes files, not that no staff exist.

## Gotchas & OpSec
- Active collection: downloading documents from the target's servers is attributable; use anonymizing infrastructure.
- Windows-only and heavyweight (SQL Server dependency); no Linux/CLI equivalent from this project.
- Modern documents are often metadata-stripped, so yield varies widely by target hygiene.

## Overlaps ("do both")
- Feeds `[[username-generation-guide]]`: FOCA gives real username/email patterns from an org's own files, which you then permute and enumerate across platforms.

## Trust & verifiability
`trust: community` — reputable open-source provenance (ElevenPaths/Telefónica) but no longer actively maintained; extracted metadata is verifiable by opening the source documents yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | foca |
| category | image-video-face |
| selectorsIn → selectorsOut | domain → username, email, metadata-exif, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
