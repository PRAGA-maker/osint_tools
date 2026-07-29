---
id: cloud-enum
name: cloud_enum
description: Use when you have an `employer-org`/`domain` or keyword and want to find that entity's exposed public cloud storage (AWS S3, Azure, GCP) — returns discovered `domain`/URL buckets and endpoints.
url: https://github.com/initstring/cloud_enum
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- aws-enumeration
bestFor: Enumerating an organisation's public/exposed cloud storage across AWS, Azure, and GCP from names and keywords.
selectorsIn:
- employer-org
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source Python tool; run locally.
opsec: active
opsecNote: It sends direct enumeration requests to AWS/Azure/GCP endpoints derived from your keywords. Those providers (and, via access logs, sometimes the resource owner) can see the probes. Run from an attributable-to-nobody host/VPN and only against targets you are authorised to assess.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source tool by initstring; widely used in cloud-security assessment. Verify buckets it flags before drawing conclusions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- initstring-linkedin2username
aliases:
- cloud_enum
tags:
- cloud-enumeration
- aws
- azure
- gcp
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# cloud_enum

> Multi-cloud OSINT enumerator that guesses and confirms an organisation's public AWS S3 buckets, Azure blobs, and GCP storage from names and keywords — a fast way to surface accidental data exposure.

## When to use
You are investigating an organisation (`employer-org`) or `domain` and want to know whether it has publicly-exposed cloud storage — buckets that may leak documents, backups, or personal data. cloud_enum brute-forces provider-specific naming patterns from your keyword list and reports which resources exist and whether they are open.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/initstring/cloud_enum.git` then `pip install -r requirements.txt`.
2. Run against a keyword: `python3 cloud_enum.py -k companyname -k company-name -k companyabbrev`.
3. Add a custom mutations wordlist (`-m`) to widen coverage; supply several keyword variants for better hit rate.
4. Read the output: it lists discovered S3/Azure/GCP resources and flags which are publicly readable vs protected.
5. Pivot: open readable buckets to inventory exposed files; feed org keywords into `[[initstring-linkedin2username]]` for the human side.

## Inputs → Outputs
- **In:** `employer-org`/`domain`/keywords (company names and abbreviations)
- **Out:** discovered cloud-storage `domain`/URLs by provider, with open/closed status
- **Empty/negative result looks like:** no resources found for your keywords — likely means poor keyword coverage or no exposure; try more name variants before concluding "clean."

## Gotchas & OpSec
- **Active** enumeration: providers log the probes; only run against authorised targets.
- Hit rate depends entirely on keyword quality — feed abbreviations, product names, and common suffixes.
- A "found but protected" bucket confirms the org uses that cloud even when you cannot read it — useful signal on its own.

## Overlaps ("do both")
- Pairs with `[[initstring-linkedin2username]]` (people side of the same org) and with subdomain-enumeration tools that map the org's broader infrastructure.

## Trust & verifiability
`trust: community` — established open-source tool; always open/verify a flagged bucket directly rather than trusting the label alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloud-enum |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org, domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
