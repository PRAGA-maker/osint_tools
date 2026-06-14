---
id: apache-tika
name: Apache Tika
description: Use when you have recovered documents, images, or media and want to extract their text and embedded metadata (EXIF, author, GPS, timestamps) at scale, locally.
url: https://tika.apache.org/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Bulk, local text and metadata extraction across thousands of mixed file types.
selectorsIn:
- document-id
- image
- metadata-exif
selectorsOut:
- metadata-exif
- geolocation
- name
- device-id
status: live
pricing: free
costNote: Free and open source (Apache 2.0); no account or API key.
opsec: passive
opsecNote: Runs entirely locally when self-hosted, so files never leave your machine — the most OpSec-safe way to read metadata from sensitive case material. (A hosted Tika server changes this; run it locally.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Mature, widely-used Apache Software Foundation project; the same content-detection/extraction engine behind many enterprise search and forensics pipelines. Output fidelity depends on what metadata the file actually contains.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Tika
tags:
- metadata
- exif
source: arf-seed
lastVerified: ''
enrichment: full
---

# Apache Tika

> A free, local content-detection and metadata-extraction toolkit covering thousands of file types in one tool.

## When to use
You have a batch of recovered files — photos, PDFs, Office docs, media — and want their embedded `metadata-exif` (GPS coordinates, camera/`device-id`, author `name`, creation timestamps) and full text without uploading anything to a third party. Ideal when an S3 dork, social scrape, or device dump leaves you with many heterogeneous files to triage.

## How to use it (`bestInteractionPattern`: cli)
1. Install Java, download the Tika app jar from https://tika.apache.org/.
2. Run on one file: `java -jar tika-app.jar -m photo.jpg` (`-m` = metadata only; `-t` = plain text; omit for full XHTML).
3. Batch a folder by looping the jar, or run `java -jar tika-server.jar` and POST files to the local REST endpoint for scripted extraction.
4. Pivot: feed extracted GPS to mapping/`geolocation` workflows, camera serials/`device-id` to device correlation, and author names to people-search.

## Inputs → Outputs
- **In:** `document-id`, `image`, `metadata-exif` (files)
- **Out:** `metadata-exif`, `geolocation` (GPS), `name` (author/creator), `device-id` (camera/make/model/serial), plus extracted text
- **Empty/negative result looks like:** sparse metadata — most web-hosted images are stripped of EXIF (esp. social-media re-uploads), so empty GPS/author is common and expected, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none for extraction; you interpret the fields.
- OpSec: passive and local when self-hosted — files never leave your machine, making it safe for sensitive case material. Do NOT use a random public hosted Tika instance for sensitive files.

## Overlaps ("do both")
- Pairs with S3/document dorks like `[[amazon-aws]]` (extract metadata from recovered files) and with reverse-image search; Tika reads the metadata, reverse search reads the pixels.

## Trust & verifiability
`trust: trusted` — a mature Apache Software Foundation project; results are deterministic and reflect exactly what is embedded in each file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apache-tika |
| category | image-video-face |
| selectorsIn → selectorsOut | document-id, image, metadata-exif → metadata-exif, geolocation, name, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
