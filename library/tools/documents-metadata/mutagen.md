---
id: mutagen
name: Mutagen
description: Use when you have an audio file and want its embedded metadata — returns `metadata-exif`-style tags (artist, encoder, timestamps, comments) that can carry attribution and device clues.
url: https://github.com/quodlibet/mutagen
category: documents-metadata
path:
- documents-metadata
bestFor: Reading (and writing) the tag metadata inside audio files — ID3/Vorbis/MP4 tags — from Python or the command line.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (GPLv2+); install via `pip install mutagen`. Requires Python 3.10+ and has no external dependencies.
opsec: passive
opsecNote: Fully offline and local — mutagen parses a file already in your possession and makes no network calls, so it leaks nothing about you or the target. Work on a copy to preserve the original evidence file's tags/hash.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: Long-established, widely used library maintained under the Quod Libet project (1,800+ commits); it reads the file's actual embedded tags, so output is as reliable as what the file contains.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- python-mutagen
- mutagen audio metadata
tags:
- Files
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Mutagen

> The audio-file counterpart to an EXIF reader: pull the tags embedded in MP3/FLAC/MP4/OGG audio — artist, encoder software, dates, comments — that can quietly reveal who made a recording and with what.

## When to use
You have an audio artefact (a voicemail, a leaked recording, a music file, a podcast clip) and want the metadata baked into it. Audio tags routinely carry an author/artist name, the encoding software/hardware, creation or tagging timestamps, and free-text comments — attribution and device clues that the audio itself doesn't announce. Mutagen reads all of it, across nearly every audio container.

## How to use it (`bestInteractionPattern`: python-lib)
1. `pip install mutagen` (Python 3.10+).
2. In Python: `from mutagen import File; f = File("evidence.mp3"); print(f.tags)` — or use the format-specific classes (`mutagen.mp3`, `mutagen.flac`, `mutagen.mp4`).
3. Read the tag frames: ID3 (MP3), Vorbis comments (FLAC/OGG), MP4 atoms — artist/author, encoder, dates, comments, cover art.
4. (Optional) write/normalise tags — but only on a working copy; never alter the original evidence file.
5. Pivot: an author/artist string feeds `name`/username OSINT; an encoder or device string narrows the recording toolchain.

## Inputs → Outputs
- **In:** a local audio file (no selector — you supply the file)
- **Out:** `metadata-exif` (embedded audio tags: artist/author, encoder, timestamps, comments, embedded art)
- **Empty/negative result looks like:** empty or `None` tags — the file was stripped, re-encoded, or never tagged; absence of tags is common and not evidence of tampering by itself.

## Gotchas & OpSec
- Tags are trivially editable and often auto-filled by software — treat an author/date as a lead, not proof, and corroborate.
- Re-encoding (e.g. a messaging app transcoding a voice note) usually strips or rewrites tags, so a clean file may simply reflect the last tool that touched it.
- Always operate on a copy and hash the original first to preserve evidentiary integrity.

## Overlaps ("do both")
- The audio analogue of image-EXIF tools in this category — use those for photos/videos and Mutagen for audio; run both when a case mixes media types.

## Trust & verifiability
`trust: trusted` — a mature, widely relied-upon open-source library; it surfaces the file's real embedded tags, so verifiability is limited only by how much the file's creator (or later tools) left in place.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mutagen |
| category | documents-metadata |
| selectorsIn → selectorsOut | — → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
