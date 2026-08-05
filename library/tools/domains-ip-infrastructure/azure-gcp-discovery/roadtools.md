---
id: roadtools
name: ROADtools
description: Use when you have credentials/tokens for an Azure AD (Entra) tenant and want to dump and map its users, groups, apps, and privilege relationships — returns an offline graph of `employer-org` identities and their roles.
url: https://github.com/dirkjanm/roadtools
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Enumerating an Azure AD / Entra tenant's objects and privilege relationships into a queryable offline database.
selectorsIn:
- domain
- employer-org
selectorsOut:
- employer-org
- email
- associate
status: live
pricing: free
costNote: Open source under the MIT licence; installable via pip, no cost.
opsec: active
opsecNote: ROADrecon authenticates to Microsoft Graph / Azure AD and pulls the directory — the queries hit Microsoft's tenant endpoints and are logged in the tenant's sign-in and audit logs. Only run against a tenant you are authorised to assess; treat it as a loud, attributable action.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: trusted
trustNote: Written and maintained by Dirk-jan Mollema (dirkjanm), a widely respected Azure AD security researcher; standard tooling in offensive and defensive Entra assessments.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- roadrecon
- roadtx
- ROADlib
tags:
- azure-ad
- entra
- cloud-recon
- enumeration
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# ROADtools

> A framework for interrogating Azure AD (Entra): given valid tenant credentials it dumps the whole directory into a local database and renders the users, groups, apps, and privilege paths as a queryable, offline graph.

## When to use
You have legitimate, authorised access — credentials, a token, or a device context — to an Azure AD / Entra tenant (typically an organisation you are assessing) and need to understand who is in it and how privilege flows. ROADrecon pulls the directory into a local SQLite/SQLAlchemy database and an Angular UI so you can explore users, group memberships, application registrations, and role assignments offline. This is org-infrastructure enumeration, not person-finding.

## How to use it (`bestInteractionPattern`: cli)
1. Install with `pip install roadrecon` (Python 3.10+); `roadtx` and the `ROADlib` library ship alongside for token exchange.
2. Authenticate to the target tenant: `roadrecon auth` (username/password, token, or device-code flow) — this requires valid, authorised credentials.
3. Dump the directory: `roadrecon dump` — pulls Azure AD graph data asynchronously into `roadrecon.db`.
4. Explore: `roadrecon gui` opens the Angular interface for offline analysis; run plugins to output users, group graphs, and privilege relationships.
5. Pivot: identified accounts (`email`, display names, `associate` links via group/role membership) feed people- and email-OSINT; app registrations feed infrastructure mapping.

## Inputs → Outputs
- **In:** authorised auth context for a `domain`/`employer-org` tenant (credentials, token, or device context)
- **Out:** an offline graph of users (`email`, names), groups, applications, roles, and who-can-do-what privilege mappings
- **Empty/negative result looks like:** auth fails, or the account has too little privilege to read directory objects (a locked-down tenant), yielding an empty or partial dump — not proof the tenant is empty.

## Gotchas & OpSec
- Human-in-the-loop: you must supply and complete a real tenant login (MFA/device-code prompts included); there is no anonymous mode.
- OpSec: **active and attributable** — every Graph call lands in the tenant's sign-in/audit logs. This is authorised-assessment tooling; never point it at a tenant you do not have written permission to test.
- Scope creep risk: a full dump is large and noisy — collect only what the engagement authorises.

## Overlaps ("do both")
- Pairs with other Azure/Entra discovery tools in this suite (e.g. unauthenticated tenant-reconnaissance utilities) — those map a tenant from the outside; ROADtools enumerates it in depth once you hold credentials.

## Trust & verifiability
`trust: trusted` — authored by Dirk-jan Mollema, a leading Azure AD security researcher, and MIT-licensed with open source you can audit. The directory data it returns is Microsoft's own tenant data, so it is authoritative within the scope you are permitted to read.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | roadtools |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, employer-org → employer-org, email, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
