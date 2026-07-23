---
id: cloudbrute
name: CloudBrute
description: Use when you have a company `name`/`domain` and want to discover its cloud assets (buckets, apps) across providers — returns exposed storage and app URLs.
url: https://github.com/0xsha/CloudBrute
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Black-box enumeration of a target's cloud storage/apps across AWS, GCP, Azure, DO, Alibaba, Vultr, Linode.
selectorsIn:
- domain
- employer-org
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free and open source (Go). No cloud credentials needed. Last release 2020 — functional but unmaintained; provider endpoints/behaviour may have drifted.
opsec: active
opsecNote: CloudBrute actively probes cloud-provider endpoints with generated names, and successful hits are real requests to the target's cloud assets that those providers (and the asset owner's access logs) can record. It supports proxy and user-agent randomisation for a reason — route through a burner proxy/VPS and only enumerate assets you're authorised to assess.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular (1k+ stars) open-source recon tool, but unmaintained since 2020; wordlist quality drives results and provider changes may cause misses/false negatives. Verify each hit is live and belongs to the target.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- 0xsha/CloudBrute
tags:
- Domain/IP/Links
- Subdomains scan/brute
- cloud-enumeration
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# CloudBrute

> A Go CLI that hunts a target's cloud footprint — storage buckets and apps across seven major providers — using keyword/wordlist permutations, unauthenticated (black-box).

## When to use
You're mapping an organisation's external attack surface and want the cloud assets that DNS enumeration misses: S3/GCS/Azure blob buckets, cloud-hosted apps, and exposed files tied to a company `name`/`domain`. Give it the org keyword and a wordlist; it generates candidate asset names and probes each provider for ones that exist.

## How to use it (`bestInteractionPattern`: cli)
1. Install from the repo (Go binary), and prepare/select a wordlist of likely asset-name fragments.
2. Run with the target `domain`/keyword, wordlist, thread count, timeout, and (recommended) proxy + random-UA options.
3. Choose mode — storage enumeration vs app enumeration — across the supported providers (AWS, GCP, Azure, DigitalOcean, Alibaba, Vultr, Linode).
4. Review hits: for each existing asset, verify it's live and actually belongs to the target (public buckets from unrelated orgs are common false positives).
5. Pivot: an exposed/listable bucket feeds a manual content review; discovered app hosts feed subdomain/infra mapping.

## Inputs → Outputs
- **In:** a company `name`/keyword or `domain` (+ wordlist)
- **Out:** existing cloud storage buckets and app URLs (`domain`) on the probed providers
- **Empty/negative result looks like:** no assets found — a weak wordlist, aggressive provider rate-limiting, or the target simply has no discoverable public assets. Try a richer wordlist before concluding.

## Gotchas & OpSec
- **Active** enumeration: hits are real requests to the target's cloud assets and can be logged; only run against scopes you're authorised to test, via a burner proxy/VPS.
- Results are wordlist-bound — thoroughness scales with the list; a thin list finds little.
- Unmaintained since 2020: provider changes can cause false negatives; corroborate with a maintained tool.

## Overlaps ("do both")
- Complements passive subdomain finders (`[[subdomain-finder]]`) and app-asset extractors (`[[bevigil-cli]]`) — those find hosts passively; CloudBrute actively guesses cloud-specific assets they won't surface.

## Trust & verifiability
`trust: community` — a well-known but dormant recon tool. Reliable at *probing* provider endpoints; every "found" asset needs manual confirmation that it's live and target-owned before it means anything.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudbrute |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, employer-org → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
