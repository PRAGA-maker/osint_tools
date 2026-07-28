---
id: nvd-nist
name: NVD (NIST National Vulnerability Database)
description: Use when you have a software product, version, or CVE ID and want authoritative vulnerability details and severity — returns CVE records, CVSS scores, and affected-product data.
url: https://nvd.nist.gov/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- advisories
bestFor: Authoritative lookup of CVEs, CVSS severity, and affected software versions for a product.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free US-government resource; open data plus a free public API (rate-limited without a free key).
opsec: passive
opsecNote: Fully passive — you query NIST's public database about software/CVEs, not any target system. No login for browsing; an optional free API key raises rate limits.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The US government's authoritative vulnerability database (NIST); the reference source for CVE enrichment and CVSS scoring.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- NVD
- nvd.nist.gov
- National Vulnerability Database
tags:
- domain-and-ip-research
- advisories
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# NVD (NIST National Vulnerability Database)

> The US government's authoritative catalog of software vulnerabilities — look up any CVE for its full description, CVSS severity, and the exact products/versions affected.

## When to use
During infrastructure/attack-surface work: you've identified the software or version a target runs (from a banner, a `domain`'s tech stack, or a scan) and want to know its known vulnerabilities, how severe they are (CVSS), and whether patches exist. Also the canonical place to resolve a bare CVE ID into full details. It's a technical/security resource with only indirect relevance to person-finding.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nvd.nist.gov/ and use "Search" → "Vulnerabilities (CVE)".
2. Query by CVE ID (e.g. `CVE-2021-44228`), by product/keyword, or by CPE (vendor:product:version).
3. Read each record: description, CVSS v2/v3 base score and vector, affected CPEs (version ranges), and references to advisories/patches.
4. For bulk/automated enrichment, use the free NVD REST API (request a free API key to raise the rate limit).
5. Pivot: affected-version data tells you whether a target's observed software is exploitable; references link to vendor advisories and PoCs.

## Inputs → Outputs
- **In:** `domain` (as a proxy for its software stack), a product/version, or a CVE ID
- **Out:** `document-id` (CVE records with CVSS severity, affected CPEs, advisory links)
- **Empty/negative result looks like:** no CVEs for a product/version means none are catalogued in NVD (not proof the software is secure — new or unreported issues won't appear).

## Gotchas & OpSec
- NVD reflects **published** CVEs; zero-days and unreported issues aren't here, and enrichment can lag disclosure by days.
- Matching relies on correct CPE/version — a vague product string may miss or over-match; verify the affected version ranges carefully.
- Passive and authoritative; no target system is touched.

## Overlaps ("do both")
- Pairs with vendor advisories, CISA KEV (known-exploited list), and exploit databases — NVD gives the authoritative record and score; the others tell you what's actively exploited and how.

## Trust & verifiability
`trust: trusted` — the official NIST vulnerability database; the authoritative source for CVE/CVSS data, suitable to cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nvd-nist |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
