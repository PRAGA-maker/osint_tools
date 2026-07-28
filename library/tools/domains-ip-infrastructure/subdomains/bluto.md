---
id: bluto
name: Bluto
description: Use when you have a `domain` and want an all-in-one recon pass (DNS records, zone-transfer/brute subdomains, and harvested staff emails) — returns domain, email, name.
url: https://github.com/darryllane/Bluto
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Legacy one-shot DNS recon that also enumerates staff emails from a target domain.
selectorsIn:
- domain
selectorsOut:
- domain
- email
- name
status: degraded
pricing: free
costNote: Free and open-source (MIT). No account. Requires an Email Hunter (hunter.io) API key for the email-enumeration feature.
opsec: active
opsecNote: Bluto runs active lookups — DNS brute-forcing, attempted zone transfers, and third-party queries (NetCraft, Hunter, breach checks) that touch infrastructure related to the target. Run from an attributable-safe host/VPN; DNS brute force is noisy and may appear in the authoritative server's logs.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by darryllane (originally RandomStorm). Last release 2.4.7 in July 2018 and effectively unmaintained; requires Python 2.7 (end-of-life), so treat as legacy.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- domain-dossier
- dnsdumpster
- theharvester
aliases:
- darryllane/Bluto
tags:
- dns-recon
- subdomains
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Bluto

> A legacy all-in-one DNS reconnaissance CLI: from one domain it pulls DNS records, tries a zone transfer, brute-forces subdomains, and scrapes staff emails.

## When to use
You have a `domain` (usually an organisation the subject is tied to) and want a single command that maps its DNS surface and harvests employee `email`/`name` artifacts. In practice, reach for this only if you specifically want Bluto's combined workflow — because it is unmaintained and Python 2.7-only, modern tools below usually do each job better.

## How to use it (`bestInteractionPattern`: cli)
1. Install into a Python 2.7 environment: `pip install bluto` (Python 3 is not supported).
2. (Optional) Obtain a free hunter.io API key to enable email enumeration.
3. Run against the target: `bluto` then supply the domain, or pass switches for subdomain list/timeout.
4. Read the terminal output and the generated HTML evidence report: MX/NS records, discovered subdomains (via NetCraft + brute force + zone transfer), and any harvested emails/staff names.
5. Pivot: subdomains → `[[dnsdumpster]]`/port-scan the live hosts; harvested emails/names → people-search and breach lookups.

## Inputs → Outputs
- **In:** `domain` (+ optional Hunter API key)
- **Out:** `domain` (subdomains), `email` (staff addresses), `name` (staff), plus DNS/MX/NS records
- **Empty/negative result looks like:** no zone transfer allowed (normal), few/no brute-forced subdomains, and no emails when no Hunter key is supplied — none of which means the domain is inactive.

## Gotchas & OpSec
- **Legacy / degraded:** Python 2.7 is end-of-life; expect install friction and stale data sources. This is why `status: degraded`.
- Active recon: DNS brute force and zone-transfer attempts are noisy and can be logged by the target's DNS. Use a VPN/disposable host.
- Email enumeration needs a hunter.io API key; without it you lose the people-facing half of the tool.

## Overlaps ("do both")
- Prefer `[[dnsdumpster]]` for passive DNS/subdomain mapping and `[[theharvester]]` for email/name harvesting — both are maintained and cover Bluto's jobs without Python 2.
- Pairs with `[[domain-dossier]]` for a quick passive WHOIS/DNS baseline before running anything active.

## Trust & verifiability
`trust: community` — open-source but abandoned since 2018 and Python-2-only. Fine as a reference/legacy option; for live investigations use the maintained alternatives above.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bluto |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
