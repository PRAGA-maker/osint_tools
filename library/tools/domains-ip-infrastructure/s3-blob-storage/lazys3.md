---
id: lazys3
name: lazys3
description: Use when you have a `domain`/company name and want to find its cloud storage — brute-forces likely S3 bucket names and returns which ones exist and are accessible.
url: https://github.com/nahamsec/lazys3
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Permutation-based discovery of a target's Amazon S3 buckets from a company/domain keyword.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (Ruby) on GitHub; no account or key required.
opsec: active
opsecNote: lazys3 sends direct HTTP requests to AWS S3 endpoints for each guessed bucket name, so requests originate from your IP and are logged by AWS on any bucket that exists. This is active enumeration — run it from disposable/proxied infrastructure and only against organisations you are authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Authored by a well-known bug-bounty researcher (nahamsec); small, auditable Ruby script that permutes names and checks S3 — reliability rests on your wordlist, not a data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- nahamsec lazys3
tags:
- s3
- bucket-discovery
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# lazys3

> A quick S3-bucket name brute-forcer: give it a company/domain keyword and it permutes common naming patterns to find which Amazon S3 buckets actually exist — and whether they're publicly listable.

## When to use
You have an organisation tied to a `domain` or brand name and suspect it stores data in Amazon S3. lazys3 generates permutations (`company`, `company-dev`, `company-backups`, `company.assets`, region/environment suffixes, etc.) and checks each against S3, surfacing real buckets and any that are misconfigured to allow public listing — a common source of exposed documents and, occasionally, personal data.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/nahamsec/lazys3` (Ruby).
2. Run it with your base keyword(s): `ruby lazys3.rb company` (optionally supply a custom wordlist).
3. Read the results: bucket names that resolve, and the HTTP response indicating whether each is private, exists-but-denied, or openly listable.
4. For an accessible bucket, inspect its contents (via the AWS CLI or the web endpoint) — carefully and within authorisation.
5. Pivot: an exposed bucket's contents feed document/metadata analysis; discovered bucket-naming conventions feed further enumeration of the same org.

## Inputs → Outputs
- **In:** `domain`/company keyword (+ optional wordlist)
- **Out:** existing S3 bucket names and their accessibility (keyed back to the target `domain`/org)
- **Empty/negative result looks like:** no buckets resolve, or all return access-denied — the org may not use predictably-named S3, may use a different provider, or may be properly locked down; absence isn't proof of no cloud storage.

## Gotchas & OpSec
- **Active and logged:** every guess is a real request to AWS; existing buckets record it. Proxy it, throttle, and stay within scope.
- Results are only as good as the permutation wordlist — think about the org's real naming habits.
- Finding a bucket ≠ authorisation to read it; accessing contents may cross legal lines outside a sanctioned engagement.

## Overlaps ("do both")
- Pairs with other cloud-storage enumeration tools in this `s3-blob-storage` path (and with recon tools like [[magnifier]]) — different name-generation strategies surface different buckets, so run more than one.

## Trust & verifiability
`trust: community` — a small, inspectable script from a reputable researcher; it introduces no data of its own, so a "hit" is directly verifiable by querying the bucket yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lazys3 |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
