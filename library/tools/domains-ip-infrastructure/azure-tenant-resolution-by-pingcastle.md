---
id: azure-tenant-resolution-by-pingcastle
name: Azure Tenant Resolution by PingCastle
description: Use when you have a `domain` (or Azure tenant ID) and want to map an organisation's Microsoft/Entra tenant — returns the tenant ID and other domains registered to the same tenant.
url: https://tenantresolution.pingcastle.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Resolving a company's email/web domain to its Azure AD (Entra ID) tenant and enumerating sibling domains under that tenant.
selectorsIn:
- domain
selectorsOut:
- domain
- employer-org
status: live
pricing: free
costNote: Free public tool from PingCastle (Netwrix). No account required.
opsec: passive
opsecNote: Domain lookups read Microsoft's public OpenID configuration; ID lookups hit PingCastle's precomputed database built from certificate-transparency logs. The target organisation is not notified. Your query is seen only by PingCastle and Microsoft's public endpoints.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: PingCastle is a well-established Active Directory / Azure security vendor (part of Netwrix); the data derives from Microsoft's own OpenID config and public CT records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- PingCastle Tenant Resolution
- Azure AD tenant lookup
- Entra tenant resolver
tags:
- azure
- entra-id
- tenant-enumeration
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Azure Tenant Resolution by PingCastle

> Turns a domain into its Microsoft cloud identity: which Azure AD / Entra tenant owns it, and what other domains sit under the same tenant.

## When to use
You have a company `domain` (email or web) and want to understand the organisation's Microsoft 365 / Entra ID footprint — its tenant ID and every other domain federated into the same tenant. That sibling-domain list often exposes acquisitions, brand aliases, and internal domains that aren't obvious from the website. This is org/infrastructure mapping; direct missing-persons value is low, but it helps establish which entity truly controls an email domain tied to a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tenantresolution.pingcastle.com.
2. Enter either a `domain` (e.g. `contoso.com`) or a tenant `document-id`/UUID and submit.
3. Read the results:
   - **Domain input** → the tenant ID (pulled live from Microsoft's OpenID configuration) plus the list of domains attached to that tenant.
   - **Tenant-ID input** → domains associated with that tenant, from PingCastle's database (7M+ tenants indexed from certificate-transparency records).
4. Pivot: each sibling `domain` becomes a new investigative lead — feed them to WHOIS, passive DNS, or breach lookups to expand the org's footprint.

## Inputs → Outputs
- **In:** `domain` or Azure tenant ID (UUID)
- **Out:** tenant ID, list of associated `domain`s, implied `employer-org` identity
- **Empty/negative result looks like:** "no tenant found" / no OpenID config — the domain is not backed by an Azure AD/Entra tenant (e.g. it's on Google Workspace or self-hosted mail), so this pivot doesn't apply.

## Gotchas & OpSec
- The sibling-domain list from the ID-based lookup is only as complete as PingCastle's CT-derived database; the live domain lookup is authoritative for the tenant ID but may not list every attached domain.
- A domain resolving to a tenant confirms Microsoft 365 usage — useful for phishing-surface and org-structure inferences, but says nothing about individual users.
- OpSec: passive; no notification reaches the target org.

## Overlaps ("do both")
- Pairs with WHOIS/passive-DNS and breach-lookup tools: use tenant resolution to *enumerate* an org's domains, then run each domain through those tools to enrich. Complements other Azure/Entra recon (e.g. AADInternals-style tooling).

## Trust & verifiability
`trust: trusted` — sourced from Microsoft's public OpenID configuration and certificate-transparency logs and served by a reputable AD-security vendor; the tenant ID is authoritative, the sibling-domain list is best-effort.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | azure-tenant-resolution-by-pingcastle |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
