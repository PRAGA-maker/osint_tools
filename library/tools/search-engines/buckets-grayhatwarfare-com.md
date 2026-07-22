---
id: buckets-grayhatwarfare-com
name: buckets.grayhatwarfare.com
description: Use when you have a `name`, company `domain` or keyword and want to find exposed files sitting in public cloud buckets — returns matching public files and their buckets.
url: http://buckets.grayhatwarfare.com
category: search-engines
path:
- search-engines
bestFor: Searching billions of files in publicly exposed cloud storage buckets (S3, Azure, GCP, DO, Alibaba) by keyword, filename or extension.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Free (registered or not) with limited features; Premium/Enterprise unlock more buckets, bucket-exclusion and regex search.
opsec: passive
opsecNote: Searching the index is passive. Downloading a found file, however, pulls it from the exposed bucket (your IP touches the storage endpoint) — use a disposable IP, and remember that exposed ≠ authorised: handle any personal/sensitive data you find lawfully and minimally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known researcher-run index of publicly exposed buckets; results are real files you can verify directly, though coverage is a subset of all buckets.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- grayhatwarfare
- public-buckets
aliases:
- GrayHatWarfare buckets
- public buckets search
tags:
- Search engines
- Public buckets search tools
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# buckets.grayhatwarfare.com

> A search engine over billions of files in *publicly exposed* cloud storage buckets — find documents, backups and media that an organization or person left open to the world.

## When to use
You're investigating a company or individual and suspect misconfigured cloud storage has leaked files — invoices, backups, photos, spreadsheets containing PII. GrayHatWarfare indexes open S3/Azure/GCP/DigitalOcean/Alibaba buckets, so you can search by a `name`, company `domain`, or keyword and surface files that were never meant to be public.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://buckets.grayhatwarfare.com/.
2. Search by keyword, filename, or extension (e.g. a surname, a company name, `filetype:xlsx`); combine terms and exclusions.
3. Review matching files and the buckets they live in.
4. Note the free-tier limits (no bucket exclusion; regex is Enterprise-only) and refine queries accordingly.
5. Pivot: names/domains/emails inside found files feed the matching selector searches — but handle sensitive data responsibly and lawfully.

## Inputs → Outputs
- **In:** a `name`, `domain`, keyword, filename or extension
- **Out:** matching public files (`document-id`) and their bucket locations
- **Empty/negative result looks like:** no hits means nothing matching is in the *indexed subset* of open buckets — absence isn't proof no exposure exists; coverage is partial.

## Gotchas & OpSec
- Freemium: free search is capped; bucket-exclusion and regex are paid.
- **Exposed ≠ authorized:** finding a file doesn't make accessing/redistributing it lawful — treat personal/sensitive data with care and stay within your legal scope.
- Downloading a file touches the origin bucket from your IP — use a disposable IP if needed.

## Overlaps ("do both")
- Complements Google dorks for open directories and other exposed-file search engines — GrayHatWarfare is bucket-specific and deep, while dorks catch open web directories it doesn't index.

## Trust & verifiability
`trust: community` — a researcher-run index of real exposed files; every hit is a genuine object you can inspect directly, though the index covers only a subset of all public buckets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buckets-grayhatwarfare-com |
