---
id: s3scanner
name: S3Scanner
description: Use when you have a target `domain`/organisation and want to find its open cloud storage buckets — returns exposed S3-compatible buckets and their read/write permissions.
url: https://github.com/sa7mon/s3scanner
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Enumerating and permission-testing open S3 (and S3-compatible) buckets across cloud providers.
selectorsIn:
- domain
- employer-org
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source (MIT); Go CLI with Docker support. No account for public-bucket checks.
opsec: active
opsecNote: ACTIVE — it sends requests to candidate bucket endpoints and tests permissions, which cloud providers/targets can log. Only run against organisations you are authorised to assess; do NOT download or alter bucket contents. Route through a VPN.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, well-maintained open-source scanner (sa7mon); it reports bucket existence/permissions accurately, but candidate name generation is only as good as your wordlist.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- s3scanner
tags:
- domains-ip-infrastructure
- cloud
- s3
- bucket-enumeration
- cli
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# S3Scanner

> A CLI scanner that finds open S3 (and S3-compatible) buckets and tests their permissions — surface an organisation's exposed cloud storage.

## When to use
You are assessing an organisation (`employer-org`/`domain`) and want to know whether it has publicly-readable or writable cloud storage leaking documents. S3Scanner checks candidate bucket names across AWS, GCP, DigitalOcean, Linode, Scaleway and custom endpoints, and reports which exist and what permissions (read/write/ACP) are open.

## How to use it (`bestInteractionPattern`: cli)
1. Install the Go binary or use the Docker image (see https://github.com/sa7mon/s3scanner).
2. Feed it a bucket name, or a file of candidate names generated from the target's `domain`/`employer-org` (e.g. `acme-backups`, `acme-assets`).
3. Run the scan; read console/JSON output showing each bucket's existence and open permissions.
4. Pivot: an open, readable bucket may expose documents (`document-id`), backups, or credentials — note them for the report; never exfiltrate.

## Inputs → Outputs
- **In:** candidate bucket names derived from `domain`/`employer-org`
- **Out:** which buckets exist and their open permissions (potential exposed `document-id`s)
- **Empty/negative result looks like:** all candidates return "not found" or "access denied" — no open buckets under the names you tried; try a broader/smarter wordlist before concluding none exist.

## Gotchas & OpSec
- ACTIVE and logged — authorisation required; treat like any external scan.
- Findings depend entirely on your candidate name list; a miss means "not these names", not "no exposure".
- Testing permissions is fine; reading/altering contents may be unlawful even when the bucket is open — stop at existence/permission.

## Overlaps ("do both")
- Complements broader recon (`[[finalrecon]]`) and cert/subdomain enumeration — those give you the org's naming conventions to build better bucket wordlists for this.

## Trust & verifiability
`trust: community` — a mature, widely-used open-source tool that reliably reports bucket state; the completeness of a scan is bounded by your wordlist, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | s3scanner |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, employer-org → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
