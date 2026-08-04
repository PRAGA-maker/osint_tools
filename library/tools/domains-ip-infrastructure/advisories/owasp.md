---
id: owasp
name: OWASP
description: Use when you need authoritative application-security reference material (Top 10, ASVS, cheat sheets) to understand a vulnerability or harden your own tooling — returns guidance, not lookups.
url: https://www.owasp.org/index.php/Main_Page
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- advisories
bestFor: The reference standard for web-application security risks and defensive guidance (Top 10, ASVS, Cheat Sheet Series).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open; a volunteer non-profit foundation. No account. The old wiki URL now redirects to the modern owasp.org site.
opsec: passive
opsecNote: Passive reference reading; you consult guidance, not a target. No subject data is involved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the OWASP Foundation, the widely-recognised community standard body for application security; authoritative for its own guidance.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Open Worldwide Application Security Project
- owasp.org
tags:
- advisories
- appsec
- reference
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# OWASP

> The community standard for application-security knowledge — reference guidance (Top 10, ASVS, Cheat Sheets), not an investigative lookup.

## When to use
You are assessing a web vulnerability, hardening your own investigative infrastructure, or need to explain a class of web-app risk with an authoritative citation. It supplies definitions, checklists, and defensive guidance; it does not return data about a domain, IP, or person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://owasp.org/ (the legacy `www.owasp.org/index.php/Main_Page` wiki URL redirects there).
2. Pick the resource: **Top Ten** for the headline risks, **ASVS** for a verification standard, **Cheat Sheet Series** for concrete how-to guidance, or **Projects** for community tools.
3. Read the relevant page and cite the specific project/version.
4. Use it as the backing reference when documenting a web-security finding in a report.

## Inputs → Outputs
- **In:** a security topic/risk (not a personal selector)
- **Out:** standards, checklists, and defensive guidance
- **Empty/negative result looks like:** a niche topic not covered by a flagship project — check OWASP's project list or community chapters.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive reference use only.
- Content is versioned/volunteer-authored — cite the specific project and edition rather than "OWASP says".

## Overlaps ("do both")
- Complements CVE/advisory databases: OWASP explains the *class* of weakness and how to test/defend it, advisory feeds track *specific* vulnerabilities in products.

## Trust & verifiability
`trust: trusted` — the recognised community standards body for application security; authoritative for its own published guidance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | owasp |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
