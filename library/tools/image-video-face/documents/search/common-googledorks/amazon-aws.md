---
id: amazon-aws
name: Amazon AWS
description: Use when you want to surface publicly exposed files in Amazon S3 buckets tied to a name, company, or project by running a Google site-search dork.
url: https://www.google.com/search?q=site:s3.amazonaws.com+%3Csearchterm%3E
category: image-video-face
path:
- image-video-face
- documents
- search
- common-googledorks
bestFor: Finding open/misconfigured S3 buckets and the documents, images, or backups inside them via Google dorking.
selectorsIn:
- name
- employer-org
- domain
selectorsOut:
- document-id
- image
- metadata-exif
status: live
pricing: free
costNote: Uses Google search; free.
opsec: passive
opsecNote: The dork query hits Google, not the target. Opening any discovered S3 object, however, contacts AWS directly and leaves your IP in bucket/CDN logs — pivot through a sock-puppet/VPN before downloading.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A standard, well-known Google dork pattern (site:s3.amazonaws.com); the technique is reliable, results depend entirely on what is publicly indexed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- s3.amazonaws.com dork
- S3 bucket Google dork
tags:
- google-dork
- cloud-storage
source: arf-seed
lastVerified: ''
enrichment: full
---

# Amazon AWS (S3 bucket Google dork)

> A Google site-search dork that surfaces files exposed in public Amazon S3 buckets.

## When to use
You have a `name`, `employer-org`, or `domain` and want to find documents, photos, or backups a person or organization left in a publicly readable S3 bucket — material that often carries `metadata-exif` (geotags, device IDs) useful in a missing-persons case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the URL and replace `<searchterm>` with your term, e.g. `site:s3.amazonaws.com "JohnDoe"` or `site:s3.amazonaws.com companyname`.
2. Run it in Google; refine with file-type operators (`filetype:pdf`, `filetype:jpg`) or extra keywords.
3. Review hits — each is a publicly indexed object URL in some bucket.
4. Pivot: download via a sandboxed/VPN session, then run images through EXIF/metadata extraction (`[[apache-tika]]`) and reverse-image search.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `domain`
- **Out:** `document-id`, `image`, `metadata-exif`
- **Empty/negative result looks like:** zero results (nothing indexed) — does NOT mean no exposed buckets exist, only that Google has not indexed them. Try `s3.us-east-1.amazonaws.com` and other region/host variants.

## Gotchas & OpSec
- Human-in-the-loop: heavy dorking triggers Google CAPTCHAs/rate limits.
- OpSec: the search itself is passive (against Google). Fetching any discovered object contacts AWS and logs your IP — always pivot through a sock puppet/VPN before opening files. Accessing genuinely private data can be unlawful; stay within public, indexed content.

## Overlaps ("do both")
- Pairs with metadata extraction (`[[apache-tika]]`) on any documents/images you recover, and with reverse-image search to identify people in recovered photos.

## Trust & verifiability
`trust: community` — a long-established Google dork pattern; the method is sound, coverage is whatever is publicly indexed at query time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-aws |
| category | image-video-face |
| selectorsIn → selectorsOut | name, employer-org, domain → document-id, image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
