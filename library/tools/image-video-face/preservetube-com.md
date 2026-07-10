---
id: preservetube-com
name: PreserveTube
description: Use when you have a YouTube video/channel (`social-profile`) and want to recover or archive it before/after deletion — returns the preserved video plus its title, description and metadata.
url: https://preservetube.com/
category: image-video-face
path:
- image-video-face
bestFor: Archiving YouTube videos and channels so removed/deleted content stays viewable, and searching whether a given video/channel has already been preserved.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free service; no account. It stores video files and metadata for later retrieval.
opsec: passive
opsecNote: Requesting an archive or viewing a preserved copy is done through PreserveTube's servers; you don't contact the uploader, so it's passive toward the subject. Note that submitting a video to be archived is a public action on a third-party service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community video-preservation service; genuinely archives YouTube content, but it's a third-party host — coverage is limited to what's been submitted, and long-term availability isn't guaranteed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- PreserveTube
- preservetube.com
tags:
- youtube
- YouTube Related Sites
- archive
- deleted-content
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# PreserveTube

> A "time capsule for YouTube" — it snapshots videos (and their titles, descriptions and metadata) so they stay viewable even after the original is deleted or taken down.

## When to use
You need YouTube content that might vanish, or already has: a subject's video you fear they'll delete, a channel likely to be removed, or a clip that's already gone from YouTube. PreserveTube lets you (a) archive a video/channel proactively, and (b) search whether a video/channel has already been preserved so you can recover deleted evidence. Deleted-video recovery is the high-value case for investigations where the subject scrubs their trail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://preservetube.com/.
2. **To recover:** use "Search for archived videos/channels" with the video ID/URL or channel to see if a preserved copy exists, and view it with its saved title/description/metadata.
3. **To preserve:** submit a YouTube video or channel URL to archive it before it disappears.
4. Extract the preserved video and its `metadata-exif` (title, description, upload data) for your record.
5. Pivot: a preserved video's metadata/description feeds channel and identity OSINT; the content itself may carry geotags, faces or timestamps to analyse.

## Inputs → Outputs
- **In:** a YouTube video/channel URL or ID (`social-profile`)
- **Out:** `social-profile` (the preserved video/channel), `metadata-exif` (title, description, upload metadata)
- **Empty/negative result looks like:** the video/channel isn't in the archive — meaning no one preserved it (yet); a deleted video that was never archived here is simply unrecoverable via this service.

## Gotchas & OpSec
- **Coverage = what's been submitted** — it can't retroactively recover a deleted video nobody archived; archive proactively when a video matters.
- Third-party host: long-term availability isn't guaranteed; download a local copy of anything critical.
- OpSec: passive; submitting an archive request is a visible third-party action.

## Overlaps ("do both")
- Pairs with the Wayback Machine and yt-dlp — Wayback may hold a page snapshot, yt-dlp downloads live videos before they're removed, and PreserveTube keeps a playable copy; use together to maximise recovery.

## Trust & verifiability
`trust: community` — a genuine community preservation service; a preserved copy is authentic to its capture, but coverage is partial and hosting isn't guaranteed, so keep local backups of anything important.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | preservetube-com |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
