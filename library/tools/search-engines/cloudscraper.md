---
id: cloudscraper
name: CloudScraper
description: Use when you have a `domain` and want to find cloud storage it references — spiders the site and returns S3/Azure/DigitalOcean bucket URLs embedded in its code.
url: https://github.com/jordanpotti/CloudScraper
category: search-engines
path:
- search-engines
bestFor: Discovering AWS S3, Azure Blob, and DigitalOcean Spaces buckets referenced in a target website's pages and source.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free/open-source (MIT); Python CLI, no account or payment.
opsec: active
opsecNote: It crawls the target's live website (multiple page requests), so the site's server sees your traffic. Route through a VPN/proxy and mind crawl depth. Only accessing storage that's publicly exposed is one thing; do not download or tamper with private data you weren't authorized to touch.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community security-recon tool by jordanpotti; MIT-licensed but low recent activity — audit before running on anything sensitive.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- awsbucketdump
- lazys3
aliases:
- CloudScraper
tags:
- toddington
- curated-directory
- cloud-recon
- infrastructure
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# CloudScraper

> A recon tool that spiders a website looking for the cloud-storage buckets it references — S3, Azure Blob, DigitalOcean Spaces — for infrastructure mapping and exposure discovery.

## When to use
You're mapping a `domain`'s infrastructure (a suspicious site, a subject's business, a service tied to a case) and want to find the cloud storage it relies on. CloudScraper crawls the site and parses HTML/JS/source for tell-tale strings (`s3.amazonaws.com`, `*.blob.core.windows.net`, DigitalOcean Spaces) to enumerate referenced buckets — which may host files, images, or documents that extend your investigation. This is infrastructure/recon work, so its direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/jordanpotti/CloudScraper and `pip install -r requirements.txt` (Python 3.6+: requests, rfc3987, termcolor).
2. Run against the target: `python CloudScraper.py -u https://target.example -d 5` (crawl depth, default 5; supports parallelism and verbose output).
3. Review the discovered bucket/blob URLs it reports.
4. For each bucket, check whether it's publicly listable (misconfigured) — but only inspect what's lawfully exposed; don't exfiltrate private data.
5. Pivot: bucket contents → documents/images for the case; storage naming → other domains/orgs on the same infrastructure via `[[awsbucketdump]]`.

## Inputs → Outputs
- **In:** a target `domain`/URL
- **Out:** referenced cloud-storage bucket URLs (S3/Azure/DO), which resolve to hosting `domain`/`ip-address`
- **Empty/negative result looks like:** no buckets found — the site doesn't reference cloud storage in its front-end code (or uses a CDN/proxy that hides it); absence isn't proof it uses none.

## Gotchas & OpSec
- **Active:** it crawls the target's live site, so your traffic is logged there — use a VPN/proxy and reasonable crawl depth.
- Legal line: finding a publicly-exposed bucket is recon; downloading/altering private data is not. Stay on the right side of authorization.
- Low maintenance — verify it still parses current cloud URL patterns before trusting a clean result.

## Overlaps ("do both")
- Pairs with `[[awsbucketdump]]` — CloudScraper finds buckets a site *references*; AWSBucketDump brute-forces/enumerates bucket names and dumps listable contents. Run in sequence.
- Pairs with `[[lazys3]]` for guessing bucket names from a company/keyword when the site doesn't reference any.

## Trust & verifiability
`trust: community` — an open-source recon tool, unaudited and lightly maintained. Its findings (bucket URLs) are directly verifiable by resolving them yourself; don't assume completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudscraper |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
