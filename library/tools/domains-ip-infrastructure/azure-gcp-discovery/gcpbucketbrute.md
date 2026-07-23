---
id: gcpbucketbrute
name: GCPBucketBrute
description: Use when you have a target `name`/`domain` and want its Google Cloud Storage buckets — returns valid bucket names and their access/permission status.
url: https://github.com/RhinoSecurityLabs/GCPBucketBrute
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Enumerating and permission-testing likely Google Cloud Storage bucket names for a target.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source (Rhino Security Labs); Python. Works unauthenticated or with (your own) GCP credentials for privilege checks.
opsec: active
opsecNote: "GCPBucketBrute sends requests directly to Google Cloud Storage endpoints for each candidate bucket, so the activity is visible in Google's/target's logs and originates from your IP unless proxied — this is active enumeration. Only run it against targets you're authorized to assess; brute-forcing others' cloud infrastructure may be unlawful. Route through a proxy and use throwaway GCP creds for the permission checks."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by Rhino Security Labs, a reputable cloud-security firm; it tests real GCS endpoints, so a reported bucket/permission is verifiable, though wordlist-driven guessing is inherently incomplete.
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
- GCPBucketBrute
- RhinoSecurityLabs/GCPBucketBrute
tags:
- gcp
- cloud-storage
- bucket-enumeration
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# GCPBucketBrute

> Generates likely Google Cloud Storage bucket names from a keyword and tests each for existence and access — the GCS counterpart to S3 bucket enumeration.

## When to use
You're mapping a target's (`name`/`domain`) cloud footprint and want to find their Google Cloud Storage buckets and whether any are misconfigured (publicly listable/readable, or open to authenticated users). It permutes a base keyword into candidate bucket names and checks permissions. Infrastructure/breach-focused; an exposed bucket can incidentally hold documents about people, but direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: cli)
1. Clone from https://github.com/RhinoSecurityLabs/GCPBucketBrute and install its Python requirements.
2. Run with a keyword: `python3 gcpbucketbrute.py -k <target-keyword> -u` (`-u` = unauthenticated), optionally supplying GCP creds to test authenticated access.
3. It generates permutations, queries GCS, and reports which buckets exist and their access level (public, authenticated, private).
4. For any open bucket, review contents carefully and only within your authorization; treat exposed files (`document-id`s) as findings.
5. Pivot discovered assets/keywords into broader recon.

## Inputs → Outputs
- **In:** target keyword (from a `name`/`domain`) + optional GCP creds
- **Out:** valid GCS bucket names with access/permission status; exposed objects (`document-id`s)
- **Empty/negative result looks like:** no valid buckets or all private — the target may use no public GCS, or names not covered by your keyword/permutations; absence isn't proof of no cloud storage.

## Gotchas & OpSec
- **Active + legal:** direct requests to GCS are logged; enumerating third-party cloud infrastructure can be unlawful — only run against authorized targets.
- Coverage is wordlist-bound — a real bucket with an unguessed name won't appear; enrich the keyword list.
- Accessing an "open" bucket's data still requires authorization; open ≠ permitted.

## Overlaps ("do both")
- The GCS analogue of S3 tools like [[bucketloot]] and index search [[public-buckets]] — enumerate GCS here, S3 with those; run both to cover a multi-cloud target.

## Trust & verifiability
`trust: community` — from a reputable cloud-security firm; results are live GCS checks and thus directly verifiable, with wordlist coverage as the main limitation.
