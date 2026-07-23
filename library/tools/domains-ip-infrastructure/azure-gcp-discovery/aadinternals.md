---
id: aadinternals
name: AADInternals
description: Use when a target uses Microsoft 365 / Entra ID (Azure AD) and you want tenant reconnaissance — returns tenant details, domains, and user/login-existence signals.
url: https://github.com/Gerenios/AADInternals
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Azure AD / M365 tenant enumeration (tenant ID, domains, user existence) from a domain or email.
selectorsIn:
- domain
- email
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open-source (MIT) PowerShell module; `Install-Module AADInternals`. Docs at aadinternals.com.
opsec: active
opsecNote: Some functions are PASSIVE (unauthenticated tenant recon via public Microsoft endpoints — tenant ID, domains). Others (user-existence probing, login attempts) are ACTIVE and can be logged by the target tenant and may trigger alerts. Only use against tenants you are authorised to assess; prefer the passive recon cmdlets for OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Well-known, actively-maintained toolkit by Dr. Nestori Syynimaa (Gerenios); widely used in Azure AD security research and red-teaming.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- AADInternals
- Azure AD Internals
tags:
- domains-ip-infrastructure
- azure-ad
- m365
- recon
- powershell
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# AADInternals

> A PowerShell toolkit for Azure AD / Microsoft 365 internals — including unauthenticated tenant reconnaissance from just a domain or email.

## When to use
Your target organisation uses Microsoft 365 / Entra ID and you want to map their tenant: confirm they use Azure AD, get the tenant ID and registered `domain`s, check whether a given `email`/user exists, and understand federation/authentication setup. The passive recon cmdlets need no credentials and are a strong footprinting step for M365-hosted orgs.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `Install-Module AADInternals` (PowerShell); import the module.
2. Passive recon: `Invoke-AADIntReconAsOutsider -DomainName example.com` returns tenant ID, tenant name, verified domains, and MX/SPF/DMARC/desktop-SSO signals.
3. User existence: `Invoke-AADIntUserEnumerationAsOutsider` checks whether specific `email`s are valid tenant users (ACTIVE — use only when authorised).
4. Pivot: verified `domain`s expand your target surface; confirmed users feed phishing-surface analysis (in authorised engagements) and org mapping.

## Inputs → Outputs
- **In:** `domain` or `email` of the target org
- **Out:** tenant ID/name, verified `domain`s, authentication config, and user-existence (`email`) signals
- **Empty/negative result looks like:** "not a managed tenant" — the domain isn't backed by Azure AD (they use another provider), so outsider recon returns nothing.

## Gotchas & OpSec
- Split behaviour: outsider *recon* is passive; user-*enumeration*/login functions are active and logged — get authorisation for those.
- User-existence probing can trip tenant alerting/lockouts; go carefully and scoped.
- It's Microsoft-cloud-specific — useless for orgs not on Azure AD/M365.

## Overlaps ("do both")
- Pairs with DNS/cert recon (`[[dnsrecon]]`, `[[google-s-certificate-transparency]]`) — those map hosts/subdomains; AADInternals maps the identity/tenant layer for M365 orgs.

## Trust & verifiability
`trust: trusted` — a mature, well-known, actively-maintained research toolkit; its outsider-recon output comes straight from Microsoft's own endpoints, so tenant facts are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aadinternals |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, email → domain, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
