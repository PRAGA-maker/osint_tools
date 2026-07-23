---
id: bucketloot
name: BucketLoot
description: Use when you have an exposed cloud bucket URL (`domain`) and want to mine it — returns secrets, sensitive files, and extracted `email`/`domain`/subdomain assets.
url: https://github.com/redhuntlabs/BucketLoot
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Automated inspection of a public S3/GCS/DigitalOcean bucket for secrets, keywords, and leaked assets.
selectorsIn:
- domain
selectorsOut:
- email
- domain
status: live
pricing: free
costNote: Free and open-source (MIT); a single Go binary. Guest mode scans up to ~1,000 files without any cloud credentials.
opsec: active
opsecNote: "BucketLoot fetches objects directly from the target bucket, so the cloud provider's access logs record your IP against those GET requests — this is active collection. Only run it against buckets you are authorized to inspect; accessing others' storage may be unlawful even when 'public.' Route through a proxy/VPN and a sock-puppet identity, and never exfiltrate real personal data you find."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by RedHunt Labs (open-source, presented at Black Hat); it inspects public/exposed storage, and any secret it flags should be validated before you rely on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- BucketLoot
- redhuntlabs/BucketLoot
tags:
- s3
- cloud-storage
- secrets-scanning
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# BucketLoot

> An automated cloud-bucket inspector: point it at an exposed S3/GCS/DigitalOcean bucket and it scans the objects for secrets, sensitive files, and extractable assets.

## When to use
You have found (or been given) a publicly-exposed cloud storage bucket linked to a target `domain` and want to know what's inside — leaked credentials, config files, and embedded URLs/subdomains/`email`s — without downloading and grepping it by hand. Infrastructure/breach-focused work; direct missing-persons relevance is low, but a leaked bucket can incidentally expose contact data or documents about people.

## How to use it (`bestInteractionPattern`: cli)
1. Download the release binary or `go install` from https://github.com/redhuntlabs/BucketLoot.
2. Run in guest mode against a target bucket URL: `bucketloot <bucket-url>` (scans up to ~1,000 files with no credentials).
3. For a full scan, supply the relevant cloud credentials; use "Dig Mode" to check whether a non-S3 site references buckets.
4. Read the JSON report: detected secrets (80+ signatures), sensitive filenames, and extracted assets (URLs, subdomains, `domain`s, `email`s), or run custom keyword/regex searches.
5. Validate any flagged secret before acting; pivot extracted `domain`s/subdomains into passive-DNS tooling.

## Inputs → Outputs
- **In:** a cloud bucket URL (S3/GCS/DigitalOcean/custom `domain`)
- **Out:** secrets, sensitive files, extracted `email`s/`domain`s/subdomains, JSON report
- **Empty/negative result looks like:** no matches / access denied — the bucket may be genuinely clean, actually private, or restrict listing; a null result isn't proof there's nothing there.

## Gotchas & OpSec
- **Active + legal risk:** you fetch objects directly (logged by the provider), and accessing third-party storage can be unlawful even if "public" — only scan what you're authorized to.
- Regex secret detection produces false positives; validate before trusting a flagged key.
- Guest mode caps at ~1,000 files, so large buckets are sampled, not fully covered.

## Overlaps ("do both")
- Pairs with other S3/blob-discovery tools (to *find* buckets) and passive-DNS tools like [[dns-dumpster]] — discovery tools locate the bucket, BucketLoot loots it, then you pivot the extracted domains onward.

## Trust & verifiability
`trust: community` — a reputable, conference-vetted open-source tool from RedHunt Labs; its findings are leads (especially the regex secret hits), so confirm each before relying on it.
