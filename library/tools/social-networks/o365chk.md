---
id: o365chk
name: o365chk
description: Use when you have a `domain` and want to know if it uses Microsoft 365 — returns the tenant's federation/auth details, associated domains, and validity of specific email addresses.
url: https://github.com/nixintel/o365chk
category: social-networks
path:
- social-networks
bestFor: Checking whether a domain runs Microsoft 365 and enumerating its tenant details and sibling domains.
selectorsIn:
- domain
- email
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free, open-source Python script. Queries Microsoft's public auth endpoints; no account or key.
opsec: active
opsecNote: Queries Microsoft's login/autodiscover endpoints about the target domain/tenant. These are unauthenticated public endpoints (not a login attempt), but you are touching Microsoft infrastructure regarding the target — run from a clean IP. Email-validity checks (GetCredentialType) query whether specific addresses exist; keep volume low to avoid tripping tenant defenses.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Written by nixintel, a respected OSINT practitioner; it wraps Microsoft's own public tenant endpoints, so results are as reliable as those endpoints.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- account-live-com
- o365-attack-toolkit
aliases:
- nixintel/o365chk
tags:
- office365
- microsoft
- tenant-enumeration
- python
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# o365chk

> A small Python tool that asks Microsoft's public endpoints whether a domain runs Microsoft 365, and pulls the tenant's federation, sign-in, and associated-domain details.

## When to use
You're investigating an organization by its `domain` and want to know its email/identity infrastructure: does it use Microsoft 365, is authentication federated (to ADFS/another IdP), and what other domains belong to the same tenant? Tenant metadata reveals corporate structure (sibling brands/domains under one tenant), confirms the email provider before crafting an email-format guess, and — via the credential-type check — can validate whether specific addresses exist.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/nixintel/o365chk` and install its Python dependencies.
2. Run it against the target `domain`; it queries Microsoft's `getuserrealm`/autodiscover endpoints for tenant and federation info.
3. Read the output: whether the domain is Managed (native M365) or Federated (and to which IdP), the tenant's associated domains, and MX/auth hints.
4. Optionally check specific email addresses' validity against the tenant (GetCredentialType) — do this sparingly.
5. Pivot: associated domains → WHOIS/infrastructure mapping; confirmed M365 + email format → `[[account-live-com]]` and email-OSINT; federation to a niche IdP can itself identify the org.

## Inputs → Outputs
- **In:** `domain` (optionally specific `email` addresses to validate)
- **Out:** `domain` (tenant-associated domains), `email` existence/validity, federation & sign-in details
- **Empty/negative result looks like:** "not a Microsoft 365 domain" / no tenant — the org uses Google Workspace or self-hosted mail; not an error, just a different provider. Redirect to the appropriate provider's checks.

## Gotchas & OpSec
- Only meaningful for M365 tenants; a null result just means the domain isn't on Microsoft 365.
- OpSec: **active** toward Microsoft's endpoints (though unauthenticated). Email-validity enumeration at volume can trip tenant protections/logging — keep it minimal and use a clean IP.
- Tool depends on Microsoft's endpoint behaviour, which Microsoft occasionally changes; verify against a second method if results look off.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (existence oracle for individual Microsoft accounts) — o365chk profiles the org's tenant, while account.live.com checks a specific person's Microsoft account; use both when investigating an org and its people.

## Trust & verifiability
`trust: community` — built by a well-known OSINT author on top of Microsoft's own public endpoints, so results are reliable to the extent those endpoints are; cross-check tenant claims if a decision hinges on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | o365chk |
| category | social-networks |
| selectorsIn → selectorsOut | domain, email → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
