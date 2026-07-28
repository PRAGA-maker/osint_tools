---
id: two-factor-authentication-list
name: 2FA Directory (twofactorauth)
description: Use when you want to know whether a given service supports two-factor authentication and which methods — for hardening your own accounts or reasoning about a subject's account security.
url: https://2fa.directory/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Checking which sites support 2FA and what methods (TOTP, SMS, hardware key) they offer.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source community directory (formerly twofactorauth.org, now 2fa.directory). No account.
opsec: passive
opsecNote: Passive read of a public directory; you look up a service, not a person, so nothing about a subject is disclosed. Its main value is defensive — hardening the accounts you investigate from.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained open-source directory (GitHub); entries are crowd-updated and can lag a site's current options — verify on the service itself for decisions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- twofactorauth.org
- 2fa.directory
tags:
- 2fa
- account-security
- opsec
- curated-directory
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# 2FA Directory (twofactorauth)

> A crowd-maintained directory of which online services support two-factor authentication and by what method — the reference for locking down accounts, yours or reasoning about a subject's.

## When to use
Primarily OpSec: you're setting up sock-puppet or work accounts and want to know which services offer strong 2FA (TOTP/hardware key) versus weak/none, so you harden the identities you investigate from. Secondarily, it helps you reason about a subject's likely account security — whether a given service they use even offers 2FA, which informs how exposed their account is. It describes services' security features; it doesn't look up people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://2fa.directory/ and search the service/`domain`.
2. Read whether it supports 2FA and which methods (software TOTP, SMS, phone call, hardware/U2F, email).
3. For your own accounts, prefer services offering TOTP or hardware keys; enable them.
4. Confirm on the actual service before relying on an entry (crowd data can lag).
5. Pivot: use it to prioritise which of your investigative accounts to harden first.

## Inputs → Outputs
- **In:** a service name / `domain`
- **Out:** that service's 2FA support and supported methods (no person-level `selectorsOut`)
- **Empty/negative result looks like:** a service not listed, or "no" for 2FA — coverage is broad but not total, and entries can be outdated; check the service directly.

## Gotchas & OpSec
- OpSec: passive; you query the directory, not a target.
- Crowd-sourced and occasionally stale — verify on the live service before making a security decision.
- It reports *availability* of 2FA, not whether a specific account has it enabled.

## Overlaps ("do both")
- Complements the broader hardening resources in `opsec-investigator-tooling` — this answers "does this service even support strong 2FA," which feeds your account-setup and OpSec checklist.

## Trust & verifiability
`trust: community` — an open-source, crowd-maintained directory; useful and generally accurate, but confirm current 2FA options on the service itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | two-factor-authentication-list |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
