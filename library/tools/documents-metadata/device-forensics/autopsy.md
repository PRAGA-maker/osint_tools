---
id: autopsy
name: Autopsy
description: Use when you have a `device-id` disk image or phone backup and want to extract artifacts — returns files, deleted data, timelines, EXIF/geolocation, and app databases.
url: https://www.autopsy.com/
category: documents-metadata
path:
- documents-metadata
- device-forensics
bestFor: Deep forensic analysis of a disk image, phone backup, or file system — recovering deleted files, building timelines, and pulling embedded metadata.
selectorsIn:
- device-id
- metadata-exif
selectorsOut:
- metadata-exif
- geolocation
- document-id
status: live
pricing: free
costNote: Free and open source (built on The Sleuth Kit); optional paid training/support exists but the platform itself is free.
opsec: passive
opsecNote: Passive — you analyze a static forensic image or backup locally on your own machine; nothing touches the internet or the source device, so there is zero leakage to any subject. Ensure you have lawful authority over the image you examine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: The premier open-source digital-forensics platform (Sleuth Kit Labs / Basis Technology), used by tens of thousands of law-enforcement and corporate investigators; source is auditable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Autopsy Forensic Browser
- Sleuth Kit Autopsy
tags:
- device-forensics
- disk-image
- deleted-files
- timeline
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Autopsy

> The leading open-source digital-forensics workstation — mount a disk image or phone backup and recover the files, deleted data, timelines, and metadata that place a person and reconstruct their activity.

## When to use
You have lawful access to a `device-id` artifact — a hard-drive/phone image, an app database, or a backup — belonging to (or found with) a missing or investigated person, and you need to extract everything of intelligence value: recently used files, deleted photos, browser and location history, message databases, and embedded EXIF/GPS. This is the workhorse when the evidence is a *device*, not a live web account, and it is high-value in missing-persons work because a subject's own device often carries their last-known-location and contacts.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Autopsy from https://www.autopsy.com/ (Windows; also runs on Linux/macOS via The Sleuth Kit).
2. Create a case and add a data source — a disk image (E01/dd), a logical file set, or a phone extraction/backup.
3. Let the ingest modules run: hash lookup, keyword search, EXIF, web artifacts, recent activity, deleted-file recovery, and timeline.
4. Review results by module: **Geolocation** and **EXIF** for where photos were taken, **Web History** for accounts/locations, **Timeline** to reconstruct the sequence of activity, **Deleted Files** for recovered content.
5. Pivot: recovered `metadata-exif`/`geolocation` feeds a map; account names and emails feed username/email OSINT; a `document-id` or contact list feeds identity work.

## Inputs → Outputs
- **In:** a `device-id` forensic image / backup / app database (and the `metadata-exif` embedded within)
- **Out:** recovered files and `document-id`s, deleted data, activity timelines, `metadata-exif`, and GPS `geolocation`
- **Empty/negative result looks like:** a wiped, encrypted, or full-disk-encrypted source yields little or nothing — an empty ingest means inaccessible data, not a clean device.

## Gotchas & OpSec
- **Authority required:** only examine images you are lawfully entitled to analyze; forensic soundness (write-blocking, hashing the original) matters if findings must hold up.
- Local and offline — no network exposure — but the analysis machine now holds sensitive data; handle and store it securely.
- Encryption (BitLocker/FileVault/modern iOS/Android) will block content without keys; Autopsy can't break it.
- It analyzes *images/backups*, not live devices — acquire the image with a proper tool first.

## Overlaps ("do both")
- Complements cloud/account OSINT — Autopsy reconstructs what's *on the device* (deleted photos, local databases), while account-side tools reconstruct what's *in the cloud*; together they cross-fill each other's gaps.

## Trust & verifiability
`trust: trusted` — open-source and built on the widely peer-reviewed Sleuth Kit; its methods are documented and its results reproducible, which is why it's a courtroom-grade standard in DFIR.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | autopsy |
| category | documents-metadata |
| selectorsIn → selectorsOut | device-id, metadata-exif → metadata-exif, geolocation, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
