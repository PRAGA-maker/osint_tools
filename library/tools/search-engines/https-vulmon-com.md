---
id: https-vulmon-com
name: Vulmon
description: Use when you have a `domain`/software or a CVE and want vulnerability intelligence — returns CVE details, affected products and exploit references for infrastructure OSINT.
url: https://vulmon.com/
category: search-engines
path:
- search-engines
bestFor: Searching CVEs by product, version or keyword to assess the exposure of infrastructure tied to a target domain/organisation.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free vulnerability search and CVE details; "Vulmon Recon" e-mail alerts are also free with signup. No paywall for core search.
opsec: passive
opsecNote: Searching Vulmon's CVE database is passive and touches only Vulmon — it does NOT scan the target. Actually probing a subject's host for the vulnerabilities you find is active and intrusive; keep to research unless authorised.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known vulnerability search engine aggregating public CVE/advisory data; the underlying CVE data is authoritative, the aggregation is third-party.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- vulmon.com
tags:
- vulnerabilities
- cve
- infrastructure
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Vulmon

> A vulnerability search engine over public CVE and advisory data — search by product, version or keyword to understand what a piece of infrastructure is exposed to.

## When to use
This is an **infrastructure/security** OSINT tool, not a people-finder. Once you've fingerprinted the software, versions or products behind a target's `domain` or organisation (via other recon), Vulmon tells you which known CVEs apply, how severe they are, and where public exploit/advisory references live — context for assessing an org's exposure or corroborating a security narrative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vulmon.com/.
2. Search by product/version (e.g. `nginx 1.18`), CVE id, or keyword.
3. Read the CVE record: description, CVSS severity, affected products/versions, and links to advisories/exploits.
4. Optionally set up a free **Vulmon Recon** alert to be emailed on new CVEs for products you care about.
5. Pivot: map findings back to the target's fingerprinted stack — but stop at research; scanning/exploiting a live host is a different, authorised activity.

## Inputs → Outputs
- **In:** `domain`-adjacent product/version info, a CVE id, or a keyword
- **Out:** CVE details, affected products, severity, and exploit/advisory references
- **Empty/negative result looks like:** no CVEs for a product/version — it may be patched/obscure, or you've mis-fingerprinted the stack. Absence of a known CVE is not proof of security.

## Gotchas & OpSec
- **Not a people-search tool** — relevance to missing-persons work is indirect (assessing an org's/site's infrastructure).
- Searching is safe; acting on findings against a live target without authorisation is not — keep to passive research.
- CVE data is aggregated from public sources; verify severity/applicability against the vendor advisory.

## Overlaps ("do both")
- Pairs with infrastructure-fingerprinting and CVE databases (NVD, Shodan) — those tell you what's running and exposed, Vulmon explains what that software is vulnerable to.

## Trust & verifiability
`trust: community` — a reputable third-party aggregator of authoritative CVE data. Confirm any specific vulnerability against the official CVE/NVD record and vendor advisory before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | https-vulmon-com |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
