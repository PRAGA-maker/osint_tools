---
id: ghiro
name: Ghiro
description: Use when you have one or many `image`s and want automated forensic analysis — returns extracted EXIF/metadata, GPS `geolocation`, hashes, and manipulation signals from a self-hosted appliance.
url: https://getghiro.org/
category: image-video-face
path:
- image-video-face
- images
- forensics
bestFor: Batch, automated image forensics — metadata, GPS, hashing, and tamper indicators — on your own infrastructure.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free and open source; self-hosted (a downloadable appliance/VM or Docker). Runs on your own hardware, so no per-use cost.
opsec: passive
opsecNote: Runs entirely on infrastructure you control — images never leave your environment, which is ideal for sensitive evidence and chain-of-custody. No third party sees the files. Keep the instance isolated/patched.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: An established open-source digital-image-forensics project; results are reproducible and auditable, but it is community-maintained and updates are infrequent.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- metadata2go
- online-exif-viewer
aliases:
- Ghiro
- getghiro
tags:
- image-forensics
- exif
- metadata
- self-hosted
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Ghiro

> A self-hosted image-forensics appliance — feed it a batch of photos and get metadata, GPS, hashes, and tamper indicators, all on your own infrastructure.

## When to use
You have one or (especially) many `image`s and want automated, repeatable forensic analysis without uploading anything to a third party. Ghiro extracts EXIF/IPTC/XMP metadata, pulls GPS `geolocation`, computes hashes, runs signature/consistency checks, and flags manipulation — at scale and in a case-managed way. It's the right choice when files are sensitive (missing-persons evidence) or when you need to process a large image set consistently rather than one-off online lookups.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy Ghiro on your own hardware (download the appliance/VM or run via Docker) and create a case.
2. Upload the `image`(s) into the case — single files or bulk.
3. Let it analyse: it extracts metadata, GPS, hashes, thumbnails, and forensic signals automatically.
4. Read the per-image report: EXIF (`metadata-exif`), map of any GPS `geolocation`, hash matches, and error-level/consistency findings.
5. Pivot: GPS coordinates feed mapping; hashes support dedup/known-image matching; metadata anchors timelines.

## Inputs → Outputs
- **In:** `image`(s), individually or in bulk, into a case
- **Out:** `metadata-exif`, GPS `geolocation`, hashes, thumbnails, and manipulation/consistency signals
- **Empty/negative result looks like:** little metadata and no GPS — common for social-media-sourced images (EXIF is stripped on upload). An empty metadata report reflects the file, not a Ghiro failure.

## Gotchas & OpSec
- Requires **self-hosting** (appliance/Docker) — more setup than an online viewer, but that's the point for sensitive evidence.
- Community-maintained with infrequent updates; verify it runs on current infrastructure.
- Social-media images usually have stripped EXIF — absence of GPS is expected there.
- OpSec: **passive** and confidential — files stay on your infrastructure.

## Overlaps ("do both")
- Pairs with `[[metadata2go]]` and `[[online-exif-viewer]]` — those are quick online one-offs; Ghiro is the batch, case-managed, self-hosted option for volume and confidentiality.

## Trust & verifiability
`trust: community` — open source and auditable (you control the pipeline), though community-maintained; ideal when reproducibility and keeping evidence in-house matter.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghiro |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
