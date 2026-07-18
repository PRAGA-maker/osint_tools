---
id: cloud-bucket-search-engine
name: Cloud Bucket Search Engine
description: Use when you have a `name`, `employer-org`, or keyword and want exposed cloud storage — returns public S3/Azure/GCS bucket listings and files indexed by Google.
url: https://cse.google.com/cse?cx=d80f8518b11b1438e
category: search-engines
path:
- search-engines
bestFor: Finding publicly-exposed cloud storage buckets (AWS S3, Azure Blob, Google Cloud Storage) and their files via a pre-built Google Custom Search Engine.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free Google Custom Search Engine (CSE); no account needed.
opsec: passive
opsecNote: You search Google's index of already-public bucket listings, not the buckets' owners — passive discovery. Do NOT download or exfiltrate files you find; viewing a listing is passive, but accessing/harvesting exposed data can be active and may be unlawful. Treat found data as sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built Google CSE that scopes searches to known cloud-storage domains; results are genuine Google index entries, but the CSE's target list and freshness depend on its (anonymous) maintainer.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cloud storage bucket search
- S3 bucket finder CSE
tags:
- cloud-storage
- s3
- google-cse
- data-exposure
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Cloud Bucket Search Engine

> A pre-scoped Google Custom Search Engine that hunts publicly-exposed cloud storage — S3/Azure/GCS bucket listings and files Google has indexed.

## When to use
You want to know whether a person or organisation has leaked files via a misconfigured public bucket. Search a `name`, `employer-org`, project codename, or keyword and the CSE returns matches restricted to cloud-storage domains (amazonaws.com S3, blob.core.windows.net, storage.googleapis.com, etc.). Good for discovering exposed documents, backups, or media tied to a subject that aren't on the open web proper.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=d80f8518b11b1438e.
2. Search a `name`, company/`employer-org`, username, or distinctive keyword; combine terms to narrow (e.g. surname + city, or a project name).
3. Read results: bucket index pages and file URLs on cloud-storage hosts.
4. Inspect a listing to see file names/paths (`document-id`) and, where files are documents/images, their embedded `metadata-exif`.
5. Pivot: an exposed file's metadata (author, GPS, device) is high-value; a bucket name often encodes the owning org, feeding further recon.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or keyword
- **Out:** public bucket listings and file URLs (`document-id`), plus any `metadata-exif` in exposed files
- **Empty/negative result looks like:** no hits — either nothing relevant is publicly exposed and indexed, or Google hasn't crawled it; absence is not proof of no exposure.

## Gotchas & OpSec
- It only finds what is **already public and indexed** — private buckets and un-crawled listings won't appear; combine with dedicated bucket-enumeration tools for active discovery.
- **Legal/ethical:** viewing an indexed listing is passive, but downloading or bulk-harvesting exposed data can cross into unauthorised access — stop at confirming exposure unless you have authority.
- Google CSEs can silently change scope or be retired by their maintainer; verify it's still returning cloud-domain results.

## Overlaps ("do both")
- Pairs with active bucket-enumeration tools (e.g. permutation-based S3 scanners) and Google-dork sheets — this CSE is the quick indexed-search pass; the scanners find un-indexed buckets it misses.

## Trust & verifiability
`trust: community` — a third-party CSE over Google's index. Individual results are verifiable (open the URL), but the engine's target-domain list and upkeep are controlled by an anonymous maintainer, so treat coverage as best-effort.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloud-bucket-search-engine |
