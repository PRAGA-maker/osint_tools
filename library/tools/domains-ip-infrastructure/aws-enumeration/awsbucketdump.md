---
id: awsbucketdump
name: AWSBucketDump
description: Use when you have an `employer-org`/`domain` and want to find exposed Amazon S3 buckets and download their contents — returns discovered bucket names and their public object listings/files.
url: https://github.com/jordanpotti/AWSBucketDump
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- aws-enumeration
bestFor: Guessing an organisation's S3 bucket names from keywords/wordlists and grabbing any publicly-readable files.
selectorsIn:
- employer-org
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source Python tool; run locally.
opsec: active
opsecNote: It sends requests directly to AWS S3 endpoints and can download objects — this touches AWS infrastructure and, for a targeted org, may be logged/attributable. Only run against assets you're authorised to test; route through a proxy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Known open-source S3-enumeration tool (jordanpotti). Effective but older; results depend entirely on your keyword/wordlist quality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- cloudscraper
aliases: []
tags:
- aws-enumeration
- cloud-recon
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# AWSBucketDump

> An S3-bucket brute-forcer — feed it an organisation's names and keywords, and it finds guessable public buckets and pulls down whatever they expose.

## When to use
You have an `employer-org`/`domain` and suspect misconfigured cloud storage — organisations routinely leave S3 buckets world-readable, exposing documents, backups and databases. AWSBucketDump generates candidate bucket names from your keywords/wordlist, checks which exist and are readable, and downloads the contents. Infrastructure/security-recon tool; low direct missing-persons relevance but can surface leaked documents naming people.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/jordanpotti/AWSBucketDump && pip install -r requirements.txt`.
2. Prepare a wordlist of likely bucket names (org name, brands, projects + common suffixes).
3. Run: `python AWSBucketDump.py -l wordlist.txt -D` (with `-D` to download found objects), optionally a grep list of interesting filenames.
4. Review discovered buckets and downloaded files.
5. Pivot: leaked documents may contain `name`s, `email`s, `address`es and internal detail — treat exposed files as leads and handle responsibly.

## Inputs → Outputs
- **In:** `employer-org`/`domain`-derived keywords and a wordlist
- **Out:** discovered S3 bucket names and their public object listings/files (`document-id`)
- **Empty/negative result looks like:** no readable buckets found — the org has no guessable public buckets (good hygiene) or your wordlist missed the naming scheme. Refine keywords before concluding nothing is exposed.

## Gotchas & OpSec
- Human-in-the-loop: none, but quality hinges on the wordlist you supply.
- OpSec: **active** — direct requests to AWS and file downloads are attributable and may be logged. Only test authorised targets; proxy your traffic; be mindful that downloading third-party data can have legal implications.
- Older tool; modern alternatives (cloud_enum, S3Scanner) cover more providers — cross-check for completeness.

## Overlaps ("do both")
- Pairs with `[[cloudscraper]]` and broader cloud-enumeration tools — AWSBucketDump targets S3 specifically; run a multi-cloud enumerator to cover GCP/Azure storage too.

## Trust & verifiability
`trust: community` — an established open-source recon tool; found buckets and files are real, but relevance and completeness depend on your inputs, so treat coverage as non-exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awsbucketdump |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org, domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
