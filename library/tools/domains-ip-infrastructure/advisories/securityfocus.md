---
id: securityfocus
name: SecurityFocus
description: Use when you have a software product/version and want its historical vulnerability advisories and Bugtraq discussion — returns BID vulnerability records and mailing-list posts (no personal selectors).
url: https://www.securityfocus.com/bid
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- advisories
bestFor: Looking up historical vulnerability (BID) records and Bugtraq mailing-list history for a product.
input: Software product / vendor / keyword
output: Vulnerability advisory records (BID) and Bugtraq mailing-list threads
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
opsec: passive
opsecNote: Reading public vulnerability advisories is passive and touches no target. Note that historical scope only — the BID database was frozen for years; do not treat absence of a recent entry as absence of a vulnerability.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The classic SecurityFocus/Bugtraq resource; after years dormant under Symantec/Broadcom/Accenture it was revived under independent community stewardship, but the legacy BID database is essentially frozen and coverage stops in the late 2010s.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Bugtraq
- SecurityFocus BID
tags:
- vulnerability-advisories
- bugtraq
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# SecurityFocus

> The historic home of Bugtraq and the BID vulnerability database — a research archive for older advisories and mailing-list discussion, now community-revived but frozen in coverage.

## When to use
You are profiling the software/infrastructure a target runs (from a `domain`/banner) and want the historical vulnerability record: what BIDs were filed against a product/version, and how the security community discussed them on Bugtraq. It is a background/enrichment source for the technical side of an investigation, not a people-finder. Because the BID database stopped being updated in the late 2010s, use it for legacy context and pair a current CVE source for anything recent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.securityfocus.com/bid and search by vendor, product, or keyword.
2. Open a BID record for the vulnerability class, affected versions, and references.
3. Cross-read the Bugtraq mailing-list threads for exploitation notes and community context.
4. Pivot: a confirmed vulnerable product/version on a target `domain` guides further (authorized) technical assessment; feed CVE IDs into a current advisory database.

## Inputs → Outputs
- **In:** software product / vendor / keyword
- **Out:** BID advisory records and Bugtraq threads — technical intelligence, no personal selectors
- **Empty/negative result looks like:** no BID for your product, or only pre-2019 entries — expected, because the legacy database is frozen; check a live CVE/NVD source before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none; it is public reading.
- OpSec: fully passive.
- Coverage is historical (`status: degraded`) — the site was dormant for years and revived under new stewardship; treat it as an archive, not a current feed, and corroborate with NVD/CVE for anything modern.

## Overlaps ("do both")
- Pairs with a current CVE/NVD or exploit database — SecurityFocus gives the historical Bugtraq context and older BIDs; a live advisory source covers everything after the freeze.

## Trust & verifiability
`trust: community` — a storied, now community-stewarded resource; the legacy records are genuine but dated, so always confirm a vulnerability's current status against an authoritative, maintained source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | securityfocus |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
