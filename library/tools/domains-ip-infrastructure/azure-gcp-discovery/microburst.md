---
id: microburst
name: MicroBurst
description: Use when you have an `employer-org`/`domain` and want to enumerate its public Azure footprint (storage accounts, subdomains, services) or audit a tenant you have credentials for — returns discovered Azure `domain`s and service endpoints.
url: https://github.com/NetSPI/MicroBurst
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Enumerating an organization's public Azure resources (blob storage, subdomains, services) and testing tenant exposure.
selectorsIn:
- employer-org
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (PowerShell) from NetSPI; no account. Some modules run anonymously; others need Azure credentials you already hold.
opsec: active
opsecNote: Anonymous enumeration (guessing storage-account/subdomain names) sends requests to Microsoft's Azure endpoints, not the org directly, but generates traffic patterns Microsoft can see; authenticated modules act inside a tenant you have rights to. Never run authenticated checks against a tenant you are not authorized to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by NetSPI, a reputable security firm; widely used in Azure penetration testing and auditable as open-source PowerShell.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- scoutsuite
aliases:
- NetSPI MicroBurst
tags:
- azure
- cloud-recon
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# MicroBurst

> A PowerShell toolkit for Azure recon and exposure testing — from anonymously guessing an org's public storage/subdomains to auditing a tenant you have credentials for.

## When to use
You're profiling an organization's cloud footprint. Given an `employer-org` name or `domain`, MicroBurst's anonymous modules brute-guess Azure resource names (blob storage accounts, `*.azurewebsites.net` apps, subdomains) that follow the org's naming conventions, surfacing publicly-exposed or misconfigured resources. Given credentials to a tenant you're authorized to assess, its authenticated modules dump subscriptions, services and secrets for a posture review.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and import the module in PowerShell: `Import-Module ./MicroBurst.psm1`.
2. Anonymous recon: run e.g. `Invoke-EnumerateAzureBlobs -Base <orgname>` or the subdomain/service enumeration modules with the org's naming stub.
3. Authenticated audit (only on tenants you're allowed to test): connect with `Connect-AzAccount`, then run the `Get-Az*` dump/enumeration functions.
4. Read the output — discovered storage containers, service `domain`s/endpoints, and (authenticated) subscription/secret findings.
5. Pivot: exposed blob containers feed data review; discovered service subdomains feed further web recon.

## Inputs → Outputs
- **In:** `employer-org` naming stub / `domain` (anonymous), or tenant credentials (authenticated)
- **Out:** discovered Azure storage/service `domain`s and endpoints; authenticated resource/secret inventory
- **Empty/negative result looks like:** no resources resolve for the guessed names — the org may not use Azure, uses non-obvious naming, or has nothing public. Absence isn't proof of no cloud presence.

## Gotchas & OpSec
- Anonymous name-guessing is noisy and hits Microsoft endpoints; authenticated modules must ONLY be run against tenants you have explicit authorization to test — this is the line between recon and unauthorized access.
- PowerShell/Az module dependencies; some functions track Azure API changes and may lag.
- OpSec: active — generates request traffic Microsoft logs; proxy anonymous enumeration and stay strictly in-scope for authenticated work.

## Overlaps ("do both")
- Pairs with `[[scoutsuite]]` — MicroBurst is Azure-focused enumeration/exposure testing, while ScoutSuite gives a broader multi-cloud configuration audit of accounts you control.

## Trust & verifiability
`trust: community` — open-source and maintained by NetSPI, a well-known security consultancy; the code is auditable and the tool is a standard part of Azure security assessments.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | microburst |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org, domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
