---
id: public-buckets
name: Public Buckets
description: Use when you have a `name`, `domain`, or keyword and want files leaking in open cloud storage — returns indexed public bucket objects with downloadable links.
url: https://buckets.grayhatwarfare.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Searching a pre-built index of open S3/Azure/GCP buckets by keyword, domain, or filename without scanning yourself.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
- email
status: live
pricing: freemium
costNote: Free searching with a (free) account returns limited results; deeper access, more results, and API use require a paid GrayHatWarfare subscription.
opsec: passive
opsecNote: "GrayHatWarfare queries its own precompiled index of already-public buckets, so searching does not touch the target's storage — passive. Opening/downloading a listed object does fetch it from the provider, which logs your IP. Your searches are tied to your GrayHatWarfare account; use a sock-puppet account, and only access data you are authorized to."
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial index of exposed buckets; results reflect what its crawler has found and may be stale (a listed object can be removed/secured since indexing).
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- buckets-grayhatwarfare-com
- grayhatwarfare
- url-shorteners-search
aliases:
- GrayHatWarfare Public Buckets
- buckets.grayhatwarfare.com
tags:
- s3
- cloud-storage
- exposed-data
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Public Buckets

> GrayHatWarfare's searchable index of open S3/Azure/GCP buckets — find exposed files by keyword, domain, or filename without running your own scanner.

## When to use
You want to know whether documents, backups, or media tied to a target — a `domain`, a `name`, a project keyword — are sitting in a misconfigured public cloud bucket. Because it searches a pre-built index, you get results instantly and passively, rather than brute-forcing bucket names yourself. Infrastructure/breach-oriented; a leaked bucket can incidentally expose people's documents and contact data, but direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (free) account at https://buckets.grayhatwarfare.com/ and log in via a sock-puppet identity.
2. Search by keyword, `domain`, filename, or extension (e.g. `target.com`, `passwords.xlsx`, `.sql`).
3. Read the indexed matches: bucket name, object path/filename, size, and a link.
4. Before opening a file, note that clicking fetches it from the provider (logged); only access what you're authorized to.
5. Pivot: an exposed document's `document-id`/contents or an embedded `email` feeds the rest of your investigation.

## Inputs → Outputs
- **In:** `name`, `domain`, or keyword/filename
- **Out:** indexed public bucket objects (paths, links); potential `document-id`s and `email`s inside the files
- **Empty/negative result looks like:** no matches — nothing matching your terms is in GHW's index; the target may have no exposed bucket, or one GHW hasn't crawled. Absence isn't proof of no exposure.

## Gotchas & OpSec
- Free tier caps results heavily; the full index and API need a paid plan.
- The index can be stale — a listed object may already be secured/deleted (404 on open), and new exposures may not be indexed yet.
- **Legal/ethical:** "public" does not mean you're authorized to download; treat access carefully and lawfully.

## Overlaps ("do both")
- Complements active scanners like [[bucketloot]] and its siblings [[grayhatwarfare]] / [[buckets-grayhatwarfare-com]] — search the index here first (passive), then use a scanner to loot a specific bucket you're authorized to inspect.

## Trust & verifiability
`trust: community` — an established commercial index; results are real crawler findings but can be dated, so verify a hit by (authorized) direct access and don't assume a listing is still live.
