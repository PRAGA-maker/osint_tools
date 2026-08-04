---
id: trickest-inventory
name: Trickest Inventory
description: Use when you have a company/`employer-org` running a bug-bounty program and want its known public asset surface — returns enumerated `domain`s and hosts from a maintained inventory.
url: https://github.com/trickest/inventory
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pulling the continuously-updated public asset (domain/host) inventory for 800+ bug-bounty programs.
selectorsIn:
- employer-org
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open data hosted on GitHub (results committed to the repo); no account. The commercial Trickest platform is separate and paid.
opsec: passive
opsecNote: You are reading pre-computed results already committed to a public GitHub repo, so no enumeration touches any target when you browse — fully passive. (The upstream scanning that produced the data was active, but that is Trickest's traffic, not yours.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Trickest, a known security-automation vendor; data is machine-generated from public bug-bounty scopes and refreshed automatically, so freshness is good but entries should be confirmed live.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mkpath
- mksub
aliases:
- trickest/inventory
tags:
- domains-ip-infrastructure
- recon
- bug-bounty
- asset-inventory
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Trickest Inventory

> A public, auto-refreshed GitHub repo of the enumerated asset surface for 800+ bug-bounty programs — recon results you can read without running a scan.

## When to use
You're investigating an organization (`employer-org`) that runs a public bug-bounty program and want its known internet-facing asset surface — apex domains and discovered subdomains — without doing your own enumeration. Trickest continuously enumerates in-scope assets for hundreds of programs and commits the results to this repo. It's a fast way to see an org's public footprint, spot naming conventions, and seed deeper infrastructure work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/trickest/inventory.
2. Navigate to the folder for the target organization/program (repo is organized per program).
3. Open the results files to read the enumerated `domain`s/subdomains for that org.
4. Note scope, naming patterns, and interesting hosts (staging, admin, vpn, dev) as leads.
5. Pivot: feed selected `domain`s into live recon — `[[domainrecon]]`, `[[wappalyzer]]`, reverse-IP (`[[tcp-ip-utils-domain-neighbors]]`) — and confirm which hosts are currently live before acting.

## Inputs → Outputs
- **In:** `employer-org` / program name (or a `domain` to look up within a program)
- **Out:** enumerated `domain`s / subdomains for that program's public scope
- **Empty/negative result looks like:** the organization isn't among the covered programs (no folder), or a listed host has since gone offline. Coverage is bug-bounty programs only — most companies won't be present.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you read committed results; you generate no scanning traffic against the target.
- Scope and staleness: it only covers organizations with public bug-bounty programs, and the committed lists are snapshots — always re-verify a host is live and still in scope (and stay within authorized/legal bounds) before probing it.

## Overlaps ("do both")
- Complements live recon tools — Trickest Inventory hands you a ready subdomain list to skip cold enumeration; pair with `[[domainrecon]]` and reverse-IP to validate and expand what's still active.

## Trust & verifiability
`trust: community` — vendor-maintained, machine-generated data from public program scopes. Entries are checkable (resolve the domains yourself), but treat the lists as recon leads to confirm, not a guaranteed-current source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trickest-inventory |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org, domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
