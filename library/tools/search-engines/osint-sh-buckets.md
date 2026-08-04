---
id: osint-sh-buckets
name: OSINT.SH Public Buckets
description: Use when you have a keyword/`employer-org`/`domain` and want publicly-exposed cloud storage — searches AWS S3 and Azure Blob for open buckets matching the term, returns bucket URLs and their file listings.
url: http://osint.sh/buckets
category: search-engines
path:
- search-engines
bestFor: Finding open AWS S3 / Azure Blob buckets tied to a name, brand, or project keyword, and browsing their exposed files.
selectorsIn:
- employer-org
- domain
selectorsOut:
- document-id
- domain
status: live
pricing: free
costNote: Free web tool, part of the OSINT.SH all-in-one toolkit; no account required.
opsec: passive
opsecNote: The keyword search hits OSINT.SH's index, not the target — passive. But OPENING a discovered bucket/file fetches it from the cloud provider and is logged in that bucket's access logs; browse discovered buckets through a VPN and never download anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known free OSINT toolkit; bucket results depend on what's currently indexed/public and can be incomplete or stale — verify by opening the bucket.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- osint.sh buckets
- Public Buckets search
tags:
- cloud-buckets
- s3
- azure-blob
- exposed-storage
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# OSINT.SH Public Buckets

> Keyword search across open AWS S3 and Azure Blob storage — find misconfigured public buckets tied to a name, brand, or project, then browse what's exposed inside.

## When to use
You have a keyword that names a person, `employer-org`, product, or `domain`, and want to know if any cloud storage bucket bearing that name is publicly readable. Exposed buckets frequently contain documents, backups, images, and occasionally credentials — a rich source of `document-id`s and leads. Reach for it when investigating an organisation's data hygiene, hunting for leaked files tied to a project, or expanding from a brand name to its infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://osint.sh/buckets/.
2. Enter a keyword — a company name, product, username, or domain fragment.
3. Review returned buckets (AWS S3 / Azure Blob) matching the term; each hit is a bucket URL.
4. Open a bucket to view its public file listing (if the ACL allows listing).
5. Pivot: exposed `document-id`s feed metadata/EXIF analysis; the bucket naming and linked `domain` feed infrastructure OSINT. Browse via VPN — opening files is logged by the provider.

## Inputs → Outputs
- **In:** keyword (`employer-org`, `domain`, product, name)
- **Out:** open bucket URLs, their file listings (`document-id`s), associated `domain`
- **Empty/negative result looks like:** no buckets for the keyword — either none are public/indexed, or the naming doesn't match your term; try name variants and combine with GrayhatWarfare before concluding nothing is exposed.

## Gotchas & OpSec
- Results reflect what's *indexed and currently public*; a bucket may have been closed since indexing (open the URL to confirm).
- Legal/ethical: viewing a public listing is passive, but downloading exposed private data can cross legal lines — record locations, don't exfiltrate.
- OpSec: opening a bucket/file hits the provider and is logged; use a VPN and a sock-puppet context.

## Overlaps ("do both")
- Pairs with `[[grayhatwarfare]]`-style bucket databases: OSINT.SH and GrayhatWarfare index different subsets of public buckets — run the same keyword through both to maximise coverage.

## Trust & verifiability
`trust: community` — a popular free toolkit, but bucket indexes are inherently partial and time-sensitive; treat every hit as a lead and verify current exposure by opening the bucket yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-sh-buckets |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, domain → document-id, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
