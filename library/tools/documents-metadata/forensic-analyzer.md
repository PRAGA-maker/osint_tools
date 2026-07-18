---
id: forensic-analyzer
name: Forensic Analyzer
description: Use when you have an `image` and want to check for manipulation and pull embedded metadata — returns EXIF/IPTC/XMP blocks, GPS `geolocation`, hashes, and an error-level-analysis map.
url: https://www.imageforensic.org
category: documents-metadata
path:
- documents-metadata
bestFor: Free browser-based error-level analysis plus full EXIF/GPS/metadata extraction on a single uploaded image.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free to use; results are stored for 7 days then expire (resubmit to regenerate). No account required.
opsec: active
opsecNote: Active in the sense that you upload the target image to a third-party server that retains it for 7 days. Never upload sensitive/case-original media you cannot risk exposing; strip nothing beforehand if you need the metadata, but assume the file leaves your control. Use a copy, not the master.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent hobby/research image-forensics service implementing the well-documented Krawetz ELA method plus the open-source exifr parser; results are reproducible but the operator is not a named institution.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- image-forensic-ghiro-online
aliases:
- imageforensic.org
- Digital Image Forensic Analyzer
tags:
- metadata
- exif
- image-forensics
- error-level-analysis
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Forensic Analyzer

> Browser-based image forensics: error-level analysis to spot edits, plus a full EXIF/IPTC/XMP/GPS dump — with coordinates that link straight into a map.

## When to use
You have an `image` (a photo of a person, place, or document) and want two things at once: (1) whether it has been manipulated/re-compressed, via error-level analysis, and (2) any embedded metadata — camera model, timestamps, and especially GPS coordinates that place where the shot was taken. Ideal for verifying a photo attached to a missing-persons tip, a social-media image, or a classified-ad listing before trusting it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.imageforensic.org in a sock-puppet browser session.
2. Upload the image (use a copy — the server keeps it for 7 days).
3. Read the **Error Level Analysis** map: regions at compression equilibrium render dark; areas with a different compression history (a pasted face, an added object, an erased plate) render bright — those bright patches flag likely edits.
4. Read the **metadata** panel: dimensions, MIME type, SHA-256 fingerprint, and full EXIF/IPTC/XMP/ICC blocks. If GPS tags survive, the coordinates link directly to OpenStreetMap.
5. Pivot: GPS `geolocation` feeds a map/reverse-geocode workflow; a camera serial or timestamp corroborates or contradicts a subject's story; an ELA-flagged edit means treat the image as untrusted.
6. (Optional) A simple REST API accepts an HTTP POST of the image for automated submission.

## Inputs → Outputs
- **In:** an uploaded `image` (and by extension its embedded `metadata-exif`)
- **Out:** parsed `metadata-exif` (EXIF/IPTC/XMP/ICC), GPS `geolocation`, file hashes, and an ELA overlay
- **Empty/negative result looks like:** a stripped image (uploaded to a social network, screenshotted, or re-saved) returns little or no EXIF and no GPS — absence of metadata is common and is not proof of tampering; ELA on a clean original is uniformly dark.

## Gotchas & OpSec
- **Upload leaves your control:** the file sits on a third-party server for 7 days. Use a non-sensitive copy; never submit case-original media you must keep contained.
- ELA is a heuristic, not proof — heavy compression, resizing, or a single global re-save can produce misleading bright areas. Corroborate before concluding "faked."
- Most images from social platforms are already stripped of EXIF/GPS; don't expect coordinates from a Facebook/Instagram download.

## Overlaps ("do both")
- Pairs with `[[image-forensic-ghiro-online]]` — run both when a result is ambiguous, since different ELA/quantization implementations surface different artifacts, and cross-confirmation reduces false positives.

## Trust & verifiability
`trust: community` — an independent forensics service built on the openly documented Krawetz ELA technique and the open-source `exifr` metadata parser; the method is reproducible and auditable even though the operator isn't a named institution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensic-analyzer |
| category | documents-metadata |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
